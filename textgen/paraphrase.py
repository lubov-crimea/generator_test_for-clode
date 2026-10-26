"""Fact cards and the paraphrase bank: the writer gets facts as a card, not as the verbatim sentences of the knowledge base.

Why: 61 % of the words that sibling texts shared were knowledge-base sentences copied word for word (a Brand Information block was echoed by
the writer of every variant). Names, figures, periods and other short values (protected.py) stay exact; every SENTENCE of the knowledge base
(steps, conditions, descriptions) is given to the writer of a variant in one of `slots` alternative wordings of the paraphrase bank, so two
variants never see the same sentence. The bank is made once per knowledge base:

    data/paraphrase_banks/<knowledge base title>.json
    {"kb": "...", "slots": 12, "items": {"<key>": {"text": <sentence>, "paraphrases": [<12 wordings>]}}}

A paraphrase is valid (`validate_item`) when it keeps every figure and protected phrase of the sentence, invents no figure, shares no run of
`n` words with the sentence or with another paraphrase of the same sentence, and has about the same length. The slot of a variant is its
number (v03 -> 2); a base run uses slot 0. Lists of the card that are not ordered (providers, languages, payment methods, offers) are shown
in an order that depends on the run, tables get another header word pair: the layout of the facts differs from variant to variant too.
"""
from __future__ import annotations

import hashlib
import json
import random
import re
from pathlib import Path
from typing import Any

from .config import ROOT
from .protected import PLACEHOLDER, Mask, is_sentence, unmask, walk_leaves
from .shingles import find_duplicates, tokens

BANK_DIR = ROOT / "data" / "paraphrase_banks"
NUMBER_RE = re.compile(r"\d[\d.,]*[%x]?")
ORDERED_KEY_RE = re.compile(r"step|procedure|order|sequence|level|tier|rank|rating|position|index|stage|phase|day|week|month|time|period|year|point", re.I)
HEADER_PAIRS = [("Parameter", "Details"), ("Item", "Value"), ("Fact", "Detail"), ("Topic", "Information"), ("Feature", "Summary"),
                ("Point", "What to know"), ("Aspect", "Description"), ("Category", "Data"), ("Question", "Answer"), ("Area", "Facts"),
                ("Field", "Content"), ("Subject", "Overview")]


def bank_path(kb_title: str) -> Path:
    return BANK_DIR / f"{re.sub(r'[^A-Za-z0-9._-]+', '_', kb_title)}.json"


def text_key(s: str) -> str:
    return hashlib.sha1(" ".join(tokens(s)).encode("utf-8")).hexdigest()[:12]


def load_bank(kb_title: str) -> dict:
    p = bank_path(kb_title)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"kb": kb_title, "slots": 12, "items": {}}


def save_bank(bank: dict) -> Path:
    BANK_DIR.mkdir(parents=True, exist_ok=True)
    p = bank_path(bank["kb"])
    p.write_text(json.dumps(bank, ensure_ascii=False, indent=1), encoding="utf-8")
    return p


def sentences_of(kb: dict) -> dict[str, str]:
    """{key: sentence} of every sentence leaf (not protected) of a loaded knowledge base."""
    out: dict[str, str] = {}
    for var, val in kb["variables"].items():
        for _, s in walk_leaves(val, var):
            if is_sentence(s):
                out.setdefault(text_key(s), s.strip())
    return out


def numbers_of(s: str) -> list[str]:
    return [t for t in tokens(s) if re.search(r"\d", t)]


def must_keep(s: str, mask: Mask) -> tuple[list[str], list[str]]:
    """(figures, protected phrases) of a sentence that every paraphrase has to keep."""
    masked = mask(tokens(s))
    # names: multi-word protected phrases and single words written with a capital inside the sentence (Neteller, Skrill, Monday);
    # a common single word that merely happens to be a short value of the knowledge base ("deposits", "casino") is not a name
    caps = {w.lower() for w in re.findall(r"(?<![.!?]\s)(?<!^)\b([A-Z][\w'-]*)", s)}
    phrases = [unmask(t) for t in masked if t.startswith(PLACEHOLDER) and not re.search(r"\d", t)
               and ("_" in t or t[1:] in caps or t[1:] in getattr(mask, "names", ()))]
    figs = [t for t in tokens(s) if re.search(r"\d", t)]
    return list(dict.fromkeys(figs)), list(dict.fromkeys(phrases))


def validate_paraphrase(original: str, para: str, mask: Mask, n: int = 9) -> list[str]:
    errs: list[str] = []
    if not isinstance(para, str) or not para.strip():
        return ["empty"]
    if "—" in para or ";" in para:
        errs.append("em dash or semicolon")
    o_tok, p_tok = tokens(original), tokens(para)
    if " ".join(o_tok) == " ".join(p_tok):
        errs.append("identical to the original")
    figs, phrases = must_keep(original, mask)
    for f in figs:
        if f not in p_tok:
            errs.append(f"figure lost: {f}")
    new_figs = [t for t in p_tok if re.search(r"\d", t) and t not in o_tok]
    if new_figs:
        errs.append(f"figure invented: {', '.join(new_figs)}")
    p_masked = mask(p_tok)
    for ph in phrases:
        if PLACEHOLDER + "_".join(tokens(ph)) not in p_masked:
            errs.append(f"name lost: {ph}")
    if not 0.55 * len(o_tok) <= len(p_tok) <= 1.8 * len(o_tok) + 3:
        errs.append(f"length {len(p_tok)} words vs {len(o_tok)} in the original")
    dup = find_duplicates({"o": [("b", original)], "p": [("b", para)]}, n, mask).get("p")
    if dup:
        errs.append(f"shares {dup[0]['words']} words with the original: {dup[0]['text'][:60]}")
    return errs


def validate_item(original: str, paras: list[str], mask: Mask, slots: int = 12, n: int = 9) -> list[str]:
    errs: list[str] = []
    if len(paras) != slots:
        errs.append(f"{len(paras)} paraphrases, {slots} required")
    for i, p in enumerate(paras):
        errs += [f"#{i}: {e}" for e in validate_paraphrase(original, p, mask, n)]
    dup = find_duplicates({str(i): [("b", p)] for i, p in enumerate(paras)}, n, mask)
    for k, runs in dup.items():
        errs.append(f"#{k} shares {runs[0]['words']} words with #{','.join(runs[0]['with'][:3])}: {runs[0]['text'][:60]}")
        break
    return errs


class Cards:
    """Renders knowledge-base values for the writer of one run: sentences by the paraphrase bank, unordered lists in the order of the run."""

    def __init__(self, kb: dict, mask: Mask, bank: dict, slot: int, seed: str, require: bool = False):
        self.kb, self.mask, self.bank, self.slot, self.seed, self.require = kb, mask, bank, slot, seed, require
        self.missing: dict[str, str] = {}
        self.used = 0

    def paraphrase(self, s: str) -> str | None:
        item = self.bank.get("items", {}).get(text_key(s))
        paras = item["paraphrases"] if item else []
        if paras:
            return paras[self.slot % len(paras)]
        self.missing[text_key(s)] = s
        if self.require:
            raise RuntimeError(f"no paraphrase in the bank for a sentence of the knowledge base: {s[:90]!r} (python -m textgen bank ...)")
        return None

    def _walk(self, node: Any, path: str, key: str) -> Any:
        if isinstance(node, str):
            if is_sentence(node):
                p = self.paraphrase(node)
                if p:
                    self.used += 1
                    return p
            return node
        if isinstance(node, dict):
            return {k: self._walk(v, f"{path}.{k}", k) for k, v in node.items()}
        if isinstance(node, list):
            items = [self._walk(v, f"{path}[{i}]", key) for i, v in enumerate(node)]
            if len(items) >= 3 and not ORDERED_KEY_RE.search(key) and not _ordered_items(node):
                random.Random(f"{self.seed}|{path}").shuffle(items)
            return items
        return node

    def render_value(self, path: str, value: Any) -> str:
        out = self._walk(value, path, path.split(".")[-1])
        return out if isinstance(out, str) else json.dumps(out, ensure_ascii=False, indent=None)

    def keep_line(self, value: Any) -> str:
        """Figures and protected names of the sentences of a value: they stay exact whatever the wording."""
        figs: list[str] = []
        names: list[str] = []
        for _, s in walk_leaves(value, ""):
            if is_sentence(s):
                f, p = must_keep(s, self.mask)
                figs += f
                names += p
        figs, names = list(dict.fromkeys(figs)), list(dict.fromkeys(names))
        return ("; keep exactly: " + ", ".join(figs[:10] + names[:6])) if figs or names else ""

    def header_pair(self) -> tuple[str, str]:
        return HEADER_PAIRS[self.slot % len(HEADER_PAIRS)]


def _ordered_items(items: list) -> bool:
    """A list of objects that carry a rank, a level, a step or a day is a sequence: never reordered."""
    return any(isinstance(x, dict) and any(ORDERED_KEY_RE.search(k) for k in x) for x in items)


def slot_of(brief: dict) -> int:
    v = brief.get("variant", {}).get("id", "") if isinstance(brief.get("variant"), dict) else ""
    m = re.search(r"(\d+)", v or "")
    return max(int(m.group(1)) - 1, 0) if m else 0
