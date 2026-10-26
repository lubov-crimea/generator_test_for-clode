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

Page language: Italian (it). GEO: IT.
All tracked keywords: Incaspin, Inca Spin, Incaspin casino

Headings to localize:
[
 {
  "id": "b01",
  "level": 1,
  "english_heading": "Incaspin Casino: Bonus, Registration, Games and Withdrawals",
  "keywords_the_heading_must_contain": {
   "Incaspin casino": 1
  }
 },
 {
  "id": "b02",
  "level": 2,
  "english_heading": "Incaspin Casino Overview",
  "keywords_the_heading_must_contain": {
   "Incaspin casino": 1
  }
 },
 {
  "id": "b03",
  "level": 2,
  "english_heading": "Casino Information at a Glance",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b04",
  "level": 2,
  "english_heading": "Registration at Incaspin Casino",
  "keywords_the_heading_must_contain": {
   "Incaspin casino": 1
  }
 },
 {
  "id": "b05",
  "level": 3,
  "english_heading": "Login and Account Security",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b06",
  "level": 2,
  "english_heading": "Welcome Bonus at Incaspin Casino",
  "keywords_the_heading_must_contain": {
   "Incaspin casino": 1
  }
 },
 {
  "id": "b07",
  "level": 3,
  "english_heading": "Bonus Terms at a Glance",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b08",
  "level": 3,
  "english_heading": "Promo Code and Activation",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b09",
  "level": 2,
  "english_heading": "More Promotions and Cashback at Incaspin",
  "keywords_the_heading_must_contain": {
   "Incaspin": 1
  }
 },
 {
  "id": "b10",
  "level": 2,
  "english_heading": "Games at Incaspin Casino",
  "keywords_the_heading_must_contain": {
   "Incaspin casino": 1
  }
 },
 {
  "id": "b11",
  "level": 3,
  "english_heading": "Slots",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b12",
  "level": 3,
  "english_heading": "Live Casino",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b13",
  "level": 3,
  "english_heading": "Table Games, Jackpots and Crash Games",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b14",
  "level": 3,
  "english_heading": "Game Providers",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b15",
  "level": 2,
  "english_heading": "Sports Betting and Esports at Incaspin",
  "keywords_the_heading_must_contain": {
   "Incaspin": 1
  }
 },
 {
  "id": "b16",
  "level": 2,
  "english_heading": "Deposits and Payment Methods",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b17",
  "level": 2,
  "english_heading": "Withdrawals at Incaspin",
  "keywords_the_heading_must_contain": {
   "Incaspin": 1
  }
 },
 {
  "id": "b18",
  "level": 3,
  "english_heading": "Account Verification (KYC)",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b19",
  "level": 2,
  "english_heading": "Mobile Play: Incaspin on Android and iOS",
  "keywords_the_heading_must_contain": {
   "Incaspin": 1
  }
 },
 {
  "id": "b20",
  "level": 2,
  "english_heading": "VIP and Loyalty Programme at Incaspin",
  "keywords_the_heading_must_contain": {
   "Incaspin": 1
  }
 },
 {
  "id": "b21",
  "level": 2,
  "english_heading": "Safety and Licence at Incaspin Casino",
  "keywords_the_heading_must_contain": {
   "Incaspin casino": 1
  }
 },
 {
  "id": "b22",
  "level": 2,
  "english_heading": "Responsible Gambling",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b23",
  "level": 2,
  "english_heading": "Customer Support",
  "keywords_the_heading_must_contain": {}
 },
 {
  "id": "b24",
  "level": 2,
  "english_heading": "Frequently Asked Questions about Incaspin Casino",
  "keywords_the_heading_must_contain": {
   "Incaspin casino": 1
  }
 },
 {
  "id": "b25",
  "level": 2,
  "english_heading": "Conclusion",
  "keywords_the_heading_must_contain": {}
 }
]
