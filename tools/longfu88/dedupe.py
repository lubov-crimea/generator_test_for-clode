"""Technical duplicates (shingle 9) of one finished run against all the other texts of the Longfu88 SG set. Run from the project root.

    python tools/longfu88/dedupe.py report <run>                 shared runs of 9+ words, block by block, with the sentence around them
    python tools/longfu88/dedupe.py apply <run> <bNN> <file>     check a new body of one block (size, keywords, format, language), put it
                                                                 into 02_blocks.json, re-run step 4, print what is still shared in that block

The reference corpus: the other 11 texts of the same page type, the texts of the two other page types and the 12 SG home pages
(runs longfu88-{login,bonus,app}-sg-v01..v12 and longfu88-sg-v01..v12, the finished text is 04_final.json). The home pages are never changed.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from textgen import shingles as S  # noqa: E402
from textgen import store  # noqa: E402
from textgen.checks import check_block  # noqa: E402
from textgen.config import Settings  # noqa: E402
from textgen.protected import Mask, protected_phrases  # noqa: E402
from textgen.siblings import sibling_corpus  # noqa: E402
from textgen.step2 import clean_output  # noqa: E402
from textgen.store import Run  # noqa: E402
from textgen.textutil import count_words  # noqa: E402

ROOT = Path(".")


def load(name: str) -> list[tuple[str, str]]:
    f = json.loads((ROOT / "runs" / name / "04_final.json").read_text(encoding="utf-8"))
    return [(f"b{i + 1:02d} {b['heading']}", b["heading"] + "\n\n" + b["text"]) for i, b in enumerate(f["blocks"])]


def corpus_for(run: str) -> dict:
    """The finished text of the run and the texts of its siblings (same brand, GEO, language and knowledge base)."""
    return {run: load(run), **sibling_corpus(ROOT / "runs" / run)}


def shared(run: str) -> list[dict]:
    r = Run.open(run)
    kb = r.knowledge_base()
    mask = Mask.for_kb(kb, r.job().brand_name) if kb else None
    return S.find_duplicates(corpus_for(run), Settings.load().shingle_n, mask).get(run, [])


def sentence_of(block_text: str, run_text: str) -> str:
    """The original sentence/cell that holds the first words of a shared run (for the report)."""
    head = " ".join(run_text.split()[:4])
    for part in re.split(r"(?<=[.!?])\s+|\n+", block_text):
        if head in " ".join(S.tokens(part)):
            return part.strip()
    return ""


def report(run: str) -> None:
    final = json.loads((ROOT / "runs" / run / "04_final.json").read_text(encoding="utf-8"))
    runs = shared(run)
    total = sum(count_words(b["text"]) for b in final["blocks"])
    print(f"{run}: {len(runs)} shared runs, {sum(r['words'] for r in runs)} words of {total}")
    by_block: dict[str, list[dict]] = {}
    for r in runs:
        by_block.setdefault(r["block"], []).append(r)
    for label, lst in by_block.items():
        bid = label.split()[0]
        idx = int(bid[1:]) - 1
        text = final["blocks"][idx]["text"]
        print(f"\n--- {label}  ({len(lst)} runs)")
        for r in lst:
            sent = sentence_of(text, r["text"])
            print(f"  * [{r['words']}w, with {', '.join(x.replace('longfu88-', '').replace('-sg', '') for x in r['with'][:5])}] {r['text'][:100]}")
            if sent:
                print(f"      in: {sent[:220]}")


def apply(run: str, bid: str, path: str) -> None:
    r = Run.open(run)
    brief = r.load_json(store.BRIEF)
    b = next(x for x in brief["blocks"] if x["id"] == bid)
    state = r.load_json(store.BLOCKS)
    blk = state["blocks"][bid]
    settings = Settings.load()
    text = clean_output(Path(path).read_text(encoding="utf-8-sig"), blk["heading"])
    problems = check_block(b, text, brief["keywords"], brief["language"], settings, r.job().brand_name)
    n = count_words(text)
    print(f"{bid}: {n} words (range {b['words_min']}-{b['words_max']}, cap {int(b['words_max'] * (1 + settings.words_overflow))})")
    if problems:
        for p in problems:
            print(f"  FAIL [{p['check']}] {p['problem']}")
        print("NOT APPLIED")
        sys.exit(1)
    blk["text"] = text
    blk["version"] += 1
    blk["history"] = blk.get("history", []) + [{"iteration": "dedupe-shingle9", "fixes": []}]
    r.save_json(store.BLOCKS, state)
    rc = subprocess.run([sys.executable, "-m", "textgen", "step4", run], capture_output=True, text=True, encoding="utf-8")
    print(f"applied, step4 rc={rc.returncode} {rc.stderr.strip()[:120]}")
    left = [x for x in shared(run) if x["block"].startswith(bid + " ")]
    print(f"still shared in {bid}: {len(left)} runs")
    for x in left:
        print(f"  * [{x['words']}w with {', '.join(y.replace('longfu88-', '') for y in x['with'][:4])}] {x['text'][:110]}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "report":
        report(sys.argv[2])
    elif cmd == "apply":
        apply(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit(__doc__)
