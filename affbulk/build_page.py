"""Build the AffBulk `pages_create` payload from a finished run.

    python -m affbulk.build_page <run>            # runs/<run>/04_final.json + runs/<run>/05_affbulk_config.json
                                                  #   -> runs/<run>/05_affbulk_page.json  (the `data` argument of pages_create)

The layout rules live in prompts/affbulk_import.md; this module only applies them mechanically:
Hero -> 3 x Swiper -> Preview -> Article (intro) -> [CTA] Article ... -> Reviews 2 -> FAQ -> Promo.
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

from .links import check_anchors, wrap_phrase

RUNS_DIR = Path(__file__).resolve().parent.parent / "runs"
LINK = "{{rezerv_casino}}"
CTA_COUNT = 5

# Game tiles are brand-neutral and identical on every site: media ids from the shared Media Library folders 45 / 46 / 47.
SWIPERS = {
    "slots": [
        ("Mega Moolah", 99), ("StarBurst", 73), ("Sweet Bonanza", 100), ("Big Bass Bonanza", 72), ("Razor Shark", 83),
        ("Book of Dead", 109), ("Buffalo King Megaways", 91), ("Sugar Rush", 87), ("Wolf Gold", 106),
        ("Gates Of Olympus 1000", 84), ("The Dog House", 92), ("3 Hot Chilli Peppers", 107),
    ],
    "crash": [
        ("Aviamasters", 78), ("Aviator", 89), ("Aviatrix", 77), ("Ballonix", 81), ("Balloon", 86), ("Big Bass Crash", 88),
        ("Chicken Road", 97), ("F777 Fighters", 108), ("JetX", 70), ("Lucky Jet", 104), ("Penalty Shoot Out", 90),
        ("Piggy Tap", 82),
    ],
    "live": [
        ("American Roulette", 2628), ("Crazy Balls", 2630), ("Crazy Time", 2208), ("Ice Fishing", 102),
        ("Infinite Blackjack", 2626), ("Sweet Bonanza", 235),
    ],
}

LOCALES = {
    "en": {
        "register": "Register", "play": "Play Now", "claim": "Claim Bonus", "join": "Join Now", "bonus_cta": "Get Your Bonus",
        "swipers": ["Top Slots", "Crash & Instant", "Live"], "reviews": "Real Player Reviews", "faq": "FAQ",
        "disclaimer": "18+. T&Cs apply. Gamble responsibly.",
    },
    "pl": {
        "register": "Zarejestruj się", "play": "Graj teraz", "claim": "Odbierz bonus", "join": "Dołącz teraz", "bonus_cta": "Sprawdź bonus",
        "swipers": ["Najlepsze sloty", "Crash i gry błyskawiczne", "Na żywo"], "reviews": "Opinie graczy", "faq": "Najczęstsze pytania",
        "disclaimer": "18+. Obowiązują warunki i zasady. Graj odpowiedzialnie.",
    },
    "it": {
        "register": "Registrati", "play": "Gioca ora", "claim": "Ottieni il bonus", "join": "Unisciti ora", "bonus_cta": "Scopri il bonus",
        "swipers": ["Slot top", "Crash e giochi istantanei", "Live"], "reviews": "Recensioni dei giocatori", "faq": "Domande frequenti",
        "disclaimer": "18+. Si applicano termini e condizioni. Gioca responsabilmente.",
    },
    "no": {
        "register": "Registrer deg", "play": "Spill nå", "claim": "Hent bonus", "join": "Bli med nå", "bonus_cta": "Se bonusen",
        "swipers": ["Toppslots", "Crash og instant", "Live"], "reviews": "Spillernes meninger", "faq": "Ofte stilte spørsmål",
        "disclaimer": "18+. Vilkår gjelder. Spill ansvarlig.",
    },
    "uk": {
        "register": "Зареєструватися", "play": "Грати зараз", "claim": "Отримати бонус", "join": "Приєднатися", "bonus_cta": "Забрати бонус",
        "swipers": ["Топ-слоти", "Crash та миттєві ігри", "Live"], "reviews": "Відгуки гравців", "faq": "Поширені запитання",
        "disclaimer": "18+. Діють умови та положення. Грайте відповідально.",
    },
    "id": {
        "register": "Daftar", "play": "Main Sekarang", "claim": "Klaim Bonus", "join": "Gabung Sekarang", "bonus_cta": "Dapatkan Bonus",
        "swipers": ["Slot Teratas", "Crash & Game Instan", "Live Casino"], "reviews": "Ulasan Pemain", "faq": "FAQ",
        "disclaimer": "18+. Syarat dan ketentuan berlaku. Bermainlah dengan bijak.",
    },
    "ms": {
        "register": "Daftar", "play": "Main Sekarang", "claim": "Tuntut Bonus", "join": "Sertai Sekarang", "bonus_cta": "Dapatkan Bonus",
        "swipers": ["Slot Teratas", "Crash & Permainan Pantas", "Kasino Langsung"], "reviews": "Ulasan Pemain", "faq": "Soalan Lazim",
        "disclaimer": "18+. Terma dan syarat terpakai. Bermain secara bertanggungjawab.",
    },
    "vi": {
        "register": "Đăng ký", "play": "Chơi ngay", "claim": "Nhận thưởng", "join": "Tham gia ngay", "bonus_cta": "Nhận ưu đãi",
        "swipers": ["Slot hàng đầu", "Crash & game nhanh", "Live casino"], "reviews": "Đánh giá của người chơi", "faq": "Câu hỏi thường gặp",
        "disclaimer": "18+. Áp dụng điều khoản và điều kiện. Hãy chơi có trách nhiệm.",
    },
    "th": {
        "register": "สมัครสมาชิก", "play": "เล่นเลย", "claim": "รับโบนัส", "join": "เข้าร่วมเลย", "bonus_cta": "ดูโบนัส",
        "swipers": ["สล็อตยอดนิยม", "เกมแครชและเกมด่วน", "คาสิโนสด"], "reviews": "รีวิวจากผู้เล่น", "faq": "คำถามที่พบบ่อย",
        "disclaimer": "18+ ใช้เงื่อนไขและข้อกำหนด เล่นอย่างรับผิดชอบ",
    },
}


def button(text: str, variant: str = "main") -> dict:
    return {"variant": variant, "link": LINK, "text": text, "linkStatus": "affiliate"}


# ---------------------------------------------------------------- markdown -> html
def _inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return s


def _table(rows: list[str]) -> str:
    out = ["<table>"]
    for i, row in enumerate(rows):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        out.append("<tr>\n" + "\n".join(f"<td>{_inline(c)}</td>" for c in cells) + "\n</tr>")
    out.append("</table>")
    return "\n".join(out)


def md_to_html(text: str) -> str:
    """Paragraphs, `- ` lists, `1. ` lists and `| |` tables (the only formats textgen produces)."""
    lines = text.strip().splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
        elif line.lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            out.append(_table(lines[i:j]))
            i = j
        elif re.match(r"^\s*[-*]\s+", line):
            j = i
            items = []
            while j < len(lines) and re.match(r"^\s*[-*]\s+", lines[j]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[j]).strip())
                j += 1
            out.append("<ul>\n" + "\n".join(f"<li>{_inline(x)}</li>" for x in items) + "\n</ul>")
            i = j
        elif re.match(r"^\s*\d+[.)]\s+", line):
            j = i
            items = []
            while j < len(lines) and re.match(r"^\s*\d+[.)]\s+", lines[j]):
                items.append(re.sub(r"^\s*\d+[.)]\s+", "", lines[j]).strip())
                j += 1
            out.append("<ol>\n" + "\n".join(f"<li>{_inline(x)}</li>" for x in items) + "\n</ol>")
            i = j
        else:
            j = i
            para = []
            while j < len(lines) and lines[j].strip() and not lines[j].lstrip().startswith("|") \
                    and not re.match(r"^\s*([-*]|\d+[.)])\s+", lines[j]):
                para.append(lines[j].strip())
                j += 1
            out.append("<p>" + _inline(" ".join(para)) + "</p>")
            i = j
    return "\n".join(out)


FAQ_ITEM = re.compile(r"^\s*[-*]\s+\*\*(.+?)\*\*\s*(.*)$")


def parse_faq(text: str) -> list[dict] | None:
    """`- **Question?** Answer` lines -> [{question, answer}]; None when the block is not in that shape."""
    items = []
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        if not items and not re.match(r"^\s*[-*]\s+", line):
            continue  # a one-sentence lead-in before the first question is not part of the FAQ block
        m = FAQ_ITEM.match(line)
        if not m or not m.group(2).strip():
            return None
        items.append({"question": m.group(1).strip(), "answer": m.group(2).strip()})
    return items if len(items) >= 3 else None


# ---------------------------------------------------------------- page
def cta_positions(n_h2: int, count: int = CTA_COUNT) -> list[int]:
    """Indexes (into the list of H2 sections) that get a CTA right before them: evenly spread, the first one before the first H2."""
    if n_h2 <= count:
        return list(range(n_h2))
    return sorted({round(i * n_h2 / count) for i in range(count)})


def build_page(final: dict, cfg: dict) -> dict:
    lang = cfg.get("locale") or final.get("language") or "en"
    loc = LOCALES[lang]
    blocks = final["blocks"]
    h1 = next(b for b in blocks if b["level"] == 1)
    body = [b for b in blocks if b is not h1]

    faq_block = None
    sections = []
    for b in body:
        faq = parse_faq(b["text"]) if "list" in (b.get("formats") or []) else None
        if faq and faq_block is None and b["level"] == 2:
            faq_block = (b, faq)
        else:
            sections.append(b)

    content: list[dict] = []
    hero = cfg["hero"]
    content.append({
        "__component": "blocks.hero", "title": h1["heading"], "label": hero["label"], "mainLabel": hero.get("mainLabel") or "",
        "background": hero["background"], "buttons": [button(hero.get("button") or loc["register"])],
    })
    for title, key in zip(cfg.get("swiper_titles") or loc["swipers"], ("slots", "crash", "live")):
        content.append({
            "__component": "blocks.swiper", "title": title, "variant": "small",
            "blocks": [{"description": name, "image": img, "button": button(loc["play"])} for name, img in (cfg.get("swipers") or SWIPERS)[key]],
        })
    pv = cfg["preview"]
    content.append({
        "__component": "blocks.preview", "title": pv["title"],
        "items": [{
            "image": it["image"],
            "content": f"<h3><strong>{html.escape(it['title'], quote=False)}</strong></h3>\n{html.escape(it['text'], quote=False)}" if it.get("title") else "",
            "buttons": [button(it.get("button") or loc["claim"])],
        } for it in pv["items"]],
    })
    content.append({"__component": "blocks.article", "article": md_to_html(h1["text"])})

    h2_idx = [i for i, b in enumerate(sections) if b["level"] == 2]
    cta_before = {h2_idx[p] for p in cta_positions(len(h2_idx))}
    cta_texts = cfg.get("cta_texts") or [loc["claim"], loc["play"], loc["register"], loc["bonus_cta"], loc["join"]]
    n_cta = 0
    for i, b in enumerate(sections):
        if i in cta_before:
            content.append({"__component": "blocks.call-to-action", "buttons": [button(cta_texts[n_cta % len(cta_texts)])]})
            n_cta += 1
        tag = f"h{b['level']}"
        content.append({"__component": "blocks.article", "article": f"<{tag}>{html.escape(b['heading'], quote=False)}</{tag}>\n{md_to_html(b['text'])}"})

    apply_internal_links(content, cfg)  # home page: a short anchor for every internal page (config `internal_links`)
    rv = cfg["reviews"]
    content.append({"__component": "blocks.reviews-2", "title": rv.get("title") or loc["reviews"], "reviews": [
        {"username": r["username"], "review": r["review"], "date": r["date"], "avatar": r["avatar"],
         "rating": {"ratingValue": r.get("rating", 5), "bestRating": 5}} for r in rv["items"]]})
    if faq_block:
        b, faq = faq_block
        content.append({"__component": "blocks.faq", "title": b["heading"], "faqs": faq})
    elif cfg.get("faq"):  # the text has no FAQ section: Claude writes the pairs from facts already stated in the text
        content.append({"__component": "blocks.faq", "title": cfg["faq"].get("title") or loc["faq"], "faqs": cfg["faq"]["items"]})
    pr = cfg["promo"]
    content.append({
        "__component": "blocks.promo", "title": pr["title"], "description": pr["description"], "disclaimer": pr.get("disclaimer") or loc["disclaimer"],
        "image": pr.get("image") or hero["background"], "buttons": [button(pr.get("button") or loc["claim"])],
    })

    seo = {"title": cfg["seo"]["title"], "description": cfg["seo"]["description"], "index": True}
    for k in ("customCanonical", "customPageLang"):  # multi-language sites: canonical to itself, page language
        if cfg["seo"].get(k):
            seo[k] = cfg["seo"][k]
    data = {
        "website": cfg["website_id"], "slug": cfg.get("slug", "index"), "seo": seo,
        "keywords": {"mainKeywords": cfg["keywords"]["main"], "additionalKeywords": cfg["keywords"]["additional"]},
        "tableOfContent": False, "content": content,
    }
    if cfg.get("customHeadHTML"):  # hreflang links
        data["customHeadHTML"] = cfg["customHeadHTML"]
    return data


def link_anchor(content: list[dict], anchor: str, href: str) -> None:
    """Wrap the first mention of `anchor` in the running text of an article with an internal link (see `links.wrap_phrase`: at most
    3 words, headings and existing links are skipped, nothing is added to the text; raises when the anchor is not in the text)."""
    wrap_phrase(content, anchor, href, what="home link anchor")


def apply_internal_links(content: list[dict], cfg: dict) -> None:
    """Config `internal_links`: [{"anchor", "href"}] - short phrases (at most 3 words) of the running text that become links to other pages."""
    for l in cfg.get("internal_links") or []:
        wrap_phrase(content, l["anchor"], l["href"], what="internal link anchor")


SUBPAGE_CTA_COUNT = 2


def build_subpage(final: dict, cfg: dict) -> dict:
    """A focused page of a brand (brand-subpage: login, app, VIP, payments ...): Hero -> [Preview, only for bonus pages] -> Article (intro) ->
    [CTA] Article ... -> FAQ -> Promo. No Swiper, no Reviews. Two CTA (`SUBPAGE_CTA_COUNT`) stand before an H2 article, spread evenly
    (the first before the first H2). The link to the home page is the brand name in the running text (`home_link.anchor`)."""
    lang = cfg.get("locale") or final.get("language") or "en"
    loc = LOCALES[lang]
    blocks = final["blocks"]
    h1 = next(b for b in blocks if b["level"] == 1)
    faq_block, sections = None, []
    for b in (b for b in blocks if b is not h1):
        faq = parse_faq(b["text"]) if "list" in (b.get("formats") or []) else None
        if faq and faq_block is None and b["level"] == 2:
            faq_block = (b, faq)
        else:
            sections.append(b)

    hero = cfg["hero"]
    content: list[dict] = [{
        "__component": "blocks.hero", "title": h1["heading"], "label": hero["label"], "mainLabel": hero.get("mainLabel") or "",
        "background": hero["background"], "buttons": [button(hero.get("button") or loc["register"])],
    }]
    if cfg.get("preview"):  # bonus / promo code pages only
        pv = cfg["preview"]
        content.append({"__component": "blocks.preview", "title": pv["title"], "items": [{
            "image": it["image"],
            "content": f"<h3><strong>{html.escape(it['title'], quote=False)}</strong></h3>\n{html.escape(it['text'], quote=False)}" if it.get("title") else "",
            "buttons": [button(it.get("button") or loc["claim"])]} for it in pv["items"]]})
    content.append({"__component": "blocks.article", "article": md_to_html(h1["text"])})
    h2_idx = [i for i, b in enumerate(sections) if b["level"] == 2]
    cta_before = {h2_idx[p] for p in cta_positions(len(h2_idx), SUBPAGE_CTA_COUNT)}
    cta_texts = cfg.get("cta_texts") or [loc["register"], loc["play"], loc["join"], loc["claim"], loc["bonus_cta"]]
    n_cta = 0
    for i, b in enumerate(sections):
        if i in cta_before:
            content.append({"__component": "blocks.call-to-action", "buttons": [button(cta_texts[n_cta % len(cta_texts)])]})
            n_cta += 1
        tag = f"h{b['level']}"
        content.append({"__component": "blocks.article", "article": f"<{tag}>{html.escape(b['heading'], quote=False)}</{tag}>\n{md_to_html(b['text'])}"})
    if cfg.get("home_link"):  # the brand name in the running text becomes the one internal link to the home page; no extra paragraph
        hl = cfg["home_link"]
        link_anchor(content, hl["anchor"], hl.get("href", "/"))
    apply_internal_links(content, cfg)
    if faq_block:
        b, faq = faq_block
        content.append({"__component": "blocks.faq", "title": b["heading"], "faqs": faq})
    elif cfg.get("faq"):
        content.append({"__component": "blocks.faq", "title": cfg["faq"].get("title") or loc["faq"], "faqs": cfg["faq"]["items"]})
    pr = cfg["promo"]
    content.append({
        "__component": "blocks.promo", "title": pr["title"], "description": pr["description"], "disclaimer": pr.get("disclaimer") or loc["disclaimer"],
        "image": pr.get("image") or hero["background"], "buttons": [button(pr.get("button") or loc["claim"])],
    })
    seo = {"title": cfg["seo"]["title"], "description": cfg["seo"]["description"], "index": True}
    return {"website": cfg["website_id"], "slug": cfg["slug"], "seo": seo,
            "keywords": {"mainKeywords": cfg["keywords"]["main"], "additionalKeywords": cfg["keywords"]["additional"]},
            "tableOfContent": False, "content": content}


def check_subpage(data: dict) -> list[str]:
    errs = []
    kinds = [b["__component"].split(".")[-1] for b in data["content"]]
    if kinds[0] != "hero":
        errs.append("first block is not Hero")
    if kinds[-1] != "promo":
        errs.append("last block is not Promo")
    for k in ("promo", "hero"):
        if kinds.count(k) != 1:
            errs.append(f"expected exactly one {k}, got {kinds.count(k)}")
    if kinds.count("faq") > 1:  # a variant text may have no FAQ section on purpose (its structure differs from the others): then no FAQ block
        errs.append(f"expected at most one faq, got {kinds.count('faq')}")
    for k in ("swiper", "reviews-2", "offer-list"):
        if k in kinds:
            errs.append(f"{k} is not used on a brand-subpage")
    h2 = sum(1 for b in data["content"] if b["__component"] == "blocks.article" and b["article"].startswith("<h2>"))
    want = min(SUBPAGE_CTA_COUNT, h2)
    if kinds.count("call-to-action") != want:
        errs.append(f"expected {want} CTA blocks, got {kinds.count('call-to-action')}")
    for i, b in enumerate(data["content"]):
        if b["__component"] == "blocks.call-to-action":
            nxt = data["content"][i + 1] if i + 1 < len(data["content"]) else {}
            if not nxt.get("article", "").startswith("<h2>"):
                errs.append(f"CTA at position {i} is not followed by an H2 article")
        for btn in b.get("buttons") or []:
            if btn.get("linkStatus") != "affiliate":
                errs.append(f"button without linkStatus at position {i}")
    return errs + check_anchors(data["content"])


def check_page(data: dict) -> list[str]:
    """Structural checks of the mandatory layout; returns a list of problems."""
    errs = []
    kinds = [b["__component"].split(".")[-1] for b in data["content"]]
    order = ["hero", "swiper", "preview", "article", "reviews-2", "promo"]
    if kinds[0] != "hero":
        errs.append("first block is not Hero")
    if kinds.count("swiper") != 3:
        errs.append(f"expected 3 Swiper blocks, got {kinds.count('swiper')}")
    if kinds.count("call-to-action") != CTA_COUNT:
        errs.append(f"expected {CTA_COUNT} CTA blocks, got {kinds.count('call-to-action')}")
    for k in ("preview", "reviews-2", "faq", "promo"):
        if kinds.count(k) != 1:
            errs.append(f"expected exactly one {k}, got {kinds.count(k)}")
    if kinds[-1] != "promo":
        errs.append("last block is not Promo")
    if "faq" in kinds and "reviews-2" in kinds and kinds.index("reviews-2") > kinds.index("faq"):
        errs.append("Reviews 2 must come before FAQ")
    for i, b in enumerate(data["content"]):
        if b["__component"] == "blocks.call-to-action":
            nxt = data["content"][i + 1] if i + 1 < len(data["content"]) else {}
            if not nxt.get("article", "").startswith("<h2>"):
                errs.append(f"CTA at position {i} is not followed by an H2 article")
        for btn in (b.get("buttons") or []) + [x.get("button") for x in b.get("blocks", []) if x.get("button")]:
            if btn.get("linkStatus") != "affiliate":
                errs.append(f"button without linkStatus at position {i}")
    for it in next((b for b in data["content"] if b["__component"] == "blocks.preview"), {}).get("items", []):
        if not it.get("image") or not it.get("buttons"):
            errs.append("Preview item without image or button")
    return errs + check_anchors(data["content"])


def main(argv: list[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 1:
        sys.exit("usage: python -m affbulk.build_page <run>")
    run = RUNS_DIR / argv[0]
    final = json.loads((run / "04_final.json").read_text(encoding="utf-8"))
    cfg = json.loads((run / "05_affbulk_config.json").read_text(encoding="utf-8"))
    subpage = final.get("page_type") == "brand-subpage"
    data = build_subpage(final, cfg) if subpage else build_page(final, cfg)
    errs = check_subpage(data) if subpage else check_page(data)
    out = run / "05_affbulk_page.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    kinds = [b["__component"].split(".")[-1] for b in data["content"]]
    print(f"{out}: {len(data['content'])} blocks, {len(json.dumps(data, ensure_ascii=False))} chars")
    print(" ".join(kinds))
    if errs:
        sys.exit("PROBLEMS:\n- " + "\n- ".join(errs))


if __name__ == "__main__":
    main()
