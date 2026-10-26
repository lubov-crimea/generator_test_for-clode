"""Protected facts: names, amounts, periods and short values of the knowledge base that must stay word for word in every text.

A technical duplicate (shingle 9, see shingles.py) is a run of words shared by two texts. Names of offers and programmes, sizes of bonuses,
periods, currency codes, languages, providers, the licence number and the e-mail are facts: the texts of all sibling pages repeat them
exactly, and that is allowed. Such a phrase counts as ONE word of the run (it is replaced by a placeholder `§phrase`), so the words around
it still have to differ ("claim the §casino_welcome_bonus on the first deposit" is a run of 9 words and is reported) but a name or a figure alone
never makes a duplicate.

What is protected (`protected_phrases`): every short leaf value of the knowledge base that is not a sentence (at most `SHORT_WORDS` words,
not ending with a full stop) and every value of a name-like field (`NAME_KEYS`) up to `NAME_WORDS` words, plus the brand name. Sentences
(steps, conditions, descriptions) are not protected: they are paraphrased (paraphrase.py) and checked.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Iterable

from .inputs import Job
from .shingles import tokens

SHORT_WORDS = 12
NAME_WORDS = 10
NAME_KEYS = {
    "name", "title", "label", "jurisdiction", "operator", "registration_number", "email", "type", "level", "tier", "tiers", "currency",
    "currencies", "brand_name", "provider", "providers", "game", "games", "method", "methods", "language", "languages", "channels",
    "url", "domain", "bank", "banks", "wallet", "wallets", "network", "networks",
}
SENTENCE_END = re.compile(r"[.!?]\s*$")
MIN_SENTENCE_WORDS = 5
PLACEHOLDER = "§"


def is_sentence(s: str) -> bool:
    return bool(SENTENCE_END.search(s.strip())) and len(tokens(s)) >= MIN_SENTENCE_WORDS


def is_protected_leaf(key: str, s: str) -> bool:
    n = len(tokens(s))
    if n == 0:
        return False
    if is_sentence(s):
        return False
    if key in NAME_KEYS and n <= NAME_WORDS:
        return True
    return n <= SHORT_WORDS


def walk_leaves(node: Any, key: str = "") -> Iterable[tuple[str, str]]:
    """(nearest dict key, string) of every string leaf of a knowledge-base value."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk_leaves(v, k)
    elif isinstance(node, list):
        for v in node:
            yield from walk_leaves(v, key)
    elif isinstance(node, str):
        yield key, node


def protected_phrases(kb: dict | None, brand: str = "", extra: Iterable[str] = ()) -> set[tuple[str, ...]]:
    """Token tuples of the protected phrases of a loaded knowledge base (textgen.kb.load), the brand name and `extra` phrases."""
    out: set[tuple[str, ...]] = set()
    if kb:
        for var, val in kb["variables"].items():
            for key, s in walk_leaves(val, var):
                if is_protected_leaf(key, s):
                    tk = tuple(tokens(s))
                    if tk:
                        out.add(tk)
    for s in [brand, *extra, *_extras_of(kb)]:
        tk = tuple(tokens(s or ""))
        if tk:
            out.add(tk)
    return out


def _extras_of(kb: dict | None) -> list[str]:
    """Names that stand only inside sentences of the knowledge base (button labels, programme names): one per line in
    data/paraphrase_banks/<knowledge base title>.protected.txt."""
    if not kb or not kb.get("title"):
        return []
    p = Path(__file__).resolve().parent.parent / "data" / "paraphrase_banks" / f"{re.sub(r'[^A-Za-z0-9._-]+', '_', kb['title'])}.protected.txt"
    if not p.exists():
        return []
    return [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")]


class Mask:
    """Replaces every occurrence of a protected phrase in a token list by ONE placeholder token (longest phrase first)."""

    @classmethod
    def for_kb(cls, kb: dict | None, brand: str = "") -> "Mask":
        """The mask of a knowledge base: its protected phrases, the brand and the explicit names of its `.protected.txt` file."""
        extras = [t for s in _extras_of(kb) if (t := tuple(tokens(s))) and len(t) == 1]
        return cls(protected_phrases(kb, brand), names={t[0] for t in extras})

    def __init__(self, phrases: Iterable[tuple[str, ...]], names: Iterable[str] = ()):
        self.names: set[str] = set(names)  # single words that are names whatever their place in a sentence (Neteller, Skrill, Monday)
        self.by_first: dict[str, list[tuple[str, ...]]] = defaultdict(list)
        for p in phrases:
            self.by_first[p[0]].append(p)
        for lst in self.by_first.values():
            lst.sort(key=len, reverse=True)
        self.size = sum(len(v) for v in self.by_first.values())

    def __call__(self, toks: list[str]) -> list[str]:
        out: list[str] = []
        i, n = 0, len(toks)
        while i < n:
            hit = None
            for p in self.by_first.get(toks[i], ()):
                if tuple(toks[i:i + len(p)]) == p:
                    hit = p
                    break
            if hit:
                out.append(PLACEHOLDER + "_".join(hit))
                i += len(hit)
            else:
                out.append(toks[i])
                i += 1
        return out


def unmask(tok: str) -> str:
    return tok[1:].replace("_", " ") if tok.startswith(PLACEHOLDER) else tok


def unmask_text(toks: Iterable[str]) -> str:
    return " ".join(unmask(t) for t in toks)


def mask_for_runs(names: Iterable[str], runs_dir: Path | None = None) -> Mask:
    """The mask of the union of the knowledge bases and brand names of the given runs (folders in runs/)."""
    from . import kb as KB
    from .config import RUNS_DIR

    base = runs_dir or RUNS_DIR
    phrases: set[tuple[str, ...]] = set()
    names_: set[str] = set()
    seen_kb: set[str] = set()
    for name in names:
        p = base / name / "00_knowledge_base.json"
        if not p.exists():
            continue
        raw = p.read_text(encoding="utf-8")
        brand = ""
        inp = base / name / "00_input.json"
        if inp.exists():
            brand = Job(**json.loads(inp.read_text(encoding="utf-8"))).brand_name
        key = str(len(raw)) + raw[:200] + raw[-200:]
        if key in seen_kb:  # the same knowledge base again: only the brand name can be new
            phrases |= protected_phrases(None, brand)
            continue
        seen_kb.add(key)
        m = Mask.for_kb(KB.load(json.loads(raw)), brand)
        phrases |= {p for lst in m.by_first.values() for p in lst}
        names_ |= m.names
    return Mask(phrases, names_)


def mask_callable(mask: Mask | None) -> Callable[[list[str]], list[str]] | None:
    return mask if mask and mask.size else None
