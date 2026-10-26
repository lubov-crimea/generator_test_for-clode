"""Notes of the briefs of the variants in the words of each variant (the writer echoes its brief; identical notes = identical texts).

    python tools/longfu88/notes_diversify.py show  <run>    what has to be rewritten (free parts of summary, notes, connections) as readable text
    python tools/longfu88/notes_diversify.py apply <run>    validate runs/<run>/llm/notes_div.json and write it into 01_brief.json / 01_brief.md
    python -m textgen lexical <base run>                     the gate: no two variants may share a run of 9 words in their briefs

The answer file runs/<run>/llm/notes_div.json:
    {"intent_summary": "...", "blocks": {"b01": {"summary": "...", "copywriter_notes": "...",
        "connections": [{"relation": "...", "object": "..."}, ...]}, ...}}
Rules checked by `apply`:
  - every block of the brief is answered; the connections keep their number, subject and priority (relation and object are re-worded);
  - the sentences written by code (keyword counts, "Keep the tracked keywords out of ...") stand in the new notes word for word;
  - every figure and protected phrase (name, amount, period) of the old notes stands in the new notes; no new figure appears;
  - the new notes are not the old ones (they share no run of 9 words with them, protected facts excluded).
Run `apply` again after `python -m textgen variants ... --force` (the notes of the variant are then rebuilt from the base).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from textgen import brief as B  # noqa: E402
from textgen import kb as KB  # noqa: E402
from textgen import store  # noqa: E402
from textgen.lexical import CODE_SENTENCE, SPLIT  # noqa: E402
from textgen.protected import Mask, protected_phrases  # noqa: E402
from textgen.shingles import DEFAULT_N, find_duplicates, tokens  # noqa: E402
from textgen.store import Run  # noqa: E402

ROOT = Path(".")


def code_sentences(notes: str) -> list[str]:
    return [s.strip() for s in SPLIT.split(notes) if CODE_SENTENCE.match(s.strip())]


def figures(text: str) -> set[str]:
    return {t for t in tokens(text) if re.search(r"\d", t)}


def show(run: Run) -> None:
    r = run.load_json(store.BRIEF)
    print(f"intent_summary: {r['intent_summary']}\n")
    for b in r["blocks"]:
        print(f"[{b['id']}] H{b['level']} {b['heading']}\n  summary: {b['summary']}\n  notes: {b['copywriter_notes']}")
        for c in b["entity_connections"]:
            print(f"  connection: {c['subject']} -> {c['relation']} -> {c['object']} [{c['priority']}]")
        print()


def apply(run: Run) -> None:
    r = run.load_json(store.BRIEF)
    ans = json.loads((run.path / "llm" / "notes_div.json").read_text(encoding="utf-8-sig"))
    kb = run.knowledge_base()
    mask = Mask.for_kb(kb, run.job().brand_name) if kb else None
    errs: list[str] = []
    new_blocks = ans.get("blocks", {})
    for b in r["blocks"]:
        a = new_blocks.get(b["id"])
        if not a:
            errs.append(f"{b['id']}: no answer")
            continue
        notes = a.get("copywriter_notes", "").strip()
        for s in code_sentences(b["copywriter_notes"]):
            if s not in notes:
                errs.append(f"{b['id']}: the sentence written by code is missing word for word: {s[:80]!r}")
        lost = figures(b["copywriter_notes"] + " " + b["summary"]) - figures(notes + " " + a.get("summary", ""))
        if lost:
            errs.append(f"{b['id']}: figures of the old notes lost: {sorted(lost)}")
        allowed = figures(b["copywriter_notes"] + " " + b["summary"] + " " + " ".join(str(i["value"]) for i in b.get("brand_info", [])))
        invented = figures(notes + " " + a.get("summary", "")) - allowed
        if invented:
            errs.append(f"{b['id']}: figures that the old brief does not have: {sorted(invented)}")
        old_free = " ".join(s for s in SPLIT.split(b["copywriter_notes"]) if not CODE_SENTENCE.match(s.strip()))
        new_free = " ".join(s for s in SPLIT.split(notes) if not CODE_SENTENCE.match(s.strip()))
        if notes == b["copywriter_notes"].strip():  # left as it is (second pass): nothing to compare
            old_free = ""
        same = find_duplicates({"old": [("n", old_free)], "new": [("n", new_free)]}, DEFAULT_N, mask)
        if "new" in same:
            errs.append(f"{b['id']}: the new notes still share {same['new'][0]['words']} words with the old ones: {same['new'][0]['text'][:60]}")
        conns = a.get("connections", [])
        if len(conns) != len(b["entity_connections"]):
            errs.append(f"{b['id']}: {len(conns)} connections, {len(b['entity_connections'])} required")
        if not a.get("summary", "").strip():
            errs.append(f"{b['id']}: empty summary")
    if errs:
        print("NOT APPLIED:\n- " + "\n- ".join(errs[:40]))
        sys.exit(1)
    for b in r["blocks"]:
        a = new_blocks[b["id"]]
        b["copywriter_notes"] = a["copywriter_notes"].strip()
        b["summary"] = a["summary"].strip()
        for c, n in zip(b["entity_connections"], a["connections"]):
            c["relation"], c["object"] = n["relation"].strip(), n["object"].strip()
    if ans.get("intent_summary", "").strip():
        r["intent_summary"] = ans["intent_summary"].strip()
    run.save_json(store.BRIEF, r)
    job = run.job()
    meta = {"geo": job.geo, "language": job.language, "knowledge_base": r["knowledge_base"]["title"] if r.get("knowledge_base") else None, "page_type": job.page_type}
    brief_view = {k: r[k] for k in ("intent_summary", "blocks", "skipped_clusters", "site_pages", "brand") if k in r}
    run.save_text(store.BRIEF_MD, B.render_markdown(brief_view, meta, r["targets"]))
    (run.path / "01_notes_div.json").write_text(json.dumps(ans, ensure_ascii=False, indent=1), encoding="utf-8")
    run.mark("notes_diversify", "done", blocks=len(r["blocks"]))
    print(f"applied to {len(r['blocks'])} blocks of {run.path.name}; 01_brief.md re-rendered")


if __name__ == "__main__":
    cmd, name = sys.argv[1], sys.argv[2]
    if cmd == "conflicts":  # writes runs/<variant>/llm/lexical_conflicts.txt for every variant of the base run
        from textgen.lexical import lexical_conflicts

        found, _ = lexical_conflicts(name, ROOT / "runs", DEFAULT_N)
        for v, lst in found.items():
            lines = [f"[{r['block']}] {r['text']}   (also in {', '.join(x[-3:] for x in r['with'])})" for r in lst]
            (ROOT / "runs" / v / "llm" / "lexical_conflicts.txt").write_text("\n".join(lines), encoding="utf-8")
            print(v, len(lst))
        sys.exit(0)
    run = Run.open(name)
    show(run) if cmd == "show" else apply(run) if cmd == "apply" else sys.exit(__doc__)
