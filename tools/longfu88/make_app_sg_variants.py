"""Blueprint of 12 ТЗ variants for the Longfu88 app page (brand-subpage, GEO SG) -> input/variants/longfu88-app-sg.json.
Base run: runs/longfu88-app-sg (tools/longfu88/make_app_sg_base.py, the OPTIMUM group `medium`). Run from the project root:
    python tools/longfu88/make_app_sg_variants.py
    python -m textgen variants input/variants/longfu88-app-sg.json --force
    python tools/longfu88/attach_links_variants.py longfu88-app-sg          (internal links of step 1.7, variants do not get them from textgen)

Size groups (python -m textgen tiers longfu88-app-sg --texts 12):
    small  759       -> target 759,  limit 911      3 variants: v01-v03
    medium 975 / 983 -> target 979,  limit 1175     4 variants: v04-v07
    large  1372/1539 -> limit 1456 (x1.0)           5 variants: v08-v12 (a ceiling: shorter where the facts end)
The sum of the words_max of a text must stay within its limit, so the middles below are chosen with that in mind.

Base blocks: b01 intro, b02 what works on a phone, b03 install lead, b04 Android steps, b05 iOS steps, b06 devices and browsers,
b07 shortcut or browser tab, b08 account access, b09 security, b10 troubleshooting, b11 support, b12 FAQ.
The App knowledge base is poor (a home-screen shortcut only), so the topics that make the texts differ come from the neighbouring
sections of the same knowledge base (games, sports, payments, withdrawals, welcome offer, registration, verification, responsible
gaming, data, eligibility, currencies), one or two short blocks each. Every variant has its own set of base blocks (the mandatory
clusters that the page leaves out are listed in `skipped_clusters`, at most half of them), its own set of those extra topics and its own
depth for the topics it shares (facts, format, size, level). The install trio b03-b05 is kept in every text because the keywords
download / Android / iOS / apk live there; its depth differs (merged, nested, ordered differently).
The knowledge base has no native app, so every block repeats the NO_APP_CLAIMS rule of the base notes."""
import json
from pathlib import Path

K0, K_APP, K_LAPP, K_IOS, K_AND, K_APK, K_DL, K_MC = ("Longfu88", "Longfu88 app", "Longfu app", "Longfu88 iOS", "Longfu88 Android",
                                                      "Longfu88 apk", "Longfu88 download", "Longfu88 mobile casino")

# exact pieces of the base notes (tools/longfu88/make_app_sg_base.py) that a variant changes
B02_LIST = ("then a bulleted list with the six items of the Brand Information in the order given (casino, sportsbook, account access, deposits, withdrawals, bonuses), "
            "each item a short phrase of 3-6 words saying what the player can do, then one closing sentence.")
B02_PROSE = ("then one flowing paragraph that names the six items of the Brand Information in the order given (casino, sportsbook, account access, deposits, withdrawals, bonuses) "
             "and says what the player can do with each, in a few words.")
B10_LIST = 'then a bulleted list of four items "problem: fix":'
B10_PROSE = 'then one short paragraph with four problems and the plain fix for each, in this order:'

NO_APP_CLAIMS = ("Do not say or imply that a native app, an APK or IPA file, a file download, an app-store listing (Google Play, App Store), a version number, push notifications, "
                 "fingerprint or Face ID login, an offline mode, an in-app chat, or system requirements (OS versions, storage, memory, internet speed) exist: none of them is given. "
                 "Mobile access is the responsive website in the browser of a smartphone or a tablet, plus a home-screen shortcut.")
NO_SECURITY_CLAIMS = "Do not mention two-factor authentication, SMS codes, CAPTCHA, SSL, TLS, encryption, code signing, biometric login or an audit: no such protection is given."
NO_LIMITS = "Do not quote any limit, minimum or maximum amount of a payment method and do not convert amounts."
NO_INVENT = "Use only the facts of the Brand Information of this block, character for character; add no other fact, no promise of winnings and no comparison with other casinos."
LEGAL = "Do not say or imply that the casino is licensed, legal or approved in Singapore, and do not discuss the licence on this page."
VOICE_TAIL = " All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore."

FAQ = {
    "app": ("is there a store app to download (no: the casino opens in the browser and is added to the home screen as a shortcut)", ["brandinfo_app.app_information.mobile_access"]),
    "phones": ("which phones work (Android, iOS and the mobile web of smartphones and tablets)", ["brandinfo_app.app_information.platforms"]),
    "android": ("how the Android shortcut is added (open the casino website in Chrome, choose Add to Home screen in the browser menu, confirm the shortcut)",
                ["brandinfo_app.app_information.android_installation"]),
    "ios": ("how the iOS shortcut is added (open the casino website in Safari, tap Share, choose Add to Home Screen, confirm Add)", ["brandinfo_app.app_information.ios_installation"]),
    "login": ("how a player logs in on a phone (with the registered e-mail and password, as on a computer)", ["brandinfo_account.login.method"]),
    "support": ("where to turn when something fails (customer support: live chat 24/7 or e-mail; do not print the e-mail address)", ["brandinfo_general.customer_support.channels"]),
    "age": ("what the minimum age is (18, and the player must be legally permitted to gamble where they live)", ["brandinfo_general.minimum_age"]),
    "tablet": ("whether a tablet works too (yes: the website is usable in smartphone and tablet browsers)", ["brandinfo_app.app_information.mobile_access"]),
    "features": ("what a player can do from a phone (casino, sportsbook, account access, deposits, withdrawals, bonuses)", ["brandinfo_app.app_information.features"]),
    "lang": ("which languages support speaks (English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese)", ["brandinfo_general.customer_support.languages"]),
    "tab": ("whether the shortcut is required (no: the same website opens in a browser tab)", ["brandinfo_app.app_information.mobile_access"]),
    "sports": ("whether the sportsbook is on the phone too (yes: the sportsbook is one of the features of the mobile website)", ["brandinfo_app.app_information.features"]),
    "reg": ("how a player opens an account on a phone (by e-mail, with the registration form of the website)", ["brandinfo_account.registration.methods"]),
}
BASE_FAQ_REFS = ["brandinfo_app.app_information.platforms", "brandinfo_app.app_information.mobile_access", "brandinfo_account.login.method",
                 "brandinfo_general.minimum_age", "brandinfo_general.customer_support.channels"]

NID: dict[str, str] = {}  # heading -> id of the extra topic (for the honest structure report)


def faq(keys):
    """Override of the FAQ block: the questions of this variant, in order, and only the facts they need."""
    qs = "; ".join(f"({i}) {FAQ[k][0]}" for i, k in enumerate(keys, 1))
    notes = (f'A bulleted list of {len(keys)} items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required '
             f"here for the question text only. Questions, in this order: {qs}. Answers repeat the facts of the sections of the page in other words and add "
             f"nothing new. {NO_APP_CLAIMS}")
    need = list(dict.fromkeys(r for k in keys for r in FAQ[k][1]))
    return {"notes": notes, "refs_add": [r for r in need if r not in BASE_FAQ_REFS], "refs_drop": [r for r in BASE_FAQ_REFS if r not in need],
            "summary": f"{len(keys)} short questions and answers on the mobile version of the casino."}


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


def intro(heading, words, kw, topics, ka=True, km=True, first=None):
    """H1 block with its own notes (the base notes name both phrases; a variant may put one of them into a heading)."""
    first = first or ('Open with the keyword "Longfu88" as the subject of the first sentence: the casino is used on a smartphone or tablet through its responsive website, '
                      'on Android and iOS.')
    parts = [first]
    if km:
        parts.append('The phrase "Longfu88 mobile casino" stands once, in a sentence that says what the Longfu88 mobile casino is (the responsive website in the phone browser).')
    if ka:
        parts.append('The phrase "Longfu app" stands once, in a sentence that says that players who look for the Longfu app will find the mobile version of the website '
                     'with a home-screen shortcut (not a store app).')
    parts.append("State once that the casino is for players aged 18 or over and that the page is written for players from Singapore. "
                 f"Signpost the topics of the page in one sentence {topics} without detail. {LEGAL} {NO_APP_CLAIMS} Neutral tone, no promises.")
    return blk(["b01"], 1, heading, words, kw, notes=" ".join(parts))


def new(nid, level, heading, words, refs, ents, conns, summary, notes, covers, fmt=None, kw=None):
    """A block that the base ТЗ does not have: its facts come from `refs` only."""
    NID[heading.lower()] = nid
    return blk([], level, heading, words, kw or {}, fmt, summary=summary, entities=ents, connections=conns, kb_refs=refs, notes=notes, covers_clusters=covers)


PL = ["paragraph", "list"]
PT = ["paragraph", "table"]

# ---------------------------------------------------------------- the install trio
INSTALL_FLAT_HEAD = ("Three parts in ONE continuous section without sub-headings, in this order. (1) Two or three sentences: the casino works in the browser of a smartphone or tablet and a "
                     "home-screen shortcut is added once; one sentence says that nobody needs an installation file or an APK because the casino opens in the mobile browser and is added to the "
                     "home screen as a shortcut (no file and no store listing); where the phrases \"Longfu88 apk\", \"Longfu88 download\", \"Longfu88 Android\" or \"Longfu88 iOS\" are used they stand "
                     "in these sentences. ")
INSTALL_FLAT_LISTS = ("(2) Android: one lead-in sentence, then a NUMBERED list with the three steps in the order of the Brand Information (open the casino website in Chrome; open the browser "
                      "menu and choose Add to Home screen; confirm the shortcut). (3) iOS: one lead-in sentence, then a NUMBERED list with the three steps in the order of the Brand "
                      "Information (open the casino website in Safari; tap Share and choose Add to Home Screen; confirm Add). The tracked keywords belong to the sentences before the lists; write "
                      "\"the site\" or \"the casino website\" in the steps instead of the brand name. Do not give a download link, file size or version number. ")
INSTALL_REFS = ["brandinfo_app.app_information.mobile_access"]


# ---------------------------------------------------------------- extra topics (neighbouring sections of the knowledge base)
def n_games(heading, words, level=2, short=False):
    return new("games", level, heading, words, ["brandinfo_games.game_types"] + ([] if short else ["brandinfo_games.providers"]),
               [["Casino Games", 10]] + ([] if short else [["Game Providers", 6]]),
               [["Player", "chooses", "among slots, live dealer games, table games, jackpots and other categories in the casino", 8]],
               "Which game categories" + ("" if short else " and providers") + " the casino section of the mobile website offers.",
               "One lead-in sentence that says that the casino section of the mobile website offers these game categories, then a bulleted list of the categories exactly as in the Brand Information "
               "(slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, crash and instant games)."
               + ("" if short else " One closing sentence names four or five providers from the list of the Brand Information (for example Evolution, Pragmatic Play, NetEnt, Hacksaw Gaming).")
               + " No game names, RTP values, volatility, maximum multipliers or claims that a particular game works on a phone. " + NO_APP_CLAIMS, ["k08"], PL)


def n_sports(heading, words, level=2, short=False):
    refs = ["brandinfo_sportsbook.sportsbook.sports_available", "brandinfo_sportsbook.sportsbook.live_betting"]
    if not short:
        refs += ["brandinfo_sportsbook.sportsbook.bet_types", "brandinfo_sportsbook.sportsbook.important_terms"]
    return new("sports", level, heading, words, refs, [["Sportsbook", 10], ["Live Betting", 8]], [["Live Betting", "offers", "live odds and in-play markets", 8]],
               "Which sports" + ("" if short else " and bet types") + " the sportsbook offers and that live betting has live odds and in-play markets.",
               "The sportsbook is one of the features of the mobile website. One lead-in sentence, then a bulleted list of the sports as given (football, basketball, tennis, badminton, cricket, table tennis, "
               "volleyball, esports, virtual football)" + ("." if short else ", then one sentence with the bet types (single, accumulator, live, handicap, totals, outrights, Bet Builder)")
               + " and one with live betting: live odds and in-play markets."
               + ("" if short else " Say that event availability and markets can vary by jurisdiction.")
               + " No odds, bonuses, limits or promises of winnings. " + NO_APP_CLAIMS, ["k05"], PL)


def n_pay(heading, words, level=2, rows=4):
    idx = [(20, "PayNow"), (21, "PayNow QR"), (7, "DBS Bank"), (17, "OCBC Bank")][:rows]
    refs = [f"brandinfo_deposit.deposit_methods[{i}].{f}" for i, _ in idx for f in ("method", "currencies", "transaction_speed")]
    names = ", ".join(n for _, n in idx)
    return new("pay", level, heading, words, refs, [["Payment Methods", 10], ["Deposits", 7]], [["Player", "pays", f"with {names} in Singapore dollars", 8]],
               f"{rows} payment methods in Singapore dollars with their deposit speed.",
               f"One lead-in sentence that says that the cashier is part of the mobile website, then a TABLE with three columns, method | currency | deposit speed, and {rows} rows in this order: "
               f"{names} (currency SGD and the speed exactly as in the Brand Information). " + NO_LIMITS + " Name no other payment methods and no fees. " + NO_APP_CLAIMS,
               ["k09"], PT)


def n_wd(heading, words, level=2, short=False):
    refs = ["brandinfo_withdrawal.withdrawal_guide", "brandinfo_privacy_policy.terms_conditions.withdrawal_terms[1]"]
    if not short:
        refs += ["brandinfo_privacy_policy.terms_conditions.withdrawal_terms[2]", "brandinfo_privacy_policy.terms_conditions.withdrawal_terms[3]"]
    return new("wd", level, heading, words, refs, [["Withdrawal", 10], ["Cashier", 6]], [["Player", "submits", "a withdrawal request in the cashier and waits for casino processing", 8]],
               "The six steps of a withdrawal request from the cashier and how long processing takes.",
               "One lead-in sentence that says that the cashier is part of the mobile website, then a NUMBERED list with the six steps of the withdrawal guide in the order of the Brand Information "
               "(write \"the casino\" or \"the cashier\" where a step names the brand). After the list "
               + ("one sentence: requests are generally processed within three working days."
                  if short else "two sentences: requests are generally processed within three working days; bank transfers may need another 3-5 business days; the operator may request KYC documents before processing.")
               + " " + NO_LIMITS + " No fees, no limits, no speed promises beyond those sentences. " + NO_APP_CLAIMS, ["k10"], PL)


def n_welcome(heading, words, level=2):
    refs = [f"brandinfo_welcome.welcome_bonus.{f}" for f in ("name", "bonus_percentage", "maximum_bonus", "free_spins", "minimum_deposit", "wagering_requirement")]
    return new("welcome", level, heading, words, refs, [["Casino Welcome Bonus", 10], ["First Deposit", 7]],
               [["Casino Welcome Bonus", "requires", "a first qualifying deposit of €50 and activation in My Bonuses", 8]],
               "What a new account can claim: the Casino Welcome Bonus, its size, the minimum first deposit and the wagering.",
               "Strictly the Brand Information: the Casino Welcome Bonus is a first-deposit casino bonus of 188% up to €2,088 plus 18 free spins; the minimum first deposit is €50; wagering is 25x the "
               "deposit plus bonus amount; the bonus is activated in My Bonuses before placing any wager. Use the €50 minimum of the bonus; do NOT mention the general minimum deposit of €10. No terms that "
               "are not listed and no promises of winnings. " + NO_APP_CLAIMS, ["k14"])


def n_kyc(heading, words, level=2, short=False):
    refs = ["brandinfo_account.verification.triggers", "brandinfo_account.verification.documents", "brandinfo_account.verification.document_submission_window"]
    if not short:
        refs += ["brandinfo_account.verification.typical_review_time"]
    return new("kyc", level, heading, words, refs, [["Account Verification", 10], ["Identity Documents", 7]],
               [["Account Verification", "may be requested", "before a withdrawal or after unusual activity", 8]],
               "When verification can be requested and which documents are needed.",
               "One lead-in sentence that says when verification can be requested (account review, before a withdrawal, unusual or high-value transactions, changes to account or payment details), then a bulleted "
               "list of the four document types of the Brand Information (government-issued photo ID or passport, proof of residential address, proof of ownership of a payment method, source of funds "
               "or wealth documents when requested), then one sentence: documents are submitted within up to 30 days when requested"
               + ("." if short else " and a complete set is typically reviewed within up to 10 days.") + " " + NO_INVENT + " " + NO_APP_CLAIMS, [], PL)


def n_rg(heading, words, level=2, short=False):
    base = "brandinfo_responsible_gaming.responsible_gaming"
    refs = [f"{base}.policy", f"{base}.self_assessment", f"{base}.support_organizations"]
    if not short:
        refs += [f"{base}.account_closure", f"{base}.self_exclusion.effect"]
    return new("rg", level, heading, words, refs, [["Responsible Gaming", 10], ["Self-Assessment", 6]],
               [["Self-Assessment", "helps", "players identify possible gambling-related harm", 8]],
               "Responsible gaming on the mobile website: the age rule, self-assessment" + ("" if short else ", account closure, self-exclusion") + " and independent support organisations.",
               "State the policy as given: players must be at least 18 years old and gamble only where lawful. Then the self-assessment questions that help players identify possible gambling-related harm"
               + ("" if short else ", the closure of the account on request through customer support and that self-exclusion may restrict account access and gambling for the agreed period")
               + ", and name the independent support organisations (GamCare, Gamblers Anonymous, Gambling Therapy). Do not print any contact address and do not quote the processing time. "
               + NO_INVENT + " " + NO_APP_CLAIMS, [])


def n_reg(heading, words, level=2, short=False):
    refs = ["brandinfo_account.registration.steps", "brandinfo_account.registration.required_details"]
    if not short:
        refs += ["brandinfo_account.registration.eligibility"]
    return new("reg", level, heading, words, refs, [["Registration", 10], ["Required Details", 6]],
               [["Player", "registers", "with an e-mail address and a password on the registration form", 8]],
               "The five steps of the registration form with the details it asks for.",
               "One lead-in sentence, then a NUMBERED list with the five steps of the Brand Information in order (write \"the website\" where a step names the brand), then one sentence with the required "
               "details (e-mail, password, legal name, date of birth, residential address)"
               + ("." if short else " and one with the eligibility rules: 18 or over, legally permitted to gamble where the player lives, one personal account per player.")
               + " " + NO_SECURITY_CLAIMS + " " + NO_APP_CLAIMS, ["k03"], PL)


def n_data(heading, words, level=2, short=False):
    refs = ["brandinfo_privacy_policy.privacy_policy.data_collected.technical_data", "brandinfo_privacy_policy.privacy_policy.cookies"]
    if not short:
        refs += ["brandinfo_privacy_policy.privacy_policy.data_sharing"]
    return new("data", level, heading, words, refs, [["Technical Data", 10], ["Cookies", 7]],
               [["Mobile Website", "collects", "technical data such as the IP address, device data, browser information and cookies", 8]],
               "Which technical data the website collects from a phone and what the cookies are for.",
               "The technical data collected by the website: IP address, device data, browser information and cookies; the cookies are necessary, preference, analytics and marketing cookies that support website "
               "functions and measurement" + ("." if short else "; the data may be shared with payment service providers, identity verification providers, technology providers and, when required, regulators and law enforcement.")
               + " Do not print the contact addresses of the privacy policy. " + NO_SECURITY_CLAIMS + " " + NO_APP_CLAIMS, [])


def n_elig(heading, words, level=2):
    base = "brandinfo_privacy_policy.terms_conditions.eligibility"
    return new("elig", level, heading, words, [f"{base}.minimum_age", f"{base}.residency_requirements", f"{base}.player_requirements"],
               [["Eligibility", 10], ["Player Requirements", 6]], [["Player", "meets", "the age, residence and account rules of the terms", 8]],
               "Who can play: the minimum age, the residence rule and the account rules.",
               "State the rules as given: the minimum age is 18; players must be legally permitted to gamble in their place of residence (say this as a rule of the terms, never as a statement that the casino "
               "is legal in Singapore); the player registers with accurate information, uses only one personal account and does not use third-party payment methods. "
               + LEGAL + " " + NO_APP_CLAIMS, [], PL)


def n_cur(heading, words, level=2):
    return new("cur", level, heading, words, ["brandinfo_general.currencies", "brandinfo_general.customer_support.languages"],
               [["Currencies", 10], ["Support Languages", 6]], [["Casino", "accepts", "EUR, USD, MYR, THB, SGD and USDT", 8]],
               "The currencies of the casino and the languages of the support team.",
               "Name the six currencies exactly as given (EUR, USD, MYR, THB, SGD, USDT) in one sentence and the six support languages (English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese) in another. "
               "Do not convert amounts and do not say which currency a player should choose. " + NO_APP_CLAIMS, [])


def n_vip(heading, words, level=2):
    base = "brandinfo_loyalty.loyalty_vip_program"
    return new("vip", level, heading, words, [f"{base}.name", f"{base}.tiers", f"{base}.progression", f"{base}.additional_benefits"],
               [["VIP Program", 10], ["VIP Points", 7]], [["VIP Points", "unlock", "numbered reward levels", 8]],
               "The VIP programme: five tiers, VIP points from real-money play that unlock reward levels, and the additional benefits.",
               "Name the programme as given in the Brand Information (it carries the brand name, which is the one occurrence of the keyword of this block), the five tiers (Bronze, Silver, Gold, Platinum, "
               "Diamond), that VIP points are earned through eligible real-money gameplay and unlock numbered reward levels, and the four additional benefits (personalised offers, VIP cashback, higher withdrawal "
               "limits, a personal VIP manager for eligible high tiers). No level rewards, no cashback percentages, no limits. " + NO_INVENT + " " + NO_APP_CLAIMS, [], PL, {K0: 1})


def n_promo(heading, words, level=2):
    p = "brandinfo_promotions.other_bonuses"
    return new("promo", level, heading, words, [f"{p}[9].name", f"{p}[9].reward", f"{p}[9].opt_in", f"{p}[4].name", f"{p}[4].reward", f"{p}[4].minimum_deposit"],
               [["Casino Weekly Cashback", 10], ["Casino Weekend Reload", 8]], [["Casino Weekly Cashback", "returns", "up to 10% of weekly net casino losses", 8]],
               "Two ongoing offers a phone player can use: the weekly cashback and the weekend reload.",
               "Two offers, one sentence or two each, exactly as in the Brand Information: the Casino Weekly Cashback returns up to 10% of weekly net casino losses, capped at €6,988, and the player opts in for a "
               "four-week cycle; the Casino Weekend Reload is up to €3,360 + 50 Free Spins with a minimum deposit of €50. One closing sentence: offers are activated in My Bonuses. No wagering figures, no VIP cashback "
               "levels, no promises of winnings. " + NO_INVENT + " " + NO_APP_CLAIMS, [])


variants = []

# ================================================================ SMALL (target 759, limit 911): the most important blocks only
variants.append({
    "id": "v01", "name": "Quick shortcut guide (small, flat)", "tier": "small", "angle": "A player who wants the shortcut on the phone within a minute.",
    "intent_summary": ("Short brand-subpage for the small size group of the competitors: putting the Longfu88 casino on the home screen of a phone in Singapore in the fewest words: the "
                       "shortcut steps for Android and iOS in one section, what works on mobile, devices, login, fixes and a very short FAQ; no security, support or tab-versus-shortcut sections. "
                       "Page voice: short, dense paragraphs of two sentences, sentences of about 14 words, imperative where a step is described, no scene-setting, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 App Quick Guide: Mobile Casino on a Singapore Phone", 65, {K0: 1, K_LAPP: 1, K_MC: 1}, "(shortcut steps for Android and iOS, features, devices, login, fixes)"),
        blk(["b03", "b04", "b05"], 2, "Longfu88 Download: Android and iOS Shortcut Steps", 195, {K_AND: 1, K_IOS: 1, K_APK: 1}, PL,
            notes=INSTALL_FLAT_HEAD + INSTALL_FLAT_LISTS + NO_APP_CLAIMS, summary="Why no file is needed and the shortcut steps for Android in Chrome and iOS in Safari."),
        blk(["b02"], 2, "What Works on Mobile", 100, {K0: 1}),
        blk(["b06"], 2, "Phones and Browsers", 70, {K0: 1}),
        blk(["b08"], 2, "Logging In from a Phone", 85, {K0: 1}),
        blk(["b10"], 2, "If Something Fails", 90, {K0: 1}),
        blk(["b12"], 2, "Quick Questions and Answers", 110, {K0: 1}, **faq(["app", "phones", "android", "login", "support"])),
    ],
})

variants.append({
    "id": "v02", "name": "Android first (small)", "tier": "small", "angle": "A player on an Android phone who wants the Chrome steps first.",
    "intent_summary": ("Short brand-subpage for the small size group: a player with an Android phone in Singapore adds the Longfu88 casino to the home screen in Chrome, and an iPhone or iPad "
                       "user finds the Safari steps right below; then the choice between the shortcut and a browser tab, how the account is protected, which technical data the website collects, "
                       "support and a short FAQ; no device list, login or fixes sections. "
                       "Page voice: a practical guide in plain \"first, then\" order, sentences of about 15 words, one plain recommendation. Flat H2s with one H3." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Android Casino: Add It to Your Phone in Chrome", 60, {K0: 1, K_LAPP: 1, K_MC: 1}, "(Android and iOS shortcut steps, shortcut or browser tab, safety, technical data, support)"),
        blk(["b03", "b04"], 2, "Longfu88 Download: Android Home Screen Shortcut", 150, {K_APK: 1, K0: 1}, PL,
            notes=("Two parts in ONE continuous section without sub-headings. (1) Two or three sentences: the casino works in the browser of a smartphone or tablet; one sentence says that "
                   "nobody needs an installation file or an APK because the casino opens in the mobile browser and is added to the home screen as a shortcut (no file and no store listing); "
                   "where the phrase \"Longfu88 apk\" is used it stands in these sentences. (2) Android: one lead-in sentence, then a NUMBERED list with the three steps in "
                   "the order of the Brand Information (open the casino website in Chrome; open the browser menu and choose Add to Home screen; confirm the shortcut). Write \"the site\" or "
                   "\"the casino website\" in the steps instead of the brand name; tracked keywords belong to the sentences before the list. Do not give a download link, file size or version "
                   "number. " + NO_APP_CLAIMS),
            summary="Why no file is needed and the three Android steps in Chrome."),
        blk(["b05"], 3, "Longfu88 iOS: Safari Steps for iPhone Owners", 55, {}),
        blk(["b07"], 2, "Shortcut or Browser Tab", 100, {K0: 1}),
        blk(["b09"], 2, "How the Account Stays Safe", 100, {K0: 1}),
        n_data("Data the Mobile Website Collects", 70, short=True),
        blk(["b11"], 2, "Contact Support", 60, {K0: 1}),
        blk(["b12"], 2, "Longfu88 App Questions: Chrome and Safari", 105, {K0: 1}, **faq(["app", "android", "ios", "tab", "support"])),
    ],
})

variants.append({
    "id": "v03", "name": "Checklist (small, lists and tables)", "tier": "small", "angle": "A reader who works through a list.",
    "intent_summary": ("Checklist-style short brand-subpage for the small size group: what to check on the phone before adding the Longfu88 casino to the home screen in Singapore (device and browser), "
                       "the shortcut steps for iOS and Android, the login steps, a table of fixes, the Singapore-dollar payment methods of the cashier, who can play and the contacts; no features, "
                       "security or FAQ sections. Page voice: terse and scannable, a one-sentence lead-in per "
                       "section, then a list or a table; sentences of about 12 words; no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu App Checklist: Phone Setup for Singapore Players", 55, {K0: 1}, "(device check, shortcut steps for iOS and Android, login, fixes, payments, eligibility, contacts)", ka=False, km=False),
        blk(["b06"], 2, "Longfu88 Mobile Casino Device Checklist", 70, {K0: 1}, PL,
            edit=[("Lead with the three platforms exactly as given", "Lead-in of one sentence, then a bulleted list with the three platforms exactly as given")]),
        blk(["b03", "b04", "b05"], 2, "Longfu88 iOS and Android Shortcut Checklist", 180, {K_AND: 1, K_DL: 1, K_APK: 1}, PL,
            notes=INSTALL_FLAT_HEAD + INSTALL_FLAT_LISTS + "Put the iOS list before the Android list. " + NO_APP_CLAIMS,
            summary="Why no file is needed and the shortcut steps for iOS in Safari and Android in Chrome."),
        blk(["b08"], 2, "Login Checklist", 80, {K0: 1}, PL, edit=[("Name the steps in one flowing paragraph, not a list.", "A lead-in sentence, then a bulleted list of the steps.")]),
        blk(["b10"], 2, "Troubleshooting Checklist", 95, {K0: 1}, PT,
            notes=("One lead-in sentence, then a TABLE with two columns, problem | fix, and four rows in this order: the shortcut does not appear | repeat the steps in Chrome on Android or in Safari "
                   "on iOS; the page does not load | reload it and check the internet connection; the login fails | check the e-mail address and use Forgot Password on the login screen; "
                   "the problem remains | contact support through live chat, 24/7, or by e-mail (do not print the e-mail address here). General wording only, no error codes and no "
                   "browser-setting instructions presented as casino facts. " + NO_APP_CLAIMS)),
        n_pay("Longfu88 App Payments: Deposit Methods Checklist", 95, rows=4),
        n_elig("Eligibility Checklist", 60),
        blk(["b11"], 2, "Support Contacts", 55, {K0: 1}),
    ],
})

# ================================================================ MEDIUM (target 979, limit 1175)
variants.append({
    "id": "v04", "name": "Newcomer walkthrough (steps, nested)", "tier": "medium", "angle": "A new player who has not used the casino on a phone and wants one guided path.",
    "intent_summary": ("Step-by-step brand-subpage for a newcomer to the Longfu88 mobile casino in Singapore: what the mobile site offers, how to put it on the home screen (Android and iOS), whether the "
                       "phone and the browser fit, how to sign in, whether to keep the shortcut or the browser tab, how the account stays safe, what to do when something fails and where to get help. "
                       "All the base topics, none of the extra ones. "
                       "Page voice: a patient guide, \"first, then\" logic, sentences of about 17 words, one plain invitation to start. Steps are H2s, the two platforms are H3s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 App Guide for Beginners: Mobile Casino on Android and iOS", 65, {K0: 2, K_LAPP: 1, K_MC: 1}, "(what the mobile site offers, shortcut steps for Android and iOS, devices, sign-in, safety, fixes, support)"),
        blk(["b02"], 2, "Step 1: See What the Mobile Site Offers", 100, {K0: 1}),
        blk(["b03"], 2, "Step 2: Longfu88 Download Without a File", 70, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Steps in Chrome", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Steps for iPhone and iPad", 55, {}),
        blk(["b06"], 2, "Step 3: Check Your Phone and Browser", 70, {K0: 1}),
        blk(["b08"], 2, "Step 4: Sign In from the Phone", 85, {K0: 1}),
        blk(["b07"], 2, "Shortcut or Browser Tab: Which to Keep", 85, {K0: 2}),
        blk(["b09"], 2, "Keeping the Account Safe on a Phone", 80, {K0: 1}),
        blk(["b10"], 2, "When Something Does Not Work", 75, {K0: 1}),
        blk(["b11"], 2, "Help for Phone Players", 55, {K0: 1}),
        blk(["b12"], 2, "First-Time Phone Questions", 105, {K0: 2}, **faq(["app", "phones", "android", "ios", "login", "support"])),
    ],
})

variants.append({
    "id": "v05", "name": "Decision-led: app or mobile site", "tier": "medium", "angle": "A player who is deciding between an app and the mobile site.",
    "intent_summary": ("Decision-led brand-subpage about the Longfu88 mobile casino in Singapore for a player who expects an app and wants to know what is offered instead: the shortcut versus the "
                       "browser tab, which phones and browsers work (a table), the shortcut steps for Android and iOS, what the mobile site gives access to, how an account is opened and used, how "
                       "to withdraw from the cashier, fixes and account protection; no separate support section. "
                       "Page voice: calm and comparative, the choice first and the steps after it, sentences of about 16 words, a short consequence after each point; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu App or Mobile Site? Using Longfu88 on a Phone", 65, {K0: 1, K_MC: 1}, "(shortcut or browser tab, devices, shortcut steps for Android and iOS, features, account, withdrawals, fixes, protection)", ka=False),
        blk(["b07"], 2, "Shortcut or Browser Tab: Pick Your Route", 95, {K0: 2}),
        blk(["b06"], 2, "Which Phones and Browsers Work", 70, {K0: 1}, PT,
            notes=("One lead-in sentence that says that the layout adapts to smartphone and tablet screens, then a TABLE with three columns, platform | browser | how it opens, and three rows "
                   "as given in the Brand Information: Android | Chrome | Add to Home screen from the browser menu; iOS | Safari | Add to Home Screen from the Share menu; mobile web | the browser "
                   "of a smartphone or tablet | the responsive website opens directly. Do not state OS versions, device models, storage, memory or connection speed: none are given. " + NO_APP_CLAIMS)),
        blk(["b03"], 2, "Longfu88 Download Is Not Needed: Add the Shortcut Once", 70, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome Route", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari Route", 55, {}),
        blk(["b02"], 2, "Features Available on Mobile", 90, {K0: 1}, ["paragraph"], edit=[(B02_LIST, B02_PROSE)]),
        n_reg("Opening an Account: Registration Steps on a Phone", 75, short=True),
        blk(["b08"], 2, "Sign In from a Phone", 75, {K0: 1}),
        n_wd("Cashing Out from a Phone", 85, short=True),
        blk(["b10"], 2, "Fixing Phone Problems Before Contacting Support", 75, {K0: 1}, edit=[(B10_LIST, B10_PROSE)], fmt=["paragraph"]),
        blk(["b09"], 2, "Protecting the Account on a Phone", 75, {K0: 1}),
        blk(["b12"], 2, "Longfu88 App FAQ: Route and Setup", 100, {K0: 2}, **faq(["app", "tab", "phones", "tablet", "reg", "support"])),
    ],
})

variants.append({
    "id": "v06", "name": "Security-conscious", "tier": "medium", "angle": "A cautious player who wants to know what protects the account before using a phone.",
    "intent_summary": ("Security-conscious brand-subpage about the Longfu88 mobile casino in Singapore for a cautious reader: how the account is protected on a phone, which technical data the website collects, "
                       "how to sign in safely, why the casino needs no installation file and how the shortcut is added on Android and iOS, the choice between the shortcut and a browser tab, "
                       "which identity checks can be requested, responsible gaming and support; no feature list and no fix list. "
                       "Page voice: sober and exact, every claim tied to a stated fact, sentences of about 18 words with a few shorter ones, no reassurance beyond the "
                       "facts; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 on Android and iOS: Safe Mobile Casino Access", 70, {K0: 1, K_LAPP: 1, K_MC: 1}, "(account protection, technical data, safe sign-in, the shortcut instead of a file, identity checks, responsible gaming, support)"),
        blk(["b09"], 2, "How the Account Stays Protected on a Phone", 100, {K0: 1}),
        n_data("Which Technical Data the Website Collects", 65),
        blk(["b08"], 2, "Signing In Safely from a Phone", 75, {K0: 1}, refs_drop=["brandinfo_account.registration.methods", "brandinfo_account.registration.required_details"],
            extra="Only the login: leave the registration form out of this block."),
        blk(["b03"], 2, "Longfu88 Download: A Shortcut Instead of a File", 70, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome Shortcut", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari Shortcut", 55, {}),
        blk(["b07"], 2, "Shortcut Versus Browser Tab", 70, {K0: 1}),
        n_kyc("Identity Checks and Account Verification", 85),
        n_rg("Responsible Play on a Phone", 70, short=True),
        blk(["b06"], 2, "Devices and Browsers", 60, {K0: 1}),
        blk(["b11"], 2, "Reaching Support", 55, {K0: 1}),
        blk(["b12"], 2, "Longfu88 App Safety FAQ", 100, {K0: 2}, **faq(["app", "login", "age", "ios", "android", "support"])),
    ],
})

variants.append({
    "id": "v07", "name": "Help-led: fixes, games and payments", "tier": "medium", "angle": "A player who already tried and cannot get the casino working on a phone, and wants to know what to expect inside.",
    "intent_summary": ("Help-led brand-subpage about the Longfu88 mobile casino in Singapore for a player whose phone setup did not work: the quick fixes first (a table), how to add the shortcut "
                       "again on Android and iOS, sign-in trouble, the switch between the shortcut and a browser tab, what should work on mobile, the game categories, the Singapore-dollar payment methods "
                       "and when to contact support; no device checks and no security section. "
                       "Page voice: practical and calm, cause then fix, sentences of about 16 words; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Mobile Casino Help: Set It Up, Fix It, Play", 65, {K0: 1, K_LAPP: 1}, "(quick fixes, adding the shortcut again on Android and iOS, sign-in trouble, games, payments, support)", km=False),
        blk(["b10"], 2, "Longfu88 App Problems and Quick Fixes", 85, {K0: 1}, PT,
            notes=("One lead-in sentence, then a TABLE with two columns, problem | fix, and four rows in this order: the shortcut does not appear | repeat the steps in Chrome on Android or in Safari "
                   "on iOS; the page does not load | reload it and check the internet connection; the login fails | check the e-mail address and use Forgot Password on the login screen; "
                   "the problem remains | contact support through live chat, 24/7, or by e-mail (do not print the e-mail address here). General wording only, no error codes and no "
                   "browser-setting instructions presented as casino facts. " + NO_APP_CLAIMS)),
        blk(["b03"], 2, "Longfu88 Download Help: Add the Shortcut Again", 70, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Add the Shortcut Again in Chrome", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Add the Shortcut Again in Safari", 55, {}),
        blk(["b08"], 2, "Sign-In Trouble on a Phone", 75, {K0: 1}),
        blk(["b07"], 2, "Switching Between the Shortcut and a Browser Tab", 75, {K0: 2}),
        blk(["b02"], 2, "What Should Work on Mobile", 85, {K0: 1}),
        n_games("Casino Games Available on a Phone", 65),
        n_pay("Deposit Methods in Singapore Dollars", 90, rows=4),
        blk(["b11"], 2, "When to Contact Support", 55, {K0: 1}),
        blk(["b12"], 2, "Mobile Help FAQ", 100, {K0: 2}, **faq(["app", "features", "phones", "login", "tab", "sports"])),
    ],
})

# ================================================================ LARGE (limit 1456 = the mean of the group): base plus topics of the neighbouring sections
variants.append({
    "id": "v08", "name": "Complete mobile handbook (large)", "tier": "large", "angle": "A reader who wants everything about the casino on a phone on one page.",
    "intent_summary": ("Complete brand-subpage for the large size group of the competitors, built like the longest app pages of the query: a handbook of the Longfu88 mobile casino for players from Singapore "
                       "with the shortcut instead of a file (Android and iOS), supported devices, the choice between the shortcut and a browser tab, what the mobile site gives access to (casino games, "
                       "sports betting), paying from a phone, the welcome offer, account access, security, troubleshooting, support and a FAQ. All the base topics plus five extra ones (games, sports, payments, the welcome offer, ongoing bonuses). Page voice: reference-like, each H2 opens "
                       "with what the section is for, sentences of about 18 words, a consequence after each condition; one plain invitation to start. Every extra section is written only from the "
                       "facts of its Brand Information; where a section has few facts it stays short. H2 sections with H3 details." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 App Handbook for Singapore Players: Everything on Mobile", 70, {K0: 2, K_LAPP: 1, K_MC: 1}, "(the shortcut for Android and iOS, devices, shortcut or browser tab, games, sports, paying from a phone, the welcome offer, account access, security, fixes, support)"),
        blk(["b03"], 2, "Longfu88 Download: No File, Only a Shortcut", 70, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome Walkthrough", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari Walkthrough", 55, {}),
        blk(["b06"], 2, "Supported Devices and Browsers", 65, {K0: 1}),
        blk(["b07"], 2, "Choosing Between the Shortcut and a Browser Tab", 80, {K0: 2}),
        blk(["b02"], 2, "Everything You Can Do on a Phone", 85, {K0: 1}),
        n_games("Casino Games on a Phone", 55, level=3),
        n_sports("Sports Betting on a Phone", 60, level=3),
        n_pay("Paying from a Phone: Payment Methods in SGD", 90, rows=4),
        n_welcome("Welcome Offer from Your Phone", 65),
        n_promo("Ongoing Bonuses on a Phone: Cashback and Weekend Reload", 80),
        blk(["b08"], 2, "Account Access on a Phone: Registration and Login", 75, {K0: 1}, PL),
        blk(["b09"], 2, "Mobile Security and Privacy Terms", 75, {K0: 1}, refs_add=["brandinfo_privacy_policy.privacy_policy.data_sharing"],
            extra="Add with whom data may be shared, as a short list inside the paragraph."),
        blk(["b10"], 2, "Fixing Common Mobile Problems Step by Step", 75, {K0: 1}),
        blk(["b11"], 2, "Support Channels for Mobile Players", 55, {K0: 1}),
        blk(["b12"], 2, "Mobile Handbook FAQ", 100, {K0: 2}, **faq(["app", "phones", "android", "ios", "features", "sports", "login", "support"])),
    ],
})

variants.append({
    "id": "v09", "name": "Account lifecycle (large)", "tier": "large", "angle": "A player who wants to follow the whole account path from the phone: register, verify, play safely, cash out.",
    "intent_summary": ("Large brand-subpage about the Longfu88 mobile casino in Singapore along the life of an account: the home-screen shortcut for Android and iOS, what the mobile site offers, the registration "
                       "steps, the login, the identity checks, withdrawing, account protection, technical data, responsible gaming, VIP tiers, fixes and a FAQ; no device list, no shortcut-versus-tab section and no support section. "
                       "Page voice: a narrative of the account in the order it happens, sentences of about 17 words, a short consequence after each stage; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 App Account Path: From Shortcut to Cash-Out on Mobile", 65, {K0: 1, K_LAPP: 1, K_MC: 1}, "(the shortcut, registration, login, identity checks, withdrawals, protection, data, responsible gaming, fixes)"),
        blk(["b03"], 2, "Stage 1: Longfu88 Download Is a Shortcut", 70, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Setup in Chrome", 50, {}),
        blk(["b05"], 3, "Longfu88 iOS: Setup in Safari", 50, {}),
        blk(["b02"], 2, "Stage 2: What the Mobile Site Gives You", 80, {K0: 1}, ["paragraph"], edit=[(B02_LIST, B02_PROSE)]),
        n_reg("Stage 3: Registration Steps on the Phone", 85),
        blk(["b08"], 2, "Stage 4: Logging In and Getting Back In", 70, {K0: 1}, refs_drop=["brandinfo_account.registration.methods", "brandinfo_account.registration.required_details"]),
        n_kyc("Stage 5: Identity Checks and Documents", 90),
        n_wd("Stage 6: Cashing Out from the Phone", 95),
        blk(["b09"], 2, "Account Protection Across Devices", 75, {K0: 1}),
        n_data("Technical Data and Cookies", 60, short=True),
        n_rg("Responsible Gaming from the Phone", 75),
        n_vip("VIP Tiers and Points for Phone Players", 65),
        blk(["b10"], 2, "Fixes for Problems Along the Way", 70, {K0: 1}),
        blk(["b12"], 2, "Account Path FAQ", 95, {K0: 2}, **faq(["app", "phones", "ios", "reg", "login", "age"])),
    ],
})

variants.append({
    "id": "v10", "name": "Payments, rules and sports (large)", "tier": "large", "angle": "A player who wants to know the rules of play, payments and sports before putting the casino on the phone.",
    "intent_summary": ("Large brand-subpage about the Longfu88 mobile casino in Singapore for a player who cares about the rules and the money: the home-screen shortcut for Android and iOS, what the mobile site "
                       "gives access to, who can play, the currencies and support languages, the sportsbook, the game categories, cashback and reload offers, the Singapore-dollar payment methods, withdrawing, devices, account access, support and a FAQ; "
                       "no security section, no fix list and no shortcut-versus-tab section. "
                       "Page voice: businesslike and compact, a fact first and its consequence second, sentences of about 15 words; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 App Rules and Payments: Mobile Casino for Singapore Players", 65, {K0: 2, K_LAPP: 1, K_MC: 1}, "(the shortcut, features, eligibility, currencies, sports, payments, withdrawals, devices, account access, support)"),
        blk(["b03"], 2, "Longfu88 Download: The Home Screen Route", 70, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome Menu Steps", 50, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari Share Steps", 50, {}),
        blk(["b02"], 2, "Mobile Features at a Glance", 85, {K0: 1}, ["paragraph", "table"],
            notes=("One lead-in sentence that says the website adapts to smartphone and tablet browsers (responsive), then a TABLE with two columns, feature | what the player can do, and six rows in the "
                   "order of the Brand Information (casino, sportsbook, account access, deposits, withdrawals, bonuses), each cell a short phrase of 3-6 words. No game names, providers, RTP values, "
                   "payment method names or bonus amounts here (other sections cover them). " + NO_APP_CLAIMS)),
        n_elig("Who Can Play from a Phone", 60),
        n_cur("Currencies and Support Languages", 55),
        n_sports("Sports Betting Rules on Mobile", 70),
        n_games("Which Game Categories the Casino Section Offers", 60, short=True),
        n_promo("Cashback and Reload Offers for Mobile Players", 80),
        n_pay("Payment Methods for Singapore Players", 95, rows=4),
        n_wd("Taking Money Out from a Mobile Account", 85),
        blk(["b06"], 2, "Phones and Browsers That Work", 55, {K0: 1}),
        blk(["b08"], 2, "Signing In from a Phone", 70, {K0: 1}),
        blk(["b11"], 2, "Support for Players on the Go", 55, {K0: 1}),
        blk(["b12"], 2, "Rules and Payments FAQ", 90, {K0: 2}, **faq(["app", "phones", "age", "lang", "sports", "support"])),
    ],
})

variants.append({
    "id": "v11", "name": "Play, bet and get rewarded (large)", "tier": "large", "angle": "A player who wants to know what there is to play and claim on the phone.",
    "intent_summary": ("Large brand-subpage about the Longfu88 mobile casino in Singapore for a player who wants to know what there is to do on a phone: the home-screen shortcut for Android and iOS, the "
                       "devices, the shortcut versus the browser tab, the game categories, the sportsbook, the welcome offer, account access, identity checks, account protection, responsible gaming, VIP tiers, a withdrawal request and support; "
                       "no feature overview, no fix list and no FAQ. "
                       "Page voice: lively but factual, the activity first and its condition second, sentences of about 16 words, a plain invitation to start; no promises." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Mobile Casino on Your Phone: Play, Bet and Claim", 70, {K0: 2, K_LAPP: 1}, "(the shortcut for Android and iOS, devices, games, sports, the welcome offer, account access, checks, safety, responsible gaming, support)", km=False),
        blk(["b06"], 2, "Which Phones and Browsers You Can Use", 60, {K0: 1}),
        blk(["b03"], 2, "Longfu88 Download: Skip the File, Add the Shortcut", 70, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome Shortcut in Three Steps", 50, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari Shortcut in Three Steps", 50, {}),
        blk(["b07"], 2, "Browser Tab or Home Screen Icon", 75, {K0: 1}),
        n_games("Slots, Live Dealer and More on a Phone", 65),
        n_sports("Betting on Sports from a Phone", 70, level=3),
        n_welcome("Claiming the Welcome Offer on Mobile", 70),
        blk(["b08"], 2, "Account Access: Register and Sign In on a Phone", 80, {K0: 1}, PL),
        n_kyc("Verification Before You Cash Out", 75, short=True),
        n_wd("Sending a Cash-Out Request from the Phone", 80, short=True),
        blk(["b09"], 2, "Staying Secure While You Play on Mobile", 70, {K0: 1}),
        n_rg("Playing Responsibly on a Phone", 80),
        n_vip("VIP Tiers and Rewards on Mobile", 65),
        blk(["b11"], 2, "Longfu88 App Support Around the Clock", 60, {K0: 1}),
    ],
})

variants.append({
    "id": "v12", "name": "Reference sheet (large, tables)", "tier": "large", "angle": "A reader who wants a compact reference with tables and short sections.",
    "intent_summary": ("Large brand-subpage written as a reference sheet about the Longfu88 mobile casino in Singapore: the shortcut for Android and iOS, the features in a table, the shortcut versus the "
                       "browser tab, registration, withdrawals, protection, technical data, the sportsbook, game categories, deposit methods, currencies and languages, fixes, support and a FAQ; no device section and no login section "
                       "(the registration section carries both). Page voice: compact reference style, a one-line purpose per section, sentences of about 14 words, nouns over verbs; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 App Reference: Mobile Casino Facts for Singapore", 60, {K0: 1, K_LAPP: 1, K_MC: 1}, "(the shortcut, features, shortcut or browser tab, registration, withdrawals, protection, data, sports, currencies, fixes, support)"),
        blk(["b02"], 2, "Mobile Features Reference", 80, {K0: 1}, ["paragraph", "table"],
            notes=("One lead-in sentence that says the website adapts to smartphone and tablet browsers (responsive), then a TABLE with two columns, feature | what the player can do, and six rows in the "
                   "order of the Brand Information (casino, sportsbook, account access, deposits, withdrawals, bonuses), each cell a short phrase of 3-6 words. No game names, providers, RTP values, "
                   "payment method names or bonus amounts here (other sections cover them). " + NO_APP_CLAIMS)),
        blk(["b03"], 2, "Longfu88 Download Reference: Shortcut, Not a File", 65, {K_APK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome Reference", 50, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari Reference", 50, {}),
        blk(["b07"], 2, "Home Screen Icon Versus Browser Tab", 70, {K0: 1}),
        n_reg("Account Opening and Login Reference", 85),
        n_wd("Cash-Out Reference for Mobile Players", 80),
        blk(["b09"], 2, "Account Security Reference", 70, {K0: 1}),
        n_data("Technical Data Reference", 65),
        n_sports("Sportsbook Reference", 60, short=True),
        n_games("Game Category Reference", 50, short=True),
        n_pay("Deposit Method Reference", 80, rows=3),
        n_cur("Currency and Language Reference", 50),
        blk(["b10"], 2, "Problem and Fix Reference", 70, {K0: 1}),
        blk(["b11"], 2, "Support Reference", 50, {K0: 1}),
        blk(["b12"], 2, "Reference FAQ", 90, {K0: 2}, **faq(["app", "phones", "tab", "reg", "lang", "support"])),
    ],
})

# keywords that would not stand anywhere: v11 has no "Longfu88 mobile casino" (km=False) -> put it into the heading of the devices block
for v in variants:
    if v.pop("kw_mc_heading", False):
        for b in v["blocks"]:
            if b["heading"] == "Which Phones and Browsers You Can Use":
                b["heading"] = "Which Phones Run the Longfu88 Mobile Casino"

# the skipped mandatory clusters of every text: those that no block covers (at most half of the six)
COVER = {"b02": "k01", "b03": "k01", "b04": "k01", "b05": "k01", "b06": "k01", "b07": "k01", "b08": "k03", "b09": "k07", "b12": "k06"}
NEW_COVER = {"games": "k08", "pay": "k09", "reg": "k03"}
MANDATORY = ["k01", "k03", "k06", "k07", "k08", "k09"]
REASON = {
    "k03": "registration and login are left to the login page of the site; this short text keeps the shortcut and the fixes",
    "k06": "no FAQ in this text: the questions are answered in the sections themselves",
    "k07": "the account protection is one clause of the login block; security belongs to its own pages of the site",
    "k08": "the games overview belongs to the games pages of the site; the app page names the casino as one feature of the mobile website",
    "k09": "the payment methods belong to the payments page of the site; the app page names deposits and withdrawals as features of the mobile website",
}
for v in variants:
    covered = set()
    for b in v["blocks"]:
        if b["from"]:
            covered |= {COVER[i] for i in b["from"] if i in COVER}
        else:
            covered |= {NEW_COVER[NID[b["heading"].lower()]]} if NID[b["heading"].lower()] in NEW_COVER else set()
    left = [c for c in MANDATORY if c not in covered]
    assert len(left) <= 3, (v["id"], left)
    v["skipped_clusters"] = [{"id": c, "reason": REASON[c]} for c in left]

intrinsic = {
    "b11": {"keyword": K0, "count": 1,
            "replace": [['; it contains the tracked keyword "Longfu88", which is the one occurrence this block allows (so do not write the brand name anywhere else in the block).', "."]],
            "note": 'The e-mail address contains the tracked keyword "Longfu88"; it is part of the exact count of this block.'},
}
blueprint = {"base_run": "longfu88-app-sg", "brand_names": ["Longfu88 Mobile Casino", "Longfu88 Download", "Longfu88 Android", "Longfu88 iOS", "Longfu88"], "keyword_labels": {},
             "intrinsic": intrinsic, "variants": variants}

heads = [b["heading"].lower() for v in variants for b in v["blocks"]]
dup = {h for h in heads if heads.count(h) > 1}
assert not dup, dup
out = Path("input/variants/longfu88-app-sg.json")
out.write_text(json.dumps(blueprint, ensure_ascii=False, indent=1), encoding="utf-8")
Path("output").mkdir(exist_ok=True)
Path("output/longfu88-app-sg-topics.json").write_text(json.dumps(NID, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(variants), "variants")
