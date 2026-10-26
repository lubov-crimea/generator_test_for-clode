"""Sibling texts: the other runs of the same brand, GEO and knowledge base. Their finished (or being written) texts are the corpus a text must
not duplicate (shingles.py): other variants of the same page, other page types of the brand and the home pages of the same site set."""
from __future__ import annotations

import json
from pathlib import Path

from . import store
from .inputs import Job


def _identity(path: Path) -> tuple | None:
    p = path / store.INPUT
    if not p.exists():
        return None
    job = Job(**json.loads(p.read_text(encoding="utf-8")))
    return (job.brand_name, job.geo, job.knowledge_base or "", job.language or "")


def text_of_run(path: Path) -> list[tuple[str, str]] | None:
    """[(block label, heading + body)] of a run: the finished text (04_final.json) or the text being written (02_blocks.json)."""
    final = path / store.FINAL_JSON
    if final.exists():
        blocks = json.loads(final.read_text(encoding="utf-8"))["blocks"]
        return [(f"b{i + 1:02d} {b['heading']}", b["heading"] + "\n\n" + b["text"]) for i, b in enumerate(blocks)]
    drafts, brief = path / store.BLOCKS, path / store.BRIEF
    if drafts.exists() and brief.exists():
        state = json.loads(drafts.read_text(encoding="utf-8"))["blocks"]
        heads = {b["id"]: b["heading"] for b in json.loads(brief.read_text(encoding="utf-8"))["blocks"]}
        return [(f"{bid} {heads.get(bid, '')}", heads.get(bid, "") + "\n\n" + b.get("text", "")) for bid, b in state.items() if b.get("text")]
    return None


def sibling_names(run_path: Path, runs_dir: Path | None = None) -> list[str]:
    """Names of the other runs with the same brand, GEO, language and knowledge base that have a text (finished or in progress)."""
    base = runs_dir or run_path.parent  # the runs live side by side (tests use a temporary folder)
    me = _identity(run_path)
    if me is None or not me[0]:
        return []
    out = []
    for d in sorted(base.iterdir()):
        if d.is_dir() and d.resolve() != run_path.resolve() and not d.name.startswith("_") and _identity(d) == me and text_of_run(d):
            out.append(d.name)
    return out


def sibling_corpus(run_path: Path, runs_dir: Path | None = None) -> dict[str, list[tuple[str, str]]]:
    base = runs_dir or run_path.parent
    return {n: text_of_run(base / n) for n in sibling_names(run_path, runs_dir)}
