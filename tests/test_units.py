import pytest

from textgen.analysis import mine_entities
from textgen.brief import (block_range, compute_targets, normalize, rebalance_keywords, render_markdown, section_totals,
                           validate, visual_elements)
from textgen.checks import check_block
from textgen.config import Settings
from textgen.inputs import make_slug, parse_json, parse_text
from textgen.lang import check_language
from textgen.textutil import analyze_format, count_keywords, count_words, text_segments

KW = ["VegasHunter", "Vegas Hunter", "VegasHunter casino", "VegasHunter login"]


@pytest.fixture
def settings():
    return Settings.load()


def test_parse_text_user_format():
    job = parse_text(
        "GEO - Australia\nBrand - VegasHunter\nFacts - Licence: example\nKeywrds - VegasHunter, Vegas Hunter, VegasHunter casino\n"
        "Competitors:\nhttps://a.com/au/\nhttps://b.org/\n"
    )
    assert job.geo == "Australia"
    assert job.keywords == ["VegasHunter", "Vegas Hunter", "VegasHunter casino"]
    assert job.competitors == ["https://a.com/au/", "https://b.org/"]
    assert job.brand_name == "VegasHunter" and job.facts == ["Licence: example"]
    assert make_slug(job) == "vegashunter-australia"


def test_brand_defaults_to_first_keyword():
    job = parse_text("GEO - PL\nKeywords - Rockyspin, Rocky Spin\nCompetitors:\nhttps://a.pl/")
    assert job.brand_name == "Rockyspin"


def test_parse_json_and_missing():
    job = parse_json('{"geo":"Germany","keywords":"a, b","competitors":["https://x.de"],"language":"de"}')
    assert job.keywords == ["a", "b"] and job.language == "de"
    with pytest.raises(ValueError):
        parse_json('{"geo":"Germany","keywords":[],"competitors":[]}')


def test_count_keywords_longest_match_first():
    text = "VegasHunter casino is great. Try VegasHunter login or just VegasHunter. Vegas  Hunter too, vegashunter again."
    c = count_keywords(text, KW)
    assert c == {"VegasHunter": 2, "Vegas Hunter": 1, "VegasHunter casino": 1, "VegasHunter login": 1}


def test_count_keywords_whole_words_only():
    assert count_keywords("VegasHunters and MyVegasHunter", ["VegasHunter"]) == {"VegasHunter": 0}
    assert count_keywords("VegasHunter's bonus", ["VegasHunter"]) == {"VegasHunter": 1}


def test_count_words_ignores_markdown():
    text = "**Bold** word\n\n- item one\n- item two\n\n| A | B |\n|---|---|\n| 1,000 | x |\n"
    assert count_words(text) == 2 + 4 + 4  # Bold word / item one item two / A B 1,000 x


def test_analyze_format():
    text = "Intro paragraph.\nstill same paragraph.\n\n- a\n- b\n\n| h1 | h2 |\n|---|---|\n| x | y |\n\nOutro.\n"
    assert analyze_format(text) == {"paragraph": 2, "list": 1, "table": 1, "heading": 0}
    assert analyze_format("## Oops\ntext")["heading"] == 1


def test_text_segments():
    segs = text_segments("Para one.\n\n- item\n\n| a | b |\n|---|---|\n| c | d |")
    assert segs == ["Para one.", "item", "a", "b", "c", "d"]


def test_language_check():
    ok = "The welcome bonus gives new players extra spins and matched deposits on the first three payments."
    ru = "Приветственный бонус даёт новым игрокам дополнительные вращения и повышенный депозит на первые три платежа."
    assert check_language(ok, "en", KW) == []
    bad = check_language(ok + "\n\n" + ru, "en", KW)
    assert len(bad) == 1 and bad[0]["reason"] == "foreign script"
    de = "Der Willkommensbonus bietet neuen Spielern zusätzliche Freispiele und einen Einzahlungsbonus auf die ersten drei Einzahlungen."
    assert check_language(de, "en", KW)[0]["detected"] == "de"


def mk(level=2, heading="H", lo=15, hi=25, kws=None, formats=("paragraph",), **extra):
    b = {
        "id": "x", "level": level, "heading": heading, "source": "mandatory", "words_min": lo, "words_max": hi,
        "keywords": kws or {}, "summary": "s", "copywriter_notes": "n", "formats": list(formats),
        "entities": [{"name": "Online Casino", "priority": 10}],
        "entity_connections": [{"subject": "Licence", "relation": "regulates", "object": "Online Casino", "priority": 8}],
    }
    b.update(extra)
    return b


def test_check_block_ok(settings):
    text = "VegasHunter offers pokies and live tables for Australian players who want a simple lobby and quick deposits."
    n = count_words(text)
    b = normalize({"blocks": [mk(lo=n - 3, hi=n + 3, kws={"VegasHunter": 1})]}, KW)["blocks"][0]
    assert check_block(b, text, KW, "en", settings) == []


def test_check_block_reports_everything(settings):
    text = "- VegasHunter login\n- VegasHunter login\n- VegasHunter login"
    b = normalize({"blocks": [mk(lo=50, hi=70, kws={"VegasHunter login": 1}, formats=("paragraph", "table"))]}, KW)["blocks"][0]
    checks = {p["check"] for p in check_block(b, text, KW, "en", settings)}
    assert checks == {"size", "keywords", "format"}


def test_block_range_is_exactly_the_tz_range(settings):
    b = normalize({"blocks": [mk(lo=60, hi=80)]}, KW)["blocks"][0]
    assert block_range(b) == (60, 80) and b["words"] == 70
    size = lambda n: [p for p in check_block(b, " ".join(["word"] * n), KW, "en", settings) if p["check"] == "size"]  # noqa: E731
    assert not size(60) and not size(80)
    assert size(59)  # too short


def test_block_may_exceed_words_max_by_10_percent(settings):
    b = normalize({"blocks": [mk(lo=60, hi=80)]}, KW)["blocks"][0]
    size = lambda n: [p for p in check_block(b, " ".join(["word"] * n), KW, "en", settings) if p["check"] == "size"]  # noqa: E731
    assert not size(81) and not size(88)  # 80 * 1.1 = 88
    assert size(89) and "88" in size(89)[0]["fix"]


def test_value_words_and_fact_words(settings):
    from textgen.brief import fact_words, value_words

    assert value_words("Up to €2,750") == 3 and value_words(188) == 1 and value_words({"a": ["x y", "z"], "b": "w"}) == 4
    para = {"formats": ["paragraph"]}
    assert fact_words(188, para, settings) == 3 and fact_words("€50", para, settings) == 3  # a short scalar still needs a few words
    assert fact_words("25x the deposit plus bonus amount", para, settings) == 7  # 6 words * 1.2
    long_list = ["one two three four five six seven eight nine ten"] * 5  # 50 words
    assert fact_words(long_list, para, settings) == 30  # the cap of one item in prose
    shown = {"formats": ["paragraph", "table"]}
    assert fact_words(long_list, shown, settings) == 40  # a list or a table: the words of the items, a third more for the cap
    assert fact_words(["a b c d"] * 3, shown, settings) == 12  # factor 1.0 where it is shown
    assert fact_words("one two three four five six", {"formats": ["list"]}, settings) == 6  # no prose around a list


def test_coverage_need_counts_connections_and_facts_but_not_entities(settings):
    from textgen.brief import coverage_need

    b = normalize({"blocks": [mk(brand_info=[], entities=[{"name": f"E{i}", "priority": 5} for i in range(9)])]}, KW)["blocks"][0]
    b["brand_info"] = [{"path": "p", "value": 188}]
    assert coverage_need(b, settings) == {"facts": 3, "connections": 15, "need": 18}  # nine entities add nothing
    b["entity_connections"] = b["entity_connections"] * 3
    assert coverage_need(b, settings)["connections"] == 45


WELCOME_FACTS = ["Casino Welcome Bonus", 188, "€2,088", 18, "€50", "25x the deposit plus bonus amount",
                 ["Register an account and complete the required personal details.", "Make the first qualifying deposit.",
                  "Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.", "Play eligible casino games and complete the wagering before expiry."]]


def _budget_brief(formats=("paragraph",), lo=60, hi=80, info=None, connections=1):
    b = mk(lo=lo, hi=hi, formats=formats, brand_info=[{"path": f"p{i}", "value": v} for i, v in enumerate(info or [])])
    b["entity_connections"] = b["entity_connections"] * connections
    return {"blocks": [dict(b, id="b01", words=(lo + hi) // 2)]}, {"target_body_words": 70}


def _free(settings, **kw):
    import dataclasses

    return dataclasses.replace(settings, **kw)


def test_welcome_block_needs_about_70_words_not_240(settings):
    from textgen.brief import apply_coverage_budget, coverage_need

    brief, targets = _budget_brief(lo=53, hi=67, info=WELCOME_FACTS)  # the b07 block of the Login ТЗ: 7 facts, 1 connection, 4 entities
    b = brief["blocks"][0]
    assert coverage_need(b, settings) == {"facts": 53, "connections": 15, "need": 68}  # 4 + 3 + 3 + 3 + 3 + 7 + 30, and 15
    report = apply_coverage_budget(brief, targets, settings)
    assert (b["words_min"], b["words_max"]) == (60, 76) and report[0]["from"] == [53, 67] and report[0]["need"] == 68
    assert b["words_base"] == [53, 67] and b["coverage_words"]["need"] == 68
    assert targets["base_body_words"] == 70 and targets["target_body_words"] == 68


def test_coverage_budget_growth_is_capped_at_20_percent_of_the_competitor_range(settings):
    from textgen.brief import apply_coverage_budget, plan_budget

    brief, targets = _budget_brief(info=["word " * 29] * 6)  # six long facts: 30 words each, 180 words
    row = plan_budget(brief, settings)[0]
    assert row["need"] == 195 and row["ceiling"] == 84 and row["overloaded"]  # the block cannot hold them
    apply_coverage_budget(brief, targets, settings)
    b = brief["blocks"][0]
    assert (b["words_min"], b["words_max"]) == (72, 96)  # 60 * 1.2 and 80 * 1.2
    assert b["words"] == 84


def test_coverage_budget_pure_formula_without_a_growth_cap(settings):
    from textgen.brief import apply_coverage_budget

    brief, targets = _budget_brief(info=["a b c d e f g h i j k l"] * 4, connections=2)  # 4 facts of 12 words -> 14 words each, 2 connections
    apply_coverage_budget(brief, targets, _free(settings, max_growth=10))
    b = brief["blocks"][0]
    assert b["words"] == 86 and (b["words_min"], b["words_max"]) == (76, 96)  # need 56 + 30 = 86, +-12%


def test_normalize_keeps_only_real_listed_entities():
    b = normalize({"blocks": [mk(listed_entities=["Online Casino", "Nope", "Online Casino"])]}, KW)["blocks"][0]
    assert b["listed_entities"] == ["Online Casino"]


def test_coverage_budget_never_shrinks_and_skips_tables(settings):
    from textgen.brief import apply_coverage_budget

    brief, targets = _budget_brief(lo=300, hi=340, info=["a"])  # base 320 words > what one fact and one connection need
    assert apply_coverage_budget(brief, targets, settings) == [] and brief["blocks"][0]["words_max"] == 340
    brief, targets = _budget_brief(formats=("table",), info=["a b c d e f g h"] * 9)
    assert apply_coverage_budget(brief, targets, settings) == [] and brief["blocks"][0]["words_max"] == 80


def test_a_list_states_its_facts_in_fewer_words_than_prose(settings):
    from textgen.brief import plan_budget

    facts = ["alpha beta gamma delta epsilon zeta eta theta"] * 5  # 8 words each
    prose = plan_budget(*[_budget_brief(info=facts)[0], settings])[0]
    listed = plan_budget(*[_budget_brief(formats=("list",), info=facts)[0], settings])[0]
    assert prose["facts"] == 50 and listed["facts"] == 40  # 10 words per fact in prose, 8 in a list


def test_validate_checks_overload_and_the_limit_of_the_whole_text(settings):
    kws = ["a"]
    targets = {"target_body_words": 140, "competitor_body_words": 120, "max_body_words": 144, "tier": "medium", "keyword_targets": {"a": 0}}
    brief = {"blocks": [mk(1, "T", 60, 80, source="h1"), mk(2, "Part", 60, 80)]}
    normalize(brief, kws)
    errs = validate(brief, targets, kws, settings)
    assert len(errs) == 1 and "up to 160 words" in errs[0] and "limit is 144" in errs[0] and 'size group "medium": competitor mean 120 x 1.2' in errs[0]
    targets["max_body_words"] = 160
    assert validate(brief, targets, kws, settings) == []
    brief["blocks"][1]["brand_info"] = [{"path": "p", "value": "word " * 29}] * 6  # six long facts do not fit into a 60-80 word block
    errs = validate(brief, targets, kws, settings)
    assert any(e.startswith("b02") and "need about 195 words" in e and "84 at most" in e for e in errs)
    del targets["max_body_words"]  # a ТЗ without a limit (older runs) is not checked against it
    assert not any("limit" in e for e in validate(brief, targets, kws, settings))


def test_count_keywords_inflected_forms():
    kws = ["Incaspin", "Incaspin casino"]
    text = "Incaspin Casinos und das Incaspin. Incaspinie wird genannt, Incaspinxyzw nicht."
    assert count_keywords(text, kws) == {"Incaspin": 2, "Incaspin casino": 0}  # "Incaspin Casinos" is only the brand plus a word
    assert count_keywords(text, kws, inflect=True) == {"Incaspin": 2, "Incaspin casino": 1}  # + "Incaspinie"; "Casinos" joins the longer keyword


def test_brand_name_is_free_where_the_limit_is_zero_up_to_one_per_50_words(settings):
    kws = ["Incaspin", "Incaspin casino", "login"]
    b = normalize({"blocks": [mk(lo=10, hi=400, kws={"Incaspin casino": 1})]}, kws)["blocks"][0]
    filler = " ".join(["slots"] * 90)

    def kw_problems(text, **kw):
        return [p for p in check_block(b, text, kws, "en", settings, **kw) if p["check"] == "keywords"]

    ok = f"Incaspin casino lists games. Incaspin has slots. {filler} It has tables."  # ~100 words, 1 free use of the brand
    assert kw_problems(ok, brand="Incaspin") == []
    two = ok.replace("It has tables", "Incaspin has tables")  # 2 free uses in ~100 words: still within one per 50 words
    assert kw_problems(two, brand="Incaspin") == []
    three = two + " Incaspin again."  # 3 free uses in ~100 words
    assert any("at most 2" in p["fix"] for p in kw_problems(three, brand="Incaspin"))
    assert kw_problems(ok)  # without a brand the zero limit still bans it
    assert [p for p in kw_problems("Incaspin casino here. Incaspin twice. Incaspin thrice.", brand="Incaspin")]  # 16 words: only 1 allowed


def _stats(median_words, totals):
    return {"aggregate": {"median_body_words": median_words, "median_total": totals}, "competitors": [{"body_words": median_words}]}


def test_compute_targets_caps_density(settings):
    t = compute_targets(_stats(1000, {"a": 100, "b": 0}), ["a", "b"], settings)
    assert t["target_body_words"] == 1000
    assert t["keyword_targets"]["b"] == 1
    assert sum(t["keyword_targets"].values()) <= 41  # 4% of 1000 + rounding of min 1


def test_validate_and_rebalance(settings):
    kws = ["a", "b"]
    brief = {"blocks": [
        mk(1, "About a", 90, 110, {"a": 1}, source="h1"),
        mk(2, "Part", 90, 110, formats=("list",)),
    ]}
    normalize(brief, kws)
    targets = {"target_body_words": 200, "keyword_targets": {"a": 3, "b": 2}}
    errs = validate(brief, targets, kws, settings)
    assert any('keyword "a"' in e for e in errs) and any('keyword "b"' in e for e in errs)
    rebalance_keywords(brief, targets, kws)
    assert validate(brief, targets, kws, settings) == []


def test_validate_level_jump_and_missing_fields(settings):
    kws = ["a"]
    brief = {"blocks": [mk(1, "T", 90, 110, source="h1"), mk(3, "Jump", 90, 110, entities=[], summary="", entity_connections=[])]}
    normalize(brief, kws)
    errs = validate(brief, {"target_body_words": 200, "keyword_targets": {"a": 0}}, kws, settings)
    assert any("jumps" in e for e in errs)
    assert any("no entities" in e for e in errs) and any("no entity connections" in e for e in errs) and any("empty summary" in e for e in errs)


def test_validate_range_rules(settings):
    kws = ["a"]
    brief = {"blocks": [mk(1, "T", 100, 300, source="h1")]}
    normalize(brief, kws)
    assert any("too wide" in e for e in validate(brief, {"target_body_words": 200, "keyword_targets": {"a": 0}}, kws, settings))


def test_section_totals_and_render(settings):
    kws = ["a"]
    brief = {"intent_summary": "x", "blocks": [
        mk(1, "Title", 90, 110, source="h1", formats=("paragraph",)),
        mk(2, "Games", 140, 160, formats=("paragraph",)),
        mk(3, "Types", 90, 110, formats=("table",)),
        mk(3, "Crash", 90, 110, formats=("list",)),
        mk(2, "Pay", 90, 110, formats=("table",)),
    ]}
    normalize(brief, kws)
    totals = section_totals(brief["blocks"])
    assert totals["b02"] == (140 + 90 + 90, 160 + 110 + 110)
    assert totals["b05"] == (90, 110)
    assert visual_elements(brief["blocks"][2], brief["blocks"]) == "Table — 1 of 2 tables on the page"
    assert visual_elements(brief["blocks"][4], brief["blocks"]) == "Table — 2 of 2 tables on the page"
    assert visual_elements(brief["blocks"][0], brief["blocks"]) == "None specified"
    md = render_markdown(brief, {"geo": "Australia", "language": "en"}, {"target_body_words": 500, "keyword_targets": {"a": 1}})
    assert "Word Count: 320-380 words total including subsections / 140-160 words for this heading" in md
    assert "Entities to cover: Online Casino [10]" in md
    assert "Licence → regulates → Online Casino [8]" in md
    assert "Summary: s" in md and "Copywriter Notes: n" in md


def test_mine_entities():
    pages = [
        {"ok": True, "headings": [{"level": 2, "text": "Payment Methods"}], "text": "You can pay with Skrill or Neteller. Skrill is fast. Pragmatic Play makes slots."},
        {"ok": True, "headings": [], "text": "Deposit with Skrill today. Pragmatic Play and BGaming provide games."},
    ]
    rows = {r["entity"]: r for r in mine_entities(pages, ["Brand"])}
    # the sentence-initial "Skrill is fast" is not counted, the two mid-sentence mentions are
    assert rows["Skrill"]["competitors"] == 2 and rows["Skrill"]["count"] == 2
    assert rows["Pragmatic Play"]["competitors"] == 2
    assert "You" not in rows and "Deposit" not in rows  # sentence-initial single words are ignored


# ---------------- knowledge base ----------------
import json as _json

from textgen import kb as KBM

RAW_KB = {
    "id": 1, "title": "demo-kb", "category": "brand-data",
    "variables": [
        {"key": "brandinfo_welcome", "type": "json", "value": _json.dumps(
            {"welcome_bonus": {"total_bonus": "Up to €2,750", "total_free_spins": 275, "free_spins_games": ["Gates of Olympus", "Aztec Magic"]}})},
        {"key": "brandinfo_deposit", "type": "json", "value": _json.dumps({"deposit_methods": [{"method": "Visa", "minimum": "€15"}, {"method": "Skrill", "minimum": "€15"}]})},
        {"key": "note", "type": "text", "value": "plain text"},
    ],
}


def test_kb_load_and_resolve():
    kb = KBM.load(RAW_KB)
    assert kb["title"] == "demo-kb" and kb["variables"]["note"] == "plain text"
    assert KBM.resolve(kb, "brandinfo_welcome.welcome_bonus.total_bonus") == "Up to €2,750"
    assert KBM.resolve(kb, "brandinfo_welcome.welcome_bonus.free_spins_games[1]") == "Aztec Magic"
    assert KBM.resolve(kb, "brandinfo_deposit.deposit_methods[0]") == {"method": "Visa", "minimum": "€15"}
    assert KBM.resolve(kb, "note") == "plain text"
    with pytest.raises(KeyError, match="path not found"):
        KBM.resolve(kb, "brandinfo_welcome.welcome_bonus.nope")
    with pytest.raises(KeyError):
        KBM.resolve(kb, "brandinfo_deposit.deposit_methods[5]")
    assert "brandinfo_deposit.deposit_methods[1].method" in KBM.leaf_paths(kb)
    assert KBM.variable_of("brandinfo_deposit.deposit_methods[1].method") == "brandinfo_deposit"


def test_brand_info_is_inserted_verbatim_and_validated(settings):
    kb = KBM.load(RAW_KB)
    kws = ["a"]
    brief = {"blocks": [
        mk(1, "T", 90, 110, source="h1", kb_refs=["brandinfo_welcome.welcome_bonus.total_bonus", "note"]),
        mk(2, "Pay", 90, 110, kb_refs=["brandinfo_deposit.deposit_methods"]),
    ]}
    normalize(brief, kws, kb)
    assert brief["blocks"][0]["brand_info"] == [
        {"path": "brandinfo_welcome.welcome_bonus.total_bonus", "value": "Up to €2,750"}, {"path": "note", "value": "plain text"}]
    assert brief["blocks"][1]["brand_info"][0]["value"][1]["method"] == "Skrill"
    targets = {"target_body_words": 200, "keyword_targets": {"a": 0}}
    errs = validate(brief, targets, kws, settings, kb=kb)
    assert [e for e in errs if not e.startswith("no fact table")] == []  # every variable is used, every ref resolves
    assert any(e.startswith("no fact table") for e in errs)  # with a knowledge base the fact sheet is mandatory


def test_kb_validation_errors(settings):
    kb = KBM.load(RAW_KB)
    kws = ["a"]
    brief = {"blocks": [
        mk(1, "T", 90, 110, source="h1", kb_refs=["brandinfo_welcome.welcome_bonus.bogus"]),
        mk(2, "Pay", 90, 110, kb_refs=[]),
    ]}
    normalize(brief, kws, kb)
    errs = validate(brief, {"target_body_words": 200, "keyword_targets": {"a": 0}}, kws, settings, kb=kb)
    assert any("path not found" in e for e in errs)
    assert any("no knowledge-base references" in e for e in errs)
    assert any('variable "brandinfo_deposit" is not used' in e for e in errs)
    assert any('variable "note" is not used' in e for e in errs)


def test_render_shows_brand_info_verbatim(settings):
    kb = KBM.load(RAW_KB)
    brief = {"intent_summary": "x", "blocks": [mk(1, "T", 90, 110, source="h1", kb_refs=["brandinfo_welcome.welcome_bonus.total_bonus"])]}
    normalize(brief, ["a"], kb)
    md = render_markdown(brief, {"geo": "DE", "language": "de", "knowledge_base": "demo-kb"}, {"target_body_words": 100, "keyword_targets": {"a": 0}})
    assert "AffBulk knowledge base: demo-kb" in md
    assert "- brandinfo_welcome.welcome_bonus.total_bonus: Up to €2,750" in md


# ---------------- brand fact table ----------------
FACT_KB = KBM.load({"id": 7, "title": "facts-kb", "variables": [
    {"key": "brandinfo_general", "type": "json", "value": _json.dumps({
        "release_year": 2025,
        "operator": {"company_name": "Legasta Technologies SRL", "jurisdiction": "Costa Rica"},
        "licences": [{"authority": "Tobique Gaming Commission", "licence_number": "0000158", "jurisdiction": "Tobique"}],
        "currencies": ["EUR", "BRL", "BTC"],
        "customer_support": {"email": "support@incaspin.com", "languages": ["English", "Multiple languages"]},
        "business_overview": {"welcome_bonus": "Up to €2,750 + 275 Free Spins", "minimum_deposit": "€20",
                              "payment_methods_overview": ["Visa", "Mastercard", "Skrill"]}})},
    {"key": "brandinfo_promotions", "type": "json", "value": _json.dumps(
        {"other_bonuses": [{"name": "Weekly Cashback", "cashback": "Up to 25% of weekly net losses"}]})},
]})

FACT_ROWS = [
    ("company", "Company", ["brandinfo_general.operator.company_name"]),
    ("licence", "Licence", ["brandinfo_general.licences"]),
    ("founded", "Launch year", ["brandinfo_general.release_year"]),
    ("languages", "Languages", ["brandinfo_general.customer_support.languages"]),
    ("currencies", "Currencies", ["brandinfo_general.currencies"]),
    ("payment_methods", "Payment methods", ["brandinfo_general.business_overview.payment_methods_overview"]),
    ("welcome_bonus", "Welcome bonus", ["brandinfo_general.business_overview.welcome_bonus"]),
    ("cashback", "Cashback", ["brandinfo_promotions.other_bonuses[0].cashback"]),
    ("min_deposit", "Minimum deposit", ["brandinfo_general.business_overview.minimum_deposit"]),
    ("support", "Support", ["brandinfo_general.customer_support.email"]),
]


def fact_brief(rows=FACT_ROWS, position=1, table_kws=1):
    """H1 + overview + games, with the fact sheet inserted at `position` (index among the blocks)."""
    table = mk(2, "Casino Facts", 80, 100, {"Incaspin": table_kws}, formats=("table",),
               fact_table=[{"key": k, "label": label, "kb_refs": refs} for k, label, refs in rows])
    blocks = [mk(1, "Review", 90, 110, source="h1", kb_refs=["brandinfo_general.release_year"]),
              mk(2, "Overview", 90, 110, kb_refs=["brandinfo_general.operator"]),
              mk(2, "Games", 90, 110, kb_refs=["brandinfo_promotions.other_bonuses[0].name"])]
    blocks.insert(position, table)
    brief = {"blocks": blocks}
    normalize(brief, ["Incaspin"], FACT_KB)
    return brief


FACT_TARGETS = {"target_body_words": 390, "keyword_targets": {"Incaspin": 1}}


@pytest.mark.parametrize("position", [1, 2])
def test_fact_table_is_accepted_as_2nd_or_3rd_block(settings, position):
    brief = fact_brief(position=position)
    assert validate(brief, FACT_TARGETS, ["Incaspin"], settings, kb=FACT_KB) == []
    table = brief["blocks"][position]
    # values are inserted verbatim, row refs are added to the block's brand information
    assert table["fact_table"][1]["values"][0]["value"][0]["licence_number"] == "0000158"
    assert table["fact_table"][9]["values"] == [{"path": "brandinfo_general.customer_support.email", "value": "support@incaspin.com"}]
    assert {i["path"] for i in table["brand_info"]} == {p for _, _, refs in FACT_ROWS for p in refs}
    assert set(table["kb_refs"]) == {i["path"] for i in table["brand_info"]}


def test_fact_table_position_and_shape_errors(settings):
    errs = validate(fact_brief(position=3), FACT_TARGETS, ["Incaspin"], settings, kb=FACT_KB)
    assert any("2nd or the 3rd block" in e for e in errs)

    no_cashback = [r for r in FACT_ROWS if r[0] != "cashback"]
    errs = validate(fact_brief(no_cashback), FACT_TARGETS, ["Incaspin"], settings, kb=FACT_KB)
    assert any('no "cashback" row' in e for e in errs)

    errs = validate(fact_brief(FACT_ROWS + [("licence", "License", ["brandinfo_general.licences"])]), FACT_TARGETS, ["Incaspin"], settings, kb=FACT_KB)
    assert any('"licence" appears 2 times' in e for e in errs)

    bad = [("support", "Support", ["brandinfo_general.customer_support.nope"]) if r[0] == "support" else r for r in FACT_ROWS]
    errs = validate(fact_brief(bad), FACT_TARGETS, ["Incaspin"], settings, kb=FACT_KB)
    assert any("path not found" in e for e in errs)
    assert not any("has no knowledge-base reference" in e for e in errs)  # the unresolved path is reported, not a missing ref

    ru = [("licence", "Лицензия", ["brandinfo_general.licences"]) if r[0] == "licence" else r for r in FACT_ROWS]
    assert any("must be in English" in e for e in validate(fact_brief(ru), FACT_TARGETS, ["Incaspin"], settings, kb=FACT_KB))


def test_fact_table_must_budget_the_keyword_inside_its_values(settings):
    # the support e-mail contains the tracked keyword, so the table block has to allow it
    brief = fact_brief(table_kws=0)
    brief["blocks"][2]["keywords"]["Incaspin"] = 1  # the target sum still matches, the table block just does not allow it
    errs = validate(brief, FACT_TARGETS, ["Incaspin"], settings, kb=FACT_KB)
    assert any('contain the tracked keyword "Incaspin"' in e for e in errs)

    # the last-resort rebalancing never takes the keyword away from the table
    brief = fact_brief(table_kws=1)
    rebalance_keywords(brief, {"keyword_targets": {"Incaspin": 0}}, ["Incaspin"])
    assert brief["blocks"][1]["keywords"]["Incaspin"] == 1


def test_fact_table_is_not_required_without_knowledge_base(settings):
    brief = {"blocks": [mk(1, "Review", 90, 110, source="h1"), mk(2, "Games", 90, 110)]}
    normalize(brief, ["a"])
    assert validate(brief, {"target_body_words": 200, "keyword_targets": {"a": 0}}, ["a"], settings) == []


def test_fact_table_in_rendered_brief_and_writer_message():
    from textgen.brief import render_markdown
    from textgen.step2 import _fact_table

    brief = fact_brief()
    md = render_markdown(brief, {"geo": "DE", "language": "de", "knowledge_base": "facts-kb"}, FACT_TARGETS)
    assert "table (fact table)" in md and "Brand Fact Table" in md
    assert "10. Support [support] ← brandinfo_general.customer_support.email" in md
    spec = _fact_table(brief["blocks"][1])
    assert "exactly two columns" in spec and "at most 25 words" in spec
    assert "1. Company [company]: brandinfo_general.operator.company_name = Legasta Technologies SRL" in spec
    assert "10. Support [support]: brandinfo_general.customer_support.email = support@incaspin.com" in spec
    assert _fact_table(brief["blocks"][0]) == ""


def test_check_fact_table(settings):
    b = fact_brief()["blocks"][1]
    body = "\n".join(f"| {label} | Short value {i} |" for i, (_, label, _) in enumerate(FACT_ROWS))
    table = "| Parameter | Details |\n|---|---|\n" + body
    assert [p for p in check_block(b, table, ["Incaspin"], "en", settings) if p["check"] == "fact_table"] == []
    short = "| Parameter | Details |\n|---|---|\n" + "\n".join(body.splitlines()[:-2])
    assert any("8 table rows, required 10" in p["problem"] for p in check_block(b, short, ["Incaspin"], "en", settings))
    long_value = table.replace("Short value 0", " ".join(["word"] * 30))
    assert any("longer than 25 words" in p["problem"] for p in check_block(b, long_value, ["Incaspin"], "en", settings))


def test_competitor_fact_tables_are_extracted_and_summarised():
    from textgen.analysis import fact_table_summary
    from textgen.fetcher import parse_page

    def page(rows):
        trs = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
        return (f"<html><body><main><h1>T</h1><h2>Casino Information</h2><table>{trs}</table>"
                "<table><tr><td>a</td><td>b</td><td>c</td></tr></table></main></body></html>")

    p1 = parse_page(page([("Licence", "Tobique"), ("Currencies", "EUR, BRL"), ("Support", "a@b.c")]), "https://one.example/")
    p2 = parse_page(page([("Licence:", "Curacao"), ("Languages", "English"), ("Support", "x@y.z")]), "https://two.example/")
    assert p1["fact_tables"] == [{"heading": "Casino Information", "rows": [["Licence", "Tobique"], ["Currencies", "EUR, BRL"], ["Support", "a@b.c"]]}]
    summary = fact_table_summary([{**p1, "ok": True}, {**p2, "ok": True}, {"ok": False, "url": "x"}])
    assert len(summary["tables"]) == 2
    labels = {r["label"]: r["competitors"] for r in summary["labels"]}
    assert labels["licence"] == 2 and labels["support"] == 2 and labels["languages"] == 1  # "Licence:" and "Licence" are one label


def test_parse_knowledge_base_line():
    job = parse_text("GEO - DE\nLanguage - de\nKeywords - Incaspin, Inca Spin\nKnowledge Base - incaspin-new\nCompetitors:\nhttps://a.de/")
    assert job.knowledge_base == "incaspin-new" and job.language == "de"
    assert parse_json('{"geo":"DE","keywords":["a"],"competitors":["https://x.de"],"knowledge_base":"kb1"}').knowledge_base == "kb1"


def test_brand_info_hazards_and_warning():
    from textgen.brief import brand_info_hazards, render_block, section_totals
    from textgen.step2 import _brand_info

    kb = KBM.load({"id": 1, "title": "t", "variables": [{"key": "v", "type": "json", "value": _json.dumps(
        {"guide": ["Open incaspin.com and choose Sign up."], "email": "support@incaspin.com", "plain": "Visa, 15 EUR"})}]})
    brief = {"blocks": [mk(1, "T", 90, 110, kws={"Incaspin": 0}, source="h1", kb_refs=["v.guide", "v.email", "v.plain"])]}
    normalize(brief, ["Incaspin"], kb)
    b = brief["blocks"][0]
    assert brand_info_hazards(b, ["Incaspin"]) == {"Incaspin": 2}
    assert "Counting hazard" in render_block(b, brief["blocks"], section_totals(brief["blocks"]))
    msg = _brand_info(b)
    assert "Counting warning" in msg and '"Incaspin" (x2)' in msg
    brief2 = {"blocks": [mk(1, "T", 90, 110, source="h1", kb_refs=["v.plain"])]}
    normalize(brief2, ["Incaspin"], kb)
    assert brand_info_hazards(brief2["blocks"][0], ["Incaspin"]) == {} and "Counting warning" not in _brand_info(brief2["blocks"][0])


def _page_blocks():
    blocks = [mk(level=1, heading="Review"), mk(heading="Welcome Bonus"), mk(level=3, heading="Bonus Terms"),
              mk(level=3, heading="Promo Code"), mk(heading="Games")]
    for b, s in zip(blocks, ["Intro", "The package", "Wagering and validity", "Codes", "Slots and live"]):
        b["summary"] = s
    return normalize({"blocks": blocks}, KW)["blocks"]


def test_sections_group_h2_with_its_subsections():
    from textgen.step2 import sections

    groups = sections(_page_blocks())
    assert [[b["id"] for b in g] for g in groups] == [["b01"], ["b02", "b03", "b04"], ["b05"]]


def test_parse_section_splits_at_markers_and_ignores_strangers():
    from textgen.step2 import parse_section

    raw = "noise\n=== b02 ===\nFirst body.\n\nMore.\n=== b03 ===\nSecond body.\n=== b99 ===\nForeign.\n=== b04 ===\n"
    assert parse_section(raw, ["b02", "b03", "b04"]) == {"b02": "First body.\n\nMore.", "b03": "Second body."}  # b04 is empty -> lost


def test_page_structure_carries_the_summary_of_every_block(settings):
    from textgen.step2 import _outline, build_section_message

    blocks = _page_blocks()
    assert "b03" in _outline(blocks) and ": Wagering and validity" in _outline(blocks)
    brief = {"blocks": blocks, "brand": "VegasHunter", "geo": "Australia", "language": "en", "keywords": KW}
    msg = build_section_message(blocks[1:4], brief, {}, settings)
    assert "`=== bNN ===`" in msg and "b02, b03, b04" in msg
    assert msg.count("## BLOCK BRIEF") == 3 and "written in the same answer" in msg
    assert ": The package" in msg  # the outline reaches the section call


def test_generate_writes_a_section_in_one_call_and_a_lost_block_on_its_own(settings):
    from textgen.step2 import _generate

    class Fake:
        def __init__(self):
            self.calls = []

        def text(self, system, user, model, max_tokens=0):
            self.calls.append(user)
            if "## SECTION" in user:  # the answer forgets b04
                return "=== b02 ===\nParent text.\n=== b03 ===\nChild text."
            return "Single text."

    blocks = _page_blocks()
    brief = {"blocks": blocks, "brand": "VegasHunter", "geo": "Australia", "language": "en", "keywords": KW}
    headings = {b["id"]: b["heading"] for b in blocks}
    llm = Fake()
    out = _generate(blocks[1:4], brief, {}, settings, llm, "sys", headings)
    assert out == {"b02": "Parent text.", "b03": "Child text.", "b04": "Single text."}
    assert len(llm.calls) == 2 and "Parent text." in llm.calls[1]  # the lost block sees its already written neighbours


def test_validate_visuals_minimum_tables_and_lists():
    from textgen.brief import validate_visuals

    fine = [mk(heading="Registration at X", formats=("paragraph", "list")), mk(heading="Payment Methods", formats=("paragraph", "table")),
            mk(heading="Pros and Cons", formats=("table",)), mk(heading="Games")]
    assert validate_visuals(fine) == []
    bad = [mk(heading="Registration at X"), mk(heading="Deposits and Withdrawals", formats=("list",)), mk(heading="Advantages of X", formats=("list",))]
    errs = validate_visuals(bad)
    assert len(errs) == 3 and any("payments table" in e for e in errs) and any("registration steps list" in e for e in errs)
    assert validate_visuals([mk(heading="Games")]) == []  # a page without such blocks is not forced to have them