# SYSTEM

You are a senior SEO content strategist for iGaming affiliate sites. You build the technical brief (ТЗ) for ONE casino-brand review page that must outrank the given competitors for the given keywords in the given GEO.

You receive JSON with: geo, page language, brand and keywords, competitor H1s, keyword statistics of competitors, heading clusters (frequency, mandatory flag, typical section length, typical position), entity candidates mined from competitor texts, and numeric targets.

Work like this:

1. Decide the search intent behind the keywords (usually: brand query -> informational + navigational review page: what the casino is, register, login, bonuses, games, payments, app, safety). Put it in `intent_summary`.

2. Build the heading structure as a flat ordered list of blocks. Block 1 is the H1 (level 1) with a short intro. All other blocks are H2-H6.
   - EVERY cluster flagged `mandatory: true` must be covered by a heading (several near-duplicate clusters may share one heading; list their ids in `covers_clusters`).
   - Add a unique (non-mandatory) cluster only if it fits the intent and adds value. Skip off-topic ones.
   - Order blocks logically, using `avg_position` as a hint. Never skip heading levels (H2 -> H4). H3+ must sit under a fitting parent.
   - Headings are written in the page language. Put keywords into headings only where it reads naturally and where competitors do it.

3. For EVERY block provide all of the following (this is the format of the ТЗ):
   - `words_min` / `words_max`: allowed length of the BODY text (heading excluded). Use competitors' typical section lengths. The range width is about ±15% of the middle (max/min <= 1.4 is typical; never above 1.8). The sum of all middles must be close to `target_body_words`. A parent heading's own range covers only its own intro text; sub-sections have their own ranges.
   - `keywords`: how many times each keyword must appear in the BODY of this block (heading excluded). Include EVERY keyword, 0 when unused. For every keyword: sum over all blocks + occurrences inside headings must equal `keyword_targets[keyword]` exactly. Counting rules: case-insensitive, whole words, longest match first (an occurrence of "X casino" counts only for "X casino", not also for "X"). Spread them naturally: the brand early (intro) and in key sections, long-tail variants (login, app, register...) in the sections where they belong. Never more than 1 keyword mention per ~15 words in a block.
   - `entities`: 2-10 entities the block must cover, each with `priority` 1-10 (10 = the main entity of the block). Take them from `entity_candidates` and from the topic (payment systems, game providers, regulators, bonus types, technical terms, game types). Use generic names for the brand itself (e.g. "Online Casino"), never the brand name. Entities that are specific facts about the brand (a licence, a payment method, a provider) may be listed only if they appear in `facts_to_respect` or are clearly competitor-wide industry standards; otherwise list the category (e.g. "E-wallets") and let the notes say "name specifics only if given in the brand information".
   - `entity_connections`: 1-4 relations between entities the text must state explicitly, as subject -> relation (a verb phrase) -> object, with `priority` 1-10. Example: Licence -> regulates -> Online Casino [8].
   - `summary`: 1-3 sentences, what the block says, in the page language.
   - `copywriter_notes`: binding instructions in the page language: which entity to lead with, order of the argument, what to avoid, which facts must not be invented, tone. Concrete, not generic.
   - `formats`: list from ["paragraph", "list", "table"]. Steps/features -> list, comparisons/payment methods/specs -> table, explanations -> paragraph. A block may combine formats (e.g. ["paragraph","list"]).
   - `source`: "h1", "mandatory" or "unique".
   Write `summary`, `copywriter_notes` and entity/relation names in the PAGE LANGUAGE (like a real ТЗ for a writer in that language).

4. Check the whole brief for consistency before answering: logical order, no overlapping blocks, the intro does not duplicate later sections, entity connections do not contradict each other, keyword and word sums are correct.

Return the result through the tool.

# USER

{
 "geo": "Australia",
 "page_language": "English",
 "keywords": [
  "VegasHunter",
  "Vegas Hunter",
  "VegasHunter casino",
  "Vegas Hunter casino",
  "VegasHunter login",
  "VegasHunter app",
  "VegasHunter pokies",
  "VegasHunter register",
  "VegasHunter official",
  "VegasHunter online casino"
 ],
 "facts_to_respect": [],
 "competitor_h1": [
  "Vegas Hunter Online Casino Australia",
  "CrashPirate Casino UK"
 ],
 "competitor_stats": [
  {
   "url": "https://vegas-hunter.org/",
   "body_words": 1195,
   "keywords_in_total": {
    "VegasHunter": 0,
    "Vegas Hunter": 6,
    "VegasHunter casino": 0,
    "Vegas Hunter casino": 1,
    "VegasHunter login": 0,
    "VegasHunter app": 0,
    "VegasHunter pokies": 0,
    "VegasHunter register": 0,
    "VegasHunter official": 0,
    "VegasHunter online casino": 0
   },
   "keywords_in_h1": {
    "VegasHunter": 0,
    "Vegas Hunter": 1,
    "VegasHunter casino": 0,
    "Vegas Hunter casino": 0,
    "VegasHunter login": 0,
    "VegasHunter app": 0,
    "VegasHunter pokies": 0,
    "VegasHunter register": 0,
    "VegasHunter official": 0,
    "VegasHunter online casino": 0
   },
   "keywords_in_h2": {
    "VegasHunter": 0,
    "Vegas Hunter": 3,
    "VegasHunter casino": 0,
    "Vegas Hunter casino": 1,
    "VegasHunter login": 0,
    "VegasHunter app": 0,
    "VegasHunter pokies": 0,
    "VegasHunter register": 0,
    "VegasHunter official": 0,
    "VegasHunter online casino": 0
   }
  },
  {
   "url": "https://crashpirate.games/en-en1/",
   "body_words": 3403,
   "keywords_in_total": {
    "VegasHunter": 0,
    "Vegas Hunter": 0,
    "VegasHunter casino": 0,
    "Vegas Hunter casino": 0,
    "VegasHunter login": 0,
    "VegasHunter app": 0,
    "VegasHunter pokies": 0,
    "VegasHunter register": 0,
    "VegasHunter official": 0,
    "VegasHunter online casino": 0
   },
   "keywords_in_h1": {
    "VegasHunter": 0,
    "Vegas Hunter": 0,
    "VegasHunter casino": 0,
    "Vegas Hunter casino": 0,
    "VegasHunter login": 0,
    "VegasHunter app": 0,
    "VegasHunter pokies": 0,
    "VegasHunter register": 0,
    "VegasHunter official": 0,
    "VegasHunter online casino": 0
   },
   "keywords_in_h2": {
    "VegasHunter": 0,
    "Vegas Hunter": 0,
    "VegasHunter casino": 0,
    "Vegas Hunter casino": 0,
    "VegasHunter login": 0,
    "VegasHunter app": 0,
    "VegasHunter pokies": 0,
    "VegasHunter register": 0,
    "VegasHunter official": 0,
    "VegasHunter online casino": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 2299,
  "keyword_targets": {
   "VegasHunter": 1,
   "Vegas Hunter": 3,
   "VegasHunter casino": 1,
   "Vegas Hunter casino": 1,
   "VegasHunter login": 1,
   "VegasHunter app": 1,
   "VegasHunter pokies": 1,
   "VegasHunter register": 1,
   "VegasHunter official": 1,
   "VegasHunter online casino": 1
  }
 },
 "heading_clusters": [
  {
   "id": "k01",
   "canonical_title": "About the Casino",
   "topic": "Casino overview / introduction",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 150,
   "avg_position": 0.04,
   "examples": [
    "Introduction",
    "Everything About the CrashPirate Casino Site"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "Games and Pokies Overview",
   "topic": "Games overview",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 78,
   "avg_position": 0.19,
   "examples": [
    "Casino Game Categories at Vegas Hunter",
    "Games we cover",
    "Online Slots and Casino Games"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Game Categories",
   "topic": "Game types: slots, table, jackpot, specialty games",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 44,
   "avg_position": 0.38,
   "examples": [
    "Slots",
    "Card Games",
    "Roulette",
    "Game Shows"
   ]
  },
  {
   "id": "k02",
   "canonical_title": "Bonuses and Promotions",
   "topic": "Bonuses, welcome offer and promotions",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 81,
   "avg_position": 0.5,
   "examples": [
    "Vegas Hunter Casino Bonuses & Promotions",
    "Welcome Bonus and Ongoing Promotions",
    "What Is the CrashPirate Welcome Bonus?"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Game Providers",
   "topic": "Game providers",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 102,
   "avg_position": 0.5,
   "examples": [
    "Top Providers",
    "Game Providers"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "How to Register and Start Playing",
   "topic": "Registration / getting started",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 130,
   "avg_position": 0.51,
   "examples": [
    "How to Start Playing (Step-by-Step Guide)",
    "Registering an Account at CrashPirate"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Crash Games",
   "topic": "Crash games",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 136,
   "avg_position": 0.56,
   "examples": [
    "Crash Games",
    "Crash Games and How They Work",
    "How Do Crash Games Work?"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Payment Methods",
   "topic": "Payment methods and deposits",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 54,
   "avg_position": 0.59,
   "examples": [
    "Payment Methods at Vegas Hunter Australia",
    "Traditional Payment Methods",
    "Cryptocurrency Payments",
    "Payment Methods, Deposits and Withdrawals"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Mobile App for Android and iOS",
   "topic": "Mobile app",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 104,
   "avg_position": 0.68,
   "examples": [
    "Mobile Casino App for Android & iOS",
    "CrashPirate App and Mobile Play",
    "Does CrashPirate Have a Mobile App?"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "Customer Support",
   "topic": "Customer support",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 64,
   "avg_position": 0.68,
   "examples": [
    "Support",
    "Customer Support and Complaints",
    "How Do I Contact CrashPirate Customer Support?"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Why Players Choose the Casino",
   "topic": "Why choose / pros and cons",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 126,
   "avg_position": 0.75,
   "examples": [
    "Why Australian Players Choose Vegas Hunter",
    "Pros and Cons of CrashPirate Casino"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Responsible Gambling",
   "topic": "Responsible gambling and player protection",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 105,
   "avg_position": 0.81,
   "examples": [
    "Responsible Gambling",
    "Responsible Gambling and Player Protection"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "KYC Verification",
   "topic": "KYC verification",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 153,
   "avg_position": 0.28,
   "examples": [
    "KYC Verification: Which Documents and How Long"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Licensing and Safety",
   "topic": "Licensing, safety and legitimacy",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 112,
   "avg_position": 0.42,
   "examples": [
    "Licensing, Safety and Is CrashPirate Legit?",
    "Is CrashPirate Casino Legit and Safe to Use?"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Live Dealer Games",
   "topic": "Live dealer games",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 164,
   "avg_position": 0.48,
   "examples": [
    "Live Dealer Games"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Withdrawals: Times and Limits",
   "topic": "Withdrawals timing and limits",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 101,
   "avg_position": 0.54,
   "examples": [
    "Withdrawal Times, Limits and Processing",
    "How Long Do CrashPirate Withdrawals Take?"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Tournaments and Prize Drops",
   "topic": "Tournaments and prize drops",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 78,
   "avg_position": 0.6,
   "examples": [
    "Tournaments and Prize Drops"
   ]
  },
  {
   "id": "k20",
   "canonical_title": "VIP Club and Loyalty Rewards",
   "topic": "VIP and loyalty program",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 148,
   "avg_position": 0.64,
   "examples": [
    "VIP Club and Loyalty Rewards"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Additional Payment Information",
   "topic": "Payments additional information",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 44,
   "avg_position": 0.79,
   "examples": [
    "Additional Information"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "Who Can Play",
   "topic": "Eligibility of players from a country",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 56,
   "avg_position": 0.8,
   "examples": [
    "Can UK Players Ppen an Account at CrashPirate?"
   ]
  },
  {
   "id": "k21",
   "canonical_title": "Conclusion",
   "topic": "Conclusion",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 35,
   "avg_position": 0.96,
   "examples": [
    "Conclusion"
   ]
  },
  {
   "id": "k22",
   "canonical_title": "FAQ",
   "topic": "FAQ",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 63,
   "avg_position": 1.0,
   "examples": [
    "FAQ"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "APK",
   "competitors": 2
  },
  {
   "entity": "Android",
   "competitors": 2
  },
  {
   "entity": "Curaçao",
   "competitors": 2
  },
  {
   "entity": "BTC",
   "competitors": 2
  },
  {
   "entity": "ETH",
   "competitors": 2
  },
  {
   "entity": "RTP",
   "competitors": 2
  },
  {
   "entity": "Safari",
   "competitors": 2
  },
  {
   "entity": "USDT",
   "competitors": 2
  },
  {
   "entity": "Virtual Sports",
   "competitors": 2
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 2
  },
  {
   "entity": "KYC",
   "competitors": 2
  },
  {
   "entity": "Crash Games",
   "competitors": 2
  },
  {
   "entity": "Game Shows",
   "competitors": 2
  },
  {
   "entity": "Video Poker",
   "competitors": 2
  },
  {
   "entity": "Payment Methods",
   "competitors": 2
  },
  {
   "entity": "Responsible Gambling",
   "competitors": 2
  },
  {
   "entity": "App",
   "competitors": 2
  },
  {
   "entity": "BGaming",
   "competitors": 2
  },
  {
   "entity": "Crash Pirate Casino",
   "competitors": 1
  },
  {
   "entity": "RNG",
   "competitors": 1
  },
  {
   "entity": "AUD",
   "competitors": 1
  },
  {
   "entity": "PayID",
   "competitors": 1
  },
  {
   "entity": "Nautilus Entertainment Ltd",
   "competitors": 1
  },
  {
   "entity": "Curaçao Gaming Control Board",
   "competitors": 1
  },
  {
   "entity": "GCB",
   "competitors": 1
  },
  {
   "entity": "UKGC",
   "competitors": 1
  },
  {
   "entity": "Google Play",
   "competitors": 1
  },
  {
   "entity": "Gaming",
   "competitors": 1
  },
  {
   "entity": "Instant Win",
   "competitors": 1
  },
  {
   "entity": "USD",
   "competitors": 1
  },
  {
   "entity": "LTC",
   "competitors": 1
  },
  {
   "entity": "Infinite Blackjack",
   "competitors": 1
  },
  {
   "entity": "Apple App Store",
   "competitors": 1
  },
  {
   "entity": "Deposit Match",
   "competitors": 1
  },
  {
   "entity": "ACMA",
   "competitors": 1
  },
  {
   "entity": "Login",
   "competitors": 1
  },
  {
   "entity": "CrashPirate Casino UK",
   "competitors": 1
  },
  {
   "entity": "Account",
   "competitors": 1
  },
  {
   "entity": "CrashPirate",
   "competitors": 1
  },
  {
   "entity": "Table Games",
   "competitors": 1
  },
  {
   "entity": "VIP Club",
   "competitors": 1
  },
  {
   "entity": "EUR",
   "competitors": 1
  },
  {
   "entity": "German",
   "competitors": 1
  },
  {
   "entity": "Finnish",
   "competitors": 1
  },
  {
   "entity": "Norwegian",
   "competitors": 1
  },
  {
   "entity": "Min Deposit",
   "competitors": 1
  },
  {
   "entity": "SSL",
   "competitors": 1
  },
  {
   "entity": "Tech Labs",
   "competitors": 1
  },
  {
   "entity": "Cashier",
   "competitors": 1
  },
  {
   "entity": "Neteller",
   "competitors": 1
  },
  {
   "entity": "Pirate Crash",
   "competitors": 1
  },
  {
   "entity": "Slots",
   "competitors": 1
  },
  {
   "entity": "Wins",
   "competitors": 1
  },
  {
   "entity": "Evolution Gaming",
   "competitors": 1
  },
  {
   "entity": "Lightning Roulette",
   "competitors": 1
  },
  {
   "entity": "Crazy Time",
   "competitors": 1
  },
  {
   "entity": "Salon Privé Baccarat",
   "competitors": 1
  },
  {
   "entity": "VIP",
   "competitors": 1
  },
  {
   "entity": "Promotions",
   "competitors": 1
  },
  {
   "entity": "Casino Game Categories",
   "competitors": 1
  }
 ]
}
