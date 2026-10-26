"""Compare a page read back from AffBulk (pages_find_one, populate=deep, saved tool result) with the payload that was sent.

    python -m affbulk.verify_page <run> <readback.json>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from .build_page import RUNS_DIR


def _media_id(m):
    return m.get("id") if isinstance(m, dict) else m


def _norm(b: dict) -> dict:
    out = {"__component": b["__component"]}
    for k in ("title", "label", "article", "description", "disclaimer"):
        if k in b and b[k] not in (None, ""):
            out[k] = b[k]
    for k in ("background", "image"):
        if b.get(k):
            out[k] = _media_id(b[k])
    for k in ("buttons",):
        if b.get(k):
            out[k] = [(x["text"], x["link"], x["linkStatus"], x["variant"]) for x in b[k]]
    if b.get("blocks"):
        out["blocks"] = [(x["description"], _media_id(x["image"]), x["button"]["linkStatus"]) for x in b["blocks"]]
    if b.get("items"):
        out["items"] = [(_media_id(x.get("image")), x["content"], [y["linkStatus"] for y in x.get("buttons", [])]) for x in b["items"]]
    if b.get("reviews"):
        out["reviews"] = [(x["username"], x["review"], x["date"], _media_id(x.get("avatar")), x["rating"]["ratingValue"]) for x in b["reviews"]]
    if b.get("faqs"):
        out["faqs"] = [(x["question"], x["answer"]) for x in b["faqs"]]
    return out


def compare(expected: dict, got: dict) -> list[str]:
    errs = []
    if expected["slug"] != got.get("slug"):
        errs.append(f"slug {got.get('slug')} != {expected['slug']}")
    for k in ("title", "description"):
        if expected["seo"][k] != got["seo"][k]:
            errs.append(f"seo.{k} differs")
    for k in ("customCanonical", "customPageLang"):  # multi-language sites
        if expected["seo"].get(k) and expected["seo"][k] != (got.get("seo") or {}).get(k):
            errs.append(f"seo.{k} {(got.get('seo') or {}).get(k)!r} != {expected['seo'][k]!r}")
    if expected.get("customHeadHTML") and expected["customHeadHTML"].replace("\r\n", "\n") != (got.get("customHeadHTML") or "").replace("\r\n", "\n"):
        errs.append("customHeadHTML differs")
    e, g = expected["content"], got["content"]
    if len(e) != len(g):
        errs.append(f"block count {len(g)} != {len(e)}")
    for i, (x, y) in enumerate(zip(e, g)):
        nx, ny = _norm(x), _norm(y)
        if nx != ny:
            diff = [k for k in nx.keys() | ny.keys() if nx.get(k) != ny.get(k)]
            errs.append(f"block {i} {x['__component']}: fields differ {diff}")
    return errs


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: python -m affbulk.verify_page <run> <readback.json>")
    expected = json.loads((RUNS_DIR / sys.argv[1] / "05_affbulk_page.json").read_text(encoding="utf-8"))
    got = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    if isinstance(got, list):
        got = got[0]
    errs = compare(expected, got)
    print(f"{len(got['content'])} blocks read back; {'OK' if not errs else 'DIFFERENCES'}")
    for e in errs:
        print("-", e)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
