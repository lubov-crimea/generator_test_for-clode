"""Longfu88 bonuses pages (brand-subpage, MY): the AffBulk configs and payloads. Run from the project root:
    python tools/longfu88/make_bonus_pages.py
For each variant vNN (runs/longfu88-bonus-my-vNN, finished text in 04_final.json) and the site of the MY review variant with the same number
(tools/longfu88/domains.json, geo my) it writes runs/longfu88-bonus-my-vNN/05_affbulk_config.json and builds 05_affbulk_page.json with
`python -m affbulk.build_page` (Hero -> Preview -> intro -> 2 CTA -> articles -> FAQ -> Promo). Nothing is written to AffBulk here.
The Preview tiles use the six bonus images of the brand folder longfu88/bonus (media ids 4652-4657), each with the offer of the knowledge base
that the image belongs to (verified on the home pages): all six tiles on every page, another order per variant (the user wants full tiles always)."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERO = 140
BRAND = "Longfu88"
DOMAINS = {e["variant"]: e for e in json.loads((ROOT / "tools/longfu88/domains.json").read_text(encoding="utf-8")) if e["geo"] == "my"}
ADDITIONAL = "bonuses, promotions, offers, promo code, welcome bonus, free spins, reload bonus, cashback, wagering requirements, My Bonuses, casino, Malaysia, MY, Malaysian players"

LIVE = (4657, "Live Casino Welcome Bonus", "125% up to €888")
CRYPTO = (4654, "Casino Crypto Welcome Bonus", "188% up to 2,888 USDT")
SPORT = (4656, "Sport First Deposit Bonus", "100% up to €1,888")
WEEKEND = (4655, "Casino Weekend Crypto Reload", "75% up to 750 USDT + 100 Free Spins")
CASHBACK = (4652, "Casino Weekly Cashback", "Up to 10% of weekly net casino losses")
CRAB = (4653, "Bonus Crab", "Qualifying picks reveal bonus credits, free spins or coins")
BTN = ["Claim Bonus", "Get Offer", "See Offer", "Claim Now", "Get Bonus", "Join Now"]


def preview(title, tiles):
    return {"title": title, "items": [{"image": i, "title": t, "text": x, "button": BTN[(n + len(title)) % len(BTN)]} for n, (i, t, x) in enumerate(tiles)]}


PAGES = {
    "v01": dict(
        title="Longfu88 Promotions: Bonuses and Promo Code",
        description="Longfu88 bonuses for Malaysia: the 188% welcome bonus with 18 free spins, how to claim it, the terms, the promo code question, reloads and cashback.",
        label="Welcome offer: 188% up to €2,088 + 18 Free Spins",
        cta=["Claim Bonus", "Register"], preview=preview("Longfu88 Bonuses at a Glance", [LIVE, WEEKEND, CASHBACK, CRYPTO, CRAB, SPORT])),
    "v02": dict(
        title="Longfu88 Welcome Bonus: Offer, Terms, Promo Code",
        description="Longfu88 welcome bonus for Malaysian players: 188% up to €2,088 plus 18 free spins, claiming steps, wagering, minimum deposits and the promo code answer.",
        label="Casino Welcome Bonus: 188% up to €2,088 + 18 Free Spins",
        cta=["Register", "Claim Bonus"], preview=preview("Welcome Offers of the Casino", [CRYPTO, LIVE, SPORT, CASHBACK, WEEKEND, CRAB])),
    "v03": dict(
        title="Longfu88 Promotions Checklist for Malaysia",
        description="Longfu88 bonus checklist for Malaysian players: what to check before claiming the welcome bonus, the claim steps, reload offers, cashback and rewards.",
        label="Check the terms first, then claim the welcome bonus",
        cta=["Play Now", "Claim Bonus"], preview=preview("Offers on the Checklist", [CASHBACK, CRAB, WEEKEND, LIVE, CRYPTO, SPORT])),
    "v04": dict(
        title="Longfu88 Welcome Bonus and Promotions for Beginners",
        description="Longfu88 bonuses for new players in Malaysia: how the welcome offer works, claiming it, minimum deposits per offer, reloads, cashback and the rewards area.",
        label="New here? Start with the Casino Welcome Bonus",
        cta=["Join Now", "Claim Bonus"], preview=preview("First Offers for New Players", [CRYPTO, LIVE, WEEKEND, CASHBACK, CRAB, SPORT])),
    "v05": dict(
        title="Longfu88 Offers for Crypto and Live Casino Players",
        description="Longfu88 offers for crypto and live casino players in Malaysia: three welcome offers compared, USDT reloads, live cashback, terms and eligible coins.",
        label="Crypto and live casino offers in one place",
        cta=["Claim Bonus", "Register"], preview=preview("Crypto and Live Casino Offers", [CRYPTO, WEEKEND, LIVE, CASHBACK, CRAB, SPORT])),
    "v06": dict(
        title="Longfu88 Promotions for Casino and Sports Players",
        description="Longfu88 promotions for casino and sports players in Malaysia: welcome bonus, reloads, cashback, unlimited rebates and sports bonuses with required odds.",
        label="Casino and sports bonuses side by side",
        cta=["Register", "Get Offer"], preview=preview("Casino and Sports Bonuses", [SPORT, LIVE, CASHBACK, WEEKEND, CRAB, CRYPTO])),
    "v07": dict(
        title="Longfu88 Bonus Terms to Check Before You Claim",
        description="Longfu88 bonus terms for Malaysian players: wagering, maximum bet, verification before payout, seasonal offers, cashback conditions and responsible use.",
        label="Read the terms before you claim a bonus",
        cta=["Play Now", "Claim Bonus"], preview=preview("Offers and Their Terms", [LIVE, CASHBACK, CRYPTO, WEEKEND, CRAB, SPORT])),
    "v08": dict(
        title="Longfu88 Promotions Handbook: Bonuses and Terms",
        description="Longfu88 promotions handbook for Malaysia: every bonus, wagering terms, minimum deposits, crypto, live, sports and seasonal offers, cashback by VIP level.",
        label="Every Longfu88 bonus, term and rule in one handbook",
        cta=["Register", "Claim Bonus"], preview=preview("All Longfu88 Bonus Types", [CRYPTO, LIVE, SPORT, WEEKEND, CASHBACK, CRAB])),
}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    for vid, p in PAGES.items():
        d = DOMAINS[vid]
        run = f"longfu88-bonus-my-{vid}"
        assert 120 <= len(p["description"]) <= 160 and len(p["title"]) <= 60, (vid, len(p["title"]), len(p["description"]))
        cfg = {
            "website_id": d["website_id"], "domain": d["domain"], "locale": "en", "slug": "bonuses",
            "seo": {"title": p["title"], "description": p["description"]},
            "keywords": {"main": BRAND, "additional": ADDITIONAL},
            "hero": {"label": p["label"], "mainLabel": "", "background": HERO, "button": p["cta"][0]},
            "cta_texts": p["cta"],
            "preview": p["preview"],
            "home_link": {"anchor": BRAND, "href": "/"},
            "promo": {"title": "Casino Welcome Bonus", "description": "188% up to €2,088 + 18 Free Spins", "button": "Claim Bonus"},
        }
        (ROOT / "runs" / run / "05_affbulk_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-m", "affbulk.build_page", run], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        print(f"{vid} {d['domain']:24} site {d['website_id']}: " + (r.stdout.strip().splitlines() or [r.stderr.strip()])[0], "| " + r.stderr.strip().replace("\n", " ")[:300] if r.returncode else "")


if __name__ == "__main__":
    main()
