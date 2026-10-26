"""Step 1, items 1-2: keyword occurrence stats and heading clustering."""
from __future__ import annotations

import math
import re
import statistics
from collections import Counter
from typing import Any

from .config import Settings
from .llm import LLM
from .prompts import load_prompt
from .textutil import count_keywords


def usable_pages(pages: list[dict]) -> list[dict]:
    """A page that loaded but has no text (script-rendered, blocked) says nothing about the length, the keywords or the headings of a
    competitor: it is treated like a page that failed to load (the file with the raw pages stays as it was fetched)."""
    return [{**p, "ok": False, "error": "no text found"} if p.get("ok") and not p.get("body_words") else p for p in pages]


def keyword_stats(pages: list[dict], keywords: list[str]) -> dict:
    """Keyword occurrences per competitor: in the body, in each heading level H1..H6, and in total."""
    rows = []
    for p in usable_pages(pages):
        if not p.get("ok"):
            continue
        by_level: dict[str, dict[str, int]] = {}
        for lvl in range(1, 7):
            joined = "\n".join(h["text"] for h in p["headings"] if h["level"] == lvl)
            by_level[str(lvl)] = count_keywords(joined, keywords)
        body = count_keywords(p["text"], keywords)
        heads = {k: sum(by_level[l][k] for l in by_level) for k in keywords}
        rows.append(
            {
                "url": p["url"],
                "word_count": p["word_count"],
                "body_words": p["body_words"],
                "body": body,
                "headings_by_level": by_level,
                "headings_total": heads,
                "total": {k: body[k] + heads[k] for k in keywords},
            }
        )
    if not rows:
        raise RuntimeError("No competitor page could be loaded. Save HTML into input/html/<domain>.html or check the URLs.")
    med = lambda vals: statistics.median(vals)  # noqa: E731
    aggregate = {
        "competitors_ok": len(rows),
        "median_body_words": round(med([r["body_words"] for r in rows])),
        "median_total": {k: round(med([r["total"][k] for r in rows])) for k in keywords},
        "median_headings_total": {k: round(med([r["headings_total"][k] for r in rows])) for k in keywords},
        "median_h1": {k: round(med([r["headings_by_level"]["1"][k] for r in rows])) for k in keywords},
    }
    return {"competitors": rows, "aggregate": aggregate}


_CAP = r"A-ZĄĆĘŁŃÓŚŹŻÀ-ÖØ-Þ"
_LOW = r"a-ząćęłńóśźżß-öø-ÿ"
ENTITY_RE = re.compile(rf"[{_CAP}][\w'’\-]*(?:[ \t]+(?:[{_CAP}0-9][\w'’\-]*))*")


def mine_entities(pages: list[dict], keywords: list[str], top: int = 80) -> list[dict]:
    """Capitalised names/terms found in competitor texts (payment systems, providers, regulators, bonus names...).

    Single capitalised words at the start of a sentence are ignored. Ranked by number of competitors, then frequency.
    The result is a candidate list for the ТЗ author, not a final entity list.
    """
    per_page: list[Counter] = []
    for p in pages:
        if not p.get("ok"):
            continue
        text = "\n".join([h["text"] for h in p["headings"]] + [p["text"]])
        cnt: Counter = Counter()
        for m in ENTITY_RE.finditer(text):
            ent = re.sub(r"^(?:The|A|An)\s+", "", m.group(0).strip())
            before = text[: m.start()].rstrip(" \t")[-1:]  # a newline counts as a sentence boundary
            if " " not in ent and (before in ("", ".", "!", "?", ":", "\n") or len(ent) < 3):
                continue  # single word at the start of a sentence
            cnt[ent] += 1
        per_page.append(cnt)
    kw_norm = {re.sub(r"\s+", " ", k.lower()) for k in keywords}
    total: Counter = Counter()
    seen_in: Counter = Counter()
    for cnt in per_page:
        for ent, n in cnt.items():
            total[ent] += n
            seen_in[ent] += 1
    rows = [
        {"entity": e, "competitors": seen_in[e], "count": total[e]}
        for e in total
        if re.sub(r"\s+", " ", e.lower()) not in kw_norm and not any(k in e.lower() for k in kw_norm)
    ]
    rows.sort(key=lambda r: (-r["competitors"], -r["count"]))
    return rows[:top]


def fact_table_summary(pages: list[dict], top: int = 30) -> dict:
    """What competitors put into their brand fact sheets (two-column tables): the tables themselves and how many
    competitors use each row label. Candidates for the rows of our fact table, not the final row list.

    Cells are shortened (label 60, value 120 chars) because only the kind of fact matters here.
    """
    tables, seen_in = [], {}
    for i, p in enumerate(pages):
        if not p.get("ok"):
            continue
        for t in p.get("fact_tables", []):
            rows = [[label[:60], value[:120]] for label, value in t["rows"]]
            tables.append({"competitor": i, "url": p["url"], "heading": t["heading"], "rows": rows})
            for label, _ in rows:
                seen_in.setdefault(re.sub(r"\s+", " ", label.lower()).strip(" :"), set()).add(i)
    labels = sorted(({"label": k, "competitors": len(v)} for k, v in seen_in.items()), key=lambda r: (-r["competitors"], r["label"]))
    return {"tables": tables, "labels": labels[:top]}


CLUSTER_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "clusters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "Short label of the shared meaning"},
                    "canonical_title": {"type": "string", "description": "Best heading wording for this topic, in the page language"},
                    "member_ids": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["topic", "canonical_title", "member_ids"],
            },
        }
    },
    "required": ["clusters"],
}


def cluster_headings(pages: list[dict], settings: Settings, llm: LLM) -> list[dict]:
    """Group H2-H6 headings of all competitors by meaning. Frequency, mean size, position are computed in code."""
    flat: dict[str, dict] = {}
    ok_idx = [i for i, p in enumerate(pages) if p.get("ok")]
    for i in ok_idx:
        n = len(pages[i]["headings"])
        for j, h in enumerate(pages[i]["headings"]):
            if h["level"] == 1:
                continue
            flat[f"c{i}h{j}"] = {**h, "competitor": i, "pos": j / max(n - 1, 1)}

    listing = "\n".join(f'{hid} | H{h["level"]} | {h["text"]}' for hid, h in flat.items())
    data = llm.json(
        load_prompt("step1_cluster"),
        f"Competitor headings (id | level | text). Group them by meaning.\n\n{listing}",
        CLUSTER_SCHEMA,
        settings.model_analysis,
        name="heading_clusters",
    )

    assigned: set[str] = set()
    clusters: list[dict] = []
    for c in data["clusters"]:
        ids = [m for m in c["member_ids"] if m in flat and m not in assigned]
        if not ids:
            continue
        assigned.update(ids)
        clusters.append({"topic": c["topic"], "canonical_title": c["canonical_title"], "ids": ids})
    for hid in flat:  # headings the model skipped become their own cluster
        if hid not in assigned:
            clusters.append({"topic": flat[hid]["text"], "canonical_title": flat[hid]["text"], "ids": [hid]})

    # "frequent" = in at least mandatory_ratio of the pages we could LOAD (a competitor that failed to download must neither
    # lower nor raise the bar), but never fewer than 2 pages when 2+ pages are available
    need = max(2 if len(ok_idx) >= 2 else 1, math.ceil(settings.mandatory_ratio * len(ok_idx)))
    out = []
    for n, c in enumerate(clusters, 1):
        members = [flat[i] for i in c["ids"]]
        comps = {m["competitor"] for m in members}
        out.append(
            {
                "id": f"k{n:02d}",
                "topic": c["topic"],
                "canonical_title": c["canonical_title"],
                "frequency": len(comps),
                "mandatory": len(comps) >= need,
                "levels": sorted({m["level"] for m in members}),
                "avg_section_words": round(statistics.mean(m["words"] for m in members)),
                "avg_position": round(statistics.mean(m["pos"] for m in members), 2),
                "examples": [{"competitor": m["competitor"], "level": m["level"], "text": m["text"]} for m in members][:8],
            }
        )
    out.sort(key=lambda c: (-c["frequency"], c["avg_position"]))
    return out
