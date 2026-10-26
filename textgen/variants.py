"""Step 1.8 - brief variants: several different ТЗ for the same input (uniqueness at the brief level).

One run of step 1 (competitor analysis, clusters, knowledge base) is shared. A blueprint (input/variants/<name>.json) describes how
each variant differs: the blocks and their order (merged, dropped, split, new ones), headings, sizes, formats, keyword placement,
entity priorities, fact-table rows, extra writing directions and the page angle/voice. This module composes real ТЗ blocks from the
blueprint and the base ТЗ, so everything that must stay true (verbatim knowledge-base facts, conflict rulings in the copywriter
notes, mandatory clusters, every knowledge-base variable used, the fact table in block 2 or 3) is inherited and re-checked with the
same `validate` as step 1. Keyword sentences of the notes are regenerated from the final counts.

Reads : runs/<base>/00_*.json, 01_*.json (step 1 of the base run) + the blueprint
Writes: runs/<base>-<variant id>/ (copies of the step 1 inputs, 01_brief.json, 01_brief.md, 01_variant.json, state.json)
"""
from __future__ import annotations

import json
import os
import re
import shutil
from itertools import combinations
from pathlib import Path

from . import brief as B
from . import store
from . import tiers as TIERS
from .config import RUNS_DIR, Settings
from .store import Run
from .textutil import count_keywords

COPY_FILES = [store.INPUT, store.KNOWLEDGE_BASE, store.COMPETITORS_RAW, store.KEYWORD_STATS, store.CLUSTERS, store.ENTITIES,
              store.FACT_TABLES, store.TIERS]
VARIANT = "01_variant.json"
MAX_ENTITIES = 10
MAX_CONNECTIONS = 4
KEYWORD_LABEL = {"Inca Spin": '"Inca Spin" (written as two words)', "Incaspin casino": '"Incaspin casino" (written as the name Incaspin Casino)'}

# A base block whose verbatim knowledge-base value contains the tracked keyword (e-mail, steps of the app installation): the block
# cannot go below that count. `replace` removes the old count statement from the base notes, `note` takes its place.
INTRINSIC: dict[str, dict] = {
    "b02": {"keyword": "Incaspin", "count": 1,
            "replace": [(', which is the one occurrence this block allows; no other tracked keyword here.', '.')],
            "note": 'The Support row prints the e-mail address exactly as given; it contains the tracked keyword "Incaspin", which counts toward the exact count of this block.'},
    "b18": {"keyword": "Incaspin", "count": 2,
            "drop_prefix": "Step one of each list uses the brand name",
            "note": 'Step one of the iOS list and of the Android list names the brand as in the Brand Information; these two occurrences of "Incaspin" are part of the exact count of this block, the rest goes into the running text.'},
    "b21": {"keyword": "Incaspin", "count": 1,
            "replace": [(' and is the one occurrence of "Incaspin" of this block.', '.')],
            "note": 'The e-mail address contains the tracked keyword "Incaspin"; it is part of the exact count of this block.'},
}

BRAND_NAMES = ["Incaspin Casino", "Incaspin"]  # removed from the notes of merged blocks (the notes must not carry the brand)


def configure(blueprint: dict) -> None:
    """A blueprint of another brand brings its own `intrinsic` rules (same shape as INTRINSIC, keyed by base block id), `brand_names`
    (longest first) and `keyword_labels`; without them the defaults above (Incaspin) stay."""
    if "intrinsic" in blueprint:
        INTRINSIC.clear()
        INTRINSIC.update(blueprint["intrinsic"])
    if "brand_names" in blueprint:
        BRAND_NAMES[:] = blueprint["brand_names"]
    if "keyword_labels" in blueprint:
        KEYWORD_LABEL.clear()
        KEYWORD_LABEL.update(blueprint["keyword_labels"])
    for rules in INTRINSIC.values():
        rules["replace"] = [tuple(r) for r in rules.get("replace", [])]


def _no_brand(heading: str) -> str:
    for name in BRAND_NAMES:
        heading = heading.replace(name, "the casino")
    return heading


SENTENCE = re.compile(r'(?<=[.!?])\s+(?=[A-Z"(])')


def _times(n: int) -> str:
    return {1: "once", 2: "twice", 3: "three times"}.get(n, f"{n} times")


def _replace_once(text: str, old: str, new: str, where: str) -> str:
    if old not in text:
        raise ValueError(f"{where}: text to replace not found: {old[:70]!r}")
    return text.replace(old, new, 1)


def clean_notes(block: dict) -> str:
    """Base copywriter notes without the keyword-count sentences (they are regenerated from the final counts). Everything else
    (conflict rulings, order of the argument, what to avoid) is kept."""
    text = block["copywriter_notes"]
    intr = INTRINSIC.get(block["id"], {})
    for old, new in intr.get("replace", []):
        text = _replace_once(text, old, new, f'{block["id"]} notes')
    out: list[str] = []
    for s in SENTENCE.split(text):
        if intr.get("drop_prefix") and s.startswith(intr["drop_prefix"]):
            continue
        if s.startswith('Use "') and " exactly " in s:  # 'Use "Incaspin" exactly twice ...; do not ...' -> keep what follows ';'
            tail = s.split(";", 1)[1].strip() if ";" in s else ""
            if tail:
                out.append(tail[0].upper() + tail[1:])
            continue
        out.append(s)
    return " ".join(out)


def keyword_sentence(kw: dict[str, int], formats: list[str], notes: list[str], lists_ok: bool, tail: str) -> str:
    used = [(k, n) for k, n in kw.items() if n]
    if not used:
        s = "Use no tracked keyword in the body of this block."
    else:
        parts = [f'{KEYWORD_LABEL.get(k, chr(34) + k + chr(34))} exactly {_times(n)}' for k, n in used]
        s = "Use " + (", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else parts[0])
        s += "." if len(used) == len(kw) else ", and no other tracked keyword."
    if not lists_ok and ({"list", "table"} & set(formats)) and used:
        s += " Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them."
    return " ".join([s, *notes, tail]).strip()


def _union(lists: list[list]) -> list:
    return list(dict.fromkeys(x for l in lists for x in l))


def _entities(spec: dict, srcs: list[dict]) -> list[dict]:
    ents: dict[str, int] = {}
    for s in srcs:
        for e in s["entities"]:
            ents[e["name"]] = max(ents.get(e["name"], 0), int(e["priority"]))
    if spec.get("entities"):
        ents = {n: int(p) for n, p in spec["entities"]}
    for n, p in spec.get("entities_add", []):
        ents[n] = int(p)
    for n in spec.get("ent_drop", []):
        if n not in ents:
            raise ValueError(f'{spec["heading"]}: ent_drop {n!r} is not an entity of the block')
        del ents[n]
    for n, p in spec.get("ent_prio", {}).items():
        if n not in ents:
            raise ValueError(f'{spec["heading"]}: ent_prio {n!r} is not an entity of the block')
        ents[n] = int(p)
    items = list(ents.items())
    keep = spec.get("ent_top", MAX_ENTITIES)
    if len(items) > keep:  # the highest priorities stay, in their original order
        cut = sorted(items, key=lambda x: -x[1])[:keep]
        items = [x for x in items if x in cut]
    return [{"name": n, "priority": p} for n, p in items]


def _connections(spec: dict, srcs: list[dict]) -> list[dict]:
    if spec.get("connections"):
        conns = [{"subject": a, "relation": r, "object": c, "priority": int(p)} for a, r, c, p in spec["connections"]]
    else:
        conns = _union([[json.dumps(c, sort_keys=True) for c in s["entity_connections"]] for s in srcs])
        conns = [json.loads(c) for c in conns]
    conns += [{"subject": a, "relation": r, "object": c, "priority": int(p)} for a, r, c, p in spec.get("connections_add", [])]
    keep = sorted(conns, key=lambda c: -c["priority"])[: spec.get("conn_top", MAX_CONNECTIONS)]
    return [c for c in conns if c in keep]


def _fact_rows(spec: dict, base_rows: list[dict]) -> list[dict]:
    by_key = {r["key"]: r for r in base_rows}
    rows = []
    for item in spec["fact_rows"]:
        if isinstance(item, str):
            item = {"key": item}
        base = by_key.get(item["key"], {}) if item["key"] != "other" else {}
        row = {"key": item["key"], "label": item.get("label", base.get("label", "")), "kb_refs": item.get("kb_refs", base.get("kb_refs", []))}
        if not row["kb_refs"]:
            raise ValueError(f'fact row {item}: no kb_refs (unknown base row?)')
        rows.append(row)
    return rows


def compose_block(spec: dict, base_by_id: dict[str, dict], keywords: list[str], settings: Settings) -> dict:
    srcs = [base_by_id[i] for i in spec.get("from", [])]
    where = spec["heading"]
    new = not srcs
    if new and not all(spec.get(k) for k in ("entities", "connections", "kb_refs", "notes", "summary")):
        raise ValueError(f"{where}: a new block needs entities, connections, kb_refs, notes and summary")
    mid = spec["words"]
    kw = {k: int(spec.get("kw", {}).get(k, 0)) for k in keywords}
    formats = spec.get("formats") or [f for f in B.FORMATS if any(f in s["formats"] for s in srcs)] or ["paragraph"]
    intr = [INTRINSIC[s["id"]] for s in srcs if s["id"] in INTRINSIC]
    for it in intr:
        if kw[it["keyword"]] < it["count"]:
            raise ValueError(f'{where}: needs "{it["keyword"]}" ×{it["count"]} at least (verbatim value of the knowledge base), got {kw[it["keyword"]]}')

    if spec.get("notes"):
        text = spec["notes"].strip()
    else:
        parts = [clean_notes(s) for s in srcs]
        if len(parts) == 1:
            text = parts[0]
        else:
            label = _no_brand  # notes must not carry the brand
            text = ("This block covers several topics in ONE continuous section without sub-headings, in this order, each topic in "
                    "proportion to its share of the block. " + " ".join(f'({i}) {label(s["heading"])}: {p}' for i, (s, p) in enumerate(zip(srcs, parts), 1)))
        for old, newtext in spec.get("edit", []):
            text = _replace_once(text, old, newtext, f"{where} edit")
    if spec.get("extra"):
        text += " Variant direction: " + spec["extra"].strip()
    notes = keyword_sentence(kw, formats, [it["note"] for it in intr], bool(spec.get("kw_lists_ok")), spec.get("kw_tail", ""))
    text = f"{text} {notes}"

    b = {
        "id": "", "level": spec["level"], "heading": spec["heading"],
        "source": spec.get("source") or ("unique" if new else ("mandatory" if any(s["source"] == "mandatory" for s in srcs) else srcs[0]["source"])),
        "covers_clusters": _union([s["covers_clusters"] for s in srcs]) + spec.get("covers_clusters", []),
        "kb_refs": [p for p in (spec["kb_refs"] if new else _union([s["kb_refs"] for s in srcs]) + spec.get("refs_add", []))
                    if p not in spec.get("refs_drop", [])],
        "words_min": round(mid * (1 - settings.range_width)), "words_max": round(mid * (1 + settings.range_width)),
        "keywords": kw,
        "entities": _entities(spec, srcs), "entity_connections": _connections(spec, srcs),
        "listed_entities": [n for n in _union([s["listed_entities"] for s in srcs]) + spec.get("listed_entities", [])],
        "summary": spec.get("summary") or srcs[0]["summary"], "copywriter_notes": text, "formats": formats,
        "variant_origin": [s["id"] for s in srcs] or ["new"],
    }
    if spec.get("fact_rows"):
        b["fact_table"] = _fact_rows(spec, next(s for s in srcs if s.get("fact_table"))["fact_table"])
        b["kb_refs"] = []  # the paths of the rows are added by the knowledge-base attachment
    return b


TIER_DEFAULTS = {  # entities / connections kept per block unless the blueprint says otherwise: the small text cuts them to the minimum
    # (a connection costs 15 words of the block, an entity none, but the writer has to name it)
    "small": {"ent_top": 3, "conn_top": 1}, "medium": {"ent_top": 4, "conn_top": 2}, "large": {"ent_top": 6, "conn_top": 3}}


def variant_tier(base: dict, spec: dict) -> tuple[str, dict | None]:
    """(name, group) of the size group of a variant: `tier` of the blueprint, else the one of the base ТЗ. The group carries the target
    (mean of the competitors of the group) and the limit of the whole text; None for a base ТЗ made before the groups existed."""
    name = spec.get("tier") or base.get("targets", {}).get("tier", TIERS.BASE)
    groups = base.get("targets", {}).get("tiers", {}).get("tiers", {})
    if groups and name not in groups:
        raise ValueError(f'{spec["id"]}: the base ТЗ has no size group "{name}" (it has: {", ".join(groups)})')
    return name, groups.get(name)


def build_variant(base: dict, spec: dict, kb: dict, keywords: list[str], settings: Settings, clusters: list[dict]) -> tuple[dict, dict, list[str]]:
    base_by_id = {b["id"]: b for b in base["blocks"]}
    tier, group = variant_tier(base, spec)
    defaults = TIER_DEFAULTS[tier] if group else {}  # a base ТЗ made before the groups existed keeps the old behaviour
    blocks = [compose_block({**defaults, **bs}, base_by_id, keywords, settings) for bs in spec["blocks"]]
    brief = {"intent_summary": spec["intent_summary"], "blocks": blocks}
    page_type = base.get("page_type", "brand-review")
    if page_type != "brand-review":  # the clusters the base left out stay out unless the variant says otherwise
        brief["skipped_clusters"] = spec.get("skipped_clusters", base.get("skipped_clusters", []))
    brief = B.normalize(brief, keywords, kb)
    targets = {"target_body_words": sum(b["words"] for b in blocks),
               **({"competitor_body_words": group["target"], "max_body_words": group["limit"], "tier": tier, "tiers": base["targets"]["tiers"]} if group
                  else {k: base["targets"][k] for k in ("competitor_body_words", "max_body_words") if k in base.get("targets", {})}),  # older base ТЗ
               "keyword_targets": B.keyword_totals(brief, keywords)}
    errs = B.validate(brief, targets, keywords, settings, clusters, kb, page_type)
    total = targets["target_body_words"]
    for k, n in targets["keyword_targets"].items():
        if n < 1:
            errs.append(f'keyword "{k}" is not used anywhere')
    if sum(targets["keyword_targets"].values()) > total * settings.max_keyword_density:
        errs.append(f'keywords {sum(targets["keyword_targets"].values())} in {total} words: denser than {settings.max_keyword_density:.0%}')
    return brief, targets, errs


def write_variant(base_run: Run, spec: dict, settings: Settings, force: bool = False) -> dict:
    slug = f'{base_run.path.name}-{spec["id"]}'
    path = RUNS_DIR / slug
    if (path / store.BLOCKS).exists() and not force:
        raise RuntimeError(f"{slug}: text generation already started (02_blocks.json exists); use --force to rebuild the brief")
    run = Run(path)
    for name in COPY_FILES:
        if (base_run.path / name).exists() or name != store.TIERS:
            shutil.copyfile(base_run.path / name, path / name)
    kb = run.knowledge_base()
    job = run.job()
    clusters = run.load_json(store.CLUSTERS)
    base = base_run.load_json(store.BRIEF)
    brief, targets, errs = build_variant(base, spec, kb, job.keywords, settings, clusters)
    if errs:
        run.save_json(store.BRIEF, {"targets": targets, "brief": brief, "validation_errors": errs})
        raise RuntimeError(f"{slug}: ТЗ did not pass validation:\n- " + "\n- ".join(errs))
    budget = B.apply_coverage_budget(brief, targets, settings)
    result = {
        "geo": job.geo, "language": job.language, "keywords": job.keywords, "targets": targets, "brand": job.brand_name,
        "knowledge_base": {"id": kb["id"], "title": kb["title"]}, "intent_summary": brief["intent_summary"], "blocks": brief["blocks"],
        "review_issues": [], "coverage_budget": budget,
        **({} if job.page_type == "brand-review" else {"page_type": job.page_type, "skipped_clusters": brief.get("skipped_clusters", [])}),
        "variant": {"id": spec["id"], "name": spec["name"], "base_run": base_run.path.name, "angle": spec.get("angle", ""), "tier": targets.get("tier")},
    }
    run.save_json(store.BRIEF, result)
    run.save_json(VARIANT, spec)
    run.save_text(store.BRIEF_MD, B.render_markdown(
        brief, {"geo": job.geo, "language": job.language, "knowledge_base": kb["title"], "page_type": job.page_type}, targets))
    run.mark("step1", "done", blocks=len(brief["blocks"]), variant=spec["id"])
    return result


# ---------------------------------------------------------------- comparison

def _words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower())) - {"and", "the", "at", "of", "in", "to", "for", "a", "with"}


def _lcs(a: list[str], b: list[str]) -> int:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            dp[i + 1][j + 1] = dp[i][j] + 1 if x == y else max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]


def _facts(briefs: dict[str, dict]) -> dict[str, dict]:
    out = {}
    for vid, r in briefs.items():
        bl = r["blocks"]
        out[vid] = {
            "blocks": len(bl), "h2": sum(b["level"] == 2 for b in bl), "h3": sum(b["level"] == 3 for b in bl),
            "words": r["targets"]["target_body_words"], "base_words": r["targets"].get("base_body_words"),
            "limit": r["targets"].get("max_body_words"), "tier": r["targets"].get("tier"),
            "range": (sum(b["words_min"] for b in bl), sum(b["words_max"] for b in bl)),
            "tables": sum("table" in b["formats"] for b in bl), "lists": sum("list" in b["formats"] for b in bl),
            "prose_only": sum(b["formats"] == ["paragraph"] for b in bl),
            "fact_pos": next((i + 1 for i, b in enumerate(bl) if b.get("fact_table")), "-"),  # a brand-subpage has no fact table
            "fact_rows": len(next((b for b in bl if b.get("fact_table")), {"fact_table": []})["fact_table"]),
            "kw": r["targets"]["keyword_targets"], "headings": [b["heading"] for b in bl],
            "origin": [b["variant_origin"][0] for b in bl],
            "formats": {b["variant_origin"][0]: tuple(sorted(b["formats"])) for b in bl if b["variant_origin"][0] != "new"},
            "levels": {b["variant_origin"][0]: b["level"] for b in bl if b["variant_origin"][0] != "new"},
        }
    return out


def topic_set(brief: dict) -> set[str]:
    """The topics a variant covers: every base block it draws on (merged blocks count for each source) and every new block (by heading).
    Reordering, renaming and merging do not change this set, so two variants with the same set have the same structure."""
    out: set[str] = set()
    for b in brief["blocks"]:
        origin = b.get("variant_origin") or ["new"]
        out |= {f'new:{" ".join(sorted(_words(b["heading"])))}'} if origin == ["new"] else set(origin)
    return out


MIN_STRUCT_DISTANCE = float(os.environ.get("TEXTGEN_MIN_STRUCT_DISTANCE", "2.0"))  # structure distance that two variants must reach
# weights of the depth difference of one shared topic (they sum to 1: a topic that differs in everything counts as one topic)
DEPTH_WEIGHTS = {"facts": 0.4, "format": 0.25, "size": 0.25, "level": 0.1}
SIZE_FULL_DIFF = 0.4  # a block that is 40% smaller than the other differs completely in size


def topic_profile(brief: dict, base: dict | None = None) -> dict[str, dict]:
    """Per topic of a variant: how deep it is covered. `facts` = the knowledge-base paths of the block that belong to the topic (all paths of
    the block when no base ТЗ is given), `format`, `words` (the middle of the range; a merged block shares it between its topics) and `level`.
    A welcome-bonus block with only the amount and one with the amount, the conditions and the claiming steps are the same topic at two depths."""
    base_refs = {b["id"]: set(b.get("kb_refs", [])) for b in (base or {}).get("blocks", [])}
    out: dict[str, dict] = {}
    for b in brief["blocks"]:
        origin = b.get("variant_origin") or ["new"]
        mid = (b["words_min"] + b["words_max"]) / 2
        refs = set(b.get("kb_refs", []))
        for o in origin:
            key = f'new:{" ".join(sorted(_words(b["heading"])))}' if o == "new" else o
            facts = refs & base_refs[o] if o in base_refs else refs
            out[key] = {"facts": facts, "format": tuple(sorted(b["formats"])), "words": mid / len(origin), "level": b["level"]}
    return out


def depth_difference(a: dict, b: dict) -> tuple[float, list[str]]:
    """0..1 difference in depth between two coverings of one topic, and what differs."""
    parts: dict[str, float] = {}
    union = a["facts"] | b["facts"]
    parts["facts"] = 1 - len(a["facts"] & b["facts"]) / len(union) if union else 0.0
    parts["format"] = float(a["format"] != b["format"])
    lo, hi = sorted((a["words"], b["words"]))
    parts["size"] = min(1.0, (1 - lo / hi) / SIZE_FULL_DIFF) if hi else 0.0
    parts["level"] = float(a["level"] != b["level"])
    notes = [f'{k} {v:.0%}' for k, v in parts.items() if v]
    return sum(DEPTH_WEIGHTS[k] * v for k, v in parts.items()), notes


def structure_distance(pa: dict[str, dict], pb: dict[str, dict]) -> tuple[float, int, float, list[str]]:
    """(total, topics only one of the two covers, depth difference summed over the shared topics, the shared topics that differ most).
    One topic that only one variant has counts 1; a shared topic that differs in facts, format, size and level counts up to 1."""
    only = len(pa.keys() ^ pb.keys())
    diffs = {t: depth_difference(pa[t], pb[t]) for t in pa.keys() & pb.keys()}
    depth = sum(d for d, _ in diffs.values())
    top = [f'{t}: {", ".join(n)}' for t, (d, n) in sorted(diffs.items(), key=lambda x: -x[1][0]) if d >= 0.3][:4]
    return only + depth, only, depth, top


def structure_conflicts(briefs: dict[str, dict], base: dict | None = None, min_distance: float = MIN_STRUCT_DISTANCE) -> list[str]:
    """Pairs of variants whose structure distance (topics that only one covers + depth differences of the shared topics) is below
    `min_distance`: the texts would have the same structure under other headings. Give one of them a topic the other lacks, or cover the
    shared topics at another depth (other facts of the knowledge base, another format, another size)."""
    prof = {vid: topic_profile(r, base) for vid, r in briefs.items()}
    out = []
    for a, b in combinations(prof, 2):
        total, only, depth, _ = structure_distance(prof[a], prof[b])
        if total < min_distance:
            out.append(f"{a} / {b}: structure distance {total:.1f} < {min_distance:g} ({only} topics only one covers, depth difference of the shared topics {depth:.1f})")
    return out


def compare(briefs: dict[str, dict], base: dict | None = None) -> str:
    """Markdown report: what differs between the variants (size, structure, formats, keywords) and how similar each pair is."""
    f = _facts(briefs)
    ids = list(f)
    rows = ["| | " + " | ".join(ids) + " |", "|---|" + "---|" * len(ids)]

    def line(label: str, fn) -> None:
        rows.append(f"| {label} | " + " | ".join(str(fn(f[i])) for i in ids) + " |")

    line("blocks (H2 / H3)", lambda x: f'{x["blocks"]} ({x["h2"]} / {x["h3"]})')
    line("body words (before -> after coverage budget)", lambda x: f'{x["base_words"]} -> {x["words"]}')
    line("sum of ranges", lambda x: f'{x["range"][0]}-{x["range"][1]}')
    line("size group, limit of the whole text", lambda x: f'{x["tier"] or "-"}, {x["limit"] or "-"}')
    line("blocks with a table / a list / prose only", lambda x: f'{x["tables"]} / {x["lists"]} / {x["prose_only"]}')
    line("fact table: position, rows", lambda x: f'{x["fact_pos"]}, {x["fact_rows"]}')
    for k in next(iter(f.values()))["kw"]:
        line(f"keyword «{k}» (total)", lambda x, k=k: x["kw"][k])
    pair = ["| pair | headings in common | same order of topics | different formats / levels on shared topics | size ratio |", "|---|---|---|---|---|"]
    for a, b in combinations(ids, 2):
        ha, hb = {" ".join(sorted(_words(h))) for h in f[a]["headings"]}, {" ".join(sorted(_words(h))) for h in f[b]["headings"]}
        same_head = len(ha & hb) / max(1, min(len(ha), len(hb)))
        order = _lcs(f[a]["origin"], f[b]["origin"]) / max(1, min(len(f[a]["origin"]), len(f[b]["origin"])))
        size = min(f[a]["words"], f[b]["words"]) / max(f[a]["words"], f[b]["words"])
        shared = f[a]["formats"].keys() & f[b]["formats"].keys()
        fmt = sum(f[a]["formats"][i] != f[b]["formats"][i] for i in shared) / max(1, len(shared))
        lvl = sum(f[a]["levels"][i] != f[b]["levels"][i] for i in shared) / max(1, len(shared))
        pair.append(f"| {a} / {b} | {same_head:.0%} | {order:.0%} | {fmt:.0%} / {lvl:.0%} | {size:.2f} |")
    conflicts = structure_conflicts(briefs, base)
    prof = {i: topic_profile(briefs[i], base) for i in ids}
    dist = ["| pair | distance | topics only one covers | depth difference of the shared topics | shared topics that differ most |", "|---|---|---|---|---|"]
    for a, b in combinations(ids, 2):
        total, only, depth, top = structure_distance(prof[a], prof[b])
        dist.append(f'| {a} / {b} | {total:.1f}{" **TOO CLOSE**" if total < MIN_STRUCT_DISTANCE else ""} | {only} | {depth:.1f} | {"; ".join(top) or "-"} |')
    out = ["# Brief variants: comparison", "", *rows, "", *pair, "",
           f"## Structure distance (every pair must reach {MIN_STRUCT_DISTANCE:g}: 1 per topic only one variant covers, up to 1 per shared topic "
           "for other facts / format / size / level)", "", *dist, "",
           *(f"- CONFLICT {c}" for c in conflicts), *([] if conflicts else ["- every pair is far enough apart"]), "", "## Headings", ""]
    for i in ids:
        out += [f"**{i}**", "", *[f'{"  " * (b["level"] - 1)}- H{b["level"]} {b["heading"]}' for b in briefs[i]["blocks"]], ""]
    return "\n".join(out)
