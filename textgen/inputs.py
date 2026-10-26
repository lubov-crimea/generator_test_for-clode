"""Input parsing: JSON or the plain-text format used in the task description."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path

URL_RE = re.compile(r"https?://\S+")

# brand-review  - the general review page of ONE brand (home page of a brand site)
# brand-subpage - a focused page of ONE brand about one topic (login, app, VIP programme, sports, bonuses, payments ...)
# top-list      - a ranking/comparison page of SEVERAL casinos for a query ("best online casinos", "fast withdrawal casinos")
PAGE_TYPES = ("brand-review", "brand-subpage", "top-list")
TOP_LIST_MIN_CASINOS = 2


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


@dataclass
class Job:
    geo: str
    keywords: list[str]
    competitors: list[str]
    language: str | None = None  # ISO code, e.g. "en"; inferred from GEO if empty
    facts: list[str] = field(default_factory=list)  # optional facts every block must stay consistent with
    brand: str | None = None  # brand name; defaults to the first keyword (review pages only, see `brand_name`)
    knowledge_base: str | None = None  # title of the AffBulk knowledge base with the brand information
    page_type: str = "brand-review"
    slug: str | None = None  # name of the run folder; default `<first keyword>-<geo>` (see make_slug)
    # slugs of the internal pages of the site this page links to (textgen/sitemap.py); None = the base set (bonuses, app, promo-code, login,
    # no-deposit-bonus, payments) without the page itself
    site_pages: list[str] | None = None
    # top-list only: the casinos of the page in ranking order, [{"name", "slug", "knowledge_base"}]
    casinos: list[dict] = field(default_factory=list)

    @property
    def brand_name(self) -> str:
        """The tracked brand. A review page takes it from the first keyword when `Brand` is not given; a top list has no brand."""
        if self.page_type == "top-list":
            return self.brand or ""
        return self.brand or self.keywords[0]

    def to_dict(self) -> dict:
        return asdict(self)


def _split_keywords(raw: str) -> list[str]:
    seen: dict[str, None] = {}
    for part in re.split(r"[,\n;]", raw):
        part = part.strip()
        if part:
            seen.setdefault(part, None)
    return list(seen)


def _casino(raw: str) -> dict:
    """`Name | knowledge base title` (a leading bullet is ignored)."""
    raw = re.sub(r"^\s*[-*•]\s*", "", raw)
    name, _, kb = raw.partition("|")
    name = name.strip()
    return {"name": name, "slug": slugify(name), "knowledge_base": kb.strip() or None}


def parse_text(text: str) -> Job:
    """Format:
        GEO - Australia
        Keywords - kw1, kw2, ...
        Competitors:
        https://a.com/
        https://b.com/

    Optional: `Site pages - bonuses, app, login` (the internal pages this page links to; default: the base set bonuses, app, promo-code,
    login, no-deposit-bonus, payments), `Page type - brand-review | brand-subpage | top-list`, and for a top list the casinos in ranking order:
        Casinos:
        - Incaspin | incaspin-new
        - Longfu88 | longfu88-new
    (one casino per line, `Casino - Name | knowledge base` works as well).
    """
    geo = ""
    keywords: list[str] = []
    competitors: list[str] = []
    casinos: list[dict] = []
    language = None
    brand = None
    knowledge_base = None
    page_type = "brand-review"
    slug = None
    site_pages: list[str] | None = None
    facts: list[str] = []
    in_competitors = in_casinos = False
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if m := re.match(r"(?i)^geo\s*[-:–]\s*(.+)$", line):
            geo, in_competitors, in_casinos = m.group(1).strip(), False, False
        elif m := re.match(r"(?i)^lang(?:uage)?\s*[-:–]\s*(.+)$", line):
            language, in_competitors, in_casinos = m.group(1).strip().lower(), False, False
        elif m := re.match(r"(?i)^(?:page[\s_-]*)?type\s*[-:–]\s*(.+)$", line):
            page_type, in_competitors, in_casinos = re.sub(r"[\s_]+", "-", m.group(1).strip().lower()), False, False
        elif m := re.match(r"(?i)^(?:run[\s_-]*)?slug\s*[-:–]\s*(.+)$", line):
            slug, in_competitors, in_casinos = slugify(m.group(1)), False, False
        elif m := re.match(r"(?i)^site[\s_-]*pages\s*[-:–]\s*(.*)$", line):
            site_pages, in_competitors, in_casinos = [slugify(s) for s in re.split(r"[,;]", m.group(1)) if s.strip()], False, False
        elif m := re.match(r"(?i)^(?:knowledge[\s_-]*base|kb)\s*[-:–]\s*(.+)$", line):
            knowledge_base, in_competitors, in_casinos = m.group(1).strip(), False, False
        elif m := re.match(r"(?i)^brand\s*[-:–]\s*(.+)$", line):
            brand, in_competitors, in_casinos = m.group(1).strip(), False, False
        elif m := re.match(r"(?i)^facts?\s*[-:–]\s*(.+)$", line):
            facts.append(m.group(1).strip())
            in_competitors = in_casinos = False
        elif m := re.match(r"(?i)^key\w*\s*[-:–]\s*(.+)$", line):
            keywords = _split_keywords(m.group(1))
            in_competitors = in_casinos = False
        elif re.match(r"(?i)^casinos?\s*[-:–]?\s*$", line):
            in_casinos, in_competitors = True, False
        elif m := re.match(r"(?i)^casinos?\s*[-:–]\s*(.+)$", line):
            casinos.append(_casino(m.group(1)))
            in_casinos, in_competitors = True, False
        elif re.match(r"(?i)^competitors?\s*[-:–]?\s*$", line):
            in_competitors, in_casinos = True, False
        elif m := re.match(r"(?i)^competitors?\s*[-:–]\s*(.+)$", line):
            competitors += URL_RE.findall(m.group(1))
            in_competitors, in_casinos = True, False
        elif in_casinos:
            casinos.append(_casino(line))
        elif in_competitors or URL_RE.match(line):
            competitors += URL_RE.findall(line)
    return _validate(Job(geo=geo, keywords=keywords, competitors=competitors, language=language, facts=facts, brand=brand,
                     knowledge_base=knowledge_base, page_type=page_type, slug=slug, casinos=casinos, site_pages=site_pages))


def parse_json(text: str) -> Job:
    data = json.loads(text)
    kws = data.get("keywords", [])
    if isinstance(kws, str):
        kws = _split_keywords(kws)
    casinos = [_casino(c) if isinstance(c, str) else {"name": c.get("name", "").strip(), "slug": c.get("slug") or slugify(c.get("name", "")),
                                                      "knowledge_base": c.get("knowledge_base") or None}
               for c in data.get("casinos", [])]
    return _validate(
        Job(
            geo=data.get("geo", "").strip(),
            keywords=[k.strip() for k in kws if k.strip()],
            competitors=[c.strip() for c in data.get("competitors", []) if c.strip()],
            language=(data.get("language") or None),
            facts=data.get("facts", []),
            brand=data.get("brand") or None,
            knowledge_base=data.get("knowledge_base") or None,
            page_type=data.get("page_type") or "brand-review",
            slug=slugify(data["slug"]) if data.get("slug") else None,
            casinos=casinos,
            site_pages=[slugify(s) for s in data["site_pages"]] if data.get("site_pages") is not None else None,
        )
    )


def _validate(job: Job) -> Job:
    missing = [n for n, v in (("geo", job.geo), ("keywords", job.keywords), ("competitors", job.competitors)) if not v]
    if missing:
        raise ValueError(f"Input is missing: {', '.join(missing)}")
    if job.page_type not in PAGE_TYPES:
        raise ValueError(f'Unknown page type "{job.page_type}" (allowed: {", ".join(PAGE_TYPES)})')
    if job.page_type == "brand-subpage" and not job.brand:
        raise ValueError("A brand-subpage needs `Brand - <name>`: the first keyword names the topic of the page ('Longfu88 login'), "
                         "so the brand cannot be taken from it")
    if job.page_type == "top-list":
        if len(job.casinos) < TOP_LIST_MIN_CASINOS:
            raise ValueError(f"A top-list needs at least {TOP_LIST_MIN_CASINOS} casinos (`Casinos:` + one `Name | knowledge base` line each)")
        for c in job.casinos:
            if not c["name"] or not c["slug"]:
                raise ValueError(f"A casino has no name: {c}")
            if not c["knowledge_base"]:
                raise ValueError(f'Casino "{c["name"]}" has no knowledge base: write `{c["name"]} | <knowledge base title in AffBulk>`')
        slugs = [c["slug"] for c in job.casinos]
        if len(set(slugs)) != len(slugs):
            raise ValueError("Casino names must be different: " + ", ".join(slugs))
        if job.knowledge_base:
            raise ValueError("A top-list takes its facts from the knowledge bases of the casinos: remove the `Knowledge Base` line")
    elif job.casinos:
        raise ValueError("`Casinos` belong to a top-list (`Page type - top-list`)")
    return job


def load_job(path: str | Path) -> Job:
    path = Path(path)
    text = path.read_text(encoding="utf-8-sig")
    return parse_json(text) if path.suffix.lower() == ".json" else parse_text(text)


def make_slug(job: Job) -> str:
    """Run folder name: `Slug` of the input, else `<first keyword>-<geo>`. Several pages of one brand and GEO (login, app, ...) share
    the first keyword, so a brand-subpage input gives its own `Slug`."""
    if job.slug:
        return job.slug
    base = f"{job.keywords[0]}-{job.geo}"
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-") or "run"
