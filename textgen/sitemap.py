"""Site structure of a brand site: the base set of pages, internal links between them and the menu rules.

The same table serves three steps: the brief plants the links in the blocks where the topic comes up (`attach_internal_links`), the AffBulk
builder wraps the anchors and checks them (`affbulk/links.py`), the menu planner keeps the header and the footer in order (`affbulk/menu.py`).
Rules (also in CLAUDE.md and prompts/affbulk_import.md): the anchor of an internal link has at most `MAX_ANCHOR_WORDS` words; the header menu
has at most `MAX_HEADER_ITEMS` items; the home page links to every internal page and every internal page links to the home page.
"""
from __future__ import annotations

import re

MAX_ANCHOR_WORDS = 3
MAX_HEADER_ITEMS = 6
MIN_HEADER_AFFILIATE = 3  # a full header keeps at least this many affiliate items; the other internal pages go to the footer

# The base set of a brand site (the home page is "/"). `menu`: which menu items are the same topic; `block`: which brief blocks name the topic.
BASE_SITE_PAGES = [
    {"slug": "bonuses", "label": "Bonuses", "menu": r"bonus|promotion|promo|offer",
     "block": r"bonus|welcome|promotion|offer|cashback|reload|free spin"},
    {"slug": "app", "label": "App", "menu": r"\bapp\b|mobile|download|apk",
     "block": r"\bapp\b|mobile|download|apk|smartphone|phone"},
    {"slug": "promo-code", "label": "Promo Code", "menu": r"promo[\s-]*code|coupon", "block": r"promo[\s-]*code|coupon|bonus code"},
    {"slug": "login", "label": "Login", "menu": r"log[\s-]?in|sign[\s-]?in",
     "block": r"log[\s-]?in|sign[\s-]?in|regist|sign[\s-]?up|account"},
    {"slug": "no-deposit-bonus", "label": "No Deposit Bonus", "menu": r"no[\s-]*deposit|free[\s-]*(?:chip|spins?)",
     "block": r"no[\s-]*deposit|free (?:chip|spin)"},
    {"slug": "payments", "label": "Payments", "menu": r"payment|deposit|withdraw|banking|cashier",
     "block": r"payment|deposit|withdraw|banking|cashier"},
]
# the most specific topic is tried first ("No Deposit Bonus" is a bonus and a deposit word, but its own topic)
TOPIC_ORDER = ["promo-code", "no-deposit-bonus", "login", "app", "payments", "bonuses"]
_BY_SLUG = {p["slug"]: p for p in BASE_SITE_PAGES}


def page_info(slug: str) -> dict:
    """Base page by slug; an unknown slug is a custom page named after its words."""
    if slug in _BY_SLUG:
        return _BY_SLUG[slug]
    words = slug.replace("-", " ")
    return {"slug": slug, "label": words.title(), "menu": re.escape(words), "block": re.escape(words)}


def topic_of(text: str) -> str | None:
    """Slug of the base page whose topic the menu item / keyword is about (None for 'Casino', 'Live Casino' ...)."""
    for slug in TOPIC_ORDER:
        if re.search(_BY_SLUG[slug]["menu"], text, re.I):
            return slug
    return None


def short_label(label: str, brand: str) -> str:
    """Menu item names do not carry the brand: 'Longfu88 Bonuses' -> 'Bonuses'."""
    out = re.sub(re.escape(brand), " ", label, flags=re.I) if brand else label
    out = re.sub(r"\s+", " ", out).strip(" -:|")
    return out or label


def own_slug(keywords: list[str]) -> str | None:
    """The page a brand-subpage is: 'Longfu88 login' -> login."""
    return topic_of(keywords[0]) if keywords else None


def site_pages_for(job) -> list[str]:
    """Slugs of the internal pages this page links to: `Site pages` of the input, else the base set without the page itself. A top list has none."""
    if job.page_type == "top-list":
        return []
    pages = list(job.site_pages) if job.site_pages is not None else [p["slug"] for p in BASE_SITE_PAGES]
    me = own_slug(job.keywords) if job.page_type == "brand-subpage" else None
    return [s for s in pages if s != me]


def attach_internal_links(brief: dict, pages: list[str], required: bool) -> dict[str, list[str]]:
    """Plant each page in the first block (not the H1) whose heading or summary names the topic and set `b["internal_links"]`.
    A home page (`required`) puts the pages that match no block into the intro; a subpage links its siblings only where the topic is named
    (optional). Returns {slug: block id}."""
    blocks = brief["blocks"]
    placed: dict[str, list[str]] = {}
    for slug in pages:
        info = page_info(slug)
        rx = re.compile(info["block"], re.I)
        hit = next((b for b in blocks[1:] if rx.search(b["heading"])), None) or next((b for b in blocks[1:] if rx.search(b.get("summary", ""))), None)
        if hit is None and required:
            hit = blocks[0]
        if hit is not None:
            hit.setdefault("internal_links", []).append({"slug": slug, "href": f"/{slug}", "label": info["label"], "required": required})
            placed.setdefault(hit["id"], []).append(slug)
    return {s: bid for bid, slugs in placed.items() for s in slugs}


def internal_link_note(b: dict) -> str:
    """Line of the block brief (render_block / step 2) for the internal links planted in the block."""
    links = b.get("internal_links") or []
    if not links:
        return ""
    names = "; ".join(f'{l["label"]} page ({l["href"]})' for l in links)
    kind = "required" if any(l.get("required") for l in links) else "optional, only where a sentence of the block needs the topic"
    return (f"Internal links ({kind}): {names}. Name the topic in a short natural phrase of at most {MAX_ANCHOR_WORDS} words inside a sentence of the "
            "body (never in a list, a table or a heading, never a sentence written only to carry the link); the page builder wraps that phrase. "
            "A tracked keyword used as the phrase counts as usual.")
