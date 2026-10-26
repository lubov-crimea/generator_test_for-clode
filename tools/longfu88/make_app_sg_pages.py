"""Longfu88 app pages (brand-subpage, SG): the AffBulk configs and the payloads. Run from the project root:
    python tools/longfu88/make_app_sg_pages.py

For each variant vNN (runs/longfu88-app-sg-vNN, finished text in 04_final.json) the site is taken from tools/longfu88/domains.json
(geo sg, list order, index 1..12): app vNN -> site index ((NN-1+8) % 12)+1  (v01 -> 9, v04 -> 12, v05 -> 1, v12 -> 8).
  runs/longfu88-app-sg-vNN/05_affbulk_config.json  -> python -m affbulk.build_page -> 05_affbulk_page.json (pages_create `data`)
The home page update and the header (menus, home links) are made separately for all page types together.
Nothing is written to AffBulk here.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERO = 140  # hero image of the brand
BRAND = "Longfu88"

SG_SITES = [e for e in json.loads((ROOT / "tools/longfu88/domains.json").read_text(encoding="utf-8")) if e["geo"] == "sg"]
assert len(SG_SITES) == 12
ADDITIONAL = ("app, mobile casino, Android, iOS, home screen shortcut, mobile browser, smartphone, tablet, account access, "
              "customer support, casino, Singapore, SG, Singapore players")

# `links`: exact phrases (at most 3 words) of the finished text, wrapped on their first mention in the running text.
PAGES = {
    "v01": dict(
        title="Longfu88 App Quick Guide: Android and iOS Shortcut",
        description="Longfu88 mobile casino for Singapore players: add the site to an Android or iOS home screen, see what works on a phone, log in and fix common problems.",
        label="Add the casino to your phone's home screen",
        cta=["Register", "Play Now"], promo_button="Claim Bonus",
        links=[("pages on bonuses", "/bonuses"), ("Login", "/login")]),
    "v02": dict(
        title="Longfu88 on Android: Add the Casino Shortcut in Chrome",
        description="How Longfu88 works on Android and iOS: Chrome and Safari home screen steps, shortcut or browser tab, account safety, data collected and support contacts.",
        label="Android first: Chrome steps, iOS steps right below",
        cta=["Play Now", "Log In"], promo_button="Get Offer",
        links=[("bonuses", "/bonuses"), ("login page", "/login")]),
    "v03": dict(
        title="Longfu App Checklist: Phone Setup for Singapore",
        description="Longfu app checklist for Singapore players: device check, iOS and Android shortcut, login, fixes, deposit methods, eligibility and support contacts.",
        label="Phone setup in one checklist",
        cta=["Log In", "Register"], promo_button="Claim Bonus",
        links=[("Login", "/login")]),
    "v04": dict(
        title="Longfu88 Mobile Casino Guide for Beginners in Singapore",
        description="Beginner guide to the Longfu88 mobile casino in Singapore: what the site offers, Android and iOS shortcut steps, sign-in, account safety, fixes and help.",
        label="Four steps from first visit to first login on a phone",
        cta=["Join Now", "Play Now"], promo_button="Join Now",
        links=[("bonuses page", "/bonuses"), ("Login", "/login")]),
    "v05": dict(
        title="Longfu88 Shortcut or Mobile Site: Pick Your Route",
        description="Longfu88 on a phone: use a home-screen shortcut or a browser tab, check supported phones and browsers, register, sign in, cash out and fix common issues.",
        label="Shortcut or browser tab: pick your route",
        cta=["Register", "Claim Bonus"], promo_button="Get Offer",
        links=[("bonus offers", "/bonuses"), ("Login", "/login")]),
    "v06": dict(
        title="Longfu88 Mobile Safety: Account Protection on a Phone",
        description="Longfu88 mobile casino safety for Singapore players: account protection, data the site collects, safe sign-in, identity checks, responsible play and support.",
        label="Use the casino on a phone with the account protected",
        cta=["Play Now", "Join Now"], promo_button="Claim Bonus",
        links=[("bonuses", "/bonuses"), ("login page", "/login")]),
    "v07": dict(
        title="Longfu88 Mobile Help: Quick Fixes and Phone Setup",
        description="Longfu88 mobile help: fix common phone problems, add the shortcut again on Android or iOS, sign-in trouble, games, SGD deposit methods and support contacts.",
        label="Phone not working? Start with the quick fixes",
        cta=["Log In", "Claim Bonus"], promo_button="Claim Offer",
        links=[("bonuses page", "/bonuses"), ("Login", "/login")]),
    "v08": dict(
        title="Longfu88 Mobile Casino Handbook for Singapore Players",
        description="Longfu88 handbook for Singapore players on mobile: shortcut, devices, games, sports, SGD payments, welcome offer, cashback, login, security and support.",
        label="Everything about Longfu88 on a phone in one handbook",
        cta=["Register", "Join Now"], promo_button="Join Now",
        links=[("bonuses page", "/bonuses"), ("login page", "/login")]),
    "v09": dict(
        title="Longfu88 Mobile Account Path: Shortcut to Cash-Out",
        description="Longfu88 account path on a phone: add the shortcut, register, log in, pass identity checks, cash out, protect the account, play responsibly and fix issues.",
        label="Follow the account path from shortcut to cash-out",
        cta=["Claim Bonus", "Log In"], promo_button="Get Offer",
        links=[("bonuses", "/bonuses"), ("login page", "/login")]),
    "v10": dict(
        title="Longfu88 Mobile Rules and Payments for Singapore",
        description="Longfu88 on mobile for Singapore players: who can play, currencies and languages, sports betting rules, game categories, payment methods and cash-outs.",
        label="Rules, currencies and payments for mobile players",
        cta=["Join Now", "Register"], promo_button="Claim Bonus",
        links=[("Login", "/login")]),
    "v11": dict(
        title="Longfu88 Mobile Casino: Play, Bet and Claim on a Phone",
        description="Longfu88 mobile casino on a phone: add the shortcut, play slots and live dealer games, bet on sports, claim the welcome offer, verify and request a cash-out.",
        label="Play, bet and claim from your phone",
        cta=["Play Now", "Claim Bonus"], promo_button="Claim Offer",
        links=[("welcome offer", "/bonuses"), ("login page", "/login")]),
    "v12": dict(
        title="Longfu88 Mobile Casino Reference: Facts for Singapore",
        description="Longfu88 mobile casino reference for Singapore: shortcut steps for Android and iOS, features, account, cash-outs, security, sportsbook, games, payments.",
        label="Mobile casino facts in one reference",
        cta=["Log In", "Play Now"], promo_button="Join Now",
        links=[("bonuses", "/bonuses"), ("login screen", "/login")]),
}


def site_for(vid: str) -> dict:
    n = int(vid[1:])
    return SG_SITES[(n - 1 + 8) % 12]


def context(page: dict, href: str) -> str:
    for b in page["content"]:
        a = b.get("article") or ""
        m = re.search(r'<a href="%s">(.*?)</a>' % re.escape(href), a)
        if m:
            txt = re.sub(r"<[^>]+>", "", a[max(0, m.start() - 70):m.end() + 40])
            return txt.replace("\n", " ")
    return ""


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    titles, descs = set(), set()
    for vid, p in PAGES.items():
        d = site_for(vid)
        run = f"longfu88-app-sg-{vid}"
        assert len(p["title"]) <= 60 and 120 <= len(p["description"]) <= 160, (vid, len(p["title"]), len(p["description"]))
        assert p["title"] not in titles and p["description"] not in descs
        titles.add(p["title"]); descs.add(p["description"])
        assert len(p["cta"]) == 2 and p["cta"][0] != p["cta"][1]
        for a, _ in p["links"]:
            assert len(a.split()) <= 3, a
        cfg = {
            "website_id": d["website_id"], "domain": d["domain"], "locale": "en", "slug": "app",
            "seo": {"title": p["title"], "description": p["description"]},
            "keywords": {"main": BRAND, "additional": ADDITIONAL},
            "hero": {"label": p["label"], "mainLabel": "", "background": HERO, "button": p["cta"][0]},
            "cta_texts": p["cta"],
            "home_link": {"anchor": BRAND, "href": "/"},  # the brand name in the running text of the page, no extra paragraph
            "internal_links": [{"anchor": a, "href": h} for a, h in p["links"]],
            "promo": {"title": "Casino Welcome Bonus", "description": "188% up to €2,088 + 18 Free Spins", "button": p["promo_button"]},
        }
        (ROOT / "runs" / run / "05_affbulk_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-m", "affbulk.build_page", run], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        out = (r.stdout.strip().splitlines() or [""])[0]
        print(f"{vid} {d['domain']:24} site {d['website_id']} (sg idx {SG_SITES.index(d) + 1}) title {len(p['title'])} desc {len(p['description'])}: "
              f"rc={r.returncode} {out}" + (" | " + r.stderr.strip().replace("\n", " ")[:400] if r.returncode else ""))
        if r.returncode == 0:
            page = json.loads((ROOT / "runs" / run / "05_affbulk_page.json").read_text(encoding="utf-8"))
            for a, h in p["links"]:
                print(f"     {h}: ...{context(page, h)}...")


if __name__ == "__main__":
    main()
