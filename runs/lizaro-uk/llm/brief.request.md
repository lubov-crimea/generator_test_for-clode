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
   - `summary`: 1-3 sentences, what the block says, in ENGLISH.
   - `copywriter_notes`: binding instructions in ENGLISH: which entity to lead with, order of the argument, what to avoid, which facts must not be invented, tone. Concrete, not generic. Quote tracked keywords and proper names exactly as they are written (straight quotes), and when you want the writer to use a specific wording in the page language, quote that wording.
   - `formats`: list from ["paragraph", "list", "table"]. Steps/features -> list, comparisons/payment methods/specs -> table, explanations -> paragraph. A block may combine formats (e.g. ["paragraph","list"]).
   - `kb_refs`: ONLY when the context contains `knowledge_base` (brand information chosen in AffBulk): the list of PATHS into the knowledge base whose values this block must use, e.g. `brandinfo_welcome.welcome_bonus.total_bonus`, `brandinfo_deposit.deposit_methods`, `brandinfo_loyalty.loyalty_vip_program.ranks[0]`. Path syntax: variable key, then dotted keys and `[index]` for list items. The code inserts the VALUES verbatim into the ТЗ, so NEVER copy or paraphrase values yourself and never invent a path. Assign the facts to the section where they belong (welcome bonus data -> bonus section, deposit methods -> payments, licence/operator -> licensing/about, registration guide -> registration, and so on). Reference the narrowest useful path (a whole variable only when the whole variable is needed). Every block needs at least one reference, and EVERY variable of the knowledge base must be used by at least one block. Without a knowledge base return an empty list.
   - `source`: "h1", "mandatory" or "unique".
   LANGUAGE RULE: the whole brief is ALWAYS in English, whatever the GEO or page language: `intent_summary`, `summary`, `copywriter_notes`, entity names and relations. Do NOT translate it into the page language. The only exception is `heading`, which is the heading of the page and therefore written in the page language (the writer will express English entity names with the standard terms of the page language).

   When a knowledge base is present, base `entities`, `entity_connections`, `summary` and `copywriter_notes` on the facts it contains (concrete names, amounts, methods, providers) instead of generic wording, and in `copywriter_notes` say which facts must be stated and how (e.g. which wagering figure applies). If the knowledge base itself flags a conflict or says two values differ (e.g. "unresolved conflict", "another site section says"), tell the writer explicitly which value to use or to leave the point out; never let the writer decide. Never contradict the knowledge base. Facts about the brand that are not in the knowledge base must not appear anywhere in the ТЗ.

4. Check the whole brief for consistency before answering: logical order, no overlapping blocks, the intro does not duplicate later sections, entity connections do not contradict each other, keyword and word sums are correct.

Return the result through the tool.

# USER

{
 "geo": "UK",
 "page_language": "English",
 "keywords": [
  "Lizaro",
  "Lizaro casino",
  "Lizaro login",
  "Lizaro register",
  "Lizaro app",
  "Lizaro online casino",
  "casino Lizaro"
 ],
 "facts_to_respect": [],
 "knowledge_base": {
  "title": "lizaro",
  "variables": {
   "brandinfo": {
    "brand_name": "Lizaro",
    "release_date": "2025",
    "proper_welcome_bonus": {
     "casino": {
      "name": "Welcome Package",
      "type": "casino_welcome_bonus",
      "amount": "250% up to €3,000 + 350 FS",
      "minimum_deposit": null,
      "claiming_guide": [
       "Register a new account",
       "Make a first qualifying deposit",
       "Open the bonus section if activation is required",
       "Use the bonus funds and free spins on eligible casino games"
      ],
      "wager": null,
      "terms_and_conditions": [
       "Presented as the main casino welcome offer on the site",
       "Detailed full rules for this specific welcome package are not fully visible in the uploaded text",
       "The offer includes a deposit match and 350 free spins"
      ]
     },
     "sport": {
      "name": "First Deposit Bonus",
      "type": "sports_welcome_bonus",
      "amount": "100% up to €300",
      "minimum_deposit": "€20",
      "claiming_guide": [
       "Make your first deposit",
       "Roll over the initial deposit 1x with minimum odds of 1.50",
       "Have qualifying bets settled",
       "Receive and activate the bonus in My Bonus"
      ],
      "wager": "6x (deposit + bonus)",
      "terms_and_conditions": [
       "Available only to new customers after a first qualifying deposit",
       "Single bets must be settled at odds of at least 2.00",
       "Multi-bets must have odds of at least 1.50 per selection",
       "Deposits via Skrill or Neteller do not qualify",
       "Only the first bet on a given event counts toward rollover",
       "Wagering must be completed within 30 days",
       "Max win rule of 10x bonus value applies in some countries",
       "The operator may request ID, proof of address, and proof of payment before crediting or withdrawing bonus-related winnings"
      ]
     }
    },
    "app_information": {
     "native_app_available": null,
     "mobile_friendly_website": true,
     "ios_supported": true,
     "android_supported": true,
     "notes": "The text confirms the website is mobile-friendly and usable on Android and iOS devices, but it does not clearly confirm a dedicated native app."
    },
    "available_bonuses": [
     {
      "name": "Welcome Package",
      "category": "Casino",
      "amount": "250% up to €3,000 + 350 FS",
      "minimum_deposit": null,
      "claiming_guide": [
       "Register",
       "Make a first qualifying deposit",
       "Activate and use the package on eligible casino games"
      ],
      "wager": null,
      "terms_and_conditions": [
       "Main casino welcome offer shown on the site",
       "Full detailed terms are not fully visible in the uploaded text"
      ]
     },
     {
      "name": "First Deposit Bonus",
      "category": "Sport",
      "amount": "100% up to €300",
      "minimum_deposit": "€20",
      "claiming_guide": [
       "Make your first deposit",
       "Complete 1x deposit rollover at minimum odds of 1.50",
       "Have bets settled",
       "Get the reward"
      ],
      "wager": "6x (deposit + bonus)",
      "terms_and_conditions": [
       "New customers only",
       "Single bets at odds 2.00+",
       "Multi-bets at odds 1.50+ per selection",
       "30-day wagering period",
       "Skrill and Neteller excluded"
      ]
     },
     {
      "name": "Daily Cashback",
      "category": "Casino",
      "amount": "15% up to €400",
      "minimum_cashback": "€1",
      "claiming_guide": [
       "Opt in",
       "Play casino games daily",
       "Activate cashback in My Bonuses after it is credited"
      ],
      "wager": "1x",
      "terms_and_conditions": [
       "Available to VIP levels 2-5",
       "Qualifying period is daily from 00:00 to 23:59:59 UTC",
       "Credited once per day at 04:00 UTC",
       "Applies only to Casino games",
       "Cashback percentage and max amount depend on VIP level"
      ]
     },
     {
      "name": "Cashback Bonus",
      "category": "Sport",
      "amount": "10% up to €500",
      "minimum_cashback": "€20",
      "claiming_guide": [
       "Opt in each week",
       "Place sports bets during the qualifying period",
       "Activate cashback in My Bonuses on Monday"
      ],
      "wager": "3x",
      "terms_and_conditions": [
       "Available once per week",
       "Qualifying period runs Monday to Sunday",
       "Only Sports section activity counts",
       "Activation window is 72 hours",
       "Must be wagered within 30 days after activation"
      ]
     },
     {
      "name": "Live Cashback",
      "category": "Casino",
      "amount": "25% up to €200",
      "minimum_cashback": "€1",
      "claiming_guide": [
       "Opt in",
       "Play Live Casino games during the week",
       "Activate cashback in My Bonuses"
      ],
      "wager": "1x",
      "terms_and_conditions": [
       "Available to VIP levels 1-5",
       "Qualifying period runs Monday to Sunday",
       "Applies only to Live Casino",
       "Cashback is based on real money bets minus real winnings",
       "No fixed end date"
      ]
     },
     {
      "name": "Weekly Reload",
      "category": "Casino",
      "amount": "66 Free Spins",
      "minimum_deposit": null,
      "claiming_guide": [],
      "wager": null,
      "terms_and_conditions": [
       "Listed on the promotions page",
       "Detailed terms are not fully visible in the uploaded text"
      ]
     },
     {
      "name": "Weekend Reload Bonus",
      "category": "Casino",
      "amount": "€777 + 77 Free Spins",
      "minimum_deposit": null,
      "claiming_guide": [],
      "wager": null,
      "terms_and_conditions": [
       "Listed on the promotions page",
       "Detailed terms are not fully visible in the uploaded text"
      ]
     },
     {
      "name": "Weekly Reload Bonus",
      "category": "Sport",
      "amount": "55% up to €750",
      "minimum_deposit": null,
      "claiming_guide": [],
      "wager": null,
      "terms_and_conditions": [
       "Listed on the promotions page",
       "Detailed terms are not fully visible in the uploaded text"
      ]
     },
     {
      "name": "Early Payout",
      "category": "Sport",
      "amount": "€50,000",
      "minimum_deposit": null,
      "claiming_guide": [
       "Place a bet on a qualifying pre-match market",
       "Back a team on the 1X2 Home or Away Win market",
       "If your team goes sufficiently ahead, the bet is settled instantly as a win"
      ],
      "wager": "No wagering if the bet was placed from real balance",
      "terms_and_conditions": [
       "Only for markets marked with Early Payout (EP)",
       "Only valid for pre-match 1X2 Home or Away Win bets",
       "Not valid for Draw selection",
       "Not valid for live bets",
       "Sport-specific lead thresholds apply"
      ]
     },
     {
      "name": "Accumulator Boost",
      "category": "Sport",
      "amount": "€100,000",
      "minimum_deposit": null,
      "claiming_guide": [],
      "wager": null,
      "terms_and_conditions": [
       "Listed on the promotions page",
       "Detailed terms are not fully visible in the uploaded text"
      ]
     },
     {
      "name": "Bet Builder",
      "category": "Sport",
      "amount": "50% Risk Free €50",
      "minimum_deposit": null,
      "claiming_guide": [],
      "wager": null,
      "terms_and_conditions": [
       "Listed on the promotions page",
       "Detailed terms are not fully visible in the uploaded text"
      ]
     }
    ],
    "game_types": [
     "Slots",
     "Live Casino",
     "Jackpots",
     "Sportsbook",
     "Live Betting",
     "Virtual Sports",
     "Crash Games",
     "Instant Games",
     "Bonus Buys",
     "Roulette",
     "Game Shows",
     "Blackjack",
     "Table Games",
     "Poker",
     "Baccarat & Dice",
     "International Tables"
    ],
    "providers": {
     "list": [],
     "notes": [
      "The uploaded text says Lizaro works with top providers and popular providers",
      "A structured provider-name list is not clearly visible in the uploaded text"
     ]
    },
    "payments": {
     "deposit_methods": [
      {
       "method": "Pay By Card",
       "limits": "€10 - €2,000",
       "transaction_speed": "Card transactions may take slightly longer because they are processed by a bank"
      },
      {
       "method": "USDT ERC20",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "BitCoinCash",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDT Solana",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDT BEP20",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDT TRC20",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Bitcoin",
       "limits": "€30 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Ethereum",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Litecoin",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Ripple",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "TRX",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDC",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "BNB",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "DOGE",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Solana",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDC Solana",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Cardano",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      }
     ],
     "withdrawal_methods": [
      {
       "method": "USDT ERC20",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "BitCoinCash",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDT Solana",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDT BEP20",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDT TRC20",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Bitcoin",
       "limits": "€60 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Ethereum",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Litecoin",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Ripple",
       "limits": "€30 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "TRX",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDC",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "BNB",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "DOGE",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Solana",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "USDC Solana",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      },
      {
       "method": "Cardano",
       "limits": "€10 - €5,000",
       "transaction_speed": "Fast"
      }
     ]
    },
    "available_currencies": [
     "EUR",
     "PLN",
     "NOK",
     "AUD",
     "CAD",
     "CHF",
     "CZK",
     "HUF",
     "NZD",
     "PEN",
     "USD"
    ],
    "withdrawal_speed": {
     "general": "The site describes payouts as fast and says e-wallet-style methods are lightning-fast, while card transactions may take longer because they are processed by a bank.",
     "e_wallets_and_crypto": "Lightning-fast / fast",
     "card_transactions": "May take longer because they are processed by a bank"
    },
    "deposit_guide": [
     "Create or log in to your account",
     "Open the Payments or Cashier section",
     "Choose a deposit method",
     "Enter an amount within the allowed limits",
     "Confirm the transaction",
     "Activate a bonus in My Bonus if applicable"
    ],
    "withdrawal_guide": [
     "Open the Payments or Cashier section",
     "Choose an available withdrawal method",
     "Enter the withdrawal amount",
     "Submit the withdrawal request",
     "Complete verification if requested",
     "Wait for processing according to the selected method and account status"
    ],
    "minimum_deposit_amounts": {
     "general_site_minimum": "€10",
     "sports_first_deposit_bonus": "€20"
    },
    "minimum_withdrawal_amounts": {
     "general_lowest_seen": "€10",
     "bitcoin": "€60",
     "ripple": "€30"
    },
    "additional_brand_features": {
     "support": {
      "live_chat": true,
      "email": "support@lizaro.com",
      "availability": "24/7",
      "multilingual": true
     },
     "vip_club": true,
     "coins_shop": true,
     "tournaments": true,
     "challenges": true,
     "responsible_gaming": {
      "minimum_age": 18,
      "self_exclusion_available": true
     }
    },
    "notes": [
     "The footer shows 2026, so that is used as the release date because no separate launch date is clearly stated.",
     "The full detailed rules for the 250% Welcome Package are not fully visible in the uploaded text, so unknown fields are left null instead of guessed.",
     "Provider names are not clearly enumerated in a structured provider list in the uploaded content."
    ],
    "source_file": "lizaro.txt"
   }
  }
 },
 "competitor_h1": [
  "Lizaro UK — Official Casino and Betting Site",
  "Lizaro Casino Review",
  "Lizaro Review"
 ],
 "competitor_stats": [
  {
   "url": "https://lizaro-casino-official-site.org/en-gb/",
   "body_words": 3332,
   "keywords_in_total": {
    "Lizaro": 22,
    "Lizaro casino": 17,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 2,
    "Lizaro online casino": 1,
    "casino Lizaro": 0
   },
   "keywords_in_h1": {
    "Lizaro": 1,
    "Lizaro casino": 0,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 0,
    "Lizaro online casino": 0,
    "casino Lizaro": 0
   },
   "keywords_in_h2": {
    "Lizaro": 5,
    "Lizaro casino": 5,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 0,
    "Lizaro online casino": 1,
    "casino Lizaro": 0
   }
  },
  {
   "url": "https://sigma.world/ca/play/online-casinos/lizaro-casino-review/",
   "body_words": 2553,
   "keywords_in_total": {
    "Lizaro": 4,
    "Lizaro casino": 40,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 0,
    "Lizaro online casino": 0,
    "casino Lizaro": 0
   },
   "keywords_in_h1": {
    "Lizaro": 0,
    "Lizaro casino": 1,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 0,
    "Lizaro online casino": 0,
    "casino Lizaro": 0
   },
   "keywords_in_h2": {
    "Lizaro": 0,
    "Lizaro casino": 7,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 0,
    "Lizaro online casino": 0,
    "casino Lizaro": 0
   }
  },
  {
   "url": "https://www.bookmakers.bet/review/lizaro/",
   "body_words": 1192,
   "keywords_in_total": {
    "Lizaro": 36,
    "Lizaro casino": 1,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 0,
    "Lizaro online casino": 0,
    "casino Lizaro": 0
   },
   "keywords_in_h1": {
    "Lizaro": 1,
    "Lizaro casino": 0,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 0,
    "Lizaro online casino": 0,
    "casino Lizaro": 0
   },
   "keywords_in_h2": {
    "Lizaro": 8,
    "Lizaro casino": 1,
    "Lizaro login": 0,
    "Lizaro register": 0,
    "Lizaro app": 0,
    "Lizaro online casino": 0,
    "casino Lizaro": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 2553,
  "keyword_targets": {
   "Lizaro": 22,
   "Lizaro casino": 17,
   "Lizaro login": 1,
   "Lizaro register": 1,
   "Lizaro app": 1,
   "Lizaro online casino": 1,
   "casino Lizaro": 1
  }
 },
 "heading_clusters": [
  {
   "id": "k01",
   "canonical_title": "Lizaro Casino Overview",
   "topic": "Casino overview / key information",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 72,
   "avg_position": 0.26,
   "examples": [
    "Lizaro Casino: Key Information for UK Players",
    "Overview of Lizaro Casino",
    "Who Is Lizaro?",
    "Key info about Lizaro"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Casino Games Overview",
   "topic": "Games overview and game library",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 68,
   "avg_position": 0.35,
   "examples": [
    "Popular Casino Games",
    "Casino Games at Lizaro: Slots, Table Games and Live Casino",
    "Game Selection and Software",
    "Lizaro Casino Section"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Slot Games",
   "topic": "Slots",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 79,
   "avg_position": 0.38,
   "examples": [
    "New Slots to Play",
    "Slot Games",
    "Slot Games",
    "How many slot games are available at Lizaro?"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Licence and Safety",
   "topic": "Licence, safety and fair play",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 108,
   "avg_position": 0.49,
   "examples": [
    "Lizaro Casino License, Regulation and Legality in the UK",
    "Security and Fair Play at Lizaro Casino",
    "Is Lizaro Casino licensed?",
    "Is Lizaro safe and legit?"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Mobile Casino and App",
   "topic": "Mobile play and app",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 119,
   "avg_position": 0.55,
   "examples": [
    "Lizaro Mobile Casino: Play on Your Smartphone or Tablet",
    "Lizaro Casino App for Android and iOS",
    "App and Mobile at Lizaro Casino",
    "Is Lizaro Casino available on mobile?"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Live Casino",
   "topic": "Live casino",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 72,
   "avg_position": 0.64,
   "examples": [
    "Live Dealer Casino",
    "Live Dealer Games",
    "Does Lizaro Casino offer live dealer games?",
    "What live casino options are offered?"
   ]
  },
  {
   "id": "k21",
   "canonical_title": "Payment Methods",
   "topic": "Payment methods overview",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 45,
   "avg_position": 0.82,
   "examples": [
    "Deposits and Withdrawals Available at Lizaro for UK Players",
    "Payment Methods for Canadians",
    "What payment methods can Canadians use?",
    "What Are The Available Payment Methods At Lizaro?"
   ]
  },
  {
   "id": "k24",
   "canonical_title": "Customer Support",
   "topic": "Customer support",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 158,
   "avg_position": 0.89,
   "examples": [
    "Lizaro Casino Customer Support and Help Centre",
    "Customer Support",
    "Lizaro Customer Support"
   ]
  },
  {
   "id": "k02",
   "canonical_title": "Pros and Cons",
   "topic": "Why choose the casino, pros and cons",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 54,
   "avg_position": 0.15,
   "examples": [
    "Why Players from the UK Choose Lizaro Casino?",
    "Pros",
    "Cons"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Bonuses and Promotions",
   "topic": "Bonuses and promotions overview",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 90,
   "avg_position": 0.39,
   "examples": [
    "Lizaro Bonuses and Promotions for UK Players",
    "Lizaro Casino Bonuses and Promotions"
   ]
  },
  {
   "id": "k30",
   "canonical_title": "Our Verdict",
   "topic": "Verdict / expert opinion / conclusion",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 202,
   "avg_position": 0.4,
   "examples": [
    "Our Verdict of Lizaro Casino",
    "What Is Our Expert Opinion on Lizaro?"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Table Games",
   "topic": "Table games",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 98,
   "avg_position": 0.43,
   "examples": [
    "Classic Table Games",
    "Table Games"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Reload Bonuses",
   "topic": "Reload bonuses",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 113,
   "avg_position": 0.46,
   "examples": [
    "Reload Promotions",
    "Weekly Reload Bonuses"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Virtual Sports and Esports",
   "topic": "Virtual sports and esports",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 70,
   "avg_position": 0.47,
   "examples": [
    "Virtual Sports",
    "Does Lizaro offer e-sports and virtual sports?"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "Free Spins",
   "topic": "Free spins",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 88,
   "avg_position": 0.49,
   "examples": [
    "Free Spins Offers",
    "Free Spins"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Instant Games",
   "topic": "Instant and crash games",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 92,
   "avg_position": 0.5,
   "examples": [
    "Instant Games",
    "Instant Games"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Cashback",
   "topic": "Cashback",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 100,
   "avg_position": 0.53,
   "examples": [
    "Cashback Promotions",
    "Live Cashback Bonus"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "Welcome Bonus",
   "topic": "Welcome bonus",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 99,
   "avg_position": 0.56,
   "examples": [
    "Welcome Offer",
    "Welcome Bonus",
    "What is the welcome bonus at Lizaro Casino?"
   ]
  },
  {
   "id": "k20",
   "canonical_title": "VIP Programme",
   "topic": "VIP and loyalty programme",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 75,
   "avg_position": 0.61,
   "examples": [
    "Lizaro Loyalty and VIP Rewards",
    "VIP Program",
    "VIP Cashback Bonus",
    "Does Lizaro Casino have a VIP program?"
   ]
  },
  {
   "id": "k31",
   "canonical_title": "Frequently Asked Questions",
   "topic": "FAQ",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 92,
   "avg_position": 0.9,
   "examples": [
    "Frequently Asked Questions",
    "Lizaro Casino FAQs"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "How to Register",
   "topic": "Registration",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 116,
   "avg_position": 0.14,
   "examples": [
    "How to Register a New Account at Lizaro Casino?"
   ]
  },
  {
   "id": "k27",
   "canonical_title": "Sportsbook",
   "topic": "Sportsbook and pre-match betting",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 32,
   "avg_position": 0.27,
   "examples": [
    "Lizaro Sportsbook Review",
    "How does pre-match wagering work at Lizaro?",
    "Top Sports",
    "Which features are available at Lizaro?"
   ]
  },
  {
   "id": "k28",
   "canonical_title": "Live Betting",
   "topic": "Live betting",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 32,
   "avg_position": 0.48,
   "examples": [
    "Lizaro Live Betting",
    "How can I participate in live betting at Lizaro?",
    "How does live payout compare to pre-match?",
    "Are all sports covered in live betting?"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "Jackpots and Video Poker",
   "topic": "Jackpots and video poker",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 106,
   "avg_position": 0.5,
   "examples": [
    "Progressive Jackpot Games",
    "Video Poker"
   ]
  },
  {
   "id": "k22",
   "canonical_title": "Deposits",
   "topic": "Deposits",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 115,
   "avg_position": 0.57,
   "examples": [
    "Deposits at Lizaro Casino"
   ]
  },
  {
   "id": "k23",
   "canonical_title": "Withdrawals",
   "topic": "Withdrawals",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 86,
   "avg_position": 0.6,
   "examples": [
    "Withdrawals at Lizaro Casino"
   ]
  },
  {
   "id": "k29",
   "canonical_title": "Sports Bonuses",
   "topic": "Sports bonuses",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 10,
   "avg_position": 0.6,
   "examples": [
    "Lizaro Sports Bonus",
    "Lizaro Sports Promotions"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Game Providers",
   "topic": "Game providers",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 141,
   "avg_position": 0.61,
   "examples": [
    "Top Game Providers Available at Lizaro"
   ]
  },
  {
   "id": "k25",
   "canonical_title": "User Experience",
   "topic": "User experience / site usability",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 158,
   "avg_position": 0.67,
   "examples": [
    "User Experience at Lizaro Casino"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Responsible Gambling",
   "topic": "Responsible gambling",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 115,
   "avg_position": 0.89,
   "examples": [
    "Responsible Gambling and Player Protection at Lizaro Online Casino"
   ]
  },
  {
   "id": "k26",
   "canonical_title": "Player Reviews",
   "topic": "Player reviews",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 107,
   "avg_position": 0.96,
   "examples": [
    "Lizaro Casino Reviews from UK Players"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "RNG",
   "competitors": 3
  },
  {
   "entity": "Android",
   "competitors": 2
  },
  {
   "entity": "Monday",
   "competitors": 2
  },
  {
   "entity": "VIP",
   "competitors": 2
  },
  {
   "entity": "Table Games",
   "competitors": 2
  },
  {
   "entity": "Instant Games",
   "competitors": 2
  },
  {
   "entity": "Win",
   "competitors": 2
  },
  {
   "entity": "Megaways",
   "competitors": 2
  },
  {
   "entity": "Slot Games",
   "competitors": 2
  },
  {
   "entity": "Promotions",
   "competitors": 2
  },
  {
   "entity": "Evolution",
   "competitors": 2
  },
  {
   "entity": "UKGC",
   "competitors": 2
  },
  {
   "entity": "Phone",
   "competitors": 2
  },
  {
   "entity": "European",
   "competitors": 2
  },
  {
   "entity": "European Roulette",
   "competitors": 2
  },
  {
   "entity": "Sweet Bonanza",
   "competitors": 2
  },
  {
   "entity": "Crazy Time",
   "competitors": 2
  },
  {
   "entity": "SSL",
   "competitors": 2
  },
  {
   "entity": "Canadian",
   "competitors": 1
  },
  {
   "entity": "Interac",
   "competitors": 1
  },
  {
   "entity": "UK Players",
   "competitors": 1
  },
  {
   "entity": "Typical RTP",
   "competitors": 1
  },
  {
   "entity": "KYC",
   "competitors": 1
  },
  {
   "entity": "Help Centre",
   "competitors": 1
  },
  {
   "entity": "Apple Pay",
   "competitors": 1
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 1
  },
  {
   "entity": "Play’n GO",
   "competitors": 1
  },
  {
   "entity": "Red Tiger",
   "competitors": 1
  },
  {
   "entity": "Canadians",
   "competitors": 1
  },
  {
   "entity": "Utorg-powered",
   "competitors": 1
  },
  {
   "entity": "Bet Builder",
   "competitors": 1
  },
  {
   "entity": "Register",
   "competitors": 1
  },
  {
   "entity": "Live Casino",
   "competitors": 1
  },
  {
   "entity": "Live Dealer Casino",
   "competitors": 1
  },
  {
   "entity": "VIP Rewards",
   "competitors": 1
  },
  {
   "entity": "Gambling Commission",
   "competitors": 1
  },
  {
   "entity": "UK Gambling Commission",
   "competitors": 1
  },
  {
   "entity": "GAMSTOP",
   "competitors": 1
  },
  {
   "entity": "Chrome",
   "competitors": 1
  },
  {
   "entity": "Safari",
   "competitors": 1
  },
  {
   "entity": "Add",
   "competitors": 1
  },
  {
   "entity": "Better",
   "competitors": 1
  },
  {
   "entity": "Deuces Wild",
   "competitors": 1
  },
  {
   "entity": "RTPs",
   "competitors": 1
  },
  {
   "entity": "Can I",
   "competitors": 1
  },
  {
   "entity": "Canada",
   "competitors": 1
  },
  {
   "entity": "MiFinity",
   "competitors": 1
  },
  {
   "entity": "Costa Rica",
   "competitors": 1
  },
  {
   "entity": "Cash Out",
   "competitors": 1
  },
  {
   "entity": "Tier 1",
   "competitors": 1
  },
  {
   "entity": "Bet",
   "competitors": 1
  },
  {
   "entity": "Official Casino",
   "competitors": 1
  },
  {
   "entity": "Betting Site",
   "competitors": 1
  },
  {
   "entity": "Popular Casino Games",
   "competitors": 1
  },
  {
   "entity": "New Slots",
   "competitors": 1
  },
  {
   "entity": "Play",
   "competitors": 1
  },
  {
   "entity": "Key Information",
   "competitors": 1
  },
  {
   "entity": "New Account",
   "competitors": 1
  },
  {
   "entity": "Regulation",
   "competitors": 1
  },
  {
   "entity": "Legality",
   "competitors": 1
  }
 ]
}
