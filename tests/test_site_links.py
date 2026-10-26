import pytest

from affbulk.build_page import build_page, build_subpage, check_page, check_subpage
from affbulk.links import check_anchors, internal_links, site_link_report, wrap_phrase
from affbulk.menu import plan_menu
from textgen.inputs import Job, parse_text
from textgen.sitemap import (BASE_SITE_PAGES, attach_internal_links, internal_link_note, own_slug, short_label, site_pages_for, topic_of)

from tests.test_affbulk_build import CFG, SUB_CFG, _final


def aff(text):
    return {"text": text, "link": "{{rezerv_casino}}", "linkStatus": "affiliate"}


def test_topic_and_short_label():
    assert topic_of("Promotions") == "bonuses" and topic_of("Longfu88 Login") == "login" and topic_of("Longfu88 App") == "app"
    assert topic_of("No Deposit Bonus") == "no-deposit-bonus" and topic_of("Promo Code") == "promo-code" and topic_of("Casino") is None
    assert topic_of("Payments") == "payments"
    assert short_label("Longfu88 Bonuses", "Longfu88") == "Bonuses" and short_label("Longfu88", "Longfu88") == "Longfu88"


def test_menu_replaces_same_topic_shortens_and_limits_header_to_six():
    header = [aff(t) for t in ("Promotions", "Casino", "Live Casino", "Sports", "Live Betting")]
    footer = [aff(t) for t in ("Casino", "Promotions", "About Us")]
    for slug, label in (("login", "Longfu88 Login"), ("app", "Longfu88 App"), ("bonuses", "Longfu88 Bonuses")):
        header, footer, log = plan_menu(header, footer, brand="Longfu88", slug=slug, label=label)
        assert len(header) <= 6
    assert [x["text"] for x in header] == ["Bonuses", "Casino", "Live Casino", "Sports", "Login", "App"]
    assert header[0] == {"text": "Bonuses", "link": "/bonuses", "linkStatus": "internal"}  # Promotions is replaced in place, not duplicated
    assert [x["text"] for x in footer] == ["Casino", "Bonuses", "About Us", "Live Betting"]  # the affiliate analog became the internal link
    assert footer[1]["linkStatus"] == "internal" and footer[1]["link"] == "/bonuses"
    again, _, log = plan_menu(header, footer, brand="Longfu88", slug="bonuses", label="Longfu88 Bonuses")
    assert again == header and "already there" in log[0]  # idempotent


def test_menu_keeps_three_affiliate_items_and_sends_the_rest_to_the_footer():
    header = [aff("Casino"), aff("Live Casino"), aff("Sports")] + [
        {"text": t, "link": f"/{s}", "linkStatus": "internal"} for t, s in (("Bonuses", "bonuses"), ("Login", "login"), ("App", "app"))]
    h, f, log = plan_menu(header, [], brand="X", slug="payments", label="X Payments")
    assert h == header and f == [{"text": "Payments", "link": "/payments", "linkStatus": "internal"}]
    # internal items that still carry the brand are shortened
    h, f, _ = plan_menu([{"text": "X Login", "link": "/login", "linkStatus": "internal"}], [], brand="X", slug="app", label="X App")
    assert [x["text"] for x in h] == ["Login", "App"]


def test_anchor_limit_three_words_and_site_report():
    content = [{"__component": "blocks.article", "article": "<p>The Longfu88 bonus for newly registered players and a Longfu caino login.</p>"}]
    with pytest.raises(ValueError, match="more than 3 words"):
        wrap_phrase(content, "Longfu88 bonus for newly registered players", "/bonuses")
    wrap_phrase(content, "Longfu88 bonus", "/bonuses")
    wrap_phrase(content, "Longfu caino login", "/login")
    assert internal_links(content) == [("Longfu88 bonus", "/bonuses"), ("Longfu caino login", "/login")]
    assert check_anchors(content) == []
    long = [{"__component": "blocks.article", "article": '<p><a href="/bonuses">one two three four</a></p>'}]
    assert "4 words" in check_anchors(long)[0]

    inner = [{"__component": "blocks.article", "article": '<p><a href="/">Brand</a> login.</p>'}]
    assert site_link_report({"index": content, "login": inner, "bonuses": inner}) == []
    assert site_link_report({"index": content, "app": inner}) == ["index: no link to /app"]
    assert site_link_report({"index": content, "login": [{"__component": "blocks.article", "article": "<p>none</p>"}]}) == [
        "login: no link to the home page"]


def test_builders_apply_internal_links_and_reject_long_anchors():
    final = _final(8)
    final["blocks"][0]["text"] = "Brand has a login page and a welcome offer in the app."
    cfg = {**CFG, "internal_links": [{"anchor": "login page", "href": "/login"}, {"anchor": "welcome offer", "href": "/bonuses"}]}
    data = build_page(final, cfg)
    assert check_page(data) == []
    assert sorted(h for _, h in internal_links(data["content"])) == ["/bonuses", "/login"]
    sub = build_subpage(final, {**SUB_CFG, "internal_links": [{"anchor": "the app", "href": "/app"}]})
    assert check_subpage(sub) == [] and ("the app", "/app") in internal_links(sub["content"]) and ("Brand", "/") in internal_links(sub["content"])
    with pytest.raises(ValueError, match="more than 3 words"):
        build_page(final, {**CFG, "internal_links": [{"anchor": "a login page and a welcome offer", "href": "/login"}]})


def _brief():
    def b(i, level, heading, summary=""):
        return {"id": f"b{i:02d}", "level": level, "heading": heading, "summary": summary}
    return {"blocks": [b(1, 1, "Brand Casino Review"), b(2, 2, "Registration and Login"), b(3, 2, "Welcome Bonus"),
                       b(4, 2, "Mobile Version", "The app on iOS and Android"), b(5, 2, "Banking")]}


def test_attach_internal_links_plants_each_page_where_its_topic_is_named():
    brief = _brief()
    placed = attach_internal_links(brief, ["login", "bonuses", "app", "payments", "promo-code"], required=True)
    assert placed == {"login": "b02", "bonuses": "b03", "app": "b04", "payments": "b05", "promo-code": "b01"}  # no promo block: the intro
    note = internal_link_note(brief["blocks"][1])
    assert "required" in note and "/login" in note and "at most 3 words" in note
    sub = _brief()
    placed = attach_internal_links(sub, ["login", "promo-code"], required=False)
    assert placed == {"login": "b02"} and "optional" in internal_link_note(sub["blocks"][1])  # a subpage links only where the topic is named


def test_site_pages_default_and_input_line():
    review = parse_text("GEO - Malaysia\nKeywords - Longfu88, Longfu88 casino\nCompetitors:\nhttps://a.com/\n")
    assert review.site_pages is None and site_pages_for(review) == [p["slug"] for p in BASE_SITE_PAGES]
    sub = parse_text("GEO - Malaysia\nKeywords - Longfu88 login\nBrand - Longfu88\nPage type - brand-subpage\nCompetitors:\nhttps://a.com/\n")
    assert own_slug(sub.keywords) == "login" and "login" not in site_pages_for(sub) and "bonuses" in site_pages_for(sub)
    custom = parse_text("GEO - Malaysia\nKeywords - Longfu88\nSite pages - Bonuses, app\nCompetitors:\nhttps://a.com/\n")
    assert custom.site_pages == ["bonuses", "app"] and site_pages_for(custom) == ["bonuses", "app"]
    top = Job(geo="x", keywords=["best casinos"], competitors=["https://a.com/"], page_type="top-list")
    assert site_pages_for(top) == []
