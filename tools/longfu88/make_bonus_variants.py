"""Blueprint of 8 ТЗ variants for the Longfu88 bonuses and promo code page (brand-subpage, GEO MY) -> input/variants/longfu88-bonus-my.json.
Base run: runs/longfu88-bonus-my (tools/longfu88/make_bonus_base.py, the OPTIMUM group `medium`). Run from the project root:
    python tools/longfu88/make_bonus_variants.py
    python -m textgen variants input/variants/longfu88-bonus-my.json --force

The competitors fall into three size groups (python -m textgen tiers longfu88-bonus-my --texts 8):
    small   757   -> target 757,  limit 908      3 variants: v01-v03, the most important blocks, entities and facts cut to the minimum
    medium  1029  -> target 1029, limit 1235     4 variants: v04-v07, the base ТЗ with another set of topics, order, headings, formats, facts
    large   2544  -> limit 2544 (x1.0)           1 variant:  v08, the base plus every topic the knowledge base can fill (shorter than the limit)
Base blocks: b01 intro, b02 bonus types, b03 welcome bonus, b04 claim steps, b05 wagering and terms, b06 promo code, b07 reload bonuses,
b08 free spins, b09 cashback, b10 rewards area, b11 FAQ.
Extra topics of the pool (only some variants have them, so that the structures differ): minimum deposit by offer (MD), crypto offers (CR),
live casino offers (LV), sports bonuses (SP), seasonal promotions (SE), rebates (RB), verification before bonus winnings (VF), responsible use
(RG), mobile access (MB), before-you-claim checklist (CK).
The five single keywords ("Longfu bonus", "Longfu88 welcome bonus", "Longfu88 promo code", "Longfu88 offers", "Longfu88 promotions") are used
exactly once per text, in a heading or in a body; "Longfu88" is counted by the code over bodies and headings."""
import json
from pathlib import Path

K0, KB, KW, KC, KO, KP = ("Longfu88", "Longfu bonus", "Longfu88 welcome bonus", "Longfu88 promo code", "Longfu88 offers", "Longfu88 promotions")

P = "brandinfo_promotions.other_bonuses"
W = "brandinfo_welcome.welcome_bonus"
G = "brandinfo_promotions.gamification_features"
S = "brandinfo_sportsbook.sportsbook.sports_bonuses"

LEGAL = "Do not say or imply that the casino or its bonuses are licensed, legal or approved in Malaysia, and do not discuss the licence on this page."
NO_INVENT = ("Use only the amounts, percentages, wagering multiples, periods and names of the Brand Information, character for character; no other offer, no code, no bonus that is not listed, "
             "no promise of winnings, no advice to claim every offer, no comparison with other casinos. Do not convert the euro amounts into other currencies.")
NO_CODE = "Do not invent a promo code, a coupon or a bonus code, and do not name any."
VOICE_TAIL = " All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Malaysia."


def rrefs(*idx, extra=()):
    """name, reward, minimum deposit and wagering of the other_bonuses items (a table row each)."""
    return [f"{P}[{i}].{f}" for i in idx for f in ("name", "reward", "minimum_deposit", "wagering_requirement")] + list(extra)


# exact pieces of the base notes (tools/longfu88/make_bonus_base.py) that a variant changes
B09_REBATES = ("Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback) in one sentence, and the Unlimited Casino Rebate (0.9%) and the Unlimited Live Casino Rebate (1.0%) in one sentence: "
               "rebates are credited daily and carry 1x wagering on the credited rebate (that figure is in the Brand Information, state it once). ")
B09_REBATES_DROP = [f"{P}[11].rebate_percentage", f"{P}[12].rebate_percentage"]
B09_LIVE_DROP = [f"{P}[10].reward", f"{P}[10].wagering_requirement"]
B09_VIPNOTE = "Do not give the VIP cashback levels (the VIP page of the site covers them). "

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
}
BASE_FAQ_REFS = [f"{W}.minimum_deposit", f"{W}.validity", f"{W}.important_terms[2]", f"{P}[9].opt_in", "brandinfo_general.customer_support.channels"]


def faq(keys):
    """Override of the FAQ block: the questions of this variant, in order, and only the facts they need."""
    qs = "; ".join(f"({i}) {FAQ[k][0]}" for i, k in enumerate(keys, 1))
    notes = (f'A bulleted list of {len(keys)} items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required here for the question text only. '
             f"Questions, in this order: {qs}. Answers repeat the facts of the sections above in other words and add nothing new. {NO_INVENT}")
    need = list(dict.fromkeys(r for k in keys for r in FAQ[k][1]))
    return {"notes": notes, "refs_add": [r for r in need if r not in BASE_FAQ_REFS], "refs_drop": [r for r in BASE_FAQ_REFS if r not in need],
            "summary": f"{len(keys)} short questions and answers on the bonuses of the casino."}


def blk(ids, level, heading, words, kw=None, fmt=None, edit=None, extra=None, summary=None, **more):
    b = {"from": ids, "level": level, "heading": heading, "words": words, "kw": kw or {}}
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


def intro(heading, words, kw, extra=None, edit=None):
    return blk(["b01"], 1, heading, words, kw, extra=extra, edit=edit)


def new(level, heading, words, refs, ents, conns, summary, notes, covers, fmt=None, kw=None):
    """A block that the base ТЗ does not have: its facts come from `refs` only."""
    return blk([], level, heading, words, kw or {}, fmt, summary=summary, entities=ents, connections=conns, kb_refs=refs, notes=notes, covers_clusters=covers)


PL = ["paragraph", "list"]
PT = ["paragraph", "table"]
SKIP_OV = {"id": "k16", "reason": "left out of the short text; the offer families are named in the sections that follow"}
SKIP_VIP = {"id": "k07", "reason": "belongs to the VIP Program page of the site; the VIP cashback levels are left to that page"}
SKIP_RL = {"id": "k04", "reason": "left out of the short text; the Weekly Reload appears in the free spins section"}
SKIP_FS = {"id": "k06", "reason": "free spins are covered inside the reload and seasonal sections"}

# ---------------------------------------------------------------- blocks of the extra topics (shared notes, each variant sets its own size and keywords)


def md(heading, words, idx, kw=None):
    """Minimum deposit by offer: a two-column table, one row per offer index (-1 = the Casino Welcome Bonus)."""
    refs = []
    names = []
    for i in idx:
        base = W if i == -1 else f"{P}[{i}]"
        refs += [f"{base}.name", f"{base}.minimum_deposit"]
    return new(2, heading, words, refs,
               [["Minimum Deposit", 10], ["Bonus Offers", 7]], [["Minimum Deposit", "differs by", "offer and by currency of the deposit", 8]],
               "The minimum deposit that each listed offer asks for, offer by offer.",
               "One lead-in sentence that says that the minimum deposit depends on the offer, then a TABLE with two columns, offer | minimum deposit, and one row per offer in this order: "
               + ", ".join(["Casino Welcome Bonus" if i == -1 else {0: "Live Casino Welcome Bonus", 1: "Casino Crypto Welcome Bonus", 2: "Casino Weekly Reload", 3: "Casino Weekly Crypto Reload",
                                                                     4: "Casino Weekend Reload", 5: "Casino Weekend Crypto Reload", 6: "Casino Double Fortune: One-Day Reload Special",
                                                                     7: "Casino Trick or Treat Pumpkin Bonanza", 8: "Casino Dragon Quest: Get Verified and Get Extra!"}[i] for i in idx])
               + " (names and values exactly as in the Brand Information; crypto offers in USDT). One closing sentence: the general minimum deposit of the casino is not the minimum of an offer, so the player checks "
               f"the offer first. Do NOT state the general minimum deposit amount. {NO_INVENT}", ["k03"], PT, kw)


def cr(heading, words, kw=None):
    return new(2, heading, words,
               [f"{P}[1].name", f"{P}[1].reward", f"{P}[1].minimum_deposit", f"{P}[1].wagering_requirement", f"{P}[1].validity", f"{P}[1].important_terms[1]",
                f"{P}[1].eligible_cryptocurrencies"] + rrefs(3, 5),
               [["Crypto Bonuses", 10], ["USDT", 7], ["Eligible Cryptocurrencies", 6]], [["Casino Crypto Welcome Bonus", "accepts", "a first qualifying crypto deposit", 8]],
               "The crypto offers: the Casino Crypto Welcome Bonus (188% up to 2,888 USDT), the weekly and weekend crypto reloads and the eligible coins.",
               "Lead with the Casino Crypto Welcome Bonus: 188% up to 2,888 USDT for a first qualifying crypto deposit of at least 50 USDT, wagering 40x deposit plus bonus, valid 10 days, maximum bonus wager 5 USDT per spin. "
               "Then a TABLE with four columns, offer | reward | minimum deposit | wagering, and two rows: Casino Weekly Crypto Reload, Casino Weekend Crypto Reload (values exactly as in the Brand Information). "
               "Then one sentence with the eligible cryptocurrencies as given (USDT, BTC, BCH, LTC, ETH, XRP, USDC). The Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers: say so once. "
               f"{NO_INVENT}", ["k01", "k04"], PT, kw)


def lv(heading, words, kw=None):
    return new(2, heading, words,
               [f"{P}[0].name", f"{P}[0].reward", f"{P}[0].minimum_deposit", f"{P}[0].wagering_requirement", f"{P}[0].validity", f"{P}[0].important_terms[1]",
                f"{P}[10].name", f"{P}[10].reward", f"{P}[10].wagering_requirement", f"{P}[12].name", f"{P}[12].rebate_percentage"],
               [["Live Casino", 10], ["Live Casino Cashback", 7]], [["Live Casino Welcome Bonus", "targets", "new players who start with live casino games", 8]],
               "The live casino offers: the Live Casino Welcome Bonus (125% up to €888), the Live Casino Cashback (25% up to €850) and the Unlimited Live Casino Rebate (1.0%).",
               "Lead with the Live Casino Welcome Bonus: 125% up to €888, minimum deposit €30, wagering 30x the deposit plus bonus, valid 7 days, maximum bet €25, for new players on the first qualifying deposit. "
               "Then the Live Casino Cashback in one sentence (25% up to €850, wagering 10x the credited cashback, based on real-money stakes less winnings in eligible Live Casino games) and the Unlimited Live Casino Rebate "
               f"in one sentence (1.0%, credited daily). No game names. {NO_INVENT}", ["k01", "k05"], ["paragraph"], kw)


def sp(heading, words, idx=(0, 2, 3), kw=None, level=2):
    rows = ", ".join({0: "Sport First Deposit Bonus", 1: "Sport Crypto Welcome Bonus", 2: "Sport Weekly Reload Bonus", 3: "Sport Weekend Reload Bonus"}[i] for i in idx)
    return new(level, heading, words,
               [f"{S}[{i}].{f}" for i in idx for f in ("name", "reward", "minimum_deposit", "wagering_requirement")]
               + [f"{S}[0].validity", f"{S}[0].important_terms[1]", f"{S}[0].important_terms[2]", f"{S}[9].name", f"{S}[9].reward"],
               [["Sports Betting Bonuses", 10], ["Qualifying Bets", 7], ["Wagering Requirement", 6]], [["Qualifying Sports Bets", "count toward", "the wagering of a sports bonus", 8]],
               "The sports bonuses: first deposit and reload offers with a low 8x wagering, the odds required for qualifying bets and the Parlay Boost.",
               "One lead-in sentence that says that the sportsbook has its own bonuses, then a TABLE with four columns, offer | reward | minimum deposit | wagering, and rows in this order: " + rows
               + " (values exactly as in the Brand Information). After the table two sentences: only settled qualifying sports bets count toward the wagering, single bets need odds of at least 2.00 and each accumulator selection at least 1.50, "
               "voided and cashed-out bets do not qualify; the offers are valid for 30 days. One closing sentence names the Parlay Boost: up to 100% extra winnings on qualifying accumulators. "
               f"No sports tips, no odds of events. {NO_INVENT}", ["k12"], PT, kw)


def se(heading, words, kw=None):
    return new(2, heading, words,
               rrefs(7, 8) + [f"{P}[7].validity", f"{P}[8].eligibility", f"{P}[8].important_terms[2]"],
               [["Seasonal Promotions", 10], ["Account Verification", 6]], [["Casino Dragon Quest", "rewards", "players who complete the requested account verification", 8]],
               "Two limited campaigns: the Trick or Treat Pumpkin Bonanza with up to 100 Free Spins and the Dragon Quest verification reward of a €10 bonus credit.",
               "Say first that campaigns come and go, so the list may change: the player checks the promotions page of the casino. Then the two campaigns of the Brand Information: the Casino Trick or Treat Pumpkin Bonanza "
               "(up to 100 Free Spins, minimum deposit €20, wagering 40x Free Spins winnings, valid 7 days) and the Casino Dragon Quest: Get Verified and Get Extra! (a €10 bonus credit for players who complete the requested "
               "account verification during the campaign, minimum deposit €20, wagering 30x the promotional credit, valid 7 days). Both carry the €5 per spin maximum stake while wagering bonus funds and cannot be combined with another active "
               f"casino bonus. Do not claim that either campaign is running now. {NO_INVENT}", ["k06"], ["paragraph"], kw)


def rb(heading, words, level=2, kw=None):
    return new(level, heading, words,
               [f"{P}[{i}].{f}" for i in (11, 12, 13, 14) for f in ("name", "rebate_percentage")] + [f"{P}[11].crediting", f"{P}[11].wagering_requirement"],
               [["Rebate", 10], ["Rewards Balance", 6]], [["Unlimited Rebate", "returns", "a share of qualifying settled real-money wagering every day", 8]],
               "Four unlimited rebates of 0.8% to 1.0% of qualifying wagering, credited daily with 1x wagering on the credited rebate.",
               "One lead-in sentence that says that a rebate returns a share of qualifying settled real-money wagering on a game category, then a TABLE with two columns, rebate | rate, and four rows in this order: "
               "Unlimited Casino Rebate 0.9%, Unlimited Live Casino Rebate 1.0%, Unlimited P2P Rebate 0.8%, Unlimited Lottery Rebate 1.0%. One closing sentence: the rebate is credited daily to the rewards balance and carries "
               f"1x wagering on the credited rebate. {NO_INVENT}", ["k05"], PT, kw)


def vf(heading, words, kw=None):
    return new(2, heading, words,
               [f"{W}.important_terms[5]", f"{W}.important_terms[3]", "brandinfo_account.verification.documents", "brandinfo_account.verification.document_submission_window",
                "brandinfo_account.verification.typical_review_time"],
               [["Account Verification", 10], ["Promotional Winnings", 7]], [["Account Verification", "can precede", "the payment of promotional winnings", 8]],
               "Verification can be required before promotional winnings are paid; the documents, the 30-day submission window and the review time of up to 10 days.",
               "Say first that account verification may be required before promotional winnings are paid and that a withdrawal request before claiming a bonus or while it is active can void the promotional eligibility. "
               "Then the documents of the Brand Information as a short bulleted list (government-issued photo ID or passport; proof of residential address; proof of ownership of a payment method; source of funds or wealth documents "
               "when requested), then one sentence with the submission window (up to 30 days when requested) and the review time (up to 10 days after a complete document set is received). "
               f"No other documents, no promise of speed. {NO_INVENT}", ["k03"], PL, kw)


def rg(heading, words, kw=None):
    return new(2, heading, words,
               ["brandinfo_general.minimum_age", "brandinfo_responsible_gaming.responsible_gaming.policy", "brandinfo_responsible_gaming.responsible_gaming.self_assessment",
                "brandinfo_responsible_gaming.responsible_gaming.support_organizations", f"{W}.important_terms[4]"],
               [["Responsible Gambling", 10], ["Minimum Age", 6]], [["Bonus Terms", "should be read", "before the player accepts an offer", 7]],
               "Bonuses are for players of 18 or over who gamble where it is lawful; read the terms first, use the self-assessment questions and the support organisations of the casino.",
               "Say that the bonuses are for players aged 18 or over who gamble only where it is lawful, and that the terms of an offer (wagering, maximum bet, validity) should be read before accepting it. Cancelling the promotion "
               "forfeits bonus funds and unconverted promotional winnings (state it as a fact). Then one sentence on the self-assessment questions that help players identify possible gambling-related harm and one that names the "
               f"support organisations (GamCare, Gamblers Anonymous, Gambling Therapy). No advice to chase losses, no promise. {LEGAL} {NO_INVENT}", ["k03"], ["paragraph"], kw)


def mb(heading, words, kw=None):
    return new(2, heading, words,
               ["brandinfo_app.app_information.mobile_access", "brandinfo_app.app_information.features"],
               [["Mobile Access", 10], ["My Bonuses", 6]], [["Responsive Website", "gives access to", "bonuses, deposits and the account on a phone", 7]],
               "The bonuses can be reached on a phone through the responsive website; no separate app is given.",
               "Two or three sentences: the casino website is responsive and works in the browser of a smartphone or tablet, and bonuses are among the features of the mobile website next to the casino, the sportsbook, account access, "
               "deposits and withdrawals. Do not say or imply that a native app, an APK file, a store listing or push notifications of bonuses exist: none is given. One pointer to the mobile page of the site is allowed in one clause. "
               f"{NO_INVENT}", ["k14"], ["paragraph"], kw)


def ck(heading, words, kw=None):
    return new(2, heading, words,
               [f"{W}.eligibility", f"{W}.minimum_deposit", f"{W}.important_terms[0]", f"{W}.important_terms[2]", f"{W}.important_terms[3]", f"{W}.important_terms[5]",
                f"{W}.claiming_procedure[2]"],
               [["Bonus Checklist", 10], ["My Bonuses", 7], ["Eligibility", 6]], [["Player", "checks", "eligibility, deposit and active bonus before claiming", 7]],
               "Seven checks before claiming the Casino Welcome Bonus: new player, first qualifying deposit of €50, Neteller and Skrill excluded, one active bonus, activation before wagering, no withdrawal request, verification.",
               "One lead-in sentence, then a bulleted list of seven short checks in this order: the player is a new registered player (one welcome offer per account); the first qualifying deposit is at least €50; the deposit is not made with Neteller or "
               "Skrill; no other promotional bonus is active; the bonus is activated in My Bonuses before any wager; no withdrawal request is made before claiming or while the bonus is active; verification may be required before promotional winnings "
               f"are paid. Each item one clause of up to 14 words. {NO_INVENT}", ["k02", "k03"], PL, kw)


def wc(heading, words, kw=None, level=2):
    """The welcome bonus as a comparison of the three welcome offers (replaces the notes of b03)."""
    return blk(["b03"], level, heading, words, kw, PT,
               notes=("Lead-in of two sentences: the Casino Welcome Bonus is the main offer, a first-deposit casino bonus of 188% up to €2,088 plus 18 Free Spins for new registered players on the first qualifying deposit, one welcome offer per account; "
                      "the Casino Welcome Bonus and the Casino Crypto Welcome Bonus are alternative first-deposit offers. Then a TABLE with four columns, offer | reward | minimum deposit | validity, and three rows in this order: Casino Welcome Bonus "
                      "(188% up to €2,088 + 18 Free Spins | €50 | 10 days from activation), Live Casino Welcome Bonus (125% up to €888 | €30 | 7 days), Casino Crypto Welcome Bonus (188% up to 2,888 USDT | 50 USDT | 10 days). "
                      f"Use the €50 of the bonus, do NOT mention the general minimum deposit of €10. No wagering numbers here (the terms section gives them). {NO_INVENT}"),
               refs_add=[f"{P}[0].minimum_deposit", f"{P}[0].validity", f"{P}[1].minimum_deposit", f"{P}[1].validity"], refs_drop=[f"{P}[1].important_terms[2]"])


variants = []

# ================================================================ SMALL (target 757, limit 908): the most important blocks only
variants.append({
    "id": "v01", "name": "Quick bonus guide (small, flat)", "tier": "small", "angle": "A player who wants the welcome offer, the terms and the promo code answer in a minute.",
    "skipped_clusters": [SKIP_OV, SKIP_VIP],
    "intent_summary": ("Short brand-subpage for the small size group of the competitors: the Longfu88 welcome bonus with its claiming steps, the terms, the promo code question, the reload, free spin and cashback offers in the fewest words "
                       "for a player from Malaysia. Page voice: short, dense paragraphs of two or three sentences, sentences of about 14 words, facts before comment, no scene-setting, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions: Quick Guide to Bonuses and Promo Code", 50, {K0: 2, KB: 1}),
        blk(["b03", "b04"], 2, "Longfu88 Welcome Bonus and How to Claim It", 140, {K0: 2, KW: 0}, PL, summary="The Casino Welcome Bonus of 188% up to €2,088 plus 18 Free Spins and the four steps to claim it."),
        blk(["b05"], 2, "Terms in Brief", 85, {K0: 1}),
        blk(["b06"], 2, "Promo Code: What to Know", 50, {K0: 1, KC: 1}),
        blk(["b07"], 2, "Weekly and Weekend Reloads", 95, {K0: 1}, PT,
            notes=("One lead-in sentence that says that the reload offers reward repeat deposits, then a TABLE with four columns, offer | reward | minimum deposit | wagering, and three rows in this order: Casino Weekend Reload, "
                   "Casino Weekend Crypto Reload, Casino Double Fortune: One-Day Reload Special (values exactly as in the Brand Information). After the table one sentence: the weekend offers are valid for 7 days and the Double Fortune special "
                   f"for 24 hours, and a reload cannot be combined with another active casino bonus. {NO_INVENT}"),
            refs_drop=rrefs(3) + [f"{P}[4].important_terms[2]"], refs_add=[f"{P}[4].important_terms[1]"]),
        blk(["b08"], 2, "Free Spins", 60, {K0: 1}),
        blk(["b09"], 2, "Weekly Cashback", 80, {K0: 1}, edit=[(B09_REBATES, "Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback) in one sentence. "), (B09_VIPNOTE, "")],
            refs_drop=B09_REBATES_DROP),
        blk(["b11"], 2, "Longfu88 Offers: Quick Answers", 80, {K0: 1}, **faq(["mindep", "one", "valid", "support"])),
    ],
})

variants.append({
    "id": "v02", "name": "Welcome first with deposit table (small)", "tier": "small", "angle": "A new player who compares what each offer asks for the first deposit.",
    "skipped_clusters": [SKIP_OV, SKIP_RL, SKIP_VIP],
    "intent_summary": ("Short brand-subpage for the small size group: the Longfu88 welcome bonus first (size, steps, terms), the minimum deposit that each offer asks for in one table, the promo code question, the free spins and the cashback, for a "
                       "player from Malaysia. Page voice: practical and comparative, a one-line verdict after each section, sentences of about 15 words, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Welcome Bonus: Offer, Terms and Promo Code", 50, {K0: 1, KB: 1, KP: 1}, extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        blk(["b03"], 2, "Casino Welcome Bonus: Size and Alternatives", 85, {K0: 2}),
        blk(["b04"], 2, "Claiming Step by Step", 75, {K0: 1}),
        blk(["b05"], 2, "Wagering and Limits", 90, {K0: 1}),
        md("Minimum Deposit by Offer", 75, [-1, 0, 1, 2, 4, 6], {K0: 1}),
        blk(["b06"], 2, "Longfu88 Promo Code: Is One Listed?", 50, {K0: 1},
            edit=[('The phrase "Longfu88 promo code" stands once in the first sentence, which says that the Brand Information of the casino lists no Longfu88 promo code for its offers.',
                   'The first sentence says that the Brand Information of the casino lists no promo code for its offers.')]),
        blk(["b08"], 2, "Where Free Spins Come From", 60, {K0: 1}),
        blk(["b09"], 2, "Cashback Rules", 80, {K0: 1}, edit=[(B09_REBATES, "Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback) in one sentence. "), (B09_VIPNOTE, "")],
            refs_drop=B09_REBATES_DROP),
        blk(["b11"], 2, "Longfu88 Offers: Welcome Questions", 85, {K0: 1}, **faq(["mindep", "excl", "valid", "code", "support"])),
    ],
})

variants.append({
    "id": "v03", "name": "Checklist (small, lists)", "tier": "small", "angle": "A reader who works through a list before depositing.",
    "skipped_clusters": [SKIP_OV, SKIP_VIP],
    "intent_summary": ("Checklist-style short brand-subpage for the small size group: what to check before claiming the Longfu88 welcome bonus in Malaysia, the claiming steps, the reload and free spin offers in one table, the cashback, the "
                       "rewards area and a few questions. Page voice: terse and scannable, a one-sentence lead-in per section, then a list or a table; sentences of about 12 words; no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions Checklist: Bonuses Before You Claim", 45, {K0: 1, KB: 1, KC: 1},
              extra='Where the phrase "Longfu88 promo code" is used it stands in the sentence that signposts the topics and says that the Brand Information lists no such code.'),
        ck("Before You Claim: Seven Checks", 85, {K0: 1}),
        blk(["b03"], 2, "Casino Welcome Bonus in Short", 70, {K0: 1, KW: 1},
            extra='Where the phrase "Longfu88 welcome bonus" is used it stands in the first sentence.'),
        blk(["b04"], 2, "Claim Steps", 70, {K0: 1}),
        blk(["b07", "b08"], 2, "Reload and Free Spin Offers at a Glance", 125, {K0: 1}, PT,
            notes=("This block covers two topics in ONE continuous section without sub-headings. One lead-in sentence that says that the reload and free spin offers reward repeat deposits, then a TABLE with four columns, offer | reward | "
                   "minimum deposit | wagering, and three rows in this order: Casino Weekly Reload, Casino Weekend Reload, Casino Double Fortune: One-Day Reload Special (values exactly as in the Brand Information). After the table two sentences: "
                   "the weekly and weekend offers are valid for 7 days and the Double Fortune special for 24 hours; a reload cannot be combined with another active casino bonus. "
                   f"{NO_INVENT}"),
            refs_drop=rrefs(3, 5) + [f"{P}[7].name", f"{P}[7].reward", f"{P}[7].minimum_deposit", f"{P}[7].wagering_requirement", f"{W}.free_spins_wagering", f"{P}[4].important_terms[2]"],
            summary="Three reload offers with reward, minimum deposit and wagering, including the 50 Free Spins of the Weekly Reload."),
        blk(["b09"], 2, "Cashback in Brief", 70, {K0: 1}, edit=[(B09_REBATES, "Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback) in one sentence. "), (B09_VIPNOTE, "")],
            refs_drop=B09_REBATES_DROP),
        blk(["b10"], 2, "Rewards Area at a Glance", 60, {K0: 1}),
        blk(["b11"], 2, "Longfu88 Offers: Checklist Questions", 75, {K0: 1}, **faq(["code", "mindep", "wd", "support"])),
    ],
})

# ================================================================ MEDIUM (target 1029, limit 1235): the base ТЗ, differently composed
variants.append({
    "id": "v04", "name": "Newcomer path with deposit table", "tier": "medium", "angle": "A new player who has not claimed a bonus before and wants one guided path.",
    "skipped_clusters": [SKIP_OV, SKIP_VIP],
    "intent_summary": ("Step-by-step brand-subpage for a newcomer to the Longfu88 bonuses in Malaysia: how the welcome offer works, how to claim it, the terms before depositing, the minimum deposit of every offer in one table, the promo code question, "
                       "the reload, free spin and cashback offers and the rewards area. Page voice: a patient guide, \"first, then\" logic, sentences of about 17 words, one plain consequence after each term; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Welcome Bonus and Promotions for New Players", 65, {K0: 2, KB: 1, KP: 1}, extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        blk(["b03"], 2, "How the Welcome Offer Works", 90, {K0: 2}),
        blk(["b04"], 2, "Claim It in Four Steps", 80, {K0: 2}),
        blk(["b05"], 2, "Terms to Read Before You Deposit", 110, {K0: 1}),
        md("Minimum Deposit of Every Offer", 90, [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], {K0: 1}),
        blk(["b06"], 2, "Longfu88 Promo Code: Is One Listed Today?", 55, {K0: 1},
            edit=[('The phrase "Longfu88 promo code" stands once in the first sentence, which says that the Brand Information of the casino lists no Longfu88 promo code for its offers.',
                   'The first sentence says that the Brand Information of the casino lists no promo code for its offers.')]),
        blk(["b07"], 2, "Reload Offers for Your Next Deposits", 120, {K0: 2}),
        blk(["b08"], 2, "Free Spin Offers", 70, {K0: 1}),
        blk(["b09"], 2, "Cashback and Rebates", 105, {K0: 2}),
        blk(["b10"], 2, "Rewards Area for Active Players", 70, {K0: 2}),
        blk(["b11"], 2, "Longfu88 Offers for Newcomers: FAQ", 95, {K0: 1}, **faq(["mindep", "one", "code", "valid", "cb", "support"])),
    ],
})

variants.append({
    "id": "v05", "name": "Crypto and live casino focus", "tier": "medium", "angle": "A player who deposits in crypto or plays live casino and wants the matching offers.",
    "skipped_clusters": [SKIP_VIP],
    "intent_summary": ("Brand-subpage about the Longfu88 offers for crypto and live casino players in Malaysia: the bonus families side by side, the three welcome offers compared, the claiming steps, the crypto offers with the eligible coins, the live casino "
                       "offers, the terms, the reload and free spin offers, the weekly cashback and the questions. Page voice: calm and comparative, the choice first and the numbers after it, sentences of about 16 words; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Offers for Crypto and Live Casino Players", 65, {K0: 2, KB: 1, KP: 1}, extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        blk(["b02"], 2, "Offer Families Compared", 85, {K0: 1}),
        wc("Welcome Bonus Options: Casino, Live and Crypto", 115, {K0: 1, KW: 1},
           ),
        blk(["b04"], 2, "Claiming a Welcome Offer", 75, {K0: 1, KC: 1},
            extra='Where the phrase "Longfu88 promo code" is used it stands in the closing sentence, which says that the Brand Information lists no promo code and that the activation happens in My Bonuses.'),
        cr("Crypto Bonuses and Eligible Coins", 105, {K0: 1}),
        lv("Live Casino Bonuses", 90, {K0: 1}),
        blk(["b05"], 2, "Wagering and Terms of the Main Offer", 100, {K0: 2}),
        blk(["b07", "b08"], 2, "Reload and Free Spin Offers in Euro", 110, {K0: 1}, PT,
            notes=("This block covers two topics in ONE continuous section without sub-headings. One lead-in sentence that says that the euro offers reward repeat deposits, then a TABLE with four columns, offer | reward | minimum deposit | wagering, "
                   "and three rows in this order: Casino Weekly Reload, Casino Weekend Reload, Casino Double Fortune: One-Day Reload Special (values exactly as in the Brand Information). After the table two sentences: the weekly and weekend offers are "
                   f"valid for 7 days and the Double Fortune special for 24 hours; the stake while wagering bonus funds is limited to €5 per spin. {NO_INVENT}"),
            refs_drop=rrefs(3, 5) + [f"{P}[7].name", f"{P}[7].reward", f"{P}[7].minimum_deposit", f"{P}[7].wagering_requirement", f"{W}.free_spins_wagering"],
            summary="Three euro reload offers with reward, minimum deposit and wagering, including the 50 Free Spins of the Weekly Reload."),
        blk(["b09"], 2, "Weekly Cashback and Rebates", 95, {K0: 1}, edit=[("Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback) in one sentence, and the Unlimited Casino Rebate (0.9%) and the Unlimited Live Casino Rebate (1.0%) in one sentence: ",
                                                                         "Then the Unlimited Casino Rebate (0.9%) in one sentence: ")],
            refs_drop=[f"{P}[10].reward", f"{P}[10].wagering_requirement", f"{P}[12].rebate_percentage"]),
        blk(["b11"], 2, "Crypto and Live Offers FAQ", 95, {K0: 1}, **faq(["crypto", "live", "excl", "mindep", "cb", "support"])),
    ],
})

variants.append({
    "id": "v06", "name": "Casino and sports bonuses", "tier": "medium", "angle": "A player who bets on sports as well as plays casino and wants both bonus sets.",
    "skipped_clusters": [SKIP_OV, SKIP_VIP],
    "intent_summary": ("Brand-subpage about the Longfu88 bonuses for casino and sports players in Malaysia: the welcome bonus and its activation, the terms, the promo code check, the reload, free spin and cashback offers, the unlimited rebates and the "
                       "sports bonuses with the odds they need. Page voice: sober and exact, every number tied to the offer it belongs to, sentences of about 18 words with a few shorter ones; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions for Casino and Sports Players", 65, {K0: 2, KB: 1}),
        blk(["b03"], 2, "Casino Welcome Bonus in Brief", 80, {K0: 1, KW: 1}, extra='Where the phrase "Longfu88 welcome bonus" is used it stands in the first sentence.'),
        blk(["b04"], 2, "Activate the Offer in My Bonuses", 75, {K0: 1}),
        blk(["b05"], 2, "Wagering, Maximum Bet and Cashout", 100, {K0: 2}),
        blk(["b06"], 2, "Promo Code Check", 55, {K0: 1, KC: 1}),
        blk(["b07"], 2, "Reload Bonuses Week by Week", 120, {K0: 2}),
        blk(["b08"], 2, "Free Spins with Their Own Wagering", 70, {K0: 1}),
        blk(["b09"], 2, "Weekly and Live Casino Cashback", 90, {K0: 2}, edit=[(B09_REBATES, "Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback) in one sentence. ")],
            refs_drop=B09_REBATES_DROP),
        rb("Unlimited Rebates by Game Category", 60, kw={K0: 1}),
        sp("Sports Betting Bonuses", 140, (0, 2, 3), {K0: 2}),
        blk(["b11"], 2, "Longfu88 Offers: Casino and Sports Questions", 95, {K0: 1}, **faq(["mindep", "sport", "one", "reload", "cap", "support"])),
    ],
})

variants.append({
    "id": "v07", "name": "Terms, verification and responsible use", "tier": "medium", "angle": "A cautious player who wants to know the rules before accepting an offer.",
    "skipped_clusters": [SKIP_FS, SKIP_VIP],
    "intent_summary": ("Terms-led brand-subpage about the Longfu88 bonuses in Malaysia for a cautious reader: the offer families, the welcome bonus and its claiming steps, the wagering and the rules that can cost a bonus, verification before bonus winnings, the "
                       "reload and seasonal offers, the cashback and the responsible use of bonuses. Page voice: sober and exact, every claim tied to a stated term, sentences of about 18 words, no reassurance beyond the facts; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Bonus Terms to Check Before You Claim", 65, {K0: 2, KB: 1, KP: 1}, extra='Where the phrase "Longfu88 promotions" is used it stands in the sentence that signposts the topics.'),
        blk(["b02"], 2, "The Offers and Their Rules at a Glance", 80, {K0: 1}),
        blk(["b03"], 2, "The Welcome Offer", 85, {K0: 1}),
        blk(["b04"], 2, "Claiming Without Losing Eligibility", 75, {K0: 1, KC: 1},
            extra='Where the phrase "Longfu88 promo code" is used it stands in the closing sentence, which says that the Brand Information lists no promo code and that the activation happens in My Bonuses.'),
        blk(["b05"], 2, "Longfu88 Welcome Bonus Terms and Wagering", 110, {K0: 2}),
        vf("Verification Before Bonus Winnings", 85, {K0: 1}),
        blk(["b07"], 2, "Reload Offers and Their Conditions", 115, {K0: 1}),
        se("Seasonal and Limited-Time Campaigns", 85, {K0: 1}),
        blk(["b09"], 2, "Cashback Conditions", 95, {K0: 2}),
        rg("Using Bonuses Responsibly", 70, {K0: 1}),
        blk(["b11"], 2, "Longfu88 Offers and Terms: Frequently Asked Questions", 95, {K0: 1}, **faq(["wd", "ver", "excl", "one", "age", "support"])),
    ],
})

# ================================================================ LARGE (limit 2544 = the mean of the group): the base plus every topic the knowledge base can fill
variants.append({
    "id": "v08", "name": "Complete bonus handbook (large)", "tier": "large", "angle": "A reader who wants every bonus, term and rule of the casino on one page.",
    "skipped_clusters": [SKIP_VIP],
    "intent_summary": ("Complete brand-subpage for the large size group of the competitors, built like the longest bonus page of the query: a handbook of the Longfu88 bonuses for players from Malaysia with the offer families, the welcome bonus with its steps "
                       "and terms, the promo code question, the minimum deposits, the reload, free spin, seasonal, crypto and live casino offers, the cashback with the rates by VIP level, the rebates, the rewards area, the sports bonuses, verification, "
                       "responsible use and mobile access, and a long FAQ. Page voice: reference-like, each H2 opens with what the section is for, sentences of about 18 words, a consequence after each condition. Every section is written only from the facts "
                       "of its Brand Information; where a section has few facts it stays short. H2 sections with H3 details." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Promotions Handbook: Every Bonus, Term and Promo Code", 70, {K0: 2, KB: 1}),
        blk(["b02"], 2, "All Bonus Families in One Place", 100, {K0: 1}),
        wc("Longfu88 Welcome Bonus: The Main Offer and Its Alternatives", 115, {K0: 2, KW: 0}),
        blk(["b04"], 3, "How to Claim the Casino Welcome Bonus", 85, {K0: 1}),
        blk(["b05"], 3, "Wagering and Rules of the Welcome Bonus", 120, {K0: 1}),
        blk(["b06"], 2, "Is There a Promo Code?", 65, {K0: 1, KC: 1}),
        md("Minimum Deposit of Every Offer at a Glance", 95, [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], {K0: 1}),
        blk(["b07"], 2, "Reload Bonuses: Weekly, Weekend and One-Day", 125, {K0: 1}),
        blk(["b08"], 2, "Free Spins: Weekly Reload and Seasonal Offers", 75, {K0: 1}),
        se("Seasonal and Verification Campaigns", 90, {K0: 1}),
        cr("Crypto Welcome and Reload Offers with USDT", 100, {K0: 1}),
        lv("Offers for Live Dealer Games", 85, {K0: 1}),
        blk(["b09"], 2, "Cashback: Weekly, Live and by VIP Level", 130, {K0: 2}, PT,
            edit=[(B09_REBATES, "Then the Live Casino Cashback (25% up to €850, wagering 10x the credited cashback) in one sentence. "), (B09_VIPNOTE, "After the paragraph a TABLE with three columns, VIP level | cashback percentage | maximum, and five rows (VIP Bronze 2% €1,888; VIP Silver 4% €2,388; VIP Gold 6% €2,988; VIP Platinum 8% €3,988; VIP Diamond 10% €6,988) as in the Brand Information. "
                                 "Say in one clause that the VIP Program has its own page. ")],
            refs_add=[f"{P}[9].cashback_by_vip"], refs_drop=B09_REBATES_DROP),
        rb("Unlimited Rebates", 55, level=3, kw={K0: 1}),
        blk(["b10"], 2, "Rewards Area: Bonus Crab, Wheel of Fortune and Coin Shop", 80, {K0: 1}),
        sp("Sportsbook Offers and Qualifying Odds", 150, (0, 1, 2, 3), {K0: 1}),
        vf("Documents and Checks Before Payout", 80, {K0: 1}),
        rg("Bonus Terms and Safer Play", 65, {K0: 1}),
        mb("Claiming Bonuses on a Phone", 50, {K0: 1}),
        blk(["b11"], 2, "Longfu88 Offers: Complete FAQ", 155, {K0: 1}, **faq(["mindep", "code", "one", "excl", "wd", "ver", "cb", "coin"])),
    ],
})

intrinsic = {}
blueprint = {"base_run": "longfu88-bonus-my", "brand_names": ["Longfu88 Welcome Bonus", "Longfu88 Promotions", "Longfu88 Offers", "Longfu88 Promo Code", "Longfu88"], "keyword_labels": {},
             "intrinsic": intrinsic, "variants": variants}

heads = [b["heading"].lower() for v in variants for b in v["blocks"]]
dup = {h for h in heads if heads.count(h) > 1}
assert not dup, dup
out = Path("input/variants/longfu88-bonus-my.json")
out.write_text(json.dumps(blueprint, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(variants), "variants")
