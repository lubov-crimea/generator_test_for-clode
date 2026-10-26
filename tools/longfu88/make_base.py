"""Builds runs/<run>/llm/brief.json (the answer of the manual step-1 brief request) for the Longfu88 base runs."""
import json
import sys

GEO = {
    "longfu88-sg": dict(
        geo="Singapore", adj="Singapore", cur="SGD",
        local="PayNow, PayNow QR, DBS Bank and OCBC Bank (SGD)",
        local_names="PayNow, PayNow QR, DBS Bank, OCBC Bank",
        h1="Longfu88 Casino Review for Singapore Players",
        extra_kw={},
    ),
    "longfu88-my": dict(
        geo="Malaysia", adj="Malaysian", cur="MYR",
        local="DuitNow, Touch'n Go, GrabPay and Online Banking (MYR)",
        local_names="DuitNow, Touch'n Go, GrabPay, Online Banking",
        h1="Longfu88 Casino Review for Malaysian Players",
        extra_kw={"b05": {"Longfu caino login": 1}},
    ),
    "longfu88-indonesia": dict(
        geo="Indonesia", adj="Indonesian", cur="",
        local="QRIS, DANA, OVO Wallet, Mandiri, BNI and BCA (IDR)",
        local_names="QRIS, DANA, OVO Wallet, Mandiri, BNI",
        h1="Longfu88 Casino Review for Indonesian Players",
        extra_kw={"b05": {"Longfu caino login": 1}},
    ),
    "longfu88-malaysia": dict(
        geo="Malaysia", adj="Malaysian", cur="MYR",
        local="DuitNow, Touch'n Go, GrabPay and Online Banking (MYR)",
        local_names="DuitNow, Touch'n Go, GrabPay, Online Banking",
        h1="Longfu88 Casino Review for Malaysian Players",
        extra_kw={"b05": {"Longfu caino login": 1}},
    ),
    "longfu88-vietnam": dict(
        geo="Vietnam", adj="Vietnamese", cur="",
        local="MoMo, Zalo, ViettelPay and VietQR (VND)",
        local_names="MoMo, Zalo, ViettelPay, VietQR",
        h1="Longfu88 Casino Review for Vietnamese Players",
        extra_kw={"b05": {"Longfu caino login": 1}},
    ),
    "longfu88-thailand": dict(
        geo="Thailand", adj="Thai", cur="THB",
        local="PromptPay QR (THB)",
        local_names="PromptPay QR, Visa, Mastercard, Bitcoin",
        h1="Longfu88 Casino Review for Thai Players",
        extra_kw={"b05": {"Longfu caino login": 1}},
    ),
    "longfu88-singapore": dict(
        geo="Singapore", adj="Singaporean", cur="SGD",
        local="PayNow, PayNow QR, DBS Bank and OCBC Bank (SGD)",
        local_names="PayNow, PayNow QR, DBS Bank, OCBC Bank",
        h1="Longfu88 Casino Review for Singaporean Players",
        extra_kw={"b05": {"Longfu caino login": 1}},
    ),
}


def rng(mid):
    return round(mid * 0.88), round(mid * 1.12)


def build(run):
    g = GEO[run]
    curtxt = f" (including {g['cur']})" if g["cur"] else ""
    legal = (f'NEVER say or imply that the casino is licensed, legal or approved in {g["geo"]}; the licence named in the Brand Information is the only licence statement.')
    blocks = []

    def add(level, heading, source, covers, refs, mid, kw, formats, ents, conns, summary, notes, listed=None, fact_table=None):
        lo, hi = rng(mid)
        b = dict(level=level, heading=heading, source=source, covers_clusters=covers, kb_refs=refs, words_min=lo, words_max=hi,
                 keywords=kw, formats=formats, entities=[{"name": n, "priority": p} for n, p in ents],
                 entity_connections=[{"subject": a, "relation": r, "object": c, "priority": p} for a, r, c, p in conns],
                 summary=summary, copywriter_notes=notes)
        if listed:
            b["listed_entities"] = listed
        if fact_table:
            b["fact_table"] = fact_table
        blocks.append(b)

    # b01
    add(1, g["h1"], "h1", [], ["brandinfo_general.release_year", "brandinfo_general.minimum_age", "brandinfo_games.game_types"], 75,
        {"Longfu88": 2}, ["paragraph"],
        [("Online Casino", 10), (f'Players from {g["geo"]}', 8), ("Game Categories", 7), ("Sportsbook", 6)],
        [("Online Casino", "combines", "casino games, live dealer games, sports betting and lottery", 8), ("Adult Players", "must be at least", "18 years old", 7)],
        f'Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from {g["geo"]}.',
        f'Open with the keyword "Longfu88" as the subject of the first sentence, followed by a definition of the online casino by its game areas (slots, live dealer games, table games, jackpots, fishing, P2P, fast games, lottery, crash and instant games) and a sportsbook, and the launch year from the Brand Information. State the 18+ age limit once. Say that the page is written for players from {g["geo"]}. {legal} Use "Longfu88" exactly twice and no other tracked keyword. No bonus amounts, payment or registration details here; only signpost the topics of the page (facts, licence, bonuses, games, payments, mobile play, responsible gambling). Neutral-positive tone, no promises of winnings.')

    # b02 fact table
    ft = [
        {"key": "company", "label": "Operator", "kb_refs": ["brandinfo_privacy_policy.privacy_policy.data_controller.company_name"]},
        {"key": "licence", "label": "Licence", "kb_refs": ["brandinfo_general.licences[0]"]},
        {"key": "founded", "label": "Launched", "kb_refs": ["brandinfo_general.release_year"]},
        {"key": "languages", "label": "Support languages", "kb_refs": ["brandinfo_general.customer_support.languages"]},
        {"key": "currencies", "label": "Currencies", "kb_refs": ["brandinfo_general.currencies"]},
        {"key": "payment_methods", "label": "Payment methods", "kb_refs": ["brandinfo_general.payment_methods.deposit"]},
        {"key": "welcome_bonus", "label": "Welcome bonus", "kb_refs": ["brandinfo_general.welcome_bonus_summary"]},
        {"key": "cashback", "label": "Cashback", "kb_refs": ["brandinfo_promotions.other_bonuses[9].reward"]},
        {"key": "min_deposit", "label": "Minimum deposit", "kb_refs": ["brandinfo_general.minimum_deposit"]},
        {"key": "support", "label": "Support", "kb_refs": ["brandinfo_general.customer_support.email", "brandinfo_general.customer_support.channels"]},
    ]
    add(2, "Casino Facts at a Glance", "unique", [], [], 85, {"Longfu88": 1}, ["table"],
        [("Operator", 8), ("Gambling Licence", 8), ("Welcome Bonus", 7), ("Payment Methods", 6), ("Currencies", 5), ("Customer Support", 5)],
        [("Gambling Licence", "belongs to", "the Online Casino", 7), ("Welcome Bonus", "is offered by", "the Online Casino", 6)],
        "A compact fact sheet of the casino: operator, licence, launch year, support languages, currencies, payment methods, welcome bonus, cashback, minimum deposit and support e-mail.",
        'The table has exactly the rows of the Fact Table list, in this order, nothing else; the left cell is the row label, the right cell a short fact (a figure, a name or a comma-separated list, at most 20 words), no sentences. Licence = jurisdiction, operator and registration number as given. Welcome bonus = the summary line as given, shortened to the percentage, the maximum amount and the number of free spins. Cashback = the percentage and its base only (weekly net casino losses). Minimum deposit = the general minimum deposit of the casino (€10); do not use the €50 of the welcome bonus here. Payment methods = five or six well-known names taken from the list (for example Visa, Mastercard, Bank Transfer, Bitcoin, USDT, ' + g["local_names"].split(", ")[0] + '), not the whole list. Currencies and support languages = names only. Support = the e-mail address exactly as given plus the live chat: the e-mail contains the tracked keyword "Longfu88", which is the one occurrence this block allows; no other tracked keyword here. Do not add a lead-in sentence or closing text.',
        listed=["Operator", "Gambling Licence", "Welcome Bonus", "Payment Methods", "Currencies", "Customer Support"], fact_table=ft)

    # b03 overview
    add(2, "About the Casino", "mandatory", ["k01"],
        ["brandinfo_general.release_year", "brandinfo_general.currencies", "brandinfo_privacy_policy.terms_conditions.eligibility"], 60,
        {"Longfu88": 1, "Longfu 88 Official Site": 1}, ["paragraph"],
        [("Online Casino", 10), ("Official Website", 7), ("Account Currencies", 5), ("Player Eligibility", 6)],
        [("Online Casino", "was launched", "in 2026", 7), ("Players", "must be", "legally permitted to gamble where they live", 6)],
        f'What the casino is for a player from {g["geo"]}: launch year, account currencies, the official website and who may play.',
        f'Give the launch year (2026) and the account currencies from the Brand Information{curtxt}. Where "Longfu 88 Official Site" is used, put it in a natural phrase, for example that players should use the Longfu 88 Official Site address and not look-alike pages (this is advice, not a fact claim about domains). Explain who may play: 18+, legally permitted to gamble in the place of residence, one personal account, no third-party payment methods. {legal} Use "Longfu88" exactly once and "Longfu 88 Official Site" exactly once, and no other tracked keyword. Do not repeat the licence or bonus details (later sections).')

    # b04 safety
    add(2, "Licence, Operator and Data Protection", "mandatory", ["k18"],
        ["brandinfo_general.licences[0]", "brandinfo_privacy_policy.privacy_policy.data_controller", "brandinfo_privacy_policy.privacy_policy.security",
         "brandinfo_privacy_policy.privacy_policy.data_sharing", "brandinfo_privacy_policy.privacy_policy.data_subject_rights", "brandinfo_privacy_policy.terms_conditions.account_terms"], 105,
        {"Longfu88": 1, "casino Longfu88": 1}, ["paragraph"],
        [("Gambling Licence", 10), ("Operator", 8), ("Data Protection", 8), ("Data Controller", 6), ("Account Security", 6)],
        [("Gambling Licence", "is held by", "the operator", 8), ("Operator", "protects", "accounts, payments and personal data with technical and organisational safeguards", 7)],
        "Who licenses and runs the casino (jurisdiction, operator, registration number) and how personal data and accounts are protected.",
        f'Lead with the licence: jurisdiction Costa Rica, the operator named there (Lumina) and the registration number, exactly as in the Brand Information. The operator also acts as the data controller; the data protection officer is reached at the e-mail given in the privacy policy (print it only if it fits; it contains the tracked keyword "Longfu88", which then counts). Explain who the data may be shared with (payment service providers, identity verification providers, technology providers, regulators and law enforcement when required) and which rights the player has (access, rectification, erasure where legally permitted, restriction, objection, portability, withdrawal of consent). The account holder is responsible for safeguarding credentials. Use "casino Longfu88" exactly once; where "casino Longfu88" is used, it sits in a natural sentence about the licence. {legal} Do not claim an audit, eCOGRA, RNG certificate, SSL or any other certification: none is given. Use "Longfu88" exactly once and "casino Longfu88" exactly once and no other tracked keyword. Do not repeat identity-check details (next section).')

    # b05 registration
    kw5 = {"Longfu88": 1, "Longfu88 login": 1}
    kw5.update(g["extra_kw"].get("b05", {}))
    extra_login = ' Use "Longfu caino login" exactly once; where "Longfu caino login" is used, write it verbatim with this spelling in a sentence about logging in or about a player who searches for the login page.' if "b05" in g["extra_kw"] else ""
    add(2, "Registration and Login", "unique", ["k13"],
        ["brandinfo_account.registration", "brandinfo_account.login"], 100 if not g["extra_kw"] else 105, kw5, ["paragraph", "list"],
        [("Registration", 10), ("Login", 8), ("Password Recovery", 6), ("Two Accounts Rule", 5), ("Email Confirmation", 5)],
        [("Registration", "requires", "email, password, legal name, date of birth and residential address", 8), ("Player", "may hold", "only one personal account", 7)],
        "How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.",
        f'One lead-in sentence, then a NUMBERED list with the five registration steps in order as given in the Brand Information, then a short paragraph on login (select Login, enter registered email and password, complete any security check) and password recovery (Forgot Password on the login screen, reset link by email). Mention the required details (email, password, legal name, date of birth, residential address) and the rule of one personal account per player. Use "Longfu88 login" exactly once; where "Longfu88 login" is used, it sits in the login paragraph.{extra_login} Use "Longfu88" exactly once and no other tracked keyword besides those named; do not put tracked keywords into list items unless the verbatim step contains the brand. Do not mention the identity-document check here (next sub-section).')

    # b06 verification
    add(3, "Identity Verification Before Withdrawals", "unique", [],
        ["brandinfo_account.verification", "brandinfo_privacy_policy.kyc_aml.required_documents", "brandinfo_privacy_policy.kyc_aml.processing_time",
         "brandinfo_privacy_policy.kyc_aml.failure_consequences"], 70, {"Longfu88": 1}, ["paragraph", "list"],
        [("KYC Verification", 10), ("Identity Documents", 8), ("Proof of Address", 6), ("Source of Funds", 5)],
        [("Verification", "may be required", "before a withdrawal", 8), ("Complete Document Set", "is reviewed within", "10 days", 7)],
        "When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.",
        'State the triggers (before withdrawal, unusual or high-value transactions, changes to account or payment details), give the document types as a compact bulleted list (identity: passport, national identity card or driving licence; address: utility bill or bank statement; proof of payment-method ownership; source of funds when requested), the 30-day window to send documents and the review time of up to 10 days after a complete set. Say that withdrawals may be held until the checks are done and that failed checks can mean refused transactions or restrictions. Use "Longfu88" exactly once and no other tracked keyword.')

    # b07 welcome
    add(2, "Welcome Bonus", "mandatory", ["k10"],
        ["brandinfo_welcome.welcome_bonus.name", "brandinfo_welcome.welcome_bonus.type", "brandinfo_welcome.welcome_bonus.bonus_percentage",
         "brandinfo_welcome.welcome_bonus.maximum_bonus", "brandinfo_welcome.welcome_bonus.free_spins", "brandinfo_welcome.welcome_bonus.minimum_deposit",
         "brandinfo_welcome.welcome_bonus.eligibility", "brandinfo_welcome.welcome_bonus.claiming_procedure",
         "brandinfo_promotions.other_bonuses[0]", "brandinfo_promotions.other_bonuses[1]"], 100,
        {"Longfu88": 1, "Longfu88 bonus": 1, "Longfu88 promo code": 1}, ["paragraph", "list"],
        [("Casino Welcome Bonus", 10), ("Deposit Bonus", 8), ("Free Spins", 7), ("Minimum Deposit", 6), ("My Bonuses", 5)],
        [("Casino Welcome Bonus", "gives", "188% up to €2,088 plus 18 free spins", 9), ("Casino Welcome Bonus", "is activated", "in My Bonuses before any wager", 7)],
        "The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.",
        'Name the offer "Casino Welcome Bonus" and give 188% up to €2,088 plus 18 Free Spins exactly as in the Brand Information. It is for new registered players on the first qualifying deposit, one welcome offer per account; the qualifying minimum deposit of THIS bonus is €50 (this is not the general minimum deposit of the casino, which is €10: never mix the two). Give the four claiming steps as a short bulleted list (register, make the first qualifying deposit, activate the bonus in My Bonuses before placing any wagers, play eligible games and finish the wagering before expiry). PROMO CODE: the claiming steps contain no code. Use "Longfu88 promo code" exactly once; where "Longfu88 promo code" is used, it sits in a sentence that says the claiming route is the My Bonuses activation after the qualifying deposit and that no promo code step is part of the listed claiming procedure; never invent, name or hint at a code. Name the two alternatives in one sentence: the Live Casino Welcome Bonus (125% up to €888, minimum deposit €30) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, minimum deposit 50 USDT); say the Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers. Use "Longfu88 bonus" exactly once; where "Longfu88 bonus" is used, it sits in the sentence that gives the percentage and the maximum amount. Use "Longfu88" exactly once and no other tracked keyword. Do not explain wagering, maximum bet or validity here (next sub-section).')

    # b08 terms
    add(3, "Wagering, Validity and Bet Limits", "unique", [],
        ["brandinfo_welcome.welcome_bonus.wagering_requirement", "brandinfo_welcome.welcome_bonus.free_spins_wagering", "brandinfo_welcome.welcome_bonus.validity",
         "brandinfo_welcome.welcome_bonus.maximum_bet", "brandinfo_welcome.welcome_bonus.maximum_cashout", "brandinfo_welcome.welcome_bonus.important_terms"], 70,
        {"Longfu88": 1}, ["paragraph", "table"],
        [("Wagering Requirement", 10), ("Maximum Bet", 7), ("Maximum Cashout", 7), ("Bonus Validity", 6), ("Free Spins Winnings", 6)],
        [("Wagering Requirement", "is 25 times", "the deposit plus the bonus amount", 9), ("Bonus", "expires", "10 days after activation", 7)],
        "The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.",
        'One lead-in sentence, then a Markdown table Condition | Value with the rows: wagering (25x the deposit plus bonus amount), free spins wagering (40x Free Spins winnings), validity (10 days from activation), maximum bet (€22.5 per spin), maximum cashout (5x the initial bonus amount). After the table, one or two sentences on the exclusions and rules: Neteller and Skrill deposits are excluded, only one promotional bonus can be active at a time, a withdrawal request before claiming or while the bonus is active can void eligibility, cancelling forfeits bonus funds and unconverted winnings, verification may be required before bonus winnings are paid. Use "Longfu88" exactly once and no other tracked keyword. Keep tracked keywords out of table cells.',
        listed=["Wagering Requirement", "Maximum Bet", "Maximum Cashout", "Bonus Validity", "Free Spins Winnings"])

    # b09 ongoing promos
    add(2, "Reloads and Seasonal Promotions", "mandatory", ["k11"],
        [f"brandinfo_promotions.other_bonuses[{i}]" for i in (2, 3, 4, 5, 6, 7, 8)], 85, {}, ["paragraph", "table"],
        [("Weekly Reload", 9), ("Weekend Reload", 8), ("Crypto Reload", 7), ("One-Day Reload Special", 5), ("Seasonal Promotion", 5), ("Free Spins", 5)],
        [("Weekly Reload", "gives", "50 Free Spins", 7), ("Promotions", "cannot be combined with", "another active casino bonus", 8)],
        "The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.",
        'One lead-in sentence, then a Markdown table Offer | Reward | Min. deposit | Wagering | Validity for the seven offers as given: Casino Weekly Reload, Casino Weekly Crypto Reload, Casino Weekend Reload, Casino Weekend Crypto Reload, Casino Double Fortune (one-day reload special), Casino Trick or Treat Pumpkin Bonanza, Casino Dragon Quest (verification reward). After the table state the shared rules once: activation in My Bonuses, one claim per promotional period, no combination with another active casino bonus, maximum stake €5 per spin while wagering bonus funds.',
        listed=["Weekly Reload", "Weekend Reload", "Crypto Reload", "One-Day Reload Special", "Seasonal Promotion"])

    # b10 cashback
    add(3, "Cashback and Rebates", "unique", [],
        [f"brandinfo_promotions.other_bonuses[{i}]" for i in (9, 10, 11, 12, 13, 14)], 55, {}, ["paragraph", "table"],
        [("Weekly Cashback", 10), ("Live Casino Cashback", 8), ("Unlimited Rebate", 7), ("VIP Cashback Rates", 6)],
        [("Weekly Cashback", "returns", "up to 10% of weekly net casino losses", 9), ("Rebates", "are credited", "daily", 7)],
        "Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.",
        'Cover the Casino Weekly Cashback (up to 10% of weekly net casino losses, capped at €6,988; period Monday 00:00 UTC to Sunday 23:59 UTC; opt-in for a four-week cycle; credited to My Bonuses on Monday; 10x wagering of the cashback; the rate depends on the VIP tier: Bronze 2%, Silver 4%, Gold 6%, Platinum 8%, Diamond 10%, shown as a compact table of tier, percentage and maximum) and the Live Casino Cashback (25% up to €850). Mention the four daily rebates in one sentence (casino 0.9%, live casino 1.0%, P2P 0.8%, lottery 1.0%, each with 1x wagering). Only real-money bets count, bonus funds do not. The tier percentages here belong to the weekly cashback; do not mix them with the VIP level percentages of the VIP section.')

    # b11 rewards hub
    add(3, "Rewards Hub: Bonus Crab, Wheel and Coin Shop", "unique", [],
        ["brandinfo_promotions.gamification_features"], 55, {}, ["paragraph"],
        [("Bonus Crab", 8), ("Wheel of Fortune", 7), ("Challenges", 6), ("Collections", 5), ("Coin Shop", 6)],
        [("Coins", "are exchanged in", "the Coin Shop for rewards", 7), ("Challenges", "unlock", "coins, free spins and bonus credits", 6)],
        "The gamification features of the rewards area: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop.",
        'Describe the five features in short sentences as given: Bonus Crab (claim picks to open a crab reward, valid 7 days, 30x on bonus credit and 40x on free spin winnings), Wheel of Fortune (spend an eligible spin or Coins, 7 days, 30x), Challenges and Collections (found under Rewards), Coin Shop (exchange Coins for rewards and bonus credits up to €4,500, prices vary by item, separate wagering may apply). Say that rewards can carry their own wagering requirements.')

    # b12 VIP
    add(2, "Longfu88 VIP Programme", "mandatory", ["k12"],
        ["brandinfo_loyalty.loyalty_vip_program.name", "brandinfo_loyalty.loyalty_vip_program.tiers", "brandinfo_loyalty.loyalty_vip_program.progression",
         "brandinfo_loyalty.loyalty_vip_program.levels[0]", "brandinfo_loyalty.loyalty_vip_program.levels[3]", "brandinfo_loyalty.loyalty_vip_program.levels[4]", "brandinfo_loyalty.loyalty_vip_program.levels[9]",
         "brandinfo_loyalty.loyalty_vip_program.levels[14]", "brandinfo_loyalty.loyalty_vip_program.levels[19]", "brandinfo_loyalty.loyalty_vip_program.levels[24]",
         "brandinfo_loyalty.loyalty_vip_program.additional_benefits", "brandinfo_loyalty.loyalty_vip_program.important_terms"], 75, {"Longfu88": 0}, ["paragraph", "table"],
        [("VIP Programme", 10), ("VIP Points", 8), ("VIP Levels", 8), ("Withdrawal Limits", 6), ("Personal VIP Manager", 5)],
        [("VIP Points", "unlock", "numbered reward levels", 8), ("Higher VIP Levels", "raise", "withdrawal limits and cashback", 7)],
        "How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.",
        'Explain that VIP points come from eligible real-money play and unlock numbered reward levels (25 levels grouped into the tiers Bronze, Silver, Gold, Platinum and Diamond). Show a compact table Level | Points | Reward | Cashback | Withdrawal limit for levels 1, 5, 10, 15, 20 and 25 exactly as given in the Brand Information (level 1: 1 point, €9.8, 1%, €9,800; level 25: 5,500 points, €980, 10%, €147,000). Say what higher levels add: personalised offers, cashback, higher withdrawal limits and a personal VIP manager from level 4. Reward and withdrawal limits may differ by VIP level and currency and the rules can change. The programme name "Longfu88 VIP Program" as given contains the tracked keyword "Longfu88": if the name is printed it counts toward the exact count of this block. Do not repeat the weekly cashback tier table (cashback section).',
        listed=["VIP Levels"])
    blocks[-1]["heading"] = "Longfu88 VIP Programme"

    # b13 games overview
    add(2, "Games Overview", "mandatory", ["k02"],
        ["brandinfo_games.game_types"], 60, {"Longfu88": 1, "Longfu88 casino": 1}, ["paragraph"],
        [("Game Categories", 10), ("Slots", 7), ("Live Dealer Games", 7), ("Jackpots", 5), ("Crash Games", 5)],
        [("Online Casino", "offers", "slots, live dealer games, table games, jackpots, fishing, P2P, fast games, lottery and crash games", 8)],
        "The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.",
        'Name the nine categories of the Brand Information in flowing text and lead into the sub-sections on slots, live casino and the other categories without retelling their facts. Do not state a number of games or providers: none is given. Use "Longfu88 casino" (the name Longfu88 Casino) exactly once and "Longfu88" exactly once, and no other tracked keyword.')

    # b14 slots
    add(3, "Slots", "mandatory", ["k03"], ["brandinfo_games.game_examples"], 70, {}, ["paragraph"],
        [("Slots", 10), ("Gates of Olympus", 7), ("Sweet Bonanza", 7), ("Wanted Dead or a Wild", 7), ("RTP", 6), ("Volatility", 5)],
        [("Gates of Olympus", "has", "an RTP of 96.50% and a maximum multiplier of 5,000x", 7), ("Hacksaw Gaming", "supplies", "Wanted Dead or a Wild", 6)],
        "Three example slots with their provider, RTP, volatility and maximum multiplier.",
        'Name the three example slots with the figures exactly as in the Brand Information: Gates of Olympus (Pragmatic Play, RTP 96.50%, high volatility, 5,000x), Sweet Bonanza (Pragmatic Play, RTP 96.48%, high volatility, 21,175x) and Wanted Dead or a Wild (Hacksaw Gaming, RTP 96.38%, very high volatility, 12,500x). Explain in one sentence what RTP and volatility mean for the player. Do not claim that these are the only or the most popular slots and name no other title.')

    # b15 live casino
    add(3, "Live Casino", "mandatory", ["k04"], ["brandinfo_games.original_games", "brandinfo_games.providers[0]", "brandinfo_games.providers[6]"], 65,
        {"Longfu 88 casino": 1, "Longfu88": 1}, ["paragraph"],
        [("Live Dealer Games", 10), ("Evolution", 7), ("SA Gaming", 6), ("Longfu88 Baccarat", 6)],
        [("Live Casino", "includes", "the exclusive Longfu88 Baccarat", 7), ("Live Casino", "is powered by", "Evolution and SA Gaming among other studios", 6)],
        "The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.",
        'Describe the live dealer section as a category of the lobby, name the exclusive game "Longfu88 Baccarat" exactly as given (an exclusive live or table game with baccarat gameplay; the name is the one occurrence of "Longfu88" of this block) and name Evolution and SA Gaming from the provider list as live studios only if the sentence stays factual (they are in the provider list; do not say which live games each one supplies). Do not name any other live game or show. Use "Longfu 88 casino" exactly once, written in a natural sentence, and no other tracked keyword.')

    # b16 other categories
    add(3, "Table, Fishing, P2P, Fast Games and Lottery", "unique", ["k05", "k06", "k09"], ["brandinfo_games.game_types"], 60, {}, ["paragraph"],
        [("Table Games", 8), ("Fishing Games", 6), ("P2P Games", 6), ("Fast Games", 6), ("Lottery", 6), ("Crash Games", 5)],
        [("Online Casino", "also offers", "fishing, P2P, fast, lottery and crash games", 6)],
        "The remaining game categories in one block: table games, fishing, P2P, fast games, lottery and crash and instant games.",
        'Describe each category in a sentence as a type of game only (what the player does): table games, fishing, P2P (play against other players), fast games, lottery, crash and instant games. Name no titles, no providers per category and no numbers; none are given.')

    # b17 providers
    add(2, "Game Providers", "unique", ["k07"], ["brandinfo_games.providers"], 55, {"Longfu88": 1}, ["paragraph"],
        [("Game Providers", 10), ("Evolution", 7), ("Pragmatic Play", 7), ("Hacksaw Gaming", 6), ("Red Tiger", 5), ("NetEnt", 5)],
        [("Game Providers", "supply", "slots, live and table games to the casino", 7)],
        "Which studios supply the games, named from the provider list.",
        'Name the ten providers of the Brand Information in a running sentence or two, exactly as given: Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft, Hacksaw Gaming. Do not say how many studios there are in total and which game each supplies, except what the slots section states. Use "Longfu88" exactly once and no other tracked keyword.',
        listed=["Evolution", "Pragmatic Play", "Hacksaw Gaming", "Red Tiger", "NetEnt"])

    # b18 sports
    add(2, "Sports Betting", "mandatory", ["k08"],
        ["brandinfo_sportsbook.sportsbook.sports_available", "brandinfo_sportsbook.sportsbook.bet_types", "brandinfo_sportsbook.sportsbook.live_betting",
         "brandinfo_sportsbook.sportsbook.important_terms"], 75, {"Longfu88": 1, "Longfu sports": 1}, ["paragraph"],
        [("Sportsbook", 10), ("Football", 7), ("Esports", 6), ("Live Betting", 7), ("Bet Builder", 5), ("Accumulator", 5)],
        [("Sportsbook", "covers", "football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football", 8), ("Live Betting", "offers", "live odds and in-play markets", 7)],
        "The sportsbook: the sports and esports covered, the bet types and live betting.",
        f'Give the nine sports and esports as listed (football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports, virtual football), the seven bet types (single, accumulator, live, handicap, totals, outrights, Bet Builder) and live betting with live odds and in-play markets. Use "Longfu sports" exactly once; where "Longfu sports" is used, write it as a natural phrase for the sports section (for example the Longfu sports section). Use "Longfu88" exactly once. Event availability and market selection can vary by jurisdiction. Name no sports league or event and no sportsbook platform.')

    # b19 sports bonuses
    add(3, "Sports Bonuses and Promotions", "unique", [], ["brandinfo_sportsbook.sportsbook.sports_bonuses"], 55, {}, ["paragraph", "table"],
        [("Sport First Deposit Bonus", 10), ("Sports Cashback", 7), ("Parlay Boost", 6), ("Bet Builder Risk Free", 5), ("Minimum Odds", 6)],
        [("Sport First Deposit Bonus", "gives", "100% up to €1,888", 8), ("Qualifying Bets", "need", "minimum odds of 2.00 for singles", 7)],
        "The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.",
        'Give a compact table Offer | Reward | Min. deposit | Wagering for the Sport First Deposit Bonus (100% up to €1,888, €50, 8x, 30 days), the Sport Weekly Reload Bonus (50% up to €2,500, €50, 8x) and the Sport Weekend Reload Bonus (50% up to €3,750, €50, 8x); then name the crypto equivalents, Sports Cashback (10% up to €2,500 of eligible sports net losses, weekly), Unlimited Sports Rebate (0.70%), 2 Goals Ahead early payout, Parlay Boost (up to 100% extra winnings, at least three legs) and Bet Builder Risk Free (50% stake return up to €250) in prose. Rules that apply: only settled qualifying sports bets count, single bets need odds of at least 2.00 and each accumulator selection at least 1.50, voided and cashed-out bets do not qualify. Do not mix these with the casino bonuses.',
        listed=["Sport First Deposit Bonus"])

    # b20 payments
    add(2, "Deposit Methods and Limits", "mandatory", ["k14", "k16"],
        ["brandinfo_deposit.deposit_methods", "brandinfo_deposit.deposit_guide", "brandinfo_general.minimum_deposit", "brandinfo_general.currencies"], 90,
        {"Longfu88": 1}, ["paragraph", "table"],
        [("Payment Methods", 10), ("Bank Transfer", 7), ("Cryptocurrency", 7), ("E-wallets", 6), ("Deposit Limits", 7), ("Processing Speed", 6)],
        [("Deposits", "are credited", "within 1-2 minutes", 8), ("Casino", "charges", "no processing fee on deposits, while provider or network fees may apply", 7)],
        f'Deposit methods grouped by type with the general limits and speed, the local options for {g["geo"]} and the six-step deposit route.',
        f'One lead-in sentence, then a Markdown table Method type | Examples | Currencies with the groups: local bank and wallet methods, cards (Visa, Mastercard), bank transfer, cryptocurrencies (Bitcoin, Ethereum, Litecoin, USDT in TRC20, ERC20 and BEP20, USDC and others from the list), e-wallets (Neteller, Skrill) and the European methods (Sofort, Giropay). For {g["geo"]} highlight {g["local"]} as given. General limits for every method: minimum €10, maximum €5,000 per transaction, speed 1-2 minutes, no casino processing fee, provider or blockchain network fees may apply. Do NOT quote the per-currency limit lines of single methods (they mix euro signs with local-currency amounts) and say that the limits can differ by country, currency and method. Neteller and Skrill deposits are excluded from the welcome bonus. After the table, the six deposit steps in one flowing sentence or two. Use "Longfu88" exactly once; keep tracked keywords out of the table.',
        listed=["Bank Transfer", "Cryptocurrency", "E-wallets"])

    # b21 withdrawals
    add(3, "Withdrawals and Payout Times", "unique", ["k15"],
        ["brandinfo_withdrawal.withdrawal_methods", "brandinfo_withdrawal.withdrawal_guide", "brandinfo_privacy_policy.terms_conditions.withdrawal_terms",
         "brandinfo_privacy_policy.terms_conditions.conditional_fees", "brandinfo_general.payment_methods.withdrawal"], 80,
        {"Longfu88": 1, "Lngfu88 withdrawal time": 1}, ["paragraph", "list"],
        [("Withdrawal Time", 10), ("Withdrawal Methods", 8), ("Minimum Withdrawal", 7), ("Withdrawal Fees", 7), ("Deposit Turnover", 6)],
        [("Withdrawal", "is processed within", "up to 3 business days", 9), ("Bank Transfer", "may need", "3-5 more business days for delivery", 7)],
        "How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.",
        'Give the methods as listed (bank transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT in three networks, Touch\'n Go, DANA, MoMo, DBS Bank, Online Banking), the minimum €20 and maximum €5,000, the six steps as a NUMBERED list, and the processing time: card, crypto and wallet withdrawals take 1 to 3 business days; bank transfer takes up to 3 business days for casino processing plus 3 to 5 business days for bank delivery; requests are generally processed within three working days. Use "Lngfu88 withdrawal time" exactly once; where "Lngfu88 withdrawal time" is used, write it verbatim with this spelling in the sentence that gives the processing time. Fees: no standard casino withdrawal fee, provider and blockchain fees may apply; a 10% commission (minimum €2.25) can apply where turnover is below the deposited amount (a minimum 1x deposit turnover can apply before a withdrawal) and 15% on some card or bank transfer funded transactions. Do NOT quote the per-market minimum lines of single methods (they mix euro signs with local-currency amounts). Identity checks can delay a payout (see the verification section). Use "Longfu88" exactly once and no other tracked keyword.')

    # b22 mobile
    add(2, "Mobile Access", "mandatory", ["k17"], ["brandinfo_app.app_information"], 70, {"Longfu88": 0, "Longfu88 app": 1}, ["paragraph", "list"],
        [("Mobile Access", 10), ("Add to Home Screen", 8), ("Android", 6), ("iOS", 6), ("Responsive Website", 7)],
        [("Responsive Website", "works on", "smartphone and tablet browsers", 8), ("Home Screen Shortcut", "gives", "quick access to the casino and sportsbook", 6)],
        "Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.",
        'Explain that the casino runs as a responsive website on smartphone and tablet browsers (platforms Android, iOS and mobile web) and can be added to the home screen as a shortcut; give the Android route (Chrome, browser menu, Add to Home screen, confirm) and the iOS route (Safari, Share, Add to Home Screen, Add) as two short numbered lists, each preceded by one sentence. Name the available functions (casino, sportsbook, account access, deposits, withdrawals, bonuses). Use "Longfu88 app" exactly once; where "Longfu88 app" is used, it sits in a sentence that makes clear it is the home-screen version of the site. Do NOT claim a download from an app store or an APK file: none is given. The brand name appears in the first step of each list only if a verbatim step contains it, and then counts toward the exact count of this block (budgeted at zero extra occurrences: write "the casino" in prose).')
    blocks[-1]["keywords"] = {"Longfu88 app": 1, "Longfu88": 2}
    blocks[-1]["copywriter_notes"] = blocks[-1]["copywriter_notes"].replace(' The brand name appears in the first step of each list only if a verbatim step contains it, and then counts toward the exact count of this block (budgeted at zero extra occurrences: write "the casino" in prose).', ' Step one of the Android list and of the iOS list names the brand as in the Brand Information ("Open Longfu88 in Chrome" and "Open Longfu88 in Safari"); these two occurrences of "Longfu88" are part of the exact count of this block, the rest goes into running text as "the casino".')

    # b23 RG
    add(2, "Responsible Gambling", "mandatory", ["k20"], ["brandinfo_responsible_gaming.responsible_gaming"], 75, {"Longfu88": 0}, ["paragraph", "list"],
        [("Responsible Gambling", 10), ("Self-Exclusion", 8), ("Account Closure", 6), ("Self-Assessment", 5), ("GamCare", 5), ("Gambling Therapy", 5)],
        [("Self-Exclusion", "is requested", "by e-mail to customer support", 8), ("Players", "can seek help from", "GamCare, Gamblers Anonymous and Gambling Therapy", 7)],
        "Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.",
        'State that players must be at least 18 and gamble only where lawful. Explain self-exclusion (requested by e-mail to customer support, restricts access and gambling for the agreed period, processed within 24 hours after the request is processed) and account closure through customer support, the four-step procedure in short, and self-assessment questions that help to spot harm. Give the organisations GamCare, Gamblers Anonymous and Gambling Therapy as a short bulleted list. Say that the page cannot replace independent help. The e-mail address of the Brand Information contains the tracked keyword "Longfu88": write "e-mail customer support" and do not print the address here.')
    blocks[-1]["keywords"] = {"Longfu88": 1}
    blocks[-1]["copywriter_notes"] = blocks[-1]["copywriter_notes"].replace('The e-mail address of the Brand Information contains the tracked keyword "Longfu88": write "e-mail customer support" and do not print the address here.', 'The e-mail address of the Brand Information contains the tracked keyword "Longfu88": when it is printed (for example in the sentence about self-exclusion) it is the one occurrence of this block.')

    # b24 support
    add(2, "Customer Support", "mandatory", ["k19"], ["brandinfo_general.customer_support"], 55, {"Longfu88": 1}, ["paragraph"],
        [("Customer Support", 10), ("Live Chat", 8), ("Email Support", 7), ("Support Languages", 6)],
        [("Live Chat", "is available", "24/7", 8), ("Customer Support", "speaks", "English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese", 6)],
        "Support channels, availability and languages.",
        'Give the two channels (24/7 live chat and e-mail), the e-mail address exactly as given (it contains the tracked keyword "Longfu88" and is the one occurrence of "Longfu88" of this block) and the six support languages (English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese). Do not mention a phone line, a ticket system, an average response time or a social account: none is given.')

    # b25 pros and cons
    add(2, "Pros and Cons", "unique", ["k23"],
        ["brandinfo_general.minimum_deposit", "brandinfo_welcome.welcome_bonus.wagering_requirement", "brandinfo_privacy_policy.terms_conditions.conditional_fees",
         "brandinfo_games.providers", "brandinfo_promotions.other_bonuses[9].reward"], 55, {}, ["table"],
        [("Advantages", 8), ("Disadvantages", 8), ("Welcome Bonus", 6), ("Withdrawal Fees", 5), ("Payment Methods", 5)],
        [("Advantages", "are balanced against", "the conditions that come with them", 7)],
        "A pros and cons table built only from facts stated elsewhere on the page.",
        'A Markdown table with exactly two columns, Pros | Cons, four or five rows. Pros are facts from the page (a low general minimum deposit of €10, a large choice of payment methods including cryptocurrencies, a weekly cashback of up to 10%, a VIP programme with 25 levels, 24/7 live chat); cons are the conditions that go with them (the welcome bonus needs a €50 deposit and 25x wagering on deposit plus bonus, a 10% or 15% commission can apply to withdrawals under the turnover rule, bank withdrawals can take several business days, verification may delay the first payout). No intro sentence beyond one line, no new facts, no tracked keyword in the table.')

    # b26 FAQ
    add(2, "Frequently Asked Questions", "mandatory", ["k22"],
        ["brandinfo_account.login.password_recovery", "brandinfo_general.minimum_deposit", "brandinfo_welcome.welcome_bonus.claiming_procedure"], 60,
        {"Longfu 88": 1, "Longfu88": 1}, ["list"],
        [("Frequently Asked Questions", 8), ("Promo Code", 7), ("Minimum Deposit", 7), ("Withdrawal Time", 7), ("Password Recovery", 6)],
        [("Frequently Asked Questions", "cover", "bonus claiming, minimum deposit, withdrawal time and password recovery", 6)],
        "Four short answers: how to claim the bonus, the minimum deposit, how long a withdrawal takes and how to recover a password.",
        'A bulleted list of exactly four items, each a bold question followed by a short answer of 20-30 words, in this order: (1) how to claim the welcome bonus (activate it in My Bonuses after the first qualifying deposit of €50; no code step is part of the procedure); (2) what is the minimum deposit (€10 in general, €50 for the welcome bonus); (3) how long a withdrawal takes (up to 3 business days of casino processing, then bank or network time; wording must differ from the withdrawals section); (4) how to recover the password (Forgot Password on the login screen, reset link by e-mail): the question must contain the keyword "Longfu 88" in the form "my Longfu 88 account" (exactly once in the block). "Longfu88" goes into one answer, not into a question. These are the only questions on the page; the questions are the one place where question form is allowed. Use "Longfu 88" exactly once and "Longfu88" exactly once.')

    # b27 verdict
    add(2, "Verdict", "mandatory", ["k21"], ["brandinfo_general.minimum_age", "brandinfo_responsible_gaming.responsible_gaming.policy"], 70,
        {"Longfu88": 1, "Longfu": 1, "Longfu88 casino": 1}, ["paragraph"],
        [("Verdict", 10), ("Welcome Bonus Terms", 6), ("Responsible Gambling", 6), ("Minimum Age", 5)],
        [("Player", "should check", "the bonus terms and payment limits before depositing", 7)],
        "A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.",
        f'Close with three or four sentences: which kind of player the facts fit (someone who wants casino, live and sports betting in one account with local and crypto payments), what to check before depositing (the €50 qualifying deposit, 25x wagering, the withdrawal turnover rule and verification), then the 18+ limit with the reminders that gambling is not a source of income, that losses should not be chased and that a budget and breaks help. Use "Longfu88 casino" exactly once; where "Longfu88 casino" is used (the name Longfu88 Casino), it sits in the first sentence. Use "Longfu" exactly once; where "Longfu" is used, write it as the short name of the casino. Use "Longfu88" exactly once. Repeat no figures, make no promises of winnings, no hype. {legal}')

    intent = (f'Brand-related (navigational and informational) review page about the Longfu88 online casino for players from {g["geo"]}: what the casino is, key facts, licence and data protection, registration, login and verification, welcome bonus and its terms, reloads, cashback and rewards, VIP programme, games and providers, sports betting, payments and withdrawals, mobile access, responsible gambling, support, pros and cons, FAQ and verdict. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in {g["geo"]}.')
    return {"intent_summary": intent, "blocks": blocks}


def fit_targets(run, out):
    """Other GEOs have other competitor medians: scale the block sizes to the target body length and let the code nudge the keyword
    counts to the targets (textgen.brief.rebalance_keywords), then print what validate still finds."""
    sys.path.insert(0, ".")
    from textgen import brief as B
    from textgen.config import Settings
    from textgen.store import Run

    r = Run.open(run)
    job, kb, settings = r.job(), r.knowledge_base(), Settings.load()
    targets = B.compute_targets(r.load_json("01_keyword_stats.json"), job.keywords, settings)
    total = sum(round((b["words_min"] + b["words_max"]) / 2) for b in out["blocks"])
    f = targets["target_body_words"] / total
    for b in out["blocks"]:
        mid = (b["words_min"] + b["words_max"]) / 2
        if b.get("fact_table"):
            continue
        b["words_min"], b["words_max"] = max(15, round(mid * f * 0.88)), max(20, round(mid * f * 1.12))
    brief = B.normalize(out, job.keywords, kb)
    B.rebalance_keywords(brief, targets, job.keywords)
    errs = B.validate(brief, targets, job.keywords, settings, r.load_json("01_heading_clusters.json"), kb)
    print("target words", targets["target_body_words"], "scale", round(f, 2), "| validate:", errs or "OK")
    out["blocks"] = brief["blocks"]


def translate_covers(run, out):
    """The blocks carry the cluster ids of the Singapore run; other runs have their own ids: map by topic."""
    old = {c["id"]: c["topic"] for c in json.load(open("runs/longfu88-sg/01_heading_clusters.json", encoding="utf-8"))}
    new = {c["topic"]: c["id"] for c in json.load(open(f"runs/{run}/01_heading_clusters.json", encoding="utf-8"))}
    missing = sorted({old[c] for b in out["blocks"] for c in b["covers_clusters"] if old.get(c) not in new})
    if missing:
        print("topics without a competitor cluster (not needed):", missing)
    for b in out["blocks"]:
        b["covers_clusters"] = [new[old[c]] for c in b["covers_clusters"] if old.get(c) in new]


if __name__ == "__main__":
    run = sys.argv[1]
    out = build(run)
    if run not in ("longfu88-sg", "longfu88-my"):
        translate_covers(run, out)
        fit_targets(run, out)
    path = f"runs/{run}/llm/brief.json"
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(path, len(out["blocks"]), sum(round((b["words_min"] + b["words_max"]) / 2) for b in out["blocks"]))


