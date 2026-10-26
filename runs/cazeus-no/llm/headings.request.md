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

Page language: Norwegian (no). GEO: NO.
All tracked keywords: Cazeus, Cazues casino

Headings to localize:
[
 {
  "id": "b01",
  "level": 1,
  "english_heading": "Cazeus Casino Norway: Review of Bonuses, Games and Payments",
  "keywords_the_heading_must_contain": {
   "Cazeus": 1
  }
 },
 {
  "id": "b02",
  "level": 2,
  "english_heading": "Casino Facts at a Glance",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b03",
  "level": 2,
  "english_heading": "About Cazeus Casino",
  "keywords_the_heading_must_contain": {
   "Cazeus": 1
  }
 },
 {
  "id": "b04",
  "level": 2,
  "english_heading": "Cazeus Welcome Package and Bonuses",
  "keywords_the_heading_must_contain": {
   "Cazeus": 1
  }
 },
 {
  "id": "b05",
  "level": 3,
  "english_heading": "Reload Bonuses and Cashback",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b06",
  "level": 3,
  "english_heading": "Challenges, Collections and Rewards Shop",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b07",
  "level": 2,
  "english_heading": "Casino Games",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b08",
  "level": 3,
  "english_heading": "Providers and Popular Slots",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b09",
  "level": 3,
  "english_heading": "Live Casino",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b10",
  "level": 2,
  "english_heading": "Sports Betting",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b11",
  "level": 2,
  "english_heading": "Cazeus Registration and Login",
  "keywords_the_heading_must_contain": {
   "Cazeus": 1
  }
 },
 {
  "id": "b12",
  "level": 3,
  "english_heading": "Account Verification",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b13",
  "level": 2,
  "english_heading": "Deposits and Withdrawals",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b14",
  "level": 3,
  "english_heading": "Deposit Methods",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b15",
  "level": 3,
  "english_heading": "Withdrawals",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b16",
  "level": 2,
  "english_heading": "VIP Club",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b17",
  "level": 2,
  "english_heading": "Mobile Casino and App",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b18",
  "level": 2,
  "english_heading": "Licence, Security and Data Protection",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b19",
  "level": 2,
  "english_heading": "Customer Support",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b20",
  "level": 2,
  "english_heading": "Responsible Gambling",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b21",
  "level": 2,
  "english_heading": "Player Experience: Pros and Cons",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b22",
  "level": 2,
  "english_heading": "Verdict on Cazeus Casino",
  "keywords_the_heading_must_contain": {
   "Cazeus": 1
  }
 }
]
