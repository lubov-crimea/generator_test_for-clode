"""Manual-mode helper for step 2: one call per block.

    python tools/longfu88/next_request.py <run>

1. If answers exist (llm/text_NNN.txt), checks the LAST one with check_answer.py (the code checks of step 3 + style warnings).
2. Deletes 02_blocks.json (the text_NNN numbering restarts in every process) and runs `python -m textgen step2 <run> --llm manual`.
3. Prints either `STEP 2 DONE` or the path of the answer file to write and the part of the request you need: the first request is shown
   whole (context, page structure, brief); later ones only from `## SECTION` / `## BLOCK BRIEF` on (the context and the structure are the
   same, the blocks already written are your own texts).
"""
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    run = sys.argv[1]
    llm = ROOT / "runs" / run / "llm"
    answers = sorted(llm.glob("text_*.txt"))
    if answers:
        last = answers[-1]
        print(f"=== check of {last.name} ===")
        r = subprocess.run([sys.executable, str(ROOT / "tools/longfu88/check_answer.py"), run, str(last)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        print(r.stdout.strip())
        if r.stderr.strip():
            print(r.stderr.strip())
        if r.returncode:
            print("\nThe last answer FAILS the code checks: fix it (same file) and run this script again.")
            return 1
    blocks = ROOT / "runs" / run / "02_blocks.json"
    if blocks.exists():
        blocks.unlink()
    r = subprocess.run([sys.executable, "-m", "textgen", "step2", run, "--llm", "manual"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout + r.stderr)
    m = re.search(r"Answer needed: (.+?\.(?:txt|json)) \(request: (.+?\.request\.md)\)", out)
    if m and Path(m.group(1)).name == "text_002.txt" and not (llm / "text_001.txt").exists() and (ROOT / "runs" / run / "02_headings.json").exists():
        # the headings answer was read in this process and used up call number 1: the next process numbers the first text as text_001
        Path(m.group(2)).unlink(missing_ok=True)
        if blocks.exists():
            blocks.unlink()
        r = subprocess.run([sys.executable, "-m", "textgen", "step2", run, "--llm", "manual"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        out = (r.stdout + r.stderr)
        m = re.search(r"Answer needed: (.+?\.(?:txt|json)) \(request: (.+?\.request\.md)\)", out)
    if not m:
        if r.returncode == 0:
            print("\nSTEP 2 DONE (02_text_draft.md written). Next: python -m textgen step3 " + run + " --llm manual")
            return 0
        print(out)
        return 2
    ans, req = Path(m.group(1)), Path(m.group(2))
    text = req.read_text(encoding="utf-8")
    user = text.split("# USER", 1)[1]
    if ans.suffix == ".json":  # the localized page headings (or a repair of them): the whole request, the answer is JSON
        print(f"\n=== WRITE THE JSON ANSWER TO: {ans}\n(request file: {req.name}; format {{\"headings\": [{{\"id\": \"b01\", \"heading\": \"...\"}}, ...]}}, one entry for EVERY id of the request; each heading keeps exactly the keywords listed for it)\n")
        print(user.strip())
        return 0
    if ans.name == "text_001.txt":
        shown = user
    else:
        k = re.search(r"^## (TAKEN PHRASES|SECTION|BLOCK BRIEF)", user, re.MULTILINE)  # the taken phrases change as sibling texts are written
        shown = user[k.start():] if k else user
    print(f"\n=== WRITE THE ANSWER TO: {ans}\n(request file: {req.name}; section answers need a `=== bNN ===` line before every block)\n")
    print(shown.strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
