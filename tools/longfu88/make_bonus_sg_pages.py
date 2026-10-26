"""Longfu88 bonuses pages (brand-subpage, SG): the AffBulk configs and payloads. Run from the project root:
    python tools/longfu88/make_bonus_sg_pages.py
For each variant vNN (runs/longfu88-bonus-sg-vNN, finished text in 04_final.json) and the SG site with the same number
(tools/longfu88/domains.json, geo sg, list order) it writes runs/longfu88-bonus-sg-vNN/05_affbulk_config.json and builds 05_affbulk_page.json
with `python -m affbulk.build_page` (Hero -> Preview -> intro -> 2 CTA -> articles -> FAQ -> Promo). Nothing is written to AffBulk here.
The Preview tiles are the six bonus images of the brand folder longfu88/bonus (media ids 4652-4657) with the offers of the knowledge base
(same as in make_bonus_pages.py for MY): all six tiles on every page, a different order per variant.
Cross-links /login and /app: only where the finished text has a phrase of at most 3 words that names the topic (exact text, nothing added)."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERO = 140
BRAND = "Longfu88"
DOMAINS = {f"v{n:02d}": e for n, e in enumerate([e for e in json.loads((ROOT / "tools/longfu88/domains.json").read_text(encoding="utf-8")) if e["geo"] == "sg"], 1)}
ADDITIONAL = "bonuses, promotions, offers, promo code, welcome bonus, free spins, reload bonus, cashback, wagering requirements, My Bonuses, casino, Singapore, SG, Singapore players"

LIVE = (4657, "Live Casino Welcome Bonus", "125% up to €888")
CRYPTO = (4654, "Casino Crypto Welcome Bonus", "188% up to 2,888 USDT")
SPORT = (4656, "Sport First Deposit Bonus", "100% up to €1,888")
WEEKEND = (4655, "Casino Weekend Crypto Reload", "75% up to 750 USDT + 100 Free Spins")
CASHBACK = (4652, "Casino Weekly Cashback", "Up to 10% of weekly net casino losses")
CRAB = (4653, "Bonus Crab", "Qualifying picks reveal bonus credits, free spins or coins")
BASE = [LIVE, WEEKEND, CASHBACK, CRYPTO, CRAB, SPORT]
BTN = ["Claim Bonus", "Get Offer", "See Offer", "Claim Now", "Get Bonus", "Join Now"]


def order(n: int) -> list[tuple]:
    """Twelve different orders of the six tiles: six rotations, then six rotations of the reversed list."""
    k = (n - 1) % 6
    seq = BASE if n <= 6 else BASE[::-1]
    return seq[k:] + seq[:k]


def preview(n: int, title: str) -> dict:
    return {"title": title, "items": [{"image": i, "title": t, "text": x, "button": BTN[(n + j) % len(BTN)]} for j, (i, t, x) in enumerate(order(n))]}


# anchors: exact phrases of the finished texts (checked by the builder); at most one link per target page
PAGES = {
    "v01": dict(
        title="Longfu88 Bonuses Quick Guide: Welcome Offer, Cashback",
        description="Longfu88 bonuses for Singapore players: the 188% welcome bonus with 18 free spins, claiming steps, terms, the promo code answer, reloads and cashback.",
        label="Quick guide to the Longfu88 welcome offer",
        cta=["Claim Bonus", "Register"], promo_btn="Claim Bonus", prev="Longfu88 Bonuses at a Glance", links=[]),
    "v02": dict(
        title="Longfu88 Welcome Bonus: Minimum Deposits, Crypto Offer",
        description="Longfu88 welcome bonus for Singapore players: 188% up to €2,088 plus 18 free spins, minimum deposits by offer, the crypto offer, wagering and checks.",
        label="Welcome bonus, deposits and the crypto offer",
        cta=["Register", "Get Offer"], promo_btn="Get Offer", prev="Welcome Offers of the Casino", links=[]),
    "v03": dict(
        title="Longfu88 Cashback and Sports Bonuses: Odds, VIP Rates",
        description="Longfu88 sports bonuses and cashback for Singapore players: the odds rule, VIP cashback rates, daily rebates and responsible use of the offers.",
        label="Cashback, rebates and sports bonuses explained",
        cta=["Play Now", "Claim Bonus"], promo_btn="See Offer", prev="Cashback and Sports Offers", links=[]),
    "v04": dict(
        title="Longfu88 Rewards and VIP Points for Loyal Players",
        description="Longfu88 rewards for loyal Singapore players: VIP points and levels, Bonus Crab, wheel and coin shop, live casino offers and phone access to bonuses.",
        label="Rewards and VIP points for loyal players",
        cta=["Join Now", "Claim Bonus"], promo_btn="Claim Now", prev="First Offers and Rewards", links=[("app page", "/app")]),
    "v05": dict(
        title="Longfu88 Bonuses for New Players: Claim, Terms, Reloads",
        description="Longfu88 bonuses for new players in Singapore: three welcome offers compared, claim steps, terms, reloads, cashback and cashing out bonus winnings.",
        label="New here? Start with the three welcome offers",
        cta=["Register", "Claim Now"], promo_btn="Get Bonus", prev="Offers a Newcomer Meets First", links=[("Log in", "/login")]),
    "v06": dict(
        title="Longfu88 Crypto and Live Casino Offers Compared",
        description="Longfu88 crypto and live casino offers for Singapore players: welcome bonuses compared, wagering of nine offers, USDT minimums, reloads and sports bonuses.",
        label="Crypto and live casino offers side by side",
        cta=["Get Bonus", "Register"], promo_btn="Join Now", prev="Crypto and Live Casino Offers", links=[("app page", "/app")]),
    "v07": dict(
        title="Longfu88 Casino and Sports Bonuses for Singapore",
        description="Longfu88 casino and sports promotions for Singapore players: welcome bonus, reloads, cashback, VIP points, qualifying odds, early payout and parlay boost.",
        label="Casino and sports promotions in one place",
        cta=["Play Now", "Get Offer"], promo_btn="Claim Bonus", prev="Casino and Sports Bonuses", links=[("login", "/login")]),
    "v08": dict(
        title="Longfu88 Bonus Rules: Wagering, Validity, Cashout",
        description="Longfu88 bonus rules for Singapore players: wagering, validity periods, minimum deposits, verification, cashing out and a checklist before you claim.",
        label="Read the bonus rules before you claim",
        cta=["Register", "See Offer"], promo_btn="See Offer", prev="Offers and Their Rules", links=[("Log in", "/login")]),
    "v09": dict(
        title="Longfu88 Active Player Rewards: VIP, Cashback, Reloads",
        description="Longfu88 promotions for active players in Singapore: reloads, cashback by VIP level, the VIP program, the rewards area, Bonus Crab and seasonal campaigns.",
        label="Rewards for players who come back",
        cta=["Join Now", "Claim Now"], promo_btn="Get Offer", prev="Offers for Regular Players", links=[("app page", "/app")]),
    "v10": dict(
        title="Longfu88 Bonus Ledger: Every Offer in One Table",
        description="Longfu88 offers compared in tables for Singapore players: welcome variants, reloads, crypto, live, cashback, rebates, the sports odds rule and validity.",
        label="Every offer as a row of the ledger",
        cta=["Claim Bonus", "Join Now"], promo_btn="Claim Now", prev="Offer Ledger at a Glance", links=[]),
    "v11": dict(
        title="Longfu88 Promotions Handbook: Bonuses, Terms, Promo Code",
        description="Longfu88 promotions handbook for Singapore players: every bonus, the promo code answer, minimum deposits, VIP levels, rewards area, glossary and checks.",
        label="The complete Longfu88 promotions handbook",
        cta=["Register", "Get Bonus"], promo_btn="Join Now", prev="Bonus Families in the Handbook", links=[("Log in", "/login"), ("app page", "/app")]),
    "v12": dict(
        title="Longfu88 Bonus Guide: Offers, Rules and Rewards",
        description="Longfu88 bonus guide for Singapore players: offers compared side by side, claiming steps, wagering, validity, cashback, VIP, sports bonuses and documents.",
        label="Every offer, rule and reward explained",
        cta=["Play Now", "Register"], promo_btn="Get Bonus", prev="Longfu88 Offers Compared", links=[]),
}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    assert len(PAGES) == len(DOMAINS) == 12
    assert len({p["title"] for p in PAGES.values()}) == 12 and len({p["description"] for p in PAGES.values()}) == 12
    assert len({p["label"] for p in PAGES.values()}) == 12
    for n, (vid, p) in enumerate(PAGES.items(), 1):
        d = DOMAINS[vid]
        run = f"longfu88-bonus-sg-{vid}"
        assert 120 <= len(p["description"]) <= 160 and len(p["title"]) <= 60, (vid, len(p["title"]), len(p["description"]))
        assert p["cta"][0] != p["cta"][1]
        cfg = {
            "website_id": d["website_id"], "domain": d["domain"], "locale": "en", "slug": "bonuses",
            "seo": {"title": p["title"], "description": p["description"]},
            "keywords": {"main": BRAND, "additional": ADDITIONAL},
            "hero": {"label": p["label"], "mainLabel": "", "background": HERO, "button": p["cta"][0]},
            "cta_texts": p["cta"],
            "preview": preview(n, p["prev"]),
            "home_link": {"anchor": BRAND, "href": "/"},
            "promo": {"title": "Casino Welcome Bonus", "description": "188% up to €2,088 + 18 Free Spins", "button": p["promo_btn"]},
        }
        if p["links"]:
            cfg["internal_links"] = [{"anchor": a, "href": h} for a, h in p["links"]]
        (ROOT / "runs" / run / "05_affbulk_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-m", "affbulk.build_page", run], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        links = ",".join(f"{a}->{h}" for a, h in p["links"]) or "-"
        print(f"{vid} {d['domain']:24} site {d['website_id']} | title {len(p['title'])} desc {len(p['description'])} | links {links} | "
              + ("OK " if r.returncode == 0 else "FAIL ") + (r.stdout.strip().splitlines() or [""])[0]
              + (" | " + r.stderr.strip().replace("\n", " ")[:300] if r.returncode else ""))


if __name__ == "__main__":
    main()
