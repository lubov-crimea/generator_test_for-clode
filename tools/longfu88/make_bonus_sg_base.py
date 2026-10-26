"""Builds runs/longfu88-bonus-sg/llm/brief.json and review.json (the answers of the manual step-1 requests) for the Longfu88
bonuses and promo code page (brand-subpage, GEO SG). Run from the project root:  python tools/longfu88/make_bonus_sg_base.py

This is the BASE ТЗ for the OPTIMUM size group of the competitors (`medium`: 2544 words = tips.gg, limit 3053; see runs/longfu88-bonus-sg/01_tiers.json;
small 631/683, large 2634 = longfu88-play.my). Four competitors were read (tips.gg and tribuna.com from the browser, their HTML is saved in
input/html/). The structure follows the clusters of the competitors (heading_clusters: tools/longfu88/make_bonus_sg_clusters.py):
k01 overview, k02 welcome bonus, k03 claim steps, k04 wagering and terms, k05 reload, k06 cashback, k20 FAQ, k21 verdict/strategy are mandatory
(the verdict is covered by a neutral "how to compare offers" checklist, never by advice); the unique topics that the knowledge base can fill are the
promo code question (the keyword), minimum deposits and payment rules (k12), free spins (k07), crypto and live offers, seasonal campaigns,
unlimited rebates, VIP program (k10), the rewards area (k09), sports bonuses (k11), verification, responsible use, mobile access (k13).
The base holds the WHOLE pool of topics: the variants (make_bonus_sg_variants.py) take a subset of it at different depths.

Facts: only the knowledge base longfu88-new. It has NO promo code, NO no-deposit bonus, NO bonus archive, NO country table. The competitors
show other sizes (100% up to $400, ~20x wagering, 10-14 days, "referral bonus", "bonus by country"): none of them may reach the text."""
import json
from pathlib import Path

RUN = Path("runs/longfu88-bonus-sg")
LEGAL = "Do not say or imply that the casino or its bonuses are licensed, legal or approved in Singapore, and do not discuss the licence on this page."
NO_INVENT = ("Use only the amounts, percentages, wagering multiples, periods and names of the Brand Information, character for character; no other offer, no code, no bonus that is not listed, "
             "no promise of winnings, no advice to claim every offer, no comparison with other casinos. Do not convert the euro amounts into Singapore dollars or other currencies.")
NO_CODE = "Do not invent a promo code, a coupon or a bonus code, and do not name any."
VIP_NOTE = ("Do not give the cashback percentages of the 25 VIP reward levels and do not link the five VIP tiers (Bronze to Diamond) to the numbered levels: the Brand Information does not say which level belongs to which tier. ")

P = "brandinfo_promotions.other_bonuses"
W = "brandinfo_welcome.welcome_bonus"
G = "brandinfo_promotions.gamification_features"
S = "brandinfo_sportsbook.sportsbook.sports_bonuses"
L = "brandinfo_loyalty.loyalty_vip_program"
V = "brandinfo_account.verification"

OFFER_NAMES = {-1: "Casino Welcome Bonus", 0: "Live Casino Welcome Bonus", 1: "Casino Crypto Welcome Bonus", 2: "Casino Weekly Reload", 3: "Casino Weekly Crypto Reload",
               4: "Casino Weekend Reload", 5: "Casino Weekend Crypto Reload", 6: "Casino Double Fortune: One-Day Reload Special",
               7: "Casino Trick or Treat Pumpkin Bonanza", 8: "Casino Dragon Quest: Get Verified and Get Extra!"}
SPORT_NAMES = {0: "Sport First Deposit Bonus", 1: "Sport Crypto Welcome Bonus", 2: "Sport Weekly Reload Bonus", 3: "Sport Weekend Reload Bonus",
               4: "Sport Crypto Weekly Reload", 5: "Sport Crypto Weekend Reload"}


def rng(mid):
    return round(mid * 0.88), round(mid * 1.12)


def rrefs(*idx, extra=()):
    """name, reward, minimum deposit and wagering of the other_bonuses items (a table row each)."""
    return [f"{P}[{i}].{f}" for i in idx for f in ("name", "reward", "minimum_deposit", "wagering_requirement")] + list(extra)


def mdrefs(idx):
    refs = []
    for i in idx:
        base = W if i == -1 else f"{P}[{i}]"
        refs += [f"{base}.name", f"{base}.minimum_deposit"]
    return refs


def srefs(idx):
    return [f"{S}[{i}].{f}" for i in idx for f in ("name", "reward", "minimum_deposit", "wagering_requirement")]


# pieces of the notes that the variants replace (exact text, shared through this module)
B13_LIVE = ("Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback, opt-in and activation in My Bonuses) in one sentence. ")
B13_VIP = ("After the paragraph a TABLE with three columns, VIP level | cashback percentage | maximum, and five rows (VIP Bronze 2% €1,888; VIP Silver 4% €2,388; VIP Gold 6% €2,988; "
           "VIP Platinum 8% €3,988; VIP Diamond 10% €6,988) exactly as in the Brand Information. ")
B13_TAIL = "Only real-money casino bets count toward the cashback; bonus funds are excluded. "

blocks = []


def add(level, heading, source, covers, refs, mid, kw, formats, ents, conns, summary, notes):
    lo, hi = rng(mid)
    blocks.append(dict(level=level, heading=heading, source=source, covers_clusters=covers, kb_refs=refs, words_min=lo, words_max=hi,
                       keywords=kw, formats=formats, entities=[{"name": n, "priority": p} for n, p in ents],
                       entity_connections=[{"subject": a, "relation": r, "object": c, "priority": p} for a, r, c, p in conns],
                       summary=summary, copywriter_notes=notes))


# keyword plan of the base (python -m textgen: keyword_targets Longfu88 27, the others 1; "Longfu88 bonus" 2):
#   headings: b01 "Longfu88 promotions", b02 + b05 "Longfu88 bonus", b03 "Longfu88 welcome bonus", b06 "Longfu88 promo code", b22 "Longfu88 offers";
#   body: "Longfu bonus" in b01, "Longfu88" 27 over all blocks (b01 3, b03 2, b04 2, b22 2, the others 1).
ZERO = {"Longfu bonus": 0, "Longfu88 bonus": 0, "Longfu88 welcome bonus": 0, "Longfu88 promo code": 0, "Longfu88 offers": 0, "Longfu88 promotions": 0}


def kw(brand, **more):
    d = {"Longfu88": brand, **ZERO}
    d.update(more)
    return d


# b01 intro (the H1 carries the keyword "Longfu88 promotions")
add(1, "Longfu88 Promotions: Bonuses and Promo Code Guide for Singapore", "h1", [],
    ["brandinfo_general.welcome_bonus_summary", "brandinfo_general.minimum_age"], 80,
    kw(3, **{"Longfu bonus": 1}), ["paragraph"],
    [("Casino Bonuses", 10), ("Welcome Bonus", 8), ("Minimum Age", 5)],
    [("Casino Bonuses", "start with", "the Casino Welcome Bonus for new players", 8)],
    "What the page covers: the welcome bonus and how to claim it, the terms behind every offer, the promo code question, reload, free spin, crypto and live offers, cashback, the VIP program, the rewards area and the sports bonuses.",
    'Open with "Longfu88" as the subject of the first sentence: the casino runs a set of bonuses that start with the Casino Welcome Bonus. The phrase "Longfu bonus" stands once in a sentence that says that players '
    'looking for the Longfu bonus find the welcome offer, the weekly and weekend reloads, cashback and a rewards area on this page. Quote the welcome bonus summary of the Brand Information once, character for character '
    '(188% up to €2,088 + 18 Free Spins; 25x deposit plus bonus, 40x Free Spins winnings). State once that the bonuses are for players aged 18 or over and that the page is written for players from Singapore. '
    f'Signpost the topics in one sentence without detail. {LEGAL} {NO_INVENT} Neutral tone, no promises. '
    'Use "Longfu88" exactly three times and "Longfu bonus" once, and no other tracked keyword (the heading carries "Longfu88 promotions").')

# b02 overview (k01); the heading carries "Longfu88 bonus"
add(2, "Longfu88 Bonus Types at a Glance", "mandatory", ["k01"],
    [f"{W}.name", f"{P}[0].name", f"{P}[1].name", f"{P}[4].name", f"{P}[2].name", f"{P}[9].name", f"{P}[10].name", f"{P}[11].name", f"{S}[0].name", f"{G}[0].name"], 110,
    kw(1), ["paragraph", "list"],
    [("Bonus Types", 10), ("Promotions", 7), ("Casino Welcome Bonus", 6)],
    [("Casino Bonuses", "fall into", "welcome offers, reload offers, cashback and rebates, sports offers and the rewards area", 8)],
    "An orientation list of the offer families: three welcome offers, the weekly and weekend reloads, the weekly and live cashback, the unlimited rebates, the sports offers and the rewards area.",
    'One lead-in sentence that says that the bonuses fall into five families, then a bulleted list of five items "family: names": welcome offers (Casino Welcome Bonus, Live Casino Welcome Bonus, Casino Crypto Welcome Bonus); '
    'reload offers (Casino Weekend Reload, Casino Weekly Reload); cashback and rebates (Casino Weekly Cashback, Live Casino Cashback, Unlimited Casino Rebate); sports offers (Sport First Deposit Bonus with the other sports bonuses named in one phrase); '
    'the rewards area (Bonus Crab with the other features named in one phrase). Use the names exactly as given; no amounts here (the sections below give them). One closing sentence says that every offer has its own terms and is activated in My Bonuses. '
    f'{NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword (the heading carries "Longfu88 bonus").')

# b03 welcome bonus (k02); the heading carries "Longfu88 welcome bonus"
add(2, "Longfu88 Welcome Bonus for New Players", "mandatory", ["k02"],
    [f"{W}.name", f"{W}.bonus_percentage", f"{W}.maximum_bonus", f"{W}.free_spins", f"{W}.minimum_deposit", f"{W}.eligibility",
     f"{P}[0].name", f"{P}[0].reward", f"{P}[1].name", f"{P}[1].reward", f"{P}[1].important_terms[2]"], 140,
    kw(2), ["paragraph"],
    [("Casino Welcome Bonus", 10), ("First Deposit", 8), ("Free Spins", 6)],
    [("Casino Welcome Bonus", "rewards", "the first qualifying deposit with a match bonus and free spins", 8)],
    "The main offer: the Casino Welcome Bonus of 188% up to €2,088 plus 18 Free Spins for a first deposit of €50, and the two alternative welcome offers (live casino and crypto).",
    'Lead with the Casino Welcome Bonus: a first-deposit casino bonus of 188% up to €2,088 plus 18 Free Spins; the minimum first deposit of the bonus is €50 (use the €50 of the bonus, do NOT mention the general minimum deposit of €10); '
    'it is for new registered players on the first qualifying deposit, one welcome offer per account. Then, in two or three sentences, the two alternatives of the Brand Information: the Live Casino Welcome Bonus (125% up to €888) and '
    'the Casino Crypto Welcome Bonus (188% up to 2,888 USDT), and say that the Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers. No wagering numbers here (the terms section gives them). '
    f'{NO_INVENT} Use "Longfu88" exactly twice and no other tracked keyword (the heading carries "Longfu88 welcome bonus").')

# b04 claim steps (k03)
add(2, "How to Claim the Welcome Bonus in Four Steps", "mandatory", ["k03"],
    [f"{W}.claiming_procedure", f"{W}.validity"], 100,
    kw(2), ["paragraph", "list"],
    [("Bonus Claim", 10), ("My Bonuses", 8), ("Wagering", 5)],
    [("Player", "activates", "the Casino Welcome Bonus in My Bonuses before placing any wager", 9)],
    "The four steps from registration to completed wagering, with the activation in My Bonuses before the first wager and the validity of 10 days.",
    'One lead-in sentence, then a NUMBERED list with the four steps of the claiming procedure in the order of the Brand Information (register an account and complete the required personal details; make the first qualifying deposit; '
    'activate the Casino Welcome Bonus in My Bonuses before placing any wagers; play eligible casino games and complete the wagering before expiry). Do not copy a step that contains the brand name: write "the casino" there. '
    'One closing sentence gives the validity: 10 days from activation, and warns that the activation must happen before any wager. '
    f'{NO_INVENT} Use "Longfu88" exactly twice (in the lead-in and the closing sentence, never inside the steps) and no other tracked keyword.')

# b05 wagering and terms (k04); the heading carries "Longfu88 bonus"
add(2, "Longfu88 Bonus Terms: Wagering, Limits and Validity", "mandatory", ["k04"],
    [f"{W}.wagering_requirement", f"{W}.free_spins_wagering", f"{W}.validity", f"{W}.maximum_bet", f"{W}.maximum_cashout",
     f"{W}.important_terms[0]", f"{W}.important_terms[2]", f"{W}.important_terms[3]", f"{W}.important_terms[4]"], 150,
    kw(1), ["paragraph", "table"],
    [("Wagering Requirement", 10), ("Maximum Bet", 7), ("Maximum Cashout", 6)],
    [("Wagering Requirement", "applies to", "the deposit plus the bonus amount, and separately to Free Spins winnings", 9)],
    "The terms of the Casino Welcome Bonus: wagering 25x deposit plus bonus and 40x Free Spins winnings, 10 days validity, maximum bet €22.5 per spin, maximum cashout 5x, and four rules that can cost the bonus.",
    'A TABLE with two columns, term | value, and five rows in this order: wagering (25x the deposit plus bonus amount), Free Spins wagering (40x Free Spins winnings), validity (10 days from activation), maximum bet '
    '(€22.5 per spin), maximum cashout (5x the initial bonus amount). After the table a short paragraph with the rules of the Brand Information that matter most: Neteller and Skrill deposits are excluded; only one promotional '
    'bonus may be active at a time; a withdrawal request before claiming or while the bonus is active can void the eligibility; cancelling the promotion forfeits bonus funds and unconverted promotional winnings. State them as facts, one clause each. '
    f'These terms belong to the Casino Welcome Bonus: say so. {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword (the heading carries "Longfu88 bonus").')

# b06 promo code (unique k08); the heading carries "Longfu88 promo code"
add(2, "Is There a Longfu88 Promo Code?", "unique", ["k08"],
    [f"{W}.claiming_procedure[2]", f"{P}[2].claiming_method"], 80,
    kw(1), ["paragraph"],
    [("Promo Code", 10), ("My Bonuses", 8)],
    [("My Bonuses", "activates", "every listed offer once the deposit conditions are met", 8)],
    "What the Brand Information says about claiming: the offers are activated in My Bonuses, and it lists no promo code.",
    'Answer the question of the heading in 3-4 sentences. The first sentence says that the Brand Information of the casino lists no promo code for its offers. '
    'Then say that the offers are activated in My Bonuses: the Casino Welcome Bonus before the first wager, the other offers after their eligibility and deposit conditions are met. Do NOT claim that codes never exist, '
    f'do NOT say that no code is "required" anywhere else and do not mention coupons or codes of other sites or of affiliate links. {NO_CODE} {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword (the heading carries "Longfu88 promo code").')

# b07 minimum deposits and payment rules (k12)
add(2, "Minimum Deposits and Payment Rules of Each Offer", "unique", ["k12"],
    mdrefs([-1, 0, 1, 2, 3, 4, 5, 6, 7]) + [f"{W}.important_terms[0]"], 100,
    kw(1), ["paragraph", "table"],
    [("Minimum Deposit", 10), ("Bonus Offers", 7), ("Excluded Payment Methods", 6)],
    [("Minimum Deposit", "differs by", "offer and by currency of the deposit", 8)],
    "The minimum deposit that each listed offer asks for, offer by offer, and the payment methods that are excluded from the welcome offers.",
    "One lead-in sentence that says that the minimum deposit depends on the offer, then a TABLE with two columns, offer | minimum deposit, and one row per offer in this order: "
    + ", ".join(OFFER_NAMES[i] for i in [-1, 0, 1, 2, 3, 4, 5, 6, 7])
    + " (names and values exactly as in the Brand Information; crypto offers in USDT). One closing sentence: Neteller and Skrill deposits are excluded from the Casino Welcome Bonus and from the Live Casino Welcome Bonus; "
    "the general minimum deposit of the casino is not the minimum of an offer, so the player checks the offer first. Do NOT state the general minimum deposit amount and do not list payment methods. "
    f'{NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b08 reload bonuses (k05)
add(2, "Reload Bonuses: Weekly, Weekend and One-Day Offers", "mandatory", ["k05"],
    rrefs(3, 4, 5, 6) + [f"{P}[4].validity", f"{P}[6].validity", f"{P}[4].important_terms[2]", f"{P}[4].important_terms[1]"], 170,
    kw(1), ["paragraph", "table"],
    [("Reload Bonus", 10), ("Minimum Deposit", 7), ("Wagering Requirement", 6)],
    [("Reload Bonus", "rewards", "repeat deposits during the week or at the weekend", 8)],
    "Four reload offers with reward, minimum deposit and wagering: weekly crypto reload, weekend reload, weekend crypto reload and the one-day Double Fortune special.",
    'One lead-in sentence that says that the reload offers reward repeat deposits, then a TABLE with four columns, offer | reward | minimum deposit | wagering, and four rows in this order: Casino Weekly Crypto Reload, '
    'Casino Weekend Reload, Casino Weekend Crypto Reload, Casino Double Fortune: One-Day Reload Special (values exactly as in the Brand Information). After the table two sentences: the weekly and weekend offers are valid for '
    '7 days and the Double Fortune special for 24 hours; the stake while wagering bonus funds is limited to €5 per spin, and a reload cannot be combined with another active casino bonus. The Casino Weekly Reload (50 Free Spins) '
    f'belongs to the free spins section: do not describe it here. {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b09 free spins (k07)
add(2, "Free Spins Offers and Their Wagering", "unique", ["k07"],
    [f"{P}[2].name", f"{P}[2].reward", f"{P}[2].minimum_deposit", f"{P}[2].wagering_requirement", f"{P}[7].name", f"{P}[7].reward",
     f"{P}[7].minimum_deposit", f"{P}[7].wagering_requirement", f"{W}.free_spins_wagering"], 90,
    kw(1), ["paragraph"],
    [("Free Spins", 10), ("Free Spins Winnings", 7)],
    [("Free Spins", "carry", "their own wagering on the winnings", 8)],
    "Where free spins come from: the 50 Free Spins of the Casino Weekly Reload, the up to 100 Free Spins of the seasonal Trick or Treat Pumpkin Bonanza and the 18 Free Spins of the welcome bonus, all with 40x wagering on the winnings.",
    'Lead with the Casino Weekly Reload: 50 Free Spins, minimum deposit €30, 40x winnings from Free Spins, valid 7 days. Then the seasonal Casino Trick or Treat Pumpkin Bonanza: up to 100 Free Spins, minimum deposit €20, '
    '40x Free Spins winnings. One clause recalls that the welcome bonus adds 18 Free Spins with 40x Free Spins winnings. Say that wagering is counted on the winnings of the free spins. '
    f'No game names for the spins (none are given), no spin value, no claim that the seasonal offer is running now. {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b10 crypto offers
add(2, "Crypto Welcome and Reload Offers", "unique", ["k02", "k05"],
    [f"{P}[1].name", f"{P}[1].reward", f"{P}[1].minimum_deposit", f"{P}[1].wagering_requirement", f"{P}[1].validity", f"{P}[1].important_terms[1]",
     f"{P}[1].eligible_cryptocurrencies"] + rrefs(3, 5), 120,
    kw(1), ["paragraph", "table"],
    [("Crypto Bonuses", 10), ("USDT", 7), ("Eligible Cryptocurrencies", 6)],
    [("Casino Crypto Welcome Bonus", "accepts", "a first qualifying crypto deposit", 8)],
    "The crypto offers: the Casino Crypto Welcome Bonus (188% up to 2,888 USDT), the weekly and weekend crypto reloads and the eligible coins.",
    "Lead with the Casino Crypto Welcome Bonus: 188% up to 2,888 USDT for a first qualifying crypto deposit of at least 50 USDT, wagering 40x deposit plus bonus, valid 10 days, maximum bonus wager 5 USDT per spin. "
    "Then a TABLE with four columns, offer | reward | minimum deposit | wagering, and two rows: Casino Weekly Crypto Reload, Casino Weekend Crypto Reload (values exactly as in the Brand Information). "
    "Then one sentence with the eligible cryptocurrencies as given (USDT, BTC, BCH, LTC, ETH, XRP, USDC). The Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers: say so once. "
    f'{NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b11 live casino offers
add(2, "Live Casino Welcome Bonus, Cashback and Rebate", "unique", ["k02", "k06"],
    [f"{P}[0].name", f"{P}[0].reward", f"{P}[0].minimum_deposit", f"{P}[0].wagering_requirement", f"{P}[0].validity", f"{P}[0].important_terms[1]",
     f"{P}[10].name", f"{P}[10].reward", f"{P}[10].wagering_requirement", f"{P}[12].name", f"{P}[12].rebate_percentage"], 100,
    kw(1), ["paragraph"],
    [("Live Casino", 10), ("Live Casino Cashback", 7)],
    [("Live Casino Welcome Bonus", "targets", "new players who start with live casino games", 8)],
    "The live casino offers: the Live Casino Welcome Bonus (125% up to €888), the Live Casino Cashback (25% up to €850) and the Unlimited Live Casino Rebate (1.0%).",
    "Lead with the Live Casino Welcome Bonus: 125% up to €888, minimum deposit €30, wagering 30x the deposit plus bonus, valid 7 days, maximum bet €25, for new players on the first qualifying deposit. "
    "Then the Live Casino Cashback in one sentence (25% up to €850, wagering 10x the credited cashback, based on real-money stakes less winnings in eligible Live Casino games) and the Unlimited Live Casino Rebate "
    f'in one sentence (1.0%, credited daily). No game names. {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b12 seasonal and verification campaigns
add(2, "Seasonal and Verification Campaigns", "unique", ["k05"],
    rrefs(7, 8) + [f"{P}[7].validity", f"{P}[8].eligibility", f"{P}[8].important_terms[2]"], 110,
    kw(1), ["paragraph"],
    [("Seasonal Promotions", 10), ("Account Verification", 6)],
    [("Casino Dragon Quest", "rewards", "players who complete the requested account verification", 8)],
    "Two limited campaigns: the Trick or Treat Pumpkin Bonanza with up to 100 Free Spins and the Dragon Quest verification reward of a €10 bonus credit.",
    "Say first that campaigns come and go, so the list may change: the player checks the promotions page of the casino. Then the two campaigns of the Brand Information: the Casino Trick or Treat Pumpkin Bonanza "
    "(up to 100 Free Spins, minimum deposit €20, wagering 40x Free Spins winnings, valid 7 days) and the Casino Dragon Quest: Get Verified and Get Extra! (a €10 bonus credit for players who complete the requested "
    "account verification during the campaign, minimum deposit €20, wagering 30x the promotional credit, valid 7 days). Both carry the €5 per spin maximum stake while wagering bonus funds and cannot be combined with another active "
    f'casino bonus. Do not claim that either campaign is running now. {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b13 cashback (k06)
add(2, "Cashback: Weekly Rates by VIP Level and Live Casino Offer", "mandatory", ["k06"],
    [f"{P}[9].reward", f"{P}[9].calculation_period", f"{P}[9].minimum_cashback", f"{P}[9].opt_in", f"{P}[9].wagering_requirement", f"{P}[9].cashback_by_vip",
     f"{P}[10].reward", f"{P}[10].wagering_requirement"], 150,
    kw(1), ["paragraph", "table"],
    [("Cashback", 10), ("Net Losses", 6), ("VIP Level", 6)],
    [("Casino Weekly Cashback", "returns", "up to 10% of weekly net casino losses", 8)],
    "Cashback: the Casino Weekly Cashback of up to 10% of weekly net losses capped at €6,988 with its rates by VIP level, and the Live Casino Cashback of 25% up to €850.",
    'Lead with the Casino Weekly Cashback: up to 10% of weekly net casino losses, capped at €6,988, calculated Monday 00:00 UTC through Sunday 23:59 UTC, minimum cashback €4.5, opt-in for a four-week cycle, wagering 10x the cashback. '
    + B13_LIVE + B13_VIP + B13_TAIL +
    f'Say in one clause that the VIP program section below describes the reward levels. {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b14 rebates
add(2, "Unlimited Rebates by Game Category", "unique", ["k06"],
    [f"{P}[{i}].{f}" for i in (11, 12, 13, 14) for f in ("name", "rebate_percentage")] + [f"{P}[11].crediting", f"{P}[11].wagering_requirement"], 70,
    kw(1), ["paragraph", "table"],
    [("Rebate", 10), ("Rewards Balance", 6)],
    [("Unlimited Rebate", "returns", "a share of qualifying settled real-money wagering every day", 8)],
    "Four unlimited rebates of 0.8% to 1.0% of qualifying wagering, credited daily with 1x wagering on the credited rebate.",
    "One lead-in sentence that says that a rebate returns a share of qualifying settled real-money wagering on a game category, then a TABLE with two columns, rebate | rate, and four rows in this order: "
    "Unlimited Casino Rebate 0.9%, Unlimited Live Casino Rebate 1.0%, Unlimited P2P Rebate 0.8%, Unlimited Lottery Rebate 1.0%. One closing sentence: the rebate is credited daily to the rewards balance and carries "
    f'1x wagering on the credited rebate. {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b15 VIP program (k10)
VIP_LEVELS = [0, 4, 9, 14, 24]
add(2, "VIP Program: Points and Reward Levels", "unique", ["k10"],
    [f"{L}.tiers", f"{L}.progression", f"{L}.additional_benefits", f"{L}.important_terms[0]"]
    + [f"{L}.levels[{i}].{f}" for i in VIP_LEVELS for f in ("level", "points_required", "level_reward")], 150,
    kw(1), ["paragraph", "table"],
    [("VIP Program", 10), ("VIP Points", 8), ("Reward Levels", 7)],
    [("VIP Points", "unlock", "numbered reward levels", 8)],
    "The VIP program: VIP points earned through real-money play unlock 25 numbered reward levels with a reward and higher withdrawal limits; five named tiers from Bronze to Diamond.",
    "One or two sentences: the VIP program has five tiers (Bronze, Silver, Gold, Platinum, Diamond) and the player earns VIP points through eligible real-money gameplay, which unlock numbered reward levels. Then a TABLE with three columns, level | points required | level reward, "
    "and five rows for levels 1, 5, 10, 15 and 25 (values exactly as in the Brand Information; say in one clause that there are 25 levels in all). Then one sentence with the additional benefits (personalised offers, VIP cashback, higher withdrawal limits, a personal VIP manager for eligible high tiers) "
    "and one sentence that reward and withdrawal limits may differ by level and currency and that level-based benefits can change under the program rules. "
    f'Call it "the VIP Program" without the brand name. {VIP_NOTE}{NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b16 rewards area (k09)
add(2, "Rewards Area: Bonus Crab, Wheel of Fortune and Coin Shop", "unique", ["k09"],
    [f"{G}[0].name", f"{G}[0].mechanics", f"{G}[1].name", f"{G}[1].mechanics", f"{G}[2].name", f"{G}[3].name", f"{G}[4].name", f"{G}[4].rewards[0]"], 100,
    kw(1), ["paragraph", "list"],
    [("Rewards Area", 10), ("Coins", 7), ("Coin Shop", 6)],
    [("Coin Shop", "exchanges", "earned Coins for reward items and bonus credits", 8)],
    "The gamified part of the bonuses: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop, which exchanges Coins for rewards.",
    'One lead-in sentence that says that the rewards area adds game-like features to the bonuses, then a bulleted list of five items "name: what it does": Bonus Crab (claim qualifying picks to open a crab reward), '
    'Wheel of Fortune (spend an eligible spin or Coins to rotate a prize wheel), Challenges (complete qualifying gambling tasks to unlock listed rewards), Collections (collect campaign items by completing qualifying activity), '
    'Coin Shop (exchange earned Coins for rewards, reward items and bonus credits up to €4,500). Each item one short clause. '
    f'{NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b17 sports bonuses (k11)
add(2, "Sports Betting Bonuses and Qualifying Odds", "unique", ["k11"],
    srefs([0, 1, 2, 3]) + [f"{S}[0].validity", f"{S}[0].important_terms[1]", f"{S}[0].important_terms[2]", f"{S}[7].name", f"{S}[7].reward", f"{S}[9].name", f"{S}[9].reward"], 200,
    kw(1), ["paragraph", "table"],
    [("Sports Betting Bonuses", 10), ("Qualifying Bets", 7), ("Wagering Requirement", 6)],
    [("Qualifying Sports Bets", "count toward", "the wagering of a sports bonus", 8)],
    "The sports bonuses: first deposit, crypto welcome and reload offers with a low 8x wagering, the odds required for qualifying bets, the Sports Cashback and the Parlay Boost.",
    "One lead-in sentence that says that the sportsbook has its own bonuses, then a TABLE with four columns, offer | reward | minimum deposit | wagering, and four rows in this order: Sport First Deposit Bonus, Sport Crypto Welcome Bonus, "
    "Sport Weekly Reload Bonus, Sport Weekend Reload Bonus (values exactly as in the Brand Information). After the table two sentences: only settled qualifying sports bets count toward the wagering, single bets need odds of at least 2.00 and each "
    "accumulator selection at least 1.50, voided and cashed-out bets do not qualify; the offers are valid for 30 days. Then one sentence with the Sports Cashback (10% up to €2,500 of eligible sports net losses, weekly) and one with the Parlay Boost "
    f"(up to 100% extra winnings on qualifying accumulators). No sports tips, no odds of events. {NO_INVENT} Use \"Longfu88\" exactly once and no other tracked keyword.")

# b18 verification
add(2, "Verification Before Bonus Winnings", "unique", ["k04"],
    [f"{W}.important_terms[5]", f"{W}.important_terms[3]", f"{V}.documents", f"{V}.document_submission_window", f"{V}.typical_review_time"], 90,
    kw(1), ["paragraph", "list"],
    [("Account Verification", 10), ("Promotional Winnings", 7)],
    [("Account Verification", "can precede", "the payment of promotional winnings", 8)],
    "Verification can be required before promotional winnings are paid; the documents, the 30-day submission window and the review time of up to 10 days.",
    "Say first that account verification may be required before promotional winnings are paid and that a withdrawal request before claiming a bonus or while it is active can void the promotional eligibility. "
    "Then the documents of the Brand Information as a short bulleted list (government-issued photo ID or passport; proof of residential address; proof of ownership of a payment method; source of funds or wealth documents "
    "when requested), then one sentence with the submission window (up to 30 days when requested) and the review time (up to 10 days after a complete document set is received). "
    f'No other documents, no promise of speed. {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b19 responsible use
add(2, "Using Bonuses Responsibly", "unique", ["k04"],
    ["brandinfo_general.minimum_age", "brandinfo_responsible_gaming.responsible_gaming.policy", "brandinfo_responsible_gaming.responsible_gaming.self_assessment",
     "brandinfo_responsible_gaming.responsible_gaming.support_organizations", f"{W}.important_terms[4]"], 80,
    kw(1), ["paragraph"],
    [("Responsible Gambling", 10), ("Minimum Age", 6)],
    [("Bonus Terms", "should be read", "before the player accepts an offer", 7)],
    "Bonuses are for players of 18 or over who gamble where it is lawful; read the terms first, use the self-assessment questions and the support organisations of the casino.",
    "Say that the bonuses are for players aged 18 or over who gamble only where it is lawful, and that the terms of an offer (wagering, maximum bet, validity) should be read before accepting it. Cancelling the promotion "
    "forfeits bonus funds and unconverted promotional winnings (state it as a fact). Then one sentence on the self-assessment questions that help players identify possible gambling-related harm and one that names the "
    f'support organisations (GamCare, Gamblers Anonymous, Gambling Therapy). Do not print the e-mail address. No advice to chase losses, no promise. {LEGAL} {NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b20 mobile (k13)
add(2, "Claiming Bonuses on a Phone", "unique", ["k13"],
    ["brandinfo_app.app_information.mobile_access", "brandinfo_app.app_information.features"], 60,
    kw(1), ["paragraph"],
    [("Mobile Access", 10), ("My Bonuses", 6)],
    [("Responsive Website", "gives access to", "bonuses, deposits and the account on a phone", 7)],
    "The bonuses can be reached on a phone through the responsive website; no separate app is given.",
    "Two or three sentences: the casino website is responsive and works in the browser of a smartphone or tablet, and bonuses are among the features of the mobile website next to the casino, the sportsbook, account access, "
    "deposits and withdrawals. Do not say or imply that a native app, an APK file, a store listing or push notifications of bonuses exist: none is given. One pointer to the app page of the site is allowed in one clause. "
    f'{NO_INVENT} Use "Longfu88" exactly once and no other tracked keyword.')

# b21 compare offers (k21: replaces the competitors' verdict by a neutral checklist)
add(2, "How to Compare Offers Before You Claim", "mandatory", ["k21"],
    [f"{W}.eligibility", f"{W}.minimum_deposit", f"{W}.important_terms[0]", f"{W}.important_terms[2]", f"{W}.important_terms[3]", f"{W}.important_terms[5]",
     f"{W}.claiming_procedure[2]"], 100,
    kw(1), ["paragraph", "list"],
    [("Bonus Checklist", 10), ("My Bonuses", 7), ("Eligibility", 6)],
    [("Player", "checks", "eligibility, deposit and active bonus before claiming", 7)],
    "Seven checks before claiming the Casino Welcome Bonus: new player, first qualifying deposit of €50, Neteller and Skrill excluded, one active bonus, activation before wagering, no withdrawal request, verification.",
    "The competitors close with a verdict; this page closes with a neutral checklist and gives no recommendation. One lead-in sentence, then a bulleted list of seven short checks in this order: the player is a new registered player (one welcome offer per account); "
    "the first qualifying deposit is at least €50; the deposit is not made with Neteller or Skrill; no other promotional bonus is active; the bonus is activated in My Bonuses before any wager; no withdrawal request is made before claiming or while the bonus is active; "
    f"verification may be required before promotional winnings are paid. Each item one clause of up to 14 words. No verdict, no rating, no advice to take an offer. {NO_INVENT} Use \"Longfu88\" exactly once and no other tracked keyword.")

# b22 FAQ (k20); the heading carries "Longfu88 offers"
add(2, "Longfu88 Offers: Frequently Asked Questions", "mandatory", ["k20"],
    [f"{W}.minimum_deposit", f"{W}.validity", f"{W}.important_terms[2]", f"{P}[9].opt_in", "brandinfo_general.customer_support.channels", f"{W}.claiming_procedure[2]", f"{W}.important_terms[0]"], 180,
    kw(2), ["list"],
    [("Frequently Asked Questions", 10), ("Bonus Terms", 7)],
    [("Player", "finds", "short answers to the most frequent questions about the bonuses", 6)],
    "Seven short questions and answers on the first deposit, the number of active bonuses, the validity, the weekly cashback, the promo code, the excluded payment methods and where to get help.",
    'A bulleted list of seven items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required here for the question text only. Questions, in this order: '
    'what is the minimum first deposit for the welcome bonus (€50); how many promotional bonuses can be active at once (one); how long the welcome bonus is valid (10 days from activation); '
    'how the weekly cashback is claimed (opt in for a four-week cycle, then activate the credited cashback in My Bonuses); whether a promo code is needed (the Brand Information lists none; the offers are activated in My Bonuses); '
    'which payment methods are excluded from the welcome bonus (Neteller and Skrill); where to turn with a bonus question (customer support, live chat 24/7; do not print the e-mail address). '
    f'Answers repeat the facts of the sections above in other words and add nothing new. {NO_INVENT} Use "Longfu88" exactly twice and no other tracked keyword (the heading carries "Longfu88 offers").')

INTENT = ("A player in Singapore who searches for the Longfu88 bonus, welcome bonus, promo code, offers or promotions wants to know which bonuses the casino has, how large the welcome bonus is, "
          "how to claim it, what the wagering and other terms are, whether a promo code is needed, and what the reload, free spin, crypto, live casino, cashback, VIP, rewards and sports offers give. The facts come only from the knowledge base: "
          "the welcome bonus is 188% up to €2,088 plus 18 Free Spins, activated in My Bonuses, and no promo code is listed. The structure follows the bonus pages of the competitors of the medium size group (the longest one has about 25 headings); "
          "the competitors' own figures (100% up to $400, about 20x) are not the casino's and are not used. The page links to the login and app pages of the site only where a sentence needs the topic; the licence and payment methods belong to other pages.")

SKIPPED = []


def main():
    brief = {"intent_summary": INTENT, "blocks": blocks}
    if SKIPPED:
        brief["skipped_clusters"] = SKIPPED
    (RUN / "llm").mkdir(parents=True, exist_ok=True)
    for stale in list((RUN / "llm").glob("brief_*")) + list((RUN / "llm").glob("review_*")):
        stale.unlink()
    (RUN / "llm" / "brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=1), encoding="utf-8")
    (RUN / "llm" / "review.json").write_text(json.dumps({"issues": [], "blocks": blocks}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(blocks), "blocks, mid words", sum(round((b["words_min"] + b["words_max"]) / 2) for b in blocks))


if __name__ == "__main__":
    main()
