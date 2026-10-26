"""Technical duplicates between texts: a run of `n` (default 9) or more words that stands in the same order in two texts (shingle 9).

The texts for sibling sites (one brand, one topic) must not share such runs. A text is split into blocks (the page blocks of `04_final.json`,
headings included); a shingle never crosses a block. Words are lower-cased, markdown and punctuation do not count, a number such as 2,088
is one word. A run of shared words longer than `n` (7 words shared = two shingles) is reported as one run.

`mask` (protected.Mask) replaces names, amounts and other protected facts of the knowledge base by one placeholder word each: they may
repeat word for word, the words around them may not.

    python -m textgen shingles 'longfu88-login-sg-v*' ['longfu88-app-sg-v*' ...] [--n 9] [--json report.json] [--no-protected]
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Callable

from .textutil import strip_markdown

TOKEN_RE = re.compile(r"[^\W_]+(?:[.,][^\W_]+)*", re.UNICODE)
DEFAULT_N = 9
PLACEHOLDER = "§"


def tokens(text: str) -> list[str]:
    return TOKEN_RE.findall(strip_markdown(text).lower())


def _show(tok: str) -> str:
    return tok[1:].replace("_", " ") if tok.startswith(PLACEHOLDER) else tok


def _prepare(corpus: dict[str, list[tuple[str, str]]], mask: Callable[[list[str]], list[str]] | None):
    return {name: [(label, mask(tokens(text)) if mask else tokens(text)) for label, text in blocks] for name, blocks in corpus.items()}


def find_duplicates(corpus: dict[str, list[tuple[str, str]]], n: int = DEFAULT_N,
                    mask: Callable[[list[str]], list[str]] | None = None) -> dict[str, list[dict]]:
    """`corpus` = {text name: [(block label, block text), ...]}. Returns {text name: [run, ...]} where a run is
    {"block", "start", "end", "words", "text", "with": [names of the texts that share at least one shingle of the run]}.
    Only texts with duplicates are in the result; shingles repeated inside one text do not count. `start`/`end`/`words` count
    words after the mask (a protected phrase is one word)."""
    toks = _prepare(corpus, mask)
    owners: dict[tuple, set[str]] = defaultdict(set)
    for name, blocks in toks.items():
        for _, tk in blocks:
            for i in range(len(tk) - n + 1):
                owners[tuple(tk[i:i + n])].add(name)
    result: dict[str, list[dict]] = {}
    for name, blocks in toks.items():
        runs: list[dict] = []
        for label, tk in blocks:
            i = 0
            while i <= len(tk) - n:
                others = owners[tuple(tk[i:i + n])] - {name}
                if not others:
                    i += 1
                    continue
                start, end, with_ = i, i + n, set(others)
                j = i + 1
                while j <= len(tk) - n:
                    o = owners[tuple(tk[j:j + n])] - {name}
                    if not o or j > end:  # the next shingle must overlap the run
                        break
                    with_ |= o
                    end = j + n
                    j += 1
                runs.append({"block": label, "start": start, "end": end, "words": end - start,
                             "text": " ".join(_show(t) for t in tk[start:end]), "with": sorted(with_)})
                i = end
        if runs:
            result[name] = runs
    return result


def summary(corpus: dict[str, list[tuple[str, str]]], dups: dict[str, list[dict]]) -> list[tuple[str, int, int, int]]:
    """[(name, words in the text, runs, words inside runs)] for every text."""
    out = []
    for name, blocks in corpus.items():
        total = sum(len(tokens(t)) for _, t in blocks)
        runs = dups.get(name, [])
        out.append((name, total, len(runs), sum(r["words"] for r in runs)))
    return out


def taken_phrases(others: dict[str, list[tuple[str, str]]], n: int = DEFAULT_N, top: int = 60, max_words: int = 14,
                  mask: Callable[[list[str]], list[str]] | None = None) -> list[str]:
    """Word sequences of `n`+ words that the sibling texts already use, the most widespread first (merged into runs, cut at `max_words`):
    the list a writer is told not to reuse. A sequence made only of protected phrases is skipped."""
    toks = _prepare(others, mask)
    count: Counter = Counter()  # in how many sibling texts a shingle stands
    for blocks in toks.values():
        seen = set()
        for _, tk in blocks:
            for i in range(len(tk) - n + 1):
                seen.add(tuple(tk[i:i + n]))
        count.update(seen)
    runs: dict[tuple, int] = {}
    for blocks in toks.values():
        for _, tk in blocks:
            i = 0
            while i <= len(tk) - n:
                c = count[tuple(tk[i:i + n])]
                if c < 2:  # a phrase of one sibling is not a habit yet; the shingle check of the writer catches it
                    i += 1
                    continue
                end = i + n
                j = i + 1
                while j <= len(tk) - n and count[tuple(tk[j:j + n])] >= 2:
                    end = j + n
                    j += 1
                run = tuple(tk[i:end][:max_words])
                if sum(1 for t in run if not t.startswith(PLACEHOLDER)) >= n:
                    runs[run] = max(runs.get(run, 0), c)
                i = end
    ranked = sorted(runs.items(), key=lambda kv: (-kv[1], -len(kv[0])))
    out, seen_text = [], set()
    for run, c in ranked:
        text = " ".join(_show(t) for t in run)
        if text in seen_text:
            continue
        seen_text.add(text)
        out.append(text)
        if len(out) >= top:
            break
    return out
