"""Download a competitor page and extract headings + visible text."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup, Tag

from .textutil import count_words

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
}
NOISE_TAGS = ["script", "style", "noscript", "nav", "footer", "aside", "form", "iframe", "svg", "button"]
HEADING_TAGS = ["h1", "h2", "h3", "h4", "h5", "h6"]


def fetch_html(url: str, html_dir: Path | None = None, timeout: int = 30) -> str:
    """Prefer a hand-saved copy in html_dir/<domain>.html (for pages behind bot protection), otherwise download."""
    if html_dir:
        domain = urlparse(url).netloc.replace("www.", "")
        for cand in (html_dir / f"{domain}.html", html_dir / f"{domain}{urlparse(url).path.strip('/').replace('/', '_')}.html"):
            if cand.exists():
                return cand.read_text(encoding="utf-8", errors="ignore")
    r = requests.get(url, headers=HEADERS, timeout=timeout)
    r.raise_for_status()
    r.encoding = r.apparent_encoding if r.encoding in (None, "ISO-8859-1") else r.encoding
    return r.text


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def extract_fact_rows(root: Tag) -> list[dict]:
    """Two-column "label | value" tables and definition lists of the page: [{"heading", "rows": [[label, value], ...]}].

    Competitors put a brand fact sheet (licence, bonus, currencies, support ...) in such a table; step 1 learns from it which
    rows the fact table of the new page needs. Tables with other column counts and tables with fewer than 3 rows are skipped.
    """
    out: list[dict] = []

    def add(rows: list[list[str]], anchor: Tag) -> None:
        rows = [r for r in rows if r[0] and r[1]]
        if len(rows) >= 3:
            prev = anchor.find_previous(HEADING_TAGS)
            out.append({"heading": _clean(prev.get_text(" ")) if prev else "", "rows": rows})

    for table in root.find_all("table"):
        rows = []
        for tr in table.find_all("tr"):
            cells = [_clean(c.get_text(" ")) for c in tr.find_all(["th", "td"], recursive=False)]
            if len(cells) == 2:
                rows.append(cells)
        add(rows, table)
    for dl in root.find_all("dl"):
        dts, dds = dl.find_all("dt"), dl.find_all("dd")
        if len(dts) == len(dds):
            add([[_clean(t.get_text(" ")), _clean(d.get_text(" "))] for t, d in zip(dts, dds)], dl)
    return out


def parse_page(html: str, url: str) -> dict:
    """Returns {url, word_count, headings:[{level,text,words}], text, fact_tables}.

    `words` of a heading = words between it and the next heading of any level (its own section body).
    """
    soup = BeautifulSoup(html, "lxml")
    for t in soup(NOISE_TAGS):
        t.decompose()
    body: Tag = soup.body or soup
    root: Tag = soup.find("main") or soup.find("article") or body
    if root is not body and root.find("h1") is None and body.find("h1") is not None:
        root = body  # the H1 sits in a hero block outside <main>/<article>
    # element-by-element walk to keep document order
    headings: list[dict] = []
    paragraphs: list[str] = []
    current: dict | None = None
    for el in root.descendants:
        if not isinstance(el, Tag):
            continue
        if el.name in HEADING_TAGS:
            text = _clean(el.get_text(" "))
            if not text:
                continue
            current = {"level": int(el.name[1]), "text": text, "words": 0}
            headings.append(current)
        elif el.name in ("p", "li", "td", "th", "blockquote", "dd", "dt"):
            # skip containers whose content is already counted via a nested p/li
            if el.find(["p", "li", "td", "th", "blockquote"]):
                continue
            text = _clean(el.get_text(" "))
            if not text:
                continue
            paragraphs.append(text)
            if current is not None:
                current["words"] += count_words(text)
    body_text = "\n".join(paragraphs)
    title = _clean(soup.title.get_text()) if soup.title else ""
    return {
        "url": url,
        "title": title,
        "word_count": count_words("\n".join([h["text"] for h in headings] + paragraphs)),
        "body_words": count_words(body_text),
        "headings": headings,
        "text": body_text,
        "fact_tables": extract_fact_rows(root),
    }


def fetch_competitor(url: str, html_dir: Path | None = None) -> dict:
    try:
        page = parse_page(fetch_html(url, html_dir), url)
        page["ok"] = True
    except Exception as e:  # keep going with remaining competitors
        page = {"url": url, "ok": False, "error": str(e), "word_count": 0, "headings": [], "text": ""}
    return page
