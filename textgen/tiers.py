"""Size groups ("tiers") of the competitors.

The competitors of a query write texts of very different length (Login: 238, 385, 524, 844, 1754 words). Instead of one median, the
competitors are split into up to three groups by their natural breaks (the two largest gaps between the sorted lengths):

    Login 238 / 385 / 524  |  844  |  1754        longfu88-sg 1116 / 1473  |  1836 / 1957  |  3355

    small   the short texts: only the most important blocks, the entities and facts cut to the minimum. Limit: mean x 1.2
    medium  the optimum: the base ТЗ is built for this group.                                       Limit: mean x 1.2
    large   the longest texts: the base ТЗ plus more blocks, facts and entities. Limit: the mean (x 1.0); the text may be shorter
            when there are not enough facts and entities to fill it.

Fewer than three competitors give fewer groups: two competitors -> small and large with a synthetic medium (their mean), one -> medium
only. A large group of ONE competitor is an outlier: it gets one text per `large_per_texts` (10) texts, at least one.

The numbers live in `01_tiers.json` of a run and in `targets` of its ТЗ; a variant of the ТЗ names its group (`tier`).
"""
from __future__ import annotations

import math
import statistics

from .config import Settings

NAMES = ("small", "medium", "large")
BASE = "medium"  # the base ТЗ is built for the optimum


def split_groups(values: list[int], k: int = 3) -> list[list[int]]:
    """Natural breaks: the sorted values cut at the k-1 largest gaps (ties: the earlier gap)."""
    v = sorted(values)
    k = min(k, len(v))
    if k <= 1:
        return [v]
    cuts = sorted(sorted(range(len(v) - 1), key=lambda i: (-(v[i + 1] - v[i]), i))[: k - 1])
    groups, start = [], 0
    for c in cuts:
        groups.append(v[start:c + 1])
        start = c + 1
    groups.append(v[start:])
    return groups


def _tier(values: list[int], multiplier: float, **extra) -> dict:
    mean = statistics.mean(values)
    return {"competitors": values, "mean": round(mean), "multiplier": multiplier, "target": round(mean), "limit": round(mean * multiplier), **extra}


def build_tiers(bodies: list[int], settings: Settings, words_override: int | None = None) -> dict:
    """{"competitors": sorted lengths, "base": "medium", "tiers": {"small"|"medium"|"large": {competitors, mean, multiplier, target, limit, ...}}}.
    `target` is what the sum of the block middles should be, `limit` what the sum of the block maxima and the final text must not exceed."""
    mult = 1 + settings.page_limit
    mult_large = 1 + settings.page_limit_large
    v = sorted(b for b in bodies if b > 0)
    if words_override:  # a length given by the operator is the optimum, there are no groups
        return {"competitors": v, "base": BASE, "tiers": {BASE: _tier([words_override], mult, given=True)}}
    if not v:
        raise ValueError("no competitor text to take the length from")
    if len(v) == 1:
        return {"competitors": v, "base": BASE, "tiers": {BASE: _tier(v, mult)}}
    if len(v) == 2:
        return {"competitors": v, "base": BASE, "tiers": {
            "small": _tier(v[:1], mult), "medium": _tier(v, mult, synthetic=True), "large": _tier(v[1:], mult_large, outlier=True)}}
    small, medium, large = split_groups(v, 3)
    return {"competitors": v, "base": BASE, "tiers": {
        "small": _tier(small, mult), "medium": _tier(medium, mult), "large": _tier(large, mult_large, outlier=len(large) == 1)}}


def allocate(n_texts: int, tiers: dict, settings: Settings) -> dict[str, int]:
    """How many of `n_texts` texts go to each group. The optimum comes first, then one large text (a single outlier gets one text per
    `large_per_texts` texts, at least one), the rest is split between medium (the larger half) and small. Example: 8 texts and
    Login's groups -> small 3, medium 4, large 1."""
    present = tiers["tiers"]
    counts = {name: 0 for name in present}
    if n_texts <= 0:
        return counts
    counts[BASE] = 1
    left = n_texts - 1
    if "large" in present and left:
        large = present["large"]
        want = math.ceil(n_texts / settings.large_per_texts) if large.get("outlier") else max(1, round(n_texts * len(large["competitors"]) / len(tiers["competitors"])))
        counts["large"] = min(want, left)
        left -= counts["large"]
    if "small" in present and left:
        counts["small"] = max(1, left // 2)
        left -= counts["small"]
    counts[BASE] += left
    return counts


def describe(tiers: dict) -> str:
    rows = []
    for name in NAMES:
        t = tiers["tiers"].get(name)
        if t:
            note = " (mean of all, no group)" if t.get("synthetic") else " (single outlier)" if t.get("outlier") else ""
            rows.append(f'{name:6} {"/".join(map(str, t["competitors"]))} -> mean {t["mean"]}, limit {t["limit"]} (x{t["multiplier"]:.1f}){note}')
    return "\n".join(rows)
