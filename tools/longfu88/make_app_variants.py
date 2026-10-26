"""Blueprint of 8 ТЗ variants for the Longfu88 app page (brand-subpage, GEO MY) -> input/variants/longfu88-app-my.json.
Base run: runs/longfu88-app-my (tools/longfu88/make_app_base.py, the OPTIMUM group `medium`). Run from the project root:
    python tools/longfu88/make_app_variants.py
    python -m textgen variants input/variants/longfu88-app-my.json --force

The competitors fall into three size groups (python -m textgen tiers longfu88-app-my --texts 8):
    small  759       -> target 759,  limit 911      3 variants: v01-v03, the most important blocks, entities and facts cut to the minimum
    medium 975 / 983 -> target 979,  limit 1175     4 variants: v04-v07, the base ТЗ with another order, headings, formats, facts
    large  1372      -> limit 1372 (x1.0)           1 variant:  v08, the base plus the sections of the big competitor (games, sports, paying
                                                    from a phone, the welcome offer); shorter than the limit where the facts end
The sum of the words_max of a text must stay within its limit, so the middles below are chosen with that in mind.
Base blocks: b01 intro, b02 what works on a phone, b03 install lead, b04 Android steps, b05 iOS steps, b06 devices and browsers,
b07 shortcut or browser tab, b08 account access, b09 security, b10 troubleshooting, b11 support, b12 FAQ.
The knowledge base has no native app (home-screen shortcut only), so every block repeats the NO_APP_CLAIMS rule of the base notes."""
import json
from pathlib import Path

K0, KA, KI, KD, KAPK, KDL, KM = ("Longfu88", "Longfu app", "Longfu88 iOS", "Longfu88 Android", "Longfu88 apk", "Longfu88 download", "Longfu88 mobile casino")

# exact pieces of the base notes (tools/longfu88/make_app_base.py) that a variant changes
B01_TOPICS = "(features, home-screen shortcut for Android and iOS, supported devices, account access, security, troubleshooting, support)"
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
VOICE_TAIL = " All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Malaysia."

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
}
BASE_FAQ_REFS = ["brandinfo_app.app_information.platforms", "brandinfo_app.app_information.mobile_access", "brandinfo_account.login.method",
                 "brandinfo_general.minimum_age", "brandinfo_general.customer_support.channels"]


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


def intro(heading, words, kw, topics):
    return blk(["b01"], 1, heading, words, kw, edit=[(B01_TOPICS, topics)])


def new(level, heading, words, refs, ents, conns, summary, notes, covers, fmt=None, kw=None):
    """A block that the base ТЗ does not have (the large text adds the sections of the big competitor): its facts come from `refs` only."""
    return blk([], level, heading, words, kw or {}, fmt, summary=summary, entities=ents, connections=conns, kb_refs=refs, notes=notes, covers_clusters=covers)


PL = ["paragraph", "list"]
SKIP_TAB = {"id": "k07", "reason": "left out of the short text; the difference between the shortcut and a browser tab is one clause of another block"}
SKIP_SECURITY = {"id": "k06", "reason": "left out of the short text; the player's duty to keep the credentials is one clause of the account access block"}

INSTALL_FLAT_HEAD = ("Three parts in ONE continuous section without sub-headings, in this order. (1) Two or three sentences: the casino works in the browser of a smartphone or tablet and a "
                     "home-screen shortcut is added once; one sentence says that nobody needs an installation file or an APK because the casino opens in the mobile browser and is added to the "
                     "home screen as a shortcut (no file and no store listing); where the phrase \"Longfu88 apk\" is used it stands in that sentence. ")
INSTALL_FLAT_LISTS = ("(2) Android: one lead-in sentence, then a NUMBERED list with the three steps in the order of the Brand Information (open the casino website in Chrome; open the browser "
                      "menu and choose Add to Home screen; confirm the shortcut). (3) iOS: one lead-in sentence, then a NUMBERED list with the three steps in the order of the Brand "
                      "Information (open the casino website in Safari; tap Share and choose Add to Home Screen; confirm Add). The tracked keywords belong to the sentences before the lists; write "
                      "\"the site\" or \"the casino website\" in the steps instead of the brand name. Do not give a download link, file size or version number. ")

variants = []

# ================================================================ SMALL (target 759, limit 911): the most important blocks only
variants.append({
    "id": "v01", "name": "Quick shortcut guide (small, flat)", "tier": "small", "angle": "A player who wants the shortcut on the phone within a minute.",
    "skipped_clusters": [SKIP_TAB],
    "intent_summary": ("Short brand-subpage for the small size group of the competitors: putting the Longfu88 casino on the home screen of a phone in Malaysia in the fewest words: the "
                       "shortcut steps for Android and iOS, what works on mobile, devices, account access, fixes, safety, support and a very short FAQ. Page voice: short, dense paragraphs of "
                       "two sentences, sentences of about 14 words, imperative where a step is described, no scene-setting, no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Mobile Casino: Quick Phone Guide for Malaysia", 55, {K0: 2, KA: 1}, "(shortcut steps for Android and iOS, features, devices, account access, fixes, safety, support)"),
        blk(["b03", "b04", "b05"], 2, "Longfu88 Download: Android and iOS Shortcut Steps", 170, {KD: 1, KI: 1, KAPK: 1}, PL,
            notes=INSTALL_FLAT_HEAD + INSTALL_FLAT_LISTS + NO_APP_CLAIMS,
            summary="Why no file is needed and the shortcut steps for Android in Chrome and iOS in Safari."),
        blk(["b02"], 2, "What Works on Mobile", 85, {K0: 1}),
        blk(["b06"], 2, "Phones and Browsers", 60, {K0: 1}),
        blk(["b08"], 2, "Logging In from a Phone", 70, {K0: 1}),
        blk(["b09"], 2, "Staying Safe", 55, {K0: 1}),
        blk(["b10"], 2, "If Something Fails", 75, {K0: 1}),
        blk(["b11"], 2, "Where to Get Help", 50, {K0: 1}),
        blk(["b12"], 2, "Quick Answers", 90, {K0: 1}, **faq(["app", "phones", "android", "login", "support"])),
    ],
})

variants.append({
    "id": "v02", "name": "Android first (small)", "tier": "small", "angle": "A player on an Android phone who wants the Chrome steps first.",
    "skipped_clusters": [SKIP_SECURITY],
    "intent_summary": ("Short brand-subpage for the small size group: a player with an Android phone in Malaysia adds the Longfu88 casino to the home screen in Chrome, and an iPhone or iPad "
                       "user finds the Safari steps right below; then what works on mobile, the choice between the shortcut and a browser tab, devices, account access, fixes, support and a short FAQ. "
                       "Page voice: a practical guide in plain \"first, then\" order, sentences of about 15 words, one plain recommendation. Flat H2s with one H3." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Android Casino: Add It to Your Phone in Chrome", 55, {K0: 1, KA: 1}, "(Android and iOS shortcut steps, features, shortcut or browser tab, devices, account access, fixes, support)"),
        blk(["b03", "b04"], 2, "Add the Casino to the Android Home Screen", 115, {KDL: 1, KAPK: 1, K0: 1}, PL,
            notes=("Two parts in ONE continuous section without sub-headings. (1) Two or three sentences: the casino works in the browser of a smartphone or tablet; one sentence says that "
                   "nobody needs an installation file or an APK because the casino opens in the mobile browser and is added to the home screen as a shortcut (no file and no store listing); "
                   "where the phrases \"Longfu88 download\" and \"Longfu88 apk\" are used they stand in these sentences. (2) Android: one lead-in sentence, then a NUMBERED list with the three steps in "
                   "the order of the Brand Information (open the casino website in Chrome; open the browser menu and choose Add to Home screen; confirm the shortcut). Write \"the site\" or "
                   "\"the casino website\" in the steps instead of the brand name; tracked keywords belong to the sentences before the list. Do not give a download link, file size or version "
                   "number. " + NO_APP_CLAIMS),
            summary="Why no file is needed and the three Android steps in Chrome."),
        blk(["b05"], 3, "Longfu88 iOS: Safari Steps for iPhone and iPad", 55, {}),
        blk(["b02"], 2, "What the Longfu88 Mobile Casino Offers", 80, {K0: 1}),
        blk(["b07"], 2, "Shortcut or Browser Tab", 70, {K0: 1}),
        blk(["b06"], 2, "Compatible Devices", 55, {K0: 1}),
        blk(["b08"], 2, "Account Access on Your Phone", 65, {K0: 1}),
        blk(["b10"], 2, "Fixes for Common Phone Problems", 65, {K0: 1}),
        blk(["b11"], 2, "Contact Support", 45, {K0: 1}),
        blk(["b12"], 2, "Android and iOS Questions", 85, {K0: 1}, **faq(["app", "android", "ios", "tab", "support"])),
    ],
})

variants.append({
    "id": "v03", "name": "Checklist (small, lists)", "tier": "small", "angle": "A reader who works through a list.",
    "skipped_clusters": [SKIP_TAB],
    "intent_summary": ("Checklist-style short brand-subpage for the small size group: what to check on the phone before adding the Longfu88 casino to the home screen in Malaysia (device and browser), "
                       "the shortcut steps for iOS and Android, what the mobile site gives access to, the login, fixes, safety and contacts. Page voice: terse and scannable, a one-sentence lead-in per "
                       "section, then a list; sentences of about 12 words; no calls to action. Flat H2s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu App Checklist: Phone Setup for Malaysian Players", 50, {K0: 1, KM: 1}, "(device check, shortcut steps for iOS and Android, features, login, fixes, safety, contacts)"),
        blk(["b06"], 2, "Before You Start: Device Checklist", 55, {K0: 1}, PL, edit=[("Lead with the three platforms exactly as given", "Lead-in of one sentence, then a bulleted list with the three platforms exactly as given")]),
        blk(["b03", "b04", "b05"], 2, "Longfu88 iOS and Android Shortcut Checklist", 160, {KD: 1, KDL: 1, KAPK: 1}, PL,
            notes=INSTALL_FLAT_HEAD + INSTALL_FLAT_LISTS + "Put the iOS list before the Android list. " + NO_APP_CLAIMS,
            summary="Why no file is needed and the shortcut steps for iOS in Safari and Android in Chrome."),
        blk(["b02"], 2, "Mobile Features Checklist", 80, {K0: 1}),
        blk(["b08"], 2, "Login Checklist", 65, {K0: 1}, PL, edit=[("Name the steps in one flowing paragraph, not a list.", "A lead-in sentence, then a bulleted list of the steps.")]),
        blk(["b10"], 2, "Troubleshooting Checklist", 85, {K0: 1}),
        blk(["b09"], 2, "Safety Checklist", 55, {K0: 1}),
        blk(["b11"], 2, "Support Contacts", 40, {K0: 1}),
        blk(["b12"], 2, "Checklist Questions", 85, {K0: 1}, **faq(["phones", "ios", "android", "tablet", "support"])),
    ],
})

# ================================================================ MEDIUM (target 979, limit 1175): the base ТЗ, differently arranged
variants.append({
    "id": "v04", "name": "Newcomer walkthrough (steps, nested)", "tier": "medium", "angle": "A new player who has not used the casino on a phone and wants one guided path.",
    "intent_summary": ("Step-by-step brand-subpage for a newcomer to the Longfu88 mobile casino in Malaysia: what the mobile site offers, how to put it on the home screen (Android and iOS), whether the "
                       "phone and the browser fit, how to sign in, whether to keep the shortcut or the browser tab, how the account stays safe, what to do when something fails and where to get help. "
                       "Page voice: a patient guide, \"first, then\" logic, sentences of about 17 words, one plain invitation to start. Steps are H2s, the two platforms are H3s." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Mobile Casino: A First-Time Guide for Phone Users", 70, {K0: 2, KA: 1}, "(what the mobile site offers, shortcut steps for Android and iOS, devices, sign-in, safety, fixes, support)"),
        blk(["b02"], 2, "Step 1: See What the Mobile Site Offers", 100, {K0: 1}),
        blk(["b03"], 2, "Step 2: Longfu88 Download Without a File", 70, {KAPK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Steps in Chrome", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Steps for iPhone and iPad", 55, {}),
        blk(["b06"], 2, "Step 3: Check Your Phone and Browser", 75, {K0: 1}),
        blk(["b08"], 2, "Step 4: Sign In from the Phone", 85, {K0: 1}),
        blk(["b07"], 2, "Shortcut or Browser Tab: Which to Keep", 90, {K0: 2}),
        blk(["b09"], 2, "Keeping the Account Safe on a Phone", 80, {K0: 1}),
        blk(["b10"], 2, "When Something Does Not Work", 80, {K0: 1}),
        blk(["b11"], 2, "Help for Phone Players", 55, {K0: 1}),
        blk(["b12"], 2, "First-Time Phone Questions", 105, {K0: 2}, **faq(["app", "phones", "android", "ios", "login", "support"])),
    ],
})

variants.append({
    "id": "v05", "name": "Decision-led: app or mobile site", "tier": "medium", "angle": "A player who is deciding between an app and the mobile site.",
    "intent_summary": ("Decision-led brand-subpage about the Longfu88 mobile casino in Malaysia for a player who expects an app and wants to know what is offered instead: the shortcut versus the "
                       "browser tab, which phones and browsers work, the shortcut steps for Android and iOS, what the mobile site gives access to, sign-in, fixes, account protection and support. "
                       "Page voice: calm and comparative, the choice first and the steps after it, sentences of about 16 words, a short consequence after each point; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu App or Mobile Site? Using Longfu88 on a Phone", 70, {K0: 1, KM: 1}, "(shortcut or browser tab, devices, shortcut steps for Android and iOS, features, sign-in, fixes, protection, support)"),
        blk(["b07"], 2, "Shortcut or Browser Tab: Pick Your Route", 100, {K0: 2}),
        blk(["b06"], 2, "Which Phones and Browsers Work", 70, {K0: 1}, ["paragraph", "table"],
            notes=("One lead-in sentence that says that the layout adapts to smartphone and tablet screens, then a TABLE with three columns, platform | browser | how it opens, and three rows "
                   "as given in the Brand Information: Android | Chrome | Add to Home screen from the browser menu; iOS | Safari | Add to Home Screen from the Share menu; mobile web | the browser "
                   "of a smartphone or tablet | the responsive website opens directly. Do not state OS versions, device models, storage, memory or connection speed: none are given. " + NO_APP_CLAIMS)),
        blk(["b03"], 2, "Add the Shortcut Once: Longfu88 Download Is Not Needed", 75, {KAPK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari", 55, {}),
        blk(["b02"], 2, "Features Available on Mobile", 90, {K0: 1}, ["paragraph"], edit=[(B02_LIST, B02_PROSE)]),
        blk(["b08"], 2, "Sign In from a Phone", 80, {K0: 1}),
        blk(["b10"], 2, "Fixing Phone Problems Before Contacting Support", 80, {K0: 1}),
        blk(["b09"], 2, "Protecting the Account on a Phone", 75, {K0: 1}),
        blk(["b11"], 2, "Contact Support from the Phone", 55, {K0: 1}),
        blk(["b12"], 2, "Route and Setup FAQ", 100, {K0: 2}, **faq(["app", "tab", "phones", "tablet", "ios", "support"])),
    ],
})

variants.append({
    "id": "v06", "name": "Security-conscious", "tier": "medium", "angle": "A cautious player who wants to know what protects the account before using a phone.",
    "intent_summary": ("Security-conscious brand-subpage about the Longfu88 mobile casino in Malaysia for a cautious reader: how the account is protected on a phone, how to sign in safely, why the casino "
                       "needs no installation file and how the shortcut is added on Android and iOS, the choice between the shortcut and a browser tab, devices, fixes, what the mobile site gives "
                       "access to and support. Page voice: sober and exact, every claim tied to a stated fact, sentences of about 18 words with a few shorter ones, no reassurance beyond the "
                       "facts; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 on Android and iOS: Safe Mobile Casino Access", 70, {K0: 1, KA: 1, KM: 1}, "(account protection, safe sign-in, the shortcut instead of a file, devices, fixes, features, support)"),
        blk(["b09"], 2, "How the Account Stays Protected on a Phone", 90, {K0: 1}),
        blk(["b08"], 2, "Signing In Safely from a Phone", 80, {K0: 1}),
        blk(["b03"], 2, "Longfu88 Download: A Shortcut Instead of a File", 70, {KAPK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome Shortcut", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari Shortcut", 55, {}),
        blk(["b07"], 2, "Shortcut Versus Browser Tab", 80, {K0: 1}),
        blk(["b06"], 2, "Devices and Browsers", 65, {K0: 1}),
        blk(["b10"], 2, "Problems and Quick Fixes", 80, {K0: 1}),
        blk(["b02"], 2, "What the Mobile Site Gives Access To", 85, {K0: 1}),
        blk(["b11"], 2, "Reaching Support", 55, {K0: 1}),
        blk(["b12"], 2, "Mobile Safety FAQ", 105, {K0: 2}, **faq(["app", "login", "age", "ios", "android", "support"])),
    ],
})

variants.append({
    "id": "v07", "name": "Troubleshooting-led", "tier": "medium", "angle": "A player who already tried and cannot get the casino working on a phone.",
    "intent_summary": ("Troubleshooting-led brand-subpage about the Longfu88 mobile casino in Malaysia for a player whose phone setup did not work: the quick fixes first, then how to add the shortcut "
                       "again on Android and iOS, sign-in trouble, device and browser checks, the switch between the shortcut and a browser tab, account safety, what should work on mobile and "
                       "when to contact support. Page voice: practical and calm, cause then fix, sentences of about 16 words; no calls to action." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Mobile Casino Help: Set It Up and Fix Issues", 65, {K0: 1, KA: 1}, "(quick fixes, adding the shortcut again on Android and iOS, sign-in trouble, device checks, safety, support)"),
        blk(["b10"], 2, "Quick Fixes for Common Phone Problems", 90, {K0: 1}, ["paragraph", "table"],
            notes=("One lead-in sentence, then a TABLE with two columns, problem | fix, and four rows in this order: the shortcut does not appear | repeat the steps in Chrome on Android or in Safari "
                   "on iOS; the page does not load | reload it and check the internet connection; the login fails | check the e-mail address and use Forgot Password on the login screen; "
                   "the problem remains | contact support through live chat, 24/7, or by e-mail (do not print the e-mail address here). General wording only, no error codes and no "
                   "browser-setting instructions presented as casino facts. " + NO_APP_CLAIMS)),
        blk(["b03"], 2, "Longfu88 Download Help: Add the Shortcut Again", 70, {KAPK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Add the Shortcut Again in Chrome", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Add the Shortcut Again in Safari", 55, {}),
        blk(["b08"], 2, "Sign-In Trouble on a Phone", 80, {K0: 1}),
        blk(["b06"], 2, "Device and Browser Checks", 65, {K0: 1}),
        blk(["b07"], 2, "Switching Between the Shortcut and a Browser Tab", 80, {K0: 2}),
        blk(["b09"], 2, "Account Security Checks", 75, {K0: 1}),
        blk(["b02"], 2, "What Should Work on Mobile", 80, {K0: 1}),
        blk(["b11"], 2, "When to Contact Support", 60, {K0: 1}),
        blk(["b12"], 2, "Mobile Help FAQ", 105, {K0: 2}, **faq(["app", "features", "phones", "login", "tab", "support"])),
    ],
})

# ================================================================ LARGE (limit 1372 = the mean of the group): the base plus the sections of the big competitor
variants.append({
    "id": "v08", "name": "Complete mobile handbook (large)", "tier": "large", "angle": "A reader who wants everything about the casino on a phone on one page.",
    "intent_summary": ("Complete brand-subpage for the large size group of the competitors, built like the longest app page of the query: a handbook of the Longfu88 mobile casino for players from Malaysia "
                       "with the shortcut instead of a file (Android and iOS), supported devices, the choice between the shortcut and a browser tab, what the mobile site gives access to (casino games, "
                       "sports betting), paying and withdrawing from a phone, the welcome offer, account access, security, troubleshooting, support and a FAQ. Page voice: reference-like, each H2 opens "
                       "with what the section is for, sentences of about 18 words, a consequence after each condition; one plain invitation to start. Every extra section is written only from the "
                       "facts of its Brand Information; where a section has few facts it stays short. H2 sections with H3 details." + VOICE_TAIL),
    "blocks": [
        intro("Longfu88 Mobile Casino Handbook for Malaysian Players", 70, {K0: 2, KA: 1}, "(the shortcut for Android and iOS, devices, shortcut or browser tab, games, sports, paying from a phone, the welcome offer, account access, security, fixes, support)"),
        blk(["b03"], 2, "Longfu88 Download: No File, Only a Shortcut", 70, {KAPK: 1, K0: 1}),
        blk(["b04"], 3, "Longfu88 Android: Chrome Steps", 55, {}),
        blk(["b05"], 3, "Longfu88 iOS: Safari Steps", 55, {}),
        blk(["b06"], 2, "Supported Devices and Browsers", 65, {K0: 1}),
        blk(["b07"], 2, "Choosing Between the Shortcut and a Browser Tab", 80, {K0: 2}),
        blk(["b02"], 2, "Everything You Can Do on a Phone", 85, {K0: 1}),
        new(3, "Casino Games on a Phone", 55,
            ["brandinfo_games.game_types", "brandinfo_games.providers"],
            [["Casino Games", 10], ["Game Providers", 6]], [["Player", "chooses", "among slots, live dealer games, table games, jackpots and other categories in the casino", 8]],
            "Which game categories and providers the casino section offers.",
            "One lead-in sentence that says that the casino section of the mobile website offers these game categories, then a bulleted list of the categories exactly as in the Brand Information "
            "(slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, crash and instant games). One closing sentence names four or five providers from the list "
            "of the Brand Information (for example Evolution, Pragmatic Play, NetEnt, Hacksaw Gaming). No game names, RTP values, volatility, maximum multipliers or claims that a particular game "
            "works on a phone. " + NO_APP_CLAIMS, ["k02"], PL),
        new(3, "Sports Betting on a Phone", 65,
            ["brandinfo_sportsbook.sportsbook.sports_available", "brandinfo_sportsbook.sportsbook.bet_types", "brandinfo_sportsbook.sportsbook.live_betting",
             "brandinfo_sportsbook.sportsbook.important_terms"],
            [["Sportsbook", 10], ["Live Betting", 8]], [["Live Betting", "offers", "live odds and in-play markets", 8]],
            "Which sports and bet types the sportsbook offers and that live betting has live odds and in-play markets.",
            "The sportsbook is one of the features of the mobile website. One lead-in sentence, then a bulleted list of the sports as given (football, basketball, tennis, badminton, cricket, table tennis, "
            "volleyball, esports, virtual football), then one sentence with the bet types (single, accumulator, live, handicap, totals, outrights, Bet Builder) and one with live betting: live "
            "odds and in-play markets. Say that event availability and markets can vary by jurisdiction. No odds, bonuses, limits or promises of winnings. " + NO_APP_CLAIMS, ["k02"], PL),
        new(2, "Paying and Withdrawing from a Phone", 95,
            [f"brandinfo_deposit.deposit_methods[{i}].{f}" for i in (27, 11, 8, 19, 2) for f in ("method", "currencies", "transaction_speed")]
            + ["brandinfo_privacy_policy.terms_conditions.withdrawal_terms[1]", "brandinfo_privacy_policy.terms_conditions.withdrawal_terms[2]"],
            [["Payment Methods", 10], ["Withdrawals", 7]], [["Player", "pays", "with Touch'n Go, GrabPay, DuitNow, Online Banking or Bank Transfer in Malaysian ringgit", 8]],
            "Five payment methods in Malaysian ringgit with their deposit speed, and the processing time of withdrawals.",
            "One lead-in sentence that says that the cashier is part of the mobile website, then a TABLE with three columns, method | currency | deposit speed, and five rows in this order: "
            "Touch'n Go, GrabPay, DuitNow, Online Banking, Bank Transfer (currency MYR and the speed exactly as in the Brand Information; for Bank Transfer name MYR only). After the table two "
            "sentences on withdrawals: requests are generally processed within three working days, and bank transfers may need another 3-5 business days. " + NO_LIMITS + " Name no other payment "
            "methods and no fees. " + NO_APP_CLAIMS, ["k02"], ["paragraph", "table"]),
        new(2, "Welcome Offer from Your Phone", 65,
            ["brandinfo_welcome.welcome_bonus.name", "brandinfo_welcome.welcome_bonus.bonus_percentage", "brandinfo_welcome.welcome_bonus.maximum_bonus",
             "brandinfo_welcome.welcome_bonus.free_spins", "brandinfo_welcome.welcome_bonus.minimum_deposit", "brandinfo_welcome.welcome_bonus.wagering_requirement"],
            [["Casino Welcome Bonus", 10], ["First Deposit", 7]], [["Casino Welcome Bonus", "requires", "a first qualifying deposit of €50 and activation in My Bonuses", 8]],
            "What a new account can claim from a phone: the Casino Welcome Bonus, its size, the minimum first deposit and the wagering.",
            "Strictly the Brand Information: the Casino Welcome Bonus is a first-deposit casino bonus of 188% up to €2,088 plus 18 free spins; the minimum first deposit is €50; wagering is 25x the "
            "deposit plus bonus amount; the bonus is activated in My Bonuses before placing any wager. Use the €50 minimum of the bonus; do NOT mention the general minimum deposit of €10. No terms that "
            "are not listed and no promises of winnings. " + NO_APP_CLAIMS, ["k02"]),
        blk(["b08"], 2, "Account Access on a Phone: Registration and Login", 75, {K0: 1}, PL),
        blk(["b09"], 2, "Mobile Security and Privacy Terms", 75, {K0: 1}, refs_add=["brandinfo_privacy_policy.privacy_policy.data_sharing", "brandinfo_privacy_policy.privacy_policy.data_subject_rights"],
            extra="Add with whom data may be shared and which rights the player has, as short lists inside the paragraph."),
        blk(["b10"], 2, "Fixing Common Mobile Problems Step by Step", 75, {K0: 1}),
        blk(["b11"], 2, "Support Channels for Mobile Players", 55, {K0: 1}),
        blk(["b12"], 2, "Mobile Handbook FAQ", 100, {K0: 2}, **faq(["app", "phones", "android", "ios", "features", "sports", "login", "support"])),
    ],
})

intrinsic = {
    "b11": {"keyword": K0, "count": 1,
            "replace": [['; it contains the tracked keyword "Longfu88", which is the one occurrence this block allows (so do not write the brand name anywhere else in the block).', "."]],
            "note": 'The e-mail address contains the tracked keyword "Longfu88"; it is part of the exact count of this block.'},
}
blueprint = {"base_run": "longfu88-app-my", "brand_names": ["Longfu88 Mobile Casino", "Longfu88 Download", "Longfu88 Android", "Longfu88 iOS", "Longfu88"], "keyword_labels": {},
             "intrinsic": intrinsic, "variants": variants}

heads = [b["heading"].lower() for v in variants for b in v["blocks"] if b["heading"].lower() not in ("quick answers",)]
dup = {h for h in heads if heads.count(h) > 1}
assert not dup, dup
out = Path("input/variants/longfu88-app-my.json")
out.write_text(json.dumps(blueprint, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(variants), "variants")
