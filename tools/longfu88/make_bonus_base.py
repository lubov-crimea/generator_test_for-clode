"""Builds runs/longfu88-bonus-my/llm/brief.json and review.json (the answers of the manual step-1 requests) for the Longfu88
bonuses and promo code page (brand-subpage, GEO MY). Run from the project root:  python tools/longfu88/make_bonus_base.py

This is the BASE ТЗ for the OPTIMUM size group of the competitors (`medium`: 1029 words, limit 1235; see
runs/longfu88-bonus-my/01_tiers.json; three competitors were readable, tips.gg and tribuna.com answer 403). The structure comes from the
clusters of the competitors (the mandatory ones that belong to the topic, the VIP cluster k07 belongs to the VIP page and is skipped)
plus two unique blocks that the knowledge base can fill (the promo code question and the rewards area). The small texts are cut from it
and the large text adds blocks (tools/longfu88/make_bonus_variants.py).

Facts: only the knowledge base longfu88-new. It has NO promo code, NO no-deposit bonus, NO bonus archive: the text says what the
Brand Information says (activation in My Bonuses) and invents nothing. The competitors show other sizes (125% / $450, 200% / MYR 2,988,
60 spins): none of them may reach the text."""
import json
from pathlib import Path

RUN = Path("runs/longfu88-bonus-my")
LEGAL = "Do not say or imply that the casino or its bonuses are licensed, legal or approved in Malaysia, and do not discuss the licence on this page."
NO_INVENT = ("Use only the amounts, percentages, wagering multiples, periods and names of the Brand Information, character for character; no other offer, no code, no bonus that is not listed, "
             "no promise of winnings, no advice to claim every offer, no comparison with other casinos. Do not convert the euro amounts into other currencies.")
NO_CODE = "Do not invent a promo code, a coupon or a bonus code, and do not name any."
SPORT_PTR = "A pointer to the sports bonuses is allowed in one clause at most (the sportsbook has its own offers); do not list them."


def rng(mid):
    return round(mid * 0.88), round(mid * 1.12)


blocks = []


def add(level, heading, source, covers, refs, mid, kw, formats, ents, conns, summary, notes):
    lo, hi = rng(mid)
    blocks.append(dict(level=level, heading=heading, source=source, covers_clusters=covers, kb_refs=refs, words_min=lo, words_max=hi,
                       keywords=kw, formats=formats, entities=[{"name": n, "priority": p} for n, p in ents],
                       entity_connections=[{"subject": a, "relation": r, "object": c, "priority": p} for a, r, c, p in conns],
                       summary=summary, copywriter_notes=notes))


P = "brandinfo_promotions.other_bonuses"
W = "brandinfo_welcome.welcome_bonus"
G = "brandinfo_promotions.gamification_features"

# the six tracked keywords: "Longfu88" 28 (the heading occurrences of the longer keywords are not counted for it), the others 1 each
ZERO = {"Longfu bonus": 0, "Longfu88 welcome bonus": 0, "Longfu88 promo code": 0, "Longfu88 offers": 0, "Longfu88 promotions": 0}


def kw(brand, **more):
    d = {"Longfu88": brand, **ZERO}
    d.update(more)
    return d


# b01 intro (the H1 carries the keyword "Longfu88 promotions")
add(1, "Longfu88 Promotions: Bonuses and Promo Code Guide for Malaysia", "h1", [],
    ["brandinfo_general.welcome_bonus_summary", "brandinfo_general.minimum_age"], 60,
    kw(3, **{"Longfu bonus": 1}), ["paragraph"],
    [("Casino Bonuses", 10), ("Welcome Bonus", 8), ("Minimum Age", 5)],
    [("Casino Bonuses", "start with", "the Casino Welcome Bonus for new players", 8)],
    "What the page covers: the welcome bonus and how to claim it, the terms behind every offer, the promo code question, reload bonuses, free spins, cashback and the rewards area.",
    'Open with "Longfu88" as the subject of the first sentence: the casino runs a set of bonuses that start with the Casino Welcome Bonus. The phrase "Longfu bonus" stands once in a sentence that says that players '
    'looking for the Longfu bonus find the welcome offer, the weekly and weekend reloads, cashback and a rewards area on this page. Quote the welcome bonus summary of the Brand Information once, character for character '
    '(188% up to €2,088 + 18 Free Spins; 25x deposit plus bonus, 40x Free Spins winnings). State once that the bonuses are for players aged 18 or over and that the page is written for players from Malaysia. '
    f'Signpost the topics in one sentence without detail. {LEGAL} {NO_INVENT} Neutral tone, no promises.')

# b02 overview (k16)
add(2, "Bonus Types at a Glance", "mandatory", ["k16"],
    [f"{W}.name", f"{P}[0].name", f"{P}[1].name", f"{P}[4].name", f"{P}[2].name", f"{P}[9].name", f"{P}[10].name", f"{P}[11].name"], 85,
    kw(2), ["paragraph", "list"],
    [("Bonus Types", 10), ("Promotions", 7), ("Casino Welcome Bonus", 6)],
    [("Casino Bonuses", "fall into", "welcome offers, reload offers, cashback and rebates", 8)],
    "An orientation list of the offer families: three welcome offers, the weekly and weekend reloads, the weekly and live cashback and the unlimited rebates.",
    'One lead-in sentence that says that the bonuses fall into four families, then a bulleted list of four items "family: names": welcome offers (Casino Welcome Bonus, Live Casino Welcome Bonus, Casino Crypto Welcome Bonus); '
    'reload offers (Casino Weekend Reload, Casino Weekly Reload); cashback (Casino Weekly Cashback, Live Casino Cashback); rebates (Unlimited Casino Rebate, with the other categories named in one phrase). '
    'Use the names exactly as given; no amounts here (the sections below give them). One closing sentence says that every offer has its own terms and is activated in My Bonuses. '
    f'{SPORT_PTR} {NO_INVENT} Use "Longfu88" exactly twice and no other tracked keyword.')

# b03 welcome bonus (k01); the heading carries "Longfu88 welcome bonus"
add(2, "Longfu88 Welcome Bonus for New Players", "mandatory", ["k01"],
    [f"{W}.name", f"{W}.bonus_percentage", f"{W}.maximum_bonus", f"{W}.free_spins", f"{W}.minimum_deposit", f"{W}.eligibility",
     f"{P}[0].reward", f"{P}[1].reward", f"{P}[1].important_terms[2]"], 85,
    kw(3), ["paragraph"],
    [("Casino Welcome Bonus", 10), ("First Deposit", 8), ("Free Spins", 6)],
    [("Casino Welcome Bonus", "rewards", "the first qualifying deposit with a match bonus and free spins", 8)],
    "The main offer: the Casino Welcome Bonus of 188% up to €2,088 plus 18 Free Spins for a first deposit of €50, and the two alternative welcome offers (live casino and crypto).",
    'Lead with the Casino Welcome Bonus: a first-deposit casino bonus of 188% up to €2,088 plus 18 Free Spins; the minimum first deposit of the bonus is €50 (use the €50 of the bonus, do NOT mention the general minimum deposit of €10); '
    'it is for new registered players on the first qualifying deposit, one welcome offer per account. Then, in two sentences, the two alternatives of the Brand Information: the Live Casino Welcome Bonus (125% up to €888) and '
    'the Casino Crypto Welcome Bonus (188% up to 2,888 USDT), and say that the Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers. No wagering numbers here (the terms section gives them). '
    f'{NO_INVENT} Use "Longfu88" exactly three times and no other tracked keyword (the heading carries "Longfu88 welcome bonus").')

# b04 claim steps (k02)
add(2, "How to Claim the Welcome Bonus", "mandatory", ["k02"],
    [f"{W}.claiming_procedure", f"{W}.validity"], 80,
    kw(3), ["paragraph", "list"],
    [("Bonus Claim", 10), ("My Bonuses", 8), ("Wagering", 5)],
    [("Player", "activates", "the Casino Welcome Bonus in My Bonuses before placing any wager", 9)],
    "The four steps from registration to completed wagering, with the activation in My Bonuses before the first wager and the validity of 10 days.",
    'One lead-in sentence, then a NUMBERED list with the four steps of the claiming procedure in the order of the Brand Information (register an account and complete the required personal details; make the first qualifying deposit; '
    'activate the Casino Welcome Bonus in My Bonuses before placing any wagers; play eligible casino games and complete the wagering before expiry). Do not copy a step that contains the brand name: write "the casino" there. '
    'One closing sentence gives the validity: 10 days from activation, and warns that the activation must happen before any wager. '
    f'{NO_INVENT} Use "Longfu88" exactly three times (in the lead-in and the closing sentence, never inside the steps) and no other tracked keyword.')

# b05 wagering and terms (k03)
add(2, "Wagering and Bonus Terms", "mandatory", ["k03"],
    [f"{W}.wagering_requirement", f"{W}.free_spins_wagering", f"{W}.validity", f"{W}.maximum_bet", f"{W}.maximum_cashout",
     f"{W}.important_terms[0]", f"{W}.important_terms[2]", f"{W}.important_terms[3]", f"{W}.important_terms[5]"], 110,
    kw(2), ["paragraph", "table"],
    [("Wagering Requirement", 10), ("Maximum Bet", 7), ("Maximum Cashout", 6)],
    [("Wagering Requirement", "applies to", "the deposit plus the bonus amount, and separately to Free Spins winnings", 9)],
    "The terms of the Casino Welcome Bonus: wagering 25x deposit plus bonus and 40x Free Spins winnings, 10 days validity, maximum bet €22.5 per spin, maximum cashout 5x, and four rules that can cost the bonus.",
    'A TABLE with two columns, term | value, and five rows in this order: wagering (25x the deposit plus bonus amount), Free Spins wagering (40x Free Spins winnings), validity (10 days from activation), maximum bet '
    '(€22.5 per spin), maximum cashout (5x the initial bonus amount). After the table a short paragraph with the rules of the Brand Information that matter most: Neteller and Skrill deposits are excluded; only one promotional '
    'bonus may be active at a time; a withdrawal request before claiming or while the bonus is active can void the eligibility; verification may be required before promotional winnings are paid. State them as facts, one clause each. '
    f'These terms belong to the Casino Welcome Bonus: say so. {NO_INVENT} Use "Longfu88" exactly twice and no other tracked keyword.')

# b06 promo code (unique k09); the keyword "Longfu88 promo code" stands in the body
add(2, "Is a Promo Code Needed?", "unique", ["k09"],
    [f"{W}.claiming_procedure[2]", f"{P}[2].claiming_method"], 60,
    kw(2, **{"Longfu88 promo code": 1}), ["paragraph"],
    [("Promo Code", 10), ("My Bonuses", 8)],
    [("My Bonuses", "activates", "every listed offer once the deposit conditions are met", 8)],
    "What the Brand Information says about claiming: the offers are activated in My Bonuses, and it lists no promo code.",
    'Answer the question of the heading in 3-4 sentences. The phrase "Longfu88 promo code" stands once in the first sentence, which says that the Brand Information of the casino lists no Longfu88 promo code for its offers. '
    'Then say that the offers are activated in My Bonuses: the Casino Welcome Bonus before the first wager, the other offers after their eligibility and deposit conditions are met. Do NOT claim that codes never exist, '
    f'do NOT say that no code is "required" anywhere else and do not mention coupons or codes of other sites. {NO_CODE} {NO_INVENT} Use "Longfu88" exactly twice and the keyword "Longfu88 promo code" once.')

# b07 reload bonuses (k04)
add(2, "Reload Bonuses: Weekly and Weekend Offers", "mandatory", ["k04"],
    [f"{P}[3].name", f"{P}[3].reward", f"{P}[3].minimum_deposit", f"{P}[3].wagering_requirement",
     f"{P}[4].name", f"{P}[4].reward", f"{P}[4].minimum_deposit", f"{P}[4].wagering_requirement",
     f"{P}[5].name", f"{P}[5].reward", f"{P}[5].minimum_deposit", f"{P}[5].wagering_requirement",
     f"{P}[6].name", f"{P}[6].reward", f"{P}[6].minimum_deposit", f"{P}[6].wagering_requirement", f"{P}[6].validity", f"{P}[4].important_terms[2]"], 120,
    kw(3), ["paragraph", "table"],
    [("Reload Bonus", 10), ("Minimum Deposit", 7), ("Wagering Requirement", 6)],
    [("Reload Bonus", "rewards", "repeat deposits during the week or at the weekend", 8)],
    "Four reload offers with reward, minimum deposit and wagering: weekly crypto reload, weekend reload, weekend crypto reload and the one-day Double Fortune special.",
    'One lead-in sentence that says that the reload offers reward repeat deposits, then a TABLE with four columns, offer | reward | minimum deposit | wagering, and four rows in this order: Casino Weekly Crypto Reload, '
    'Casino Weekend Reload, Casino Weekend Crypto Reload, Casino Double Fortune: One-Day Reload Special (values exactly as in the Brand Information). After the table two sentences: the weekly and weekend offers are valid for '
    '7 days and the Double Fortune special for 24 hours; the stake while wagering bonus funds is limited to €5 per spin, and a reload cannot be combined with another active casino bonus. The Casino Weekly Reload (50 Free Spins) '
    f'belongs to the free spins section below: do not describe it here. {NO_INVENT} Use "Longfu88" exactly three times and no other tracked keyword.')

# b08 free spins (k06)
add(2, "Free Spins Offers", "mandatory", ["k06"],
    [f"{P}[2].name", f"{P}[2].reward", f"{P}[2].minimum_deposit", f"{P}[2].wagering_requirement", f"{P}[7].name", f"{P}[7].reward",
     f"{P}[7].minimum_deposit", f"{P}[7].wagering_requirement", f"{W}.free_spins_wagering"], 75,
    kw(2), ["paragraph"],
    [("Free Spins", 10), ("Free Spins Winnings", 7)],
    [("Free Spins", "carry", "their own wagering on the winnings", 8)],
    "Where free spins come from: the 50 Free Spins of the Casino Weekly Reload, the up to 100 Free Spins of the seasonal Trick or Treat Pumpkin Bonanza and the 18 Free Spins of the welcome bonus, all with 40x wagering on the winnings.",
    'Lead with the Casino Weekly Reload: 50 Free Spins, minimum deposit €30, 40x winnings from Free Spins, valid 7 days. Then the seasonal Casino Trick or Treat Pumpkin Bonanza: up to 100 Free Spins, minimum deposit €20, '
    '40x Free Spins winnings. One clause recalls that the welcome bonus adds 18 Free Spins with 40x Free Spins winnings. Say that wagering is counted on the winnings of the free spins. '
    f'No game names for the spins (none are given), no spin value, no claim that the seasonal offer is running now. {NO_INVENT} Use "Longfu88" exactly twice and no other tracked keyword.')

# b09 cashback (k05)
add(2, "Cashback and Rebates", "mandatory", ["k05"],
    [f"{P}[9].reward", f"{P}[9].calculation_period", f"{P}[9].minimum_cashback", f"{P}[9].opt_in", f"{P}[9].wagering_requirement",
     f"{P}[10].reward", f"{P}[10].wagering_requirement", f"{P}[11].rebate_percentage", f"{P}[12].rebate_percentage"], 110,
    kw(3), ["paragraph"],
    [("Cashback", 10), ("Rebate", 6), ("Net Losses", 6)],
    [("Casino Weekly Cashback", "returns", "up to 10% of weekly net casino losses", 8)],
    "Cashback and rebates: the Casino Weekly Cashback of up to 10% of weekly net losses capped at €6,988, the Live Casino Cashback of 25% up to €850 and the daily Unlimited Rebates.",
    'Lead with the Casino Weekly Cashback: up to 10% of weekly net casino losses, capped at €6,988, calculated Monday 00:00 UTC through Sunday 23:59 UTC, minimum cashback €4.5, opt-in for a four-week cycle, wagering 10x the cashback. '
    'Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback) in one sentence, and the Unlimited Casino Rebate (0.9%) and the Unlimited Live Casino Rebate (1.0%) in one sentence: '
    'rebates are credited daily and carry 1x wagering on the credited rebate (that figure is in the Brand Information, state it once). Only real-money bets count; bonus funds are excluded. '
    f'Do not give the VIP cashback levels (the VIP page of the site covers them). {NO_INVENT} Use "Longfu88" exactly three times and no other tracked keyword.')

# b10 rewards area (unique k08)
add(2, "Rewards Area: Bonus Crab, Wheel of Fortune and Coin Shop", "unique", ["k08"],
    [f"{G}[0].name", f"{G}[0].mechanics", f"{G}[1].name", f"{G}[1].mechanics", f"{G}[2].name", f"{G}[3].name", f"{G}[4].name", f"{G}[4].rewards[0]"], 70,
    kw(2), ["paragraph", "list"],
    [("Rewards Area", 10), ("Coins", 7), ("Coin Shop", 6)],
    [("Coin Shop", "exchanges", "earned Coins for reward items and bonus credits", 8)],
    "The gamified part of the bonuses: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop, which exchanges Coins for rewards.",
    'One lead-in sentence that says that the rewards area adds game-like features to the bonuses, then a bulleted list of five items "name: what it does": Bonus Crab (claim qualifying picks to open a crab reward), '
    'Wheel of Fortune (spend an eligible spin or Coins to rotate a prize wheel), Challenges (complete qualifying gambling tasks to unlock listed rewards), Collections (collect campaign items by completing qualifying activity), '
    'Coin Shop (exchange earned Coins for rewards, reward items and bonus credits up to €4,500). Each item one short clause. '
    f'{NO_INVENT} Use "Longfu88" exactly twice and no other tracked keyword.')

# b11 FAQ (k17); the heading carries "Longfu88 offers"
add(2, "Longfu88 Offers: Frequently Asked Questions", "mandatory", ["k17"],
    [f"{W}.minimum_deposit", f"{W}.validity", f"{W}.important_terms[2]", f"{P}[9].opt_in", "brandinfo_general.customer_support.channels"], 100,
    kw(3), ["list"],
    [("Frequently Asked Questions", 10), ("Bonus Terms", 7)],
    [("Player", "finds", "short answers to the most frequent questions about the bonuses", 6)],
    "Five short questions and answers on the first deposit, the number of active bonuses, the validity, the weekly cashback and where to get help.",
    'A bulleted list of five items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required here for the question text only. Questions, in this order: '
    'what is the minimum first deposit for the welcome bonus (€50); how many promotional bonuses can be active at once (one); how long the welcome bonus is valid (10 days from activation); '
    'how the weekly cashback is claimed (opt in for a four-week cycle, and activate the credited cashback in My Bonuses); where to turn with a bonus question (customer support, live chat 24/7; do not print the e-mail address). '
    f'Answers repeat the facts of the sections above in other words and add nothing new. {NO_INVENT} Use "Longfu88" exactly three times and no other tracked keyword (the heading carries "Longfu88 offers").')

intent = ("A player in Malaysia who searches for the Longfu88 bonus, welcome bonus, promo code, offers or promotions wants to know which bonuses the casino has, how large the welcome bonus is, "
          "how to claim it, what the wagering and other terms are, whether a promo code is needed, and what the reload, free spin, cashback and rewards offers give. The facts come only from the knowledge base: "
          "the welcome bonus is 188% up to €2,088 plus 18 Free Spins, activated in My Bonuses, and no promo code is listed. The structure follows the bonus pages of the competitors of the medium size group; "
          "the VIP programme, the sports offers, payments and the licence belong to other pages of the site.")

brief = {"intent_summary": intent, "blocks": blocks,
         "skipped_clusters": [{"id": "k07", "reason": "belongs to the VIP Program page of the site; the VIP cashback levels are left to that page"}]}
(RUN / "llm").mkdir(parents=True, exist_ok=True)
(RUN / "llm" / "brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=1), encoding="utf-8")
(RUN / "llm" / "review.json").write_text(json.dumps({"issues": [], "blocks": blocks}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(blocks), "blocks, mid words", sum(round((b["words_min"] + b["words_max"]) / 2) for b in blocks))
