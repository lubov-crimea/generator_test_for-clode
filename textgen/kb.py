"""AffBulk knowledge base (brand information) support.

The knowledge base is selected by name in the input file (`Knowledge Base - incaspin-new`) and fetched from AffBulk through MCP
(`knowledge_bases_find`) by Claude Code - Python cannot call MCP - and saved as runs/<run>/00_knowledge_base.json:

    {"id": 556, "title": "incaspin-new", "category": "brand-data",
     "variables": [{"key": "brandinfo_welcome", "type": "json", "value": <parsed JSON or text>}, ...]}

The ТЗ points to facts by PATH (`brandinfo_welcome.welcome_bonus.total_bonus`, `brandinfo_deposit.deposit_methods[0]`) and the code
inserts the VALUE verbatim, so the text of the knowledge base is never retyped or paraphrased by a model.
"""
from __future__ import annotations

import json
import re
from typing import Any

TOKEN_RE = re.compile(r"([^.\[\]]+)|\[(\d+)\]")


def load(raw: dict) -> dict:
    """Normalise a knowledge base: variables as {key: parsed value}. Accepts values that are JSON strings (as AffBulk returns them)."""
    out: dict[str, Any] = {}
    for v in raw["variables"]:
        val = v["value"]
        if v.get("type") == "json" and isinstance(val, str):
            val = json.loads(val)
        out[v["key"]] = val
    return {"id": raw.get("id"), "title": raw["title"], "category": raw.get("category"), "variables": out}


def merge(parts: dict[str, dict], title: str) -> dict:
    """The knowledge bases of the casinos of a top list as ONE knowledge base: the top-level keys are the casino slugs, so a path
    starts with the casino (`incaspin.brandinfo_welcome.welcome_bonus.total_bonus`) and `variable_of(path)` names the casino.
    `parts` = slug -> loaded knowledge base (see `load`)."""
    return {"id": None, "title": title, "category": "top-list", "variables": {slug: kb["variables"] for slug, kb in parts.items()}}


def digest(node: Any, max_chars: int = 220, max_items: int = 12) -> Any:
    """The same structure with long texts cut and long lists shortened, so that several knowledge bases fit into one request.
    Paths stay valid (the first `max_items` items keep their indexes); the code still inserts the full values by path."""
    if isinstance(node, dict):
        return {k: digest(v, max_chars, max_items) for k, v in node.items()}
    if isinstance(node, list):
        items = [digest(v, max_chars, max_items) for v in node[:max_items]]
        return items + ([f"... {len(node) - max_items} more items (indexes {max_items}-{len(node) - 1})"] if len(node) > max_items else [])
    if isinstance(node, str) and len(node) > max_chars:
        return node[:max_chars].rstrip() + "..."
    return node


def resolve(kb: dict, path: str) -> Any:
    """Value at `path`. Raises KeyError with a readable message when the path does not exist."""
    tokens = [(m.group(1), m.group(2)) for m in TOKEN_RE.finditer(path)]
    if not tokens or tokens[0][0] is None:
        raise KeyError(f"bad path: {path}")
    node: Any = kb["variables"]
    walked = ""
    for name, idx in tokens:
        try:
            node = node[name] if name is not None else node[int(idx)]
        except (KeyError, IndexError, TypeError):
            raise KeyError(f'path not found: {path} (stopped after "{walked or "<root>"}")') from None
        walked += f".{name}" if name is not None else f"[{idx}]"
    return node


def leaf_paths(kb: dict, max_depth: int = 6) -> list[str]:
    """Every path that can be referenced (variables, objects and scalars) - handy for listing and tests."""
    paths: list[str] = []

    def walk(node: Any, prefix: str, depth: int) -> None:
        paths.append(prefix)
        if depth >= max_depth:
            return
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{prefix}.{k}", depth + 1)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{prefix}[{i}]", depth + 1)

    for key, val in kb["variables"].items():
        walk(val, key, 0)
    return paths


def variable_of(path: str) -> str:
    m = TOKEN_RE.match(path)
    return m.group(1) if m else ""


def attach_brand_info(brief: dict, kb: dict) -> list[str]:
    """For every block turn `kb_refs` into `brand_info` = [{path, value}] (verbatim). Returns unresolved paths."""
    bad: list[str] = []
    for b in brief["blocks"]:
        info = []
        for p in b.get("kb_refs", []):
            try:
                info.append({"path": p, "value": resolve(kb, p)})
            except KeyError as e:
                bad.append(f'{b["id"]}: {e.args[0]}')
        b["brand_info"] = info
        bad += attach_fact_rows(b, kb)
    return bad


def attach_fact_rows(b: dict, kb: dict) -> list[str]:
    """Fact-table rows of a block: every row's `kb_refs` become `values` = [{path, value}] (verbatim), and the paths are added
    to the block's `kb_refs`/`brand_info` so that one place lists everything the writer may use. Returns unresolved paths."""
    bad: list[str] = []
    known = {i["path"] for i in b["brand_info"]}
    for row in b.get("fact_table", []):
        row["values"] = []
        for p in row.get("kb_refs", []):
            try:
                value = resolve(kb, p)
            except KeyError as e:
                if p not in b.get("kb_refs", []):  # a ref listed in both places is reported once
                    bad.append(f'{b["id"]}: fact table row "{row.get("key")}": {e.args[0]}')
                continue
            row["values"].append({"path": p, "value": value})
            if p not in known:
                known.add(p)
                b.setdefault("kb_refs", []).append(p)
                b["brand_info"].append({"path": p, "value": value})
    return bad


def render_value(value: Any) -> str:
    return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=None)


def outline(kb: dict, depth: int = 2) -> dict:
    """Compact map of the knowledge base (variable -> top-level keys) for prompts and README output."""
    def keys(node: Any, d: int) -> Any:
        if isinstance(node, dict) and d > 0:
            return {k: keys(v, d - 1) for k, v in node.items()}
        if isinstance(node, list):
            return f"list[{len(node)}]"
        return type(node).__name__

    return {k: keys(v, depth) for k, v in kb["variables"].items()}
