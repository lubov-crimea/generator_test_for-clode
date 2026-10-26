"""Step 4 - save the final text as a .txt file (plus a structured JSON for the AffBulk import).

Reads : 01_brief.json, 02_blocks.json, last 03_check_iter_NN.json
Writes: 04_final.txt, 04_final.json and a copy output/<slug>.txt
"""
from __future__ import annotations

import shutil

from . import headings as H
from . import store
from .config import OUTPUT_DIR
from .step2 import assemble
from .store import Run


def last_check(run: Run) -> dict | None:
    files = sorted(run.path.glob("03_check_iter_*.json"))
    return run.load_json(files[-1].name) if files else None


def run_step4(run: Run, force: bool = False) -> str:
    check = last_check(run)
    if not force and not (check and check["passed"]):
        raise RuntimeError("The text has not passed step 3. Fix it first or use --force-final.")
    brief = run.load_json(store.BRIEF)
    blocks = run.load_json(store.BLOCKS)["blocks"]
    headings = H.load(run, brief)  # localized page headings
    text = assemble(brief["blocks"], blocks, headings)
    run.save_text(store.FINAL_TXT, text)
    run.save_json(
        store.FINAL_JSON,
        {
            "geo": brief["geo"], "language": brief["language"], "keywords": brief["keywords"],
            "page_type": brief.get("page_type", "brand-review"),
            "passed_checks": bool(check and check["passed"]),
            "blocks": [{"level": b["level"], "heading": headings[b["id"]], "heading_en": b["heading"], "text": blocks[b["id"]]["text"], "formats": b["formats"]} for b in brief["blocks"]],
        },
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / f"{run.path.name}.txt"
    shutil.copyfile(run.path / store.FINAL_TXT, out)
    run.mark("step4", "done", file=str(out))
    print(f"  saved: {out}")
    return str(out)
