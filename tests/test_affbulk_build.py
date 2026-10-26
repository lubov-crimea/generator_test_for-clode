from affbulk.build_page import build_page, check_page, cta_positions, md_to_html, parse_faq

CFG = {
    "website_id": 1, "locale": "en",
    "seo": {"title": "T", "description": "D"},
    "keywords": {"main": "Brand", "additional": "casino"},
    "hero": {"label": "Bonus", "background": 10},
    "preview": {"title": "Bonuses", "items": [{"image": 11, "title": "Welcome", "text": "100% up to 500"}]},
    "reviews": {"items": [{"username": "A", "review": "Fine.", "date": "2026-10-21", "avatar": 5}]},
    "promo": {"title": "Promo", "description": "100%"},
}


def _final(n_h2: int = 8) -> dict:
    blocks = [{"level": 1, "heading": "Brand Casino", "text": "Intro text about Brand, a casino.", "formats": ["paragraph"]}]
    for i in range(n_h2):
        blocks.append({"level": 2, "heading": f"Section {i}", "text": f"Body {i}.", "formats": ["paragraph"]})
        if i == 1:
            blocks.append({"level": 3, "heading": "Sub", "text": "- a\n- b", "formats": ["list"]})
    blocks.append({"level": 2, "heading": "Questions", "formats": ["list"], "text": (
        "- **Q1?** A1.\n- **Q2?** A2.\n- **Q3?** A3.")})
    return {"language": "en", "blocks": blocks}


def test_layout_and_checks():
    data = build_page(_final(), CFG)
    assert check_page(data) == []
    kinds = [b["__component"].split(".")[-1] for b in data["content"]]
    assert kinds[:5] == ["hero", "swiper", "swiper", "swiper", "preview"]
    assert kinds.count("call-to-action") == 5
    assert kinds[-3:] == ["reviews-2", "faq", "promo"]
    assert data["content"][-2]["faqs"][0] == {"question": "Q1?", "answer": "A1."}


SUB_CFG = {
    "website_id": 2, "locale": "en", "slug": "login",
    "seo": {"title": "T", "description": "D"},
    "keywords": {"main": "Brand", "additional": "login"},
    "hero": {"label": "Log in", "background": 10, "button": "Log In"},
    "cta_texts": ["Log In", "Register"],
    "home_link": {"anchor": "Brand", "href": "/"},
    "promo": {"title": "Promo", "description": "100%"},
}


def test_brand_subpage_layout_has_no_swipers_reviews_or_preview():
    from affbulk.build_page import build_subpage, check_subpage

    data = build_subpage(_final(4), SUB_CFG)
    assert check_subpage(data) == []
    kinds = [b["__component"].split(".")[-1] for b in data["content"]]
    assert kinds[0] == "hero" and kinds[-1] == "promo" and kinds[-2] == "faq"
    assert not {"swiper", "reviews-2", "preview"} & set(kinds)
    assert kinds.count("call-to-action") == 2  # a brand-subpage has two CTA, the first before the first H2
    assert data["slug"] == "login"
    assert data["content"][1]["article"] == '<p>Intro text about <a href="/">Brand</a>, a casino.</p>'  # the brand in the intro is the home link
    assert sum('href="/"' in b.get("article", "") for b in data["content"]) == 1  # one link, no paragraph written for it
    assert data["content"][2]["__component"] == "blocks.call-to-action" and data["content"][3]["article"].startswith("<h2>")
    assert sum(b["__component"] == "blocks.call-to-action" for b in build_subpage(_final(9), SUB_CFG)["content"]) == 2
    assert sum(b["__component"] == "blocks.call-to-action" for b in build_subpage(_final(1), SUB_CFG)["content"]) == 1
    with_preview = build_subpage(_final(4), {**SUB_CFG, "preview": {"title": "Bonuses", "items": [{"image": 11, "title": "W", "text": "100%"}]}})
    assert with_preview["content"][1]["__component"] == "blocks.preview"  # only the bonus pages ask for it


def test_home_link_skips_headings_links_and_fails_without_anchor():
    from affbulk.build_page import build_subpage, link_anchor

    content = [{"__component": "blocks.article", "article": "<h2>Brand login</h2>\n<p>See <a href=\"/x\">Brand</a> and Brand again. Brandy.</p>"}]
    link_anchor(content, "Brand", "/")
    assert content[0]["article"] == '<h2>Brand login</h2>\n<p>See <a href="/x">Brand</a> and <a href="/">Brand</a> again. Brandy.</p>'
    import pytest
    with pytest.raises(ValueError, match="not in the running text"):
        link_anchor(content, "Other", "/")
    final = _final(3)
    final["blocks"][0]["text"] = "Intro without the name."
    final["blocks"][2]["text"] = "Body mentions Brand here."
    assert '<a href="/">Brand</a>' in build_subpage(final, SUB_CFG)["content"][4]["article"]  # not in the intro: the first section that has it


def test_cta_positions_spread_and_short_pages():
    assert cta_positions(10) == [0, 2, 4, 6, 8]
    assert cta_positions(10, 2) == [0, 5]
    assert cta_positions(3) == [0, 1, 2]


def test_markdown_conversion():
    out = md_to_html("Para **bold**.\n\n- a\n- b\n\n1. x\n2. y\n\n| H1 | H2 |\n|---|---|\n| v1 | v2 |")
    assert "<p>Para <strong>bold</strong>.</p>" in out
    assert "<ul>\n<li>a</li>\n<li>b</li>\n</ul>" in out
    assert "<ol>" in out and "<td>v2</td>" in out and "---" not in out


def test_faq_needs_question_answer_shape():
    assert parse_faq("- a\n- b\n- c") is None
    assert len(parse_faq("- **Q1?** A.\n- **Q2?** B.\n- **Q3?** C.")) == 3
