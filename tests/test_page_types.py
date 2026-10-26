"""Page types: brand-review (the default), brand-subpage (one topic of one brand) and top-list (several casinos)."""
import json

import pytest

from textgen import kb as KBM
from textgen import step2, step4, store
from textgen.brief import normalize, validate
from textgen.config import Settings
from textgen.inputs import parse_json, parse_text
from textgen.pipeline import run_all
from textgen.prompts import load_consistency_prompt, load_prompt, load_step1_prompt, load_writer_prompt
from textgen.store import Run
from tests.test_pipeline import FILLER, FakeLLM, page  # noqa: F401

TOP_LIST_INPUT = """GEO - Australia
Page type - top-list
Keywords - best online casinos, new online casinos
Casinos:
- Incaspin | incaspin-kb
- Longfu88 | longfu88-kb
Competitors:
https://a.example/
https://b.example/
https://c.example/
"""


@pytest.fixture
def settings():
    return Settings.load()


def mk(level=2, heading="H", lo=90, hi=110, kws=None, formats=("paragraph",), **extra):
    b = {
        "id": "x", "level": level, "heading": heading, "source": "mandatory", "words_min": lo, "words_max": hi,
        "keywords": kws or {}, "summary": "s", "copywriter_notes": "n", "formats": list(formats),
        "entities": [{"name": "Online Casino", "priority": 10}],
        "entity_connections": [{"subject": "Licence", "relation": "regulates", "object": "Online Casino", "priority": 8}],
    }
    b.update(extra)
    return b


def casino_kb(title, bonus, deposit):
    return {"id": 1, "title": title, "variables": [
        {"key": "brandinfo_welcome", "type": "json", "value": json.dumps({"welcome_bonus": {"total_bonus": bonus}})},
        {"key": "brandinfo_deposit", "type": "json", "value": json.dumps({"minimum": deposit})},
    ]}


# ---------------- input ----------------
def test_top_list_input_is_parsed():
    job = parse_text(TOP_LIST_INPUT)
    assert job.page_type == "top-list" and job.keywords == ["best online casinos", "new online casinos"]
    assert job.casinos == [{"name": "Incaspin", "slug": "incaspin", "knowledge_base": "incaspin-kb"},
                           {"name": "Longfu88", "slug": "longfu88", "knowledge_base": "longfu88-kb"}]
    assert job.competitors == ["https://a.example/", "https://b.example/", "https://c.example/"]
    assert job.brand_name == ""  # no brand: the first keyword must not become one


def test_casino_line_form_and_json_form():
    job = parse_text(TOP_LIST_INPUT.replace("Casinos:\n- Incaspin | incaspin-kb\n- Longfu88 | longfu88-kb",
                                            "Casino - Incaspin | incaspin-kb\nCasino - Long Fu 88 | longfu88-kb"))
    assert [c["slug"] for c in job.casinos] == ["incaspin", "long-fu-88"]
    job = parse_json(json.dumps({"geo": "PL", "page_type": "top-list", "keywords": ["a", "b"], "competitors": ["https://x.pl"],
                                 "casinos": [{"name": "A", "knowledge_base": "a-kb"}, "B | b-kb"]}))
    assert [(c["slug"], c["knowledge_base"]) for c in job.casinos] == [("a", "a-kb"), ("b", "b-kb")]


def test_page_type_input_errors():
    base = "GEO - PL\nKeywords - Longfu88 login, Longfu88\nCompetitors:\nhttps://a.pl/\n"
    with pytest.raises(ValueError, match="needs `Brand"):
        parse_text("Page type - brand-subpage\n" + base)
    job = parse_text("Page type - brand-subpage\nBrand - Longfu88\n" + base)
    assert job.brand_name == "Longfu88" and job.page_type == "brand-subpage"
    with pytest.raises(ValueError, match="Unknown page type"):
        parse_text("Page type - listicle\n" + base)
    with pytest.raises(ValueError, match="at least 2 casinos"):
        parse_text("Page type - top-list\n" + base)
    with pytest.raises(ValueError, match="no knowledge base"):
        parse_text(TOP_LIST_INPUT.replace(" | longfu88-kb", ""))
    with pytest.raises(ValueError, match="belong to a top-list"):
        parse_text(base + "Casino - A | a\n")
    with pytest.raises(ValueError, match="must be different"):
        parse_text(TOP_LIST_INPUT.replace("Longfu88 | longfu88-kb", "incaspin | other"))
    assert parse_text(base).page_type == "brand-review"  # the default stays


# ---------------- knowledge bases of a top list ----------------
def test_casino_knowledge_bases_are_merged_under_their_slugs(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "RUNS_DIR", tmp_path / "runs")
    run = Run.create("t", parse_text(TOP_LIST_INPUT))
    with pytest.raises(RuntimeError, match=r"(?s)00_kb.incaspin\.json.*00_kb.longfu88\.json"):  # all missing files are named at once
        run.knowledge_base()
    run.save_json("00_kb/incaspin.json", casino_kb("incaspin-kb", "Up to €2,750", "€20"))
    run.save_json("00_kb/longfu88.json", casino_kb("wrong", "Up to S$888", "S$30"))
    with pytest.raises(RuntimeError, match='holds "wrong"'):
        run.knowledge_base()
    run.save_json("00_kb/longfu88.json", casino_kb("longfu88-kb", "Up to S$888", "S$30"))
    kb = run.knowledge_base()
    assert list(kb["variables"]) == ["incaspin", "longfu88"]
    assert KBM.resolve(kb, "longfu88.brandinfo_welcome.welcome_bonus.total_bonus") == "Up to S$888"
    assert KBM.variable_of("incaspin.brandinfo_deposit.minimum") == "incaspin"


def test_digest_keeps_paths_and_shortens_values():
    kb = KBM.load(casino_kb("t", "x" * 500, "€20"))
    kb["variables"]["many"] = list(range(30))
    d = KBM.digest(kb["variables"])
    assert d["brandinfo_welcome"]["welcome_bonus"]["total_bonus"].endswith("...") and len(d["brandinfo_welcome"]["welcome_bonus"]["total_bonus"]) < 300
    assert d["many"][:12] == list(range(12)) and d["many"][12].startswith("... 18 more items")
    assert KBM.resolve(kb, "many[25]") == 25  # the full value stays reachable by path


# ---------------- validation ----------------
def sub_kb():
    return KBM.load(casino_kb("sub-kb", "Up to S$888", "S$30"))


def test_brand_review_rules_are_unchanged(settings):
    kb = sub_kb()
    brief = {"blocks": [mk(1, "T", source="h1", kb_refs=["brandinfo_welcome.welcome_bonus.total_bonus"]), mk(2, "Part")]}
    normalize(brief, ["a"], kb)
    errs = validate(brief, {"target_body_words": 200, "keyword_targets": {"a": 0}}, ["a"], settings, kb=kb)
    assert any("no knowledge-base references" in e for e in errs) and any('"brandinfo_deposit" is not used' in e for e in errs)
    assert any(e.startswith("no fact table") for e in errs)


def test_brand_subpage_needs_neither_fact_table_nor_every_variable(settings):
    kb = sub_kb()
    targets = {"target_body_words": 200, "keyword_targets": {"a": 0}}
    brief = {"blocks": [mk(1, "Login", source="h1", kb_refs=["brandinfo_welcome.welcome_bonus.total_bonus"]), mk(2, "Steps")]}
    normalize(brief, ["a"], kb)
    # one of two blocks has brand facts, brandinfo_deposit is unused, there is no fact table: all fine
    assert validate(brief, targets, ["a"], settings, kb=kb, page_type="brand-subpage") == []
    brief = {"blocks": [mk(1, "Login", source="h1"), mk(2, "Steps"), mk(2, "Help", kb_refs=["brandinfo_deposit.minimum"])]}
    normalize(brief, ["a"], kb)
    errs = validate(brief, {"target_body_words": 300, "keyword_targets": {"a": 0}}, ["a"], settings, kb=kb, page_type="brand-subpage")
    assert len(errs) == 1 and "only 1 of 3 blocks refer to the knowledge base" in errs[0]
    brief["blocks"][1]["fact_table"] = [{"key": "licence", "label": "Licence", "kb_refs": ["brandinfo_deposit.minimum"]}]
    normalize(brief, ["a"], kb)
    errs = validate(brief, {"target_body_words": 300, "keyword_targets": {"a": 0}}, ["a"], settings, kb=kb, page_type="brand-subpage")
    assert any("`fact_table` belongs to a brand-review page only" in e for e in errs)


def clusters(*mandatory_ids, optional=()):
    return [{"id": i, "canonical_title": f"Topic {i}", "mandatory": True} for i in mandatory_ids] + \
           [{"id": i, "canonical_title": f"Topic {i}", "mandatory": False} for i in optional]


def test_subpage_may_skip_off_topic_mandatory_clusters_with_a_reason(settings):
    brief = {"blocks": [mk(1, "Login", source="h1", covers_clusters=["c1"]), mk(2, "Steps", covers_clusters=["c2"])]}
    normalize(brief, ["a"])
    targets = {"target_body_words": 200, "keyword_targets": {"a": 0}}
    cl = clusters("c1", "c2", "c3", "c4")
    errs = validate(brief, targets, ["a"], settings, cl, page_type="brand-subpage")
    assert len(errs) == 2 and all("not listed in `skipped_clusters`" in e for e in errs)
    brief["skipped_clusters"] = [{"id": "c3", "reason": "belongs to the payments page"}, {"id": "c4", "reason": "games"}]
    assert validate(brief, targets, ["a"], settings, cl, page_type="brand-subpage") == []
    brief["skipped_clusters"] = [{"id": "c3", "reason": "x"}, {"id": "c4", "reason": "y"}]
    brief["blocks"][1]["covers_clusters"] = []
    errs = validate(brief, targets, ["a"], settings, cl + [], page_type="brand-subpage")
    assert any("at most 2 may be skipped" in e for e in errs)  # 3 of 4 left out
    # a brand-review page still has to cover every mandatory cluster, skipped or not
    brief["blocks"][1]["covers_clusters"] = ["c2"]
    assert any("is not covered by any heading" in e for e in validate(brief, targets, ["a"], settings, cl))


CASINOS = [{"name": "Incaspin", "slug": "incaspin"}, {"name": "Longfu88", "slug": "longfu88"}]
TOP_KB = KBM.merge({"incaspin": KBM.load(casino_kb("incaspin-kb", "Up to €2,750", "€20")),
                    "longfu88": KBM.load(casino_kb("longfu88-kb", "Up to S$888", "S$30"))}, "top-list: Incaspin, Longfu88")
BONUS = [f"{s}.brandinfo_welcome.welcome_bonus.total_bonus" for s in ("incaspin", "longfu88")]


def top_brief(order=("incaspin", "longfu88"), compare_at=1, compare_refs=BONUS, compare_formats=("table",)):
    blocks = [mk(1, "Best online casinos", source="h1")]
    for s in order:
        blocks.append(mk(2, f"{s.title()} review", kb_refs=[f"{s}.brandinfo_welcome.welcome_bonus.total_bonus", f"{s}.brandinfo_deposit.minimum"]))
    blocks.insert(compare_at, mk(2, "Comparison of the casinos", formats=compare_formats, kb_refs=list(compare_refs)))
    brief = {"blocks": blocks}
    normalize(brief, ["a"], TOP_KB)
    return brief


def top_errors(brief, settings):
    t = {"target_body_words": sum(b["words"] for b in brief["blocks"]), "keyword_targets": {"a": 0}}
    return validate(brief, t, ["a"], settings, kb=TOP_KB, page_type="top-list", casinos=CASINOS)


def test_top_list_accepts_comparison_table_and_a_section_per_casino_in_ranking_order(settings):
    assert top_errors(top_brief(), settings) == []
    assert top_errors(top_brief(compare_at=2), settings) == []  # the 2nd or the 3rd block
    assert top_errors(top_brief(compare_at=2), settings) == []
    brief = top_brief()
    assert brief["blocks"][2]["brand_info"][0] == {"path": "incaspin.brandinfo_welcome.welcome_bonus.total_bonus", "value": "Up to €2,750"}


def test_top_list_errors(settings):
    assert any("follow the order of the input" in e for e in top_errors(top_brief(order=("longfu88", "incaspin")), settings))
    errs = top_errors(top_brief(compare_refs=BONUS[:1]), settings)  # the table has the facts of one casino only
    assert any("no comparison table" in e for e in errs)
    assert any("no comparison table" in e for e in top_errors(top_brief(compare_formats=("paragraph",)), settings))
    assert any("no comparison table" in e for e in top_errors(top_brief(compare_at=3), settings))  # too late in the page
    brief = top_brief(order=("incaspin",))
    errs = top_errors(brief, settings)
    assert any('casino "Longfu88" has no section of its own' in e for e in errs)
    brief = top_brief()
    brief["blocks"][3]["kb_refs"][1] = "incaspin.brandinfo_deposit.minimum"  # a section that mixes two casinos
    normalize(brief, ["a"], TOP_KB)
    assert any('casino "Longfu88" has no section of its own' in e for e in top_errors(brief, settings))
    brief = top_brief()
    brief["blocks"][1]["fact_table"] = [{"key": "licence", "label": "Licence", "kb_refs": BONUS[:1]}]
    normalize(brief, ["a"], TOP_KB)
    assert any("`fact_table` belongs to a brand-review page only" in e for e in top_errors(brief, settings))


def test_top_list_needs_no_payments_table_for_a_withdrawal_heading(settings):
    from textgen.brief import validate_visuals

    blocks = [mk(heading="Fast withdrawal casinos", formats=("paragraph",))]
    assert validate_visuals(blocks, "top-list") == []
    assert len(validate_visuals(blocks)) == 1  # a review page still wants the payments table


# ---------------- prompts ----------------
def test_every_page_type_has_its_prompts():
    for pt in ("brand-subpage", "top-list"):
        assert load_step1_prompt("brief", pt) != load_step1_prompt("brief")
        assert load_step1_prompt("review", pt) != load_step1_prompt("review")
        for text in (load_step1_prompt("brief", pt), load_step1_prompt("review", pt)):
            assert "fact_table" in text  # each states the rule for the brand fact sheet
        assert "LANGUAGE RULE" in load_step1_prompt("brief", pt) and "skipped_clusters" in load_step1_prompt("brief", pt)
        writer = load_writer_prompt(pt)
        assert writer.startswith(load_writer_prompt()) and "# PAGE TYPE" in writer  # the addendum comes after the user's own prompt
        assert load_consistency_prompt(pt).startswith(load_consistency_prompt()) and len(load_consistency_prompt(pt)) > len(load_consistency_prompt())
    assert load_step1_prompt("brief") == load_prompt("step1_brief") and load_step1_prompt("review") == load_prompt("step1_review")
    assert load_writer_prompt("brand-review") == load_writer_prompt()
    assert "ONE TOP LIST page" in load_step1_prompt("brief", "top-list") and "ONE FOCUSED PAGE" in load_step1_prompt("brief", "brand-subpage")


# ---------------- writer message ----------------
def test_top_list_context_lists_the_casinos_and_has_no_brand(settings):
    brief = {"brand": "", "geo": "AU", "language": "en", "keywords": ["best online casinos"], "page_type": "top-list",
             "knowledge_base": {"title": "top-list: Incaspin, Longfu88"}, "facts": [],
             "casinos": CASINOS, "blocks": [mk(1, "T", source="h1", kws={"best online casinos": 1})]}
    normalize(brief, ["best online casinos"])
    ctx = step2._context(brief)
    assert "Brand: none" in ctx and "Page type: top list" in ctx
    assert "1. Incaspin (slug `incaspin`)" in ctx and "2. Longfu88 (slug `longfu88`)" in ctx
    brief["blocks"][0]["brand_info"] = [{"path": "incaspin.brandinfo_deposit.minimum", "value": "€20"}]
    msg = step2.build_user_message(brief["blocks"][0], brief, {}, settings)
    assert "- incaspin.brandinfo_deposit.minimum: €20" in msg and "0 (do not use)" not in msg.split("Keywords")[0]
    sub = {**brief, "page_type": "brand-subpage", "brand": "Longfu88"}
    assert "Page type: focused page of the brand about ONE topic" in step2._context(sub) and "Brand: Longfu88" in step2._context(sub)
    assert "Page type" not in step2._context({**brief, "page_type": "brand-review", "brand": "X"})  # review requests are unchanged


# ---------------- variants of a brand-subpage ----------------
def test_subpage_variants_keep_skipped_clusters_and_need_no_fact_table(settings, monkeypatch):
    from textgen import variants as V

    monkeypatch.setattr(V, "INTRINSIC", {})  # the Incaspin defaults would apply to the block ids b02 / b18 / b21
    kb = sub_kb()
    base = {"page_type": "brand-subpage", "skipped_clusters": [{"id": "c3", "reason": "payments page"}], "blocks": [
        {**mk(1, "Login", source="h1", covers_clusters=["c1", "c4"], kb_refs=["brandinfo_welcome.welcome_bonus.total_bonus"]), "id": "b01", "listed_entities": []},
        {**mk(2, "Steps", covers_clusters=["c2"], kb_refs=["brandinfo_deposit.minimum"]), "id": "b02", "listed_entities": []},
    ]}
    spec = {"id": "v01", "name": "n", "intent_summary": "login page", "blocks": [
        {"from": ["b01", "b02"], "level": 1, "heading": "Login Steps", "words": 100, "kw": {"a": 1}}]}
    cl = clusters("c1", "c2", "c3", "c4")
    build_variant, _facts = V.build_variant, V._facts
    brief, targets, errs = build_variant(base, spec, kb, ["a"], settings, cl)
    assert errs == [] and brief["skipped_clusters"] == base["skipped_clusters"] and targets["keyword_targets"] == {"a": 1}
    # a variant that leaves a mandatory cluster out has to say so
    spec["blocks"][0]["from"] = ["b01"]
    _, _, errs = build_variant(base, spec, kb, ["a"], settings, cl)
    assert any("c2" in e and "skipped_clusters" in e for e in errs)
    spec["skipped_clusters"] = base["skipped_clusters"] + [{"id": "c2", "reason": "covered by the intro"}]
    assert build_variant(base, spec, kb, ["a"], settings, cl)[2] == []
    facts = _facts({"v01": {"blocks": brief["blocks"], "targets": {**targets, "base_body_words": 100}}})
    assert facts["v01"]["fact_pos"] == "-" and facts["v01"]["fact_rows"] == 0


def test_a_section_marker_left_in_a_block_is_a_format_problem(settings):
    from textgen.checks import check_block

    b = normalize({"blocks": [mk(1, "T", 5, 20, source="h1")]}, ["a"])["blocks"][0]
    assert not [p for p in check_block(b, "Ten plain words in a row make a fine short body here.", ["a"], "en", settings) if "marker" in p["problem"]]
    marked = check_block(b, "=== b02 === Ten plain words in a row make a fine short body here.", ["a"], "en", settings)
    assert [p["check"] for p in marked if "marker" in p["problem"]] == ["format"]


# ---------------- whole pipeline with a fake model ----------------
class PageTypeLLM(FakeLLM):
    """FakeLLM plus the ТЗ of a top list / a subpage; remembers which prompts reached the model."""

    def __init__(self):
        super().__init__()
        self.systems: dict[str, str] = {}

    def json(self, system, user, schema, model, name="result", max_tokens=0):
        self.systems.setdefault(name, system)
        return super().json(system, user, schema, model, name, max_tokens)

    def text(self, system, user, model, max_tokens=0):
        self.systems.setdefault("text", system)
        return super().text(system, user, model, max_tokens)

    def _brief(self, ctx):
        self.ctx = ctx
        if ctx.get("page_type") == "top-list":
            return self._top_list(ctx)
        brief = super()._brief(ctx)
        brief["blocks"][0]["kb_refs"] = ["brandinfo_welcome.welcome_bonus.total_bonus"]
        brief["blocks"][1]["kb_refs"] = ["brandinfo_deposit.minimum"]
        return brief

    def _top_list(self, ctx):
        total = ctx["targets"]["target_body_words"]
        clusters = {c["canonical_title"].lower(): c for c in ctx["heading_clusters"] if c["mandatory"]}
        extra = {"entities": [{"name": "Online Casino", "priority": 10}], "copywriter_notes": "Stay general.",
                 "entity_connections": [{"subject": "Licence", "relation": "regulates", "object": "Online Casino", "priority": 8}]}
        kw0 = {k: 0 for k in ctx["keywords"]}
        casinos = ctx["casinos_in_ranking_order"]
        per = round((total - 120 - 70 - 100 * len(casinos)) / 2)
        blocks = [{"id": "b01", "level": 1, "heading": "Best online casinos for Australian players", "source": "h1", "words_min": 105, "words_max": 135,
                   "keywords": dict(kw0), "summary": "Intro", "formats": ["paragraph"], "covers_clusters": [], **extra},
                  {"id": "b02", "level": 2, "heading": "Comparison of the casinos", "source": "unique", "words_min": 60, "words_max": 80,
                   "keywords": dict(kw0), "summary": "Table", "formats": ["table"], "covers_clusters": [],
                   "kb_refs": [f"{c['slug']}.brandinfo_welcome.welcome_bonus.total_bonus" for c in casinos], **extra}]
        for c in casinos:
            blocks.append({"id": "x", "level": 2, "heading": f"{c['name']} review", "source": "unique", "words_min": 90, "words_max": 110,
                           "keywords": dict(kw0), "summary": f"The {c['name']} section", "formats": ["paragraph"], "covers_clusters": [],
                           "kb_refs": [f"{c['slug']}.brandinfo_welcome.welcome_bonus.total_bonus", f"{c['slug']}.brandinfo_deposit.minimum"], **extra})
        for title in ("registration", "bonuses"):
            blocks.append({"id": "x", "level": 2, "heading": title.title(), "source": "mandatory", "words_min": int(per * 0.9), "words_max": int(per * 1.1),
                           "keywords": dict(kw0), "summary": f"Cover {title}", "formats": ["paragraph", "list"] if title == "registration" else ["paragraph"],
                           "covers_clusters": [clusters[title]["id"]], **extra})
        spread = [b for b in blocks if b["formats"] != ["table"]]
        for k, need in ctx["targets"]["keyword_targets"].items():
            for j in range(need):
                spread[j % len(spread)]["keywords"][k] += 1
        return {"intent_summary": "top list", "blocks": blocks,
                "skipped_clusters": [{"id": clusters["payments"]["id"], "reason": "belongs to a payments page"}]}


@pytest.fixture
def env(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "RUNS_DIR", tmp_path / "runs")
    monkeypatch.setattr(step4, "OUTPUT_DIR", tmp_path / "output")
    html = tmp_path / "html"
    html.mkdir()
    kw = "Our list of best online casinos is simple. See new online casinos too. VegasHunter login. VegasHunter. Vegas Hunter. VegasHunter casino."
    (html / "a.example.html").write_text(page("A", ["Registration", "Bonuses", "Payments"], kw), encoding="utf-8")
    (html / "b.example.html").write_text(page("B", ["Registration", "Bonuses", "Support"], kw), encoding="utf-8")
    (html / "c.example.html").write_text(page("C", ["Registration", "Bonuses", "Payments"], kw), encoding="utf-8")
    return tmp_path, html


def test_top_list_pipeline(env):
    tmp_path, html = env
    run = Run.create("top", parse_text(TOP_LIST_INPUT))
    run.save_json("00_kb/incaspin.json", casino_kb("incaspin-kb", "Up to €2,750", "€20"))
    run.save_json("00_kb/longfu88.json", casino_kb("longfu88-kb", "Up to S$888", "S$30"))
    llm = PageTypeLLM()
    assert run_all(run, llm, Settings.load(), html_dir=html, words=900)

    assert "ONE TOP LIST page" in llm.systems["brief"] and "TOP LIST OF CASINOS" in llm.systems["text"]
    assert "TOP LIST SEO page" in llm.systems["review"] and "PAGE TYPE: TOP LIST" in llm.systems["consistency"]
    ctx = llm.ctx  # what the ТЗ model received: ranking, shortened facts of both casinos, no fact sheet
    assert ctx["page_type"] == "top-list" and [c["slug"] for c in ctx["casinos_in_ranking_order"]] == ["incaspin", "longfu88"]
    assert set(ctx["knowledge_base"]["variables"]) == {"incaspin", "longfu88"} and "fact_table_requirements" not in ctx

    brief = run.load_json(store.BRIEF)
    assert brief["page_type"] == "top-list" and brief["casinos"] == [{"slug": "incaspin", "name": "Incaspin"}, {"slug": "longfu88", "name": "Longfu88"}]
    assert brief["skipped_clusters"][0]["reason"] == "belongs to a payments page"
    assert "Page type: top-list" in run.load_text(store.BRIEF_MD) and "Left out on purpose" in run.load_text(store.BRIEF_MD)
    assert [b["heading"] for b in brief["blocks"]][:4] == ["Best online casinos for Australian players", "Comparison of the casinos", "Incaspin review", "Longfu88 review"]
    final = run.load_json(store.FINAL_JSON)
    assert final["page_type"] == "top-list" and len(final["blocks"]) == len(brief["blocks"])


def test_step3_shortens_blocks_when_the_whole_text_is_over_its_limit(env):
    from textgen.step1 import run_step1
    from textgen.step2 import run_step2
    from textgen.step3 import run_step3
    from textgen.textutil import count_words

    tmp_path, html = env
    text = ("GEO - Australia\nPage type - brand-subpage\nBrand - VegasHunter\nKnowledge Base - sub-kb\n"
            "Keywords - VegasHunter, Vegas Hunter, VegasHunter casino, VegasHunter login\nCompetitors:\nhttps://a.example/\nhttps://b.example/\nhttps://c.example/\n")
    run = Run.create("limit", parse_text(text))
    run.save_json(store.KNOWLEDGE_BASE, casino_kb("sub-kb", "Up to S$888", "S$30"))
    llm, settings = PageTypeLLM(), Settings.load()
    run_step1(run, llm, settings, html_dir=html)
    run_step2(run, llm, settings)
    brief, state = run.load_json(store.BRIEF), run.load_json(store.BLOCKS)
    assert brief["targets"]["max_body_words"] == round(brief["targets"]["competitor_body_words"] * 1.2)  # written into the ТЗ
    assert "Limit of the whole text" in run.load_text(store.BRIEF_MD)
    big = brief["blocks"][2]
    state["blocks"][big["id"]]["text"] += " extra" * (big["words_max"] + 5)  # this block goes over its own maximum (and over its cap)
    run.save_json(store.BLOCKS, state)
    total = sum(count_words(b["text"]) for b in state["blocks"].values())
    brief["targets"]["max_body_words"] = total - 5
    run.save_json(store.BRIEF, brief)

    passed, fixes = run_step3(run, llm, settings, iteration=0)
    assert not passed and any("limit of the whole text" in f or "over its limit" in f for f in fixes[big["id"]])
    report = run.load_json("03_check_iter_00.json")
    assert report["summary"]["max_body_words"] == total - 5
    assert [p["check"] for p in report["blocks"][big["id"]] if p["check"] == "page_limit"] == ["page_limit"]
    assert not [b for b, probs in report["blocks"].items() if b != big["id"] and any(p["check"] == "page_limit" for p in probs)]  # only the oversized block


def test_brand_subpage_pipeline(env):
    tmp_path, html = env
    text = ("GEO - Australia\nPage type - brand-subpage\nBrand - VegasHunter\nKnowledge Base - sub-kb\n"
            "Keywords - VegasHunter, Vegas Hunter, VegasHunter casino, VegasHunter login\nCompetitors:\nhttps://a.example/\nhttps://b.example/\nhttps://c.example/\n")
    run = Run.create("sub", parse_text(text))
    run.save_json(store.KNOWLEDGE_BASE, casino_kb("sub-kb", "Up to S$888", "S$30"))
    llm = PageTypeLLM()
    assert run_all(run, llm, Settings.load(), html_dir=html)

    assert "ONE FOCUSED PAGE" in llm.systems["brief"] and "FOCUSED BRAND PAGE" in llm.systems["text"]
    assert llm.ctx["page_type"] == "brand-subpage" and llm.ctx["brand"] == "VegasHunter" and "fact_table_requirements" not in llm.ctx
    brief = run.load_json(store.BRIEF)
    assert brief["page_type"] == "brand-subpage" and "casinos" not in brief
    assert not any(b["fact_table"] for b in brief["blocks"])  # no brand fact sheet on a subpage


def test_home_link_note_is_only_for_brand_subpages():
    from textgen.brief import home_link_note

    note = home_link_note({"page_type": "brand-subpage", "brand": "Longfu88"})
    assert '"Longfu88"' in note and "home page" in note
    assert home_link_note({"page_type": "brand-review", "brand": "Longfu88"}) == ""
    assert home_link_note({"page_type": "top-list"}) == ""
