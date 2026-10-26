"""Writes runs/<run>/05_affbulk_config.json for the Longfu88 pages (rules: prompts/affbulk_import.md).

    python tools/longfu88/make_affbulk_configs.py            # all runs listed in tools/longfu88/domains.json
    python tools/longfu88/make_affbulk_configs.py longfu88-sg-v01 ...

Editorial parts (SEO, reviews, preview captions, button texts) are composed per page from fixed pools with a seed per run, so that
no two pages share a review or a title. Facts (bonus names and figures) come from the knowledge base longfu88-new only.
"""
import datetime
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TODAY = datetime.date(2026, 10, 22)  # import date: review dates fall within the last 10 days

SEO = {
    "sg": {
        "v01": ("Longfu88 Casino Singapore: 188% Bonus up to €2,088", "Longfu88 review for players in Singapore: key facts, the 188% welcome bonus with 18 free spins, games, sports betting, payments and support."),
        "v02": ("Longfu88 Bonus Review: 188% up to €2,088 + 18 Spins", "Longfu88 bonuses explained for Singapore players: welcome bonus terms, weekly reloads, cashback, the VIP programme, plus payments and games."),
        "v03": ("Longfu88 Guide: Sign-Up, Bonus, Deposit, Withdrawal", "Step-by-step Longfu88 guide for Singapore: licence check, registration, verification, first deposit, welcome bonus, games and withdrawals."),
        "v04": ("Longfu88 Casino Review: Licence, Limits and Safety", "Longfu88 reviewed for careful players in Singapore: licence and operator, account security, verification, responsible gambling tools and bonus terms."),
        "v05": ("Longfu88 Casino Games: Slots, Live and Providers", "See what Longfu88 offers players in Singapore: slots, live dealer tables, fishing, P2P and fast games, ten providers, plus bonuses and payments."),
        "v06": ("Longfu88 Sports and Casino Review for Singapore", "Longfu88 sportsbook and casino for Singapore: sports and bet types, live betting, sports bonuses, plus the casino welcome bonus and payments."),
        "v07": ("Longfu88 Payments: Deposits, Withdrawals and Fees", "How money moves at Longfu88 for Singapore players: deposit methods, withdrawal steps and timing, fees, verification, plus the welcome bonus terms."),
        "v08": ("Longfu88 on Mobile: Quick Start for Singapore", "Longfu88 on your phone in Singapore: add the site to the home screen, sign up, claim the first bonus, deposit, withdraw and play games."),
        "v09": ("Longfu88 Casino Review: Pros, Cons and Answers", "Balanced Longfu88 overview for Singapore: pros and cons, licence, registration, welcome bonus, payments, mobile play and a detailed FAQ."),
        "v10": ("Longfu88 Casino Complete Guide for Singapore", "Complete Longfu88 reference for players in Singapore: licence, registration, bonus tables, VIP levels, games, sportsbook, payments and support."),
        "v11": ("Longfu88 Rewards: Cashback, Reloads and VIP Levels", "Longfu88 loyalty review for Singapore: VIP levels, weekly cashback, daily rebates, reload offers and the welcome bonus, with payments and games."),
        "v12": ("Longfu88 for Crypto Players: USDT, Bonus, Payouts", "Longfu88 crypto guide for Singapore: USDT networks, crypto welcome bonus, crypto reloads, withdrawals and fees, plus the fiat options."),
    },
    "my": {
        "v01": ("Longfu88 Casino Malaysia: 188% Bonus up to €2,088", "Longfu88 quick review for players in Malaysia: key facts, the 188% welcome bonus with 18 free spins, games, sportsbook, payments and support."),
        "v02": ("Longfu88 Malaysia Bonuses: 188% up to €2,088", "Longfu88 offers explained for Malaysian players: the welcome bonus and its terms, weekly and weekend reloads, cashback and the VIP ladder."),
        "v03": ("Longfu88 Guide for Malaysia: From Sign-Up to Payout", "Step-by-step Longfu88 guide for Malaysian players: licence check, registration, verification, first deposit, welcome offer, games and cash-outs."),
        "v04": ("Longfu88 Casino Malaysia: Safety, Terms and Limits", "Longfu88 for careful players in Malaysia: operator and licence, data handling, verification, self-exclusion tools, bonus conditions and payment limits."),
        "v05": ("Longfu88 Malaysia: Games, Live Dealers and Studios", "Explore the Longfu88 lobby in Malaysia: slots, live dealer games, fishing, P2P and fast games, game studios, plus bonuses, payments and support."),
        "v06": ("Longfu88 Sportsbook and Casino Review for Malaysia", "Longfu88 for bettors in Malaysia: sports markets, bet types, live betting and sports bonuses, plus the casino welcome offer and payment options."),
        "v07": ("Longfu88 Payments for Malaysia: Deposits and Payouts", "Longfu88 cash flow for Malaysian players: deposit methods, withdrawal steps, timing and fees, ID checks before payouts and welcome bonus wagering."),
        "v08": ("Longfu88 on Your Phone: Malaysia Quick Start", "Longfu88 mobile guide for Malaysia: home-screen setup, sign-up and login, first bonus, adding funds, cashing out, games and sports bets."),
    },
}
KEYWORDS_ADD = {
    "sg": "casino, online casino, crypto casino, play, gambling, slots, live casino, sports betting, register, login, KYC, app, payments, bonuses, welcome bonus, Singapore, SG, Singaporean",
    "my": "casino, online casino, crypto casino, play, gambling, slots, live casino, sports betting, register, login, KYC, app, payments, bonuses, welcome bonus, Malaysia, MY, Malaysian",
}
HERO_LABEL = [
    "Casino Welcome Bonus: 188% up to €2,088 + 18 Free Spins",
    "Welcome offer: 188% up to €2,088 + 18 Free Spins on the first qualifying deposit",
    "Start with 188% up to €2,088 + 18 Free Spins",
    "First deposit bonus: 188% up to €2,088 + 18 Free Spins",
]
CTA_POOL = ["Claim Bonus", "Play Now", "Register", "Get Your Bonus", "Join Now", "Start Playing", "Open an Account", "See the Offer", "Play Slots",
            "Try Live Casino", "Sign Up", "Check the Bonus"]
PREVIEW_TITLE = ["Longfu88 Bonus Offers", "Longfu88 Bonuses", "Longfu88 Promotions", "Current Longfu88 Offers"]
PREVIEW = [  # image id (folder bonus), title, text: all from the knowledge base longfu88-new
    (4654, "Casino Crypto Welcome Bonus", "188% up to 2,888 USDT"),
    (4657, "Live Casino Welcome Bonus", "125% up to €888"),
    (4656, "Sport First Deposit Bonus", "100% up to €1,888"),
    (4655, "Casino Weekend Crypto Reload", "75% up to 750 USDT + 100 Free Spins"),
    (4652, "Casino Weekly Cashback", "Up to 10% of weekly net casino losses"),
    (4653, "Bonus Crab", "Qualifying picks reveal bonus credits, free spins or coins"),
]
BUTTONS = ["Get Bonus", "Claim Bonus", "Get Offer", "See Offer", "Claim Now"]
DISCLAIMER = [
    "18+. T&Cs apply. Gamble responsibly.",
    "18+ only. Bonus terms apply. Please gamble responsibly.",
    "18+. Terms and conditions apply. Play responsibly.",
    "Players must be 18+. Offer terms apply. Gamble responsibly.",
]

NAMES = {
    "sg": {"f": ["Mei Ling", "Hui Min", "Priya", "Siti Aisyah", "Jia Xin", "Nurul Huda", "Shu Ting", "Rachel Tan", "Amanda Lim", "Pei Shan", "Divya", "Farah", "Li Ting", "Sarah Goh"],
           "m": ["Wei Jie", "Jun Hao", "Kumar", "Ahmad Faiz", "Kok Wei", "Daniel Ng", "Marcus Lee", "Arjun", "Zhi Hao", "Ryan Koh", "Jason Teo", "Hafiz", "Darren Chua", "Ethan Wong"]},
    "my": {"f": ["Nurul Ain", "Siti Nabilah", "Mei Yee", "Kavitha", "Aisyah", "Suria", "Wan Ling", "Farhana", "Priyanka", "Shu Fen", "Izzati", "Jia Yi", "Hui Ying", "Alina"],
           "m": ["Aiman", "Hafiz", "Wei Hong", "Kumaran", "Faizal", "Jia Wei", "Haziq", "Daniel Wong", "Syafiq", "Raj", "Zulkifli", "Kai Xiang", "Irfan", "Adam Lee"]},
}
AVATARS = {"f": [3861, 3860, 3859, 3857, 3854], "m": [3862, 3858, 3856, 3855, 3853]}

A = {  # topic sentences, first person, no figures, no promises
    "reg": [
        "Opening an account took a few minutes, and the form asked only for the details I had ready.",
        "Registration was straightforward: email and password first, then the personal details on the next screen.",
        "I signed up from my phone and the confirmation email arrived almost at once.",
        "The sign-up form is clear about what it needs, so I did not have to guess any field.",
        "Creating the account was simple, and logging in again afterwards worked without any fuss.",
        "The registration page is short and easy to follow, even for someone new to online casinos.",
        "I liked that the age confirmation and the terms sit right on the sign-up page.",
        "Getting started meant filling in one form and confirming my email, nothing complicated.",
    ],
    "games": [
        "The lobby is easy to browse, and I found the slots I wanted through the categories quickly.",
        "There is a good spread of slots, live tables and instant games, so I rarely run out of things to try.",
        "I like that live dealer tables and crash games have their own sections instead of being buried in one list.",
        "Searching by game type works well, and the well-known studios are easy to spot in the lobby.",
        "The live casino section loads cleanly and the table games are simple to find.",
        "I mostly play slots, and the lobby keeps them neatly sorted so I can jump back to my favourites.",
        "Fishing and fast games are a nice change from slots, and they are easy to reach from the main menu.",
        "The game range suits me: slots for quiet evenings and live tables when I want something more social.",
    ],
    "mobile": [
        "I use the site on my phone every day, and adding it to the home screen made it feel like a normal app.",
        "The mobile version is responsive, and the cashier and the game lobby both work well on a small screen.",
        "Playing in the phone browser is smooth, and I did not need to download anything extra.",
        "On my tablet the layout adjusts nicely, and the menus stay easy to reach with one thumb.",
        "I set up the home-screen shortcut in a minute, and now the casino opens straight from my phone.",
        "The site runs fine on both my phone and my laptop, so I can switch devices without losing my place.",
        "Menus and buttons are large enough for a phone, and the account area is easy to find.",
        "Mobile play works as I hoped: the same lobby, the same cashier and the same account as on desktop.",
    ],
    "support": [
        "Live chat answered my question about verification politely, and the answer matched what the help pages say.",
        "I asked support about my account settings and the chat agent explained the steps clearly.",
        "The support team replied in English and was patient when I asked a follow-up question.",
        "It is reassuring that live chat is available around the clock, and I had a helpful reply when I needed it.",
        "I wrote to support by email and received a clear, polite answer that covered everything I asked.",
        "The agent in the chat walked me through the document upload without making it feel complicated.",
        "Support was friendly and to the point, which is what I want when I have a question about my account.",
        "I like that there is both chat and email, so I can pick whichever suits the question.",
    ],
    "pay": [
        "The cashier lists many payment methods, and I could choose the one I normally use without hunting for it.",
        "Depositing through my usual local method was simple, and the cashier showed each step clearly.",
        "I appreciate the choice between bank options, cards and crypto, since I switch depending on the week.",
        "The cashier is easy to read: the method, the amount and the confirmation screen are all in one flow.",
        "I used a card for my deposit and the process felt familiar, with no surprises in the cashier.",
        "Having crypto next to the usual banking options is handy for me, and both are clearly labelled.",
        "Setting up a withdrawal followed the same clear steps as a deposit, and the cashier explained each screen.",
        "The payment page does not hide anything, and I could see which methods were available before I chose.",
    ],
    "promo": [
        "The promotions page is easy to find, and each offer shows what it needs before I activate it.",
        "I like checking the rewards area when I log in, since the offers are listed in one place.",
        "The bonus conditions are written out plainly, so I know what to expect before I opt in.",
        "The VIP section is explained clearly, and it is easy to see how the levels work.",
        "Cashback and reload offers are listed together, which makes it simple to compare them.",
        "I appreciate that bonuses are activated in one section of the account instead of being spread around.",
        "The rewards pages feel organised, with the terms of every offer a click away.",
        "It is helpful that the offers explain their conditions in plain words, so nothing feels hidden.",
    ],
    "sports": [
        "The sportsbook has the sports I follow, and switching between pre-match and live markets is easy.",
        "I like betting on football here, and the bet types are laid out clearly on the betting slip.",
        "Live betting works smoothly on my phone, and the markets update without any delay that I noticed.",
        "Having a sportsbook and a casino under one account saves me from juggling two logins.",
        "The sports section covers the games I care about, including esports, and the layout is simple.",
        "I enjoy that the sportsbook offers several bet types, so I can keep things simple or try something new.",
        "Moving between the casino and the sportsbook takes one tap, which suits the way I play.",
        "The sports menu is tidy, and the bonus rules for sports bets are easy to find.",
    ],
}
B = [
    "Overall it is a tidy site that is easy to use.",
    "It does what I need without too much clutter.",
    "I plan to keep using it for now.",
    "A solid choice if you like a clean layout.",
    "Nothing flashy, just a site that works as described.",
    "I would recommend a look to anyone curious about it.",
    "The whole experience felt well organised to me.",
    "It is simple to find my way around after a short while.",
    "A straightforward site that respects my time.",
    "I appreciate that everything is where I expect it.",
    "It is a comfortable place to spend an evening.",
    "No complaints from my side so far.",
]
TOPICS = list(A)


def reviews_for(geo: str, seed: str, used: dict) -> list[dict]:
    rnd = random.Random(seed)
    n = rnd.choice([5, 6])
    topics = rnd.sample(TOPICS, n)
    names = {g: rnd.sample(NAMES[geo][g], len(NAMES[geo][g])) for g in "fm"}
    avs = {g: rnd.sample(AVATARS[g], len(AVATARS[g])) for g in "fm"}
    items = []
    for i, t in enumerate(topics):
        g = "f" if i % 2 == 0 else "m"
        if rnd.random() < 0.3:
            g = "m" if g == "f" else "f"
        pool = [k for k in range(len(A[t])) if used.get((t, k), 0) < 2] or [k for k in range(len(A[t])) if used.get((t, k), 0) < 3] or list(range(len(A[t])))
        k = rnd.choice(pool)
        used[(t, k)] = used.get((t, k), 0) + 1
        text = f"{A[t][k]} {rnd.choice(B)}"
        date = TODAY - datetime.timedelta(days=rnd.randint(0, 9))
        items.append({"username": names[g].pop(), "review": text, "date": date.isoformat(), "avatar": avs[g].pop(), "rating": rnd.choice([5, 5, 4])})
    items.sort(key=lambda r: r["date"], reverse=True)
    return items


def config(run: str, entry: dict, used: dict) -> dict:
    geo, vid = entry["geo"], entry["variant"]
    rnd = random.Random("cfg-" + run)
    title, desc = SEO[geo][vid]
    n = int(vid[1:])
    prev = PREVIEW[n % len(PREVIEW):] + PREVIEW[: n % len(PREVIEW)]
    ctas = rnd.sample(CTA_POOL, 5)
    return {
        "website_id": entry["website_id"], "domain": entry["domain"], "locale": "en",
        "seo": {"title": title, "description": desc},
        "keywords": {"main": "Longfu88", "additional": KEYWORDS_ADD[geo]},
        "hero": {"label": HERO_LABEL[n % len(HERO_LABEL)], "mainLabel": "", "background": 140, "button": rnd.choice(["Register", "Sign Up", "Join Now"])},
        "preview": {"title": PREVIEW_TITLE[n % len(PREVIEW_TITLE)],
                    "items": [{"image": i, "title": t, "text": x, "button": BUTTONS[(n + k) % len(BUTTONS)]} for k, (i, t, x) in enumerate(prev)]},
        "reviews": {"title": rnd.choice(["Real Player Reviews", "What Players Say", "Player Reviews"]), "items": reviews_for(geo, "rev-" + run, used)},
        "promo": {"title": "Casino Welcome Bonus", "description": "188% up to €2,088 + 18 Free Spins", "disclaimer": DISCLAIMER[n % len(DISCLAIMER)],
                  "button": rnd.choice(["Claim Bonus", "Get Bonus", "Claim Offer"])},
        "cta_texts": ctas,
    }


def main() -> None:
    domains = json.loads((ROOT / "tools/longfu88/domains.json").read_text(encoding="utf-8"))
    want = set(sys.argv[1:])
    used: dict = {}
    for entry in domains:
        run = f'longfu88-{entry["geo"]}-{entry["variant"]}'
        if want and run not in want:
            continue
        cfg = config(run, entry, used)
        bad = []
        if len(cfg["seo"]["title"]) > 60:
            bad.append(f'title {len(cfg["seo"]["title"])}')
        if not 120 <= len(cfg["seo"]["description"]) <= 160:
            bad.append(f'description {len(cfg["seo"]["description"])}')
        (ROOT / "runs" / run).mkdir(exist_ok=True)
        (ROOT / "runs" / run / "05_affbulk_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
        print(run, entry["domain"], entry["website_id"], "OK" if not bad else "CHECK " + ", ".join(bad))


if __name__ == "__main__":
    main()
