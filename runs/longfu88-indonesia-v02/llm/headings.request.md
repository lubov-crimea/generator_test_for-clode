# SYSTEM

You localize the headings of a casino-review page. The brief is in English; the page is in another language. You receive JSON items with an English working heading and, for some, the tracked keywords that the localized heading must contain.

Rules:
- Write each heading in the page language, natural and idiomatic for the GEO, as an SEO editor would write it (not a word-for-word translation). Keep the meaning and the level of detail of the English heading. Sentence-style capitalisation of the language.
- Tracked keywords are brand names and fixed phrases: when `keywords_the_heading_must_contain` lists a keyword, the heading must contain it exactly as written (same spelling, same word order, not inflected), the stated number of times. When the list is empty, the heading must NOT contain any tracked keyword or brand name. Keep the heading short: usually 2-9 words.
- Proper names (programme, bonus, game, product names) may stay as they are. Established terms keep their usual form in the language.
- No quotation marks, no emojis, no trailing full stop, no em dashes. A colon is allowed.
- If `problems_to_fix` is present, rewrite the heading so that every problem is solved; keep `current_heading` where it was already fine.

Return every id you received, with the localized heading, through the tool.

# USER

Page language: Indonesian (id). GEO: Indonesia.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports

Headings to localize:
[
 {
  "id": "b01",
  "level": 1,
  "english_heading": "Longfu88 Casino Indonesia: Safety, Terms and Controls Reviewed",
  "keywords_the_heading_must_contain": {
   "Longfu88 casino": 1
  }
 },
 {
  "id": "b02",
  "level": 2,
  "english_heading": "Operator, Licence and Data Handling",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b03",
  "level": 2,
  "english_heading": "Verified Brand Details",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b04",
  "level": 2,
  "english_heading": "Registration and Login Safely",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b05",
  "level": 3,
  "english_heading": "How Verification Works and What It Takes",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b06",
  "level": 2,
  "english_heading": "Responsible Gambling: Self-Exclusion and Help",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b07",
  "level": 2,
  "english_heading": "Welcome Offer and Its Conditions",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b08",
  "level": 3,
  "english_heading": "Wagering, Caps and Exclusions",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b09",
  "level": 2,
  "english_heading": "VIP Levels and Higher Limits",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b10",
  "level": 2,
  "english_heading": "Reloads and Seasonal Offers: Rules Included",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b11",
  "level": 3,
  "english_heading": "Cashback Conditions",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b12",
  "level": 2,
  "english_heading": "Deposit Methods and Their Limits",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b13",
  "level": 3,
  "english_heading": "Withdrawals: Timing, Fees and Turnover",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b14",
  "level": 2,
  "english_heading": "Games on Offer",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b15",
  "level": 3,
  "english_heading": "Slots: RTP and Volatility",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b16",
  "level": 3,
  "english_heading": "Live Dealer Games",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b17",
  "level": 2,
  "english_heading": "Providers",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b18",
  "level": 2,
  "english_heading": "Using the Casino on Mobile",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b19",
  "level": 2,
  "english_heading": "Sportsbook Markets and Rules",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b20",
  "level": 3,
  "english_heading": "Sports Promotions",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b21",
  "level": 2,
  "english_heading": "Strengths and Limits",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b22",
  "level": 2,
  "english_heading": "Support Channels and Languages",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b23",
  "level": 2,
  "english_heading": "Questions on Verification and Payouts",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b24",
  "level": 2,
  "english_heading": "Before You Deposit",
  "keywords_the_heading_must_contain": {}
 }
]
