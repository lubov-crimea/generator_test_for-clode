"""Blueprint of 12 ТЗ variants for the Longfu88 bonuses and promo code page (brand-subpage, GEO SG) -> input/variants/longfu88-bonus-sg.json.
Base run: runs/longfu88-bonus-sg (tools/longfu88/make_bonus_sg_base.py, the OPTIMUM group `medium`). Run from the project root:
    python tools/longfu88/make_bonus_sg_variants.py
    python -m textgen variants input/variants/longfu88-bonus-sg.json --force

Size groups of the competitors (python -m textgen tiers longfu88-bonus-sg --texts 12):
    small   657   -> target 657,  limit 788      4 variants: v01-v04, the most important blocks, 3 entities and 1 connection per block
    medium  2544  -> target 2544, limit 3053     6 variants: v05-v10, the base ТЗ with another set of topics, order, headings, formats, depth
    large   2634  -> limit 2634 (x1.0)           2 variants: v11-v12, almost every topic of the pool, shallow, H3 details (may be shorter than the limit)
Topic pool = the 22 blocks of the base ТЗ + 7 extra topics (N1 glossary, N2 cashing out bonus winnings, N3 validity by offer, N4 wagering
compared, N5 ledger of all offers, N6 Bonus Crab, N7 sports extras). Codes of the base topics: B01 intro, OV overview, WB welcome bonus,
CL claim steps, TM terms, PC promo code, MD minimum deposits, RL reload, FS free spins, CR crypto, LV live casino, SE seasonal, CB cashback,
RB rebates, VP VIP program, RW rewards area, SP sports, VF verification, RG responsible use, MB mobile, CK checklist, FQ FAQ.
Every tracked keyword is used at least once per text; the five single keywords and "Longfu88 bonus" are placed in a heading or in a body
(per variant); "Longfu88" is counted by the code over bodies and headings."""
import json
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_bonus_sg_base import (B13_LIVE, B13_TAIL, B13_VIP, G, L, LEGAL, NO_CODE, NO_INVENT, OFFER_NAMES, P, S, V, W, mdrefs, rrefs,  # noqa: E402
                                srefs)

K0, KB, KBO, KW, KC, KO, KP = ("Longfu88", "Longfu bonus", "Longfu88 bonus", "Longfu88 welcome bonus", "Longfu88 promo code", "Longfu88 offers", "Longfu88 promotions")

VOICE_TAIL = (" All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore. "
              'Never write "Longfu88 bonuses", "Longfu bonuses" or "Longfu88 promo codes": such forms count as tracked keywords.')
PTR_VIP = "Say in one clause that the VIP program section below describes the reward levels."

PL = ["paragraph", "list"]
PT = ["paragraph", "table"]
PP = ["paragraph"]

# ---------------------------------------------------------------- generic block helpers


def blk(topic, ids, level, heading, words, kw=None, fmt=None, edit=None, extra=None, summary=None, **more):
    b = {"topic": topic, "from": ids, "level": level, "heading": heading, "words": words, "kw": kw or {}}
    if fmt:
        b["formats"] = fmt
    if edit:
        b["edit"] = [list(e) for e in edit]
    if extra:
        b["extra"] = extra
    if summary:
        b["summary"] = summary
    b.update(more)
    return b


def intro(heading, words, kw, extra=None):
    return blk("B01", ["b01"], 1, heading, words, kw, extra=extra)


def new(topic, level, heading, words, refs, ents, conns, summary, notes, covers, fmt, kw=None, **more):
    return blk(topic, [], level, heading, words, kw or {}, fmt, summary=summary, entities=ents, connections=conns, kb_refs=refs, notes=notes,
               covers_clusters=covers, **more)


# ---------------------------------------------------------------- FAQ
FAQ = {
    "mindep": ("what is the minimum first deposit for the welcome bonus (€50)", [f"{W}.minimum_deposit"]),
    "one": ("how many promotional bonuses can be active at once (one)", [f"{W}.important_terms[2]"]),
    "valid": ("how long the welcome bonus is valid (10 days from activation)", [f"{W}.validity"]),
    "cb": ("how the weekly cashback is claimed (opt in for a four-week cycle, then activate the credited cashback in My Bonuses)", [f"{P}[9].opt_in", f"{P}[9].crediting"]),
    "support": ("where to turn with a bonus question (customer support: live chat 24/7 or e-mail; do not print the e-mail address)", ["brandinfo_general.customer_support.channels"]),
    "code": ("whether a promo code is needed (the Brand Information lists none; the offers are activated in My Bonuses)", [f"{W}.claiming_procedure[2]"]),
    "excl": ("which payment methods are excluded from the welcome bonus (Neteller and Skrill)", [f"{W}.important_terms[0]"]),
    "wd": ("what happens if a withdrawal is requested before claiming or while a bonus is active (the promotional eligibility can be voided)", [f"{W}.important_terms[3]"]),
    "ver": ("whether verification can be required for bonus winnings (yes, before the promotional winnings are paid)", [f"{W}.important_terms[5]"]),
    "live": ("whether live casino has its own welcome offer (yes: the Live Casino Welcome Bonus, 125% up to €888)", [f"{P}[0].name", f"{P}[0].reward"]),
    "crypto": ("whether crypto deposits have a welcome offer (yes: the Casino Crypto Welcome Bonus, 188% up to 2,888 USDT)", [f"{P}[1].name", f"{P}[1].reward"]),
    "fs": ("how many Free Spins the welcome bonus includes (18)", [f"{W}.free_spins"]),
    "sport": ("whether sports bets have their own bonuses (yes: the sportsbook lists them separately, for example the Sport First Deposit Bonus of 100% up to €1,888)", [f"{S}[0].name", f"{S}[0].reward"]),
    "reload": ("how often the reload offers can be claimed (one claim per promotional period unless otherwise stated)", [f"{P}[4].important_terms[0]"]),
    "age": ("what the minimum age is (18)", ["brandinfo_general.minimum_age"]),
    "cap": ("how much the weekly cashback can return (up to 10% of weekly net casino losses, capped at €6,988)", [f"{P}[9].reward"]),
    "coin": ("what the Coin Shop gives (reward items and bonus credits up to €4,500)", [f"{G}[4].rewards[0]"]),
    "vip": ("how VIP points work (they are earned through eligible real-money gameplay and unlock numbered reward levels)", [f"{L}.progression"]),
    "crab": ("what Bonus Crab does (the player claims qualifying picks to open a crab reward and reveal a casino prize)", [f"{G}[0].mechanics"]),
    "cashout": ("how much of the welcome bonus can be cashed out (up to 5x the initial bonus amount)", [f"{W}.maximum_cashout"]),
    "maxbet": ("what the maximum bet is while the welcome bonus is wagered (€22.5 per spin)", [f"{W}.maximum_bet"]),
    "rebate": ("when the unlimited rebates are credited (daily to the rewards balance)", [f"{P}[11].crediting"]),
    "odds": ("which odds a sports bet needs to qualify (single bets at least 2.00, each accumulator selection at least 1.50)", [f"{S}[0].important_terms[1]"]),
    "dep": ("whether a deposit is needed for the welcome bonus (yes, a first qualifying deposit of at least €50; the Brand Information lists no bonus without a deposit)",
            [f"{W}.minimum_deposit", f"{W}.eligibility"]),
}
BASE_FAQ_REFS = [f"{W}.minimum_deposit", f"{W}.validity", f"{W}.important_terms[2]", f"{P}[9].opt_in", "brandinfo_general.customer_support.channels",
                 f"{W}.claiming_procedure[2]", f"{W}.important_terms[0]"]


def faq(keys, heading, words, kw, extra=None):
    n = len(keys)
    qs = "; ".join(f"({i}) {FAQ[k][0]}" for i, k in enumerate(keys, 1))
    notes = (f'A bulleted list of {n} items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required here for the question text only. '
             f"Questions, in this order: {qs}. Answers repeat the facts of the sections above in other words and add nothing new. {NO_INVENT}")
    need = list(dict.fromkeys(r for k in keys for r in FAQ[k][1]))
    return blk("FQ", ["b22"], 2, heading, words, kw, extra=extra, notes=notes, kw_lists_ok=True,
               refs_add=[r for r in need if r not in BASE_FAQ_REFS], refs_drop=[r for r in BASE_FAQ_REFS if r not in need],
               summary=f"{n} short questions and answers on the bonuses of the casino.")


# ---------------------------------------------------------------- topic builders: one function per base topic, with depth modes


def ov(heading, words, kw, mode="list", extra=None):
    if mode == "list":
        return blk("OV", ["b02"], 2, heading, words, kw, extra=extra)
    if mode == "short":
        return blk("OV", ["b02"], 2, heading, words, kw, PP, extra=extra, refs_drop=[f"{S}[0].name", f"{G}[0].name"],
                   summary="The offer families in two or three sentences: welcome offers, reloads, cashback and rebates, plus sports bonuses and a rewards area.",
                   notes=("Two or three sentences, no list: the bonuses fall into welcome offers (Casino Welcome Bonus, Live Casino Welcome Bonus, Casino Crypto Welcome Bonus), reload offers (Casino Weekend Reload, Casino Weekly Reload), "
                          "cashback and rebates (Casino Weekly Cashback, Live Casino Cashback, Unlimited Casino Rebate), plus sports bonuses and a rewards area (named without details). Use the names exactly as given; no amounts. "
                          f"One clause says that every offer has its own terms and is activated in My Bonuses. {NO_INVENT}"))
    # table: offer | type
    rows = ["Casino Welcome Bonus (First deposit casino bonus)", "Live Casino Welcome Bonus (Live casino welcome)", "Casino Crypto Welcome Bonus (Crypto casino welcome)",
            "Casino Weekly Reload (Weekly free spins)", "Casino Weekend Reload (Weekend deposit bonus)", "Casino Weekly Cashback (Casino cashback)",
            "Live Casino Cashback (Live casino cashback)", "Unlimited Casino Rebate (Rebate)"]
    return blk("OV", ["b02"], 2, heading, words, kw, PT, extra=extra, refs_drop=[f"{S}[0].name", f"{G}[0].name"],
               refs_add=[f"{W}.type", f"{P}[0].type", f"{P}[1].type", f"{P}[2].type", f"{P}[4].type", f"{P}[9].type", f"{P}[10].type", f"{P}[11].type"],
               summary="A two-column table that names every casino offer with its type.",
               notes=("One lead-in sentence that says that the offers fall into families, then a TABLE with two columns, offer | type, and eight rows in this order (name, then the type exactly as in the Brand Information in brackets here): "
                      + "; ".join(rows) + f". One closing sentence: every offer is activated in My Bonuses. No amounts here. {NO_INVENT}"))


def wb(heading, words, kw, mode="base", level=2, extra=None):
    if mode == "base":
        return blk("WB", ["b03"], level, heading, words, kw, extra=extra)
    if mode == "short":
        return blk("WB", ["b03"], level, heading, words, kw, PP, extra=extra,
                   refs_drop=[f"{P}[0].name", f"{P}[0].reward", f"{P}[1].name", f"{P}[1].reward", f"{P}[1].important_terms[2]"],
                   summary="The Casino Welcome Bonus of 188% up to €2,088 plus 18 Free Spins for a first deposit of €50, in two or three sentences.",
                   notes=("Two or three sentences about the Casino Welcome Bonus only: a first-deposit casino bonus of 188% up to €2,088 plus 18 Free Spins; the minimum first deposit of the bonus is €50 (use the €50 of the bonus, do NOT mention "
                          "the general minimum deposit of €10); it is for new registered players on the first qualifying deposit, one welcome offer per account. Do not name the other welcome offers and give no wagering numbers. "
                          f"{NO_INVENT}"))
    # cmp: the three welcome offers side by side
    return blk("WB", ["b03"], level, heading, words, kw, PT, extra=extra,
               refs_add=[f"{P}[0].minimum_deposit", f"{P}[0].validity", f"{P}[1].minimum_deposit", f"{P}[1].validity"], refs_drop=[f"{P}[1].important_terms[2]"],
               summary="The three welcome offers side by side: the Casino Welcome Bonus, the Live Casino Welcome Bonus and the Casino Crypto Welcome Bonus with reward, minimum deposit and validity.",
               notes=("Lead-in of two sentences: the Casino Welcome Bonus is the main offer, a first-deposit casino bonus of 188% up to €2,088 plus 18 Free Spins for new registered players on the first qualifying deposit, one welcome offer per account; "
                      "the Casino Welcome Bonus and the Casino Crypto Welcome Bonus are alternative first-deposit offers. Then a TABLE with four columns, offer | reward | minimum deposit | validity, and three rows in this order: Casino Welcome Bonus "
                      "(188% up to €2,088 + 18 Free Spins | €50 | 10 days from activation), Live Casino Welcome Bonus (125% up to €888 | €30 | 7 days), Casino Crypto Welcome Bonus (188% up to 2,888 USDT | 50 USDT | 10 days). "
                      f"Use the €50 of the bonus, do NOT mention the general minimum deposit of €10. No wagering numbers here (the terms section gives them). {NO_INVENT}"))


def cl(heading, words, kw, mode="base", extra=None, level=2):
    if mode == "base":
        return blk("CL", ["b04"], level, heading, words, kw, extra=extra)
    return blk("CL", ["b04"], level, heading, words, kw, PP, extra=extra,
               summary="The path from registration to completed wagering in three sentences, with the activation in My Bonuses before the first wager and the validity of 10 days.",
               notes=("Three or four sentences, no list: the player registers and completes the required personal details, makes the first qualifying deposit, activates the Casino Welcome Bonus in My Bonuses before placing any wager and "
                      "completes the wagering on eligible casino games before expiry; the offer is valid for 10 days from activation. Do not copy a step that contains the brand name. "
                      f"{NO_INVENT}"))


def tm(heading, words, kw, mode="base", extra=None, level=2):
    if mode == "base":
        return blk("TM", ["b05"], level, heading, words, kw, extra=extra)
    if mode == "short":
        return blk("TM", ["b05"], level, heading, words, kw, PP, extra=extra,
                   refs_drop=[f"{W}.important_terms[0]", f"{W}.important_terms[2]", f"{W}.important_terms[3]", f"{W}.important_terms[4]"],
                   summary="The main terms of the Casino Welcome Bonus in three sentences: wagering, validity, maximum bet and maximum cashout.",
                   notes=("Three sentences, no table: wagering 25x the deposit plus bonus amount and 40x Free Spins winnings; validity 10 days from activation; maximum bet €22.5 per spin and maximum cashout 5x the initial bonus amount. "
                          f"These terms belong to the Casino Welcome Bonus: say so. {NO_INVENT}"))
    return blk("TM", ["b05"], level, heading, words, kw, ["paragraph", "table", "list"], extra=extra,
               refs_add=[f"{W}.important_terms[1]", f"{W}.important_terms[5]"],
               summary="The terms of the Casino Welcome Bonus in a table and the six rules of the Brand Information that can cost the bonus or delay the payment.",
               notes=("A TABLE with two columns, term | value, and five rows in this order: wagering (25x the deposit plus bonus amount), Free Spins wagering (40x Free Spins winnings), validity (10 days from activation), maximum bet "
                      "(€22.5 per spin), maximum cashout (5x the initial bonus amount). After the table a bulleted list of the six rules of the Brand Information in their order: Neteller and Skrill deposits are excluded; Free Spins winnings have "
                      "separate wagering requirements; only one promotional bonus may be active at a time; a withdrawal request before claiming or while the bonus is active can void the promotional eligibility; cancelling the promotion forfeits "
                      "bonus funds and unconverted promotional winnings; account verification may be required before payment of promotional winnings. Each rule one clause. "
                      f"These terms belong to the Casino Welcome Bonus: say so. {NO_INVENT}"))


def pc(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("PC", ["b06"], 2, heading, words, kw, extra=extra)
    return blk("PC", ["b06"], 2, heading, words, kw, PP, extra=extra, refs_drop=[f"{P}[2].claiming_method"],
               summary="The Brand Information lists no promo code; the Casino Welcome Bonus is activated in My Bonuses.",
               notes=("Answer the question in 2 sentences: the Brand Information of the casino lists no promo code for its offers, and the Casino Welcome Bonus is activated in My Bonuses before the first wager. "
                      f"Do NOT claim that codes never exist and do not mention coupons or codes of other sites. {NO_CODE} {NO_INVENT}"))


def md(heading, words, kw, idx=(-1, 0, 1, 2, 3, 4, 5, 6, 7), extra=None):
    base_idx = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
    drop = mdrefs([i for i in base_idx if i not in idx])
    return blk("MD", ["b07"], 2, heading, words, kw, PT, extra=extra, refs_drop=drop,
               summary=f"The minimum deposit that {len(idx)} listed offers ask for, offer by offer, and the payment methods excluded from the welcome offers.",
               notes=("One lead-in sentence that says that the minimum deposit depends on the offer, then a TABLE with two columns, offer | minimum deposit, and one row per offer in this order: "
                      + ", ".join(OFFER_NAMES[i] for i in idx) + " (names and values exactly as in the Brand Information; crypto offers in USDT). "
                      "One closing sentence: Neteller and Skrill deposits are excluded from the Casino Welcome Bonus; the general minimum deposit of the casino is not the minimum of an offer, so the player checks the offer first. "
                      f"Do NOT state the general minimum deposit amount and do not list payment methods. {NO_INVENT}"))


def rl(heading, words, kw, rows=(3, 4, 5, 6), extra=None, level=2):
    base_rows = [3, 4, 5, 6]
    drop = rrefs(*[i for i in base_rows if i not in rows])
    if 4 not in rows:
        drop += [f"{P}[4].important_terms[2]", f"{P}[4].important_terms[1]", f"{P}[4].validity"]
    if 6 not in rows:
        drop += [f"{P}[6].validity"]
    tail = []
    if any(i in rows for i in (3, 4, 5)):
        tail.append("the weekly and weekend offers are valid for 7 days")
    if 6 in rows:
        tail.append("the Double Fortune special for 24 hours")
    return blk("RL", ["b08"], level, heading, words, kw, PT, extra=extra, refs_drop=drop,
               summary=f"{len(rows)} reload offers with reward, minimum deposit and wagering.",
               notes=("One lead-in sentence that says that the reload offers reward repeat deposits, then a TABLE with four columns, offer | reward | minimum deposit | wagering, and "
                      f"{len(rows)} rows in this order: " + ", ".join(OFFER_NAMES[i] for i in rows) + " (values exactly as in the Brand Information). After the table two sentences: "
                      + "; ".join(tail) + "; the stake while wagering bonus funds is limited to €5 per spin, and a reload cannot be combined with another active casino bonus. "
                      f"The Casino Weekly Reload (50 Free Spins) belongs to the free spins topic: do not describe it here. {NO_INVENT}"))


def fs(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("FS", ["b09"], 2, heading, words, kw, extra=extra)
    return blk("FS", ["b09"], 2, heading, words, kw, PP, extra=extra,
               refs_drop=[f"{P}[7].name", f"{P}[7].reward", f"{P}[7].minimum_deposit", f"{P}[7].wagering_requirement"],
               summary="The 50 Free Spins of the Casino Weekly Reload and the 40x wagering on the winnings.",
               notes=("Two or three sentences: the Casino Weekly Reload gives 50 Free Spins for a minimum deposit of €30, valid 7 days, with 40x wagering on the winnings from Free Spins; one clause recalls that the welcome bonus adds 18 Free Spins "
                      f"with 40x Free Spins winnings. No game names, no spin value. {NO_INVENT}"))


def cr(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("CR", ["b10"], 2, heading, words, kw, extra=extra)
    if mode == "short":
        return blk("CR", ["b10"], 2, heading, words, kw, PP, extra=extra, refs_drop=rrefs(3, 5),
                   summary="The Casino Crypto Welcome Bonus of 188% up to 2,888 USDT and the eligible coins.",
                   notes=("Three sentences: the Casino Crypto Welcome Bonus is 188% up to 2,888 USDT for a first qualifying crypto deposit of at least 50 USDT, wagering 40x deposit plus bonus, valid 10 days, maximum bonus wager 5 USDT per spin; "
                          "the eligible cryptocurrencies are USDT, BTC, BCH, LTC, ETH, XRP and USDC; the Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers. "
                          f"{NO_INVENT}"))
    return blk("CR", ["b10"], 2, heading, words, kw, PT, extra=extra,
               refs_add=[f"{P}[1].eligibility", f"{P}[1].claiming_method", f"{P}[3].validity", f"{P}[3].important_terms[0]", f"{P}[3].important_terms[2]", f"{P}[5].validity"],
               summary="The crypto offers in full: the Casino Crypto Welcome Bonus, the weekly and weekend crypto reloads with their terms and the eligible coins.",
               notes=("Lead with the Casino Crypto Welcome Bonus: 188% up to 2,888 USDT for a first qualifying crypto deposit of at least 50 USDT, wagering 40x deposit plus bonus, valid 10 days, maximum bonus wager 5 USDT per spin; it is activated in My Bonuses "
                      "after the eligibility and deposit conditions are met. Then a TABLE with four columns, offer | reward | minimum deposit | wagering, and two rows: Casino Weekly Crypto Reload, Casino Weekend Crypto Reload (values exactly as in the Brand Information). "
                      "After the table two sentences: both reloads are valid for 7 days, allow one claim per promotional period and cannot be combined with another active casino bonus; the stake while wagering bonus funds is limited to €5 per spin. "
                      "Then one sentence with the eligible cryptocurrencies as given (USDT, BTC, BCH, LTC, ETH, XRP, USDC). The Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers: say so once. "
                      f"{NO_INVENT}"))


def lv(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("LV", ["b11"], 2, heading, words, kw, extra=extra)
    if mode == "short":
        return blk("LV", ["b11"], 2, heading, words, kw, PP, extra=extra,
                   refs_drop=[f"{P}[10].name", f"{P}[10].reward", f"{P}[10].wagering_requirement", f"{P}[12].name", f"{P}[12].rebate_percentage"],
                   summary="The Live Casino Welcome Bonus: 125% up to €888.",
                   notes=("Two or three sentences about the Live Casino Welcome Bonus only: 125% up to €888, minimum deposit €30, wagering 30x the deposit plus bonus, valid 7 days, maximum bet €25, for new players on the first qualifying deposit. "
                          f"No game names. {NO_INVENT}"))
    return blk("LV", ["b11"], 2, heading, words, kw, PP, extra=extra,
               refs_add=[f"{P}[0].eligibility", f"{P}[0].claiming_method", f"{P}[0].important_terms[0]", f"{P}[0].important_terms[3]", f"{P}[10].calculation_period",
                         f"{P}[10].crediting", f"{P}[10].important_terms[0]", f"{P}[12].crediting"],
               summary="The live casino offers in full: the Live Casino Welcome Bonus, the Live Casino Cashback with its calculation period and the Unlimited Live Casino Rebate.",
               notes=("Lead with the Live Casino Welcome Bonus: 125% up to €888, minimum deposit €30, wagering 30x the deposit plus bonus, valid 7 days, maximum bet €25, for new players on the first qualifying deposit; it must be activated before wagering and "
                      "cannot be combined with another active bonus. Then the Live Casino Cashback in two sentences (25% up to €850, calculated Monday 00:00 UTC through Sunday 23:59 UTC on real-money stakes less winnings in eligible Live Casino games, "
                      "credited to My Bonuses on Monday with opt-in and activation required, wagering 10x the credited cashback) and the Unlimited Live Casino Rebate in one sentence (1.0%, credited daily). "
                      f"No game names. {NO_INVENT}"))


def se(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("SE", ["b12"], 2, heading, words, kw, extra=extra)
    return blk("SE", ["b12"], 2, heading, words, kw, PP, extra=extra, refs_drop=rrefs(8) + [f"{P}[8].eligibility", f"{P}[8].important_terms[2]"],
               summary="The seasonal Trick or Treat Pumpkin Bonanza with up to 100 Free Spins.",
               notes=("Say first that campaigns come and go, so the list may change: the player checks the promotions page of the casino. Then the Casino Trick or Treat Pumpkin Bonanza: up to 100 Free Spins, minimum deposit €20, "
                      "wagering 40x Free Spins winnings, valid 7 days, a €5 per spin maximum stake while wagering bonus funds, not combinable with another active casino bonus. "
                      f"Do not claim that the campaign is running now. {NO_INVENT}"))


def cb(heading, words, kw, mode="vip", extra=None):
    if mode == "vip":
        return blk("CB", ["b13"], 2, heading, words, kw, extra=extra)
    if mode == "novip":  # weekly + live cashback, no VIP table, no pointer to the VIP section
        return blk("CB", ["b13"], 2, heading, words, kw, PP, extra=extra, refs_drop=[f"{P}[9].cashback_by_vip"],
                   edit=[(B13_VIP, ""), (PTR_VIP, "")],
                   summary="Cashback: the Casino Weekly Cashback of up to 10% of weekly net losses capped at €6,988 and the Live Casino Cashback of 25% up to €850.")
    if mode == "short":
        return blk("CB", ["b13"], 2, heading, words, kw, PP, extra=extra, refs_drop=[f"{P}[9].cashback_by_vip", f"{P}[10].reward", f"{P}[10].wagering_requirement"],
                   edit=[(B13_LIVE, ""), (B13_VIP, ""), (PTR_VIP, "")],
                   summary="The Casino Weekly Cashback of up to 10% of weekly net losses, capped at €6,988, with its opt-in and wagering.")
    # deep: weekly + live cashback with crediting and the VIP table
    return blk("CB", ["b13"], 2, heading, words, kw, PT, extra=extra,
               refs_add=[f"{P}[9].crediting", f"{P}[9].important_terms[1]", f"{P}[10].calculation_period", f"{P}[10].crediting", f"{P}[10].important_terms[0]"],
               summary="Cashback in full: the Casino Weekly Cashback with its rates by VIP level, the crediting and the claim window, and the Live Casino Cashback.",
               edit=[(B13_TAIL, B13_TAIL + "State that the weekly cashback is credited to My Bonuses on Monday, that activation is required and that it expires if it is not activated within its claim window; "
                                           "the Live Casino Cashback is credited on Monday too and rests on real-money stakes less winnings in eligible Live Casino games. ")])


def rb(heading, words, kw, mode="base", level=2, extra=None):
    if mode == "base":
        return blk("RB", ["b14"], level, heading, words, kw, extra=extra)
    return blk("RB", ["b14"], level, heading, words, kw, PP, extra=extra, refs_drop=[f"{P}[13].name", f"{P}[13].rebate_percentage", f"{P}[14].name", f"{P}[14].rebate_percentage"],
               summary="The two main unlimited rebates: 0.9% on casino and 1.0% on live casino wagering, credited daily.",
               notes=("Two sentences: the Unlimited Casino Rebate returns 0.9% and the Unlimited Live Casino Rebate 1.0% of qualifying settled real-money wagering on the relevant game category; the rebate is credited daily to the rewards balance "
                      f"and carries 1x wagering on the credited rebate. {NO_INVENT}"))


def vp(heading, words, kw, mode="base", extra=None):
    all_idx = [0, 4, 9, 14, 24]
    drop_all = [f"{L}.levels[{i}].{f}" for i in all_idx for f in ("level", "points_required", "level_reward")]
    if mode == "short":
        return blk("VP", ["b15"], 2, heading, words, kw, PP, extra=extra, refs_drop=drop_all + [f"{L}.additional_benefits"],
                   summary="The VIP program in three sentences: five tiers, VIP points from real-money play and numbered reward levels.",
                   notes=("Three sentences, no table: the VIP program has five tiers (Bronze, Silver, Gold, Platinum, Diamond); the player earns VIP points through eligible real-money gameplay and the points unlock numbered reward levels; "
                          "reward and withdrawal limits may differ by level and currency, and level-based benefits can change under the program rules. "
                          f'Call it "the VIP Program" without the brand name. {NO_INVENT}'))
    if mode == "base":
        return blk("VP", ["b15"], 2, heading, words, kw, extra=extra)
    deep = [0, 2, 4, 7, 9, 14, 19, 24]
    return blk("VP", ["b15"], 2, heading, words, kw, PT, extra=extra, refs_drop=drop_all,
               refs_add=[f"{L}.levels[{i}].{f}" for i in deep for f in ("level", "points_required", "level_reward")],
               summary="The VIP program in depth: the tiers, the points, eight of the 25 reward levels with points and reward, and the additional benefits.",
               notes=("One or two sentences: the VIP program has five tiers (Bronze, Silver, Gold, Platinum, Diamond) and the player earns VIP points through eligible real-money gameplay, which unlock numbered reward levels. Then a TABLE with three columns, "
                      "level | points required | level reward, and eight rows for levels 1, 3, 5, 8, 10, 15, 20 and 25 (values exactly as in the Brand Information; say in one clause that there are 25 levels in all). Then one sentence with the "
                      "additional benefits (personalised offers, VIP cashback, higher withdrawal limits, a personal VIP manager for eligible high tiers) and one sentence that reward and withdrawal limits may differ by level and currency and that "
                      f'level-based benefits can change under the program rules. Call it "the VIP Program" without the brand name. Do not give the cashback percentages of the 25 levels and do not link the tiers to the numbered levels. {NO_INVENT}'))


def rw(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("RW", ["b16"], 2, heading, words, kw, extra=extra)
    if mode == "short":
        return blk("RW", ["b16"], 2, heading, words, kw, PP, extra=extra, refs_drop=[f"{G}[0].mechanics", f"{G}[1].mechanics", f"{G}[4].rewards[0]"],
                   summary="The rewards area in two sentences: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop.",
                   notes=("Two sentences, no list: the rewards area adds Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop to the bonuses; Coins are earned through qualifying activity and exchanged in the Coin Shop. "
                          f"Names exactly as given. {NO_INVENT}"))
    return blk("RW", ["b16"], 2, heading, words, kw, PL, extra=extra,
               refs_add=[f"{G}[0].access", f"{G}[0].validity", f"{G}[1].rewards", f"{G}[1].validity", f"{G}[2].access", f"{G}[3].access", f"{G}[4].access", f"{G}[4].important_terms[1]"],
               summary="The rewards area in depth: where each feature sits in the Rewards menu, what it gives and the wagering that some rewards carry.",
               notes=("One lead-in sentence that says that the rewards area adds game-like features to the bonuses, then a bulleted list of five items \"name: what it does and where it is\": Bonus Crab (claim qualifying picks to open a crab reward; "
                      "valid 7 days after the reward is assigned), Wheel of Fortune (spend an eligible spin or Coins to rotate a prize wheel; bonus credits, Free Spins or Coins; valid 7 days), Challenges (complete qualifying gambling tasks to unlock listed rewards; "
                      "found under Rewards > Challenges), Collections (collect campaign items by completing qualifying activity; Rewards > Collections), Coin Shop (exchange earned Coins for reward items and bonus credits up to €4,500; Rewards > Shop). "
                      "After the list one sentence: rewards may carry separate wagering requirements. Each list item one or two short clauses. "
                      f"{NO_INVENT}"))


def sp(heading, words, kw, mode="base", extra=None, level=2):
    if mode == "short":
        keep = [0]
        return blk("SP", ["b17"], level, heading, words, kw, PP, extra=extra,
                   refs_drop=srefs([1, 2, 3]) + [f"{S}[0].important_terms[2]", f"{S}[7].name", f"{S}[7].reward", f"{S}[9].name", f"{S}[9].reward"],
                   summary="The Sport First Deposit Bonus of 100% up to €1,888 with its 8x wagering and the odds rule.",
                   notes=("Three sentences, no table: the sportsbook has its own bonuses, for example the Sport First Deposit Bonus of 100% up to €1,888 (minimum deposit €50, wagering 8x deposit plus bonus, valid 30 days); "
                          "only settled qualifying sports bets count toward the wagering; single bets need odds of at least 2.00 and each accumulator selection at least 1.50. No sports tips, no odds of events. "
                          f"{NO_INVENT}"))
    if mode == "base":
        return blk("SP", ["b17"], level, heading, words, kw, extra=extra)
    if mode == "table3":
        return blk("SP", ["b17"], level, heading, words, kw, PT, extra=extra, refs_drop=srefs([1]) + [f"{S}[7].name", f"{S}[7].reward"],
                   summary="The sports bonuses in short: first deposit and reload offers with a low 8x wagering, the odds required for qualifying bets and the Parlay Boost.",
                   notes=("One lead-in sentence that says that the sportsbook has its own bonuses, then a TABLE with four columns, offer | reward | minimum deposit | wagering, and three rows in this order: Sport First Deposit Bonus, "
                          "Sport Weekly Reload Bonus, Sport Weekend Reload Bonus (values exactly as in the Brand Information). After the table two sentences: only settled qualifying sports bets count toward the wagering, single bets need odds of at least 2.00 and each "
                          "accumulator selection at least 1.50, voided and cashed-out bets do not qualify; the offers are valid for 30 days. One closing sentence names the Parlay Boost: up to 100% extra winnings on qualifying accumulators. "
                          f"No sports tips, no odds of events. {NO_INVENT}"))
    rows = [0, 1, 2, 3, 4, 5]
    return blk("SP", ["b17"], level, heading, words, kw, PT, extra=extra, refs_add=srefs([4, 5]),
               summary="The sports bonuses in depth: six first deposit, welcome and reload offers with a low 8x wagering, the odds required for qualifying bets, the Sports Cashback and the Parlay Boost.",
               notes=("One lead-in sentence that says that the sportsbook has its own bonuses, then a TABLE with four columns, offer | reward | minimum deposit | wagering, and six rows in this order: "
                      + ", ".join(["Sport First Deposit Bonus", "Sport Crypto Welcome Bonus", "Sport Weekly Reload Bonus", "Sport Weekend Reload Bonus", "Sport Crypto Weekly Reload", "Sport Crypto Weekend Reload"])
                      + " (values exactly as in the Brand Information). After the table three sentences: only settled qualifying sports bets count toward the wagering, single bets need odds of at least 2.00 and each accumulator selection at least 1.50, "
                      "voided and cashed-out bets do not qualify; the offers are valid for 30 days; only one claim per stated promotional period. Then one sentence with the Sports Cashback (10% up to €2,500 of eligible sports net losses, weekly) and one "
                      f"with the Parlay Boost (up to 100% extra winnings on qualifying accumulators). No sports tips, no odds of events. {NO_INVENT}"))


def vf(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("VF", ["b18"], 2, heading, words, kw, extra=extra)
    return blk("VF", ["b18"], 2, heading, words, kw, PP, extra=extra, refs_drop=[f"{V}.documents"],
               summary="Verification can be required before promotional winnings are paid: the submission window of 30 days and the review time of up to 10 days.",
               notes=("Three sentences: account verification may be required before promotional winnings are paid; a withdrawal request before claiming a bonus or while it is active can void the promotional eligibility; "
                      "the documents are requested when needed, with a submission window of up to 30 days and a review time of up to 10 days after a complete document set is received. No list of documents, no promise of speed. "
                      f"{NO_INVENT}"))


def rg(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("RG", ["b19"], 2, heading, words, kw, extra=extra)
    return blk("RG", ["b19"], 2, heading, words, kw, PP, extra=extra,
               refs_drop=["brandinfo_responsible_gaming.responsible_gaming.self_assessment", f"{W}.important_terms[4]"],
               summary="Bonuses are for players of 18 or over who gamble where it is lawful; read the terms first and use the support organisations.",
               notes=("Two or three sentences: the bonuses are for players aged 18 or over who gamble only where it is lawful; the terms of an offer (wagering, maximum bet, validity) should be read before accepting it; "
                      f"the support organisations of the casino are GamCare, Gamblers Anonymous and Gambling Therapy. No advice to chase losses, no promise. {LEGAL} {NO_INVENT}"))


def ck(heading, words, kw, mode="base", extra=None):
    if mode == "base":
        return blk("CK", ["b21"], 2, heading, words, kw, extra=extra)
    return blk("CK", ["b21"], 2, heading, words, kw, PL, extra=extra,
               refs_drop=[f"{W}.important_terms[3]", f"{W}.important_terms[5]", f"{W}.claiming_procedure[2]"],
               summary="Four checks before claiming the Casino Welcome Bonus: new player, first deposit of €50, Neteller and Skrill excluded, one active bonus.",
               notes=("The competitors close with a verdict; this block gives a neutral checklist and no recommendation. One lead-in sentence, then a bulleted list of four short checks in this order: the player is a new registered player (one welcome offer per account); "
                      "the first qualifying deposit is at least €50; the deposit is not made with Neteller or Skrill; no other promotional bonus is active. Each item one clause of up to 14 words. No verdict, no rating, no advice to take an offer. "
                      f"{NO_INVENT}"))


def mb(heading, words, kw, extra=None):
    return blk("MB", ["b20"], 2, heading, words, kw, extra=extra)


# ---------------------------------------------------------------- new topics (not in the base ТЗ)


def n1_glossary(heading, words, kw=None, level=2):
    return new("N1", level, heading, words,
               [f"{W}.wagering_requirement", f"{W}.free_spins_wagering", f"{W}.maximum_bet", f"{W}.maximum_cashout", f"{W}.validity", f"{P}[9].opt_in", f"{P}[2].claiming_method"],
               [["Bonus Terms", 10], ["Wagering Requirement", 8], ["My Bonuses", 6]], [["Wagering Requirement", "multiplies", "the deposit plus bonus amount before a withdrawal", 8]],
               "A short glossary of the bonus terms: wagering requirement, Free Spins winnings, maximum bet, maximum cashout, validity, opt-in and My Bonuses, each with the value of the Casino Welcome Bonus where there is one.",
               "One lead-in sentence that says that the terms below explain the words that bonus rules use, then a TABLE with two columns, term | meaning, and seven rows in this order, each meaning one short clause with the value from the Brand Information: "
               "wagering requirement (how many times the stake base is played through: 25x the deposit plus bonus amount for the Casino Welcome Bonus); Free Spins winnings (wagered separately: 40x); maximum bet (the largest stake while wagering: €22.5 per spin); "
               "maximum cashout (the cap on what can be withdrawn from the bonus: 5x the initial bonus amount); validity (the period to complete the wagering: 10 days from activation); opt-in (joining the four-week cycle of the Casino Weekly Cashback); "
               f"My Bonuses (the place where offers are activated). Do not add terms that are not in the Brand Information. {NO_INVENT}", ["k04"], PT, kw)


def n2_cashout(heading, words, kw=None, level=2):
    return new("N2", level, heading, words,
               [f"{W}.maximum_cashout", f"{W}.important_terms[3]", f"{W}.important_terms[5]", "brandinfo_withdrawal.withdrawal_guide"],
               [["Bonus Winnings", 10], ["Maximum Cashout", 7], ["Withdrawal Request", 6]], [["Bonus Winnings", "are paid after", "the wagering is complete and any requested verification is done", 8]],
               "How bonus winnings reach the player: the wagering first, the cap of 5x the initial bonus amount, verification when requested and the six steps of the withdrawal.",
               "Two sentences first: bonus winnings can be withdrawn after the wagering is complete; the maximum cashout of the Casino Welcome Bonus is 5x the initial bonus amount; a withdrawal request before claiming or while the bonus is active can void the promotional eligibility, "
               "and verification may be required before promotional winnings are paid. Then a NUMBERED list with the six steps of the withdrawal guide of the Brand Information in their order (open the cashier; select Withdrawal and a supported method; enter the amount and the "
               "receiving bank, wallet or blockchain address; complete identity and payment-method verification if prompted; review and confirm; wait for casino processing and any bank or network settlement). Do not copy a step that contains the brand name: write \"the casino\" there. "
               f"No withdrawal limits, fees or processing times (they belong to the payments page). {NO_INVENT}", ["k17"], PL, kw)


def n3_validity(heading, words, kw=None, level=2):
    idx = [-1, 0, 1, 2, 4, 6]
    return new("N3", level, heading, words,
               [f"{(W if i == -1 else P + '[' + str(i) + ']')}.{f}" for i in idx for f in ("name", "validity")] + [f"{S}[0].name", f"{S}[0].validity"],
               [["Bonus Validity", 10], ["Expiry", 7]], [["Bonus Validity", "starts at", "the activation of the offer", 7]],
               "How long each offer stays valid: 10 days for the Casino Welcome Bonus, 7 days for most live, crypto and reload offers, 24 hours for the Double Fortune special and 30 days for the first sports deposit bonus.",
               "One lead-in sentence that says that every offer has its own validity and that it counts from the activation, then a TABLE with two columns, offer | validity, and seven rows in this order: "
               "Casino Welcome Bonus (10 days from activation), Live Casino Welcome Bonus (7 days), Casino Crypto Welcome Bonus (10 days), Casino Weekly Reload (7 days), Casino Weekend Reload (7 days), "
               "Casino Double Fortune: One-Day Reload Special (24 hours), Sport First Deposit Bonus (30 days). One closing sentence: the unused part of an offer is lost when the validity ends is NOT in the Brand Information, so say only that the player "
               f"completes the wagering inside the period. {NO_INVENT}", ["k18"], PT, kw)


def n4_wagering(heading, words, kw=None, level=2):
    refs = [f"{W}.name", f"{W}.wagering_requirement", f"{W}.free_spins_wagering"]
    for i in (0, 1, 2, 3, 4, 9, 11):
        refs += [f"{P}[{i}].name", f"{P}[{i}].wagering_requirement"] if i != 11 else [f"{P}[11].name", f"{P}[11].wagering_requirement"]
    refs += [f"{S}[0].name", f"{S}[0].wagering_requirement"]
    return new("N4", level, heading, words, refs,
               [["Wagering Requirement", 10], ["Bonus Offers", 6]], [["Wagering Requirement", "differs by", "offer and by bonus type", 8]],
               "The wagering of nine offers side by side, from 40x on crypto and Free Spins winnings down to 1x on rebates and 8x on the sports first deposit.",
               "One lead-in sentence that says that the wagering differs by offer, then a TABLE with two columns, offer | wagering, and nine rows in this order: Casino Welcome Bonus (25x the deposit plus bonus amount; 40x Free Spins winnings), "
               "Live Casino Welcome Bonus (30x the deposit plus bonus), Casino Crypto Welcome Bonus (40x deposit plus bonus), Casino Weekly Reload (40x winnings from Free Spins), Casino Weekly Crypto Reload (30x deposit plus bonus), "
               "Casino Weekend Reload (30x deposit plus bonus; 40x Free Spins winnings), Casino Weekly Cashback (10x cashback), Unlimited Casino Rebate (1x credited rebate), Sport First Deposit Bonus (8x deposit plus bonus). "
               f"One closing sentence: the base of the wagering differs (deposit plus bonus, winnings, credited cashback), so the player reads the line of the offer. {NO_INVENT}", ["k04"], PT, kw)


def n5_ledger(heading, words, kw=None, level=2):
    refs = [f"{W}.name", f"{W}.bonus_percentage", f"{W}.maximum_bonus", f"{W}.free_spins", f"{W}.minimum_deposit", f"{W}.wagering_requirement", f"{W}.validity"]
    for i in range(0, 8):
        refs += [f"{P}[{i}].name", f"{P}[{i}].reward", f"{P}[{i}].minimum_deposit", f"{P}[{i}].wagering_requirement", f"{P}[{i}].validity"]
    return new("N5", level, heading, words, refs,
               [["Bonus Offers", 10], ["Minimum Deposit", 7], ["Wagering Requirement", 7]], [["Bonus Offers", "differ in", "reward, minimum deposit, wagering and validity", 8]],
               "One table with nine casino offers: reward, minimum deposit, wagering and validity of each.",
               "One lead-in sentence, then a TABLE with five columns, offer | reward | minimum deposit | wagering | validity, and nine rows in this order: Casino Welcome Bonus (188% up to €2,088 + 18 Free Spins | €50 | 25x deposit plus bonus; 40x Free Spins winnings | 10 days), "
               + ", ".join(OFFER_NAMES[i] for i in range(0, 8)) + " (values exactly as in the Brand Information, crypto offers in USDT). The cell text stays as short as the Brand Information value. "
               f"One closing sentence: every offer is activated in My Bonuses and cannot be combined with another active casino bonus where the offer says so. {NO_INVENT}", ["k01", "k04"], PT, kw)


def n6_crab(heading, words, kw=None, level=3):
    return new("N6", level, heading, words,
               [f"{G}[0].mechanics", f"{G}[0].access", f"{G}[0].rewards", f"{G}[0].validity", f"{G}[0].wagering_requirement"],
               [["Bonus Crab", 10], ["Crab Reward", 7]], [["Bonus Crab", "awards", "bonus credits, Free Spins or Coins", 8]],
               "How Bonus Crab works: qualifying picks open a crab reward of bonus credits, Free Spins or Coins, valid 7 days with 30x and 40x wagering.",
               "Say first how the feature works: the player claims qualifying picks to open a crab reward and reveal a casino prize; free picks may come from qualifying activity in the rewards area. Then the rewards (bonus credits, Free Spins, Coins) "
               "as a bulleted list of three items, then one sentence with the validity (7 days after the reward is assigned) and one with the wagering (30x the awarded bonus credit; 40x the winnings from Free Spins). "
               f"No prize sizes, no odds. {NO_INVENT}", ["k09"], PL, kw)


def n7_sportsx(heading, words, kw=None, level=2):
    return new("N7", level, heading, words,
               [f"{S}[8].name", f"{S}[8].reward", f"{S}[8].important_terms[0]", f"{S}[9].name", f"{S}[9].reward", f"{S}[9].minimum_legs", f"{S}[9].wagering_requirement",
                f"{S}[10].name", f"{S}[10].reward", f"{S}[10].eligibility", f"{S}[10].wagering_requirement", f"{S}[10].validity"],
               [["Parlay Boost", 8], ["Early Payout", 7], ["Risk-Free Bet", 7]], [["Parlay Boost", "adds", "extra winnings to qualifying accumulators", 8]],
               "Three sports extras that are not deposit bonuses: the early payout when a team leads by two goals, the Parlay Boost on accumulators and the Bet Builder risk-free stake.",
               "One lead-in sentence that says that the sportsbook has extras apart from the deposit bonuses, then a bulleted list of three items: 2 Goals Ahead - Early Payout (early settlement of eligible football bets when the selected team leads by two goals; "
               "only participating pre-match match-winner markets qualify); Parlay Boost (up to 100% extra winnings on qualifying accumulators of at least 3 legs; no additional bonus wagering on settled enhanced winnings); "
               "Bet Builder Risk Free (50% risk-free stake return up to €250 on qualifying pre-match Bet Builder selections; wagering 1x the credited free-bet stake; valid 7 days). Each item one or two clauses. No tips, no odds of events. "
               f"{NO_INVENT}", ["k11"], PL, kw)


# ================================================================ the 12 variants
variants = []

# ------------------------------------------------------------------ SMALL (target 657, limit 788): the most important blocks only
variants.append({
    "id": "v01", "name": "Quick bonus guide (small, flat)", "tier": "small", "angle": "A player who wants the welcome offer, the terms and the promo code answer in a minute.",
    "skipped_clusters": [{"id": "k01", "reason": "left out of the short text; the offer families are named in the sections that follow"},
                         {"id": "k21", "reason": "a verdict or checklist is left out of the short text; the terms are in their own section"}],
    "intent_summary": ("Short brand-subpage for the small size group of the competitors: the Longfu88 welcome bonus with its claiming steps, the terms, the promo code question, the reload, free spin and cashback offers in the fewest words "
                       "for a player from Singapore. Page voice: short, dense paragraphs of two or three sentences, sentences of about 14 words, facts before comment, no scene-setting, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions: Quick Guide to Bonuses and Promo Code", 50, {K0: 2, KB: 1}),
        blk("WB", ["b03", "b04"], 2, "Longfu88 Welcome Bonus and How to Claim It", 115, {K0: 2}, PL,
            notes=("Lead with the Casino Welcome Bonus in two sentences: a first-deposit casino bonus of 188% up to €2,088 plus 18 Free Spins for new registered players, minimum first deposit €50 (use the €50 of the bonus, do NOT mention the general minimum "
                   "deposit of €10), one welcome offer per account. Then a NUMBERED list with the four steps of the claiming procedure in the order of the Brand Information (register an account and complete the required personal details; make the first "
                   "qualifying deposit; activate the Casino Welcome Bonus in My Bonuses before placing any wagers; play eligible casino games and complete the wagering before expiry). Do not copy a step that contains the brand name: write \"the casino\" there. "
                   f"One closing sentence gives the validity: 10 days from activation. {NO_INVENT}"),
            refs_drop=[f"{P}[0].name", f"{P}[0].reward", f"{P}[1].name", f"{P}[1].reward", f"{P}[1].important_terms[2]"],
            summary="The Casino Welcome Bonus of 188% up to €2,088 plus 18 Free Spins and the four steps to claim it."),
        tm("Longfu88 Bonus Terms in Brief", 80, {K0: 1}, "short"),
        pc("Promo Code: What to Know", 50, {K0: 1, KC: 1}, "short",
           extra='Where the phrase "Longfu88 promo code" is used it stands in the first sentence, which says that the Brand Information of the casino lists no Longfu88 promo code for its offers.'),
        rl("Weekly and Weekend Reloads", 95, {K0: 1}, rows=(4, 5, 6)),
        fs("Free Spins", 60, {K0: 1}, "short"),
        cb("Weekly Cashback", 80, {K0: 1}, "short"),
        faq(["mindep", "one", "valid", "support"], "Longfu88 Offers: Quick Answers", 85, {K0: 1}),
    ],
})

variants.append({
    "id": "v02", "name": "Deposit table and crypto (small)", "tier": "small", "angle": "A new player who compares what each offer asks for the first deposit and who pays in crypto.",
    "skipped_clusters": [{"id": "k01", "reason": "left out of the short text; the offers are named in the deposit table"},
                         {"id": "k03", "reason": "the claiming steps are left out of the short text; the activation in My Bonuses is named in the checks"},
                         {"id": "k06", "reason": "cashback is left out of the short text; the page keeps to the first deposit offers"}],
    "intent_summary": ("Short brand-subpage for the small size group: the Longfu88 welcome bonus first, the minimum deposit that each offer asks for in one table, the crypto welcome offer, the terms, the promo code answer and a short checklist, for a "
                       "player from Singapore. Page voice: practical and comparative, a one-line verdict after each section, sentences of about 15 words, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Welcome Bonus: Deposits, Crypto Offer and Terms", 50, {K0: 1, KB: 1, KP: 1},
              extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        wb("Casino Welcome Bonus in Short", 55, {K0: 2}, "short"),
        md("Minimum Deposit by Offer", 85, {K0: 1}, idx=(-1, 0, 1, 2, 4)),
        cr("Crypto Welcome Offer", 70, {K0: 1}, "short"),
        tm("Longfu88 Bonus Wagering and Limits", 80, {K0: 1}, "short"),
        pc("Longfu88 Promo Code: Is One Listed?", 45, {K0: 1}, "short"),
        vf("Verification Before Payout", 60, {K0: 1}, "short"),
        ck("Four Checks Before the First Deposit", 70, {K0: 1}, "short"),
        faq(["mindep", "excl", "crypto", "valid", "support"], "Longfu88 Offers: Welcome Questions", 90, {K0: 1}),
    ],
})

variants.append({
    "id": "v03", "name": "Casino cashback and sports (small)", "tier": "small", "angle": "A reader who bets on sports as well as plays casino and wants both cashback sets in a few lines.",
    "skipped_clusters": [{"id": "k03", "reason": "the claiming steps are left out of the short text; the activation in My Bonuses is named in the welcome section"},
                         {"id": "k05", "reason": "reload offers are left out of the short text; the page keeps to cashback, rebates and sports"},
                         {"id": "k21", "reason": "a checklist is left out of the short text; responsible use closes the page"}],
    "intent_summary": ("Short brand-subpage for the small size group: the Longfu88 bonus families in one paragraph, the welcome offer basics, the sports bonuses with the odds rule, the weekly cashback with its VIP rates, the daily rebates and responsible use, "
                       "for a player from Singapore. Page voice: terse and scannable, a one-sentence lead-in per section, then a list or a table; sentences of about 12 words; no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions: Casino Cashback and Sports Bonuses in Brief", 50, {K0: 1, KB: 1}),
        ov("Longfu88 Bonus Types in One Paragraph", 55, {K0: 1}, "short"),
        wb("Welcome Offer Basics", 55, {K0: 1, KW: 1}, "short", extra='Where the phrase "Longfu88 welcome bonus" is used it stands in the first sentence.'),
        sp("Sports Bonuses and the Odds Rule", 115, {K0: 1}, "table3"),
        cb("Cashback and VIP Rates", 120, {K0: 1}, "vip"),
        rb("Daily Rebates", 55, {K0: 1}, "short"),
        rg("Using Offers Responsibly", 50, {K0: 1}, "short"),
        faq(["code", "odds", "cap", "support"], "Longfu88 Offers: Sports and Cashback Questions", 80, {K0: 1, KC: 1},
            extra='Where the phrase "Longfu88 promo code" is used it stands in the question about the promo code, written "Is there a Longfu88 promo code?".'),
    ],
})

variants.append({
    "id": "v04", "name": "Rewards and VIP (small)", "tier": "small", "angle": "A loyal player who looks for the rewards area, the VIP points and the live casino offer.",
    "skipped_clusters": [{"id": "k01", "reason": "left out of the short text; the offers are named in the sections that follow"},
                         {"id": "k04", "reason": "the wagering table is left out of the short text; the page keeps to the rewards and the VIP program"},
                         {"id": "k05", "reason": "reload offers are left out of the short text; the page keeps to rewards and loyalty"},
                         {"id": "k21", "reason": "a checklist is left out of the short text"}],
    "intent_summary": ("Short brand-subpage for the small size group: the Longfu88 welcome offer and its claiming path, the rewards area, the VIP points and reward levels, the live casino offer, mobile access and a few questions, for a "
                       "player from Singapore who wants the extras beyond the first deposit. Page voice: friendly but exact, a concrete example before each rule, sentences of about 13 words, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions for Loyal Players: Rewards and VIP Program", 50, {K0: 1, KB: 1}),
        wb("Starting With the Welcome Offer", 55, {K0: 1, KW: 1}, "short", extra='Where the phrase "Longfu88 welcome bonus" is used it stands in the first sentence.'),
        cl("Claim Path in Brief", 60, {K0: 1}, "short"),
        blk("RW", ["b16"], 2, "Longfu88 Bonus Crab, Wheel and Coin Shop in Brief", 75, {K0: 1}),
        vp("VIP Points and Reward Levels", 105, {K0: 1}, "base"),
        lv("Live Casino Offers", 65, {K0: 1}, "short"),
        pc("Longfu88 Promo Code: Anything Listed?", 45, {K0: 1}, "short"),
        mb("Phone Access", 45, {K0: 1}),
        faq(["vip", "coin", "live", "support"], "Longfu88 Offers: Loyalty Questions", 85, {K0: 1}),
    ],
})

# ------------------------------------------------------------------ MEDIUM (target 2544, limit 3053): the base ТЗ, differently composed
variants.append({
    "id": "v05", "name": "Newcomer path with cashing out", "tier": "medium", "angle": "A new player who has not claimed a bonus before and wants one guided path from the first deposit to the withdrawal.",
    "skipped_clusters": [],
    "intent_summary": ("Step-by-step brand-subpage for a newcomer to the Longfu88 bonuses in Singapore: how the three welcome offers compare, how to claim the main one, the terms before depositing, the minimum deposit of every offer, the promo code question, the "
                       "reload, free spin, seasonal and cashback offers, how long each offer lasts, verification and how bonus winnings are cashed out. Page voice: a patient guide, \"first, then\" logic, sentences of about 17 words, one plain consequence "
                       "after each term; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Welcome Bonus and Promotions: A Guide for New Players", 75, {K0: 3, KB: 1, KP: 1},
              extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        ov("What Bonuses Does the Casino Offer?", 100, {K0: 1}, "list"),
        wb("How the Three Welcome Offers Compare", 170, {K0: 2}, "cmp"),
        cl("Claim the Welcome Offer Step by Step", 120, {K0: 2}),
        tm("Longfu88 Bonus Terms Before You Deposit", 220, {K0: 2}, "deep"),
        md("What Each Offer Asks You to Deposit", 130, {K0: 1}),
        pc("Longfu88 Promo Code: Is One Needed?", 85, {K0: 1}),
        rl("Reload Offers for Your Next Deposits", 190, {K0: 1}),
        fs("Where Free Spins Come From", 90, {K0: 1}),
        se("Limited Campaigns to Watch", 110, {K0: 1}),
        n3_validity("How Long Each Offer Lasts", 120, {K0: 1}),
        cb("Cashback in Three Parts", 170, {K0: 1}, "vip"),
        rb("Daily Rebates in Brief", 60, {K0: 1}, "short"),
        n2_cashout("Cashing Out Bonus Winnings", 130, {K0: 1}),
        vf("Checks Before Bonus Winnings Are Paid", 100, {K0: 1}),
        sp("Sports Bonus Basics", 130, {K0: 1}, "short"),
        ck("A Checklist Before You Claim", 105, {K0: 1}),
        faq(["mindep", "dep", "one", "code", "valid", "excl", "cb", "support"], "Longfu88 Offers for Beginners: FAQ", 210, {K0: 2}),
    ],
})

variants.append({
    "id": "v06", "name": "Crypto and live casino focus", "tier": "medium", "angle": "A player who deposits in crypto or plays live casino and wants the matching offers, with sports crypto bonuses.",
    "skipped_clusters": [{"id": "k21", "reason": "a checklist is left out; the comparison tables already show the differences between the offers"}],
    "intent_summary": ("Brand-subpage about the Longfu88 offers for crypto and live casino players in Singapore: the offer families as a table, the three welcome offers compared, the claiming steps, the crypto offers with their terms and coins, the live casino offers, "
                       "the wagering of every offer side by side, the reloads, cashback, rebates and the crypto sports bonuses. Page voice: calm and comparative, the choice first and the numbers after it, sentences of about 16 words; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions for Crypto and Live Casino Players", 75, {K0: 3, KB: 1}),
        ov("Offer Families as a Table", 150, {K0: 1}, "table"),
        wb("Longfu88 Welcome Bonus Options Compared", 170, {K0: 2}, "cmp"),
        cl("Claiming a Welcome Offer", 100, {K0: 1}),
        cr("Longfu88 Bonus Options for Crypto Players", 270, {K0: 2}, "deep"),
        lv("Live Casino Bonuses in Full", 190, {K0: 2}, "deep"),
        n4_wagering("Wagering of Nine Offers Side by Side", 150, {K0: 1}),
        tm("Limits and Rules of the Main Offer", 115, {K0: 1}, "short"),
        md("Minimum Deposit in Euro and USDT", 90, {K0: 1}, idx=(-1, 0, 1, 3, 5)),
        rl("Reloads Week by Week", 160, {K0: 1}, rows=(3, 4, 5)),
        cb("Weekly Cashback Without the Fine Print", 135, {K0: 1}, "short"),
        rb("Rebates on Casino and Live Games", 70, {K0: 1}),
        sp("Sports Bonuses Paid in USDT and Euro", 230, {K0: 1}, "deep"),
        mb("Playing the Offers on a Phone", 60, {K0: 1}),
        pc("Is a Code Needed for Crypto Offers?", 70, {K0: 1, KC: 1}, "short",
           extra='Where the phrase "Longfu88 promo code" is used it stands in the first sentence, which says that the Brand Information of the casino lists no Longfu88 promo code for its offers.'),
        faq(["crypto", "live", "excl", "mindep", "sport", "code", "support"], "Longfu88 Offers: Crypto and Live Questions", 200, {K0: 1}),
    ],
})

variants.append({
    "id": "v07", "name": "Casino and sports bonuses", "tier": "medium", "angle": "A player who bets on sports as well as plays casino and wants both bonus sets with the odds they need.",
    "skipped_clusters": [{"id": "k21", "reason": "the closing checklist is left out; the FAQ closes the page"}],
    "intent_summary": ("Brand-subpage about the Longfu88 bonuses for casino and sports players in Singapore: the offer families, the welcome bonus and its activation, the terms, the promo code check, the reload, free spin, cashback and rebate offers, the crypto and live "
                       "welcome offers in short, the VIP program, the sports bonuses with the odds they need and the extras such as the Parlay Boost. Page voice: sober and exact, every number tied to the offer it belongs to, sentences of about 18 words with "
                       "a few shorter ones; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Casino and Sports Promotions: What Is on Offer for Players in Singapore", 75, {K0: 3, KB: 1, KP: 1},
              extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        ov("Casino Bonuses and Sports Bonuses Side by Side", 100, {K0: 1}, "list"),
        wb("Longfu88 Welcome Bonus in Brief", 140, {K0: 2}, "base"),
        cl("Activate the Offer in My Bonuses", 100, {K0: 1}),
        tm("Wagering, Maximum Bet and Cashout", 165, {K0: 2, KBO: 1}, "base", extra='Where the phrase "Longfu88 bonus" is used it stands in the first sentence.'),
        pc("Promo Code Check", 80, {K0: 1, KC: 1}, "base",
           extra='Where the phrase "Longfu88 promo code" is used it stands in the first sentence, which says that the Brand Information of the casino lists no Longfu88 promo code for its offers.'),
        rl("Casino Reload Bonuses Week by Week", 190, {K0: 2}),
        fs("Free Spins With Their Own Wagering", 90, {K0: 1}),
        cb("Weekly and Live Casino Cashback", 190, {K0: 2}, "vip"),
        rb("Unlimited Rebates by Game Category", 80, {K0: 1}),
        cr("The Crypto Route Into the Welcome Offer", 90, {K0: 1}, "short"),
        lv("Live Casino Welcome Offer", 90, {K0: 1}, "short"),
        vp("VIP Points and Cashback Levels", 100, {K0: 1}, "short"),
        sp("Sports Betting Bonuses and Qualifying Odds", 270, {K0: 2}, "deep"),
        n7_sportsx("Early Payout, Parlay Boost and Risk-Free Bet", 140, {K0: 1}),
        rg("Bonus Terms and Safer Play", 70, {K0: 1}),
        faq(["mindep", "sport", "odds", "one", "reload", "cap", "support"], "Longfu88 Offers: Casino and Sports Questions", 190, {K0: 1}),
    ],
})

variants.append({
    "id": "v08", "name": "Terms, verification and responsible use", "tier": "medium", "angle": "A cautious player who wants to know the rules before accepting an offer.",
    "skipped_clusters": [{"id": "k01", "reason": "the overview is left out; the terms-led page opens with the rules and names the offers inside them"}],
    "intent_summary": ("Terms-led brand-subpage about the Longfu88 bonuses in Singapore for a cautious reader: the rules at a glance, a glossary of bonus terms, the welcome offer and its claiming steps, the wagering of nine offers side by side, the validity of each offer, "
                       "verification before bonus winnings, how bonus winnings are cashed out, the promo code question, the reloads and cashback and responsible use. Page voice: sober and exact, every claim tied to a stated term, sentences of about 18 "
                       "words, no reassurance beyond the facts; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Bonus Terms and Rules: What to Check Before You Claim", 75, {K0: 3, KB: 1, KP: 1},
              extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        n1_glossary("Bonus Terms Explained", 115),
        wb("Longfu88 Welcome Bonus Rules in Short", 70, {K0: 2}, "short"),
        cl("Claiming Without Losing Eligibility", 110, {K0: 1}),
        tm("Wagering, Cashout and the Six Rules", 240, {K0: 2}, "deep"),
        n4_wagering("Wagering at a Glance", 140, {K0: 1}),
        n3_validity("Validity Period of Each Offer", 120, {K0: 1}),
        vf("Verification Before Bonus Winnings", 140, {K0: 1}),
        n2_cashout("Cashing Out After the Wagering", 140, {K0: 1}),
        pc("Longfu88 Promo Code and Activation Rules", 100, {K0: 1}),
        md("Minimum Deposits and the Excluded Payment Methods", 100, {K0: 1}, idx=(-1, 0, 1, 2, 4, 6)),
        rl("Reload Conditions in Detail", 175, {K0: 1}),
        se("Campaigns With Their Own Conditions", 115, {K0: 1, KO: 1}, extra='Where the phrase "Longfu88 offers" is used it stands in the first sentence, which says that the campaigns are not permanent Longfu88 offers.'),
        cb("Cashback Conditions", 170, {K0: 1}, "deep"),
        rg("Using Bonuses Responsibly", 110, {K0: 1}),
        ck("Seven Checks That Close the Rules", 105, {K0: 1}),
        faq(["wd", "ver", "excl", "one", "age", "cashout", "support"], "Frequently Asked Questions on Bonus Rules", 190, {K0: 1}),
    ],
})

variants.append({
    "id": "v09", "name": "Loyalty, VIP and rewards", "tier": "medium", "angle": "A regular player who wants the extras beyond the first deposit: VIP points, the rewards area, Bonus Crab and the cashback by level.",
    "skipped_clusters": [{"id": "k21", "reason": "a checklist is left out; the page closes with the FAQ"},
                         {"id": "k01", "reason": "the overview is left out; the page starts from the welcome offer and names the other offers in their sections"}],
    "intent_summary": ("Brand-subpage about the Longfu88 offers for regular players in Singapore: the welcome offer and its claiming path as the entry point, the terms in short, the reloads, free spins and seasonal campaigns, the cashback by VIP level, the rebates, "
                       "the VIP program with eight reward levels, the rewards area and how Bonus Crab works, the live casino offer and mobile access. Page voice: friendly but exact, a concrete example before each rule, sentences of about 16 words; no "
                       "calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions for Active Players: Rewards, VIP and Cashback", 75, {K0: 3, KB: 1}),
        wb("The Welcome Offer as an Entry Point", 150, {K0: 2, KW: 1}, "base", extra='Where the phrase "Longfu88 welcome bonus" is used it stands in the first sentence.'),
        cl("Claim It in Three Sentences", 70, {K0: 1}, "short"),
        tm("Terms in Short", 130, {K0: 1}, "short"),
        pc("Longfu88 Promo Code and My Bonuses", 80, {K0: 1}),
        rl("Reloads for Regular Depositors", 180, {K0: 1}, rows=(3, 4, 5, 6)),
        fs("Free Spins in Short", 70, {K0: 1}, "short"),
        se("Seasonal Campaigns", 115, {K0: 1}),
        cb("Cashback by VIP Level", 200, {K0: 2}, "deep"),
        rb("Rebates Credited Daily", 70, {K0: 1}),
        vp("The VIP Program in Depth: Eight of 25 Levels", 250, {K0: 1}, "deep"),
        rw("The Rewards Area: Where Each Feature Sits", 200, {K0: 1}, "deep"),
        n6_crab("How Longfu88 Bonus Crab Works", 120, {K0: 1}),
        lv("Live Casino Offers for Regulars", 100, {K0: 1}, "base"),
        sp("Sports Bonus Basics for Casino Players", 100, {K0: 1}, "short"),
        mb("Rewards on a Phone", 60, {K0: 1}),
        faq(["vip", "crab", "coin", "cap", "rebate", "reload", "support"], "Longfu88 Offers: Loyalty and Rewards Questions", 215, {K0: 1}),
    ],
})

variants.append({
    "id": "v10", "name": "Ledger of every offer", "tier": "medium", "angle": "A reader who wants every offer, its reward, deposit, wagering and validity in one table before reading the details.",
    "skipped_clusters": [{"id": "k03", "reason": "the claiming steps are left out; every offer is activated in My Bonuses, which the ledger and the promo code section name"}],
    "intent_summary": ("Reference-style brand-subpage about the Longfu88 offers in Singapore: one ledger table with nine casino offers, the three welcome offers compared, the terms in short, the promo code question, the minimum deposits, the reloads, free spins, crypto "
                       "and live offers, the seasonal campaigns, the cashback and rebates, the sports bonus table and a checklist. Page voice: reference-like, each section opens with what the table or paragraph is for, sentences of about 17 words; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Offers Compared: A Ledger of Bonuses and Promotions", 70, {K0: 2, KB: 1, KP: 1},
              extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        n5_ledger("Longfu88 Bonus Ledger: Every Casino Offer in One Table", 200, {K0: 1}),
        ov("The Offer Families Behind the Ledger", 100, {K0: 1}, "short"),
        wb("Longfu88 Welcome Bonus Variants Side by Side", 150, {K0: 2}, "cmp"),
        tm("Terms of the Main Offer in Short", 100, {K0: 1}, "short"),
        pc("Is a Code Part of the Ledger?", 70, {K0: 1}, "short"),
        md("Minimum Deposit Column in Detail", 105, {K0: 1}, idx=(-1, 0, 1, 2, 3, 4, 5, 6, 7)),
        rl("Reload Rows in Detail", 190, {K0: 1}),
        fs("Free Spin Rows", 100, {K0: 1}),
        cr("Crypto Rows", 150, {K0: 1}, "base"),
        lv("Live Casino Rows", 120, {K0: 1}, "base"),
        se("Seasonal Rows", 120, {K0: 1}),
        cb("Cashback and Rebate Rows", 180, {K0: 1}, "vip"),
        rb("Rebate Rates", 80, {K0: 1}),
        sp("Sports Rows With Their Odds Rule", 210, {K0: 1}, "base"),
        n3_validity("Validity Column in Detail", 115, {K0: 1}),
        ck("Checks Before Using the Ledger", 105, {K0: 1}),
        faq(["mindep", "valid", "one", "excl", "code", "reload", "support"], "Ledger Questions Answered", 190, {K0: 1, KC: 1},
            extra='Where the phrase "Longfu88 promo code" is used it stands in the question about the promo code, written "Is there a Longfu88 promo code?".'),
    ],
})

# ------------------------------------------------------------------ LARGE (limit 2634 = the mean of the group, may be shorter): almost every topic of the pool, shallow
variants.append({
    "id": "v11", "name": "Complete bonus handbook A (large)", "tier": "large", "angle": "A reader who wants every bonus, term and rule of the casino on one page, organised as a handbook with detail sections.",
    "skipped_clusters": [],
    "intent_summary": ("Complete brand-subpage for the large size group of the competitors, built like the longest bonus pages of the query: a handbook of the Longfu88 bonuses for players from Singapore with the offer families, the welcome bonus with its steps and terms "
                       "as detail sections, the promo code question, the minimum deposits, the reload, free spin, seasonal, crypto and live casino offers, the cashback with the rebates, the VIP program, the rewards area, the sports bonuses with the extras, "
                       "verification and cashing out, a glossary, responsible use and mobile access, and a long FAQ. Page voice: reference-like, each H2 opens with what the section is for, sentences of about 18 words, a consequence after each condition. Every "
                       "section is written only from the facts of its Brand Information; where a section has few facts it stays short. H2 sections with H3 details." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions Handbook: Every Bonus, Term and Promo Code", 70, {K0: 2, KB: 1}),
        ov("Longfu88 Bonus Types and Families", 90, {K0: 1}, "list"),
        wb("The Main Offer and Its Two Alternatives", 100, {K0: 1, KW: 1}, "base", extra='Where the phrase "Longfu88 welcome bonus" is used it stands in the first sentence.'),
        cl("How to Claim the Casino Welcome Bonus", 70, {K0: 1}, "base", level=3),
        tm("Wagering and Rules of the Welcome Bonus", 110, {K0: 1}, "base", level=3),
        pc("Is There a Promo Code at All?", 70, {K0: 1, KC: 1}, "base",
           extra='Where the phrase "Longfu88 promo code" is used it stands in the first sentence, which says that the Brand Information of the casino lists no Longfu88 promo code for its offers.'),
        md("Minimum Deposit of Every Offer at a Glance", 90, {K0: 1}),
        rl("Reload Bonuses: Weekly, Weekend and One-Day", 120, {K0: 1}),
        fs("Free Spins: Weekly Reload and Seasonal Offers", 70, {K0: 1}),
        cr("Crypto Welcome and Reload Offers with USDT", 90, {K0: 1}),
        lv("Offers for Live Dealer Games", 80, {K0: 1}),
        se("Seasonal and Verification Campaigns", 80, {K0: 1}),
        cb("Cashback: Weekly, Live and by VIP Level", 120, {K0: 1}, "vip"),
        rb("Unlimited Rebates", 50, {K0: 1}, "base", level=3),
        vp("VIP Program Levels and Points", 100, {K0: 1}, "base"),
        rw("Rewards Area: Crab, Wheel, Challenges and Shop", 70, {K0: 1}),
        sp("Sportsbook Offers and Qualifying Odds", 150, {K0: 1}, "base"),
        n7_sportsx("Sports Extras: Early Payout and Parlay Boost", 90, {K0: 1}, level=3),
        vf("Documents and Checks Before Payout", 80, {K0: 1}),
        n2_cashout("Cashing Out Bonus Winnings Step by Step", 80, {K0: 1}),
        n1_glossary("Glossary of Bonus Words", 70, {K0: 1}),
        rg("Bonus Terms and Responsible Play", 55, {K0: 1}),
        mb("Claiming Bonuses on a Phone", 40, {K0: 1}),
        ck("Checks Before You Claim an Offer", 85, {K0: 1}),
        faq(["mindep", "code", "one", "excl", "wd", "ver", "cb", "coin"], "Longfu88 Offers: Complete FAQ", 140, {K0: 1}),
    ],
})

variants.append({
    "id": "v12", "name": "Complete bonus handbook B (large)", "tier": "large", "angle": "A reader who compares the offers: terms tables, wagering and validity side by side, with sports extras and the Bonus Crab detail.",
    "skipped_clusters": [],
    "intent_summary": ("Complete brand-subpage for the large size group, organised around comparison: the offer families as a table, the three welcome offers compared, the claiming steps, the terms, the wagering and the validity of the offers side by side, "
                       "the promo code question, the reloads, free spins, crypto, live and seasonal offers, the cashback and rebates, the VIP program, the rewards area with Bonus Crab as a detail section, the sports bonuses with the extras, verification, "
                       "responsible use, a checklist and a long FAQ. Page voice: analytical and even, the comparison first and the explanation after it, sentences of about 17 words, no calls to action. Every section is written only from the facts of its Brand "
                       "Information. H2 sections with H3 details." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Bonus Guide: Every Offer, Rule and Reward", 70, {K0: 2, KB: 1, KP: 1},
              extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        ov("Offers at a Glance", 100, {K0: 1}, "table"),
        wb("Longfu88 Welcome Bonus Compared With Its Alternatives", 100, {K0: 1}, "cmp"),
        cl("Four Steps to Claim the Main Offer", 70, {K0: 1}, "base", level=3),
        tm("Terms of the Main Offer", 110, {K0: 1}, "base", level=3),
        n4_wagering("Wagering of Nine Offers", 110, {K0: 1}),
        n3_validity("Validity of Six Casino Offers and One Sports Offer", 90, {K0: 1}),
        pc("Promo Code and Activation", 70, {K0: 1, KC: 1}, "base",
           extra='Where the phrase "Longfu88 promo code" is used it stands in the first sentence, which says that the Brand Information of the casino lists no Longfu88 promo code for its offers.'),
        rl("Reloads Compared", 120, {K0: 1}),
        fs("Free Spins Compared", 70, {K0: 1}),
        cr("Crypto Offers", 90, {K0: 1}),
        lv("Live Casino Offers Compared", 80, {K0: 1}),
        se("Limited Campaigns", 80, {K0: 1}),
        cb("Cashback and Its VIP Rates", 120, {K0: 1}, "vip"),
        rb("Rebates Compared", 50, {K0: 1}, "base", level=3),
        vp("VIP Program in Brief", 80, {K0: 1}, "short"),
        rw("Rewards Area", 70, {K0: 1}),
        n6_crab("Bonus Crab in Detail", 90, {K0: 1}),
        sp("Sports Bonuses Compared", 150, {K0: 1}, "base"),
        n7_sportsx("Sports Extras Beyond Match Bonuses", 90, {K0: 1}, level=3),
        vf("Verification Documents", 80, {K0: 1}),
        rg("Responsible Use of Offers", 55, {K0: 1}),
        ck("Seven Checks Before Claiming", 85, {K0: 1}),
        faq(["mindep", "dep", "valid", "cashout", "maxbet", "rebate", "crab", "support"], "Longfu88 Offers: Last Questions Answered", 140, {K0: 1}),
    ],
})

# ---------------------------------------------------------------- the intro signposts only the topics that the variant has; the cashback block points to the VIP section only when there is one
COVERS = {
    "v01": "the welcome offer with its claiming steps, the terms, the promo code answer, the reloads, free spins and cashback",
    "v02": "the welcome offer, the minimum deposit of each offer, the crypto welcome offer, the terms and a short checklist",
    "v03": "the bonus families, the welcome offer basics, the sports bonuses, the weekly cashback and the rebates",
    "v04": "the welcome offer, the rewards area, the VIP points and the live casino offer",
    "v05": "the three welcome offers, the claiming steps, the terms, the reloads, the cashback and how bonus winnings are cashed out",
    "v06": "the welcome offers compared, the crypto and live casino offers, the wagering of nine offers and the sports bonuses",
    "v07": "the welcome offer, the reloads, the cashback, the VIP program and the sports bonuses with their extras",
    "v08": "a glossary of bonus terms, the wagering and validity of the offers, verification and the cashing out of bonus winnings",
    "v09": "the welcome offer, the reloads, the cashback by VIP level, the VIP program and the rewards area",
    "v10": "a ledger of nine casino offers, the welcome offers compared, the reloads, the crypto and live offers and the sports bonuses",
    "v11": "the welcome offer, the reloads, the free spins, the crypto and live offers, the cashback, the VIP program, the rewards area and the sports bonuses",
    "v12": "the welcome offers compared, the terms and the wagering side by side, the reloads, the cashback, the VIP program and the sports bonuses",
}
for v in variants:
    b0 = v["blocks"][0]
    b0["summary"] = f"What the page covers: {COVERS[v['id']]}."
    b0["notes"] = ('Open with "Longfu88" as the subject of the first sentence: the casino runs a set of bonuses that start with the Casino Welcome Bonus. The phrase "Longfu bonus" stands once in a sentence that says that players '
                   f'looking for the Longfu bonus find {COVERS[v["id"]]} on this page. Quote the welcome bonus summary of the Brand Information once, character for character '
                   '(188% up to €2,088 + 18 Free Spins; 25x deposit plus bonus, 40x Free Spins winnings). State once that the bonuses are for players aged 18 or over and that the page is written for players from Singapore. '
                   f'Signpost the topics in one sentence without detail. {LEGAL} {NO_INVENT} Neutral tone, no promises.')
    has_vip = any(b["topic"] == "VP" for b in v["blocks"])
    for b in v["blocks"]:
        if b["topic"] == "CB" and not has_vip and not b.get("notes") and not any(PTR_VIP == e[0] for e in b.get("edit", [])):
            b["edit"] = b.get("edit", []) + [[PTR_VIP, ""]]

# ---------------------------------------------------------------- sizes: the medium variants are scaled towards the mean of their group (2544), each block range stays proportionate
# (the coverage budget of the code still enlarges a block whose facts need more, and the limit of the group is checked by `textgen variants`)
SCALE = {"v05": 2450, "v06": 2400, "v07": 2350, "v08": 2400, "v09": 2380, "v10": 2450}
for v in variants:
    if v["id"] in SCALE:
        total = sum(b["words"] for b in v["blocks"])
        f = SCALE[v["id"]] / total
        for b in v["blocks"]:
            b["words"] = round(b["words"] * f)

# ---------------------------------------------------------------- self-checks of the blueprint
heads = [b["heading"].lower() for v in variants for b in v["blocks"]]
dup = {h for h in heads if heads.count(h) > 1}
assert not dup, dup

# honest distance: base topics by code, new topics by their N code (the heading differs per variant, the official metric counts it as a separate topic)
topics = {v["id"]: {b["topic"] for b in v["blocks"]} for v in variants}
pairs = sorted(((len(topics[a] ^ topics[b]), a, b) for a, b in combinations(topics, 2)))
print("topic-only distance (no depth): min", pairs[0], "| median", pairs[len(pairs) // 2][0], "| max", pairs[-1][0])

intrinsic = {}
blueprint = {"base_run": "longfu88-bonus-sg", "brand_names": ["Longfu88 Welcome Bonus", "Longfu88 Promotions", "Longfu88 Offers", "Longfu88 Promo Code", "Longfu88"], "keyword_labels": {},
             "intrinsic": intrinsic, "variants": variants}
out = Path("input/variants/longfu88-bonus-sg.json")
out.write_text(json.dumps(blueprint, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(variants), "variants")
