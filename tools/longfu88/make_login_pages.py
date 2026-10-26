"""Longfu88 login pages (brand-subpage, MY): the AffBulk configs, the payloads and everything that goes with them. Run from the project root:
    python tools/longfu88/make_login_pages.py

For each variant vNN (runs/longfu88-login-my-vNN, finished text in 04_final.json) and the site of the MY review variant with the same number
(tools/longfu88/domains.json, geo my):
  1. runs/longfu88-login-my-vNN/05_affbulk_config.json  -> python -m affbulk.build_page -> 05_affbulk_page.json (pages_create `data`)
  2. runs/longfu88-my-vNN/05_affbulk_update_login.json   the content of the home page with ONE internal link to /login/ (an existing phrase of
     the login section is wrapped, no words are added or removed); the current payload is kept as 05_affbulk_page.before_login_link.json
  3. runs/longfu88-login-my-vNN/05_affbulk_header.json   the header of the site with the new menu item (`websites_update` data)
Nothing is written to AffBulk here.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERO = 140  # hero image of the brand
LOGIN_PATH = "/login"  # the built page answers on /login (a link to /login/ is a 308 redirect)
MENU_TEXT = "Longfu88 Login"
BRAND = "Longfu88"

DOMAINS = {e["variant"]: e for e in json.loads((ROOT / "tools/longfu88/domains.json").read_text(encoding="utf-8")) if e["geo"] == "my"}
ADDITIONAL = "login, sign in, register, password reset, forgot password, account verification, KYC, account security, customer support, casino account, Malaysia, MY, Malaysian players"

PAGES = {
    "v01": dict(
        title="Longfu88 Login: Sign In and Reset Your Password",
        description="Longfu88 login explained for Malaysia: the three sign-in steps, password reset by e-mail, registration, verification documents and support.",
        label="Log in with your registered e-mail and password",
        cta=["Log In", "Register", "Join Now", "Play Now", "Claim Bonus"],
        anchor="Longfu88 login"),
    "v02": dict(
        title="Longfu88 Login and Account Guide for Malaysia",
        description="Longfu88 login and account guide for Malaysian players: open an account, sign in, replace a lost password and see which documents may be requested.",
        label="New here? Register first, then log in",
        cta=["Register", "Log In", "Join Now", "Claim Bonus", "Play Now"],
        anchor="select Login on the website"),
    "v03": dict(
        title="Longfu88 Login Checklist: Register, Verify, Sign In",
        description="Longfu88 login checklist for Malaysian players: what to prepare, the documents to keep ready, the login steps and what to do if the password is lost.",
        label="Registration, documents and login in one checklist",
        cta=["Register", "Log In", "Play Now", "Join Now", "Claim Bonus"],
        anchor="Longfu caino login"),
    "v04": dict(
        title="Longfu88 Login: Step-by-Step Guide for New Players",
        description="Longfu88 login guide for new players in Malaysia: create the account, log in, reset a forgotten password, pass verification and keep the account safe.",
        label="Create the account, then log in: three steps",
        cta=["Register", "Join Now", "Log In", "Claim Bonus", "Play Now"],
        anchor="login works with the registered email and password"),
    "v05": dict(
        title="Longfu88 Login Help: Fix Access and Reset Password",
        description="Longfu88 login help for Malaysia: the normal sign-in route, why a login fails, how to reset the password, which checks can hold an account and who to contact.",
        label="Cannot log in? Start with the checks on this page",
        cta=["Log In", "Register", "Play Now", "Join Now", "Claim Bonus"],
        anchor="Forgot Password on the login screen"),
    "v06": dict(
        title="Longfu88 Login: Secure Access and Account Checks",
        description="Longfu88 login and account security for Malaysian players: signing in safely, what protects the account, why documents are requested and who to contact.",
        label="Sign in safely with your registered e-mail and password",
        cta=["Log In", "Register", "Join Now", "Claim Bonus", "Play Now"],
        anchor="Longfu88 login"),
    "v07": dict(
        title="Longfu88 Login on Mobile and Desktop: How to Sign In",
        description="Longfu88 login on a phone or a computer: sign in with e-mail and password, add a home-screen shortcut on Android or iOS, reset the password, find support.",
        label="Log in from any phone, tablet or computer",
        cta=["Log In", "Play Now", "Register", "Join Now", "Claim Bonus"],
        anchor="Longfu88 login"),
    "v08": dict(
        title="Longfu88 Account Handbook: Login, Register, Verify",
        description="Longfu88 account handbook for Malaysian players: login, registration, password reset, verification, security, settings, mobile access and support.",
        label="Everything about the Longfu88 account in one handbook",
        cta=["Register", "Log In", "Join Now", "Play Now", "Claim Bonus"],
        anchor="select Login on the website"),
}


def wrap_anchor(content: list[dict], phrase: str, href: str) -> tuple[list[dict], str]:
    """Wrap the first occurrence of `phrase` in the text of an article about login / sign-in / registration with a link. No word is
    added or removed. Returns the new content and the heading of the article."""
    out = json.loads(json.dumps(content))
    for b in out:
        if b["__component"] != "blocks.article":
            continue
        head = re.search(r"<h[23]>(.*?)</h[23]>", b["article"])
        if not head or not re.search(r"log ?in|sign|regist|account", head.group(1), re.I):
            continue
        text = re.sub(r"<[^>]+>", "\x00", b["article"])  # the phrase must stand in the text, never inside a tag
        if phrase in text and phrase in b["article"]:
            b["article"] = b["article"].replace(phrase, f'<a href="{href}">{phrase}</a>', 1)
            return out, head.group(1)
    raise ValueError(f"phrase not found in a login section: {phrase!r}")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    header_ref = None
    for vid, p in PAGES.items():
        d = DOMAINS[vid]
        run, home = f"longfu88-login-my-{vid}", f"longfu88-my-{vid}"
        assert 120 <= len(p["description"]) <= 160 and len(p["title"]) <= 60, (vid, len(p["title"]), len(p["description"]))
        cfg = {
            "website_id": d["website_id"], "domain": d["domain"], "locale": "en", "slug": "login",
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

        # the home page of the same site: one internal link to the login page
        page_path = ROOT / "runs" / home / "05_affbulk_page.json"
        before = ROOT / "runs" / home / "05_affbulk_page.before_login_link.json"
        if not before.exists():
            before.write_text(page_path.read_text(encoding="utf-8"), encoding="utf-8")
        page = json.loads(before.read_text(encoding="utf-8"))
        assert page["website"] == d["website_id"], (home, page["website"])
        content, where = wrap_anchor(page["content"], p["anchor"], LOGIN_PATH)
        (ROOT / "runs" / home / "05_affbulk_update_login.json").write_text(json.dumps({"content": content}, ensure_ascii=False), encoding="utf-8")
        print(f"     home link: anchor {p['anchor']!r} in the section {where!r}")

        # the header: the same five items + the login page
        nav = [{"text": t, "link": "{{rezerv_casino}}", "linkStatus": "affiliate"} for t in ("Promotions", "Casino", "Live Casino", "Sports", "Live Betting")]
        nav.append({"text": MENU_TEXT, "link": LOGIN_PATH, "linkStatus": "internal"})
        buttons = [{"variant": "main", "link": "{{rezerv_casino}}", "text": "Register", "linkStatus": "affiliate"},
                   {"variant": "secondary", "link": "{{rezerv_casino}}", "text": "Login", "linkStatus": "affiliate"}]
        header = {"header": {"navLinks": nav, "buttons": buttons}}
        (ROOT / "runs" / run / "05_affbulk_header.json").write_text(json.dumps(header, ensure_ascii=False, indent=1), encoding="utf-8")
        header_ref = header


if __name__ == "__main__":
    main()

