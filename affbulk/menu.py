"""Header and footer menu of a site when an internal page is added.

    header, footer, log = plan_menu(header_nav_links, footer_links, brand="Longfu88", slug="bonuses", label="Longfu88 Bonuses")

Rules (prompts/affbulk_import.md):
- the name is short and has no brand: "Longfu88 Bonuses" -> "Bonuses";
- an item of the same topic is replaced, not duplicated ("Promotions" -> "Bonuses"), in the header and in the footer; an affiliate item is
  replaced by the internal link;
- the header has at most `MAX_HEADER_ITEMS` items; when it is full, the last affiliate item moves to the footer (the header keeps at least
  `MIN_HEADER_AFFILIATE` affiliate items), otherwise the internal page goes to the footer;
- the footer has no limit.
Items are dicts `{text, link, linkStatus}` (ids of the server are dropped). Nothing is written to AffBulk here.
"""
from __future__ import annotations

from textgen.sitemap import MAX_HEADER_ITEMS, MIN_HEADER_AFFILIATE, short_label, topic_of


def _item(x: dict) -> dict:
    return {"text": x["text"], "link": x["link"], "linkStatus": x.get("linkStatus", "affiliate")}


def _internal(x: dict) -> bool:
    return x["linkStatus"] == "internal"


def _replace_or_append(items: list[dict], new: dict, topic: str | None, log: list[str], where: str) -> None:
    same = next((i for i, x in enumerate(items) if x["link"] == new["link"] and _internal(x)), None)
    if same is None and topic:
        same = next((i for i, x in enumerate(items) if topic_of(x["text"]) == topic and not (_internal(x) and x["link"] != new["link"])), None)
    if same is None:
        items.append(new)
        log.append(f"{where}: added {new['text']!r}")
    else:
        log.append(f"{where}: {items[same]['text']!r} -> {new['text']!r}" if items[same] != new else f"{where}: {new['text']!r} is already there")
        items[same] = new


def plan_menu(header: list[dict], footer: list[dict], *, brand: str, slug: str, label: str) -> tuple[list[dict], list[dict], list[str]]:
    head = [_item(x) for x in header]
    foot = [_item(x) for x in footer]
    log: list[str] = []
    for lst in (head, foot):  # internal items already there lose the brand name
        for x in lst:
            if _internal(x):
                x["text"] = short_label(x["text"], brand)
    new = {"text": short_label(label, brand), "link": f"/{slug}", "linkStatus": "internal"}
    topic = topic_of(new["text"]) or topic_of(slug)

    in_head = any(x["link"] == new["link"] for x in head) or (topic is not None and any(topic_of(x["text"]) == topic for x in head))
    if in_head:
        _replace_or_append(head, new, topic, log, "header")
    elif len(head) < MAX_HEADER_ITEMS:
        head.append(new)
        log.append(f"header: added {new['text']!r}")
    else:
        aff = [i for i, x in enumerate(head) if not _internal(x)]
        if len(aff) > MIN_HEADER_AFFILIATE:
            moved = head.pop(aff[-1])
            if not any(x["text"].lower() == moved["text"].lower() for x in foot):
                foot.append(moved)
            head.append(new)
            log.append(f"header: full, {moved['text']!r} moved to the footer, added {new['text']!r}")
        else:
            _replace_or_append(foot, new, topic, log, "footer")
            return head, foot, log
    if any(x["link"] == new["link"] or (topic is not None and topic_of(x["text"]) == topic) for x in foot):  # the footer analog becomes the internal link
        _replace_or_append(foot, new, topic, log, "footer")
    return head, foot, log
