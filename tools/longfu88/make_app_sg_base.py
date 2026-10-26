"""Builds runs/longfu88-app-sg/llm/brief.json and review.json (the answers of the manual step-1 requests) for the Longfu88
app page (brand-subpage, GEO SG). Run from the project root:  python tools/longfu88/make_app_sg_base.py

This is the BASE ТЗ for the OPTIMUM size group of the competitors (`medium`: .best / .vin, 975 / 983 words -> target 979, limit 1175; see
runs/longfu88-app-sg/01_tiers.json; five competitors were readable, tribuna.com and the three Malay pages included). The structure comes
from the clusters of the competitors: Mobile Access k01, Registration and Login k03, Safety k07, FAQ k06 are covered; Games overview k08 and
Payment methods k09 belong to the games and payments pages of the site and are skipped with a reason (2 of 6 mandatory clusters). Two
blocks of our own help a phone user: account access (login, as on a computer) and troubleshooting. The small texts are cut from this
base and the large texts add blocks (tools/longfu88/make_app_sg_variants.py).

The knowledge base has NO native app: `brandinfo_app` describes the responsive website in the browser of a phone or a tablet and a
home-screen shortcut for Android (Chrome) and iOS (Safari). The competitors invent APK files, store listings, biometrics, push
notifications, code signing, encryption, 2FA and system requirements: none of that may reach the text (NO_APP_CLAIMS).

Keywords (targets from the competitors, 01_keyword_stats.json): Longfu88 17, every other keyword once. "Longfu88 app" stands in the H1,
"Longfu88 download", "Longfu88 Android" and "Longfu88 iOS" in the headings of the install blocks, "Longfu app", "Longfu88 mobile casino" and
"Longfu88 apk" in the body of b01 and b03."""
import json
from pathlib import Path

RUN = Path("runs/longfu88-app-sg")
LEGAL = "Do not say or imply that the casino is licensed, legal or approved in Singapore, and do not discuss the licence on this page."
NO_APP_CLAIMS = ("Do not say or imply that a native app, an APK or IPA file, a file download, an app-store listing (Google Play, App Store), a version number, push notifications, "
                 "fingerprint or Face ID login, an offline mode, an in-app chat, or system requirements (OS versions, storage, memory, internet speed) exist: none of them is given. "
                 "Mobile access is the responsive website in the browser of a smartphone or a tablet, plus a home-screen shortcut.")
NO_SECURITY_CLAIMS = ("Do not mention two-factor authentication, SMS codes, CAPTCHA, SSL, TLS, encryption, code signing, biometric login or an audit: no such protection is given.")


def rng(mid):
    return round(mid * 0.88), round(mid * 1.12)


blocks = []


def add(level, heading, source, covers, refs, mid, kw, formats, ents, conns, summary, notes):
    lo, hi = rng(mid)
    blocks.append(dict(level=level, heading=heading, source=source, covers_clusters=covers, kb_refs=refs, words_min=lo, words_max=hi,
                       keywords=kw, formats=formats, entities=[{"name": n, "priority": p} for n, p in ents],
                       entity_connections=[{"subject": a, "relation": r, "object": c, "priority": p} for a, r, c, p in conns],
                       summary=summary, copywriter_notes=notes))


# b01 intro; the H1 carries the keyword "Longfu88 app"
add(1, "Longfu88 App for Android and iOS: Mobile Casino Access in Singapore", "h1", [],
    ["brandinfo_app.app_information.platforms", "brandinfo_app.app_information.mobile_access", "brandinfo_general.minimum_age"], 75,
    {"Longfu88": 3, "Longfu app": 1, "Longfu88 mobile casino": 1}, ["paragraph"],
    [("Mobile Casino", 10), ("Home Screen Shortcut", 8), ("Minimum Age", 5)],
    [("Mobile Casino", "runs in", "the browser of a smartphone or tablet on Android and iOS", 8)],
    "What the page covers: how the casino is used on a phone or a tablet, how to add it to the home screen on Android and iOS, what works on mobile, account access, safety, troubleshooting and support.",
    'Open with the keyword "Longfu88" as the subject of the first sentence: the casino is used on a smartphone or tablet through its responsive website, on Android and iOS. '
    'The phrase "Longfu88 mobile casino" stands once, in a sentence that says what the Longfu88 mobile casino is (the responsive website in the phone browser). '
    'The phrase "Longfu app" stands once, in a sentence that says that players who look for the Longfu app will find the mobile version of the website with a home-screen shortcut '
    '(not a store app). State once that the casino is for players aged 18 or over and that the page is written for players from Singapore. Signpost the topics of the page in one sentence '
    '(features, home-screen shortcut for Android and iOS, supported devices, account access, security, troubleshooting, support) without detail. '
    f'{LEGAL} {NO_APP_CLAIMS} Neutral tone, no promises.')

# b02 what works on mobile (cluster k01)
add(2, "What You Can Do on a Phone", "mandatory", ["k01"],
    ["brandinfo_app.app_information.mobile_access", "brandinfo_app.app_information.features"], 95, {"Longfu88": 2}, ["paragraph", "list"],
    [("Mobile Features", 10), ("Responsive Website", 7), ("Sportsbook", 5)],
    [("Responsive Website", "gives access to", "the casino, the sportsbook, the account, deposits, withdrawals and bonuses", 8)],
    "What a player reaches from a phone or a tablet: the casino, the sportsbook, account access, deposits, withdrawals and bonuses on a responsive website.",
    'One lead-in sentence that says the website adapts to smartphone and tablet browsers (responsive), then a bulleted list with the six items of the Brand Information in the order given (casino, '
    'sportsbook, account access, deposits, withdrawals, bonuses), each item a short phrase of 3-6 words saying what the player can do, then one closing sentence. No game names, providers, RTP values, '
    f'payment method names or bonus amounts here (other pages of the site cover them). {NO_APP_CLAIMS} Use "Longfu88" exactly twice and no other tracked keyword.')

# b03 install lead (cluster k01); the heading carries "Longfu88 download"
add(2, "Longfu88 Download: Add the Casino to Your Home Screen", "mandatory", ["k01"],
    ["brandinfo_app.app_information.mobile_access"], 75, {"Longfu88 apk": 1, "Longfu88": 1}, ["paragraph"],
    [("Home Screen Shortcut", 10), ("Mobile Browser", 7)],
    [("Player", "adds", "a shortcut of the casino website to the home screen once", 8)],
    "How the casino gets onto a phone: the website opens in the mobile browser and a home-screen shortcut is added in three steps, with no file to install.",
    'Three or four sentences before the two sub-sections. Say that the casino works in the browser of a smartphone or tablet and that a home-screen shortcut is added once. '
    'One sentence says that nobody needs an installation file or an APK because the casino opens in the mobile browser and is added to the home screen as a shortcut '
    '(no file and no store listing); where the phrase "Longfu88 apk" is used it stands in that sentence. Say that the next two sub-sections give the steps for Android (Chrome) and for iOS (Safari). '
    f'Do not give a download link, file size or version number. {NO_APP_CLAIMS}')

# b04 Android (cluster k01, sub-section)
add(3, "Longfu88 Android: Add the Shortcut in Chrome", "mandatory", ["k01"],
    ["brandinfo_app.app_information.android_installation"], 55, {}, ["paragraph", "list"],
    [("Android", 10), ("Chrome", 8)],
    [("Chrome", "adds", "a shortcut of the casino website to the Android home screen", 8)],
    "The three Android steps: open the site in Chrome, choose Add to Home screen in the browser menu, confirm the shortcut.",
    'One lead-in sentence, then a NUMBERED list with the three steps in the order of the Brand Information (open the casino website in Chrome; open the browser menu and choose Add to Home screen; '
    'confirm the shortcut). Write "the site" or "the casino website" in the steps instead of the brand name. '
    f'One closing clause may say that the shortcut then appears among the apps of the phone. {NO_APP_CLAIMS}')

# b05 iOS (cluster k01, sub-section)
add(3, "Longfu88 iOS: Add the Shortcut in Safari", "mandatory", ["k01"],
    ["brandinfo_app.app_information.ios_installation"], 55, {}, ["paragraph", "list"],
    [("iOS", 10), ("Safari", 8)],
    [("Safari", "adds", "a shortcut of the casino website to the iPhone or iPad home screen", 8)],
    "The three iOS steps: open the site in Safari, tap Share and choose Add to Home Screen, confirm Add.",
    'One lead-in sentence, then a NUMBERED list with the three steps in the order of the Brand Information (open the casino website in Safari; tap Share and choose Add to Home Screen; confirm Add). '
    'Write "the site" or "the casino website" in the steps instead of the brand name. '
    f'The lead-in must not repeat the wording of the Android sub-section. {NO_APP_CLAIMS}')

# b06 compatibility (cluster k01)
add(2, "Supported Phones and Browsers", "mandatory", ["k01"],
    ["brandinfo_app.app_information.platforms", "brandinfo_app.app_information.mobile_access"], 70, {"Longfu88": 2}, ["paragraph"],
    [("Supported Platforms", 10), ("Mobile Browser", 8)],
    [("Supported Platforms", "include", "Android, iOS and the mobile web of smartphones and tablets", 8)],
    "Which devices work: Android phones, iPhones and iPads and any smartphone or tablet browser, with Chrome on Android and Safari on iOS for the shortcut.",
    'Lead with the three platforms exactly as given (Android, iOS, mobile web) and say that the layout adapts to smartphone and tablet screens. Chrome is the browser of the Android route and Safari of the iOS route. '
    f'Say plainly that the casino needs no installation file. Do not state OS versions, device models, storage, memory or connection speed: none are given. {NO_APP_CLAIMS} '
    'Use "Longfu88" exactly twice and no other tracked keyword.')

# b07 shortcut or browser tab (cluster k01)
add(2, "Home Screen Shortcut or Browser Tab", "mandatory", ["k01"],
    ["brandinfo_app.app_information.mobile_access", "brandinfo_app.app_information.features"], 85, {"Longfu88": 2}, ["paragraph"],
    [("Home Screen Shortcut", 10), ("Browser Tab", 8)],
    [("Home Screen Shortcut", "opens", "the same responsive website as the browser tab", 8)],
    "How the two ways of opening the casino on a phone differ: a one-tap icon from the home screen or a tab in the browser, both on the same website.",
    'Compare only what the facts allow: both ways open the same responsive website, so the account, deposits, withdrawals and bonuses are the same in both; the shortcut is set up once and gives an icon on the home screen; '
    'the browser tab needs no setup. Add one practical tip (the shortcut suits a phone that is used often, the tab suits a device that is used rarely). '
    f'Do NOT compare speed, battery, storage, notifications, offline use or login convenience: no such data. {NO_APP_CLAIMS} Use "Longfu88" exactly twice and no other tracked keyword.')

# b08 account access on a phone (cluster k03)
add(2, "Account Access on a Phone", "mandatory", ["k03"],
    ["brandinfo_account.login.method", "brandinfo_account.login.steps", "brandinfo_account.registration.methods", "brandinfo_account.registration.required_details"], 85, {"Longfu88": 1}, ["paragraph"],
    [("Player Account", 10), ("Login", 8), ("Registration", 6)],
    [("Player", "logs in to", "the Player Account on a phone with e-mail and password", 8)],
    "How a player gets into the account from a phone: registration by e-mail, then login with the registered e-mail and password, as on a computer.",
    'Registration is by e-mail only; the form asks for e-mail, password, legal name, date of birth and residential address. The login is the same on a phone as on a computer: select Login, enter the registered e-mail and password. '
    'Name the steps in one flowing paragraph, not a list. A player who forgot the password uses Forgot Password on the login screen (pointer only; the other page of the site covers it in detail). '
    f'{NO_SECURITY_CLAIMS} Do not mention a username, a player ID, saved logins or a phone number login. {NO_APP_CLAIMS} Use "Longfu88" exactly once and no other tracked keyword.')

# b09 security (cluster k07)
add(2, "Mobile Security and Privacy", "mandatory", ["k07"],
    ["brandinfo_privacy_policy.privacy_policy.security", "brandinfo_privacy_policy.terms_conditions.account_terms"], 80, {"Longfu88": 1}, ["paragraph"],
    [("Account Security", 10), ("Login Credentials", 8)],
    [("Account Holder", "safeguards", "the login credentials on every device", 8)],
    "Who protects the account on a phone: the holder keeps the credentials safe, the operator applies technical and organisational safeguards and may suspend activity for verification.",
    'Lead with the player\'s own part: the account holder is responsible for safeguarding the login credentials, also on a phone or a tablet. One general tip is allowed (do not share the device unlocked with others). '
    'Then the operator\'s part exactly at the level of detail of the Brand Information: technical and organisational safeguards protect accounts, payments and personal information, and the casino may suspend activity for verification or suspected abuse. '
    f'{NO_SECURITY_CLAIMS} {NO_APP_CLAIMS} Do not print the contact addresses of the privacy policy. Use "Longfu88" exactly once and no other tracked keyword.')

# b10 troubleshooting (unique)
add(2, "Fixing Common Mobile Problems", "unique", [],
    ["brandinfo_account.login.password_recovery", "brandinfo_general.customer_support.channels"], 75, {"Longfu88": 2}, ["paragraph", "list"],
    [("Mobile Troubleshooting", 10), ("Customer Support", 6)],
    [("Customer Support", "helps with", "problems that the checks on this page do not solve", 7)],
    "Four common phone problems and the plain fix for each: shortcut missing, page not loading, login failing, still stuck.",
    'One lead-in sentence, then a bulleted list of four items "problem: fix": the shortcut does not appear (repeat the steps in Chrome on Android or in Safari on iOS); the page does not load (reload it and check the '
    'internet connection); the login fails (check the e-mail address and use Forgot Password on the login screen); the problem remains (contact support through live chat, 24/7, or by e-mail; do not print the e-mail address here). '
    f'General wording only, no error codes and no browser-setting instructions presented as casino facts. {NO_APP_CLAIMS} Use "Longfu88" exactly twice and no other tracked keyword.')

# b11 support (non-mandatory cluster k02)
add(2, "Support for Mobile Players", "unique", ["k02"],
    ["brandinfo_general.customer_support"], 60, {"Longfu88": 1}, ["paragraph"],
    [("Customer Support", 10), ("Live Chat", 8)],
    [("Customer Support", "answers", "mobile and account questions through live chat and e-mail", 8)],
    "How to reach support from a phone: live chat around the clock, e-mail and the languages of the support team.",
    'Support channels: 24/7 live chat and e-mail. Print the e-mail address exactly as given in the Brand Information; it contains the tracked keyword "Longfu88", which is the one occurrence this block '
    'allows (so do not write the brand name anywhere else in the block). Support languages: English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese. Say which questions go here (the shortcut that does not appear, '
    f'the page that does not load, login, documents) without response-time promises. {NO_APP_CLAIMS}')

# b12 FAQ (cluster k06)
add(2, "Mobile Access FAQ", "mandatory", ["k06"],
    ["brandinfo_app.app_information.platforms", "brandinfo_app.app_information.mobile_access", "brandinfo_account.login.method", "brandinfo_general.minimum_age",
     "brandinfo_general.customer_support.channels"], 115, {"Longfu88": 2}, ["list"],
    [("Frequently Asked Questions", 10), ("Mobile Access", 7)],
    [("Player", "finds", "short answers to the most frequent questions about the casino on a phone", 6)],
    "Five short questions and answers on a downloadable app, Android and iOS, the home-screen shortcut, the login on a phone and where to get help.",
    'A bulleted list of five items in the form "- **Question?** Answer." (bold question, then a one-sentence answer); bold is required here for the question text only. Questions, in this order: '
    'is there a store app to download (no: the casino opens in the browser and is added to the home screen as a shortcut); which phones work (Android, iOS and the mobile web of smartphones and tablets); '
    'how the shortcut is added (Chrome on Android with Add to Home screen, Safari on iOS with Add to Home Screen); how a player logs in on a phone (with the registered e-mail and password); '
    'where to turn when something fails (customer support, live chat 24/7; do not print the e-mail). Answers repeat the facts of the sections of the page in other words and add nothing new. '
    f'{NO_APP_CLAIMS} Use "Longfu88" exactly twice and no other tracked keyword.')

intent = ("A player in Singapore who looks for the Longfu88 app, an APK or a download wants to use the casino on a phone: what the mobile version is, how to put it on the Android or iOS home screen, "
          "which devices work, how to log in on a phone, what protects the account and where to get help. The facts say the mobile version is the responsive website in the browser with a "
          "home-screen shortcut, so the page explains that route and does not promise a store app or a file. The structure follows the app pages of the competitors of the medium size group; the "
          "games and the payments belong to other pages of the site, and the licence and the bonus programme are not discussed here.")

brief = {"intent_summary": intent, "blocks": blocks,
         "skipped_clusters": [
             {"id": "k08", "reason": "the games overview belongs to the games pages of the site; the app page names the casino as one feature of the mobile website"},
             {"id": "k09", "reason": "the payment methods belong to the payments page of the site; the app page names deposits and withdrawals as features of the mobile website"}]}
(RUN / "llm").mkdir(parents=True, exist_ok=True)
(RUN / "llm" / "brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=1), encoding="utf-8")
(RUN / "llm" / "review.json").write_text(json.dumps({"issues": [], "blocks": blocks}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(blocks), "blocks, mid words", sum(round((b["words_min"] + b["words_max"]) / 2) for b in blocks))
