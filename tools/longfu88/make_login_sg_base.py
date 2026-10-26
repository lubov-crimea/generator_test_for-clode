"""Builds runs/longfu88-login-sg/llm/brief.json and review.json (the answers of the manual step-1 requests) for the Longfu88
login page (brand-subpage, GEO SG). Run from the project root:  python tools/longfu88/make_login_sg_base.py

This is the BASE ТЗ for the OPTIMUM size group of the competitors (`medium`; only two competitors could be read, so the group is the
mean of both: sg.com 844 words and play.my 1754 words -> target 1299, limit 1559; see runs/longfu88-login-sg/01_tiers.json). The
structure follows the clusters of the competitors (registration and login k01, bonuses k03, safety and verification k05 are mandatory;
the big competitor adds recovery, settings, currencies and accounts, closure, mobile, the VIP programme) and the knowledge base
longfu88-new, which has facts for every one of these topics except the VIP programme (left to the variants). The small texts are cut
from it and the large ones add blocks (tools/longfu88/make_login_sg_variants.py).

Facts: only the knowledge base. It has NO two-factor authentication, SSL, username or player ID, login URL, lockout rule or app download:
the notes forbid these claims."""
import json
from pathlib import Path

RUN = Path("runs/longfu88-login-sg")
LEGAL = "Do not say or imply that the casino is licensed, legal or approved in Singapore, and do not discuss the licence on this page."
NO_SECURITY_CLAIMS = ("Do not mention two-factor authentication, SMS codes, CAPTCHA, SSL or encryption, a username or a player ID: the login is e-mail and password only "
                      "and no other protection is given.")


def rng(mid):
    return round(mid * 0.88), round(mid * 1.12)


blocks = []


def add(level, heading, source, covers, refs, mid, kw, formats, ents, conns, summary, notes):
    lo, hi = rng(mid)
    blocks.append(dict(level=level, heading=heading, source=source, covers_clusters=covers, kb_refs=refs, words_min=lo, words_max=hi,
                       keywords=kw, formats=formats, entities=[{"name": n, "priority": p} for n, p in ents],
                       entity_connections=[{"subject": a, "relation": r, "object": c, "priority": p} for a, r, c, p in conns],
                       summary=summary, copywriter_notes=notes))


# The tracked keywords: "Longfu88" 24 (the median of the two competitors; the headings that carry a longer keyword do not count for it),
# "Longfu88 login", "Longfu login", "Longfu88 register" and "Longfu88 casino login" once each.

# b01 intro (the H1 carries the keyword "Longfu88 casino login")
add(1, "Longfu88 Casino Login for Singapore Players", "h1", [],
    ["brandinfo_account.login.method", "brandinfo_general.minimum_age"], 80, {"Longfu88": 2}, ["paragraph"],
    [("Player Account", 10), ("Login", 9), ("Minimum Age", 5)],
    [("Player", "logs in to", "the Player Account with e-mail and password", 8)],
    "What the page covers: how a registered player signs in to the casino account, how a lost password is reset, how the account is opened and checked, and where help is found.",
    'Open with the keyword "Longfu88" as the subject of the first sentence, followed by the fact that the account is opened with the e-mail address and the password chosen at registration. '
    'State once that the casino is for players aged 18 or over, and that the page is written for players from Singapore. Signpost the topics of the page in one sentence '
    '(login, password reset, registration, verification, security, mobile access, support) without detail. '
    f'{LEGAL} Use "Longfu88" exactly twice and no other tracked keyword in the body. No payment or game details. Neutral tone, no promises.')

# b02 registration (cluster k01)
add(2, "Longfu88 Register: Create an Account in Five Steps", "mandatory", ["k01"],
    ["brandinfo_account.registration"], 125, {"Longfu88": 2}, ["paragraph", "list"],
    [("Registration", 10), ("Required Details", 7), ("One Account Rule", 6)],
    [("Registration", "requires", "e-mail, password, legal name, date of birth and residential address", 8), ("Player", "may hold", "only one personal account", 7)],
    "Registration by e-mail in five numbered steps, the details the form asks for and the eligibility rules (18+, one account per player).",
    'One lead-in sentence, then a NUMBERED list with the five registration steps in the order of the Brand Information, then one short sentence with the required details (e-mail, password, '
    'legal name, date of birth, residential address) and the eligibility rules (18+ and of legal gambling age in the relevant jurisdiction, one personal account per player). '
    'Registration by e-mail is the only method given. Write "the site" or "the casino" in the list items instead of the brand name. Do not describe bonuses or deposits here. '
    'Use "Longfu88" exactly twice (in the lead-in and the closing sentence, never inside the list) and no other tracked keyword.')

# b03 login (cluster k01); the heading carries the keyword "Longfu88 login"
add(2, "Longfu88 Login: How to Sign In to Your Account", "mandatory", ["k01"],
    ["brandinfo_account.login.method", "brandinfo_account.login.steps"], 90, {"Longfu88": 2, "Longfu login": 1}, ["paragraph", "list"],
    [("Login", 10), ("Registered E-mail", 8), ("Security Check", 5)],
    [("Player", "enters", "the registered e-mail and password on the login screen", 8), ("Security Check", "precedes", "access to the account", 6)],
    "The three login steps in order: open Login on the website, enter the registered e-mail and password, pass any security check.",
    'One lead-in sentence that carries a fact, then a NUMBERED list with the three login steps in the order of the Brand Information (select Login on the website; enter the registered '
    'e-mail and password; complete any security check and access the account). The method is e-mail and password: say so. '
    f'{NO_SECURITY_CLAIMS} '
    'Use "Longfu login" exactly once, in the lead-in sentence, written verbatim as the phrase "Longfu login" (for example "Every Longfu login starts with the registered e-mail address and the password"). '
    'Use "Longfu88" exactly twice, in the lead-in or in the closing line, and no other tracked keyword; keep tracked keywords out of the list items. '
    'Do not explain password reset here (next sub-section).')

# b04 forgot password (cluster k01 / k13)
add(3, "Forgot Your Password", "mandatory", ["k01", "k13"],
    ["brandinfo_account.login.password_recovery"], 55, {"Longfu88": 1}, ["paragraph", "list"],
    [("Password Reset", 10), ("Reset Link", 8)],
    [("Player", "requests", "a reset link to the registered e-mail", 8)],
    "How a player who forgot the password sets a new one: Forgot Password on the login screen, reset link by e-mail, new password.",
    'One lead-in sentence, then a NUMBERED list with the three recovery steps in the order of the Brand Information (Forgot Password on the login screen; request a reset link with the registered '
    'e-mail; follow the e-mailed instructions to set a new password). A player who no longer has access to the registered mailbox should contact support (pointer only; the contact details '
    'are in the support section). Do not state how long the link is valid or how fast it arrives: no such fact is given. Use "Longfu88" exactly once, in the lead-in sentence.')

# b05 login problems (a usual block of the long competitors)
add(3, "Login Problems and Fixes", "unique", ["k01"],
    ["brandinfo_account.login.password_recovery[1]", "brandinfo_general.customer_support.channels", "brandinfo_privacy_policy.terms_conditions.account_terms"], 70, {"Longfu88": 1}, ["paragraph"],
    [("Login Error", 10), ("Account Review", 6)],
    [("Account Review", "may delay", "access until verification is complete", 6)],
    "The usual reasons for a failed login and what to check, ending with the support channels and the fact that the operator may restrict an account for verification.",
    'General industry guidance is allowed here and must stay general: check that the e-mail address is typed as registered, that the keyboard layout and caps lock are right, and use the password '
    'reset if the password is lost. The casino may suspend activity for verification or suspected abuse (account terms in the Brand Information); in that case contact support, which is available '
    'through live chat 24/7 and by e-mail (do not print the e-mail address here). Do not give browser or cache instructions as casino facts and do not mention error codes, lockout counts or '
    'lockout times: none are given. Use "Longfu88" exactly once.')

# b06 verification (cluster k05)
add(2, "Account Verification", "mandatory", ["k05"],
    ["brandinfo_account.verification.triggers", "brandinfo_account.verification.document_submission_window",
     "brandinfo_account.verification.typical_review_time", "brandinfo_privacy_policy.kyc_aml.required_documents"], 115, {"Longfu88": 1}, ["paragraph", "table"],
    [("Account Verification", 10), ("Identity Document", 7), ("Review Time", 6)],
    [("Account Verification", "is requested", "before a withdrawal, during an account review and for unusual or high-value transactions", 8)],
    "When the casino asks for verification, which documents count (identity, address, payment method, source of funds) and how long the process takes.",
    'Lead with the triggers (account review, before a withdrawal, unusual or high-value transactions, changes to account or payment details). Then a TABLE with two columns, document type | accepted '
    'documents, one row each for identity (passport, national identity card, driving licence), address (utility bill, bank statement), payment method (bank or card ownership evidence, digital '
    'wallet ownership evidence) and source of funds (proof of income, bank statements, other supporting financial documents); the source-of-funds row applies only when requested. Then one '
    'sentence with the two periods exactly as given: documents are due up to 30 days after the request, and a complete set is normally reviewed within up to 10 days. Do not say that '
    'verification is needed at registration or for login: it is requested on the triggers above. Use "Longfu88" exactly once.')

# b07 security (cluster k05)
add(2, "Account Security and Privacy", "mandatory", ["k05"],
    ["brandinfo_privacy_policy.privacy_policy.security", "brandinfo_privacy_policy.terms_conditions.account_terms"], 80, {"Longfu88": 2}, ["paragraph"],
    [("Account Security", 10), ("Login Credentials", 8)],
    [("Account Holder", "safeguards", "the login credentials", 8)],
    "Who is responsible for the credentials and what the operator does to protect accounts and data.",
    'Lead with the player\'s own part: the account holder is responsible for safeguarding the login credentials. Then the operator\'s part exactly at the level of detail of the Brand Information: '
    'technical and organisational safeguards protect accounts, payments and personal information, and the operator may suspend activity for verification or suspected abuse. '
    f'{NO_SECURITY_CLAIMS} Do not claim an audit or a certificate. Do not print the contact addresses of the privacy policy (they contain the brand name). Use "Longfu88" exactly twice.')

# b08 welcome bonus (cluster k03)
add(2, "Welcome Bonus After Registration", "mandatory", ["k03"],
    ["brandinfo_welcome.welcome_bonus.name", "brandinfo_welcome.welcome_bonus.bonus_percentage", "brandinfo_welcome.welcome_bonus.maximum_bonus",
     "brandinfo_welcome.welcome_bonus.free_spins", "brandinfo_welcome.welcome_bonus.minimum_deposit", "brandinfo_welcome.welcome_bonus.wagering_requirement",
     "brandinfo_welcome.welcome_bonus.claiming_procedure"], 75, {"Longfu88": 2}, ["paragraph"],
    [("Casino Welcome Bonus", 10), ("First Deposit", 8), ("Wagering Requirement", 7)],
    [("Casino Welcome Bonus", "requires", "a first qualifying deposit of €50 and activation in My Bonuses", 8)],
    "What a new account can claim: the Casino Welcome Bonus, its size, the minimum first deposit, the wagering and the four claiming steps.",
    'This page is about the account, so keep the bonus short and strictly to the Brand Information: the Casino Welcome Bonus is a first-deposit casino bonus of 188% up to €2,088 plus 18 free spins; '
    'the minimum first deposit is €50; wagering is 25x the deposit plus bonus amount. Claiming: register and complete the personal details, make the first qualifying deposit, activate the bonus in '
    'My Bonuses before placing any wager, play eligible games and complete the wagering. Use the €50 minimum of the bonus; do NOT mention the general minimum deposit of €10 on this page. '
    'Do not add terms that are not listed (validity, limits, exclusions are described elsewhere). Do not promise winnings. Use "Longfu88" exactly twice.')

# b09 first withdrawal (cluster k06, the big competitor has a limits section; here only what the account needs)
add(2, "Account Checks Before the First Payout", "unique", ["k06"],
    ["brandinfo_privacy_policy.kyc_aml.verification_requirements.mandatory_verification", "brandinfo_privacy_policy.kyc_aml.withdrawal_restrictions",
     "brandinfo_privacy_policy.terms_conditions.withdrawal_terms[1]", "brandinfo_privacy_policy.terms_conditions.eligibility.player_requirements[2]"], 80,
    {"Longfu88": 2}, ["paragraph"],
    [("Withdrawal", 10), ("Identity Check", 8), ("Payment Ownership", 6)],
    [("Withdrawal", "waits for", "identity, payment ownership and any required source-of-funds checks", 8)],
    "Why the first withdrawal is the moment when the account is checked: identity and payment checks, payments held until they are complete, the usual three working days and the own-payment-method rule.",
    'Lead with the fact that identity and payment checks may be required for withdrawals and that payments may be held until identification, payment ownership and any required source-of-funds '
    'checks are complete. Then the processing time exactly as given: withdrawal requests are generally processed within three working days. Then the rule that payment methods must belong to the '
    'player (no third-party payment methods). Do NOT list payment methods, limits, fees, commissions, turnover rules or bank settlement times: they belong to the payments page of the site. '
    'Do not promise payout speed. Use "Longfu88" exactly twice.')

# b10 mobile access (cluster k08); the page links to the app page of the site
add(2, "Mobile Login on a Phone or Tablet", "unique", ["k08"],
    ["brandinfo_app.app_information.mobile_access", "brandinfo_app.app_information.platforms", "brandinfo_app.app_information.android_installation",
     "brandinfo_app.app_information.ios_installation"], 80, {"Longfu88": 2}, ["paragraph", "list"],
    [("Mobile Web", 10), ("Home Screen Shortcut", 8)],
    [("Player", "adds", "a shortcut of the website to the home screen", 8)],
    "Logging in from a phone or a tablet in the browser and adding a home-screen shortcut on Android (Chrome) and iOS (Safari).",
    'The casino is a responsive website that works in the browser of a smartphone or a tablet; the Brand Information has no download from an app store: do not call it a downloadable app and do not '
    'mention APK files, app stores or app versions. The login on a phone is the same as on a computer. A short paragraph, then a bulleted list with two items: Android (open the site in Chrome, '
    'open the browser menu and choose Add to Home screen, confirm the shortcut) and iOS (open the site in Safari, tap Share and choose Add to Home Screen, confirm Add). Write "the site" in the '
    'list items instead of the brand name. Use "Longfu88" exactly twice, in the paragraph, never inside the list.')

# b11 currencies and the one-account rule (cluster k16)
add(2, "Currencies and the One-Account Rule", "unique", ["k16"],
    ["brandinfo_general.currencies", "brandinfo_privacy_policy.terms_conditions.eligibility.player_requirements"], 55, {"Longfu88": 1}, ["paragraph"],
    [("Account Currencies", 8), ("One Personal Account", 8)],
    [("Player", "uses", "one personal account in one of the supported currencies", 8)],
    "Which currencies an account can use and the rules for the account itself: accurate details, one personal account, no third-party payment methods.",
    'State the currencies exactly as listed (EUR, USD, MYR, THB, SGD and USDT) and do not convert amounts or mention exchange rates, conversion or a choice of currency at registration: '
    'none is given. The player requirements: register with accurate information, use only one personal account, do not use third-party payment methods. Calm tone, no legal advice. '
    f'{LEGAL} Use "Longfu88" exactly once.')

# b12 taking a break or closing the account (cluster k17)
add(2, "Taking a Break or Closing the Account", "unique", ["k17"],
    ["brandinfo_responsible_gaming.responsible_gaming.policy", "brandinfo_responsible_gaming.responsible_gaming.self_exclusion.effect",
     "brandinfo_responsible_gaming.responsible_gaming.account_closure", "brandinfo_responsible_gaming.responsible_gaming.support_organizations"], 90,
    {"Longfu88": 2}, ["paragraph"],
    [("Self-Exclusion", 10), ("Account Closure", 8), ("Support Organisations", 5)],
    [("Player", "requests", "self-exclusion or account closure through customer support", 8)],
    "How a player limits or ends access: self-exclusion, account closure through support and the independent help organisations.",
    'Players must be at least 18 and gamble only where lawful. A player who wants to stop contacts support and asks for self-exclusion or account closure; account access and gambling may '
    'then be restricted for the agreed period. Independent support: GamCare, Gamblers Anonymous and Gambling Therapy. Do not print the e-mail address of the self-exclusion request '
    '(it contains the brand name) and do not state a processing time. Accurate and practical, not moralising. Use "Longfu88" exactly twice.')

# b13 communication preferences and cookies (cluster k14)
add(2, "Communication Preferences and Cookies", "unique", ["k14"],
    ["brandinfo_privacy_policy.privacy_policy.marketing", "brandinfo_privacy_policy.privacy_policy.cookies"], 45, {"Longfu88": 1}, ["paragraph"],
    [("Communication Preferences", 10), ("Cookies", 6)],
    [("Player", "manages", "direct-marketing preferences and can unsubscribe from promotional communications", 8)],
    "Which settings the player controls: promotional communication and the cookies of the site.",
    'Two facts only, exactly as in the Brand Information: the player may manage direct-marketing preferences and unsubscribe from promotional communications; necessary, preference, '
    'analytics and marketing cookies support website functions and measurement. Do not invent account settings, screens, limits (deposit, loss, session) or profile fields and do not say '
    'where in the account to find these settings. Neutral tone. Use "Longfu88" exactly once.')

# b14 support (cluster k02)
add(2, "Customer Support for Account Questions", "mandatory", ["k02"],
    ["brandinfo_general.customer_support"], 55, {"Longfu88": 1}, ["paragraph"],
    [("Customer Support", 10), ("Live Chat", 8)],
    [("Customer Support", "answers", "account, login and verification questions through live chat and e-mail", 8)],
    "How to reach support with a login or account problem: live chat around the clock, e-mail and the languages of the support team.",
    'Support channels: 24/7 live chat and e-mail. Print the e-mail address exactly as given in the Brand Information; it contains the tracked keyword "Longfu88", which is the one occurrence this block '
    'allows (so do not write the brand name anywhere else in the block). Support languages: English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese. Say which kinds of account '
    'questions go here (login failure, a reset e-mail that does not arrive, document upload) without response-time promises.')

# b15 FAQ (cluster k04)
add(2, "Login and Account FAQ", "mandatory", ["k04"],
    ["brandinfo_account.login.method", "brandinfo_account.login.password_recovery[1]", "brandinfo_account.verification.typical_review_time",
     "brandinfo_general.minimum_age", "brandinfo_general.customer_support.channels"], 100, {"Longfu88": 2}, ["list"],
    [("Frequently Asked Questions", 10), ("Login", 7)],
    [("Player", "finds", "short answers to the most frequent login and account questions", 6)],
    "Six short questions and answers on login, password reset, verification time, age limit and support.",
    'A bulleted list of six items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required here for the question text only. Questions, in this order: '
    'how to log in (e-mail and password), what to do after a forgotten password (Forgot Password and the e-mailed reset link), which login method the casino uses (e-mail and password), how long '
    'verification takes (a complete document set is normally reviewed within up to 10 days), what the minimum age is (18), where to turn when login still fails (customer support, live chat 24/7; '
    'do not print the e-mail). Answers repeat the facts of the sections of the page in other words and add nothing new. Do not answer questions about multiple devices, lockouts or login limits: '
    'no data. Use "Longfu88" exactly twice and no other tracked keyword.')

intent = ("A returning or new player in Singapore wants to sign in to a Longfu88 account (or find out how to register first) and needs the exact steps, "
          "the password reset, what to do when the login fails, why the casino asks for verification, how the account works on a phone and where to get help. The page is a task page about "
          "the account entrance; the licence, the games, the payment methods and the full bonus programme belong to other pages of the site. The structure follows the "
          "login pages of the competitors of the medium size group and adds the account topics that the knowledge base can fill.")

brief = {"intent_summary": intent, "blocks": blocks, "skipped_clusters": []}
(RUN / "llm").mkdir(parents=True, exist_ok=True)
(RUN / "llm" / "brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=1), encoding="utf-8")
(RUN / "llm" / "review.json").write_text(json.dumps({"issues": [], "blocks": blocks}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(blocks), "blocks, mid words", sum(round((b["words_min"] + b["words_max"]) / 2) for b in blocks),
      "Longfu88", sum(b["keywords"].get("Longfu88", 0) for b in blocks))
