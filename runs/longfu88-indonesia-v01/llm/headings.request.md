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
  "english_heading": "Longfu88 Casino Indonesia: Bonuses, Games and Payments Reviewed",
  "keywords_the_heading_must_contain": {
   "Longfu88 casino": 1
  }
 },
 {
  "id": "b02",
  "level": 2,
  "english_heading": "Quick Facts About the Casino",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b03",
  "level": 2,
  "english_heading": "Welcome Bonus for New Players",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b04",
  "level": 3,
  "english_heading": "Terms You Must Meet to Cash Out the Bonus",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b05",
  "level": 2,
  "english_heading": "VIP Ladder: 25 Levels from Bronze to Diamond",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b06",
  "level": 2,
  "english_heading": "Weekly, Weekend and Seasonal Reloads",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b07",
  "level": 3,
  "english_heading": "Cashback and Rebate Rates",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b08",
  "level": 3,
  "english_heading": "Rewards Area: Crab, Wheel and Coin Shop",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b09",
  "level": 2,
  "english_heading": "Sports Betting and Its Bonuses",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b10",
  "level": 3,
  "english_heading": "Sports Promotions in Detail",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b11",
  "level": 2,
  "english_heading": "How to Register and Log In",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b12",
  "level": 3,
  "english_heading": "ID Checks and Document Rules",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b13",
  "level": 2,
  "english_heading": "Payment Options for Deposits",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b14",
  "level": 3,
  "english_heading": "Cashing Out: Steps, Timing and Fees",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b15",
  "level": 2,
  "english_heading": "Game Library at a Glance",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b16",
  "level": 3,
  "english_heading": "Slot Examples and Their Numbers",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b17",
  "level": 3,
  "english_heading": "Live Casino and Exclusive Baccarat",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b18",
  "level": 3,
  "english_heading": "Other Game Types: Fishing, P2P, Lottery",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b19",
  "level": 2,
  "english_heading": "Studios Behind the Games",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b20",
  "level": 2,
  "english_heading": "Licence, Operator and Eligibility",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b21",
  "level": 2,
  "english_heading": "Playing on Phone and Tablet",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b22",
  "level": 2,
  "english_heading": "Contacting Support",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b23",
  "level": 2,
  "english_heading": "Responsible Play and Self-Exclusion Tools",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b24",
  "level": 2,
  "english_heading": "Pros and Cons at a Glance",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b25",
  "level": 2,
  "english_heading": "Bonus and Payout Questions",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b26",
  "level": 2,
  "english_heading": "Overall Assessment",
  "keywords_the_heading_must_contain": {}
 }
]
