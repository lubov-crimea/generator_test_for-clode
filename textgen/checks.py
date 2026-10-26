"""Step 3 deterministic checks of one block against its ТЗ. Each problem comes with a ready fix instruction."""
from __future__ import annotations

import re

from .brief import FACT_TABLE_VALUE_MAX_WORDS, block_cap, block_range
from .config import Settings
from .lang import check_language, language_name
from .textutil import TABLE_SEP_RE, analyze_format, count_keywords, count_words, is_brand_keyword


def brand_free_max(words: int, settings: Settings) -> int:
    """Where the ТЗ allows the brand name 0 times it may still appear once per `brand_free_words` words (at least once)."""
    return max(1, words // settings.brand_free_words)


def check_block(b: dict, text: str, keywords: list[str], language: str, settings: Settings, brand: str = "") -> list[dict]:
    """b = ТЗ block, text = generated body. Returns [{check, problem, fix}]."""
    problems: list[dict] = []

    # 1. size: the ТЗ range is the target; the text may run over words_max by `words_overflow` (20%) when facts and style need the room
    n = count_words(text)
    lo, hi = block_range(b)
    cap = block_cap(b, settings)
    if n < lo or n > cap:
        problems.append({
            "check": "size",
            "problem": f"{n} words, required {lo}-{hi} (up to {cap} allowed)",
            "fix": (f"Length is {n} words but must be {lo}-{hi}; going over {hi} is allowed up to {cap} words. "
                    + (f"Shorten the block to at most {cap} words (aim for {hi}); cut the least important details." if n > cap
                       else f"Expand the block to about {round((lo + hi) / 2)} words; add useful substance, not filler.")),
        })

    # 2. keywords: inflected forms count; the brand name is free where the ТЗ allows it 0 times
    found = count_keywords(text, keywords, inflect=True)
    free = [k for k in keywords if b["keywords"].get(k, 0) == 0 and is_brand_keyword(k, brand)]
    free_used = sum(found[k] for k in free)
    free_max = brand_free_max(n, settings)
    if free_used > free_max:
        problems.append({
            "check": "keywords",
            "problem": f"brand name used {free_used} times where the ТЗ allows 0 (at most {free_max} in {n} words)",
            "fix": f"The brand name (without a count in the ТЗ for this block) appears {free_used} times, at most {free_max} are allowed "
                   f"(one per {settings.brand_free_words} words). Remove {free_used - free_max} occurrence(s): use a pronoun or a descriptive noun.",
        })
    for k in keywords:
        need = b["keywords"].get(k, 0)
        if k in free:
            continue
        if found[k] != need:
            if found[k] < need:
                act = f"add {need - found[k]} more natural occurrence(s)"
            elif need == 0:
                act = "remove all occurrences (rephrase, e.g. use a pronoun or a descriptive noun)"
            else:
                act = f"remove {found[k] - need} occurrence(s)"
            problems.append({
                "check": "keywords",
                "problem": f'"{k}": {found[k]} found, {need} required',
                "fix": f'Keyword "{k}" appears {found[k]} time(s) but must appear exactly {need}: {act}.',
            })

    # 3. language
    bad = check_language(text, language, keywords)
    if bad:
        samples = "; ".join(f'"{x["segment"][:80]}" ({x["detected"]})' for x in bad[:3])
        problems.append({
            "check": "language",
            "problem": f"{len(bad)} fragment(s) not in {language_name(language)}",
            "fix": f"Some fragments are not in {language_name(language)}: {samples}. Rewrite the whole block in {language_name(language)} only.",
        })

    # 4. formats
    if re.search(r"={3}\s*b\d+\s*={3}", text):  # the marker that splits a section answer must never stay in a finished block
        problems.append({"check": "format", "problem": "section marker left in the text",
                         "fix": "Remove the section marker line (=== bNN ===) from the text of this block; output the body text only."})
    fmt = analyze_format(text)
    want = set(b["formats"])
    if fmt["heading"]:
        problems.append({"check": "format", "problem": "headings inside the block", "fix": "Remove all headings (#) from the block body; output body text only."})
    for f in ("paragraph", "list", "table"):
        if f in want and fmt[f] == 0:
            hint = {"paragraph": "prose paragraphs", "list": 'a markdown list ("- " or "1. ")', "table": "a markdown table with a header row"}[f]
            problems.append({"check": "format", "problem": f"missing {f}", "fix": f"The ТЗ requires the format '{f}' but it is missing. Add {hint}."})
        if f not in want and fmt[f] > (1 if f == "paragraph" and want else 0):
            problems.append({"check": "format", "problem": f"unexpected {f}", "fix": f"The format '{f}' is not allowed in this block (allowed: {', '.join(b['formats'])}). Rewrite it using only the allowed formats."})
    problems += check_fact_table(b, text)
    return problems


def check_shingles(block_label: str, text: str, run_path, settings: Settings, mask=None, siblings: dict | None = None) -> list[dict]:
    """Technical duplicates (shingle `settings.shingle_n`) of one block against the sibling texts of the brand (siblings.py)."""
    from .shingles import find_duplicates
    from .siblings import sibling_corpus

    sib = siblings if siblings is not None else sibling_corpus(run_path)
    if not sib:
        return []
    runs = find_duplicates({"_self": [(block_label, text)], **sib}, settings.shingle_n, mask).get("_self", [])
    if not runs:
        return []
    shown = "; ".join(f'"{r["text"][:70]}" (also in {", ".join(x.replace("longfu88-", "") for x in r["with"][:2])})' for r in runs[:5])
    return [{
        "check": "shingle",
        "problem": f"{len(runs)} run(s) of {settings.shingle_n}+ words shared with sibling texts: {shown}",
        "fix": f"Technical duplicates: these word sequences stand word for word in other pages of the brand: {shown}. Rewrite the sentences that contain "
               f"them in different words and with a different construction (not a synonym swap). Names, figures and periods stay exact; "
               f"no {settings.shingle_n} words in a row may match another page.",
    }]


def check_fact_table(b: dict, text: str) -> list[dict]:
    """The fact sheet is a two-column table with exactly one row per ТЗ row and short values."""
    rows = b.get("fact_table") or []
    if not rows:
        return []
    lines = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("|") and not TABLE_SEP_RE.match(ln)]
    cells = [[c.strip() for c in ln.strip("|").split("|")] for ln in lines]
    data = cells[1:]  # the first row is the header
    problems: list[dict] = []
    if len(data) != len(rows):
        problems.append({
            "check": "fact_table", "problem": f"{len(data)} table rows, required {len(rows)}",
            "fix": f"The fact table must have a header row and exactly {len(rows)} data rows, one per row of the brief "
                   f"({'; '.join(r['label'] for r in rows)}), in this order. Add the missing rows or remove the extra ones.",
        })
    if any(len(r) != 2 for r in cells):
        problems.append({"check": "fact_table", "problem": "table is not two-column",
                         "fix": "The fact table has exactly two columns: label and value."})
    long_rows = [r for r in data if len(r) == 2 and count_words(r[1]) > FACT_TABLE_VALUE_MAX_WORDS]
    if long_rows:
        problems.append({
            "check": "fact_table", "problem": f"{len(long_rows)} value(s) longer than {FACT_TABLE_VALUE_MAX_WORDS} words",
            "fix": f'Shorten the value of "{long_rows[0][0]}"' + (f' and {len(long_rows) - 1} more' if len(long_rows) > 1 else "") +
                   f" to a short fact of at most {FACT_TABLE_VALUE_MAX_WORDS} words (a figure, a name or a comma-separated list), no sentences.",
        })
    return problems

