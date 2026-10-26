"""Builds input/variants/longfu88-sg.json and longfu88-my.json: 10 brief variants per GEO from the base runs longfu88-sg / -my."""
import json
import random
import sys
from collections import Counter

K = dict(L="Longfu88", L2="Longfu 88", LC="Longfu88 casino", LL="Longfu88 login", LB="Longfu88 bonus", LA="Longfu88 app",
         LP="Longfu88 promo code", L2C="Longfu 88 casino", CL="casino Longfu88", LW="Lngfu88 withdrawal time",
         LO="Longfu 88 Official Site", LF="Longfu", LS="Longfu sports", LCL="Longfu caino login")

CFG = {
    "brand_names": ["Longfu88 Casino", "Longfu88"],
    "keyword_labels": {
        "Longfu88 casino": "\"Longfu88 casino\" (written as the name Longfu88 Casino)",
        "Longfu 88 casino": "\"Longfu 88 casino\" (written as the name Longfu 88 Casino, with a space)",
        "Longfu 88": "\"Longfu 88\" (written with a space)",
        "Lngfu88 withdrawal time": "\"Lngfu88 withdrawal time\" (verbatim, with this spelling)",
        "Longfu caino login": "\"Longfu caino login\" (verbatim, with this spelling)",
    },
    "intrinsic": {
        "b02": {"keyword": "Longfu88", "count": 1, "replace": [[", which is the one occurrence this block allows; no other tracked keyword here.", "."]],
                "note": "The Support row prints the e-mail address exactly as given; it contains the tracked keyword \"Longfu88\", which counts toward the exact count of this block."},
        "b15": {"keyword": "Longfu88", "count": 1, "replace": [["; the name is the one occurrence of \"Longfu88\" of this block)", ")"]],
                "note": "The name of the exclusive game \"Longfu88 Baccarat\" contains the tracked keyword \"Longfu88\"; it is part of the exact count of this block."},
        "b22": {"keyword": "Longfu88", "count": 2, "drop_prefix": "Step one of the",
                "note": "Step one of the Android list and of the iOS list names the brand as in the Brand Information; these two occurrences of \"Longfu88\" are part of the exact count of this block, the rest goes into the running text."},
        "b24": {"keyword": "Longfu88", "count": 1, "replace": [[" and is the one occurrence of \"Longfu88\" of this block)", ")"]],
                "note": "The e-mail address contains the tracked keyword \"Longfu88\"; it is part of the exact count of this block."},
    },
}

# ---------------------------------------------------------------- edits of the base notes (format toggles, cross-references)
E = {
    "b06_prose": ("as a compact bulleted list (identity:", "in one running sentence (identity:"),
    "b08_list": ("then a Markdown table Condition | Value with the rows:", "then a bulleted list, one condition per item (the condition in bold, then its value), with these items:"),
    "b08_prose": ("then a Markdown table Condition | Value with the rows:", "then, in two flowing sentences without a table, the conditions:"),
    "b09_list": ("then a Markdown table Offer | Reward | Min. deposit | Wagering | Validity for the seven offers as given:",
                 "then a bulleted list with one bullet per offer (the name in bold, then reward, minimum deposit, wagering and validity) for the seven offers as given:"),
    "b09_prose": ("then a Markdown table Offer | Reward | Min. deposit | Wagering | Validity for the seven offers as given:",
                  "then, in flowing text without a table, the key figures of the seven offers as given:"),
    "b10_prose": ("shown as a compact table of tier, percentage and maximum)", "given in one sentence as tier, percentage and maximum)"),
    "b11_list": ("Describe the five features in short sentences as given:", "Give the five features as a bulleted list (the name in bold, then one short sentence) as given:"),
    "b12_prose": ("Show a compact table Level | Points | Reward | Cashback | Withdrawal limit for levels 1, 5, 10, 15, 20 and 25 exactly as given in the Brand Information (level 1: 1 point, €9.8, 1%, €9,800; level 25: 5,500 points, €980, 10%, €147,000).",
                  "Give level 1 and level 25 in two sentences exactly as in the Brand Information (level 1: 1 point, €9.8, 1%, €9,800; level 25: 5,500 points, €980, 10%, €147,000), without a table."),
    "b13_list": ("in flowing text and lead into", "as a compact bulleted list, one short phrase each, then lead into"),
    "b13_merge": (" and lead into the sub-sections on slots, live casino and the other categories without retelling their facts.",
                  " and cover slots, live casino and the other categories in this same block."),
    "b16_list": ("Describe each category in a sentence as a type of game only (what the player does):",
                 "Give each category as a bullet (the name in bold, then one short sentence) as a type of game only (what the player does):"),
    "b17_list": ("in a running sentence or two, exactly as given:", "as a compact bulleted list, names only, exactly as given:"),
    "b19_list": ("Give a compact table Offer | Reward | Min. deposit | Wagering for the Sport First Deposit Bonus",
                 "Give a bulleted list with one bullet per offer (the name in bold, then reward, minimum deposit and wagering) for the Sport First Deposit Bonus"),
    "b19_prose": ("Give a compact table Offer | Reward | Min. deposit | Wagering for the Sport First Deposit Bonus",
                  "Without a table, give in flowing text the Sport First Deposit Bonus"),
    "b21_prose": ("the six steps as a NUMBERED list", "the six steps in two flowing sentences without a list"),
    "b22_table": ("as two short numbered lists, each preceded by one sentence",
                  "as one Markdown table Step | Android (Chrome) | iOS (Safari) with three rows, one per step, preceded by one sentence"),
    "b23_prose": ("Give the organisations GamCare, Gamblers Anonymous and Gambling Therapy as a short bulleted list.",
                  "Name the organisations GamCare, Gamblers Anonymous and Gambling Therapy in one sentence."),
    "b13_slots": (" and lead into the sub-sections on slots, live casino and the other categories without retelling their facts.",
                  " and lead into the slots part of this block; live casino and the other categories follow in the next section."),
    "b05_prev": (" Do not mention the identity-document check here (next sub-section).", " Do not mention the identity-document check here (it has its own section)."),
    "b04_own": (" Do not repeat identity-check details (next section).", " Do not repeat identity-check details (they have their own section)."),
    "b03_later": (" Do not repeat the licence or bonus details (later sections).", ""),
    "b05_next": (" Do not mention the identity-document check here (next sub-section).", ""),
    "b07_next": ("Do not explain wagering, maximum bet or validity here (next sub-section).",
                 "Wagering, maximum bet and validity belong to the terms part of this block."),
}
# formats after a toggle
FMT = {"b06_prose": ["paragraph"], "b08_list": ["paragraph", "list"], "b08_prose": ["paragraph"], "b09_list": ["paragraph", "list"],
       "b09_prose": ["paragraph"], "b10_prose": ["paragraph"], "b11_list": ["list"], "b12_prose": ["paragraph"], "b13_list": ["paragraph", "list"],
       "b16_list": ["paragraph", "list"], "b17_list": ["list"], "b19_list": ["paragraph", "list"], "b19_prose": ["paragraph"],
       "b21_prose": ["paragraph"], "b22_table": ["paragraph", "table"], "b23_prose": ["paragraph"]}


# ---------------------------------------------------------------- FAQ
ITEMS = {
    "bonus": ("how to claim the Casino Welcome Bonus (activate it in My Bonuses after the first qualifying deposit of €50; the claiming procedure has no promo code step)",
              ["brandinfo_welcome.welcome_bonus.claiming_procedure", "brandinfo_welcome.welcome_bonus.minimum_deposit"]),
    "mindep": ("what the minimum deposit is (€10 in general, €50 for the Casino Welcome Bonus)",
               ["brandinfo_general.minimum_deposit", "brandinfo_welcome.welcome_bonus.minimum_deposit"]),
    "wtime": ("how long a withdrawal takes (card, crypto and wallet withdrawals 1 to 3 business days; bank transfer up to 3 business days of casino processing plus 3 to 5 business days of bank delivery; the wording must differ from the withdrawals section)",
              ["brandinfo_withdrawal.withdrawal_methods[0].transaction_speed", "brandinfo_withdrawal.withdrawal_methods[1].transaction_speed"]),
    "pwd": ("how to recover a forgotten password (Forgot Password on the login screen, reset link by e-mail)", ["brandinfo_account.login.password_recovery"]),
    "app": ("whether there is an app (no download is described: the casino is a responsive website that can be added to the home screen on Android and iOS)",
            ["brandinfo_app.app_information.platforms", "brandinfo_app.app_information.mobile_access"]),
    "verify": ("how long identity verification takes (up to 10 days after a complete document set; up to 30 days to send the documents when requested)",
               ["brandinfo_account.verification.typical_review_time", "brandinfo_account.verification.document_submission_window"]),
    "twoacc": ("whether a player may have more than one account (no: one personal account per player, and the account must be registered with accurate information)",
               ["brandinfo_account.registration.eligibility"]),
    "cashback": ("how the Casino Weekly Cashback works (up to 10% of weekly net casino losses, capped at €6,988; opt-in; credited to My Bonuses on Monday and activated there)",
                 ["brandinfo_promotions.other_bonuses[9].reward", "brandinfo_promotions.other_bonuses[9].crediting"]),
    "crypto": ("which cryptocurrencies can be used (for deposits Bitcoin, Ethereum, Litecoin, Ripple, USDC, Bitcoin Cash, Cardano and USDT on three networks)",
               ["brandinfo_general.payment_methods.deposit"]),
    "currency": ("which account currencies exist (EUR, USD, MYR, THB, SGD and USDT)", ["brandinfo_general.currencies"]),
    "sports": ("which sports can be bet on (football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football)",
               ["brandinfo_sportsbook.sportsbook.sports_available"]),
    "sportbonus": ("what the first sports deposit bonus is (Sport First Deposit Bonus, 100% up to €1,888, minimum deposit €50, 8x wagering, 30 days)",
                   ["brandinfo_sportsbook.sportsbook.sports_bonuses[0]"]),
    "langs": ("which languages support speaks (English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese)", ["brandinfo_general.customer_support.languages"]),
    "age": ("who may play (at least 18 years old and legally permitted to gamble in the place of residence)", ["brandinfo_general.minimum_age"]),
    "vip": ("how the VIP levels are reached (VIP points from eligible real-money play unlock 25 numbered levels)",
            ["brandinfo_loyalty.loyalty_vip_program.progression"]),
    "wager": ("what wagering applies to the welcome bonus (25x deposit plus bonus, 40x on free spin winnings, 10 days, maximum bet €22.5 per spin)",
              ["brandinfo_welcome.welcome_bonus.wagering_requirement", "brandinfo_welcome.welcome_bonus.free_spins_wagering", "brandinfo_welcome.welcome_bonus.validity",
               "brandinfo_welcome.welcome_bonus.maximum_bet"]),
    "cryptobonus": ("what the Casino Crypto Welcome Bonus is (188% up to 2,888 USDT, minimum deposit 50 USDT, 40x deposit plus bonus, 10 days; an alternative to the Casino Welcome Bonus, not an addition)",
                    ["brandinfo_promotions.other_bonuses[1]"]),
    "fees": ("whether withdrawals carry fees (no standard casino fee; provider and blockchain fees may apply; a 10% commission with a minimum of €2.25 can apply where turnover is below the deposit, and 15% on some card or bank funded transactions)",
             ["brandinfo_privacy_policy.terms_conditions.conditional_fees"]),
}
BASE_FAQ_REFS = ["brandinfo_account.login.password_recovery", "brandinfo_general.minimum_deposit", "brandinfo_welcome.welcome_bonus.claiming_procedure"]
SHORT = {"bonus": "claiming the bonus", "mindep": "minimum deposit", "wtime": "withdrawal time", "pwd": "password recovery", "app": "the app question",
         "verify": "verification time", "twoacc": "one account", "cashback": "weekly cashback", "crypto": "cryptocurrencies", "currency": "currencies",
         "sports": "sports covered", "sportbonus": "the sports bonus", "langs": "support languages", "age": "who may play", "vip": "VIP levels",
         "wager": "wagering", "fees": "withdrawal fees", "cryptobonus": "the crypto welcome bonus"}


def faq(keys, plc):
    """plc: {item key: [("q"|"a", kw key), ...]} -> block spec fields."""
    parts = []
    cnt = Counter()
    for i, k in enumerate(keys, 1):
        txt = f"({i}) {ITEMS[k][0]}"
        for where, kk in plc.get(k, []):
            cnt[K[kk]] += 1
            txt += f"; the {'question' if where == 'q' else 'answer'} contains the keyword \"{K[kk]}\" exactly once, written verbatim"
        parts.append(txt)
    refs = []
    for k in keys:
        refs += [r for r in ITEMS[k][1] if r not in refs]
    notes = (f"A bulleted list of exactly {len(keys)} items, each a bold question followed by a short answer of 20-30 words, in this order: " + "; ".join(parts) +
             ". The brand name \"Longfu88\" may stand in an answer, never in a question. These are the only questions on the page; the questions are the one place where question form is allowed.")
    return dict(notes=notes, kw=dict(cnt), refs_add=[r for r in refs if r not in BASE_FAQ_REFS], refs_drop=[r for r in BASE_FAQ_REFS if r not in refs],
                kw_lists_ok=True, formats=["list"], words=28 * len(keys) + 12,
                summary="Short answers on " + ", ".join(SHORT[k] for k in keys) + ".")


def rotate(keys, geo, shift=1):
    return keys if geo == "sg" else keys[shift:] + keys[:shift]


# ---------------------------------------------------------------- helpers
def parse_kw(s):
    out = {}
    for tok in s.split():
        a, n = tok.split("=")
        out[K[a]] = int(n)
    return out


def merged_summary(ids, base):
    return " ".join(base[i]["summary"] for i in ids)


class Ctx:
    def __init__(self, geo):
        self.geo = geo
        self.sg = geo == "sg"
        self.name = "Singapore" if self.sg else "Malaysia"


def OTH(label, *refs):
    return {"key": "other", "label": label, "kb_refs": list(refs)}


MINAGE = OTH("Minimum age", "brandinfo_general.minimum_age")
SPORTS = OTH("Sports", "brandinfo_sportsbook.sportsbook.sports_available")
PROVIDERS = OTH("Game providers", "brandinfo_games.providers")
GTYPES = OTH("Game types", "brandinfo_games.game_types")
VIPT = OTH("VIP tiers", "brandinfo_loyalty.loyalty_vip_program.tiers")
WAGERROW = OTH("Wagering", "brandinfo_welcome.welcome_bonus.wagering_requirement")
VERIFY = OTH("Verification time", "brandinfo_account.verification.typical_review_time")
MOBILE = OTH("Mobile access", "brandinfo_app.app_information.platforms")
SPBONUS = OTH("Sports bonus", "brandinfo_sportsbook.sportsbook.sports_bonuses[0].reward")
WLIMITS = OTH("Withdrawal limits", "brandinfo_withdrawal.withdrawal_methods[3].minimum", "brandinfo_withdrawal.withdrawal_methods[3].maximum")
CRYPTOB = OTH("Crypto bonus", "brandinfo_promotions.other_bonuses[1].reward")
PAYOUT = OTH("Payout speed", "brandinfo_withdrawal.withdrawal_methods[1].transaction_speed")

ROWS = {
    1: (["licence", "company", "welcome_bonus", "min_deposit", "cashback", "payment_methods", "currencies", "languages", "support"],
        ["company", "licence", "welcome_bonus", "cashback", "min_deposit", "payment_methods", "currencies", "languages", "support"]),
    2: (["welcome_bonus", WAGERROW, "min_deposit", "cashback", "licence", "company", "founded", "payment_methods", "currencies", "languages", "support"],
        ["welcome_bonus", "cashback", WAGERROW, "min_deposit", "licence", "founded", "payment_methods", "currencies", "languages", "company", "support"]),
    3: (["company", "founded", "licence", "languages", "currencies", "payment_methods", "min_deposit", "welcome_bonus", "cashback", MINAGE, "support"],
        ["founded", "company", "licence", MINAGE, "currencies", "languages", "payment_methods", "min_deposit", "welcome_bonus", "cashback", "support"]),
    4: (["licence", "company", "founded", MINAGE, "languages", "currencies", "payment_methods", "welcome_bonus", "min_deposit", "cashback", VERIFY, "support"],
        ["licence", "company", MINAGE, "founded", "currencies", "languages", "payment_methods", "min_deposit", "welcome_bonus", "cashback", VERIFY, "support"]),
    5: (["licence", "welcome_bonus", "cashback", "company", "founded", "languages", "currencies", "payment_methods", GTYPES, PROVIDERS, "support"],
        ["licence", "company", "welcome_bonus", "cashback", "founded", GTYPES, PROVIDERS, "languages", "currencies", "payment_methods", "support"]),
    6: (["licence", "company", "welcome_bonus", "cashback", "currencies", "languages", "payment_methods", SPORTS, SPBONUS, "min_deposit", "support"],
        ["company", "licence", SPORTS, SPBONUS, "welcome_bonus", "cashback", "min_deposit", "payment_methods", "currencies", "languages", "support"]),
    7: (["company", "licence", "payment_methods", "currencies", "min_deposit", WLIMITS, PAYOUT, "welcome_bonus", "cashback", "languages", "support"],
        ["licence", "company", "currencies", "payment_methods", "min_deposit", PAYOUT, WLIMITS, "welcome_bonus", "cashback", "languages", "support"]),
    8: (["licence", "welcome_bonus", "min_deposit", "payment_methods", "currencies", "languages", "cashback", MOBILE, "support"],
        ["licence", "min_deposit", "welcome_bonus", "payment_methods", MOBILE, "currencies", "languages", "cashback", "support"]),
    9: (["company", "founded", "licence", "languages", "currencies", "payment_methods", "welcome_bonus", "cashback", "min_deposit", MINAGE, VIPT, "support"],
        ["company", "licence", "founded", "currencies", "languages", "payment_methods", "welcome_bonus", "min_deposit", "cashback", VIPT, MINAGE, "support"]),
    11: (["licence", "company", "founded", "welcome_bonus", "cashback", VIPT, "min_deposit", "payment_methods", "currencies", "languages", "support"],) * 2,
    12: (["licence", "company", "payment_methods", "currencies", CRYPTOB, "welcome_bonus", "min_deposit", "cashback", "languages", "support"],) * 2,
    10: (["company", "founded", "licence", "languages", "currencies", "payment_methods", "welcome_bonus", "cashback", "min_deposit", MINAGE, PROVIDERS, SPORTS, VIPT, "support"],
         ["licence", "company", "founded", "currencies", "languages", "payment_methods", "welcome_bonus", "cashback", "min_deposit", MINAGE, SPORTS, PROVIDERS, VIPT, "support"]),
}

# keyword placements inside the FAQ per archetype: {item: [(where, kw)]}
FAQ = {
    1: (["bonus", "mindep", "wtime", "pwd"], {"pwd": [("q", "L2")], "bonus": [("a", "L")]}),
    2: (["bonus", "wager", "cashback", "vip", "wtime", "fees"], {"bonus": [("q", "LP")], "wtime": [("q", "LW")], "vip": [("a", "L")]}),
    3: (["age", "mindep", "bonus", "verify", "pwd"], {"pwd": [("q", "LL")], "age": [("a", "L")]}),
    4: (["verify", "twoacc", "fees", "wtime", "age"], {"verify": [("q", "L2")], "fees": [("a", "L")]}),
    5: (["mindep", "bonus", "crypto", "app", "currency"], {"app": [("q", "LA")], "crypto": [("a", "L")]}),
    6: (["sports", "sportbonus", "mindep", "wtime", "langs"], {"sports": [("q", "LS")], "mindep": [("a", "L")]}),
    7: (["mindep", "crypto", "currency", "wtime", "fees"], {"wtime": [("q", "LW")], "crypto": [("a", "L")]}),
    8: (["app", "pwd", "bonus", "wtime"], {"pwd": [("q", "LL")], "bonus": [("q", "LP")], "wtime": [("a", "L")]}),
    9: (["bonus", "mindep", "verify", "twoacc", "app", "wtime"], {"bonus": [("q", "LP")], "app": [("q", "LA")], "wtime": [("q", "LW")], "verify": [("a", "L")]}),
    10: (["bonus", "wager", "wtime", "cashback", "vip", "pwd"], {"pwd": [("q", "L2")], "bonus": [("a", "L")]}),
    11: (["vip", "cashback", "bonus", "wager", "mindep"], {"bonus": [("q", "LB")], "vip": [("a", "L")]}),
    12: (["crypto", "cryptobonus", "mindep", "wtime", "fees"], {"crypto": [("a", "L")], "fees": [("q", "L2")]}),
}


# ---------------------------------------------------------------- archetypes
def spec(ids, lvl, head, w, kw="", fmt=None, edit=(), extra=None, summary=None, **more):
    d = dict(ids=ids, lvl=lvl, head=head, w=w, kw=parse_kw(kw), fmt=fmt, edit=[E[e] if isinstance(e, str) else e for e in edit],
             extra=extra, summary=summary, more=more)
    return d


def toggles(*names):
    """formats and edits of a block after the given format toggles (formats = result of the LAST toggle)."""
    return dict(edit=list(names), fmt=FMT[names[-1]] if names else None)


def arch(n, c):
    s = c.sg
    h = lambda a, b: a if s else b
    nm = c.name
    T = {}
    if n == 1:
        T.update(
            name=h("Quick verdict (compact, flat)", "Fast read (compact, flat)"),
            angle="A reader who wants the verdict and the numbers fast.",
            twist=True,
            intent=(f"Compact brand-review page about the Longfu88 online casino for players from {nm}, built for a reader who wants the verdict and the numbers fast: the key facts in one table, the welcome bonus with its terms, promotions and rewards, VIP levels, games and studios, sports betting, sign-up and verification, payments, mobile play, licence and data safety, responsible gambling, support, a short FAQ and a verdict. "
                    f"Page voice: short, dense paragraphs of two to three sentences, sentences of about 14 words with an occasional longer one, every section opens with its most useful figure and ends with what it means for the player, no scene-setting and no hook sentences; calls to action only at the welcome bonus and at the verdict. All sections are flat H2s, no sub-sections. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino in Singapore: Key Facts and Verdict", "Longfu88 Casino in Malaysia: Quick Review and Key Facts"), 65, "L=1"),
                spec(["b02"], 2, h("Key Facts in One Table", "Fast Facts Table"), 0),
                spec(["b07", "b08"], 2, h("Welcome Bonus and Its Terms", "First Deposit Offer and Wagering Rules"), 150, "L=1 LB=1 LP=1", edit=["b07_next"],
                     summary="The Casino Welcome Bonus with its figures, the four claiming steps and the alternative offers, then the wagering, validity and bet limits in a table.",
                     extra="This is the main call-to-action place of the page: one plain invitation to claim the bonus is allowed."),
                spec(["b09", "b10", "b11"], 2, h("Weekly Promotions, Cashback and Rewards", "Reloads, Cashback and Reward Features"), 125, "",
                     summary="The seven reload and seasonal offers in a table, the weekly cashback with VIP rates and the rebates, and the five reward features in short."),
                spec(["b12"], 2, h("VIP Levels", "VIP Club"), 60, "", edit=["b12_prose"], fmt=FMT["b12_prose"]),
                spec(["b13", "b14", "b15", "b16", "b17"], 2, h("Games and Studios", "What You Can Play and Who Supplies It"), 190, "L=1 LC=1 L2C=1", edit=["b13_merge"],
                     summary="The nine game categories, three example slots with RTP, the live section with the exclusive baccarat, the other categories and the ten providers."),
                spec(["b18", "b19"], 2, h("Sports Betting and Sports Offers", "Sportsbook and Sports Promotions"), 115, "L=1 LS=1",
                     summary="Sports and bet types, live betting and the sports bonuses with the shared odds rule."),
                spec(["b05", "b06"], 2, h("Sign-Up, Login and ID Check", "Account Opening, Login and Verification"), 135, "L=1 LL=1 LCL=1", edit=["b05_next"],
                     summary="Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes."),
                spec(["b20", "b21"], 2, h("Deposits and Withdrawals", "Payments: Deposits and Cash-Outs"), 190, "L=1 LW=1",
                     summary="Deposit methods by type with limits and speed in a table, the deposit route, then withdrawal methods, steps, timing and fees."),
                spec(["b22"], 2, h("Playing on Your Phone", "Mobile Play"), 70, "L=2 LA=1"),
                spec(["b03", "b04"], 2, h("Licence, Operator and Data Safety", "Licence and Player Safety"), 130, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected."),
                spec(["b23"], 2, h("Responsible Gambling", "Safer Play Tools"), 70, "", **toggles("b23_prose")),
                spec(["b24"], 2, h("Support Channels", "Customer Service"), 50, "L=1"),
                spec(["b26"], 2, h("Quick Answers", "FAQ in Short"), 0, "", faq_key=1),
                spec(["b27"], 2, h("Final Verdict", "Our Take"), 65, "LF=1 L=1 LC=1",
                     extra="The second call-to-action place: one plain invitation, tied to the welcome bonus."),
            ])
    elif n == 2:
        T.update(
            name=h("Bonus-first (offer-led order, long)", "Offer-led (bonuses before games, long)"),
            angle="A reader who comes for the bonuses and wants the terms behind each figure before registering.",
            twist=True,
            intent=(f"Long brand-review page about the Longfu88 online casino for players from {nm}, ordered around the offer: the fact table, then the welcome bonus with its terms, reloads, cashback, the rewards area, the VIP programme and the sportsbook offer, followed by registration and verification, payments and withdrawals, the game lobby and providers, mobile access, licence and eligibility, responsible gambling, support, a pros and cons table, an FAQ about bonuses and payouts and a closing assessment. "
                    f"Page voice: businesslike and comparative, paragraphs of three to four sentences, sentences of about 18 words; every bonus figure is followed by the condition it depends on (context before the figure, consequence, contrast); calls to action only at the welcome bonus, at the weekly cashback and at the sportsbook offer. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino Review: Bonuses, Games and Payments for Singapore", "Longfu88 Casino Malaysia: Bonuses, Games and Payments Reviewed"), 85, "L=1 LF=0"),
                spec(["b02"], 2, h("Casino Information", "Quick Facts About the Casino"), 0),
                spec(["b07"], 2, h("The Casino Welcome Bonus", "Welcome Bonus for New Players"), 115, "L=1 LB=1",
                     extra="Start from what the bonus is for (a match on the first qualifying deposit), then the figures, and close with the plain invitation to claim it: the first of three call-to-action places of the page."),
                spec(["b08"], 3, h("Wagering, Validity and Maximum Bet", "Terms You Must Meet to Cash Out the Bonus"), 85, ""),
                spec(["b09"], 2, h("Reload Offers and Seasonal Campaigns", "Weekly, Weekend and Seasonal Reloads"), 100, ""),
                spec(["b10"], 3, h("Weekly Cashback and Daily Rebates", "Cashback and Rebate Rates"), 65, "",
                     extra="The second call-to-action place: one plain invitation tied to the weekly cashback."),
                spec(["b11"], 3, h("Bonus Crab, Wheel of Fortune and the Coin Shop", "Rewards Area: Crab, Wheel and Coin Shop"), 60, ""),
                spec(["b12"], 2, h("VIP Programme: Points, Levels and Limits", "VIP Ladder: 25 Levels from Bronze to Diamond"), 90, ""),
                spec(["b18"], 2, h("Sportsbook Offer: Markets and Bonuses", "Sports Betting and Its Bonuses"), 85, "L=1 LS=1"),
                spec(["b19"], 3, h("Sport Bonuses, Cashback and Boosts", "Sports Promotions in Detail"), 65, "",
                     extra="The third call-to-action place: one plain invitation tied to the sports first deposit bonus. Keep it clearly separate from the casino bonus."),
                spec(["b05"], 2, h("Registration and Login", "How to Register and Log In"), 105, "L=1 LL=1 LCL=1"),
                spec(["b06"], 3, h("Verification Before the First Withdrawal", "ID Checks and Document Rules"), 80, ""),
                spec(["b20"], 2, h("Deposit Methods, Limits and Speed", "Payment Options for Deposits"), 105, "L=1"),
                spec(["b21"], 3, h("Withdrawals: Steps, Timing and Fees", "Cashing Out: Steps, Timing and Fees"), 95, "L=1"),
                spec(["b13"], 2, h("Casino Lobby and Game Types", "Game Library at a Glance"), 70, "L=1 L2C=1", edit=[]),
                spec(["b14"], 3, h("Slots with Their RTP", "Slot Examples and Their Numbers"), 80, ""),
                spec(["b15"], 3, h("Live Dealer Section", "Live Casino and Exclusive Baccarat"), 75, "L=1"),
                spec(["b16"], 3, h("Fishing, P2P, Fast Games and Lottery", "Other Game Types: Fishing, P2P, Lottery"), 65, ""),
                spec(["b17"], 2, h("Software Providers", "Studios Behind the Games"), 65, "L2=1"),
                spec(["b22"], 2, h("Mobile Access on Android and iOS", "Playing on Phone and Tablet"), 85, "L=2 LA=1"),
                spec(["b03", "b04"], 2, h("Operator, Licence and Who May Play", "Licence, Operator and Eligibility"), 150, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected."),
                spec(["b23"], 2, h("Responsible Gambling and Self-Exclusion", "Responsible Play and Self-Exclusion Tools"), 90, ""),
                spec(["b24"], 2, h("Customer Support", "Contacting Support"), 60, "L=1"),
                spec(["b25"], 2, h("Pros and Cons", "Pros and Cons at a Glance"), 60, ""),
                spec(["b26"], 2, h("Questions About Bonuses and Payouts", "Bonus and Payout Questions"), 0, "", faq_key=2),
                spec(["b27"], 2, h("Bottom Line on the Offer", "Overall Assessment"), 85, "LC=1 LF=1 L=1"),
            ])
    elif n == 3:
        T.update(
            name=h("Player journey (how-to order)", "Step by step (how-to order)"),
            angle="A new player who wants to know what happens at each stage, from the licence check to the first withdrawal.",
            twist=False,
            intent=(f"Brand-review page about the Longfu88 online casino for players from {nm}, organised as the route of a new player: the basic facts, the licence check, account creation and verification, the first deposit, the welcome bonus and its wagering terms, choosing games, providers, promotions and the VIP programme after the welcome bonus, mobile access, withdrawals, sports betting, responsible gambling, support, short answers to common questions and a summary. "
                    f"Page voice: sequence-driven; each section opens with what the player does at this stage and ends by leading into the next stage, sentences of about 16 words, paragraphs of two to three sentences, the structure of the product described first and then who the feature suits; numbered lists wherever the order of steps matters; calls to action tied to concrete steps (register, deposit, claim). All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino from Sign-Up to Withdrawal: a Singapore Guide", "Longfu88 Casino Step by Step: a Malaysian Player's Guide"), 75, "L=1"),
                spec(["b02"], 2, h("Basics Before You Register", "Facts to Know Before Signing Up"), 0),
                spec(["b03", "b04"], 2, h("Checking the Licence and Operator First", "First Check: Who Runs the Casino"), 140, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected, as the first stage before an account is created."),
                spec(["b05"], 2, h("Creating the Account: Registration and Login", "Registering and Logging In"), 100, "L=1 LCL=1",
                     extra="The numbered list is the centre of the block; the login part follows it in two sentences."),
                spec(["b06"], 3, h("Passing Identity Verification", "Document Checks"), 75, ""),
                spec(["b20"], 2, h("Funding the Account: Deposit Methods", "Paying In: Deposit Methods"), 95, "L=1"),
                spec(["b07"], 2, h("Claiming the Welcome Bonus", "Taking the Welcome Offer"), 105, "L=1 LB=1 LP=1",
                     extra="Tie the plain invitation to a concrete step: register, make the first qualifying deposit of €50, activate the bonus in My Bonuses."),
                spec(["b08"], 3, h("Meeting the Wagering Terms", "Wagering and Expiry"), 80, "", **toggles("b08_list")),
                spec(["b13"], 2, h("Choosing What to Play", "Picking Your Games"), 65, "L=1 LC=1"),
                spec(["b14"], 3, h("Starting with Slots", "Slots"), 70, ""),
                spec(["b15"], 3, h("Moving to the Live Tables", "Live Dealer Tables"), 70, "L=1 L2C=1"),
                spec(["b16"], 3, h("Trying Other Game Types", "Fishing, P2P and More"), 60, "", **toggles("b16_list")),
                spec(["b17"], 2, h("The Studios Supplying the Games", "Game Providers"), 60, "L2=1"),
                spec(["b09"], 2, h("Promotions After the First Deposit", "Ongoing Promotions for Active Players"), 95, "L=1"),
                spec(["b10"], 3, h("Cashback and Rebates", "Getting Money Back: Cashback and Rebates"), 60, ""),
                spec(["b11"], 3, h("Earning Rewards and Coins", "Collecting Rewards"), 55, "", **toggles("b11_list")),
                spec(["b12"], 2, h("Climbing the VIP Levels", "Moving Up in the VIP Programme"), 80, ""),
                spec(["b22"], 2, h("Playing on the Go", "On the Move: Mobile Access"), 75, "L=2 LA=1"),
                spec(["b21"], 2, h("Withdrawing Your Winnings", "Taking Winnings Out"), 90, "L=1 LW=1"),
                spec(["b18"], 2, h("Betting on Sports as Well", "Adding Sports Bets"), 80, "L=1 LS=1"),
                spec(["b19"], 3, h("Sports Bonuses", "Sports Offers"), 60, "", **toggles("b19_list")),
                spec(["b23"], 2, h("Keeping Play Under Control", "Staying in Control"), 75, ""),
                spec(["b24"], 2, h("Getting Help", "Reaching Support"), 55, "L=1"),
                spec(["b26"], 2, h("Common Questions Along the Way", "Frequent Questions from New Players"), 0, "", faq_key=3),
                spec(["b27"], 2, h("Summary for New Players", "Recap for First-Time Players"), 70, "LC=1 LF=1 L=1"),
            ])
    elif n == 4:
        T.update(
            name=h("Safety and control (careful reader, long)", "Safety first (checks before deposit, long)"),
            angle="A careful reader who checks the licence, the terms and the protection tools before depositing.",
            twist=True,
            intent=(f"Detailed brand-review page about the Longfu88 online casino for players from {nm}, written for a careful reader: who runs the casino and under which licence, the fact sheet, registration with account security and verification, the responsible-gambling tools, the welcome bonus with its terms, other promotions and VIP limits, payments with withdrawal timing, the game library, providers, the sportsbook, mobile access, support, a pros and cons table, an FAQ and a closing checklist. "
                    f"Page voice: precise and calm, sentences of about 20 words with a few short ones, paragraphs of three to four sentences; every advantage is followed by the condition or limit that goes with it, stated in the same detail as the advantage; a fact is followed by what it means in practice; one call to action only, at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino Review: Licence, Limits and Player Protection", "Longfu88 Casino Malaysia: Safety, Terms and Controls Reviewed"), 95, "L=1",
                     extra="Open with the licence jurisdiction and the operator as the subject of the first sentence."),
                spec(["b03", "b04"], 2, h("Who Runs the Casino and Under Which Licence", "Operator, Licence and Data Handling"), 160, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator, the data controller and how data and accounts are protected."),
                spec(["b02"], 2, h("Brand Fact Sheet", "Verified Brand Details"), 0),
                spec(["b05"], 2, h("Registration, Login and Account Security", "Registration and Login Safely"), 115, "L=1 LL=1 LCL=1"),
                spec(["b06"], 3, h("Verification: Documents, Timing and Consequences", "How Verification Works and What It Takes"), 105, "L=1"),
                spec(["b23"], 2, h("Responsible Gambling Tools", "Responsible Gambling: Self-Exclusion and Help"), 100, ""),
                spec(["b07"], 2, h("Welcome Bonus and What It Requires", "Welcome Offer and Its Conditions"), 120, "L=1 LB=1 LP=1",
                     extra="Put the claiming rule (activation in My Bonuses, no code step) before the figures. One plain invitation to claim the bonus is the only call to action of the page."),
                spec(["b08"], 3, h("Bonus Conditions in Detail", "Wagering, Caps and Exclusions"), 85, ""),
                spec(["b09"], 2, h("Other Promotions and Their Rules", "Reloads and Seasonal Offers: Rules Included"), 100, "", **toggles("b09_list")),
                spec(["b10"], 3, h("Cashback and Rebate Conditions", "Cashback Conditions"), 65, ""),
                spec(["b12"], 2, h("VIP Programme and Withdrawal Limits", "VIP Levels and Higher Limits"), 90, ""),
                spec(["b20"], 2, h("Payments and Deposit Limits", "Deposit Methods and Their Limits"), 105, "L=1"),
                spec(["b21"], 3, h("Withdrawals, Fees and the Turnover Rule", "Withdrawals: Timing, Fees and Turnover"), 100, "L=1 LW=1"),
                spec(["b13"], 2, h("Game Library", "Games on Offer"), 65, "L=1"),
                spec(["b14"], 3, h("Slots and Their RTP", "Slots: RTP and Volatility"), 80, ""),
                spec(["b15"], 3, h("Live Casino", "Live Dealer Games"), 70, "L=1 L2C=1"),
                spec(["b17"], 2, h("Game Providers", "Providers"), 60, "L2=1"),
                spec(["b18"], 2, h("Sports Betting Rules and Markets", "Sportsbook Markets and Rules"), 85, "L=1 LS=1"),
                spec(["b19"], 3, h("Sports Bonus Conditions", "Sports Promotions"), 65, "", **toggles("b19_prose")),
                spec(["b22"], 2, h("Mobile Access", "Using the Casino on Mobile"), 80, "L=2 LA=1"),
                spec(["b24"], 2, h("Support and How to Reach It", "Support Channels and Languages"), 60, "L=1"),
                spec(["b25"], 2, h("Pros and Cons", "Strengths and Limits"), 60, ""),
                spec(["b26"], 2, h("Questions About Safety and Payouts", "Questions on Verification and Payouts"), 0, "", faq_key=4),
                spec(["b27"], 2, h("Checklist Before You Deposit", "Before You Deposit"), 85, "LC=1 LF=1 L=1"),
            ])
    elif n == 5:
        T.update(
            name=h("Games first (lobby-led)", "Lobby first (games before bonuses)"),
            angle="A reader who wants to see what there is to play before anything else.",
            twist=True,
            intent=(f"Brand-review page about the Longfu88 online casino for players from {nm}, led by the game lobby: the fact table, the game categories with slots, live casino and the other game types, providers, then the welcome bonus and promotions, VIP levels, sports betting, payments, registration, mobile access, licence and safety, responsible gambling, support, an FAQ and a verdict. "
                    f"Page voice: lively but factual, sentences of about 15 words, the reader is addressed as \"you\" now and then, every game category is described by what the player does in it, concrete figures (RTP, volatility, multipliers) come before adjectives, contrasts between game types; paragraphs of two to three sentences; one call to action, at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino Games, Bonuses and Payments: Singapore Review", "Longfu88 Casino Games and Offers: Malaysian Review"), 75, "L=1"),
                spec(["b02"], 2, h("Casino Facts", "Casino Details at a Glance"), 0),
                spec(["b13"], 2, h("Game Lobby", "The Casino Lobby"), 70, "L=1 LC=1", **toggles("b13_list")),
                spec(["b14"], 3, h("Slot Games", "Slots to Know"), 85, ""),
                spec(["b15"], 3, h("Live Dealer Games", "Live Dealer Studio"), 75, "L=1 L2C=1"),
                spec(["b16"], 3, h("Table, Fishing, P2P and Lottery Games", "Fishing, P2P, Fast and Lottery Games"), 70, ""),
                spec(["b17"], 2, h("Game Providers", "Who Makes the Games"), 65, "L2=1", **toggles("b17_list")),
                spec(["b07"], 2, h("Welcome Bonus for Casino Players", "Casino Welcome Offer"), 110, "L=1 LB=1 LP=1"),
                spec(["b08"], 3, h("Welcome Bonus Terms", "Terms of the Welcome Offer"), 80, ""),
                spec(["b09", "b10"], 2, h("Reloads and Cashback", "Reload Offers and Cashback"), 140, "L=1",
                     summary="The seven reload and seasonal offers in a table, then the weekly cashback with VIP rates, the live casino cashback and the rebates."),
                spec(["b11"], 3, h("Rewards Area", "Bonus Crab, Wheel and Coin Shop"), 60, ""),
                spec(["b12"], 2, h("VIP Programme", "VIP Levels and Rewards"), 85, "L=1"),
                spec(["b18"], 2, h("Sports Betting", "Sportsbook"), 80, "L=1 LS=1"),
                spec(["b19"], 3, h("Sports Bonuses", "Sports Offers"), 60, ""),
                spec(["b20", "b21"], 2, h("Payments: Deposits and Withdrawals", "Deposits and Withdrawals"), 190, "L=1 LW=1",
                     summary="Deposit methods by type with limits and speed in a table, the deposit route, then withdrawal methods, steps, timing and fees."),
                spec(["b05", "b06"], 2, h("Registration and Verification", "Registration, Login and Verification"), 135, "L=1 LL=1 LCL=1", edit=["b05_next"],
                     summary="Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes."),
                spec(["b22"], 2, h("Mobile Gaming", "Mobile Access"), 75, "L=2"),
                spec(["b03", "b04"], 2, h("Licence and Security", "Licence, Operator and Data Safety"), 135, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected."),
                spec(["b23"], 2, h("Responsible Gambling", "Responsible Gambling Tools"), 75, ""),
                spec(["b24"], 2, h("Support", "Customer Support"), 55, "L=1"),
                spec(["b26"], 2, h("Game and Account Questions", "Questions Players Ask"), 0, "", faq_key=5),
                spec(["b27"], 2, h("Verdict on the Casino", "Final Word on the Casino"), 70, "LF=1 L=1"),
            ])
    elif n == 6:
        T.update(
            name=h("Sports first (bettor's page)", "Sportsbook first (bettor's page)"),
            angle="A reader who bets on sports first and plays casino games second.",
            twist=True,
            intent=(f"Brand-review page about the Longfu88 sportsbook and online casino for players from {nm}, written for a bettor: the fact table, sports betting with markets, bet types and live betting, the sports bonuses, betting on mobile, registration and verification, payments, then the casino side with the welcome bonus, reloads and cashback, VIP levels, games and providers, licence and safety, responsible betting, support, pros and cons, an FAQ on sports and payouts and a verdict. "
                    f"Page voice: plain betting vocabulary, the reader is addressed as \"you\", sentences of about 17 words, every section starts with the market or the bet the reader makes and ends with the condition that decides the payout; paragraphs of two to four sentences; calls to action at the sports first deposit bonus and at the casino welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Sports and Casino Review for Singapore Players", "Longfu88 Sportsbook and Casino Review for Malaysia"), 75, "L=1",
                     extra="Open with the sportsbook, then the casino areas."),
                spec(["b02"], 2, h("Sports and Casino Facts", "Facts Table"), 0),
                spec(["b18"], 2, h("Sports Betting at the Casino", "Sports Betting Markets"), 90, "L=1"),
                spec(["b19"], 3, h("Sports Bonuses and Boosts", "Sports Bonuses"), 70, "", **toggles("b19_list")),
                spec(["b22"], 2, h("Betting on Mobile", "Mobile Betting and Casino"), 75, "L=2 LA=1"),
                spec(["b05", "b06"], 2, h("Registration, Login and Verification", "Sign-Up and Login"), 135, "L=1 LL=1 LCL=1", edit=["b05_next"],
                     summary="Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes."),
                spec(["b20", "b21"], 2, h("Deposits and Withdrawals", "Payments for Bettors and Players"), 195, "L=1 LW=1",
                     summary="Deposit methods by type with limits and speed in a table, the deposit route, then withdrawal methods, steps, timing and fees."),
                spec(["b07", "b08"], 2, h("Casino Welcome Bonus and Its Terms", "Casino Welcome Offer and Wagering"), 150, "L=1 LB=1 LP=1", edit=["b07_next"],
                     summary="The Casino Welcome Bonus with its figures, claiming steps and alternatives, then the wagering, validity and bet limits in a table.",
                     extra="Keep it clearly separate from the sports bonuses."),
                spec(["b09", "b10"], 2, h("Reloads and Cashback", "Casino Reloads and Cashback"), 135, "L=1",
                     summary="The seven reload and seasonal offers in a table, then the weekly cashback with VIP rates, the live casino cashback and the rebates."),
                spec(["b12"], 2, h("VIP Programme", "VIP Levels"), 80, "", **toggles("b12_prose")),
                spec(["b13", "b14"], 2, h("Casino Games and Slots", "Casino Lobby and Slots"), 120, "L=1 L2C=1", edit=["b13_slots"],
                     summary="The nine game categories and three example slots with RTP, volatility and maximum multiplier."),
                spec(["b15", "b16", "b17"], 2, h("Live Casino, Other Games and Providers", "Live Dealers, Other Games and Studios"), 170, "L=1 L2=1",
                     summary="The live dealer section with the exclusive baccarat, the other game types and the ten providers."),
                spec(["b03", "b04"], 2, h("Licence and Security", "Licence and Safety"), 135, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected."),
                spec(["b23"], 2, h("Responsible Betting and Gambling", "Safer Betting and Gambling"), 80, ""),
                spec(["b24"], 2, h("Support", "Contact Options"), 55, "L=1"),
                spec(["b25"], 2, h("Pros and Cons", "Pros and Cons for Bettors"), 60, ""),
                spec(["b26"], 2, h("Questions About Sports and Payouts", "Sports and Account Questions"), 0, "", faq_key=6),
                spec(["b27"], 2, h("Verdict for Sports Fans", "Verdict for Bettors"), 70, "LC=1 LF=1 L=1"),
            ])
    elif n == 7:
        T.update(
            name=h("Money first (payments and payouts)", "Cash flow first (payments and payouts)"),
            angle="A reader who wants to know how money gets in and out before anything else.",
            twist=True,
            intent=(f"Brand-review page about the Longfu88 online casino for players from {nm}, ordered around the cash flow: the fact table, deposit methods, withdrawals and fees, verification and payout checks, registration, the welcome bonus with wagering, cashback and rebates, reloads, VIP levels with withdrawal limits, games and providers, sports betting, mobile access, licence and data safety, responsible gambling, support, an FAQ on money questions and a verdict on the payment terms. "
                    f"Page voice: practical and number-led, sentences of about 15 words, short paragraphs of two to three sentences, every section closes with what the rule costs or how long it takes, amounts always with their currency or condition; calls to action only at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino Payments, Bonuses and Payouts Reviewed", "Longfu88 Casino Malaysia: Payments and Payout Review"), 75, "L=1"),
                spec(["b02"], 2, h("Payment and Brand Facts", "Key Payment and Brand Facts"), 0),
                spec(["b20"], 2, h("Deposit Methods and Limits", "Payment Methods for Deposits and Their Limits"), 110, "L=1"),
                spec(["b21"], 3, h("Withdrawals and Payout Times", "Payouts: Methods, Timing and Fees"), 100, "L=1"),
                spec(["b06"], 2, h("Verification and Payout Checks", "ID Checks Before You Cash Out"), 85, "L=1"),
                spec(["b05"], 2, h("Registration and Login", "Account Registration and Login"), 100, "L=1 LL=1 LCL=1", edit=["b05_prev"]),
                spec(["b07", "b08"], 2, h("Welcome Bonus and Wagering", "Welcome Offer, Wagering and Caps"), 155, "L=1 LB=1 LP=1", edit=["b07_next"],
                     summary="The Casino Welcome Bonus with its figures, claiming steps and alternatives, then the wagering, validity and bet limits in a table.",
                     extra="The one call-to-action place of the page: one plain invitation to claim the bonus is allowed."),
                spec(["b10"], 2, h("Cashback and Rebates", "Cashback and Daily Rebates"), 70, "", **toggles("b10_prose")),
                spec(["b09"], 2, h("Reloads and Seasonal Offers", "Reload Offers"), 95, "", **toggles("b09_prose")),
                spec(["b12"], 2, h("VIP Levels and Withdrawal Limits", "VIP Programme and Cash-Out Limits"), 90, ""),
                spec(["b13", "b14", "b15", "b16"], 2, h("Games You Can Play", "Game Types and Examples"), 200, "L=1 LC=1 L2C=1", edit=["b13_merge"],
                     summary="The nine game categories, three example slots with RTP, the live section with the exclusive baccarat and the other game types."),
                spec(["b17"], 2, h("Providers", "Game Studios"), 55, "L2=1"),
                spec(["b18", "b19"], 2, h("Sports Betting and Its Bonuses", "Sports Betting and Promotions"), 120, "L=1 LS=1",
                     summary="Sports and bet types, live betting and the sports bonuses with the shared odds rule."),
                spec(["b22"], 2, h("Mobile Payments and Play", "Mobile Access"), 75, "L=2 LA=1"),
                spec(["b03", "b04"], 2, h("Licence and Data Protection", "Operator, Licence and Data Safety"), 135, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected."),
                spec(["b23"], 2, h("Responsible Gambling", "Responsible Gambling Measures"), 75, "", **toggles("b23_prose")),
                spec(["b24"], 2, h("Support", "Customer Support Channels"), 55, "L=1"),
                spec(["b26"], 2, h("Money Questions", "Payment Questions"), 0, "", faq_key=7),
                spec(["b27"], 2, h("What the Payment Terms Mean", "Verdict on Payments"), 75, "LF=1 L=1"),
            ])
    elif n == 8:
        T.update(
            name=h("Mobile quick start (short sections)", "Phone first (short sections)"),
            angle="A reader on a phone who wants to get started in a few minutes.",
            twist=False,
            intent=(f"Compact brand-review page about the Longfu88 online casino for players from {nm}, built for a reader on a phone: the fact table, opening the casino on mobile, sign-up and login, the first bonus, adding funds, taking money out, what to play, sports bets, promotions and rewards, VIP levels, licence and data rules, responsible play, support, a short FAQ and a summary. "
                    f"Page voice: how-to and imperative, sentences of about 12 words, paragraphs of one to two sentences, many short flat H2 sections, each opens with the action the reader takes and ends with the one thing to check; lists and short tables where they save words; calls to action at the first bonus only. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino Mobile Review for Singapore: Quick Start", "Longfu88 Casino on Your Phone: Malaysia Review"), 65, "L=1"),
                spec(["b02"], 2, h("Quick Facts", "Facts in a Table"), 0),
                spec(["b22"], 2, h("Open the Casino on Your Phone", "Mobile Setup in Minutes"), 85, "L=2 LA=1", **toggles("b22_table")),
                spec(["b05", "b06"], 2, h("Sign Up and Log In", "Create an Account and Log In"), 130, "L=1 LCL=1", edit=["b05_next"],
                     summary="Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes."),
                spec(["b07", "b08"], 2, h("Your First Bonus", "First Bonus and Its Terms"), 140, "L=1 LB=1", edit=["b07_next"],
                     summary="The Casino Welcome Bonus with its figures, claiming steps and alternatives, then the wagering, validity and bet limits in a table.",
                     extra="The one call-to-action place of the page: one plain invitation to claim the bonus is allowed."),
                spec(["b20"], 2, h("Adding Funds: Payment Methods", "Payments: Adding Funds"), 100, "L=1"),
                spec(["b21"], 2, h("Taking Money Out", "Cashing Out"), 90, "L=1 LW=1"),
                spec(["b13", "b14", "b15", "b16", "b17"], 2, h("What to Play", "What to Play Today"), 190, "L=1 LC=1 L2C=1 L2=1", edit=["b13_merge"],
                     summary="The nine game categories, three example slots with RTP, the live section with the exclusive baccarat, the other categories and the ten providers."),
                spec(["b18"], 2, h("Sports Bets", "Sports Betting"), 75, "L=1 LS=1"),
                spec(["b09", "b10", "b11"], 2, h("Promotions and Rewards", "Ongoing Offers and Rewards"), 125, "L=1",
                     summary="The seven reload and seasonal offers in a table, the weekly cashback with VIP rates and the rebates, and the five reward features in short."),
                spec(["b12"], 2, h("VIP Programme", "VIP Club Levels"), 65, "", **toggles("b12_prose")),
                spec(["b03", "b04"], 2, h("Licence and Safety", "Licence and Data Rules"), 125, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected."),
                spec(["b23"], 2, h("Play Responsibly", "Responsible Play"), 70, "", **toggles("b23_prose")),
                spec(["b24"], 2, h("Help and Support", "Support"), 50, "L=1"),
                spec(["b26"], 2, h("Short FAQ", "Mobile FAQ"), 0, "", faq_key=8),
                spec(["b27"], 2, h("Summary", "Wrap-Up"), 60, "LC=1 LF=1 L=1"),
            ])
    elif n == 9:
        T.update(
            name=h("Q&A guide (pros and cons up front, big FAQ)", "Reader's questions (pros and cons first, big FAQ)"),
            angle="A reader who wants a balanced overview first and the detailed answers to common questions last.",
            twist=True,
            intent=(f"Brand-review page about the Longfu88 online casino for players from {nm}, built as a balanced guide: the fact table, a pros and cons table straight after it, what the casino is, licence and privacy, registration and verification, the welcome bonus, reloads and cashback, VIP levels, games and providers, sports betting, deposits and withdrawals, mobile use, responsible gambling, support, a detailed FAQ of six answers and a closing note. "
                    f"Page voice: explanatory and neutral, every section opens with the question a reader would ask (never written as a question) and answers it in the first two sentences, sentences of about 16 words, paragraphs of two to three sentences; a figure is always followed by what it means in practice; one call to action at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino Review for Singapore: What to Know First", "Longfu88 Casino Review for Malaysia: Questions Answered"), 75, "L=1"),
                spec(["b02"], 2, h("Casino Facts", "Core Facts"), 0),
                spec(["b25"], 2, h("Pros and Cons Table", "Pros and Cons Summary"), 60, ""),
                spec(["b03"], 2, h("About the Casino", "What the Casino Is"), 65, "L=1 LO=1"),
                spec(["b04"], 2, h("Licence and Data Protection", "Licence and Privacy"), 110, "L=1 CL=1"),
                spec(["b05"], 2, h("Registration and Login", "Registration and Login Steps"), 105, "L=1 LL=1 LCL=1"),
                spec(["b06"], 3, h("Identity Verification", "Verification Rules"), 75, ""),
                spec(["b07"], 2, h("Welcome Bonus", "Welcome Offer"), 105, "L=1 LB=1",
                     extra="The one call-to-action place of the page: one plain invitation to claim the bonus is allowed."),
                spec(["b08"], 3, h("Wagering and Limits", "Wagering Terms"), 75, ""),
                spec(["b09"], 2, h("Reloads and Special Offers", "Reload and Special Campaigns"), 90, "", **toggles("b09_list")),
                spec(["b10"], 3, h("Cashback and Rebates", "Cashback and Rebate Details"), 60, ""),
                spec(["b12"], 2, h("VIP Levels", "VIP Programme"), 80, "L=1"),
                spec(["b13"], 2, h("Games", "Casino Games"), 65, "L=1 LC=1"),
                spec(["b14"], 3, h("Slots", "Slot Examples"), 70, ""),
                spec(["b15"], 3, h("Live Casino", "Live Dealers"), 70, "L=1 L2C=1"),
                spec(["b17"], 2, h("Game Providers", "Game Studios"), 55, "L2=1"),
                spec(["b18", "b19"], 2, h("Sports Betting", "Sportsbook"), 115, "L=1 LS=1",
                     summary="Sports and bet types, live betting and the sports bonuses with the shared odds rule."),
                spec(["b20"], 2, h("Deposits", "Deposit Methods"), 100, "L=1"),
                spec(["b21"], 3, h("Withdrawals", "Withdrawal Rules"), 90, "L=1"),
                spec(["b22"], 2, h("Mobile Play", "Mobile Use"), 75, "L=2"),
                spec(["b23"], 2, h("Responsible Gambling", "Safer Gambling"), 75, ""),
                spec(["b24"], 2, h("Support", "Support Contacts"), 55, "L=1"),
                spec(["b26"], 2, h("Frequently Asked Questions", "Detailed FAQ"), 0, "", faq_key=9),
                spec(["b27"], 2, h("Conclusion", "Closing Thoughts"), 65, "LC=1 LF=1 L=1"),
            ])
    elif n == 10:
        T.update(
            name=h("Reference guide (longest, table-heavy)", "Full reference (longest, table-heavy)"),
            angle="A reader who wants every number in one place and compares offers in tables.",
            twist=True,
            intent=(f"Long reference page about the Longfu88 online casino for players from {nm}: what the casino offers, the fact table, licence and data protection, registration and verification, the welcome bonus with a terms table, reloads, cashback, rewards, the VIP programme, the game library by category, providers, the sportsbook with a bonus table, deposit methods, withdrawals, mobile access, responsible gambling, support, pros and cons, a six-answer FAQ and a verdict. "
                    f"Page voice: formal and exhaustive, sentences of about 21 words, paragraphs of three to four sentences, tables wherever two or more attributes belong to an item, comparative statements that put offers side by side, every table introduced by one sentence and followed by one sentence on what it means; one call to action at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, h("Longfu88 Casino Complete Guide for Singapore Players", "Longfu88 Casino Complete Guide for Malaysian Players"), 85, "L=1"),
                spec(["b03"], 2, h("What the Casino Offers", "Casino Profile"), 70, "L=1 LO=1"),
                spec(["b02"], 2, h("Casino Information", "Casino Information Table"), 0),
                spec(["b04"], 2, h("Licensing, Operator and Data Protection", "Licence, Operator and Privacy"), 120, "L=1 CL=1"),
                spec(["b05"], 2, h("Registration and Login Guide", "Registration and Login Procedure"), 110, "L=1 LL=1 LCL=1"),
                spec(["b06"], 3, h("Verification (KYC)", "KYC Document Checks"), 85, ""),
                spec(["b07"], 2, h("Casino Welcome Bonus", "Welcome Bonus Breakdown"), 115, "L=1 LB=1 LP=1",
                     extra="The one call-to-action place of the page: one plain invitation to claim the bonus is allowed."),
                spec(["b08"], 3, h("Terms of the Welcome Bonus", "Welcome Bonus Terms in a Table"), 85, ""),
                spec(["b09"], 2, h("Reload Bonuses and Seasonal Promotions", "Reloads, Specials and Seasonal Campaigns"), 100, "L=1"),
                spec(["b10"], 3, h("Cashback and Rebate Programme", "Cashback and Rebate Rates"), 65, ""),
                spec(["b11"], 3, h("Rewards Hub", "Rewards Features"), 60, ""),
                spec(["b12"], 2, h("VIP Programme: Levels, Points and Limits", "VIP Programme: Ladder and Limits"), 90, "L=1"),
                spec(["b13"], 2, h("Game Library by Category", "Game Library Overview"), 70, "L=1 L2C=1"),
                spec(["b14"], 3, h("Slot Games", "Slot Titles and Numbers"), 80, ""),
                spec(["b15"], 3, h("Live Casino Games", "Live Casino Section"), 75, "L=1"),
                spec(["b16"], 3, h("Other Game Types", "Other Categories"), 65, "", **toggles("b16_list")),
                spec(["b17"], 2, h("Software Providers", "Providers in the Lobby"), 60, "L2=1", **toggles("b17_list")),
                spec(["b18"], 2, h("Sportsbook", "Sports Betting Overview"), 85, "L=1 LS=1"),
                spec(["b19"], 3, h("Sports Bonus Table", "Sports Bonuses and Boosts"), 65, ""),
                spec(["b20"], 2, h("Payment Methods and Deposit Limits", "Deposit Methods and Limits Table"), 110, "L=1"),
                spec(["b21"], 3, h("Withdrawal Methods and Times", "Withdrawals: Steps, Times and Fees"), 100, "L=1 LW=1"),
                spec(["b22"], 2, h("Mobile Access and Installation", "Mobile Access"), 85, "L=2 LA=1"),
                spec(["b23"], 2, h("Responsible Gambling Policy", "Responsible Gambling Tools"), 85, "L=1"),
                spec(["b24"], 2, h("Customer Support Channels", "Support Channels"), 60, "L=1"),
                spec(["b25"], 2, h("Pros and Cons Overview", "Pros and Cons Compared"), 60, ""),
                spec(["b26"], 2, h("Frequently Asked Questions", "Answers to Frequent Questions"), 0, "", faq_key=10),
                spec(["b27"], 2, h("Verdict", "Final Verdict"), 80, "LC=1 LF=1 L=1"),
            ])
    elif n == 11:
        T.update(
            name="Loyalty and rewards (regular player's page)",
            angle="A regular player who wants to know what the casino gives back over time: VIP levels, cashback, rebates and reloads.",
            twist=False,
            intent=(f"Brand-review page about the Longfu88 online casino for players from {nm}, written for a regular player: the fact sheet, the VIP programme, weekly cashback and daily rebates, reloads and reward features, the welcome bonus as the entry point, the sportsbook rewards, payments and withdrawal limits, the game lobby, mobile access, registration and verification, licence and data safety, responsible gambling, support, pros and cons, a short FAQ and a verdict. "
                    f"Page voice: measured and numerate, sentences of about 19 words, paragraphs of three to four sentences, every reward is followed by the condition that earns it and by what it is worth over a month of play, comparisons between offers of the same kind; calls to action only at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, "Longfu88 Casino Rewards Review: Cashback, Reloads and VIP Levels for Singapore", 80, "L=1"),
                spec(["b02"], 2, "Rewards and Brand Facts", 0),
                spec(["b12"], 2, "How the VIP Programme Pays Back", 95, "L=1"),
                spec(["b10"], 2, "Weekly Cashback and Daily Rebates", 75, ""),
                spec(["b09"], 2, "Reloads, Weekend Offers and Seasonal Drops", 100, "", **toggles("b09_list")),
                spec(["b11"], 3, "Bonus Crab, Wheel of Fortune and Coin Shop", 60, ""),
                spec(["b07"], 2, "Welcome Bonus for New Accounts", 105, "L=1 LP=1",
                     extra="The one call-to-action place of the page: one plain invitation to claim the bonus is allowed."),
                spec(["b08"], 3, "What the Welcome Bonus Asks in Return", 80, ""),
                spec(["b18"], 2, "Sportsbook Rewards and Markets", 85, "L=1 LS=1"),
                spec(["b19"], 3, "Sports Bonuses, Cashback and Boosts", 65, "", **toggles("b19_prose")),
                spec(["b20"], 2, "Payments, Limits and Withdrawal Caps", 105, "L=1"),
                spec(["b21"], 3, "Withdrawal Steps, Fees and Timing", 95, "L=1 LW=1"),
                spec(["b13", "b14", "b15", "b16", "b17"], 2, "Where the Rewards Are Played: the Game Lobby", 190, "L=1 LC=1 L2C=1 L2=1", edit=["b13_merge"],
                     summary="The nine game categories, three example slots with RTP, the live section with the exclusive baccarat, the other categories and the ten providers."),
                spec(["b22"], 2, "Mobile Access for Regular Players", 80, "L=2 LA=1"),
                spec(["b05", "b06"], 2, "Registration, Login and Verification", 135, "L=1 LL=1 LCL=1", edit=["b05_next"],
                     summary="Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes."),
                spec(["b03", "b04"], 2, "Licence, Operator and Data Safety", 135, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected."),
                spec(["b23"], 2, "Responsible Gambling and Limits", 80, ""),
                spec(["b24"], 2, "Customer Support", 55, "L=1"),
                spec(["b25"], 2, "Pros and Cons for Regular Players", 60, ""),
                spec(["b26"], 2, "Questions About Rewards", 0, "", faq_key=11),
                spec(["b27"], 2, "Verdict for Regular Players", 75, "LC=1 LF=1 L=1"),
            ])
    else:
        T.update(
            name="Crypto-friendly guide (USDT and fiat side by side)",
            angle="A player who deposits and withdraws in cryptocurrency and wants the crypto offers and the payout rules in one place.",
            twist=False,
            intent=(f"Brand-review page about the Longfu88 online casino for crypto-friendly players from {nm}: the fact sheet, deposit methods with the cryptocurrencies and networks, crypto and fiat withdrawals with fees, the crypto welcome bonus and its alternatives, crypto reloads and the other weekly offers, sports offers, VIP levels, verification before payouts, registration, games and providers, mobile access, licence and data safety, responsible gambling, support, an FAQ on crypto questions and a verdict. "
                    f"Page voice: technical and plain, sentences of about 16 words, paragraphs of two to four sentences, every crypto figure comes with its currency or network and its condition, fiat and crypto offers are always kept apart and never mixed in one sum; one call to action, at the crypto welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {nm}."),
            blocks=[
                spec(["b01"], 1, "Longfu88 Casino for Crypto Players in Singapore: Review", 80, "L=1"),
                spec(["b02"], 2, "Casino and Crypto Facts", 0),
                spec(["b20"], 2, "Deposit Methods: Crypto Networks and Local Options", 115, "L=1",
                     extra="Lead with the cryptocurrencies and the three USDT networks, then the local and card methods; keep per-method limits out, as the notes say."),
                spec(["b21"], 3, "Crypto and Fiat Withdrawals: Timing and Fees", 100, "L=1 LW=1"),
                spec(["b07"], 2, "Crypto Welcome Bonus and the Alternatives", 115, "L=1 LB=1 LP=1",
                     extra="Present the Casino Crypto Welcome Bonus first (188% up to 2,888 USDT, minimum deposit 50 USDT, 40x deposit plus bonus, 10 days, the eligible cryptocurrencies) as the one call-to-action place of the page, then the Casino Welcome Bonus and the Live Casino Welcome Bonus in fiat; never add crypto and fiat figures together."),
                spec(["b08"], 3, "Wagering and Caps of the Fiat Welcome Bonus", 80, ""),
                spec(["b09"], 2, "Crypto Reloads and Weekly Offers", 100, "",
                     extra="Mention the Casino Weekly Crypto Reload and the Casino Weekend Crypto Reload before the fiat reloads in the table."),
                spec(["b10"], 3, "Cashback and Rebates", 65, "", **toggles("b10_prose")),
                spec(["b18", "b19"], 2, "Sports Betting with Crypto Offers", 125, "L=1 LS=1",
                     summary="Sports and bet types, live betting and the sports bonuses with the shared odds rule, including the crypto equivalents.",
                     extra="Name the Sport Crypto Welcome Bonus, the Sport Crypto Weekly Reload and the Sport Crypto Weekend Reload in the sports bonus part."),
                spec(["b12"], 2, "VIP Programme and Withdrawal Limits", 85, "L=1", **toggles("b12_prose")),
                spec(["b06"], 2, "Verification Before Crypto and Card Payouts", 85, "L=1"),
                spec(["b05"], 2, "Registration and Login", 105, "L=1 LL=1 LCL=1", edit=["b05_prev"]),
                spec(["b13", "b14", "b15", "b16", "b17"], 2, "Games and Providers", 190, "L=1 LC=1 L2C=1", edit=["b13_merge"],
                     summary="The nine game categories, three example slots with RTP, the live section with the exclusive baccarat, the other categories and the ten providers."),
                spec(["b22"], 2, "Mobile Access", 75, "L=2 LA=1"),
                spec(["b03", "b04"], 2, "Licence, Operator and Data Protection", 135, "L=1 CL=1 LO=1", edit=["b03_later"],
                     summary="Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected."),
                spec(["b23"], 2, "Responsible Gambling", 75, "", **toggles("b23_prose")),
                spec(["b24"], 2, "Support Channels", 55, "L=1"),
                spec(["b26"], 2, "Crypto Questions", 0, "", faq_key=12),
                spec(["b27"], 2, "Verdict for Crypto Users", 70, "LC=1 LF=1 L=1"),
            ])
    return T


MOVABLE = [{"b12"}, {"b22"}, {"b23"}, {"b24"}, {"b25"}, {"b18", "b19"}, {"b20", "b21"}, {"b09", "b10", "b11"}, {"b03", "b04"}]


def _tag(group):
    ids = {i for x in group for i in x["ids"]}
    for n, m in enumerate(MOVABLE):
        if ids <= m:
            return n
    return None


def twist(blocks, seed, swaps=3):
    """Swap neighbouring H2 groups (an H2 and its H3s) of independent topics (VIP, mobile, responsible gambling, support, pros and
    cons, sports, payments, promotions, licence): the H1, the fact table, the account, welcome bonus and game groups, the FAQ and the
    verdict keep their places."""
    groups = []
    for b in blocks:
        if b["lvl"] <= 2:
            groups.append([b])
        else:
            groups[-1].append(b)
    tags = [_tag(g) for g in groups]
    fact = next(i for i, g in enumerate(groups) if any(x["ids"] == ["b02"] for x in g))
    cand = [i for i in range(fact + 1, len(groups) - 3)
            if tags[i] is not None and tags[i + 1] is not None and tags[i] != tags[i + 1]]
    rnd = random.Random(seed)
    rnd.shuffle(cand)
    taken = set()
    for i in cand:
        if len(taken) >= 2 * swaps:
            break
        if i in taken or i + 1 in taken:
            continue
        groups[i], groups[i + 1] = groups[i + 1], groups[i]
        taken |= {i, i + 1}
    return [b for g in groups for b in g]


SCALE = [0.95, 1.06, 0.97, 1.04, 0.96, 1.05, 0.98, 1.06, 0.95, 1.03]  # the Malaysian pages are sized a little differently


def to_blueprint(geo):
    c = Ctx(geo)
    base_name = f"longfu88-{geo}"
    base = {b["id"]: b for b in json.load(open(f"runs/{base_name}/01_brief.json", encoding="utf-8"))["blocks"]}
    variants = []
    for n in range(1, 13 if geo == "sg" else 11):
        T = arch(n, c)
        blocks = T["blocks"]
        if T["twist"] and (geo == "my" or n in (9, 10)):
            blocks = twist(blocks, (100 if geo == "my" else 200) + n, 3 if geo == "my" else 2)
        out = []
        for s in blocks:
            d = {"from": s["ids"], "level": s["lvl"], "heading": s["head"]}
            more = s["more"]
            if s["ids"] == ["b02"]:
                rows = ROWS[n][0 if geo == "sg" else 1]
                d["fact_rows"] = rows
                d["words"] = 8 * len(rows) + 12
                d["kw"] = s["kw"] or {"Longfu88": 1}
                d["kw"] = {"Longfu88": 1}
                d["summary"] = "A fact sheet of the casino: " + ", ".join(
                    (r if isinstance(r, str) else r["label"]).replace("_", " ") for r in rows) + "."
                d["summary"] = d["summary"].replace("company", "operator").replace("founded", "launch year").replace("min deposit", "minimum deposit")
            elif "faq_key" in more:
                keys, plc = FAQ[more["faq_key"]]
                keys = rotate(keys, geo, 1) if len(keys) >= 5 else (keys if geo == "sg" else keys[::-1])
                f = faq(keys, plc)
                d.update(words=f["words"], kw=f["kw"], notes=f["notes"], refs_add=f["refs_add"], refs_drop=f["refs_drop"], kw_lists_ok=True,
                         formats=f["formats"], summary=f["summary"])
                d["entities"] = [["Frequently Asked Questions", 8]] + [[SHORT[k].capitalize(), 6] for k in keys[:4]]
                d["connections"] = [["Frequently Asked Questions", "cover", ", ".join(SHORT[k] for k in keys), 6]]
            else:
                d["words"] = round(s["w"] * (SCALE[n - 1] if geo == "my" else 1))
                d["kw"] = s["kw"]
                if len(s["ids"]) > 1 or s["summary"]:
                    d["summary"] = s["summary"] or merged_summary(s["ids"], base)
                edits = [list(e) for e in s["edit"]]
                if "b04" in s["ids"] and "b06" not in s["ids"]:
                    edits.append(list(E["b04_own"]))
                if edits:
                    d["edit"] = edits
                if s["fmt"]:
                    d["formats"] = s["fmt"]
                if s["extra"]:
                    d["extra"] = s["extra"]
            if s["ids"] == ["b01"] or s["lvl"] == 1:
                pass
            out.append(d)
        variants.append({"id": f"v{n:02d}", "name": T["name"], "angle": T["angle"], "intent_summary": T["intent"], "blocks": out})
    bp = {"base_run": base_name, **CFG, "variants": variants}
    return bp


GEOS = {  # base run -> (country, adjective, archetypes of the four sites, seed of the twist)
    "longfu88-indonesia": ("Indonesia", "Indonesian", [2, 4, 6, 8], 310),
    "longfu88-malaysia": ("Malaysia", "Malaysian", [1, 3, 5, 7], 320),
    "longfu88-vietnam": ("Vietnam", "Vietnamese", [5, 10, 1, 6], 330),
    "longfu88-thailand": ("Thailand", "Thai", [3, 5, 8, 10], 340),
    "longfu88-singapore": ("Singapore", "Singaporean", [2, 7, 9, 4], 350),
}


def to_blueprint_geo(base_name):
    """Four variants (one per site) for a GEO run of the second batch: the working headings of the Malaysian branch with the country
    names replaced; the page headings are localized in step 2."""
    name, adj, archs, seed0 = GEOS[base_name]
    c = Ctx("my")
    c.name = name
    sub = lambda s: s.replace("Malaysian", adj).replace("Malaysia", name) if isinstance(s, str) else s
    base = {b["id"]: b for b in json.load(open(f"runs/{base_name}/01_brief.json", encoding="utf-8"))["blocks"]}
    variants = []
    for k, n in enumerate(archs, 1):
        T = arch(n, c)
        blocks = T["blocks"]
        if T["twist"]:
            blocks = twist(blocks, seed0 + n, 3)
        out = []
        for s in blocks:
            d = {"from": s["ids"], "level": s["lvl"], "heading": sub(s["head"])}
            more = s["more"]
            if s["ids"] == ["b02"]:
                rows = ROWS[n][1]
                d["fact_rows"] = rows
                d["words"] = 8 * len(rows) + 12
                d["kw"] = {"Longfu88": 1}
                d["summary"] = "A fact sheet of the casino: " + ", ".join((r if isinstance(r, str) else r["label"]).replace("_", " ") for r in rows) + "."
                d["summary"] = d["summary"].replace("company", "operator").replace("founded", "launch year").replace("min deposit", "minimum deposit")
            elif "faq_key" in more:
                keys, plc = FAQ[more["faq_key"]]
                keys = rotate(keys, "my", 1) if len(keys) >= 5 else keys[::-1]
                f = faq(keys, plc)
                d.update(words=f["words"], kw=f["kw"], notes=f["notes"], refs_add=f["refs_add"], refs_drop=f["refs_drop"], kw_lists_ok=True,
                         formats=f["formats"], summary=f["summary"])
                d["entities"] = [["Frequently Asked Questions", 8]] + [[SHORT[x].capitalize(), 6] for x in keys[:4]]
                d["connections"] = [["Frequently Asked Questions", "cover", ", ".join(SHORT[x] for x in keys), 6]]
            else:
                d["words"] = round(s["w"] * SCALE[n - 1])
                d["kw"] = s["kw"]
                if len(s["ids"]) > 1 or s["summary"]:
                    d["summary"] = sub(s["summary"] or merged_summary(s["ids"], base))
                edits = [list(e) for e in s["edit"]]
                if "b04" in s["ids"] and "b06" not in s["ids"]:
                    edits.append(list(E["b04_own"]))
                if edits:
                    d["edit"] = edits
                if s["fmt"]:
                    d["formats"] = s["fmt"]
                if s["extra"]:
                    d["extra"] = sub(s["extra"])
            out.append(d)
        variants.append({"id": f"v{k:02d}", "name": T["name"], "angle": T["angle"], "intent_summary": sub(T["intent"]), "blocks": out})
    return {"base_run": base_name, **CFG, "variants": variants}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "geos":
        for base_name in GEOS:
            bp = to_blueprint_geo(base_name)
            path = f"input/variants/{base_name}.json"
            json.dump(bp, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(path, [len(v["blocks"]) for v in bp["variants"]])
        sys.exit(0)
    for geo in ("sg", "my"):
        bp = to_blueprint(geo)
        path = f"input/variants/longfu88-{geo}.json"
        json.dump(bp, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(path, [len(v["blocks"]) for v in bp["variants"]])

