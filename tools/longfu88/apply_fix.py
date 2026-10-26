"""Manual-mode helper for step 3 fixes: replaces the text of one block in runs/<run>/02_blocks.json (as step 2 does in fix mode).

    python tools/longfu88/apply_fix.py <run> <block id> <file with the new body text> [iteration]

The new text is cleaned like a step 2 answer (code fences, repeated heading). The version is raised and the fixes of the last
03_fixes_iter_NN.json for this block are put into the history.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, ".")

from textgen import store  # noqa: E402
from textgen.step2 import clean_output  # noqa: E402
from textgen.store import Run  # noqa: E402


def main() -> None:
    run = Run.open(sys.argv[1])
    bid = sys.argv[2]
    text = Path(sys.argv[3]).read_text(encoding="utf-8-sig")
    state = run.load_json(store.BLOCKS)
    blk = state["blocks"][bid]
    fixes_files = sorted(run.path.glob("03_fixes_iter_*.json"))
    fixes = json.loads(fixes_files[-1].read_text(encoding="utf-8")).get(bid, []) if fixes_files else []
    iteration = int(sys.argv[4]) if len(sys.argv) > 4 else len(fixes_files)
    blk["text"] = clean_output(text, blk["heading"])
    blk["version"] += 1
    blk["history"] = blk.get("history", []) + [{"iteration": iteration, "fixes": fixes}]
    run.save_json(store.BLOCKS, state)
    print(f"{bid}: text replaced, version {blk['version']}")


if __name__ == "__main__":
    main()
