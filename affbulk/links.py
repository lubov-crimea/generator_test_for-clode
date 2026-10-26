"""Internal links of a brand site: wrap an anchor, check anchor length, check that the home page and the inner pages link to each other.

Used by `build_page` (config `internal_links`, `home_link`), by the home-page update scripts and after deployment:

    site_link_report({"index": <content>, "login": <content>, ...})  -> list of problems
"""
from __future__ import annotations

import html
import re

from textgen.sitemap import MAX_ANCHOR_WORDS

LINK_RE = re.compile(r'<a\s[^>]*href="(/[^"]*)"[^>]*>(.*?)</a>', re.S)


def anchor_words(anchor: str) -> int:
    return len(re.sub(r"<[^>]+>", " ", anchor).split())


def wrap_phrase(content: list[dict], phrase: str, href: str, what: str = "link anchor") -> None:
    """Wrap the first mention of `phrase` in the running text of an article (headings, existing links and tags are skipped; the intro is
    searched first, then the sections in page order) with an internal link. Nothing is added to the text. Raises when the phrase is longer
    than `MAX_ANCHOR_WORDS` words or is not in the text."""
    if anchor_words(phrase) > MAX_ANCHOR_WORDS:
        raise ValueError(f"{what} {phrase!r} has more than {MAX_ANCHOR_WORDS} words")
    pat = re.compile(r"(?<![\w-])" + re.escape(html.escape(phrase, quote=False)) + r"(?![\w-])")
    for b in content:
        if b["__component"] != "blocks.article":
            continue
        parts = re.split(r"(<[^>]+>)", b["article"])
        in_link = in_head = False
        for i, p in enumerate(parts):
            if p.startswith("<"):
                tag = p.lower()
                in_link = True if tag.startswith("<a ") else False if tag == "</a>" else in_link
                in_head = True if re.match(r"<h[1-6]\b", tag) else False if re.match(r"</h[1-6]>", tag) else in_head
            elif not in_link and not in_head:
                m = pat.search(p)
                if m:
                    parts[i] = p[:m.start()] + f'<a href="{href}">{m.group(0)}</a>' + p[m.end():]
                    b["article"] = "".join(parts)
                    return
    raise ValueError(f"{what} {phrase!r} is not in the running text of the page")


def internal_links(content: list[dict]) -> list[tuple[str, str]]:
    """[(anchor, href)] of every internal link ('/...') in the articles of a page."""
    return [(re.sub(r"<[^>]+>", "", m.group(2)).strip(), m.group(1))
            for b in content if b.get("article") for m in LINK_RE.finditer(b["article"])]


def check_anchors(content: list[dict]) -> list[str]:
    return [f"anchor {a!r} -> {h} has {anchor_words(a)} words (max {MAX_ANCHOR_WORDS})"
            for a, h in internal_links(content) if anchor_words(a) > MAX_ANCHOR_WORDS]


def _slug_of(href: str) -> str:
    return href.split("#")[0].split("?")[0].strip("/") or "index"


def site_link_report(pages: dict[str, list[dict]], home: str = "index") -> list[str]:
    """`pages` = {slug: content}. The home page links to every other page, every other page links to the home page, anchors are short."""
    errs: list[str] = []
    for slug, content in pages.items():
        targets = {_slug_of(h) for _, h in internal_links(content)}
        errs += [f"{slug}: {e}" for e in check_anchors(content)]
        if slug == home:
            errs += [f"{home}: no link to /{s}" for s in pages if s != home and s not in targets]
        elif home not in targets:
            errs.append(f"{slug}: no link to the home page")
    return errs
