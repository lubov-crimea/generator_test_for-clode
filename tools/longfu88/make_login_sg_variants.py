"""Blueprint of 12 ТЗ variants for the Longfu88 login page (brand-subpage, GEO SG) -> input/variants/longfu88-login-sg.json.
Base run: runs/longfu88-login-sg (tools/longfu88/make_login_sg_base.py, the OPTIMUM group `medium`). Run from the project root:
    python tools/longfu88/make_login_sg_variants.py
    python -m textgen variants input/variants/longfu88-login-sg.json --force

The two competitors fall into three size groups (python -m textgen tiers longfu88-login-sg --texts 12):
    small  844            -> target 844,  limit 1013   4 variants: v01-v04, fewer topics, each one deeper than in a short text
    medium 844/1754 mean  -> target 1299, limit 1559   6 variants: v05-v10, ten topics each, every variant with its own set
    large  1754           -> limit 1754 (x1.0)         2 variants: v11-v12, the base plus the sections of the big competitor and more
Base blocks (the topics): b01 intro, b02 registration, b03 login, b04 password reset, b05 login problems, b06 verification,
b07 security, b08 welcome bonus, b09 account checks before the first payout, b10 mobile access, b11 currencies and the one-account
rule, b12 taking a break / closing the account, b13 communication preferences and cookies, b14 support, b15 FAQ.
New topics (a block the base does not have, facts from the knowledge base only): VIP levels, what opens after the login, the data the
casino holds, inactivity / complaints / changes of terms.

Topic sets (b01 intro is in every variant; "d" = a deeper treatment than the base):
    v01 small   b03+b04 b02 b06+b07 b14 b15
    v02 small   b02 b08(d) b03 b10 b11 b15
    v03 small   b03 b04 b05(d) b06(d) b09(d) b14
    v04 small   b02 b07(d) b11 b12 b13 b14
    v05 medium  b02 b08 b03 b04 b05 b06 b07 GAMES b14 b15
    v06 medium  b03 b05 b04 b06 b09 b07 TERMS b02 b14 b15
    v07 medium  b03 b04 b07 DATA b06 b02 b11 b13 b08 b14 b15
    v08 medium  b03 b04 b10(d) b02 b06 b07 b09 b13 b15 b14
    v09 medium  b12(d) b03 b04 b02 b06 b09 b11 b13 b14 b15
    v10 medium  b02 b08(d) b03 b09 b06 b10 b12 VIP b14 b15
    v11 large   every base topic + VIP, GAMES, DATA
    v12 large   b02 b06(d) b03 b04 b05 b07 b09(d) b10 b12(d) TERMS VIP b14 b15"""
import json
from pathlib import Path

K0, KL, K1, K2, K3 = "Longfu88", "Longfu88 login", "Longfu login", "Longfu88 register", "Longfu88 casino login"


def kw(k0=0, kl=0, k1=0, k2=0, k3=0):
    return {K0: k0, KL: kl, K1: k1, K2: k2, K3: k3}


# exact pieces of the base notes (tools/longfu88/make_login_sg_base.py) that a variant changes
B01_TOPICS = "(login, password reset, registration, verification, security, mobile access, support)"
B02_LIST = ("then a NUMBERED list with the three login steps in the order of the Brand Information (select Login on the website; enter the registered "
            "e-mail and password; complete any security check and access the account)")
B02_PROSE = ("then one short paragraph that walks through the three login steps in the order of the Brand Information (select Login on the website; "
             "enter the registered e-mail and password; complete any security check and access the account)")
B02_NEXT = "Do not explain password reset here (next sub-section)."
B02_NEXT_SEPARATE = "Do not explain password reset here (a separate section)."
B03_LIST = "One lead-in sentence, then a NUMBERED list with the three recovery steps in the order of the Brand Information"
B03_PROSE = "One short paragraph with the three recovery steps in the order of the Brand Information"
B05_TABLE = "Then a TABLE with two columns, document type | accepted documents, one row each for identity"
B05_LIST = "Then a bulleted list, one item each for identity"
B05_ROW = "; the source-of-funds row applies only when requested"
B05_ITEM = "; the source-of-funds item applies only when requested"
B08_SHORT = ("This page is about the account, so keep the bonus short and strictly to the Brand Information:", "Keep the bonus strictly to the Brand Information:")
B08_TERMS = ("Do not add terms that are not listed (validity, limits, exclusions are described elsewhere).", "Do not add terms that are not listed.")
B09_BANK = ("Do NOT list payment methods, limits, fees, commissions, turnover rules or bank settlement times: they belong to the payments page of the site.",
            "Do NOT list payment methods, limits, fees, commissions or turnover rules: they belong to the payments page of the site.")

VER_SMALL_DROP = ["brandinfo_account.verification.triggers", "brandinfo_account.verification.document_submission_window"]
VER_SMALL_TABLE = ("A TABLE with two columns, document type | accepted documents, one row each for identity (passport, national identity card, driving licence), address (utility bill, "
                   "bank statement), payment method (bank or card ownership evidence, digital wallet ownership evidence) and source of funds (proof of income, bank statements, other supporting "
                   "financial documents); the source-of-funds row applies only when requested. Before the table one sentence says that the casino may ask for these documents; then, after "
                   "the table, one sentence: a complete document set is normally reviewed within up to 10 days. Do not say that verification is needed at registration or for login.")
VER_SMALL_LIST = VER_SMALL_TABLE.replace("A TABLE with two columns, document type | accepted documents, one row each for identity", "A bulleted list, one item each for identity").replace(
    "the source-of-funds row applies only", "the source-of-funds item applies only")

# every question names the one cheap fact its answer needs (a figure, a name, one step): the answers repeat the sections, they do not retell them
FAQ = {
    "login": ("how to log in (with the registered e-mail and password, as the page explains)", ["brandinfo_account.login.method"]),
    "forgot": ("what to do after a forgotten password (request a reset link with the registered e-mail)", ["brandinfo_account.login.password_recovery[1]"]),
    "method": ("which login method the casino uses (e-mail and password)", ["brandinfo_account.login.method"]),
    "verif": ("how long verification takes (a complete document set is normally reviewed within up to 10 days)", ["brandinfo_account.verification.typical_review_time"]),
    "docs": ("which identity document is accepted (passport, national identity card or driving licence)", ["brandinfo_privacy_policy.kyc_aml.required_documents.identity"]),
    "age": ("what the minimum age is (18, and the player must be legally permitted to gamble where they live)", ["brandinfo_general.minimum_age"]),
    "support": ("where to turn when the login still fails (customer support: live chat 24/7 or e-mail; do not print the e-mail address)", ["brandinfo_general.customer_support.channels"]),
    "oneacc": ("whether a player may hold more than one account (no: one personal account per player)", ["brandinfo_account.registration.eligibility[1]"]),
    "regdet": ("which details registration asks for (e-mail, password, legal name, date of birth, residential address)", ["brandinfo_account.registration.required_details"]),
    "mobile": ("whether a player can log in from a phone (yes, in the browser of a smartphone or tablet; a home-screen shortcut is possible)", ["brandinfo_app.app_information.platforms"]),
    "bonus": ("when the welcome bonus can be claimed (after registration, on the first qualifying deposit of at least €50)", ["brandinfo_welcome.welcome_bonus.minimum_deposit"]),
    "lang": ("which languages support speaks (English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese)", ["brandinfo_general.customer_support.languages"]),
    "vip": ("whether there is a VIP programme (yes, with five tiers: Bronze, Silver, Gold, Platinum and Diamond)", ["brandinfo_loyalty.loyalty_vip_program.tiers"]),
    "payout": ("how fast a withdrawal request is processed (generally within three working days; do not promise a payout time)", ["brandinfo_privacy_policy.terms_conditions.withdrawal_terms[1]"]),
    "close": ("how to close the account (through customer support)", ["brandinfo_responsible_gaming.responsible_gaming.account_closure"]),
    "cookies": ("which cookies the site uses (necessary, preference, analytics and marketing cookies)", ["brandinfo_privacy_policy.privacy_policy.cookies"]),
    "currency": ("which currencies an account can use (EUR, USD, MYR, THB, SGD and USDT)", ["brandinfo_general.currencies"]),
    "inactive": ("what prolonged inactivity can lead to (an account review or closure under the terms)", ["brandinfo_privacy_policy.terms_conditions.inactivity"]),
}
BASE_FAQ_REFS = ["brandinfo_account.login.method", "brandinfo_account.login.password_recovery[1]", "brandinfo_account.verification.typical_review_time",
                 "brandinfo_general.minimum_age", "brandinfo_general.customer_support.channels"]


def faq(keys):
    """Override of the FAQ block: the questions of this variant, in order, and only the facts they need."""
    qs = "; ".join(f"({i}) {FAQ[k][0]}" for i, k in enumerate(keys, 1))
    notes = (f'A bulleted list of {len(keys)} items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required '
             f"here for the question text only. Questions, in this order: {qs}. Answers repeat the facts of the sections of the page in other words and add "
             "nothing new. Do not answer questions about multiple devices, lockouts or login limits: no data.")
    need = list(dict.fromkeys(r for k in keys for r in FAQ[k][1]))
    return {"notes": notes, "refs_add": [r for r in need if r not in BASE_FAQ_REFS], "refs_drop": [r for r in BASE_FAQ_REFS if r not in need],
            "summary": f"{len(keys)} short questions and answers on the login and the account."}


def blk(ids, level, heading, words, kws=None, fmt=None, edit=None, extra=None, summary=None, **more):
    b = {"from": ids, "level": level, "heading": heading, "words": words, "kw": kws or {}}
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


def intro(heading, words, topics, kws):
    return blk(["b01"], 1, heading, words, kws, edit=[(B01_TOPICS, topics)])


def new(level, heading, words, refs, ents, conns, summary, notes, covers, fmt=None, kws=None):
    """A block that the base ТЗ does not have: its facts come from `refs` only."""
    return blk([], level, heading, words, kws or {}, fmt, summary=summary, entities=ents, connections=conns, kb_refs=refs, notes=notes, covers_clusters=covers)


PL = ["paragraph", "list"]
VOICE_TAIL = " All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore."
LEGAL = "Do not say or imply that the casino is licensed, legal or approved in Singapore."
SKIP_REASON = {
    "k01": "covered by the registration and login blocks of the page",
}


# ------------------------------------------------------------------ new topics (blocks the base ТЗ does not have)
def vip(level, heading, words, kws=None):
    return new(level, heading, words,
               ["brandinfo_loyalty.loyalty_vip_program.tiers", "brandinfo_loyalty.loyalty_vip_program.progression", "brandinfo_loyalty.loyalty_vip_program.additional_benefits",
                "brandinfo_loyalty.loyalty_vip_program.important_terms"],
               [["VIP Programme", 10], ["VIP Points", 7], ["Tiers", 6]], [["Player", "earns", "VIP points through eligible real-money gameplay, which unlock reward levels", 8]],
               "What a logged-in player gets from the VIP programme: five tiers, points from real-money play, the extra benefits and the terms.",
               "Five tiers: Bronze, Silver, Gold, Platinum and Diamond. Points are earned through eligible real-money gameplay and unlock numbered reward levels. Additional benefits: personalised offers, "
               "VIP cashback, higher withdrawal limits and a personal VIP manager for eligible high tiers. Terms: reward and withdrawal limits may differ by VIP level and currency, and level-based benefits "
               "and eligibility may change under the programme rules. Do not give level numbers, point thresholds, rewards or limits (they are on the VIP page) and do not use the official name of the "
               "programme (it contains the brand name).", ["k09"], None, kws)


def games(level, heading, words, kws=None):
    return new(level, heading, words, ["brandinfo_games.game_types", "brandinfo_app.app_information.features"],
               [["Casino", 9], ["Sportsbook", 8]], [["Player Account", "gives access to", "the casino, the sportsbook, deposits, withdrawals and bonuses", 8]],
               "What a player reaches after logging in: the casino games, the sportsbook, the cashier and the bonuses.",
               "One lead-in sentence that names what the account gives access to (casino, sportsbook, account access, deposits, withdrawals, bonuses), then a bulleted list of the game categories "
               "exactly as in the Brand Information (slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, crash and instant games). No game names, providers "
               "or RTP values. Keep it short: this is a pointer to the rest of the site.", ["k07"], PL, kws)


def data(level, heading, words, kws=None):
    return new(level, heading, words,
               ["brandinfo_privacy_policy.privacy_policy.data_collected.identity_data", "brandinfo_privacy_policy.privacy_policy.data_collected.contact_data",
                "brandinfo_privacy_policy.privacy_policy.data_collected.verification_data", "brandinfo_privacy_policy.privacy_policy.data_sharing",
                "brandinfo_privacy_policy.privacy_policy.data_subject_rights"],
               [["Personal Data", 10], ["Data Sharing", 7], ["Data Subject Rights", 6]], [["Casino", "shares", "personal data with payment, identity-verification and technology providers and with regulators when required", 8]],
               "Which data the casino holds about an account holder, with whom it may be shared and which rights the player has.",
               "Three short groups of facts, exactly as in the Brand Information: the identity data (name, date of birth, identity documents), contact data (e-mail, telephone, residential address) and "
               "verification data (KYC documents, payment method ownership evidence) that the casino holds; the parties it may share data with (payment service providers, identity verification providers, "
               "technology providers, regulators and law enforcement when required); the rights of the player (access, rectification, erasure where legally permitted, restriction, objection, portability "
               "where applicable, withdrawal of consent). Do not print the e-mail addresses of the data protection contact (they contain the brand name), do not claim a certificate, an audit or "
               "encryption, and do not say how long data is kept. Neutral, no legal advice.", ["k05"], PL, kws)


def terms(level, heading, words, kws=None):
    return new(level, heading, words,
               ["brandinfo_privacy_policy.terms_conditions.inactivity", "brandinfo_privacy_policy.terms_conditions.complaints", "brandinfo_privacy_policy.terms_conditions.changes"],
               [["Account Terms", 9], ["Inactivity", 7], ["Complaints", 6]], [["Player", "contacts", "customer support to request a review of a dispute or an account decision", 8]],
               "Three rules of the terms that touch an account: inactivity, complaints about account decisions and changes of the terms.",
               "Three facts, exactly as in the Brand Information: prolonged inactivity may trigger an account review or closure under the applicable terms; a dispute or an account decision is reviewed "
               "when the player contacts customer support; the operator may modify promotional and contractual terms and publishes updates on the site. No time limits, no named regulator or "
               "ombudsman, no dispute deadlines and no promise of an outcome. Calm and factual.", ["k17"], None, kws)


variants = []

# ================================================================ SMALL (target 844, limit 1013): fewer topics, each one deeper
variants.append({
    "id": "v01", "name": "Quick access (small, flat)", "tier": "small", "angle": "A returning player who wants to get in within a minute.",
    "skipped_clusters": [{"id": "k03", "reason": "the fastest route to the account needs no welcome offer; the offer is left to the longer texts"}],
    "intent_summary": ("Short brand-subpage for the small size group of the competitors: logging in to the Longfu88 account for players from Singapore in the fewest words: the login steps "
                       "with the password reset in one section, registration for those without an account, the documents with the account security, support and a short FAQ. Page voice: short, "
                       "dense paragraphs of two or three sentences, sentences of about 14 words, imperative where a step is described, no scene-setting, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login: Quick Access for Singapore Players", 80, "(login steps, password reset, registration, documents, support)", kw(k0=1)),
        blk(["b03", "b04"], 2, "Log In and Reset a Forgotten Password", 160, kw(k0=1, kl=1, k1=1), PL, [(B02_NEXT, ""), (B03_LIST, B03_PROSE)],
            "The three login steps as a numbered list, then the password reset in one short paragraph.",
            summary="The three login steps in order, followed by the password reset through the e-mailed link."),
        blk(["b02"], 2, "Longfu88 Register: Open an Account", 150, kw(k0=1), PL),
        blk(["b06", "b07"], 2, "Verification Documents and Account Security", 200, kw(k0=1), ["paragraph", "table"],
            summary="Which documents the casino may ask for and who protects the account.",
            notes=VER_SMALL_TABLE + " Close the block with one sentence: the account holder is responsible for safeguarding the login credentials, and technical and organisational "
                  "safeguards protect accounts, payments and personal information. No certificate, encryption or two-factor claims.",
            refs_drop=VER_SMALL_DROP + ["brandinfo_privacy_policy.terms_conditions.account_terms"],
            refs_add=["brandinfo_privacy_policy.terms_conditions.account_terms[0]"]),
        blk(["b14"], 2, "Get Help", 70, kw(k0=1)),
        blk(["b15"], 2, "Login FAQ", 130, kw(k0=1), **faq(["login", "forgot", "verif", "oneacc", "regdet", "support"])),
    ],
})

variants.append({
    "id": "v02", "name": "Register first, offer-led (small)", "tier": "small", "angle": "A newcomer who needs the account, the welcome offer and the phone access.",
    "skipped_clusters": [{"id": "k05", "reason": "the short text keeps the account entry (registration, login, the welcome offer) and leaves the verification and security block to the longer texts of the site"}],
    "intent_summary": ("Short brand-subpage for the small size group: a newcomer to Longfu88 in Singapore opens the account, sees what the welcome offer asks for, logs in, uses the site on a phone "
                       "and knows the currency and one-account rules. Page voice: a patient guide in plain \"first, then\" order, sentences of about 15 words, one plain invitation to register. "
                       "The welcome offer is covered in more detail than in the other short texts. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Account Guide: Open, Log In and Start Playing", 90, "(registration, the welcome offer, login, mobile access, currencies)", kw(k0=1)),
        blk(["b02"], 2, "Open the Account First", 140, kw(k0=1, k2=1), PL, extra="One plain invitation to register is allowed here."),
        blk(["b08"], 2, "A Welcome Offer for New Accounts", 135, kw(k0=1), edit=[B08_TERMS], extra="Add the validity of the offer, its wagering on the free spins and the maximum bet while the bonus is active: facts of the Brand Information only.",
            refs_add=["brandinfo_welcome.welcome_bonus.validity", "brandinfo_welcome.welcome_bonus.free_spins_wagering", "brandinfo_welcome.welcome_bonus.maximum_bet"]),
        blk(["b03"], 2, "Longfu88 Login on the Website", 105, kw(k0=1, k1=1, k3=1), edit=[(B02_NEXT, "Do not explain password reset here.")]),
        blk(["b10"], 2, "Mobile Access in the Browser", 110, kw(k0=1)),
        blk(["b11"], 2, "Currencies and the One-Account Rule", 80, kw(k0=1), PL),
        blk(["b15"], 2, "Beginner FAQ", 130, kw(k0=1), **faq(["regdet", "login", "oneacc", "bonus", "mobile", "currency"])),
    ],
})

variants.append({
    "id": "v03", "name": "Troubleshooting (small)", "tier": "small", "angle": "A player who already has an account and cannot get in.",
    "skipped_clusters": [{"id": "k03", "reason": "the welcome bonus is no help to a player who cannot sign in; the offer is left to the longer texts"}],
    "intent_summary": ("Short troubleshooting brand-subpage for the small size group: why a Longfu88 login can fail for a player in Singapore, the normal route, the password reset, the checks that can hold "
                       "an account, what the first payout needs from the account and where to ask. Page voice: practical and calm, cause then fix, sentences of about 16 words, "
                       "no calls to action. Flat H2s with one H3." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login Problems: Quick Fixes and Checks", 90, "(the login route, password reset, reasons for a failed login, verification, payout checks, support)", kw(k0=1)),
        blk(["b03"], 2, "How the Login Works", 105, kw(k0=1, kl=1, k1=1), edit=[(B02_NEXT, B02_NEXT_SEPARATE)]),
        blk(["b04"], 3, "Reset a Lost Password", 75),
        blk(["b05"], 2, "Why a Login Fails", 125, kw(k0=1, k2=1), extra="Say that a player without an account starts with registration (use the phrase once, naturally) and add that prolonged inactivity may trigger an account review or closure.",
            refs_add=["brandinfo_privacy_policy.terms_conditions.inactivity"]),
        blk(["b06"], 2, "Checks That Can Hold an Account", 165, kw(k0=1), PL, [(B05_TABLE, B05_LIST), (B05_ROW, B05_ITEM)],
            extra="After the list add the procedure in one sentence: upload legible, current documents that match the account profile; telephone or face verification if requested; wait for approval before a withdrawal.",
            refs_add=["brandinfo_account.verification.procedure"]),
        blk(["b09"], 2, "What the Account Needs Before a Payout", 125, kw(k0=1), extra="Add that failing the checks can lead to a refused transaction, account restrictions or withheld withdrawals.",
            refs_add=["brandinfo_privacy_policy.kyc_aml.failure_consequences"]),
        blk(["b14"], 2, "Where to Get Help With the Login", 80, kw(k0=1)),
    ],
})

variants.append({
    "id": "v04", "name": "Control and privacy (small)", "tier": "small", "angle": "A cautious reader who wants to know what the player controls.",
    "skipped_clusters": [{"id": "k03", "reason": "the text is about the control of the account (privacy, settings, closing); the welcome offer is left to the longer texts"}],
    "intent_summary": ("Short brand-subpage for the small size group: what an account holder of Longfu88 in Singapore controls: the registration details, the protection of the credentials and the data, "
                       "the currency and one-account rules, taking a break or closing the account, marketing and cookie settings, and where to ask. Page voice: sober and exact, every claim "
                       "tied to a stated fact, sentences of about 17 words, no reassurance beyond the facts; no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login and Account Control for Singapore", 80, "(registration, protection of the data, rules of the account, taking a break, settings, support)", kw(k0=1, kl=1)),
        blk(["b02"], 2, "Longfu88 Register: Details and Eligibility", 150, kw(k0=1, k1=1), PL),
        blk(["b07"], 2, "Protecting Your Details", 135, kw(k0=1),
            extra="Add with whom data may be shared and which rights the player has, as two short lists inside the paragraph.",
            refs_add=["brandinfo_privacy_policy.privacy_policy.data_sharing", "brandinfo_privacy_policy.privacy_policy.data_subject_rights"]),
        blk(["b11"], 2, "Account Currencies and Player Rules", 95, kw(k0=1), extra="Add that residents must be legally permitted to gamble where they live.",
            refs_add=["brandinfo_privacy_policy.terms_conditions.eligibility.residency_requirements"]),
        blk(["b12"], 2, "Stopping, Pausing and Closing an Account", 150, kw(k0=1), PL, extra="Add the four steps of the procedure as a numbered list, in the order of the Brand Information, without the e-mail address.",
            refs_add=["brandinfo_responsible_gaming.responsible_gaming.procedure", "brandinfo_responsible_gaming.responsible_gaming.self_assessment"]),
        blk(["b13"], 2, "Marketing Messages and Cookies", 80, kw(k0=1)),
        blk(["b14"], 2, "Where to Ask Account Questions", 75, kw(k0=1)),
    ],
})

# ================================================================ MEDIUM (target 1299, limit 1559): ten topics each, every variant with its own set
variants.append({
    "id": "v05", "name": "Newcomer walkthrough (register first, nested)", "tier": "medium", "angle": "A new player who has no account yet and wants one guided path.",
    "intent_summary": ("Step-by-step brand-subpage for a newcomer to Longfu88 in Singapore: the account is created (with the welcome offer named as the reason to register), then the player logs in, "
                       "learns what to do when the password or the login fails, passes the verification, keeps the account safe and sees what the account opens. Page voice: a patient guide, "
                       "\"first, then\" logic, one short explanation of verification the first time it appears, sentences of about 17 words, one plain invitation to register. Steps are H2s, "
                       "their details H3s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Login Guide for New Players in Singapore", 85, "(registration, the welcome offer, login, password reset, verification, security, support)", kw(k0=1, k3=1)),
        blk(["b02"], 2, "Step 1: Longfu88 Register and Create Your Account", 140, kw(k0=1), PL, extra="One plain invitation to register is allowed here."),
        blk(["b08"], 3, "What a New Account Can Claim", 120, kw(k0=1), edit=[B08_TERMS], extra="Add the validity, the free-spins wagering and the maximum bet of the offer.",
            refs_add=["brandinfo_welcome.welcome_bonus.validity", "brandinfo_welcome.welcome_bonus.free_spins_wagering", "brandinfo_welcome.welcome_bonus.maximum_bet"]),
        blk(["b03"], 2, "Step 2: Log In", 95, kw(k0=1, k1=1)),
        blk(["b04"], 3, "If You Forget the Password", 65),
        blk(["b05"], 3, "When the Login Does Not Work", 75, kw(k0=1)),
        blk(["b06"], 2, "Step 3: Verify the Account", 130, kw(k0=1), extra="Explain in one clause what verification is the first time the word appears."),
        blk(["b07"], 2, "Keeping the Account Safe", 85, kw(k0=1)),
        games(2, "What Opens After the Login", 70, kw(k0=1)),
        blk(["b14"], 2, "Help With Your Account", 55, kw(k0=1)),
        blk(["b15"], 2, "Beginner Questions", 115, kw(k0=1), **faq(["regdet", "login", "forgot", "oneacc", "bonus", "support"])),
    ],
})

variants.append({
    "id": "v06", "name": "Troubleshooting-led", "tier": "medium", "angle": "A player who already has an account and cannot get in.",
    "skipped_clusters": [{"id": "k03", "reason": "a player who cannot sign in does not need the welcome offer; the offer belongs to the bonus page of the site"}],
    "intent_summary": ("Troubleshooting-led brand-subpage about the Longfu88 login in Singapore for a player who is locked out or unsure: the normal route, why a login fails, the password reset, the "
                       "checks that can hold an account and the first payout, the protection of the credentials, the rules of the terms that touch an account, registration for those who have no "
                       "account, and support. Page voice: practical and calm, cause then fix, sentences of about 16 words, a short consequence after each limit; no calls to action. "
                       "Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login Help: Fix Access Problems", 85, "(the normal login route, reasons for a failed login, password reset, verification, the first payout, security, registration, support)", kw(k0=1)),
        blk(["b03"], 2, "The Normal Login Route", 90, kw(k0=1, kl=1, k1=1), edit=[(B02_NEXT, B02_NEXT_SEPARATE)]),
        blk(["b05"], 2, "Common Reasons for a Failed Login", 110, kw(k0=1), extra="Add that prolonged inactivity may trigger an account review or closure.",
            refs_add=["brandinfo_privacy_policy.terms_conditions.inactivity"]),
        blk(["b04"], 2, "Reset the Password", 70, kw(k0=1)),
        blk(["b06"], 2, "Verification Checks and Held Accounts", 140, kw(k0=1), PL, [(B05_TABLE, B05_LIST), (B05_ROW, B05_ITEM)]),
        blk(["b09"], 2, "Why the First Payout Waits for Checks", 105, kw(k0=1), extra="Add that failing the checks can lead to a refused transaction, account restrictions or withheld withdrawals.",
            refs_add=["brandinfo_privacy_policy.kyc_aml.failure_consequences"]),
        blk(["b07"], 2, "Keeping Credentials Safe", 80, kw(k0=1)),
        terms(2, "Inactivity, Complaints and Rule Changes", 80, kw(k0=1)),
        blk(["b02"], 2, "No Account Yet? Longfu88 Register", 115, kw(k0=1), PL),
        blk(["b14"], 2, "Contact the Support Team", 55, kw(k0=1)),
        blk(["b15"], 2, "Common Login Questions", 110, kw(k0=1), **faq(["login", "forgot", "docs", "verif", "age", "support", "inactive"])),
    ],
})

variants.append({
    "id": "v07", "name": "Security-conscious", "tier": "medium", "angle": "A cautious player who wants to know what protects the account before logging in.",
    "intent_summary": ("Security-conscious brand-subpage about the Longfu88 login in Singapore for a cautious reader: how to sign in safely, what protects the account, which data the casino holds and "
                       "shares, why it asks for documents, the registration rules, the currency and one-account rules, the cookie and marketing settings, the welcome offer in brief and support. "
                       "Page voice: sober and exact, every claim tied to a stated fact, sentences of about 18 words with a few shorter ones, no reassurance beyond the facts; no calls to action. "
                       "H2 sections with one H3." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login: Secure Access to Your Account", 85, "(login, password reset, account protection, the data the casino holds, verification documents, registration, settings, support)", kw(k0=1, kl=1)),
        blk(["b03"], 2, "Signing In Safely", 90, kw(k0=1, k1=1)),
        blk(["b04"], 3, "Replacing a Lost Password", 60, kw(k0=1)),
        blk(["b07"], 2, "What Protects the Account", 90, kw(k0=1), extra="State the duty of the account holder first and the operator's safeguards second."),
        data(2, "What Data the Casino Holds", 110, kw(k0=1)),
        blk(["b06"], 2, "Why the Casino Asks for Documents", 125, kw(k0=1),
            extra="Add the stages at which checks happen (registration reviews, deposits, withdrawals, ongoing account monitoring).",
            refs_add=["brandinfo_privacy_policy.kyc_aml.verification_requirements.verification_stages"]),
        blk(["b02"], 2, "Registration Rules Behind Every Account", 105, kw(k0=1, k2=1), PL),
        blk(["b11"], 2, "Accurate Details and Account Currencies", 70, kw(k0=1)),
        blk(["b13"], 2, "Cookies and Marketing Settings", 60, kw(k0=1)),
        blk(["b08"], 2, "The Welcome Offer in Brief", 75, kw(k0=1)),
        blk(["b14"], 2, "Who to Contact", 55, kw(k0=1)),
        blk(["b15"], 2, "Account Safety Questions", 100, kw(k0=1), **faq(["login", "verif", "docs", "oneacc", "cookies", "support"])),
    ],
})

variants.append({
    "id": "v08", "name": "Mobile-first", "tier": "medium", "angle": "A player who mostly uses a phone.",
    "skipped_clusters": [{"id": "k03", "reason": "the phone login is the topic here; the welcome offer is left to the bonus page of the site"}],
    "intent_summary": ("Mobile-first brand-subpage about the Longfu88 login in Singapore: logging in from a phone, a tablet or a computer with the home-screen shortcut, the password reset, creating an "
                       "account on a phone, the documents to keep ready, account safety, the first payout from a phone, the settings, a mobile FAQ and support. Page voice: brisk and "
                       "concrete, device words in every section (phone, browser, shortcut), sentences of about 15 words; no calls to action. Flat H2s with one H3. There is no downloadable "
                       "app in the facts." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login on Mobile and Desktop", 85, "(login on a phone or a computer, password reset, registration, documents, account safety, the first payout, support)", kw(k0=1)),
        blk(["b03"], 2, "Log In from Any Device", 90, kw(k0=1, kl=1, k1=1), PL, [(B02_LIST, B02_PROSE), (B02_NEXT, B02_NEXT_SEPARATE)]),
        blk(["b04"], 3, "Password Reset on a Phone", 60, kw(k0=1)),
        blk(["b10"], 2, "Add a Home Screen Shortcut on Android and iOS", 145, kw(k0=1), PL,
            extra="Add the platforms named in the Brand Information (Android, iOS and mobile web) and say that every feature of the site is the same on a phone: casino, sportsbook, account access, deposits, withdrawals, bonuses.",
            refs_add=["brandinfo_app.app_information.features"]),
        blk(["b02"], 2, "Create an Account from Your Phone", 120, kw(k0=1, k2=1), PL),
        blk(["b06"], 2, "Documents to Keep Ready", 120, kw(k0=1), PL, [(B05_TABLE, B05_LIST), (B05_ROW, B05_ITEM)]),
        blk(["b07"], 2, "Account Safety on a Phone", 75, kw(k0=1)),
        blk(["b09"], 2, "First Payout From a Phone", 95, kw(k0=1)),
        blk(["b13"], 2, "Phone Preferences and Cookies", 60, kw(k0=1)),
        blk(["b15"], 2, "Mobile Login FAQ", 105, kw(k0=1), **faq(["mobile", "login", "forgot", "support", "lang", "payout"])),
        blk(["b14"], 2, "Support on Chat or E-mail", 55, kw(k0=1)),
    ],
})

variants.append({
    "id": "v09", "name": "Responsible account use", "tier": "medium", "angle": "A reader who wants to stay in control of the account.",
    "skipped_clusters": [{"id": "k03", "reason": "the text is about control of the account; the welcome offer is left to the bonus page of the site"}],
    "intent_summary": ("Brand-subpage about the Longfu88 account for players in Singapore who want to stay in control: how to pause, self-exclude or close the account and where independent help is found, "
                       "then the login and the password reset, the registration rules, verification, the checks before the first payout, the currency and one-account rules, the marketing and cookie "
                       "settings and support. Page voice: calm and practical, the control topic first, sentences of about 17 words, no moralising, no calls to action. H2 sections with one H3." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login: Manage Your Account Responsibly", 85, "(taking a break or closing the account, login, password reset, registration, verification, payout checks, settings, support)", kw(k0=1)),
        blk(["b12"], 2, "Taking Control: Pause, Self-Exclusion and Closure", 160, kw(k0=1), PL,
            extra="Add the four steps of the procedure as a numbered list, in the order of the Brand Information, without the e-mail address, and the self-assessment questions that help to recognise possible harm.",
            refs_add=["brandinfo_responsible_gaming.responsible_gaming.procedure", "brandinfo_responsible_gaming.responsible_gaming.self_assessment"]),
        blk(["b03"], 2, "Longfu88 Login: Entering the Account", 85, kw(k0=1, k1=1)),
        blk(["b04"], 3, "If the Password Is Lost", 60),
        blk(["b02"], 2, "Opening an Account Responsibly", 115, kw(k0=1, k2=1), PL),
        blk(["b06"], 2, "Verification Without Surprises", 115, kw(k0=1)),
        blk(["b09"], 2, "Payout Checks Explained", 95, kw(k0=1)),
        blk(["b11"], 2, "One Account, Accurate Details, Supported Currencies", 80, kw(k0=1), extra="Add that residents must be legally permitted to gamble where they live.",
            refs_add=["brandinfo_privacy_policy.terms_conditions.eligibility.residency_requirements"]),
        blk(["b13"], 2, "Choosing What You Receive", 65, kw(k0=1)),
        blk(["b14"], 2, "Customer Support and Independent Help", 60, kw(k0=1)),
        blk(["b15"], 2, "Responsible Account FAQ", 105, kw(k0=1), **faq(["close", "login", "forgot", "age", "currency", "support"])),
    ],
})

variants.append({
    "id": "v10", "name": "Offer-led account guide", "tier": "medium", "angle": "A player who registers for the welcome offer and wants to know how it all works.",
    "intent_summary": ("Brand-subpage for players in Singapore who come to Longfu88 for the welcome offer: registration, the Casino Welcome Bonus with its conditions and the activation in My Bonuses, the login, "
                       "what the first payout needs, the documents, the phone access, the VIP levels that open after the login, how to take a break and support. Page voice: brisk and concrete, "
                       "the offer named early, sentences of about 16 words, a consequence after each condition, no promises of winnings; one plain invitation to register. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Account Guide: Sign Up, Claim the Offer, Log In", 85, "(registration, the welcome offer, login, the first payout, verification, phone access, the VIP levels, taking a break, support)", kw(k0=1, k3=1)),
        blk(["b02"], 2, "Longfu88 Register: Start With the Account", 125, kw(k0=1), PL, extra="One plain invitation to register is allowed here."),
        blk(["b08"], 2, "The Casino Welcome Bonus Step by Step", 155, kw(k0=1), PL, edit=[B08_SHORT, B08_TERMS], extra="Add the validity, the free-spins wagering, the maximum bet and the maximum cashout of the offer, and show the four claiming steps as a numbered list.",
            refs_add=["brandinfo_welcome.welcome_bonus.validity", "brandinfo_welcome.welcome_bonus.free_spins_wagering", "brandinfo_welcome.welcome_bonus.maximum_bet",
                      "brandinfo_welcome.welcome_bonus.maximum_cashout", "brandinfo_welcome.welcome_bonus.important_terms[2]"]),
        blk(["b03"], 2, "Longfu88 Login and Bonus Activation", 90, kw(k0=1, k1=1), extra="Add that the offer is activated in My Bonuses after the login."),
        blk(["b09"], 2, "What Happens at the First Payout", 100, kw(k0=1)),
        blk(["b06"], 2, "Verification Before Payouts", 110, kw(k0=1)),
        blk(["b10"], 2, "Play on Mobile", 75, kw(k0=1)),
        vip(2, "VIP Levels After the Login", 85, kw(k0=1)),
        blk(["b12"], 2, "Taking a Break From the Offers", 85, kw(k0=1)),
        blk(["b14"], 2, "Questions About Offers and Accounts", 55, kw(k0=1)),
        blk(["b15"], 2, "Offer and Login FAQ", 110, kw(k0=1), **faq(["bonus", "login", "payout", "verif", "vip", "support"])),
    ],
})

# ================================================================ LARGE (limit 1754 = the mean of the group): more topics, shorter than the limit
variants.append({
    "id": "v11", "name": "Full account handbook (large)", "tier": "large", "angle": "A reader who wants the whole account topic on one page.",
    "intent_summary": ("Complete brand-subpage for the large size group of the competitors, built like the longest login page of the query: a handbook of the Longfu88 account for players from Singapore "
                       "with entry (registration and the welcome offer), access (login, lost password, failed logins), compliance (verification documents and the checks before the first payout), "
                       "protection (credentials and the data the casino holds), settings and communication, currencies and the one-account rule, taking a break or closing the account, what opens "
                       "after the login, mobile access, the VIP levels, support and a FAQ. Page voice: reference-like, each H2 opens with what the section is for, sentences of about 18 words, a "
                       "consequence after each condition; one plain invitation to register. Every section is written only from the facts of its Brand Information; where a section has few facts "
                       "it stays short. H2 sections with H3 details." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Account Handbook for Singapore Players", 90, "(entry, access, compliance, protection, settings, taking a break, mobile access, the VIP levels, support)", kw(k0=1, k3=1)),
        blk(["b02"], 2, "Entry: Opening an Account", 130, kw(k0=1, k2=1), PL, extra="One plain invitation to register is allowed here."),
        blk(["b08"], 3, "The Welcome Offer in Brief", 80, kw(k0=1)),
        blk(["b03"], 2, "Access: The Login Route", 90, kw(k0=1, kl=1, k1=1)),
        blk(["b04"], 3, "Recovering a Lost Password", 65, kw(k0=1)),
        blk(["b05"], 3, "Diagnosing Failed Logins", 80, kw(k0=1)),
        blk(["b07"], 2, "Protection: Credentials and Safeguards", 85, kw(k0=1)),
        data(3, "The Data the Casino Holds and Shares", 105, kw(k0=1)),
        blk(["b06"], 2, "Compliance: Verification Documents", 130, kw(k0=1),
            extra="After the table give the procedure in one sentence (upload legible, current documents that match the account profile; telephone or face verification if requested; wait for approval before a withdrawal).",
            refs_add=["brandinfo_account.verification.procedure"]),
        blk(["b09"], 3, "Checks Before the First Payout", 85, kw(k0=1)),
        blk(["b13"], 2, "Settings: Communication Preferences and Cookies", 50, kw(k0=1)),
        blk(["b11"], 2, "Currencies and the One-Account Rule", 55, kw(k0=1)),
        blk(["b12"], 2, "Pausing, Self-Exclusion and Closing the Account", 100, kw(k0=1), extra="Add the self-assessment questions that help to recognise possible harm.",
            refs_add=["brandinfo_responsible_gaming.responsible_gaming.self_assessment"]),
        games(2, "What Opens After the Login", 55, kw(k0=1)),
        blk(["b10"], 2, "Mobile and Tablet Access", 85, kw(k0=1)),
        vip(2, "VIP Levels and Rewards", 85, kw(k0=1)),
        blk(["b14"], 2, "Assistance and Contact Channels", 55, kw(k0=1)),
        blk(["b15"], 2, "Handbook FAQ", 120, kw(k0=1), **faq(["login", "forgot", "method", "regdet", "docs", "verif", "oneacc", "vip"])),
    ],
})

variants.append({
    "id": "v12", "name": "Account lifecycle (large)", "tier": "large", "angle": "A reader who follows the life of an account from opening to closing.",
    "skipped_clusters": [{"id": "k03", "reason": "the welcome offer is one clause of the registration block; its terms belong to the bonus page of the site"}],
    "intent_summary": ("Complete brand-subpage for the large size group, organised as the life of a Longfu88 account for players from Singapore: opening, proving who the player is, logging in and "
                       "recovering access, using the account on a phone, what the terms say about inactivity, complaints and changes, the VIP levels, taking a break or closing the account, and support. "
                       "Page voice: narrative and orderly, \"at this stage\" openings, sentences of about 19 words, one short summary sentence at the end of each section, no calls to action. H2 "
                       "stages with H3 details." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login and the Life of Your Account", 90, "(opening, verification, login, mobile access, the rules of the terms, the VIP levels, taking a break, support)", kw(k0=1)),
        blk(["b02"], 2, "Stage 1: Longfu88 Register and Open the Account", 135, kw(k0=1), PL,
            extra="Name the welcome offer in one clause (the Casino Welcome Bonus, 188% up to €2,088 plus 18 free spins, minimum first deposit €50) and say that its terms are on the bonus page.",
            refs_add=["brandinfo_welcome.welcome_bonus.name", "brandinfo_welcome.welcome_bonus.bonus_percentage", "brandinfo_welcome.welcome_bonus.maximum_bonus",
                      "brandinfo_welcome.welcome_bonus.free_spins", "brandinfo_welcome.welcome_bonus.minimum_deposit"]),
        blk(["b06"], 2, "Stage 2: Proving Who You Are", 170, kw(k0=1), PL,
            extra="Add the procedure as a numbered list of four steps (without the brand name), the stages at which checks happen and the consequences of failing the checks.",
            refs_add=["brandinfo_account.verification.procedure", "brandinfo_privacy_policy.kyc_aml.verification_requirements.verification_stages",
                      "brandinfo_privacy_policy.kyc_aml.failure_consequences"]),
        blk(["b03"], 2, "Stage 3: Logging In", 90, kw(k0=1, kl=1, k1=1)),
        blk(["b04"], 3, "Recovering a Forgotten Password", 65, kw(k0=1)),
        blk(["b05"], 3, "When Access Fails", 85, kw(k0=1)),
        blk(["b07"], 2, "Protecting the Credentials and the Account", 85, kw(k0=1)),
        blk(["b09"], 2, "Stage 4: The First Payout", 140, kw(k0=1), edit=[B09_BANK], extra="Add the other withdrawal rule of the terms: bank transfers may need another 3-5 business days for settlement, and the operator may ask for KYC documents before processing payments.",
            refs_add=["brandinfo_privacy_policy.terms_conditions.withdrawal_terms[2]", "brandinfo_privacy_policy.terms_conditions.withdrawal_terms[3]"]),
        blk(["b10"], 2, "Using the Account on a Phone", 110, kw(k0=1)),
        terms(2, "Stage 5: Inactivity, Complaints and Changes of the Terms", 90, kw(k0=1)),
        vip(2, "Stage 6: Moving Up the VIP Levels", 90, kw(k0=1)),
        blk(["b12"], 2, "Stage 7: Pausing or Closing the Account", 150, kw(k0=1), PL,
            extra="Add the four steps of the procedure as a numbered list, in the order of the Brand Information, without the e-mail address, and the self-assessment questions.",
            refs_add=["brandinfo_responsible_gaming.responsible_gaming.procedure", "brandinfo_responsible_gaming.responsible_gaming.self_assessment"]),
        blk(["b14"], 2, "Support at Every Stage", 60, kw(k0=1)),
        blk(["b15"], 2, "Account Lifecycle FAQ", 125, kw(k0=1), **faq(["regdet", "login", "forgot", "docs", "payout", "inactive", "close", "support"])),
    ],
})

# Each variant is scaled to the total of its size group (the sum of the block middles must be within 10% of the target of the group; the facts of
# the deepened topics are added through refs_add, the scaling only gives them the room).
FIT = {"v01": 790, "v02": 800, "v03": 790, "v04": 790, "v05": 1230, "v06": 1220, "v07": 1250, "v08": 1240, "v09": 1230, "v10": 1260, "v11": 1520, "v12": 1500}
for v in variants:
    total = sum(b["words"] for b in v["blocks"])
    k = FIT[v["id"]] / total
    for b in v["blocks"]:
        b["words"] = max(35, int(round(b["words"] * k / 5.0)) * 5)

intrinsic = {
    "b14": {"keyword": K0, "count": 1,
            "replace": [['; it contains the tracked keyword "Longfu88", which is the one occurrence this block allows (so do not write the brand name anywhere else in the block).', "."]],
            "note": 'The e-mail address contains the tracked keyword "Longfu88"; it is part of the exact count of this block.'},
}
blueprint = {"base_run": "longfu88-login-sg", "brand_names": ["Longfu88 Register", "Longfu88 Login", "Longfu88 Casino", "Longfu88"], "keyword_labels": {},
             "intrinsic": intrinsic, "variants": variants}
out = Path("input/variants/longfu88-login-sg.json")
out.write_text(json.dumps(blueprint, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(variants), "variants")
