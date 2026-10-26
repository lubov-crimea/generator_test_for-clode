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

Page language: Malay (ms). GEO: Malaysia.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports

Headings to localize:
[
 {
  "id": "b01",
  "level": 1,
  "english_heading": "Longfu88 Casino Malaysia: Payments and Payout Review",
  "keywords_the_heading_must_contain": {
   "Longfu88 casino": 1
  }
 },
 {
  "id": "b02",
  "level": 2,
  "english_heading": "Key Payment and Brand Facts",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b03",
  "level": 2,
  "english_heading": "Payment Methods for Deposits and Their Limits",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b04",
  "level": 3,
  "english_heading": "Payouts: Methods, Timing and Fees",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b05",
  "level": 2,
  "english_heading": "ID Checks Before You Cash Out",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b06",
  "level": 2,
  "english_heading": "Account Registration and Login",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b07",
  "level": 2,
  "english_heading": "Welcome Offer, Wagering and Caps",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b08",
  "level": 2,
  "english_heading": "Cashback and Daily Rebates",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b09",
  "level": 2,
  "english_heading": "VIP Programme and Cash-Out Limits",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b10",
  "level": 2,
  "english_heading": "Reload Offers",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b11",
  "level": 2,
  "english_heading": "Game Types and Examples",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b12",
  "level": 2,
  "english_heading": "Game Studios",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b13",
  "level": 2,
  "english_heading": "Sports Betting and Promotions",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b14",
  "level": 2,
  "english_heading": "Operator, Licence and Data Safety",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b15",
  "level": 2,
  "english_heading": "Mobile Access",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b16",
  "level": 2,
  "english_heading": "Customer Support Channels",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b17",
  "level": 2,
  "english_heading": "Responsible Gambling Measures",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b18",
  "level": 2,
  "english_heading": "Payment Questions",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b19",
  "level": 2,
  "english_heading": "Verdict on Payments",
  "keywords_the_heading_must_contain": {}
 }
]
