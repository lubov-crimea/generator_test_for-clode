"""The ТЗ (brief): numeric targets, schema, deterministic validation, rebalancing and a readable rendering."""
from __future__ import annotations

import math
import re
from typing import Any

from . import kb as KB
from . import tiers as TIERS
from .config import Settings
from .lang import check_language
from .sitemap import MAX_ANCHOR_WORDS, internal_link_note
from .textutil import count_keywords, count_words

FORMATS = ["paragraph", "list", "table"]
FORMAT_LABEL = {"list": "Bulleted/numbered list", "table": "Table"}

ENTITY_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "priority": {"type": "integer", "description": "1-10, how important the entity is for this block (10 = main)"},
    },
    "required": ["name", "priority"],
}
CONNECTION_SCHEMA = {
    "type": "object",
    "properties": {
        "subject": {"type": "string"},
        "relation": {"type": "string", "description": "verb phrase, e.g. offers, requires, regulates"},
        "object": {"type": "string"},
        "priority": {"type": "integer", "description": "1-10"},
    },
    "required": ["subject", "relation", "object", "priority"],
}

# The page always carries ONE brand fact sheet: a short "label | value" table that follows the introduction (block 2 or 3).
FACT_ROW_KEYS = ["company", "licence", "founded", "languages", "currencies", "payment_methods", "welcome_bonus", "cashback",
                 "min_deposit", "support", "other"]
REQUIRED_FACT_ROWS = ["licence", "welcome_bonus", "cashback", "currencies", "languages", "payment_methods", "support"]
FACT_TABLE_BLOCK_INDEXES = (1, 2)  # 0-based: the 2nd or the 3rd block of the page (the H1 is the 1st)
FACT_TABLE_MAX_ROWS = 14
FACT_TABLE_VALUE_MAX_WORDS = 25  # a cell is a short fact, not a sentence

FACT_ROW_SCHEMA = {
    "type": "object",
    "properties": {
        "key": {"type": "string", "enum": FACT_ROW_KEYS, "description": "kind of fact; 'other' for rows beyond the standard kinds"},
        "label": {"type": "string", "description": "row label, short, ALWAYS in English (localized by the writer)"},
        "kb_refs": {"type": "array", "items": {"type": "string"},
                    "description": "knowledge-base paths the value of this row is built from (narrowest useful path, at least one)"},
    },
    "required": ["key", "label", "kb_refs"],
}

BLOCK_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "description": "b01, b02, ... in page order"},
        "level": {"type": "integer", "description": "1 for H1, 2-6 for H2-H6"},
        "heading": {"type": "string", "description": "working heading of the block, ALWAYS in English; localized for the page in step 2"},
        "heading_keywords": {"type": "object", "additionalProperties": {"type": "integer"},
                             "description": "how many times each tracked keyword must appear in the (localized) page heading; omit if the English heading already contains them"},
        "source": {"type": "string", "enum": ["h1", "mandatory", "unique"]},
        "covers_clusters": {"type": "array", "items": {"type": "string"}},
        "kb_refs": {"type": "array", "items": {"type": "string"},
                    "description": "paths into the brand knowledge base (e.g. brandinfo_welcome.welcome_bonus.total_bonus) whose values this block must use; empty if there is no knowledge base"},
        "words_min": {"type": "integer", "description": "lower bound of body words, heading excluded"},
        "words_max": {"type": "integer", "description": "upper bound of body words, heading excluded"},
        "keywords": {"type": "object", "additionalProperties": {"type": "integer"}, "description": "keyword -> exact times in the body, all keywords listed"},
        "entities": {"type": "array", "items": ENTITY_SCHEMA, "description": "entities this block must cover, with priority"},
        "entity_connections": {"type": "array", "items": CONNECTION_SCHEMA, "description": "relations between entities that the text must state"},
        "listed_entities": {"type": "array", "items": {"type": "string"},
                            "description": "names (exactly as in `entities`) of the entities the text only lists as items of a list or table of this block; "
                                           "they need no explanation of their own"},
        "fact_table": {"type": "array", "items": FACT_ROW_SCHEMA,
                       "description": "ONLY for the brand fact sheet block (block 2 or 3 of the page, level 2, format table): its rows in page order. "
                                      "Omit for every other block."},
        "summary": {"type": "string", "description": "what the block says, 1-3 sentences"},
        "copywriter_notes": {"type": "string", "description": "binding instructions for the writer"},
        "formats": {"type": "array", "items": {"type": "string", "enum": FORMATS}},
    },
    "required": ["id", "level", "heading", "source", "words_min", "words_max", "keywords", "entities", "entity_connections",
                 "summary", "copywriter_notes", "formats"],
}

BRIEF_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "intent_summary": {"type": "string"},
        "blocks": {"type": "array", "items": BLOCK_SCHEMA},
        "skipped_clusters": {
            "type": "array",
            "description": "ONLY for brand-subpage and top-list pages: mandatory competitor clusters that do not belong to this page and are "
                           "deliberately not covered, each with the reason. Omit on a brand-review page.",
            "items": {
                "type": "object",
                "properties": {"id": {"type": "string"}, "reason": {"type": "string"}},
                "required": ["id", "reason"],
            },
        },
    },
    "required": ["intent_summary", "blocks"],
}

REVIEW_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"block_id": {"type": "string"}, "problem": {"type": "string"}, "fix": {"type": "string"}},
                "required": ["problem", "fix"],
            },
        },
        "blocks": {"type": "array", "items": BLOCK_SCHEMA},
    },
    "required": ["issues", "blocks"],
}


def block_range(b: dict) -> tuple[int, int]:
    """Allowed body length of a block, exactly as written in the ТЗ."""
    return b["words_min"], b["words_max"]


def block_cap(b: dict, settings: Settings) -> int:
    """Hard upper limit of a block: words_max plus the overflow the writer may use when facts, entities and style need the room."""
    return int(b["words_max"] * (1 + settings.words_overflow))


def _leaves(value: Any) -> list[str]:
    if isinstance(value, dict):
        return [t for v in value.values() for t in _leaves(v)]
    if isinstance(value, list):
        return [t for v in value for t in _leaves(v)]
    return [str(value)]


def value_words(value: Any) -> int:
    """Words of a knowledge-base value as the text would copy it (a figure or a name is one word, a list is the sum of its items)."""
    return count_words(" ".join(_leaves(value)))


def fact_words(value: Any, b: dict, settings: Settings) -> int:
    """Words the text needs to state one knowledge-base item. The length of the value decides: a short scalar fact (a figure, a name)
    takes `fact_min_words`, a longer one `fact_text_factor` words of prose per word of the value, but never more than `fact_max_words`
    (a long list is shortened). What a list or a table of the block shows item by item costs the words of the items themselves
    (factor 1, up to a third more than the cap for a big structure): the enumeration needs no sentences around it."""
    formats = set(b["formats"])
    shown = bool({"list", "table"} & formats) and isinstance(value, (list, dict))
    factor = 1.0 if shown or "paragraph" not in formats else settings.fact_text_factor
    cap = round(settings.fact_max_words * 4 / 3) if shown else settings.fact_max_words
    return max(settings.fact_min_words, min(cap, round(value_words(value) * factor)))


def coverage_need(b: dict, settings: Settings) -> dict:
    """Words a block needs for what it has to say: its knowledge-base facts (`fact_words` each) and its entity connections
    (`words_per_connection` each). The entities to cover take no words of their own: they are named inside those sentences."""
    facts = sum(fact_words(i["value"], b, settings) for i in b.get("brand_info", []))
    conns = settings.words_per_connection * len(b.get("entity_connections", []))
    return {"facts": facts, "connections": conns, "need": facts + conns}


def plan_budget(brief: dict, settings: Settings) -> list[dict]:
    """The size of every block once its facts and connections are planned in (nothing is changed). The competitor-based range
    (`words_base`, else the current range of the ТЗ) is the base; a block whose need is above the middle of the base moves up to
    `need` +-`range_width` (12%), but both bounds grow by at most `max_growth` (20%) over the base and never shrink. A block that
    needs more than the growth allows is `overloaded`: its facts and connections do not fit and must be cut or shown in a list or
    a table. A table-only block and the brand fact sheet keep their base: their cells are short."""
    rows: list[dict] = []
    grow = 1 + settings.max_growth
    for b in brief["blocks"]:
        base = list(b.get("words_base") or (b["words_min"], b["words_max"]))
        need = coverage_need(b, settings)
        mid = (base[0] + base[1]) / 2
        row = {"id": b["id"], "heading": b["heading"], **need, "base": base, "to": list(base), "ceiling": round(mid * grow), "overloaded": False}
        if set(b["formats"]) != {"table"} and not b.get("fact_table") and need["need"] > mid:
            lo, hi = round(need["need"] * (1 - settings.range_width)), round(need["need"] * (1 + settings.range_width))
            row["to"] = [max(base[0], min(lo, round(base[0] * grow))), max(base[1], min(hi, round(base[1] * grow)))]
            row["overloaded"] = need["need"] > mid * grow
        rows.append(row)
    return rows


def apply_coverage_budget(brief: dict, targets: dict, settings: Settings) -> list[dict]:
    """Size every block by what it has to say (see `plan_budget`). Returns one report row per changed block;
    `targets['target_body_words']` becomes the new total, the old one is kept as `base_body_words`."""
    report: list[dict] = []
    for b, row in zip(brief["blocks"], plan_budget(brief, settings)):
        b["coverage_words"] = {"facts": row["facts"], "connections": row["connections"], "need": row["need"]}
        b["words_base"] = row["base"]
        if row["to"] == row["base"]:
            continue
        b["words_min"], b["words_max"] = row["to"]
        b["words"] = round((b["words_min"] + b["words_max"]) / 2)
        report.append({"id": b["id"], "heading": b["heading"], "facts": row["facts"], "connections": row["connections"],
                       "need": row["need"], "from": row["base"], "to": row["to"]})
    targets.setdefault("base_body_words", targets["target_body_words"])
    targets["target_body_words"] = sum(b["words"] for b in brief["blocks"])
    return report


def compute_targets(stats: dict, keywords: list[str], settings: Settings, words_override: int | None = None, tier: str = TIERS.BASE) -> dict:
    """Total body length and total keyword counts for the new text. The length comes from the size group `tier` of the competitors
    (textgen/tiers.py; the base ТЗ is built for `medium`): `target_body_words` is the mean of the group, `max_body_words` the limit of
    the whole text (the mean x 1.2; x 1.0 for the large group). `words_override` (the given length) replaces the groups."""
    agg = stats["aggregate"]
    tiers = TIERS.build_tiers([r["body_words"] for r in stats["competitors"]], settings, words_override)
    t = tiers["tiers"].get(tier) or tiers["tiers"][tiers["base"]]
    words = t["target"]
    kw = {k: max(1, agg["median_total"][k]) for k in keywords}
    cap = max(len(keywords), int(words * settings.max_keyword_density))
    total = sum(kw.values())
    if total > cap:  # competitors stuff keywords; do not copy it
        kw = {k: max(1, round(v * cap / total)) for k, v in kw.items()}
    return {"target_body_words": words, "competitor_body_words": words, "max_body_words": t["limit"], "tier": tier if tier in tiers["tiers"] else tiers["base"],
            "tiers": tiers, "keyword_targets": kw}


def _limit_note(targets: dict) -> str:
    """'size group medium: competitor mean 844 x 1.2' for the messages and the rendered ТЗ."""
    mean, limit = targets.get("competitor_body_words"), targets.get("max_body_words")
    group = f'size group "{targets["tier"]}": ' if targets.get("tier") else ""
    return f"{group}competitor mean {mean} x {limit / mean:.1f}" if mean and limit else f"{group}competitor median"


def validate_budget(brief: dict, targets: dict, settings: Settings) -> list[str]:
    """The size rules of the ТЗ: no block whose facts and connections need more than the growth allows, and a page whose blocks
    (once planned in) stay within `max_body_words`, the limit of the size group of the ТЗ (textgen/tiers.py)."""
    errs: list[str] = []
    rows = plan_budget(brief, settings)
    for r in rows:
        if r["overloaded"]:
            errs.append(f'{r["id"]} "{r["heading"]}": its facts and connections need about {r["need"]} words ({r["facts"]} for the knowledge-base '
                        f'facts, {r["connections"]} for the entity connections) but the block can have {r["ceiling"]} at most (competitor-based size '
                        f'+{round(settings.max_growth * 100)}%): cut kb_refs and connections, or show enumerations in a list or a table')
    limit = targets.get("max_body_words")
    if limit:
        total = sum(r["to"][1] for r in rows)
        if total > limit:
            heavy = ", ".join(f'{r["id"]} {r["to"][1]}' for r in sorted(rows, key=lambda r: -r["to"][1])[:4])
            errs.append(f"the page would hold up to {total} words (sum of the block maxima once the facts are planned in), the limit is {limit} "
                        f"({_limit_note(targets)}): shorten or merge "
                        f"blocks, drop facts and connections; the largest blocks: {heavy}")
    return errs


def normalize(brief: dict, keywords: list[str], kb: dict | None = None) -> dict:
    """Make keyword dicts complete (all keywords present, ints), ids sequential, derived fields filled.
    With a knowledge base, `kb_refs` are resolved into `brand_info` (verbatim values)."""
    for i, b in enumerate(brief["blocks"], 1):
        b["id"] = f"b{i:02d}"
        b["level"] = int(b["level"])
        b["words_min"], b["words_max"] = int(b["words_min"]), int(b["words_max"])
        b["words"] = round((b["words_min"] + b["words_max"]) / 2)  # midpoint, used for totals
        b["keywords"] = {k: int(b.get("keywords", {}).get(k, 0)) for k in keywords}
        b.setdefault("covers_clusters", [])
        b.setdefault("entities", [])
        b.setdefault("entity_connections", [])
        b["listed_entities"] = [n for n in dict.fromkeys(b.get("listed_entities") or []) if n in {e["name"] for e in b["entities"]}]
        b["kb_refs"] = list(dict.fromkeys(b.get("kb_refs", [])))
        b["fact_table"] = [{"key": r.get("key", "other"), "label": str(r.get("label", "")).strip(),
                            "kb_refs": list(dict.fromkeys(r.get("kb_refs", [])))} for r in b.get("fact_table") or []]
        declared = b.get("heading_keywords") or count_keywords(b["heading"], keywords)
        b["heading_keywords"] = {k: int(declared.get(k, 0)) for k in keywords}
    brief["skipped_clusters"] = [{"id": str(s.get("id", "")).strip(), "reason": str(s.get("reason", "")).strip()}
                                 for s in brief.get("skipped_clusters") or []]
    brief["kb_unresolved"] = KB.attach_brand_info(brief, kb) if kb else []
    if not kb:
        for b in brief["blocks"]:
            b["brand_info"] = []
            for row in b["fact_table"]:
                row["values"] = []
    return brief


def brand_info_hazards(b: dict, keywords: list[str]) -> dict[str, int]:
    """Tracked keywords that occur INSIDE the block's knowledge-base facts (e.g. 'Incaspin Originals', 'incaspin.com',
    'support@incaspin.com'). Copying such text verbatim would add keyword occurrences, so the writer is warned."""
    text = "\n".join(KB.render_value(i["value"]) for i in b.get("brand_info", []))
    return {k: n for k, n in count_keywords(text, keywords).items() if n}


def fact_table_hazards(b: dict, keywords: list[str]) -> dict[str, int]:
    """Tracked keywords inside the VALUES of the fact-table rows (the support e-mail 'support@incaspin.com' contains 'Incaspin').
    The table has to print them, so the block must budget at least this many occurrences."""
    text = "\n".join(KB.render_value(v["value"]) for r in b.get("fact_table", []) for v in r.get("values", []))
    return {k: n for k, n in count_keywords(text, keywords).items() if n}


def validate_fact_table(blocks: list[dict], keywords: list[str]) -> list[str]:
    """The page always has exactly one brand fact sheet: block 2 or 3, H2, format table, rows built from the knowledge base."""
    errs: list[str] = []
    idx = [i for i, b in enumerate(blocks) if b.get("fact_table")]
    if not idx:
        return ["no fact table: the 2nd or the 3rd block of the page must be the brand fact sheet (H2, format table, `fact_table` rows)"]
    if len(idx) > 1:
        errs.append(f'only one block may have `fact_table`, found {len(idx)}: {", ".join(blocks[i]["id"] for i in idx)}')
    b = blocks[idx[0]]
    if idx[0] not in FACT_TABLE_BLOCK_INDEXES:
        errs.append(f'{b["id"]}: the fact table must be the 2nd or the 3rd block of the page, it is block {idx[0] + 1}')
    if b["level"] != 2:
        errs.append(f'{b["id"]}: the fact table block must be an H2, got H{b["level"]}')
    if "table" not in b["formats"]:
        errs.append(f'{b["id"]}: the fact table block must have the format "table"')
    rows = b["fact_table"]
    if len(rows) > FACT_TABLE_MAX_ROWS:
        errs.append(f'{b["id"]}: {len(rows)} fact table rows, at most {FACT_TABLE_MAX_ROWS}')
    keys = [r["key"] for r in rows]
    for key in REQUIRED_FACT_ROWS:
        if key not in keys:
            errs.append(f'{b["id"]}: the fact table has no "{key}" row (required rows: {", ".join(REQUIRED_FACT_ROWS)})')
    for key in set(keys):
        if key != "other" and keys.count(key) > 1:
            errs.append(f'{b["id"]}: fact table row "{key}" appears {keys.count(key)} times')
    for r in rows:
        if r["key"] not in FACT_ROW_KEYS:
            errs.append(f'{b["id"]}: unknown fact table row key "{r["key"]}" (allowed: {", ".join(FACT_ROW_KEYS)})')
        if not r["label"]:
            errs.append(f'{b["id"]}: fact table row "{r["key"]}" has no label')
        elif any(ord(c) > 127 and c.isalpha() for c in r["label"]):
            errs.append(f'{b["id"]}: fact table label "{r["label"]}" must be in English (the writer localizes it)')
        if not r["kb_refs"]:
            errs.append(f'{b["id"]}: fact table row "{r["label"] or r["key"]}" has no knowledge-base reference (kb_refs)')
    if b["words_max"] < 4 * len(rows):
        errs.append(f'{b["id"]}: words_max={b["words_max"]} is too small for {len(rows)} fact table rows (at least {4 * len(rows)})')
    for k, n in fact_table_hazards(b, keywords).items():
        if b["keywords"].get(k, 0) < n:
            errs.append(f'{b["id"]}: the fact table values contain the tracked keyword "{k}" {n} time(s) (e.g. the support e-mail), '
                        f'so the block\'s keywords must allow "{k}" at least {n} time(s), now {b["keywords"].get(k, 0)}')
    return errs


PAYMENT_HEADING_RE = re.compile(r"payment|deposit|banking|withdraw|cashier", re.IGNORECASE)
REGISTRATION_HEADING_RE = re.compile(r"regist|sign[- ]?up", re.IGNORECASE)
PROS_CONS_HEADING_RE = re.compile(r"\bpros\b|\bcons\b|advantage|disadvantage|benefit|drawback", re.IGNORECASE)


def validate_visuals(blocks: list[dict], page_type: str = "brand-review") -> list[str]:
    """Minimum of tables and lists: a payments table, a list of the registration steps, a table for pros and cons (when the page has
    such a block). The brand fact table is checked separately. Usage rules for lists and tables live in prompts/step1_brief.md.
    A top list compares casinos in its own comparison table, so a heading like "Fast withdrawal casinos" needs no payments table."""
    errs: list[str] = []
    pay = [b for b in blocks if PAYMENT_HEADING_RE.search(b["heading"]) and not b.get("fact_table")]
    if pay and page_type != "top-list" and not any("table" in b["formats"] for b in pay):
        errs.append(f'no payments table: one of the payment blocks ({", ".join(b["id"] for b in pay)}) must have the format "table" '
                    "(methods with limits and speed are 2+ attributes)")
    reg = [b for b in blocks if REGISTRATION_HEADING_RE.search(b["heading"])]
    if reg and not any("list" in b["formats"] for b in reg):
        errs.append(f'no registration steps list: one of the registration blocks ({", ".join(b["id"] for b in reg)}) must have the format "list" '
                    "(numbered steps)")
    for b in blocks:
        if PROS_CONS_HEADING_RE.search(b["heading"]) and "table" not in b["formats"] and not b.get("fact_table"):
            errs.append(f'{b["id"]}: the pros and cons block "{b["heading"]}" must have the format "table" (pros | cons)')
    return errs


SUBPAGE_MIN_KB_SHARE = 0.5  # a focused brand page: at least this share of the blocks carries brand facts
SKIPPED_CLUSTERS_MAX_SHARE = 0.5  # a subpage / top list may leave out at most this share of the mandatory clusters


def validate_subpage_kb(blocks: list[dict]) -> list[str]:
    """A focused page of a brand uses the part of the knowledge base that serves its topic, not all of it: the variables of other
    topics stay unused, but the page must stand on brand facts (at least half of the blocks refer to the knowledge base)."""
    need = math.ceil(len(blocks) * SUBPAGE_MIN_KB_SHARE)
    have = sum(1 for b in blocks if b.get("kb_refs"))
    if have < need:
        return [f"only {have} of {len(blocks)} blocks refer to the knowledge base (kb_refs): at least {need} blocks of a brand page must carry brand facts"]
    return []


def validate_top_list(blocks: list[dict], casinos: list[dict]) -> list[str]:
    """A top list: every casino has a section of its own (facts of this casino only), the sections follow the order of the input
    (that order is the ranking), and a comparison table with facts of ALL casinos is the 2nd or the 3rd block of the page."""
    errs: list[str] = []
    slugs = [c["slug"] for c in casinos]
    sources = [{KB.variable_of(p) for p in b.get("kb_refs", [])} for b in blocks]
    own: dict[str, list[int]] = {s: [i for i, src in enumerate(sources) if src == {s}] for s in slugs}
    for c in casinos:
        if not own[c["slug"]]:
            errs.append(f'casino "{c["name"]}" has no section of its own: add a block whose kb_refs all start with "{c["slug"]}."')
    firsts = [own[s][0] for s in slugs if own[s]]
    if firsts != sorted(firsts):
        errs.append("the casino sections must follow the order of the input (that order is the ranking): " + ", ".join(c["name"] for c in casinos))
    for i, b in enumerate(blocks):
        if sources[i] - set(slugs):
            errs.append(f'{b["id"]}: kb_refs must start with a casino slug ({", ".join(slugs)})')
    compare = [i for i, src in enumerate(sources) if src == set(slugs) and "table" in blocks[i]["formats"]]
    if not any(i in FACT_TABLE_BLOCK_INDEXES and blocks[i]["level"] == 2 for i in compare):
        errs.append("no comparison table: the 2nd or the 3rd block of the page must be an H2 with the format \"table\" whose kb_refs take "
                    "the facts of EVERY casino (one narrow path per casino and criterion)")
    return errs


def validate_skipped_clusters(brief: dict, clusters: list[dict]) -> list[str]:
    """A subpage / top list may skip a mandatory competitor cluster only with a reason, and not more than half of them."""
    blocks = brief["blocks"]
    covered = {c for b in blocks for c in b.get("covers_clusters", [])}
    skipped = {s["id"]: s["reason"] for s in brief.get("skipped_clusters", [])}
    mandatory = [c for c in clusters if c["mandatory"]]
    errs: list[str] = []
    left = [c for c in mandatory if c["id"] not in covered]
    for c in left:
        if not skipped.get(c["id"]):
            errs.append(f'mandatory cluster {c["id"]} "{c["canonical_title"]}" is not covered by any heading and not listed in `skipped_clusters` with a reason')
    if mandatory and len(left) > len(mandatory) * SKIPPED_CLUSTERS_MAX_SHARE:
        errs.append(f"{len(left)} of {len(mandatory)} mandatory clusters are left out: at most {int(len(mandatory) * SKIPPED_CLUSTERS_MAX_SHARE)} may be skipped")
    return errs


def keyword_totals(brief: dict, keywords: list[str]) -> dict[str, int]:
    return {k: sum(b["keywords"][k] + b["heading_keywords"][k] for b in brief["blocks"]) for k in keywords}


def section_totals(blocks: list[dict]) -> dict[str, tuple[int, int]]:
    """Min/max words of a heading including all its sub-headings."""
    out = {}
    for i, b in enumerate(blocks):
        lo, hi = block_range(b)
        for c in blocks[i + 1:]:
            if c["level"] <= b["level"]:
                break
            lo, hi = lo + c["words_min"], hi + c["words_max"]
        out[b["id"]] = (lo, hi)
    return out


def validate(brief: dict, targets: dict, keywords: list[str], settings: Settings, clusters: list[dict] | None = None,
             kb: dict | None = None, page_type: str = "brand-review", casinos: list[dict] | None = None) -> list[str]:
    """Rules of the ТЗ. `page_type` selects what the page needs from the knowledge base: a brand-review page uses all of it and
    carries the brand fact table; a brand-subpage uses the part that serves its topic; a top-list uses the knowledge bases of its
    `casinos` (slug -> facts) and carries a comparison table instead of the fact table."""
    errs: list[str] = []
    blocks = brief["blocks"]
    if not blocks:
        return ["brief has no blocks"]
    if brief.get("intent_summary") and check_language(brief["intent_summary"], "en", keywords):
        errs.append("intent_summary must be in English")
    if blocks[0]["level"] != 1:
        errs.append("first block must be the H1 (level 1)")
    if sum(1 for b in blocks if b["level"] == 1) != 1:
        errs.append("there must be exactly one H1")
    prev = 1
    for b in blocks[1:]:
        if not 2 <= b["level"] <= 6:
            errs.append(f'{b["id"]}: level must be 2-6, got {b["level"]}')
        elif b["level"] > prev + 1:
            errs.append(f'{b["id"]}: heading level jumps from H{prev} to H{b["level"]}')
        prev = b["level"]
    seen = set()
    for b in blocks:
        h = b["heading"].strip().lower()
        if not h:
            errs.append(f'{b["id"]}: empty heading')
        if h in seen:
            errs.append(f'{b["id"]}: duplicate heading "{b["heading"]}"')
        seen.add(h)
        if any(ord(c) > 127 and c.isalpha() for c in b["heading"]):
            errs.append(f'{b["id"]}: heading "{b["heading"]}" must be in English (the brief is always English; the page heading is localized in step 2)')
        elif len(b["heading"].split()) >= 6 and check_language(b["heading"], "en", keywords):
            errs.append(f'{b["id"]}: heading "{b["heading"]}" must be in English')
        for f in ("summary", "copywriter_notes"):
            bad = check_language(b.get(f, ""), "en", keywords) if b.get(f) else []
            if bad:
                errs.append(f'{b["id"]}: {f} must be in English, found {bad[0]["detected"]}: "{bad[0]["segment"][:70]}"')
        lo, hi = block_range(b)
        if lo < 15:
            errs.append(f'{b["id"]}: words_min={lo} is too small (min 15)')
        if hi <= lo:
            errs.append(f'{b["id"]}: words_max must be greater than words_min')
        elif hi > lo * 1.8:
            errs.append(f'{b["id"]}: range {lo}-{hi} is too wide (max/min must be <= 1.8)')
        for f in ("summary", "copywriter_notes"):
            if not b.get(f, "").strip():
                errs.append(f'{b["id"]}: empty {f}')
        if not b["formats"] or any(f not in FORMATS for f in b["formats"]):
            errs.append(f'{b["id"]}: formats must be a non-empty subset of {FORMATS}')
        if not b["entities"]:
            errs.append(f'{b["id"]}: no entities to cover')
        if not b["entity_connections"]:
            errs.append(f'{b["id"]}: no entity connections')
        for e in b["entities"]:
            if not e.get("name", "").strip() or not 1 <= int(e.get("priority", 0)) <= 10:
                errs.append(f'{b["id"]}: bad entity {e}')
        for c in b["entity_connections"]:
            if not all(c.get(k, "").strip() for k in ("subject", "relation", "object")) or not 1 <= int(c.get("priority", 0)) <= 10:
                errs.append(f'{b["id"]}: bad entity connection {c}')
        occ = sum(b["keywords"].values())
        if occ > max(1, b["words"] // 15):
            errs.append(f'{b["id"]}: {occ} keyword mentions in ~{b["words"]} words is too dense (max 1 per 15 words)')
    total_words = sum(b["words"] for b in blocks)
    t = targets["target_body_words"]
    # the large group's length is a ceiling: the text may be shorter when the facts and entities do not fill it
    too_short = targets.get("tier") != "large" and total_words < t * (1 - settings.total_words_tolerance)
    if too_short or total_words > t * (1 + settings.total_words_tolerance):
        errs.append(f"sum of block words is {total_words}, target {t} (±{int(settings.total_words_tolerance * 100)}%)")
    errs += validate_budget(brief, targets, settings)
    errs += validate_visuals(blocks, page_type)
    totals = keyword_totals(brief, keywords)
    for k in keywords:
        if totals[k] != targets["keyword_targets"][k]:
            errs.append(f'keyword "{k}": blocks+headings sum to {totals[k]}, target {targets["keyword_targets"][k]}')
    if page_type != "brand-review":
        for b in blocks:
            if b.get("fact_table"):
                errs.append(f'{b["id"]}: `fact_table` belongs to a brand-review page only: a {page_type} page has no brand fact sheet')
    if kb:
        errs += [f"knowledge base: {e}" for e in brief.get("kb_unresolved", [])]
        if page_type == "brand-subpage":
            errs += validate_subpage_kb(blocks)
        elif page_type == "top-list":
            errs += validate_top_list(blocks, casinos or [])
        else:
            for b in blocks:
                if not b.get("kb_refs"):
                    errs.append(f'{b["id"]}: no knowledge-base references (kb_refs): every block must use brand information')
            used = {KB.variable_of(p) for b in blocks for p in b.get("kb_refs", [])}
            for key in kb["variables"]:
                if key not in used and targets.get("tier") != "small":  # a small text keeps the facts to the minimum: unused variables are fine
                    errs.append(f'knowledge base variable "{key}" is not used by any block')
            errs += validate_fact_table(blocks, keywords)
    if clusters:
        if page_type == "brand-review":
            covered = {c for b in blocks for c in b.get("covers_clusters", [])}
            for c in clusters:
                if c["mandatory"] and c["id"] not in covered:
                    errs.append(f'mandatory cluster {c["id"]} "{c["canonical_title"]}" is not covered by any heading')
        else:
            errs += validate_skipped_clusters(brief, clusters)
    return errs


def rebalance_keywords(brief: dict, targets: dict, keywords: list[str]) -> None:
    """Last resort: nudge per-block counts by ±1 so the totals hit the targets exactly."""
    blocks = brief["blocks"]
    for k in keywords:
        diff = targets["keyword_targets"][k] - keyword_totals(brief, keywords)[k]
        order = sorted(blocks, key=lambda b: -b["words"])
        while diff > 0:
            room = [b for b in order if sum(b["keywords"].values()) < max(1, b["words"] // 15)]
            if not room:
                break
            room[0]["keywords"][k] += 1
            diff -= 1
            order = sorted(blocks, key=lambda b: (sum(b["keywords"].values()) / max(b["words"], 1)))
        while diff < 0:
            have = [b for b in blocks if b["keywords"][k] > fact_table_hazards(b, keywords).get(k, 0)]  # the table must keep its e-mail
            if not have:
                break
            max(have, key=lambda b: sum(b["keywords"].values()) / max(b["words"], 1))["keywords"][k] -= 1
            diff += 1


def visual_elements(b: dict, blocks: list[dict]) -> str:
    """'Table — 1 of 3 tables on the page' for blocks with a list/table, else 'None specified'."""
    parts = []
    for f in ("list", "table"):
        if f in b["formats"]:
            total = sum(1 for x in blocks if f in x["formats"])
            idx = sum(1 for x in blocks[: blocks.index(b) + 1] if f in x["formats"])
            parts.append(f"{FORMAT_LABEL[f]} — {idx} of {total} {f}s on the page")
    return "; ".join(parts) or "None specified"


def render_block(b: dict, blocks: list[dict], totals: dict[str, tuple[int, int]]) -> str:
    """One block in the ТЗ layout (heading, word count, entities, keywords, summary, visuals, notes, connections)."""
    lo, hi = block_range(b)
    lines = [f"{'#' * b['level']} {b['heading']}", ""]
    tlo, thi = totals[b["id"]]
    if b["level"] > 1 and (tlo, thi) != (lo, hi):  # for the H1 "including subsections" would be the whole page
        lines.append(f"Word Count: {tlo}-{thi} words total including subsections / {lo}-{hi} words for this heading")
    else:
        lines.append(f"Word Count: {lo}-{hi} words")
    lines.append("")
    lines.append("Entities to cover: " + ", ".join(f"{e['name']} [{e['priority']}]" for e in b["entities"]))
    kws = ", ".join(f"{k} ×{v}" for k, v in b["keywords"].items() if v)
    lines += ["", f"Keywords (exact count in body): {kws or 'none'}"]
    hk = ", ".join(f"{k} ×{v}" for k, v in b["heading_keywords"].items() if v)
    if hk:
        lines.append(f"Keywords the page heading must contain: {hk}")
    lines += ["", f"Summary: {b['summary']}", "", f"Visual Elements: {visual_elements(b, blocks)}", "",
              f"Copywriter Notes: {b['copywriter_notes']}", "", "Entity Connections:"]
    lines += [f"- {c['subject']} → {c['relation']} → {c['object']} [{c['priority']}]" for c in b["entity_connections"]]
    if b.get("internal_links"):
        lines += ["", internal_link_note(b)]
    if b.get("fact_table"):
        lines += ["", "Brand Fact Table (short label | value rows, in this order; values come from the knowledge base):"]
        for n, r in enumerate(b["fact_table"], 1):
            lines.append(f"{n}. {r['label']} [{r['key']}] ← " + (", ".join(r["kb_refs"]) or "NO SOURCE"))
    if b.get("brand_info"):
        lines += ["", "Brand Information (verbatim from the knowledge base; the writer gets it as a fact card in the step 2 request: never copy its sentences into a text):"]
        lines += [f"- {i['path']}: {KB.render_value(i['value'])}" for i in b["brand_info"]]
        hz = brand_info_hazards(b, list(b["keywords"]))
        if hz:
            lines.append("Counting hazard (the facts above contain tracked keywords): " + ", ".join(f"{k} ×{n}" for k, n in hz.items()))
    return "\n".join(lines)


def home_link_note(brief: dict) -> str:
    """brand-subpage only: the page links to the home page of the site, the anchor is the brand name in the running text of the intro
    (the page builder wraps its first mention; the writer adds no sentence for the link)."""
    if brief.get("page_type", "brand-review") != "brand-subpage" or not brief.get("brand"):
        return ""
    return (f'Home link: the first mention of the brand name "{brief["brand"]}" in the running text of this block is the anchor of the internal link to '
            "the home page of the site (the page builder adds the link). Put the brand name in a natural sentence of the body (not in a list or a table) "
            "and write no sentence whose only job is to carry a link.")


def render_markdown(brief: dict, job: dict, targets: dict) -> str:
    """Human-readable ТЗ. Always English (the brief language never follows the GEO)."""
    blocks = brief["blocks"]
    totals = section_totals(blocks)
    mids = sum(b["words"] for b in blocks)
    lines = [
        "# Brief (step 1)",
        "",
        f"- GEO: {job['geo']}  |  page language: {job['language']}",
        *([f"- Page type: {job['page_type']}"] if job.get("page_type", "brand-review") != "brand-review" else []),
        *([f"- AffBulk knowledge base: {job['knowledge_base']}"] if job.get("knowledge_base") else []),
        f"- Search intent: {brief.get('intent_summary', '')}",
        f"- Body length: target {targets['target_body_words']} words"
        + (f" (competitor-based size {targets['base_body_words']}, enlarged to give the facts and connections of a block the words they need)"
           if targets.get("base_body_words") not in (None, targets["target_body_words"]) else "")
        + f"; block midpoints add up to {mids}; "
        f"the sum of the block ranges is {sum(b['words_min'] for b in blocks)}-{sum(b['words_max'] for b in blocks)} "
        "(every block is checked against its own range; a block may exceed its maximum by the overflow named in its Word Count line)",
        *([f"- Limit of the whole text: {targets['max_body_words']} words ({_limit_note(targets)}); the final text is checked against it in step 3"
           + ("; this large text may be shorter when the facts and entities do not fill it" if targets.get("tier") == "large" else "")]
          if targets.get("max_body_words") else []),
        "- Keywords (total target, headings included): " + ", ".join(f"{k} ×{v}" for k, v in targets["keyword_targets"].items()),
        "- Headings are written in English here; the page headings are localized in step 2 (keeping the planned keywords)",
        *([f"- Left out on purpose (mandatory competitor clusters): " + "; ".join(f"{s['id']} ({s['reason']})" for s in brief["skipped_clusters"])]
          if brief.get("skipped_clusters") else []),
        *([f"- {home_link_note(brief)}"] if home_link_note(brief) else []),
        *([f"- Internal links to: {', '.join('/' + s for s in brief['site_pages'])} (anchors of at most {MAX_ANCHOR_WORDS} words, planted in the "
           "blocks below; no section is written for a link)"] if brief.get("site_pages") else []),
        "",
        "| # | Heading | Words | Keywords in body | Format | Source |",
        "|---|---|---|---|---|---|",
    ]
    for b in blocks:
        kws = ", ".join(f"{k} ×{v}" for k, v in b["keywords"].items() if v) or "—"
        lines.append(f"| {b['id']} | {'  ' * (b['level'] - 1)}H{b['level']} {b['heading']} | {b['words_min']}-{b['words_max']} | {kws} | {'+'.join(b['formats'])}{' (fact table)' if b.get('fact_table') else ''} | {b['source']} |")
    lines += ["", "---", ""]
    for b in blocks:
        lines += [f"<!-- {b['id']} -->", render_block(b, blocks, totals), "", "---", ""]
    return "\n".join(lines)
