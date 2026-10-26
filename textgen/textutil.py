"""Deterministic text measurements shared by competitor analysis (step 1) and checks (step 3)."""
from __future__ import annotations

import re
from collections import Counter

WORD_RE = re.compile(r"\w+(?:[’'\-.,/]\w+)*", re.UNICODE)
LIST_RE = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)*\|?\s*$")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")


def strip_markdown(text: str) -> str:
    """Remove markdown syntax so it is not counted as words."""
    out = []
    for line in text.splitlines():
        if TABLE_SEP_RE.match(line) and "|" in line:
            continue
        line = HEADING_RE.sub("", line)
        line = LIST_RE.sub("", line)
        line = line.replace("|", " ")
        line = re.sub(r"[*_`~]{1,3}", "", line)
        line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
        out.append(line)
    return "\n".join(out)


def count_words(text: str) -> int:
    return len(WORD_RE.findall(strip_markdown(text)))


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def is_brand_keyword(keyword: str, brand: str) -> bool:
    """A keyword that is (or contains) the brand name in any spelling: 'Incaspin', 'Inca Spin', 'Incaspin casino' for brand 'Incaspin'."""
    squash = lambda s: re.sub(r"\W+", "", s.lower())  # noqa: E731
    return bool(brand) and squash(brand) in squash(keyword)


INFLECTION_MAX = 3 # letters a word may gain at its end: Casino -> Casinos, Incaspin -> Incaspinie (case endings, plural)


def _ordered(keywords: list[str]) -> list[str]:
    # longest first so "VegasHunter casino" is matched as one keyword and not as "VegasHunter"
    return sorted({_norm(k) for k in keywords}, key=len, reverse=True)


def _kw_pattern(keywords: list[str], inflect: bool = False) -> re.Pattern:
    """With `inflect` every word of a keyword may carry a short ending (up to INFLECTION_MAX letters), so that grammatical cases
    and plurals of the keyword still count; the word order and the stem stay as given."""
    tail = rf"\w{{0,{INFLECTION_MAX}}}" if inflect else ""
    alts = [f"(?P<k{i}>" + r"\s+".join(re.escape(tok) + tail for tok in k.split(" ")) + ")" for i, k in enumerate(_ordered(keywords))]
    return re.compile(r"(?<!\w)(?:" + "|".join(alts) + r")(?!\w)", re.IGNORECASE)


def count_keywords(text: str, keywords: list[str], inflect: bool = False) -> dict[str, int]:
    """Non-overlapping, case-insensitive, longest-match-first counts. Every keyword is present in the result.
    `inflect=True` also counts inflected forms (see _kw_pattern); the default is the exact form."""
    result = {k: 0 for k in keywords}
    if not keywords:
        return result
    by_norm = {_norm(k): k for k in keywords}
    ordered = _ordered(keywords)
    found = Counter(ordered[int(m.lastgroup[1:])] for m in _kw_pattern(keywords, inflect).finditer(strip_markdown(text)))
    for norm, n in found.items():
        result[by_norm[norm]] = n
    return result


def remove_keywords(text: str, keywords: list[str]) -> str:
    return _kw_pattern(keywords).sub(" ", text) if keywords else text


def analyze_format(text: str) -> dict[str, int]:
    """Count paragraphs / lists / tables / stray headings in a markdown-ish block."""
    counts = {"paragraph": 0, "list": 0, "table": 0, "heading": 0}
    lines = text.splitlines()
    i = 0
    prev_kind = None
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            prev_kind = None
            i += 1
            continue
        if HEADING_RE.match(line):
            counts["heading"] += 1
            prev_kind = None
        elif line.strip().startswith("|"):
            j = i
            block = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                block.append(lines[j])
                j += 1
            if any(TABLE_SEP_RE.match(b) for b in block):
                counts["table"] += 1
            else:
                counts["paragraph"] += 1
            i = j
            prev_kind = None
            continue
        elif LIST_RE.match(line):
            if prev_kind != "list":
                counts["list"] += 1
            prev_kind = "list"
        else:
            if prev_kind != "paragraph":
                counts["paragraph"] += 1
            prev_kind = "paragraph"
        i += 1
    return counts


def text_segments(text: str) -> list[str]:
    """Paragraphs, list items and table cells as separate strings (for language detection)."""
    segs: list[str] = []
    buf: list[str] = []

    def flush():
        if buf:
            segs.append(" ".join(buf))
            buf.clear()

    for line in text.splitlines():
        if not line.strip() or HEADING_RE.match(line):
            flush()
        elif TABLE_SEP_RE.match(line) and "|" in line:
            flush()
        elif line.strip().startswith("|"):
            flush()
            segs.extend(c.strip() for c in line.strip().strip("|").split("|") if c.strip())
        elif LIST_RE.match(line):
            flush()
            segs.append(LIST_RE.sub("", line).strip())
        else:
            buf.append(line.strip())
    flush()
    return [re.sub(r"[*_`~]+", "", s) for s in segs if s]
