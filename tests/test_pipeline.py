"""Offline end-to-end test: fake LLM + local competitor HTML. Verifies wiring, saved artifacts and the fix loop."""
import json
import re

import pytest

from textgen import step2, step4, store
from textgen.config import Settings
from textgen.inputs import Job
from textgen.pipeline import run_all
from textgen.store import Run
from textgen.textutil import count_keywords, count_words

FILLER = (
    "players enjoy a clear lobby with fast deposits and friendly support while the casino keeps every promotion simple "
    "and the terms easy to read for new visitors from Australia"
).split()


def page(h1, sections, kw_text):
    body = "".join(f"<h2>{h}</h2><p>{' '.join(FILLER * 4)} {kw_text}</p>" for h in sections)
    return f"<html><head><title>t</title></head><body><nav>menu</nav><main><h1>{h1}</h1><p>{' '.join(FILLER * 3)} {kw_text}</p>{body}</main></body></html>"


class FakeLLM:
    def __init__(self):
        self.calls = {"text": 0, "consistency": 0}
        self.bad_once = False

    def json(self, system, user, schema, model, name="result", max_tokens=0):
        if name == "heading_clusters":
            groups = {}
            for line in user.splitlines():
                if re.match(r"^c\d+h\d+ \|", line):
                    hid, _lvl, text = [x.strip() for x in line.split("|", 2)]
                    groups.setdefault(text.lower(), []).append(hid)
            return {"clusters": [{"topic": t, "canonical_title": t.title(), "member_ids": ids} for t, ids in groups.items()]}
        if name == "brief":
            ctx = json.loads(user.split("\n\nYour previous")[0])
            return self._brief(ctx)
        if name == "review":
            return {"issues": [], "blocks": json.loads(user)["brief"]["blocks"]}
        if name == "consistency":
            self.calls["consistency"] += 1
            if self.calls["consistency"] == 1:
                return {"issues": [{"block_id": "b03", "problem": "tone differs", "fix": "Use the same neutral tone as b02."}]}
            return {"issues": []}
        raise AssertionError(name)

    def _brief(self, ctx):
        clusters = [c for c in ctx["heading_clusters"] if c["mandatory"]]
        n = len(clusters)
        total = ctx["targets"]["target_body_words"]
        per = round((total - 120) / n)
        extra = {"entities": [{"name": "Online Casino", "priority": 10}],
                 "entity_connections": [{"subject": "Licence", "relation": "regulates", "object": "Online Casino", "priority": 8}],
                 "copywriter_notes": "Stay general."}
        blocks = [{"id": "b01", "level": 1, "heading": "Casino review for Australian players", "source": "h1", "words_min": 105, "words_max": 135,
                   "keywords": {k: 0 for k in ctx["keywords"]}, "summary": "Intro", "formats": ["paragraph"], "covers_clusters": [], **extra}]
        fmts = {"registration": ["paragraph", "list"], "payments": ["paragraph", "table"]}  # the page needs a steps list and a payments table
        for i, c in enumerate(clusters):
            blocks.append({"id": f"b{i + 2:02d}", "level": 2, "heading": c["canonical_title"], "source": "mandatory",
                           "words_min": int(per * 0.9), "words_max": int(per * 1.1),
                           "keywords": {k: 0 for k in ctx["keywords"]}, "summary": f"Cover {c['topic']}",
                           "formats": fmts.get(c["canonical_title"].lower(), ["paragraph"]),
                           "covers_clusters": [c["id"]], **extra})
        for k, need in ctx["targets"]["keyword_targets"].items():
            for j in range(need):
                blocks[j % len(blocks)]["keywords"][k] += 1
        return {"intent_summary": "brand review", "blocks": blocks}

    def text(self, system, user, model, max_tokens=0):
        self.calls["text"] += 1
        spec = next(s for s in user.split("\n\n---\n\n") if s.startswith("## BLOCK BRIEF"))
        bid = re.search(r"Block: (b\d+)", spec).group(1)
        if bid == "b02" and "PROBLEMS TO FIX" not in user:
            return "Too short and wrong format."
        lo, hi = map(int, re.search(r"Word Count: (\d+)-(\d+) words", spec).groups())
        target = (lo + hi) // 2
        fmts = re.search(r"Format: (.+?)\. Visual", spec).group(1).split(" + ")
        kws = [(m.group(1), int(m.group(2))) for m in re.finditer(r'- "([^"]+)": exactly (\d+)', spec)]
        sentences = []
        for k, n in kws:
            sentences += [f"Many visitors ask about {k} before they sign up." for _ in range(n)]
        para = " ".join(sentences) + " {PAD}"
        parts = []
        if "paragraph" in fmts:
            parts.append(para)
        if "list" in fmts:
            parts.append("- Fast deposits and clear limits\n- Friendly support every day\n- Simple promotion terms" + ("" if "paragraph" in fmts else " {PAD}"))
        if "table" in fmts:
            parts.append("| Method | Speed |\n|---|---|\n| Cards | Instant |\n| Wallets | Fast {PAD} |")
            if "paragraph" not in fmts:
                parts[-1] = parts[-1] + ("" if not sentences else "\n\n" + " ".join(sentences))
        text = "\n\n".join(parts)
        n = 0
        while count_words(text.replace("{PAD}", " ".join(FILLER[i % len(FILLER)] for i in range(n)))) < target:
            n += 1
        return text.replace("{PAD}", " ".join(FILLER[i % len(FILLER)] for i in range(n)))


@pytest.fixture
def env(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "RUNS_DIR", tmp_path / "runs")
    monkeypatch.setattr(step4, "OUTPUT_DIR", tmp_path / "output")
    monkeypatch.setattr(step2, "load_writer_prompt", lambda page_type="brand-review": "You are a writer.")
    html = tmp_path / "html"
    html.mkdir()
    kw = "Try VegasHunter casino today. VegasHunter login is easy. Vegas Hunter app. VegasHunter."
    (html / "a.example.html").write_text(page("A review", ["Registration", "Bonuses", "Payments"], kw), encoding="utf-8")
    (html / "b.example.html").write_text(page("B review", ["Registration", "Bonuses", "Support"], kw), encoding="utf-8")
    (html / "c.example.html").write_text(page("C review", ["Registration", "Bonuses", "Payments"], kw), encoding="utf-8")
    job = Job(geo="Australia", keywords=["VegasHunter", "Vegas Hunter", "VegasHunter casino", "VegasHunter login"],
              competitors=["https://a.example/", "https://b.example/", "https://c.example/"])
    return Run.create("t-run", job), html


def test_full_pipeline(env):
    run, html = env
    llm = FakeLLM()
    ok = run_all(run, llm, Settings.load(), html_dir=html)
    assert ok

    # every step saved its result
    for name in [store.INPUT, store.COMPETITORS_RAW, store.KEYWORD_STATS, store.CLUSTERS, store.BRIEF, store.BRIEF_MD,
                 store.BLOCKS, store.TEXT_DRAFT, store.FINAL_TXT, store.FINAL_JSON]:
        assert run.has(name), name

    # mandatory clusters (Registration, Bonuses, Payments) -> 3 H2 + H1
    brief = run.load_json(store.BRIEF)
    assert [b["level"] for b in brief["blocks"]] == [1, 2, 2, 2]
    assert run.load_json(store.INPUT)["language"] == "en"

    # first check failed (b02 too short + consistency issue on b03), the loop fixed it
    first = run.load_json("03_check_iter_00.json")
    assert not first["passed"] and {"b02", "b03"} <= {b for b, p in first["blocks"].items() if p}
    assert run.load_json(store.BLOCKS)["blocks"]["b02"]["version"] == 2
    assert run.load_json("03_fixes_iter_00.json").keys() == {"b02", "b03"}

    # final text honours the ТЗ
    blocks = run.load_json(store.BLOCKS)["blocks"]
    for b in brief["blocks"]:
        assert count_keywords(blocks[b["id"]]["text"], brief["keywords"]) == b["keywords"]
    final = (run.path / store.FINAL_TXT).read_text(encoding="utf-8")
    assert final.startswith("# Casino review for Australian players")
    assert (env[0].path.parent.parent / "output" / "t-run.txt").exists()


def test_step2_refuses_stub_prompt(tmp_path, monkeypatch):
    from textgen import prompts

    (tmp_path / "system_prompt.md").write_text("TEXTGEN_STUB_PROMPT\nplaceholder", encoding="utf-8")
    monkeypatch.setattr(prompts, "PROMPTS_DIR", tmp_path)
    with pytest.raises(RuntimeError, match="stub"):
        prompts.load_writer_prompt()


def test_real_system_prompt_is_in_place():
    from textgen.prompts import load_writer_prompt

    text = load_writer_prompt()  # raises if the stub is still there
    for section in ("## CONTEXT", "## BLOCK BRIEF", "## ALREADY WRITTEN BLOCKS", "## FIX MODE", "## PAGE STRUCTURE FOR CONTEXT"):
        assert section in text  # the prompt describes exactly the sections that step 2 sends


def test_user_message_has_all_brief_parts(env):
    from textgen.step2 import build_user_message

    run, html = env
    run_all_brief = FakeLLM()
    from textgen.step1 import run_step1
    from textgen.config import Settings as S

    run_step1(run, run_all_brief, S.load(), html_dir=html)
    brief = run.load_json(store.BRIEF)
    brief["facts"], brief["brand"] = ["Fact one"], "VegasHunter"
    b = brief["blocks"][1]
    msg = build_user_message(b, brief, {}, S.load(), fixes=["Shorten it."])
    for part in ("## CONTEXT", "Brand: VegasHunter", "- Fact one", "## PAGE STRUCTURE FOR CONTEXT", "## BLOCK BRIEF", "Word Count:",
                 "Entities to cover [priority 1-10]:", "Entity Connections to state explicitly", "Summary:", "Copywriter Notes:",
                 "## FIX MODE", "- Shorten it."):
        assert part in msg, part


def test_missing_or_wrong_knowledge_base_is_an_error(env):
    run, _ = env
    data = run.load_json(store.INPUT)
    data["knowledge_base"] = "demo-kb"
    run.save_json(store.INPUT, data)
    with pytest.raises(RuntimeError, match="does not exist"):
        run.knowledge_base()
    run.save_json(store.KNOWLEDGE_BASE, {"id": 2, "title": "other", "variables": []})
    with pytest.raises(RuntimeError, match='holds "other"'):
        run.knowledge_base()
    run.save_json(store.KNOWLEDGE_BASE, {"id": 1, "title": "demo-kb", "variables": [{"key": "k", "type": "json", "value": "{\"a\": 1}"}]})
    assert run.knowledge_base()["variables"] == {"k": {"a": 1}}


def test_step2_message_carries_verbatim_brand_info(env):
    from textgen.step2 import build_user_message

    run, _ = env
    brief = {"brand": "X", "geo": "DE", "language": "de", "keywords": ["x"], "knowledge_base": {"title": "demo-kb"}, "facts": [],
             "blocks": [{"id": "b01", "level": 1, "heading": "T", "words_min": 50, "words_max": 70, "words": 60, "keywords": {"x": 0},
                         "formats": ["paragraph"], "summary": "s", "copywriter_notes": "n",
                         "entities": [{"name": "E", "priority": 5}], "entity_connections": [{"subject": "a", "relation": "r", "object": "b", "priority": 5}],
                         "brand_info": [{"path": "brandinfo_welcome.welcome_bonus.total_bonus", "value": "Up to €2,750"}]},
                        {"id": "b02", "level": 2, "heading": "U", "words_min": 50, "words_max": 70, "words": 60, "keywords": {"x": 0},
                         "formats": ["paragraph"], "summary": "s", "copywriter_notes": "n",
                         "entities": [{"name": "E", "priority": 5}], "entity_connections": [{"subject": "a", "relation": "r", "object": "b", "priority": 5}],
                         "brand_info": []}]}
    msg = build_user_message(brief["blocks"][0], brief, {}, Settings.load())
    assert "- brandinfo_welcome.welcome_bonus.total_bonus: Up to €2,750" in msg
    assert 'knowledge base "demo-kb"' in msg
    msg2 = build_user_message(brief["blocks"][1], brief, {}, Settings.load())
    assert "Brand Information: none for this block" in msg2

