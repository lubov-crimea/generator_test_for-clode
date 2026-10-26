"""Longfu88 login pages (brand-subpage, SG): the AffBulk configs and the payloads. Run from the project root:
    python tools/longfu88/make_login_sg_pages.py

For each variant vNN (runs/longfu88-login-sg-vNN, finished text in 04_final.json) the SG site with index ((NN-1+4) % 12)+1
(tools/longfu88/domains.json, geo sg, list order; v01 -> 5, ..., v08 -> 12, v09 -> 1, ..., v12 -> 4):
  runs/longfu88-login-sg-vNN/05_affbulk_config.json  -> python -m affbulk.build_page -> 05_affbulk_page.json (pages_create `data`)
No home-page update and no header file here (the menus and the home links are made for all page types together). Nothing is written to AffBulk.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERO = 140  # hero image of the brand
BRAND = "Longfu88"

SG_SITES = [e for e in json.loads((ROOT / "tools/longfu88/domains.json").read_text(encoding="utf-8")) if e["geo"] == "sg"]
ADDITIONAL = "login, sign in, register, password reset, forgot password, account verification, KYC, account security, customer support, casino account, Singapore, SG, Singapore players"

B = "/bonuses"
A = "/app"

# anchors are exact phrases (<= 3 words) of the finished text; the first occurrence in the running text is wrapped
PAGES = {
    "v01": dict(
        title="Longfu88 Login Singapore: Sign In, Reset, Register",
        description="Longfu88 login for Singapore players: the three sign-in steps, password reset by e-mail, registration, verification documents and how to reach support.",
        label="Sign in with your registered e-mail and password",
        cta=["Log In", "Register"], promo="Claim Bonus", links=[]),
    "v02": dict(
        title="Longfu88 Account Guide: Register, Welcome Offer, Login",
        description="Longfu88 account guide for Singapore players: open an account, claim the welcome offer, log in, use the site on a phone and choose a currency.",
        label="New here? Open the account, then log in",
        cta=["Register", "Play Now"], promo="Get Bonus",
        links=[("Casino Welcome Bonus", B), ("Mobile access", A)]),
    "v03": dict(
        title="Longfu88 Login Problems: Why Sign-In Fails and Fixes",
        description="Longfu88 login problems explained for Singapore players: the normal sign-in route, password reset, common causes of failure, account checks and support.",
        label="Cannot sign in? Check the usual causes first",
        cta=["Log In", "Join Now"], promo="Claim Offer", links=[],
        faq=dict(title="Login Questions", items=[
            dict(question="Which details does the Longfu88 login need?", answer="Only the registered e-mail address and its password. A security check is added when the site asks for one."),
            dict(question="What can a player do after forgetting the password?", answer="Choose Forgot Password on the login screen, request a reset link with the registered e-mail and follow the e-mailed instructions to set a new password."),
            dict(question="Why can a login fail with the correct password?", answer="The operator may suspend activity for verification or suspected abuse, and an account review may delay access until verification is complete."),
            dict(question="How can a player reach support about the login?", answer="Through live chat, which is open 24/7, or by e-mail at support@longfu88.com."),
        ])),
    "v04": dict(
        title="Longfu88 Account Control: Data, Breaks and Closing",
        description="Longfu88 account control for Singapore players: registration rules, protecting login details, currencies, taking a break or closing the account, and support.",
        label="Keep your account and your details under control",
        cta=["Register", "Log In"], promo="Claim Bonus", links=[("bonus offers", B)],
        faq=dict(title="Account Questions", items=[
            dict(question="How does a new player register at Longfu88?", answer="Registration runs by e-mail only: select Register, enter an e-mail address and a password, confirm age and the Terms and Conditions and the Privacy Policy, add the personal details and the residential address, then select Create Account."),
            dict(question="How many accounts can a player hold?", answer="Each player holds only one personal account, in one of the supported currencies: EUR, USD, MYR, THB, SGD or USDT."),
            dict(question="How can a player pause or close the account?", answer="Contact customer support and ask for self-exclusion or account closure. Self-exclusion may restrict account access and gambling for the agreed period."),
            dict(question="Can marketing messages be stopped?", answer="Yes. Players may manage direct-marketing preferences and unsubscribe from promotional communications."),
        ])),
    "v05": dict(
        title="Longfu88 Login Guide: Register, Log In, Verify",
        description="Longfu88 login guide for new players in Singapore: register, claim the welcome offer, sign in, reset a lost password, verify the account and get help.",
        label="Create the account, log in, then verify it",
        cta=["Join Now", "Log In"], promo="Get Bonus", links=[("Casino Welcome Bonus", B)]),
    "v06": dict(
        title="Longfu88 Login Help: Failed Sign-In and Payout Checks",
        description="Longfu88 login help for Singapore players: the normal sign-in route, reasons a login fails, password reset, account checks, first payout checks and support.",
        label="Locked out? Start with the normal login route",
        cta=["Log In", "Play Now"], promo="Claim Offer", links=[]),
    "v07": dict(
        title="Longfu88 Secure Login: Passwords, Data and Documents",
        description="Longfu88 secure login for Singapore players: sign in safely, replace a lost password, see what protects the account and which documents are requested and why.",
        label="Sign in safely and keep the account protected",
        cta=["Log In", "Register"], promo="Claim Bonus", links=[("Casino Welcome Bonus", B)]),
    "v08": dict(
        title="Longfu88 Mobile Login: Phone Sign-In and Shortcut",
        description="Longfu88 login on a phone or computer for Singapore players: sign in, reset a password, add a home screen shortcut, keep documents ready and contact support.",
        label="Log in from a phone, a tablet or a computer",
        cta=["Play Now", "Log In"], promo="Get Bonus", links=[("mobile web browser", A)]),
    "v09": dict(
        title="Longfu88 Responsible Account Guide: Pause and Login",
        description="Longfu88 account guide for Singapore players who want control: pause or self-exclusion, login, password reset, verification, payout checks and support.",
        label="Stay in control of your account",
        cta=["Register", "Join Now"], promo="Claim Offer", links=[("bonus offers", B)]),
    "v10": dict(
        title="Longfu88 Sign-Up, Welcome Bonus and Login Guide",
        description="Longfu88 account guide for Singapore players: register, claim the welcome bonus, log in, pass verification, use a phone and learn about the VIP levels.",
        label="Sign up, claim the offer and log in",
        cta=["Join Now", "Claim Bonus"], promo="Claim Bonus", links=[("Casino Welcome Bonus", B), ("mobile access", A)]),
    "v11": dict(
        title="Longfu88 Account Handbook: Access, Checks, Settings",
        description="Longfu88 account handbook for Singapore players: opening an account, login, password recovery, verification, settings, mobile access, VIP levels and support.",
        label="The whole Longfu88 account in one handbook",
        cta=["Register", "Log In"], promo="Get Bonus", links=[("Casino Welcome Bonus", B), ("mobile access", A)]),
    "v12": dict(
        title="Longfu88 Account Lifecycle: Register, Login, Payout",
        description="Longfu88 account lifecycle for Singapore players: register, verify, log in, first payout, phone access, VIP levels, taking a break or closing the account.",
        label="From the first sign-up to the last day of the account",
        cta=["Log In", "Join Now"], promo="Claim Offer", links=[("welcome offer", B), ("mobile access", A)]),
}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    assert len(SG_SITES) == 12
    for vid, p in PAGES.items():
        n = int(vid[1:])
        d = SG_SITES[((n - 1 + 4) % 12)]  # list index ((NN-1+4) % 12)+1, 1-based
        run = f"longfu88-login-sg-{vid}"
        assert 120 <= len(p["description"]) <= 160 and len(p["title"]) <= 60, (vid, len(p["title"]), len(p["description"]))
        assert len(p["cta"]) == 2 and len({c.lower() for c in p["cta"]}) == 2
        cfg = {
            "website_id": d["website_id"], "domain": d["domain"], "locale": "en", "slug": "login",
            "seo": {"title": p["title"], "description": p["description"]},
            "keywords": {"main": BRAND, "additional": ADDITIONAL},
            "hero": {"label": p["label"], "mainLabel": "", "background": HERO, "button": p["cta"][0]},
            "cta_texts": p["cta"],
            "home_link": {"anchor": BRAND, "href": "/"},  # the brand name in the running text of the page, no extra paragraph
            "promo": {"title": "Casino Welcome Bonus", "description": "188% up to €2,088 + 18 Free Spins", "button": p["promo"]},
        }
        if p.get("faq"):  # the text has no FAQ section: the pairs repeat facts already stated in the text
            cfg["faq"] = p["faq"]
        if p["links"]:
            assert len({h for _, h in p["links"]}) == len(p["links"])
            cfg["internal_links"] = [{"anchor": a, "href": h} for a, h in p["links"]]
        (ROOT / "runs" / run / "05_affbulk_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-m", "affbulk.build_page", run], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        res = (r.stdout.strip().splitlines() or [""])[0] if r.returncode == 0 else "FAILED: " + (r.stderr.strip() or r.stdout.strip()).replace("\n", " ")[-300:]
        print(f"{vid} {d['domain']:24} site {d['website_id']} | title {len(p['title'])} desc {len(p['description'])} | links {[a for a, _ in p['links']]} | {res}")


if __name__ == "__main__":
    main()

