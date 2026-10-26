"""Blueprint of 8 ТЗ variants for the Longfu88 login page (brand-subpage, GEO MY) -> input/variants/longfu88-login-my.json.
Base run: runs/longfu88-login-my (tools/longfu88/make_login_base.py, the OPTIMUM group `medium`). Run from the project root:
    python tools/longfu88/make_login_variants.py
    python -m textgen variants input/variants/longfu88-login-my.json --force

The competitors fall into three size groups (python -m textgen tiers longfu88-login-my --texts 8):
    small  238 / 385 / 524 -> target 382, limit 459     3 variants: v01-v03, the most important blocks, entities and facts cut to the minimum
    medium 844             -> target 844, limit 1013    4 variants: v04-v07, the base ТЗ with another order, merges, headings, formats, facts
    large  1754            -> limit 1754 (x1.0)         1 variant:  v08, the base plus the blocks the big competitor has (settings, currencies and
                                                        accounts, closure, games, mobile, VIP); shorter than the limit where the facts end
Base blocks: b01 intro, b02 registration, b03 login, b04 password reset, b05 login problems, b06 verification, b07 security,
b08 welcome bonus, b09 support, b10 FAQ."""
import json
from pathlib import Path

K0, K1, K2, K3 = "Longfu88", "Longfu login", "Longfu88 register", "Longfu88 casino login"

# exact pieces of the base notes (tools/longfu88/make_login_base.py) that a variant changes
B01_TOPICS = "(login, password reset, registration, verification, security, support)"
B02_LIST = ("then a NUMBERED list with the three login steps in the order of the Brand Information (select Login on the website; enter the registered "
            "e-mail and password; complete any security check and access the account)")
B02_PROSE = ("then one short paragraph that walks through the three login steps in the order of the Brand Information (select Login on the website; "
             "enter the registered e-mail and password; complete any security check and access the account)")
B02_NEXT = "Do not explain password reset here (next sub-section)."
B02_NEXT_SEPARATE = "Do not explain password reset here (a separate section)."
B03_LIST = "One lead-in sentence, then a NUMBERED list with the three recovery steps in the order of the Brand Information"
B03_PROSE = "One short paragraph with the three recovery steps in the order of the Brand Information"
B04_NO_BONUS = "Do not describe bonuses or deposits here."
B05_TABLE = "Then a TABLE with two columns, document type | accepted documents, one row each for identity"
B05_LIST = "Then a bulleted list, one item each for identity"
B05_ROW = "; the source-of-funds row applies only when requested"
B05_ITEM = "; the source-of-funds item applies only when requested"

# the small texts keep of the verification only the documents and the review time (the triggers and the 30 days are cut)
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
    "verif": ("how long verification takes (a complete document set is normally reviewed within up to 10 days)",
              ["brandinfo_account.verification.typical_review_time"]),
    "docs": ("which identity document is accepted (passport, national identity card or driving licence)",
             ["brandinfo_privacy_policy.kyc_aml.required_documents.identity"]),
    "age": ("what the minimum age is (18, and the player must be legally permitted to gamble where they live)", ["brandinfo_general.minimum_age"]),
    "support": ("where to turn when the login still fails (customer support: live chat 24/7 or e-mail; do not print the e-mail address)",
                ["brandinfo_general.customer_support.channels"]),
    "oneacc": ("whether a player may hold more than one account (no: one personal account per player)", ["brandinfo_account.registration.eligibility[1]"]),
    "regdet": ("which details registration asks for (e-mail, password, legal name, date of birth, residential address)",
               ["brandinfo_account.registration.required_details"]),
    "mobile": ("whether a player can log in from a phone (yes, in the browser of a smartphone or tablet; a home-screen shortcut is possible)",
               ["brandinfo_app.app_information.platforms"]),
    "bonus": ("when the welcome bonus can be claimed (after registration, on the first qualifying deposit of at least €50)",
              ["brandinfo_welcome.welcome_bonus.minimum_deposit"]),
    "lang": ("which languages support speaks (English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese)",
             ["brandinfo_general.customer_support.languages"]),
    "vip": ("whether there is a VIP programme (yes, with five tiers: Bronze, Silver, Gold, Platinum and Diamond)", ["brandinfo_loyalty.loyalty_vip_program.tiers"]),
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


def intro(heading, words, topics):
    return blk(["b01"], 1, heading, words, {K0: 1}, edit=[(B01_TOPICS, topics)])


def new(level, heading, words, refs, ents, conns, summary, notes, covers, fmt=None, kw=None):
    """A block that the base ТЗ does not have (the large text adds the sections of the big competitor): its facts come from `refs` only."""
    return blk([], level, heading, words, kw or {}, fmt, summary=summary, entities=ents, connections=conns, kb_refs=refs, notes=notes, covers_clusters=covers)


PL = ["paragraph", "list"]
SKIP_SECURITY = {"id": "k06", "reason": "left out of the short text; the player's duty to keep the credentials is one clause of another block"}
DEPOSITS = {"id": "k11", "reason": "Deposits and payment methods belong to the payments page of the site."}
VOICE_TAIL = (" All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Malaysia.")
variants = []

# ================================================================ SMALL (target 382, limit 459): the most important blocks only
variants.append({
    "id": "v01", "name": "Quick steps (small, flat)", "tier": "small", "angle": "A returning player who wants to get in within a minute.",
    "intent_summary": ("Short brand-subpage for the small size group of the competitors: logging in to the Longfu88 account for players from Malaysia in the fewest words: the login steps "
                       "with the password reset, registration for those without an account, the documents with the account security, support and a very short FAQ. Page voice: short, dense "
                       "paragraphs of two sentences, sentences of about 14 words, imperative where a step is described, no scene-setting, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login: Sign In Step by Step", 40, "(login steps, password reset, registration, verification and security, support)"),
        blk(["b03", "b04"], 2, "Log In and Reset a Forgotten Password", 90, {K0: 1, K1: 1}, PL, [(B02_NEXT, ""), (B03_LIST, B03_PROSE)],
            "The three login steps as a numbered list, then the password reset in one short paragraph.",
            summary="The three login steps in order, followed by the password reset through the e-mailed link."),
        blk(["b02"], 2, "Longfu88 Register: Open an Account", 70, {}, PL),
        blk(["b06", "b07"], 2, "Verification Documents and Account Security", 70, {}, ["paragraph", "table"],
            summary="Which documents the casino may ask for and who protects the account.",
            notes=VER_SMALL_TABLE + " Close the block with one sentence: the account holder is responsible for safeguarding the login credentials, and technical and organisational "
                  "safeguards protect accounts, payments and personal information. No certificate, encryption or two-factor claims.",
            refs_drop=VER_SMALL_DROP + ["brandinfo_privacy_policy.terms_conditions.account_terms"],
            refs_add=["brandinfo_privacy_policy.terms_conditions.account_terms[0]"]),
        blk(["b09"], 2, "Get Help", 35, {K0: 1}),
        blk(["b10"], 2, "Login FAQ", 55, {K0: 1}, **faq(["login", "forgot", "verif", "support"])),
    ],
})

variants.append({
    "id": "v02", "name": "Register first (small)", "tier": "small", "angle": "A new player who needs the account first.",
    "skipped_clusters": [SKIP_SECURITY, DEPOSITS],
    "intent_summary": ("Short brand-subpage for the small size group: a newcomer to Longfu88 in Malaysia creates the account, logs in, replaces a lost password and meets the verification "
                       "documents, with support and a short FAQ. Page voice: a patient guide in plain \"first, then\" order, sentences of about 15 words, one plain invitation to register. "
                       "The credentials rule is one clause of the login block. Flat H2s with one H3." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Login and Account Guide for Malaysia", 40, "(registration, login, password reset, documents, support)"),
        blk(["b02"], 2, "Open the Account First", 75, {K2: 1}, PL, extra="One plain invitation to register is allowed here."),
        blk(["b03"], 2, "Then Log In", 55, {K1: 1}, extra="Add one clause: the account holder is responsible for safeguarding the login credentials.",
            refs_add=["brandinfo_privacy_policy.terms_conditions.account_terms"]),
        blk(["b04"], 3, "Lost Password", 45),
        blk(["b06"], 2, "Documents the Casino May Ask For", 60, {}, notes=VER_SMALL_TABLE, refs_drop=VER_SMALL_DROP),
        blk(["b09"], 2, "Where to Get Help", 35, {K0: 1}),
        blk(["b10"], 2, "Beginner FAQ", 60, {K0: 1, K3: 1}, **faq(["regdet", "login", "forgot", "oneacc", "support"])),
    ],
})

variants.append({
    "id": "v03", "name": "Checklist (small, lists)", "tier": "small", "angle": "A reader who works through a list.",
    "skipped_clusters": [SKIP_SECURITY, DEPOSITS],
    "intent_summary": ("Checklist-style short brand-subpage for the small size group: what to prepare before the first Longfu88 login in Malaysia (registration), which documents to keep ready, "
                       "the login itself, the password reset, contacts and quick answers. Page voice: terse and scannable, a one-sentence lead-in per section, then a list; sentences of about "
                       "12 words; no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login Checklist for Malaysian Players", 40, "(registration, documents, login, password reset, contacts)"),
        blk(["b02"], 2, "Before the First Login: Registration Checklist", 70, {K2: 1}, PL),
        blk(["b06"], 2, "Documents Checklist", 60, {}, PL, notes=VER_SMALL_LIST, refs_drop=VER_SMALL_DROP),
        blk(["b03"], 2, "Login Checklist", 50, {K1: 1}, edit=[(B02_NEXT, B02_NEXT_SEPARATE)], extra="Keep the lead-in to one sentence."),
        blk(["b04"], 2, "If the Password Is Lost", 45),
        blk(["b09"], 2, "Contacts", 30, {K0: 1}),
        blk(["b10"], 2, "Quick Answers", 55, {K0: 1}, **faq(["login", "docs", "verif", "support"])),
    ],
})

# ================================================================ MEDIUM (target 844, limit 1013): the base ТЗ, differently arranged
variants.append({
    "id": "v04", "name": "Newcomer walkthrough (register first, nested)", "tier": "medium", "angle": "A new player who has no account yet and wants one guided path.",
    "intent_summary": ("Step-by-step brand-subpage for a newcomer to Longfu88 in Malaysia: the account is created (with the welcome offer named as the reason to register), then the player logs in, "
                       "learns what to do when the password or the login fails, passes the verification and keeps the account safe. Page voice: a patient guide, \"first, then\" logic, one "
                       "short explanation of verification the first time it appears, sentences of about 17 words, one plain invitation to register. Steps are H2s, their details H3s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login: A Guide for New Players", 75, "(registration, login, password reset, verification, security, support)"),
        blk(["b02"], 2, "Step 1: Create Your Account", 115, {K2: 1}, PL, extra="One plain invitation to register is allowed here."),
        blk(["b08"], 3, "What a New Account Can Claim", 65),
        blk(["b03"], 2, "Step 2: Log In", 70, {K1: 1}),
        blk(["b04"], 3, "If You Forget the Password", 55),
        blk(["b05"], 3, "When the Login Does Not Work", 55),
        blk(["b06"], 2, "Step 3: Verify the Account", 110, extra="Explain in one clause what verification is the first time the word appears."),
        blk(["b07"], 2, "Keeping the Account Safe", 70),
        blk(["b09"], 2, "Help With Your Account", 50, {K0: 1}),
        blk(["b10"], 2, "Beginner Questions", 100, {K0: 1, K3: 1}, **faq(["regdet", "login", "forgot", "oneacc", "bonus", "support"])),
    ],
})

variants.append({
    "id": "v05", "name": "Troubleshooting-led", "tier": "medium", "angle": "A player who already has an account and cannot get in.",
    "intent_summary": ("Troubleshooting-led brand-subpage about the Longfu88 login in Malaysia for a player who is locked out or unsure: the normal route, why a login fails, the password reset, the "
                       "checks that can hold an account, how the data is protected, registration for those who have no account with the welcome offer, and support. Page voice: practical and "
                       "calm, cause then fix, sentences of about 16 words, a short consequence after each limit; no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Login Help: Sign In and Fix Access Problems", 70, "(the normal login route, reasons for a failed login, password reset, verification, security, registration, support)"),
        blk(["b03"], 2, "The Normal Login Route", 65, {K1: 1}, edit=[(B02_NEXT, B02_NEXT_SEPARATE)]),
        blk(["b05"], 2, "Why a Login Fails", 80, extra="Add that prolonged inactivity may trigger an account review or closure.",
            refs_add=["brandinfo_privacy_policy.terms_conditions.inactivity"]),
        blk(["b04"], 2, "Reset the Password", 65),
        blk(["b06"], 2, "Checks That Can Hold an Account", 100, {}, PL, [(B05_TABLE, B05_LIST), (B05_ROW, B05_ITEM)]),
        blk(["b07"], 2, "Protecting Your Details", 70),
        blk(["b02"], 2, "No Account Yet? Create One", 100, {K2: 1}, PL),
        blk(["b08"], 2, "A Welcome Offer for New Accounts", 70),
        blk(["b09"], 2, "Contact the Support Team", 50, {K0: 1}),
        blk(["b10"], 2, "Common Login Questions", 100, {K0: 1, K3: 1}, **faq(["login", "forgot", "docs", "verif", "age", "support"])),
    ],
})

variants.append({
    "id": "v06", "name": "Security-conscious", "tier": "medium", "angle": "A cautious player who wants to know what protects the account before logging in.",
    "intent_summary": ("Security-conscious brand-subpage about the Longfu88 login in Malaysia for a cautious reader: how to sign in safely, what protects the account and the data, why the casino asks "
                       "for documents, the registration details, the welcome offer in brief and support. Page voice: sober and exact, every claim tied to a stated fact, sentences of about 18 words "
                       "with a few shorter ones, no reassurance beyond the facts; no calls to action. H2 sections with two H3." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login: Secure Access to Your Account", 70, "(login, password reset, why a login is blocked, account protection, verification documents, registration, support)"),
        blk(["b03"], 2, "Signing In Safely", 70, {K1: 1}),
        blk(["b04"], 3, "Replacing a Lost Password", 55),
        blk(["b05"], 3, "Spotting Why Access Is Blocked", 60),
        blk(["b07"], 2, "What Protects the Account", 100, {}, refs_add=["brandinfo_privacy_policy.privacy_policy.data_sharing", "brandinfo_privacy_policy.privacy_policy.data_subject_rights"],
            extra="Add with whom data may be shared and which rights the player has, as short lists inside the paragraph."),
        blk(["b06"], 2, "Why the Casino Asks for Documents", 115),
        blk(["b02"], 2, "Registration Details and Eligibility", 105, {K2: 1}, PL),
        blk(["b08"], 2, "The Welcome Offer in Brief", 70),
        blk(["b09"], 2, "Who to Contact", 50, {K0: 1}),
        blk(["b10"], 2, "Account Safety Questions", 85, {K0: 1, K3: 1}, **faq(["login", "verif", "docs", "oneacc", "support"])),
    ],
})

variants.append({
    "id": "v07", "name": "Mobile-first", "tier": "medium", "angle": "A player who mostly uses a phone.",
    "intent_summary": ("Mobile-first brand-subpage about the Longfu88 login in Malaysia: logging in from a phone, a tablet or a computer with the home-screen shortcut, the password reset, creating an "
                       "account on a phone, the documents to keep ready, account safety, what to do when the phone login fails, the welcome offer, a mobile FAQ and support. Page voice: brisk and "
                       "concrete, device words in every section (phone, browser, shortcut), sentences of about 15 words; no calls to action. Flat H2s with one H3. There is no downloadable app in the facts." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Casino Login on Mobile and Desktop", 70, "(login on a phone or a computer, password reset, registration, documents, account safety, support)"),
        blk(["b03"], 2, "Log In from Any Device", 115, {K1: 1}, PL, [(B02_LIST, B02_PROSE)],
            "The login steps in one short paragraph, then a bulleted list with two items: the home-screen shortcut on Android (Chrome) and on iOS (Safari), as in the Brand Information. "
            "The casino works in the browser of a phone or a tablet; it is not a downloadable app, so no APK files and no app stores. Write \"the site\" in the steps instead of the brand name.",
            refs_add=["brandinfo_app.app_information.platforms", "brandinfo_app.app_information.android_installation", "brandinfo_app.app_information.ios_installation"],
            summary="How to log in on a computer or a phone and how to add a home-screen shortcut on Android and iOS."),
        blk(["b04"], 3, "Password Reset on a Phone", 55),
        blk(["b02"], 2, "Create an Account from Your Phone", 105, {K2: 1}, PL),
        blk(["b06"], 2, "Documents to Keep Ready", 105, {}, PL, [(B05_TABLE, B05_LIST), (B05_ROW, B05_ITEM)]),
        blk(["b07"], 2, "Account Safety on a Phone", 70),
        blk(["b05"], 2, "When the Phone Login Fails", 65),
        blk(["b08"], 2, "Welcome Offer on Mobile", 70),
        blk(["b10"], 2, "Mobile Login FAQ", 85, {K0: 1}, **faq(["mobile", "login", "forgot", "support", "lang"])),
        blk(["b09"], 2, "Support on Chat or E-mail", 50, {K0: 1}),
    ],
})

# ================================================================ LARGE (limit 1754 = the mean of the group): the base plus the sections of the big competitor
variants.append({
    "id": "v08", "name": "Full account handbook (large)", "tier": "large", "angle": "A reader who wants the whole account topic on one page.",
    "intent_summary": ("Complete brand-subpage for the large size group of the competitors, built like the longest login page of the query: a handbook of the Longfu88 account for players from Malaysia "
                       "with access (login, lost password, failed logins), entry (registration and the welcome offer), compliance (verification documents and procedure), protection (credentials and data), "
                       "settings and communication, currencies and the one-account rule, taking a break or closing the account, what opens after the login, mobile access, the VIP programme, support and a FAQ. "
                       "Page voice: reference-like, each H2 opens with what the section is for, sentences of about 18 words, a consequence after each condition; one plain invitation to register. "
                       "Every extra section is written only from the facts of its Brand Information; where a section has few facts it stays short. H2 sections with H3 details." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Account Handbook for Malaysian Players", 90, "(access, entry, compliance, protection, settings, taking a break, mobile access, the VIP programme, support)"),
        blk(["b02"], 2, "Entry: Opening an Account", 130, {K2: 1}, PL, extra="One plain invitation to register is allowed here."),
        blk(["b08"], 3, "The Welcome Offer in Brief", 80),
        blk(["b03"], 2, "Access: The Login Route", 90, {K1: 1}),
        blk(["b04"], 3, "Recovering a Lost Password", 65),
        blk(["b05"], 3, "Diagnosing Failed Logins", 80),
        blk(["b07"], 2, "Protection: Credentials and Data", 100, {}, refs_add=["brandinfo_privacy_policy.privacy_policy.data_sharing", "brandinfo_privacy_policy.privacy_policy.data_subject_rights"],
            extra="Add with whom data may be shared and which rights the player has, as short lists inside the paragraph."),
        blk(["b06"], 2, "Compliance: Verification Documents", 130, {}, extra="After the table give the procedure in one sentence (upload legible, current documents that match the account profile; "
            "telephone or face verification if requested; wait for approval before a withdrawal).", refs_add=["brandinfo_account.verification.procedure"]),
        new(2, "Settings: Communication Preferences and Cookies", 50,
            ["brandinfo_privacy_policy.privacy_policy.marketing", "brandinfo_privacy_policy.privacy_policy.cookies"],
            [["Communication Preferences", 10], ["Cookies", 6]], [["Player", "manages", "direct-marketing preferences and can unsubscribe from promotional communications", 8]],
            "Which settings the player controls: promotional communication and the cookies of the site.",
            "Two facts only, exactly as in the Brand Information: the player may manage direct-marketing preferences and unsubscribe from promotional communications; necessary, preference, "
            "analytics and marketing cookies support website functions and measurement. Do not invent account settings, screens, limits (deposit, loss, session) or profile fields and do not say "
            "where in the account to find these settings. Neutral tone.", ["k12"]),
        new(2, "Currencies and the One-Account Rule", 55,
            ["brandinfo_general.currencies", "brandinfo_privacy_policy.terms_conditions.eligibility.player_requirements"],
            [["Account Currencies", 8], ["One Personal Account", 8]], [["Player", "uses", "one personal account in one of the supported currencies", 8]],
            "Which currencies an account can use and the rules for the account itself: accurate details, one personal account, no third-party payment methods.",
            "State the currencies exactly as listed (EUR, USD, MYR, THB, SGD and USDT) and do not convert amounts or mention exchange rates, conversion or a choice of currency at registration: "
            "none is given. The player requirements: register with accurate information, use only one personal account, do not use third-party payment methods. Calm tone, no legal advice. "
            "Do not say or imply that the casino is licensed, legal or approved in Malaysia.", ["k13"]),
        new(2, "Taking a Break or Closing the Account", 100,
            ["brandinfo_responsible_gaming.responsible_gaming.policy", "brandinfo_responsible_gaming.responsible_gaming.self_exclusion.effect",
             "brandinfo_responsible_gaming.responsible_gaming.account_closure", "brandinfo_responsible_gaming.responsible_gaming.self_assessment",
             "brandinfo_responsible_gaming.responsible_gaming.support_organizations", "brandinfo_responsible_gaming.responsible_gaming.procedure"],
            [["Self-Exclusion", 10], ["Account Closure", 8], ["Support Organisations", 5]], [["Player", "requests", "self-exclusion or account closure through customer support", 8]],
            "How a player limits or ends access: self-exclusion, account closure through support, self-assessment questions and independent help organisations.",
            "Players must be at least 18 and gamble only where lawful. A player who wants to stop contacts support and asks for self-exclusion or account closure; account access and gambling may "
            "then be restricted for the agreed period. Self-assessment questions help to recognise possible harm. Independent support: GamCare, Gamblers Anonymous and Gambling Therapy. "
            "Do not print the e-mail address of the self-exclusion request (it contains the brand name) and do not state a processing time. Accurate and practical, not moralising.", ["k14"]),
        new(2, "What Opens After the Login", 55,
            ["brandinfo_games.game_types", "brandinfo_app.app_information.features"],
            [["Casino", 9], ["Sportsbook", 8]], [["Player Account", "gives access to", "the casino, the sportsbook, deposits, withdrawals and bonuses", 8]],
            "What a player reaches after logging in: the casino games, the sportsbook, the cashier and the bonuses.",
            "One lead-in sentence that names what the account gives access to (casino, sportsbook, account access, deposits, withdrawals, bonuses), then a bulleted list of the game categories "
            "exactly as in the Brand Information (slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, crash and instant games). No game names, providers "
            "or RTP values. Keep it short: this is a pointer to the rest of the site.", ["k16"], PL),
        new(2, "Mobile and Tablet Access", 80,
            ["brandinfo_app.app_information.platforms", "brandinfo_app.app_information.android_installation", "brandinfo_app.app_information.ios_installation"],
            [["Mobile Web", 10], ["Home Screen Shortcut", 8]], [["Player", "adds", "a shortcut of the website to the home screen", 8]],
            "Logging in from a phone or a tablet in the browser and adding a home-screen shortcut on Android (Chrome) and iOS (Safari).",
            "The casino works in the browser of a smartphone or a tablet; the Brand Information has no download from an app store: do not call it a downloadable app and do not mention APK files or "
            "app stores. A short paragraph, then a bulleted list with two items: Android (open the site in Chrome, open the browser menu and choose Add to Home screen, confirm the shortcut) and "
            "iOS (open the site in Safari, tap Share and choose Add to Home Screen, confirm Add). The login on a phone is the same as on a computer. Write \"the site\" in the steps instead of the brand name.",
            ["k15"], PL),
        new(2, "VIP Levels and Rewards", 85,
            ["brandinfo_loyalty.loyalty_vip_program.tiers", "brandinfo_loyalty.loyalty_vip_program.progression", "brandinfo_loyalty.loyalty_vip_program.additional_benefits",
             "brandinfo_loyalty.loyalty_vip_program.important_terms"],
            [["VIP Programme", 10], ["VIP Points", 7], ["Tiers", 6]], [["Player", "earns", "VIP points through eligible real-money gameplay, which unlock reward levels", 8]],
            "What a logged-in player gets from the VIP programme: five tiers, points from real-money play, the extra benefits and the terms.",
            "Five tiers: Bronze, Silver, Gold, Platinum and Diamond. Points are earned through eligible real-money gameplay and unlock numbered reward levels. Additional benefits: personalised offers, "
            "VIP cashback, higher withdrawal limits and a personal VIP manager for eligible high tiers. Terms: reward and withdrawal limits may differ by VIP level and currency, and level-based benefits "
            "and eligibility may change under the programme rules. Do not give level numbers, point thresholds, rewards or limits (they are on the VIP page) and do not use the official name of the "
            "programme (it contains the brand name).", ["k17"]),
        blk(["b09"], 2, "Assistance and Contact Channels", 55, {K0: 1}),
        blk(["b10"], 2, "Handbook FAQ", 120, {K0: 1, K3: 1}, **faq(["login", "forgot", "method", "regdet", "docs", "verif", "oneacc", "vip"])),
    ],
})

intrinsic = {
    "b09": {"keyword": K0, "count": 1,
            "replace": [['; it contains the tracked keyword "Longfu88", which is the one occurrence this block allows (so do not write the brand name anywhere else in the block).', "."]],
            "note": 'The e-mail address contains the tracked keyword "Longfu88"; it is part of the exact count of this block.'},
}
blueprint = {"base_run": "longfu88-login-my", "brand_names": ["Longfu88 Register", "Longfu88 Casino", "Longfu88"], "keyword_labels": {},
             "intrinsic": intrinsic, "variants": variants}
out = Path("input/variants/longfu88-login-my.json")
out.write_text(json.dumps(blueprint, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(variants), "variants")
