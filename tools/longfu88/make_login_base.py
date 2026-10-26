"""Builds runs/longfu88-login-my/llm/brief.json and review.json (the answers of the manual step-1 requests) for the Longfu88
login page (brand-subpage, GEO MY). Run from the project root:  python tools/longfu88/make_login_base.py

This is the BASE ТЗ for the OPTIMUM size group of the competitors (`medium`: sg.com, 844 words -> target 844, limit 1013; see
runs/longfu88-login-my/01_tiers.json). The structure comes from the competitors' clusters (the mandatory ones plus the two that the
medium competitor has: login problems and the welcome bonus); the small texts are cut from it and the large text adds blocks
(tools/longfu88/make_login_variants.py). The facts are chosen narrowly (`kb_refs`), enumerations are lists or a table."""
import json
from pathlib import Path

RUN = Path("runs/longfu88-login-my")
LEGAL = "Do not say or imply that the casino is licensed, legal or approved in Malaysia, and do not discuss the licence on this page."
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


# b01 intro
add(1, "Longfu88 Casino Login for Malaysian Players", "h1", [],
    ["brandinfo_account.login.method", "brandinfo_general.minimum_age"], 75, {"Longfu88": 1}, ["paragraph"],
    [("Player Account", 10), ("Login", 9), ("Minimum Age", 5)],
    [("Player", "logs in to", "the Player Account with e-mail and password", 8)],
    "What the page covers: how a registered player signs in to the casino account, how a lost password is reset, how the account is opened and checked, and where help is found.",
    f'Open with the keyword "Longfu88" as the subject of the first sentence, followed by the fact that the account is opened with the e-mail address and the password chosen at registration. '
    f'State once that the casino is for players aged 18 or over, and that the page is written for players from Malaysia. Signpost the topics of the page in one sentence '
    f'(login, password reset, registration, verification, security, support) without detail. {LEGAL} Use "Longfu88" exactly once and no other tracked keyword in the body. '
    f'No payment or game details. Neutral tone, no promises.')

# b02 registration (cluster k01)
add(2, "Longfu88 Register: Create an Account in Five Steps", "mandatory", ["k01"],
    ["brandinfo_account.registration"], 120, {}, ["paragraph", "list"],
    [("Registration", 10), ("Required Details", 7), ("One Account Rule", 6)],
    [("Registration", "requires", "e-mail, password, legal name, date of birth and residential address", 8), ("Player", "may hold", "only one personal account", 7)],
    "Registration by e-mail in five numbered steps, the details the form asks for and the eligibility rules (18+, one account per player).",
    'One lead-in sentence, then a NUMBERED list with the five registration steps in the order of the Brand Information, then one short sentence with the required details (e-mail, password, '
    'legal name, date of birth, residential address) and the eligibility rules (18+ and of legal gambling age in the relevant jurisdiction, one personal account per player). '
    'Registration by e-mail is the only method given. Keep the brand name out of the list items. Do not describe bonuses or deposits here.')

# b03 login (cluster k02)
add(2, "How to Log In to Your Account", "mandatory", ["k02"],
    ["brandinfo_account.login.method", "brandinfo_account.login.steps"], 80, {"Longfu88": 1, "Longfu login": 1}, ["paragraph", "list"],
    [("Login", 10), ("Registered E-mail", 8), ("Security Check", 5)],
    [("Player", "enters", "the registered e-mail and password on the login screen", 8), ("Security Check", "precedes", "access to the account", 6)],
    "The three login steps in order: open Login on the website, enter the registered e-mail and password, pass any security check.",
    f'One lead-in sentence that carries a fact, then a NUMBERED list with the three login steps in the order of the Brand Information (select Login on the website; enter the registered '
    f'e-mail and password; complete any security check and access the account). The method is e-mail and password: say so. {NO_SECURITY_CLAIMS} '
    f'Use "Longfu login" exactly once, in the lead-in sentence, written verbatim as the phrase "Longfu login" (for example "Every Longfu login starts with the registered e-mail address and the password"). '
    f'Use "Longfu88" exactly once, in the lead-in or in the closing line, and no other tracked keyword; keep tracked keywords out of the list items. '
    f'Do not explain password reset here (next sub-section).')

# b04 forgot password (cluster k03)
add(3, "Forgot Your Password", "mandatory", ["k03"],
    ["brandinfo_account.login.password_recovery"], 60, {}, ["paragraph", "list"],
    [("Password Reset", 10), ("Reset Link", 8)],
    [("Player", "requests", "a reset link to the registered e-mail", 8)],
    "How a player who forgot the password sets a new one: Forgot Password on the login screen, reset link by e-mail, new password.",
    'One lead-in sentence, then a NUMBERED list with the three recovery steps in the order of the Brand Information (Forgot Password on the login screen; request a reset link with the registered '
    'e-mail; follow the e-mailed instructions to set a new password). A player who no longer has access to the registered mailbox should contact support (pointer only; the contact details '
    'are in the support section). Do not state how long the link is valid or how fast it arrives: no such fact is given.')

# b05 login problems (cluster k04, the medium competitor has it)
add(3, "Login Problems and Fixes", "unique", ["k04"],
    ["brandinfo_account.login.password_recovery[1]", "brandinfo_general.customer_support.channels", "brandinfo_privacy_policy.terms_conditions.account_terms"], 65, {}, ["paragraph"],
    [("Login Error", 10), ("Account Review", 6)],
    [("Account Review", "may delay", "access until verification is complete", 6)],
    "The usual reasons for a failed login and what to check, ending with the support channels and the fact that the operator may restrict an account for verification.",
    'General industry guidance is allowed here and must stay general: check that the e-mail address is typed as registered, that the keyboard layout and caps lock are right, and use the password '
    'reset if the password is lost. The casino may suspend activity for verification or suspected abuse (account terms in the Brand Information); in that case contact support, which is available '
    'through live chat 24/7 and by e-mail (do not print the e-mail address here). Do not give browser or cache instructions as casino facts and do not mention error codes, lockout counts or '
    'lockout times: none are given.')

# b06 verification (cluster k05)
add(2, "Account Verification", "mandatory", ["k05"],
    ["brandinfo_account.verification.triggers", "brandinfo_account.verification.document_submission_window",
     "brandinfo_account.verification.typical_review_time", "brandinfo_privacy_policy.kyc_aml.required_documents"], 110, {}, ["paragraph", "table"],
    [("Account Verification", 10), ("Identity Document", 7), ("Review Time", 6)],
    [("Account Verification", "is requested", "before a withdrawal, during an account review and for unusual or high-value transactions", 8)],
    "When the casino asks for verification, which documents count (identity, address, payment method, source of funds) and how long the process takes.",
    'Lead with the triggers (account review, before a withdrawal, unusual or high-value transactions, changes to account or payment details). Then a TABLE with two columns, document type | accepted '
    'documents, one row each for identity (passport, national identity card, driving licence), address (utility bill, bank statement), payment method (bank or card ownership evidence, digital '
    'wallet ownership evidence) and source of funds (proof of income, bank statements, other supporting financial documents); the source-of-funds row applies only when requested. Then one '
    'sentence with the two periods exactly as given: documents are due up to 30 days after the request, and a complete set is normally reviewed within up to 10 days. Do not say that '
    'verification is needed at registration or for login: it is requested on the triggers above.')

# b07 security (cluster k06)
add(2, "Account Security and Privacy", "mandatory", ["k06"],
    ["brandinfo_privacy_policy.privacy_policy.security", "brandinfo_privacy_policy.terms_conditions.account_terms"], 75, {}, ["paragraph"],
    [("Account Security", 10), ("Login Credentials", 8)],
    [("Account Holder", "safeguards", "the login credentials", 8)],
    "Who is responsible for the credentials and what the operator does to protect accounts and data.",
    f'Lead with the player\'s own part: the account holder is responsible for safeguarding the login credentials. Then the operator\'s part exactly at the level of detail of the Brand Information: '
    f'technical and organisational safeguards protect accounts, payments and personal information, and the operator may suspend activity for verification or suspected abuse. '
    f'{NO_SECURITY_CLAIMS} Do not claim an audit or a certificate. Do not print the contact addresses of the privacy policy (they contain the brand name).')

# b08 welcome bonus (cluster k10, the medium competitor has it)
add(2, "Welcome Bonus After Registration", "unique", ["k10"],
    ["brandinfo_welcome.welcome_bonus.name", "brandinfo_welcome.welcome_bonus.bonus_percentage", "brandinfo_welcome.welcome_bonus.maximum_bonus",
     "brandinfo_welcome.welcome_bonus.free_spins", "brandinfo_welcome.welcome_bonus.minimum_deposit", "brandinfo_welcome.welcome_bonus.wagering_requirement",
     "brandinfo_welcome.welcome_bonus.claiming_procedure"], 75, {}, ["paragraph"],
    [("Casino Welcome Bonus", 10), ("First Deposit", 8), ("Wagering Requirement", 7)],
    [("Casino Welcome Bonus", "requires", "a first qualifying deposit of €50 and activation in My Bonuses", 8)],
    "What a new account can claim: the Casino Welcome Bonus, its size, the minimum first deposit, the wagering and the four claiming steps.",
    'This page is about the account, so keep the bonus short and strictly to the Brand Information: the Casino Welcome Bonus is a first-deposit casino bonus of 188% up to €2,088 plus 18 free spins; '
    'the minimum first deposit is €50; wagering is 25x the deposit plus bonus amount. Claiming: register and complete the personal details, make the first qualifying deposit, activate the bonus in '
    'My Bonuses before placing any wager, play eligible games and complete the wagering. Use the €50 minimum of the bonus; do NOT mention the general minimum deposit of €10 on this page. '
    'Do not add terms that are not listed (validity, limits, exclusions are described elsewhere). Do not promise winnings.')

# b09 support (cluster k08)
add(2, "Customer Support for Account Questions", "mandatory", ["k08"],
    ["brandinfo_general.customer_support"], 55, {"Longfu88": 1}, ["paragraph"],
    [("Customer Support", 10), ("Live Chat", 8)],
    [("Customer Support", "answers", "account, login and verification questions through live chat and e-mail", 8)],
    "How to reach support with a login or account problem: live chat around the clock, e-mail and the languages of the support team.",
    'Support channels: 24/7 live chat and e-mail. Print the e-mail address exactly as given in the Brand Information; it contains the tracked keyword "Longfu88", which is the one occurrence this block '
    'allows (so do not write the brand name anywhere else in the block). Support languages: English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese. Say which kinds of account '
    'questions go here (login failure, a reset e-mail that does not arrive, document upload) without response-time promises.')

# b10 FAQ (cluster k09)
add(2, "Login and Account FAQ", "mandatory", ["k09"],
    ["brandinfo_account.login.method", "brandinfo_account.login.password_recovery[1]", "brandinfo_account.verification.typical_review_time",
     "brandinfo_general.minimum_age", "brandinfo_general.customer_support.channels"], 95, {"Longfu88": 1}, ["list"],
    [("Frequently Asked Questions", 10), ("Login", 7)],
    [("Player", "finds", "short answers to the most frequent login and account questions", 6)],
    "Six short questions and answers on login, password reset, verification time, age limit and support.",
    'A bulleted list of six items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required here for the question text only. Questions, in this order: '
    'how to log in (e-mail and password), what to do after a forgotten password (Forgot Password and the e-mailed reset link), which login method the casino uses (e-mail and password), how long '
    'verification takes (a complete document set is normally reviewed within up to 10 days), what the minimum age is (18), where to turn when login still fails (customer support, live chat 24/7; '
    'do not print the e-mail). Answers repeat the facts of the sections of the page in other words and add nothing new. Do not answer questions about multiple devices, lockouts or login limits: '
    'no data. Use "Longfu88" exactly once and no other tracked keyword.')

intent = ("A returning or new player in Malaysia wants to sign in to a Longfu88 account (or find out how to register first) and needs the exact steps, "
          "the password reset, what to do when the login fails, why the casino asks for verification and where to get help. The page is a task page about "
          "the account entrance; the licence, the games, payments and the full bonus programme belong to other pages of the site. The structure follows the "
          "login pages of the competitors of the medium size group.")
skipped = [{"id": "k11", "reason": "Deposits and payment methods belong to the payments page of the site."}]

brief = {"intent_summary": intent, "blocks": blocks, "skipped_clusters": skipped}
(RUN / "llm").mkdir(parents=True, exist_ok=True)
(RUN / "llm" / "brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=1), encoding="utf-8")
(RUN / "llm" / "review.json").write_text(json.dumps({"issues": [], "blocks": blocks}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(blocks), "blocks, mid words", sum(round((b["words_min"] + b["words_max"]) / 2) for b in blocks))
