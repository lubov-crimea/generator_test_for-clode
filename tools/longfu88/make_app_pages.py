"""Longfu88 app pages (brand-subpage, MY): the AffBulk configs, the payloads and everything that goes with them. Run from the project root:
    python tools/longfu88/make_app_pages.py

For each variant vNN (runs/longfu88-app-my-vNN, finished text in 04_final.json) and the site of the MY review variant with the same number
(tools/longfu88/domains.json, geo my):
  1. runs/longfu88-app-my-vNN/05_affbulk_config.json  -> python -m affbulk.build_page -> 05_affbulk_page.json (pages_create `data`)
  2. runs/longfu88-my-vNN/05_affbulk_update_app.json    the content of the home page with ONE internal link to /app (an existing phrase of
     the mobile section is wrapped, no words are added or removed); the current payload is kept as 05_affbulk_page.before_app_link.json
  3. runs/longfu88-app-my-vNN/05_affbulk_header.json    the header of the site: the current items (read from AffBulk) + the app page
Nothing is written to AffBulk here.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERO = 140  # hero image of the brand
APP_PATH = "/app"  # the built page answers on /app (a link to /app/ is a 308 redirect)
MENU_TEXT = "Longfu88 App"
BRAND = "Longfu88"

DOMAINS = {e["variant"]: e for e in json.loads((ROOT / "tools/longfu88/domains.json").read_text(encoding="utf-8")) if e["geo"] == "my"}
ADDITIONAL = "app, mobile casino, Android, iOS, home screen shortcut, mobile browser, smartphone, tablet, account access, customer support, casino, Malaysia, MY, Malaysian players"

PAGES = {
    "v01": dict(
        title="Longfu88 Mobile Casino: Android and iOS Shortcut",
        description="Longfu88 mobile casino for Malaysia: add the site to an Android or iOS home screen in a few steps, see what works on a phone and where to get help.",
        label="Add the casino to your phone's home screen",
        cta=["Play Now", "Register", "Join Now", "Log In", "Claim Bonus"],
        anchor="Longfu88 app"),
    "v02": dict(
        title="Longfu88 Android: Add the Casino to Your Phone",
        description="Longfu88 on Android and iOS for Malaysian players: the Chrome and Safari shortcut steps, what works on mobile, account access, fixes and support.",
        label="Android first: Chrome steps, iOS steps right below",
        cta=["Register", "Play Now", "Join Now", "Log In", "Claim Bonus"],
        anchor="home-screen version of the site"),
    "v03": dict(
        title="Longfu App Checklist: Phone Setup for Malaysia",
        description="Longfu app checklist for Malaysian players: check the device, add the shortcut on iOS or Android, log in, fix common problems and find support.",
        label="Phone setup in one checklist",
        cta=["Play Now", "Log In", "Register", "Join Now", "Claim Bonus"],
        anchor="Longfu88 app"),
    "v04": dict(
        title="Longfu88 Mobile Casino: Guide for First-Time Users",
        description="Longfu88 mobile casino guide for new players in Malaysia: what the mobile site offers, the Android and iOS shortcut steps, sign-in, safety and support.",
        label="Four steps from first visit to first login on a phone",
        cta=["Register", "Join Now", "Play Now", "Log In", "Claim Bonus"],
        anchor="home-screen version of the site"),
    "v05": dict(
        title="Longfu App or Mobile Site? Longfu88 on a Phone",
        description="Longfu88 on a phone: the home-screen shortcut or a browser tab, which phones and browsers work, the Android and iOS steps, sign-in and support.",
        label="Shortcut or browser tab: pick your route",
        cta=["Play Now", "Register", "Log In", "Join Now", "Claim Bonus"],
        anchor="responsive website on smartphone and tablet browsers"),
    "v06": dict(
        title="Longfu88 on Android and iOS: Safe Mobile Access",
        description="Longfu88 mobile casino safety for Malaysian players: how the account is protected on a phone, safe sign-in, the home-screen shortcut and support.",
        label="Use the casino on a phone with the account protected",
        cta=["Log In", "Play Now", "Register", "Join Now", "Claim Bonus"],
        anchor="home-screen shortcut"),
    "v07": dict(
        title="Longfu88 Mobile Casino Help: Setup and Fixes",
        description="Longfu88 mobile casino help for Malaysia: quick fixes for common phone problems, adding the shortcut again on Android and iOS, sign-in and support.",
        label="Phone not working? Start with the quick fixes",
        cta=["Play Now", "Log In", "Register", "Join Now", "Claim Bonus"],
        anchor="home-screen version of that site"),
    "v08": dict(
        title="Longfu88 Mobile Casino Handbook for Malaysia",
        description="Longfu88 mobile casino handbook for Malaysia: Android and iOS shortcut, devices, games, sports, payments, welcome offer, account access and support.",
        label="Everything about Longfu88 on a phone in one handbook",
        cta=["Register", "Play Now", "Join Now", "Log In", "Claim Bonus"],
        anchor="home-screen version of the site"),
}


def wrap_anchor(content: list[dict], phrase: str, href: str) -> tuple[list[dict], str]:
    """Wrap the first occurrence of `phrase` in the running text of a section about mobile play with a link. No word is added or
    removed. Returns the new content and the heading of the article."""
    out = json.loads(json.dumps(content))
    for b in out:
        if b["__component"] != "blocks.article":
            continue
        head = re.search(r"<h[23]>(.*?)</h[23]>", b["article"])
        if not head or not re.search(r"mobile|phone|move", head.group(1), re.I):
            continue
        paras = re.findall(r"<p>.*?</p>", b["article"], re.S)
        for p in paras:
            if phrase in re.sub(r"<[^>]+>", "\x00", p) and phrase in p:
                b["article"] = b["article"].replace(p, p.replace(phrase, f'<a href="{href}">{phrase}</a>', 1), 1)
                return out, head.group(1)
    raise ValueError(f"phrase not found in a mobile section: {phrase!r}")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    for vid, p in PAGES.items():
        d = DOMAINS[vid]
        run, home = f"longfu88-app-my-{vid}", f"longfu88-my-{vid}"
        assert 120 <= len(p["description"]) <= 160 and len(p["title"]) <= 60, (vid, len(p["title"]), len(p["description"]))
        cfg = {
            "website_id": d["website_id"], "domain": d["domain"], "locale": "en", "slug": "app",
            "seo": {"title": p["title"], "description": p["description"]},
            "keywords": {"main": "Longfu88", "additional": ADDITIONAL},
            "hero": {"label": p["label"], "mainLabel": "", "background": HERO, "button": p["cta"][0]},
            "cta_texts": p["cta"],
            "home_link": {"anchor": BRAND, "href": "/"},  # the brand name in the running text of the page, no extra paragraph
            "promo": {"title": "Casino Welcome Bonus", "description": "188% up to €2,088 + 18 Free Spins", "button": "Claim Bonus"},
        }
        (ROOT / "runs" / run / "05_affbulk_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-m", "affbulk.build_page", run], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        print(f"{vid} {d['domain']:24} site {d['website_id']}: " + (r.stdout.strip().splitlines() or [r.stderr.strip()])[0], "| " + r.stderr.strip().replace("\n", " ")[:300] if r.returncode else "")

        # the home page of the same site: one internal link to the app page (the login link is already in it)
        page_path = ROOT / "runs" / home / "05_affbulk_update_login.json"
        base = json.loads((ROOT / "runs" / home / "05_affbulk_page.json").read_text(encoding="utf-8"))
        before = ROOT / "runs" / home / "05_affbulk_page.before_app_link.json"
        if not before.exists():
            before.write_text(json.dumps(base, ensure_ascii=False), encoding="utf-8")
        content = json.loads(page_path.read_text(encoding="utf-8"))["content"]  # home page content including the /login link
        content, where = wrap_anchor(content, p["anchor"], APP_PATH)
        (ROOT / "runs" / home / "05_affbulk_update_app.json").write_text(json.dumps({"content": content}, ensure_ascii=False), encoding="utf-8")
        print(f"     home link: anchor {p['anchor']!r} in the section {where!r}")


if __name__ == "__main__":
    main()
