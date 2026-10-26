"""Manual-mode helper: checks an answer file (llm/text_NNN.txt) of step 2 the same way step 3 will, before the pipeline sees it.

    python tools/longfu88/check_answer.py <run> <path to llm/text_NNN.txt>
    python tools/longfu88/check_answer.py <run> <file with the body of one block> --block bNN

Prints, for every block of the answer: word count against the ТЗ range and cap, the code checks of step 3 (size, keywords, language,
format, fact table) and style warnings from prompts/system_prompt.md (em dashes, semicolons, banned words, first/second person,
rhetorical questions, routine connectors, repeated sentence openings). Exit code 1 when a code check fails.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from textgen import store  # noqa: E402
from textgen.checks import check_block, check_shingles  # noqa: E402
from textgen.config import Settings  # noqa: E402
from textgen.protected import Mask, protected_phrases  # noqa: E402
from textgen.siblings import sibling_corpus  # noqa: E402
from textgen.step2 import SECTION_MARK_RE, clean_output, parse_section  # noqa: E402
from textgen.store import Run  # noqa: E402
from textgen.textutil import count_keywords, count_words, strip_markdown  # noqa: E402

BANNED = ("meticulous navigate navigating complexities realm bespoke tailored underpins ever-changing ever-evolving unlock robust delve harness "
          "leverage unveil elevate empower seamless tapestry landscape testament pivotal crucial game-changer cutting-edge comprehensive holistic "
          "dynamic great exciting impressive fortunately unfortunately best ultimate incredible amazing guaranteed huge").split()
BANNED_PHRASES = ["the world of", "not only", "designed to enhance", "it is advisable", "it is important to note", "worth mentioning", "look no further",
                  "at the heart of", "whether you are", "in today's"]
ROUTINE = ("However,", "Moreover,", "Furthermore,", "Additionally,", "Notably,", "Importantly,", "Overall,", "In conclusion")


def lint(text: str, faq: bool, lang: str = "en") -> list[str]:
    out = []
    plain = strip_markdown(text)
    if "—" in text:
        out.append("em dash")
    if ";" in plain:
        out.append("semicolon")
    if "?" in plain and not faq:
        out.append("question mark outside the FAQ")
    low = plain.lower()
    if lang != "en":  # the word lists below are English: only the structural rules apply
        if "  " in text or " " in text:
            out.append("double or non-breaking spaces")
        return out
    for w in BANNED:
        if re.search(rf"\b{re.escape(w)}\b", low):
            out.append(f"banned word '{w}'")
    for p in BANNED_PHRASES:
        if p in low:
            out.append(f"banned phrase '{p}'")
    m = re.search(r"\b(we|We|our|Our|us)\b", plain)  # "US dollar" is not a pronoun
    if m:
        out.append(f"first person '{m.group(1)}'")
    if re.search(r"\byou(r|rs|rself)?\b", low):
        out.append("second person 'you' (allowed only in a plain call to action)")
    for r in ROUTINE:
        if re.search(rf"(^|\n|\. ){r}", plain):
            out.append(f"routine connector '{r}'")
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", plain) if len(s.split()) > 2]
    firsts = [s.split()[0].lower() for s in sents]
    for i in range(len(firsts) - 1):
        if firsts[i] == firsts[i + 1] and firsts[i] not in {"-", "|"}:
            out.append(f"two consecutive sentences start with '{firsts[i]}'")
            break
    if "  " in text or " " in text:
        out.append("double or non-breaking spaces")
    if sents:
        out.append(f"info: {len(sents)} sentences, average {sum(len(s.split()) for s in sents) / len(sents):.1f} words")
    return out


def main() -> int:
    run = Run.open(sys.argv[1])
    ans = Path(sys.argv[2])
    if len(sys.argv) > 4 and sys.argv[3] == "--block":  # a single block outside a request (step 3 fixes)
        ids = [sys.argv[4]]
    else:
        req = ans.with_name(ans.stem + ".request.md").read_text(encoding="utf-8")
        ids = re.findall(r"^Block: (b\d+),", req, re.MULTILINE)
    brief = run.load_json(store.BRIEF)
    settings = Settings.load()
    by_id = {b["id"]: b for b in brief["blocks"]}
    raw = ans.read_text(encoding="utf-8-sig")
    if len(ids) > 1 or SECTION_MARK_RE.search(raw):
        texts = {i: clean_output(t, by_id[i]["heading"]) for i, t in parse_section(raw, ids).items()}
        lost = [i for i in ids if i not in texts]
        if lost:
            print(f"MISSING blocks in the answer (marker lines `=== bNN ===` expected): {', '.join(lost)}")
    else:
        texts = {ids[0]: clean_output(raw, by_id[ids[0]]["heading"])}
    failed = bool([i for i in ids if i not in texts])
    sib = sibling_corpus(run.path)  # technical duplicates (shingle 9) against the other texts of the brand; names and figures are exempt
    kb = run.knowledge_base()
    mask = Mask.for_kb(kb, run.job().brand_name) if kb else None
    for i in ids:
        if i not in texts:
            continue
        b, t = by_id[i], texts[i]
        n = count_words(t)
        problems = check_block(b, t, brief["keywords"], brief["language"], settings, run.job().brand_name)
        problems += check_shingles(i, b["heading"] + "\n\n" + t, run.path, settings, mask, sib)
        kw = count_keywords(t, brief["keywords"], inflect=True)
        used = {k: f"{kw[k]}/{b['keywords'][k]}" for k in brief["keywords"] if kw[k] or b["keywords"][k]}
        print(f"{i} {b['heading'][:50]!r}: {n} words (range {b['words_min']}-{b['words_max']}, cap {int(b['words_max'] * (1 + settings.words_overflow))}); keywords found/required {used}")
        for p in problems:
            failed = True
            print(f"   FAIL [{p['check']}] {p['problem']}" + (f" :: {p['fix'][:330]}" if p["check"] in ("language", "fact_table") else ""))
            if p["check"] == "shingle":
                print("      -> rewrite the sentences with those words in another construction; names and figures stay exact")
        for w in lint(t, faq=b["formats"] == ["list"] and any(x in b["summary"].lower() for x in ("answers", "questions")), lang=brief["language"]):
            print(f"   warn: {w}")
    print("RESULT:", "FAIL" if failed else "code checks OK")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
