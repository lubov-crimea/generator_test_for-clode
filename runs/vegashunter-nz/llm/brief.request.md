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
   - `words_min` / `words_max`: allowed length of the BODY text (heading excluded). Use competitors' typical section lengths. The range width is about ±12% of the middle (max/min about 1.27; never above 1.8). The sum of all middles must be close to `target_body_words`. The code enlarges a block afterwards when its facts and entities need more room (about 20 words for each fact and each entity, range always ±12% of the new middle), so do not inflate ranges yourself, but keep the number of entities (2-10) and of `kb_refs` per block proportionate to the section length: every fact and every entity must be explainable in about 20 words. A parent heading's own range covers only its own intro text; sub-sections have their own ranges.
   - `keywords`: how many times each keyword must appear in the BODY of this block (heading excluded). Include EVERY keyword, 0 when unused. For every keyword: sum over all blocks + occurrences inside headings must equal `keyword_targets[keyword]` exactly. Counting rules: case-insensitive, whole words, longest match first (an occurrence of "X casino" counts only for "X casino", not also for "X"). Spread them naturally: the brand early (intro) and in key sections, long-tail variants (login, app, register...) in the sections where they belong. Never more than 1 keyword mention per ~15 words in a block.
   - `entities`: 2-10 entities the block must cover, each with `priority` 1-10 (10 = the main entity of the block). Take them from `entity_candidates` and from the topic (payment systems, game providers, regulators, bonus types, technical terms, game types). Use generic names for the brand itself (e.g. "Online Casino"), never the brand name. Entities that are specific facts about the brand (a licence, a payment method, a provider) may be listed only if they appear in `facts_to_respect` or are clearly competitor-wide industry standards; otherwise list the category (e.g. "E-wallets") and let the notes say "name specifics only if given in the brand information".
   - `entity_connections`: 1-4 relations between entities the text must state explicitly, as subject -> relation (a verb phrase) -> object, with `priority` 1-10. Example: Licence -> regulates -> Online Casino [8].
   - `summary`: 1-3 sentences, what the block says, in ENGLISH.
   - `copywriter_notes`: binding instructions in ENGLISH: which entity to lead with, order of the argument, what to avoid, which facts must not be invented, tone. Concrete, not generic. Quote tracked keywords and proper names exactly as they are written (straight quotes), and when you want the writer to use a specific wording in the page language, quote that wording.
   - `listed_entities` (optional): the names, exactly as in `entities`, of the entities that the block only enumerates as items of its list or table (payment systems in a payments table, provider names in a list, game categories in a bulleted list). They are not narrated, so they do not enlarge the block. Leave it empty when the block explains its entities in prose.
   - `formats`: list from ["paragraph", "list", "table"]; a block may combine formats (e.g. ["paragraph","list"]). Rules:
     * Bulleted list: equal items that need no attributes (features, advantages, document types, game categories).
     * Numbered list: a sequence of steps whose order matters (registration, deposit, withdrawal, installation of the app).
     * Table: whenever two or more attributes must be given per item (payment methods with limits and speed, bonus terms, VIP ranks with requirements, pros | cons, support channels with hours and languages).
     * Minimum on every page: the brand fact table (see 3a); a payments table (the block about payment methods or deposits has "table"); a list of the registration steps (the registration block has "list"); a pros and cons table, when the page has such a block (any block about pros and cons or advantages and disadvantages has "table" with the columns pros | cons).
     * Everything else is prose ("paragraph"): do not turn facts that can be explained in a sentence or two into a list or a table.
   - `kb_refs`: ONLY when the context contains `knowledge_base` (brand information chosen in AffBulk): the list of PATHS into the knowledge base whose values this block must use, e.g. `brandinfo_welcome.welcome_bonus.total_bonus`, `brandinfo_deposit.deposit_methods`, `brandinfo_loyalty.loyalty_vip_program.ranks[0]`. Path syntax: variable key, then dotted keys and `[index]` for list items. The code inserts the VALUES verbatim into the ТЗ, so NEVER copy or paraphrase values yourself and never invent a path. Assign the facts to the section where they belong (welcome bonus data -> bonus section, deposit methods -> payments, licence/operator -> licensing/about, registration guide -> registration, and so on). Reference the narrowest useful path (a whole variable only when the whole variable is needed). Every block needs at least one reference, and EVERY variable of the knowledge base must be used by at least one block. Without a knowledge base return an empty list.
   - `source`: "h1", "mandatory" or "unique".
   LANGUAGE RULE: the whole brief is ALWAYS in English, whatever the GEO or page language: `intent_summary`, `summary`, `copywriter_notes`, entity names and relations. Do NOT translate it into the page language. The only exception is `heading`, which is the heading of the page and therefore written in the page language (the writer will express English entity names with the standard terms of the page language).

   When a knowledge base is present, base `entities`, `entity_connections`, `summary` and `copywriter_notes` on the facts it contains (concrete names, amounts, methods, providers) instead of generic wording, and in `copywriter_notes` say which facts must be stated and how (e.g. which wagering figure applies). If the knowledge base itself flags a conflict or says two values differ (e.g. "unresolved conflict", "another site section says"), tell the writer explicitly which value to use or to leave the point out; never let the writer decide. Never contradict the knowledge base. Facts about the brand that are not in the knowledge base must not appear anywhere in the ТЗ.

3a. BRAND FACT TABLE (only when the context contains `knowledge_base` and `fact_table_requirements`; mandatory then). The page always carries a short brand fact sheet, like the "Casino Information" table of competitor review pages (company, licence, languages, currencies, payment methods, welcome bonus, minimum deposit, support).
   - Place it as the 2nd or the 3rd block of the page (right after the H1 intro, or after one overview H2): level 2, `formats: ["table"]`, and fill `fact_table`. Only this block has `fact_table`; the rest of the page does not repeat the table.
   - Build the rows from the competitors: `competitor_fact_tables` holds the label | value tables of the competitors and how many competitors use each label. Take the rows that most competitors have and that the knowledge base can fill. Keep the typical order of the competitors (usually company, licence, founded, languages, currencies, payment methods, welcome bonus, minimum deposit, support).
   - These rows are required whatever the competitors have: `licence`, `welcome_bonus`, `cashback`, `currencies`, `languages`, `payment_methods`, `support` (the support e-mail). Also add `company`, `founded` and `min_deposit` when the knowledge base has them, and other rows (`other`) only when most competitors have them and the knowledge base can fill them. At most the number of rows allowed in `fact_table_requirements`; one row per fact, no duplicates.
   - Every row: `key`, a short English `label` (1-3 words, e.g. "Licence", "Welcome bonus", "Cashback", "Support"), and `kb_refs` with the NARROWEST paths whose values give that fact (for example the licence list, `welcome_bonus.total_bonus` plus `total_free_spins`, the cashback of the weekly cashback promotion, the currency list, the languages of customer support, the short payment methods overview, the support e-mail). The code inserts the values verbatim; never copy values yourself. Rows must not contradict the knowledge base: when it flags a conflict (for example two different minimum deposits), say in `copywriter_notes` which value the row uses.
   - The table values are SHORT facts (a figure, a name, a comma-separated list, at most about 12 words), never sentences. Word range: roughly 8-10 words per row.
   - Counting: if a row value contains a tracked keyword (the support e-mail `support@incaspin.com` contains "Incaspin"), the block's `keywords` must allow at least that many occurrences, and `copywriter_notes` says the table prints the e-mail as given.
   - `copywriter_notes` of this block: the table has exactly the rows of `fact_table`, in this order, nothing else; values are short; which source wins on conflicts.

4. Check the whole brief for consistency before answering: logical order, no overlapping blocks, the intro does not duplicate later sections, entity connections do not contradict each other, keyword and word sums are correct.

Return the result through the tool.

# USER

{
 "geo": "NZ",
 "page_language": "English",
 "keywords": [
  "VegasHunter",
  "Vegas Hunter",
  "VegasHunter casino",
  "Vegas Hunter casino"
 ],
 "facts_to_respect": [],
 "knowledge_base": {
  "title": "Vegas Hunter NZ-new",
  "variables": {
   "brandinfo_general": {
    "brand_name": "Vegas Hunter",
    "release_year": 2026,
    "minimum_age": 18,
    "licences": [
     {
      "jurisdiction": "Curaçao",
      "regulator": "Curaçao Gaming Authority",
      "licence_number": "OGL/2024/161/0191",
      "operator": "Stable Tech N.V."
     }
    ],
    "currencies": [
     "NZD",
     "USD",
     "AUD",
     "CAD",
     "NOK"
    ],
    "customer_support": {
     "channels": [
      "24/7 live chat",
      "Email"
     ],
     "email": "support@vegashunter.com",
     "vip_service": "24/7 priority VIP assistance and personal manager",
     "website_language": "English"
    },
    "minimum_deposit": "NZ$20",
    "payment_methods": {
     "deposit": [
      "Visa",
      "Mastercard",
      "MiFinity",
      "Interac",
      "Neteller",
      "Bitcoin (BTC)",
      "Ethereum (ETH)",
      "Litecoin (LTC)",
      "Bitcoin Cash (BCH)",
      "Dogecoin (DOGE)",
      "Tether (USDT)",
      "BNB",
      "Cardano (ADA)",
      "TRON (TRX)"
     ],
     "withdrawal": [
      "Visa",
      "Mastercard",
      "MiFinity",
      "Neteller",
      "Bank Transfer",
      "Bitcoin (BTC)",
      "Ethereum (ETH)",
      "Litecoin (LTC)",
      "Bitcoin Cash (BCH)",
      "Dogecoin (DOGE)",
      "Tether (USDT)"
     ]
    },
    "welcome_bonus_summary": {
     "bonus": "Up to NZ$20,000 + 350 Free Spins",
     "wagering": "40x",
     "minimum_qualifying_deposit": "NZ$20"
    }
   },
   "brandinfo_welcome": {
    "welcome_bonus": {
     "name": "Welcome Package",
     "total_bonus_amount": "NZ$20,000",
     "total_free_spins": 350,
     "wagering_requirement": "40x each credited bonus",
     "minimum_qualifying_deposit": "NZ$20",
     "eligibility": "New players placing qualifying welcome deposits",
     "claiming_procedure": [
      "Register an account",
      "Make a first qualifying deposit to receive the initial reward",
      "For subsequent qualifying deposits, enter the corresponding bonus-specific promotional code before payment"
     ],
     "stages": [
      {
       "reward": "100% up to NZ$10,000 + 200 Free Spins",
       "minimum_deposit": "NZ$20",
       "free_spins_distribution": "40 FS daily for 5 days",
       "free_spins_game": "3 Coin Volcanoes (Booongo)",
       "alternative_game": "Aloha King Elvis (BGaming)",
       "validity": "7 days after credit",
       "maximum_winnings": "10x the bonus amount"
      },
      {
       "reward": "100% up to NZ$4,000",
       "minimum_deposit": "NZ$20",
       "promo_code": "RANGER",
       "validity": "7 days after credit",
       "maximum_winnings": "10x the bonus amount"
      },
      {
       "reward": "75% up to NZ$6,000 + 150 Free Spins",
       "minimum_deposit": "NZ$20",
       "promo_code": "SHERIFF",
       "free_spins_distribution": "50 FS daily for 3 days",
       "free_spins_game": "3 Coin Volcanoes (Booongo)",
       "alternative_game": "Aloha King Elvis (BGaming)",
       "validity": "7 days after credit",
       "maximum_winnings": "10x the bonus amount"
      }
     ],
     "important_terms": [
      "Each qualifying reward is subject to 40x wagering",
      "No maximum bet limit while playing with these bonuses",
      "General and bonus terms apply",
      "The casino may cancel the promotion"
     ]
    }
   },
   "brandinfo_promotions": {
    "other_bonuses": [
     {
      "name": "VIP Welcome Bonus",
      "type": "Casino promotion",
      "reward": "200% up to NZ$5,000 plus 7-day VIP Trial Access",
      "wagering_requirement": "40x",
      "minimum_deposit": "NZ$500",
      "validity": "One-time offer",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Maximum win 10x bonus amount",
       "No maximum bet restriction",
       "VIP trial gives exclusive bonuses, cashback, priority chat and faster payouts"
      ],
      "promo_code": "VIP"
     },
     {
      "name": "Monday Reload",
      "type": "Casino promotion",
      "reward": "50% up to NZ$200",
      "wagering_requirement": "40x",
      "minimum_deposit": "NZ$20",
      "validity": "Mondays 00:00–23:59 UTC; 7 days after credit",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Once per Monday",
       "Maximum win 10x bonus amount",
       "Claimed Free Spins, if awarded, expire after 3 days"
      ],
      "promo_code": "DESERT"
     },
     {
      "name": "Tuesday Reload",
      "type": "Casino promotion",
      "reward": "Up to 220 Free Spins (20 FS for NZ$20, 50 FS for NZ$50, 150 FS for NZ$100)",
      "wagering_requirement": "40x",
      "minimum_deposit": "NZ$20",
      "validity": "Tuesday 00:00–23:59 UTC; bonus 7 days; claimed spins 3 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Each of three deposit tiers once each Tuesday",
       "Coin Strike: Hold and Win (Playson); alternative Fruit Million (BGaming)",
       "Maximum FS winnings 10x resulting bonus funds"
      ],
      "promo_code": "WEST"
     },
     {
      "name": "Wednesday Reload",
      "type": "Casino promotion",
      "reward": "30%, 50% or 100% up to NZ$500",
      "wagering_requirement": "40x",
      "minimum_deposit": "NZ$30",
      "validity": "Wednesdays 00:00–23:59 UTC",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "30% from NZ$30 deposit; 50% from NZ$50; 100% from NZ$100",
       "Once per week",
       "Maximum win 10x bonus amount"
      ],
      "promo_code": "WIN"
     },
     {
      "name": "Friday Reload",
      "type": "Casino promotion",
      "reward": "50 Free Spins for every qualifying deposit",
      "wagering_requirement": "40x",
      "minimum_deposit": "NZ$20",
      "validity": "Fridays 00:00–23:59 UTC; credited bonus 7 days; claimed spins 3 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Unlimited Friday redemptions",
       "Coin Strike: Hold and Win (Playson), alternative Fruit Million (BGaming)",
       "Maximum FS winnings 10x the resulting bonus"
      ],
      "promo_code": "WILD"
     },
     {
      "name": "Weekend Reload",
      "type": "Casino promotion",
      "reward": "25% up to NZ$500 per qualifying deposit",
      "wagering_requirement": "40x",
      "minimum_deposit": "NZ$20",
      "validity": "Saturday and Sunday 00:00–23:59 UTC; 7 days after credit",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Unlimited qualifying deposits during weekend",
       "Maximum win 10x bonus amount"
      ],
      "promo_code": "HIT"
     },
     {
      "name": "Crash & Win 100% Reload",
      "type": "Casino promotion",
      "reward": "100% up to NZ$1,000",
      "wagering_requirement": "2x",
      "minimum_deposit": "NZ$20",
      "validity": "Once a week; claim and wager within 3 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Existing depositor only",
       "Plinko 1–2 and Chicken Road 1–2 eligible",
       "Maximum win 10x bonus amount"
      ],
      "promo_code": "BOOM",
      "wagering_contribution": {
       "Slots": "100%",
       "Instant games including Chicken Road, Plinko and Aviator": "5%",
       "Blackjack, baccarat and Hi-Lo including live versions": "5%",
       "Video poker including live versions": "5%",
       "Roulette and poker": "5%",
       "Other games": "5%"
      }
     },
     {
      "name": "Crash & Win 100 Free Spins",
      "type": "Casino promotion",
      "reward": "100 Free Spins on each qualifying deposit",
      "wagering_requirement": "1x",
      "minimum_deposit": "NZ$20",
      "validity": "Daily unlimited redemptions 00:00–23:59 UTC; claim and wager within 3 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Existing depositor only",
       "Prize game Chicken Road 2",
       "Maximum FS winnings 10x resulting bonus"
      ],
      "promo_code": "DROP",
      "wagering_contribution": {
       "Slots": "100%",
       "Instant games including Chicken Road, Plinko and Aviator": "5%",
       "Blackjack, baccarat and Hi-Lo including live versions": "5%",
       "Video poker including live versions": "5%",
       "Roulette and poker": "5%",
       "Other games": "5%"
      }
     },
     {
      "name": "Crash & Win 50% + 50 Free Spins",
      "type": "Casino promotion",
      "reward": "50% up to NZ$1,000 + 50 Free Spins",
      "wagering_requirement": "2x",
      "minimum_deposit": "NZ$20",
      "validity": "Daily unlimited redemptions 00:00–23:59 UTC; claim and wager within 3 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Existing depositor only",
       "Prize game Chicken Road 2",
       "Maximum win 10x cash bonus; maximum FS win 10x resulting bonus"
      ],
      "promo_code": "PUSH",
      "wagering_contribution": {
       "Slots": "100%",
       "Instant games including Chicken Road, Plinko and Aviator": "5%",
       "Blackjack, baccarat and Hi-Lo including live versions": "5%",
       "Video poker including live versions": "5%",
       "Roulette and poker": "5%",
       "Other games": "5%"
      }
     },
     {
      "name": "Live Boost Bonus",
      "type": "Casino promotion",
      "reward": "50% up to NZ$500",
      "wagering_requirement": "3x",
      "minimum_deposit": "NZ$40",
      "validity": "Once daily; unclaimed bonus expires after 7 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Existing depositor only",
       "Live casino games only",
       "Maximum win 10x bonus amount"
      ],
      "promo_code": "COINS"
     },
     {
      "name": "Daily Live Boost",
      "type": "Casino promotion",
      "reward": "10% up to NZ$500",
      "wagering_requirement": "3x",
      "minimum_deposit": "NZ$75",
      "validity": "Once daily; unclaimed bonus expires after 3 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Existing depositor only",
       "Live casino games only",
       "Maximum win 10x bonus amount"
      ],
      "promo_code": "LIVE"
     },
     {
      "name": "Instant Win Cashback",
      "type": "Casino promotion",
      "reward": "2%–7% of previous-day net losses, up to NZ$1,000",
      "wagering_requirement": "1x",
      "minimum_deposit": "NZ$20 on preceding day",
      "validity": "Claim within 24 hours; valid 1 day after activation",
      "claiming_method": "Make a qualifying deposit and activate the offer in the account",
      "important_terms": [
       "Deposits NZ$20/NZ$50/NZ$100/NZ$200 unlock 2%/3.5%/5%/7%",
       "For Instant Win games only",
       "Available once daily to existing depositors",
       "Maximum win 10x cashback amount"
      ]
     },
     {
      "name": "Player Referral Bonus",
      "type": "Casino promotion",
      "reward": "NZ$100 referral bonus",
      "wagering_requirement": "35x",
      "minimum_deposit": "NZ$20 qualifying deposit by referred player",
      "validity": "30 days after eligible referral",
      "claiming_method": "Make a qualifying deposit and activate the offer in the account",
      "important_terms": [
       "Referred person must create a new account and qualify through a real-money deposit",
       "One reward per eligible referred account",
       "Identity checks and anti-abuse rules apply"
      ]
     },
     {
      "name": "Crypto Bonus",
      "type": "Casino promotion",
      "reward": "7% extra on eligible cryptocurrency deposits",
      "wagering_requirement": "No wagering",
      "minimum_deposit": "Corresponding supported cryptocurrency minimum",
      "validity": "Available on qualifying deposits",
      "claiming_method": "Make a qualifying deposit and activate the offer in the account",
      "important_terms": [
       "Bonus credited automatically on eligible crypto deposits",
       "No stated maximum bonus cap"
      ]
     },
     {
      "name": "Monthly Reload",
      "type": "Casino promotion",
      "reward": "100% up to NZ$450 + 100 Free Spins",
      "wagering_requirement": "40x",
      "minimum_deposit": "NZ$30",
      "validity": "Once per calendar month; use within 7 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Offer requires eligible monthly reload deposit"
      ],
      "promo_code": "MONTHLY"
     },
     {
      "name": "Double Up Spins Tuesday Reload",
      "type": "Casino promotion",
      "reward": "60 Free Spins (30 + 30)",
      "wagering_requirement": "40x first reward; 1x second reward",
      "minimum_deposit": "NZ$30 per qualifying deposit",
      "validity": "Tuesday; 3 days for credited spins",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Two qualifying deposits unlock the separate spin portions"
      ],
      "promo_code": "2UP"
     },
     {
      "name": "Weekly Slots Cashback",
      "type": "Casino promotion",
      "reward": "10% cashback up to NZ$5,250",
      "wagering_requirement": "5x",
      "minimum_deposit": "NZ$75 aggregate weekly deposits",
      "validity": "Calculated weekly; claim within 7 days",
      "claiming_method": "Make a qualifying deposit and activate the offer in the account",
      "important_terms": [
       "Calculated against eligible slot losses during the qualifying week"
      ]
     },
     {
      "name": "Weekend Spin Streak Reload",
      "type": "Casino promotion",
      "reward": "Up to 240 Free Spins",
      "wagering_requirement": "40x",
      "minimum_deposit": "NZ$30 per qualifying day",
      "validity": "Friday through Sunday; claim within 3 days",
      "claiming_method": "Make a qualifying deposit using the offer code",
      "important_terms": [
       "Increasing spin awards for consecutive qualifying days"
      ],
      "promo_code": "SPIN3"
     }
    ],
    "gamification_features": [
     {
      "name": "Lucky Spin",
      "mechanics": "Spin-based prize feature",
      "rewards": "Advertised prizes up to NZ$200,000",
      "access": "Available to eligible registered casino players",
      "limits": "One eligible award per spin",
      "validity": "Rewards subject to their individual claim period"
     },
     {
      "name": "Lucky Box",
      "mechanics": "Mystery-box reward selection",
      "rewards": "Advertised prizes up to NZ$175,000",
      "access": "Eligible logged-in players",
      "limits": "Box rewards determined by offer rules",
      "validity": "Claim within the displayed reward window"
     },
     {
      "name": "Bonus Shop",
      "mechanics": "Earn VHC Coins from eligible real-money wagering and redeem them for rewards",
      "progression": "1 VHC Coin per NZ$30 eligible wagering",
      "rewards": {
       "cash": [
        "NZ$30",
        "NZ$80",
        "NZ$120",
        "NZ$160"
       ],
       "free_spins": [
        100,
        150,
        200,
        300
       ],
       "devices": [
        "Apple Watch Series 10",
        "PlayStation 5",
        "iPhone 17 Pro Max",
        "MacBook Pro M4"
       ],
       "premium_gifts": [
        "Dior x Rimowa suitcase",
        "Van Cleef bracelet",
        "Rolex Datejust 41",
        "Tesla Model S"
       ]
      },
      "access": "Registered players with sufficient VHC Coin balance",
      "limits": "Rewards require the displayed quantity of VHC Coins"
     },
     {
      "name": "Rank Progression",
      "mechanics": "Play and gain rank progress for access to tailored rewards",
      "rewards": "Cashback, special promotions and rank-related privileges",
      "access": "Qualifying play under player account",
      "limits": "Rank benefits vary by eligibility"
     }
    ]
   },
   "brandinfo_loyalty": {
    "loyalty_vip_program": {
     "name": "Vegas Hunter VIP Club",
     "entry_requirement": "NZ$2,500 cumulative deposits",
     "joining_guide": [
      "Register and accumulate eligible deposits totalling NZ$2,500",
      "Await contact from a personal VIP manager within 24 hours",
      "Discuss personalised benefits or request transfer of VIP status from another casino"
     ],
     "vip_levels": [
      {
       "name": "Entry",
       "weekly_withdrawal_limit": "NZ$30,000"
      },
      {
       "name": "Bronze",
       "weekly_withdrawal_limit": "NZ$30,000"
      },
      {
       "name": "Silver",
       "weekly_withdrawal_limit": "NZ$45,000"
      },
      {
       "name": "Gold",
       "weekly_withdrawal_limit": "NZ$45,000"
      },
      {
       "name": "Platinum",
       "weekly_withdrawal_limit": "NZ$60,000"
      },
      {
       "name": "Black",
       "weekly_withdrawal_limit": "NZ$90,000"
      },
      {
       "name": "Supreme",
       "weekly_withdrawal_limit": "Customised"
      }
     ],
     "progression": "VIP status and progression are assessed through account activity and personalised manager review; rank-based perks may vary",
     "benefits": [
      "Personal VIP manager",
      "VIP concierge",
      "24/7 priority multilingual VIP support",
      "Higher cashback",
      "Exclusive bonuses and tournaments",
      "Reduced wagering on selected VIP offers",
      "Faster processing of eligible payments",
      "Individually increased withdrawal limits",
      "Private events, Formula 1, concerts, exhibitions and fashion events",
      "Birthday and holiday gifts",
      "Offline gifts and tailored surprises",
      "Transfer of eligible VIP standing from another casino"
     ]
    }
   },
   "brandinfo_account": {
    "registration": {
     "methods": [
      "Email and password",
      "Google sign-up",
      "Fast Track registration"
     ],
     "required_fields": [
      "Email",
      "Password",
      "Country",
      "Account currency",
      "Acceptance of Terms and Conditions and Privacy Policy",
      "Age confirmation 18+"
     ],
     "steps": [
      "Choose Sign Up",
      "Select email, Google or Fast Track registration",
      "Fill the fields requested for the chosen method",
      "Confirm legal age and acceptance of casino policies",
      "Submit registration and access the account"
     ],
     "restrictions": [
      "One personal account per player",
      "Only eligible adult residents of legally permitted countries"
     ]
    },
    "login": {
     "methods": [
      "Registered email and password",
      "Google account when registered through Google"
     ],
     "procedure": [
      "Open Log In",
      "Enter account credentials or use linked Google authentication",
      "Complete any requested security check"
     ],
     "password_recovery": "Use the account password reset flow and confirm ownership of registered email"
    },
    "verification": {
     "mandatory_triggers": [
      "Cumulative deposits reaching NZ$2,000 equivalent",
      "Cumulative withdrawals reaching NZ$2,000 equivalent",
      "Two or more payment systems used",
      "Casino-initiated security or fraud check"
     ],
     "documents": [
      "Photo of valid identity document",
      "Proof of payment method used for deposit, except crypto",
      "Proof of address when requested",
      "Selfie holding identity document when requested",
      "Selfie with note or live challenge when requested",
      "Source of funds or wealth records when requested"
     ],
     "procedure": [
      "Respond to the account verification request",
      "Submit legible identity and payment proof",
      "Provide supplementary evidence or video verification when requested",
      "Await casino review before affected transactions proceed"
     ],
     "important_terms": [
      "Documents normally use Latin or Cyrillic characters; video verification may be required otherwise",
      "Failure to supply full KYC information within 40 days of request can lead to confiscation of winnings",
      "If unreachable for two weeks after withdrawal request the account may be locked"
     ]
    }
   },
   "brandinfo_responsible_gaming": {
    "responsible_gaming": {
     "minimum_age": 18,
     "tools": [
      {
       "name": "Deposit limits",
       "details": "Request deposit controls through player support or account functions; deposits via Cryptoprocessing cannot be subject to deposit limits"
      },
      {
       "name": "Temporary cooling-off",
       "details": "Request a temporary account break through support; common periods of 24 hours, 7 days or 30 days may be arranged"
      },
      {
       "name": "Self-exclusion",
       "details": "Ask support for gambling-related account exclusion; the request is subject to verification and agreed exclusion period"
      },
      {
       "name": "Voluntary account closure",
       "details": "Ask support to close the account for gambling-control reasons"
      },
      {
       "name": "Session awareness",
       "details": "Players are encouraged to monitor time and spending daily"
      }
     ],
     "setting_procedure": [
      "Contact 24/7 support with the requested responsible-gaming restriction",
      "Provide any account ownership verification requested",
      "Receive confirmation and avoid using the account during an active exclusion"
     ],
     "external_support": [
      "GamCare",
      "Gambling Therapy",
      "Gamblers Anonymous"
     ],
     "minor_protection_tools": [
      "Cyber Patrol",
      "GamBlock",
      "Solid Oak",
      "Net Nanny"
     ],
     "contact": "support@vegashunter.com"
    }
   },
   "brandinfo_games": {
    "game_types": [
     "Slots",
     "Live Casino",
     "Game Shows",
     "Instant Win",
     "Crash Games",
     "Plinko",
     "Dice",
     "Keno",
     "Limbo",
     "Mines",
     "Hi-Lo",
     "Fishing Games",
     "Roulette",
     "Blackjack",
     "Poker",
     "Baccarat",
     "Jackpot Games",
     "Bonus Buy",
     "Megaways",
     "Hold & Win",
     "Sic Bo",
     "Bingo",
     "Andar Bahar",
     "Craps",
     "Lottery"
    ],
    "game_examples": [
     {
      "name": "Aloha King Elvis",
      "provider": "BGaming",
      "rtp": "94.98%",
      "volatility": "Medium-high",
      "maximum_multiplier": "2,000x"
     },
     {
      "name": "3 Coin Volcanoes",
      "provider": "Booongo",
      "rtp": "95.7%",
      "volatility": "High",
      "maximum_multiplier": "2,500x"
     },
     {
      "name": "Coin Strike: Hold and Win",
      "provider": "Playson",
      "rtp": "95.66%",
      "volatility": "Medium",
      "maximum_multiplier": "2,000x"
     },
     {
      "name": "Sugar Rush",
      "provider": "Pragmatic Play",
      "rtp": "96.5%",
      "volatility": "High",
      "maximum_multiplier": "5,000x"
     }
    ],
    "original_games": {
     "has_original_games": false
    },
    "providers": [
     "BGaming",
     "Booongo",
     "Playson",
     "Pragmatic Play",
     "PG Soft",
     "Endorphina",
     "Hacksaw Gaming",
     "Belatra",
     "NetGame",
     "Betsoft"
    ]
   },
   "brandinfo_sportsbook": {
    "sportsbook": {
     "has_sportsbook": false
    }
   },
   "brandinfo_deposit": {
    "deposit_methods": [
     {
      "method": "Visa",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "Instant",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Only payment instruments owned by the player",
       "Availability depends on country and selected account currency"
      ]
     },
     {
      "method": "Mastercard",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "Instant",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Only payment instruments owned by the player",
       "Availability depends on country and selected account currency"
      ]
     },
     {
      "method": "MiFinity",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "Instant",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Only payment instruments owned by the player",
       "Availability depends on country and selected account currency"
      ]
     },
     {
      "method": "Interac",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "Instant",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Only payment instruments owned by the player",
       "Availability depends on country and selected account currency"
      ]
     },
     {
      "method": "Neteller",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "Within 24 hours",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Only payment instruments owned by the player",
       "Availability depends on country and selected account currency"
      ]
     },
     {
      "method": "Bitcoin (BTC)",
      "minimum": "0.0001 BTC",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "BTC"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     },
     {
      "method": "Ethereum (ETH)",
      "minimum": "0.01 ETH",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "ETH"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     },
     {
      "method": "Litecoin (LTC)",
      "minimum": "0.01 LTC",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "LTC"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     },
     {
      "method": "Bitcoin Cash (BCH)",
      "minimum": "0.001 BCH",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "BCH"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     },
     {
      "method": "Dogecoin (DOGE)",
      "minimum": "1 DOGE",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "DOGE"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     },
     {
      "method": "Tether (USDT)",
      "minimum": "0.01 USDT",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "USDT"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     },
     {
      "method": "BNB",
      "minimum": "0.01 BNB",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "BNB"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     },
     {
      "method": "Cardano (ADA)",
      "minimum": "5 ADA",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "ADA"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     },
     {
      "method": "TRON (TRX)",
      "minimum": "10 TRX",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; blockchain network charges may apply",
      "transaction_speed": "Instant following required blockchain confirmation",
      "currencies": [
       "TRX"
      ],
      "important_terms": [
       "Send funds only to the supported coin and network displayed at payment",
       "Crypto deposits are excluded from the fiat deposit-limit feature"
      ]
     }
    ],
    "deposit_guide": [
     "Sign in to the Vegas Hunter account",
     "Open the Deposit or Wallet section",
     "Select a supported payment method and eligible currency",
     "Enter a deposit amount at or above the applicable minimum",
     "Supply card, wallet or crypto transfer details as prompted",
     "Authorize the payment and check the account balance after confirmation"
    ]
   },
   "brandinfo_withdrawal": {
    "withdrawal_methods": [
     {
      "method": "Visa",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "1–3 banking days",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Card payouts require eligible non-corporate cards issued in supported countries",
       "Visa OCT or Mastercard Payment Transfer may be used",
       "Bank issuer may decline the transfer",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Mastercard",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "1–3 banking days",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Card payouts require eligible non-corporate cards issued in supported countries",
       "Visa OCT or Mastercard Payment Transfer may be used",
       "Bank issuer may decline the transfer",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "MiFinity",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "Instant",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Payment account must belong to casino account holder",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Neteller",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No fees charged by the casino",
      "transaction_speed": "Instant for MiFinity; up to 1 day for Neteller",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Payment account must belong to casino account holder",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Bank Transfer",
      "minimum": "NZ$20",
      "maximum": "NZ$5,000",
      "fee": "No casino fee; intermediary bank charges may apply, commonly up to NZ$16 equivalent",
      "transaction_speed": "Within 3 banking days",
      "currencies": [
       "NZD"
      ],
      "important_terms": [
       "Bank transfer payouts are not available in USD",
       "Bank account must be owned by the casino player",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Bitcoin (BTC)",
      "minimum": "0.0002 BTC",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; network fees may apply",
      "transaction_speed": "Instant after release, subject to blockchain confirmation",
      "currencies": [
       "BTC"
      ],
      "important_terms": [
       "Crypto-origin funds are withdrawn to crypto wallets",
       "Payout wallet must be controlled by player",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Ethereum (ETH)",
      "minimum": "0.01 ETH",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; network fees may apply",
      "transaction_speed": "Instant after release, subject to blockchain confirmation",
      "currencies": [
       "ETH"
      ],
      "important_terms": [
       "Crypto-origin funds are withdrawn to crypto wallets",
       "Payout wallet must be controlled by player",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Litecoin (LTC)",
      "minimum": "0.01 LTC",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; network fees may apply",
      "transaction_speed": "Instant after release, subject to blockchain confirmation",
      "currencies": [
       "LTC"
      ],
      "important_terms": [
       "Crypto-origin funds are withdrawn to crypto wallets",
       "Payout wallet must be controlled by player",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Bitcoin Cash (BCH)",
      "minimum": "0.001 BCH",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; network fees may apply",
      "transaction_speed": "Instant after release, subject to blockchain confirmation",
      "currencies": [
       "BCH"
      ],
      "important_terms": [
       "Crypto-origin funds are withdrawn to crypto wallets",
       "Payout wallet must be controlled by player",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Dogecoin (DOGE)",
      "minimum": "1 DOGE",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; network fees may apply",
      "transaction_speed": "Instant after release, subject to blockchain confirmation",
      "currencies": [
       "DOGE"
      ],
      "important_terms": [
       "Crypto-origin funds are withdrawn to crypto wallets",
       "Payout wallet must be controlled by player",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     },
     {
      "method": "Tether (USDT)",
      "minimum": "0.01 USDT",
      "maximum": "NZ$5,000 equivalent",
      "fee": "No fees charged by the casino; network fees may apply",
      "transaction_speed": "Instant after release, subject to blockchain confirmation",
      "currencies": [
       "USDT"
      ],
      "important_terms": [
       "Crypto-origin funds are withdrawn to crypto wallets",
       "Payout wallet must be controlled by player",
       "Each deposit must be wagered 1x before related funds may be withdrawn; otherwise processing charges may apply",
       "Method transaction limits are separate from aggregate weekly/monthly limits",
       "VIP withdrawal-limit exceptions may be granted",
       "{'weekly': 'NZ$7,500', 'monthly': 'NZ$30,000', 'large_payouts': 'Winnings exceeding NZ$30,000 may be paid in monthly instalments up to NZ$30,000; progressive jackpots paid in full'}"
      ]
     }
    ],
    "withdrawal_guide": [
     "Log in to the account",
     "Open the Wallet or Withdrawal section",
     "Choose an available withdrawal method and currency",
     "Enter the requested withdrawal amount and payout details",
     "Complete any requested KYC check",
     "Submit the request and track its status",
     "Receive payment after casino approval and provider processing"
    ]
   },
   "brandinfo_app": {
    "app_information": {
     "android": {
      "native_app": true,
      "installation": [
       "Visit the Vegas Hunter download page",
       "Scan the QR code or select Android download",
       "Download APK from the provided link",
       "Approve installation and open the app"
      ],
      "minimum_os": "Android 8.0",
      "minimum_ram": "1 GB",
      "minimum_storage": "1 GB"
     },
     "ios": {
      "native_app": true,
      "installation": [
       "Open the Vegas Hunter app download page on iPhone or iPad",
       "Scan the iOS QR code",
       "Follow the installation instructions",
       "Open the app and sign in"
      ],
      "minimum_os": "iOS 16.7",
      "minimum_ram": "1 GB",
      "minimum_storage": "1 GB"
     },
     "mobile_web": true,
     "platforms": [
      "Android",
      "iOS",
      "Desktop browser",
      "Mobile browser"
     ],
     "features": [
      "Casino games",
      "Deposits and withdrawals",
      "VIP Club",
      "Bonus Shop",
      "Biometric security",
      "2FA",
      "TLS encryption"
     ]
    }
   },
   "brandinfo_privacy_policy": {
    "privacy_policy": {
     "last_updated": "02.07.2026",
     "data_controller": {
      "company_name": "Stable Tech N.V.",
      "jurisdiction": "Curaçao",
      "contact_email": "support@vegashunter.com"
     },
     "data_collected": {
      "identity_data": [
       "Name",
       "Date of birth",
       "Address"
      ],
      "contact_data": [
       "Contact information"
      ],
      "account_data": [
       "Login information",
       "Preferences",
       "Transaction history"
      ],
      "financial_data": [
       "Bank and card details",
       "Deposit and withdrawal records"
      ],
      "verification_data": [
       "Identity documents",
       "Proof of address"
      ],
      "gaming_activity": [
       "Bets",
       "Games played",
       "Sessions"
      ],
      "technical_data": [
       "IP address",
       "Device",
       "Operating system",
       "Location"
      ],
      "communication_data": [
       "Customer support conversations"
      ],
      "other_data": [
       "Cookies",
       "Browsing and usage information"
      ]
     },
     "data_collection_methods": [
      "Registration",
      "Account usage",
      "Payments",
      "Verification",
      "Gameplay",
      "Support communication",
      "Cookies and third-party services"
     ],
     "data_usage": [
      "Account provision and management",
      "Payment processing",
      "Fraud prevention and AML compliance",
      "Platform security",
      "Customer support",
      "Marketing communications",
      "Service improvement",
      "AI-assisted support workflow and conversation analysis"
     ],
     "legal_basis": {
      "contractual_necessity": "Provide casino service and manage account",
      "legal_obligation": "Gambling, KYC and AML compliance",
      "legitimate_interests": "Security, fraud prevention, service analytics and AI-assisted customer support",
      "consent": "Selected marketing communications and optional services"
     },
     "third_party_sharing": {
      "recipients": [
       "Payment processors",
       "Analytics suppliers",
       "Technology vendors",
       "Conversational AI providers including OpenAI, Anthropic and Gemini",
       "Regulatory and legal authorities"
      ],
      "sharing_purposes": [
       "Payments",
       "Analytics",
       "Technical support",
       "AI-assisted customer service",
       "Legal obligations"
      ]
     },
     "international_transfers": {
      "safeguards": [
       "Standard contractual clauses or similar legally recognised safeguards"
      ]
     },
     "data_retention": {
      "general_retention": "Only as long as necessary for stated purposes",
      "financial_records_retention": "At least 5 years where required by AML rules",
      "identity_document_retention": "At least 5 years where required by AML rules",
      "deletion_conditions": "Secure deletion or anonymisation after applicable retention obligations end"
     },
     "data_security": [
      "Encryption",
      "Access controls",
      "Security monitoring",
      "Restricted access for authorised personnel and service partners"
     ],
     "user_rights": [
      "Access",
      "Correction",
      "Erasure",
      "Restriction",
      "Objection",
      "Data portability",
      "Withdrawal of consent"
     ],
     "privacy_requests": {
      "contact_email": "support@vegashunter.com",
      "identity_confirmation": "May be required before fulfilling a request"
     },
     "cookies_policy": {
      "cookie_purposes": [
       "Website functionality",
       "Remembered preferences",
       "Usage analytics",
       "Relevant offers"
      ],
      "cookie_management": "Manage cookies in browser settings"
     },
     "marketing_communications": {
      "marketing_channels": [
       "Email",
       "Platform notifications"
      ],
      "marketing_consent": "Consent requested when legally required",
      "unsubscribe": "Withdraw consent or change account contact preferences"
     },
     "automated_decision_making": {
      "profiling_activities": [
       "AI-supported analysis of support tickets, customer profiles and conversation patterns"
      ],
      "processing_purposes": [
       "Support workflows",
       "Customer service responses and insights"
      ]
     },
     "minors_privacy": {
      "age_restrictions": "18+",
      "data_deletion": "Information identified as belonging to a minor is deleted immediately"
     },
     "privacy_complaints": {
      "complaint_submission": "Contact customer support at support@vegashunter.com"
     },
     "policy_updates": {
      "notification": "Post updated policy on website and, when appropriate, notify by email or platform message"
     }
    },
    "kyc_aml": {
     "last_updated": "20.05.2026",
     "verification_requirements": {
      "mandatory_verification": "Required on defined activity triggers or when requested by the casino",
      "verification_scope": [
       "Player identity",
       "Payment ownership",
       "Additional risk-based checks"
      ]
     },
     "verification_triggers": [
      "Cumulative deposits NZ$2,000 equivalent including crypto",
      "Cumulative withdrawals NZ$2,000 equivalent including crypto",
      "Use of two or more payment systems",
      "Suspicion of fraud or false documents",
      "Casino-requested checks before withdrawal"
     ],
     "required_documents": {
      "identity_documents": [
       "Photo of valid identity document"
      ],
      "payment_documents": [
       "Photo of payment card",
       "Wallet screenshot",
       "Bank statement"
      ],
      "address_documents": [
       "Utility bill if requested"
      ],
      "additional_documents": [
       "Selfie with identity document",
       "Selfie with special note or live challenge",
       "Source of funds records",
       "Source of wealth records"
      ],
      "document_requirements": [
       "Latin or Cyrillic documents preferred",
       "Video verification may be required for other scripts"
      ],
      "cryptocurrency_exception": "Deposit payment-option proof requirement does not apply to cryptocurrency deposits"
     },
     "verification_process": [
      "Receive and review KYC request",
      "Submit identification and payment ownership evidence",
      "Provide optional supplementary documents as requested",
      "Complete review before restricted withdrawals"
     ],
     "verification_time": {
      "document_submission_deadline": "Complete requested KYC information within 40 days to avoid possible confiscation of winnings",
      "contact_deadline": "Account may be locked if player cannot be reached within 2 weeks of withdrawal request"
     },
     "age_verification": {
      "minimum_age": 18,
      "methods": [
       "Identity document",
       "Phone verification when requested"
      ]
     },
     "identity_verification": [
      "Full name and identity matching",
      "Valid ID photo",
      "Additional selfie or video check if required"
     ],
     "address_verification": [
      "Utility bill if requested"
     ],
     "payment_verification": {
      "ownership_requirements": "Player must use own cards, bank accounts and wallets",
      "third_party_payments": "Prohibited; may lead to account closure and fund confiscation",
      "cryptocurrency_verification": "Proof of the crypto deposit method is exempted from mandatory payment-document rule"
     },
     "source_of_funds": {
      "requirements": "Supporting information may be requested during risk-based checks",
      "accepted_documents": [
       "Bank statements",
       "Income evidence",
       "Transaction records"
      ]
     },
     "source_of_wealth": {
      "requirements": "Additional evidence of overall wealth origin may be requested",
      "accepted_documents": [
       "Income and asset records",
       "Business ownership evidence"
      ]
     },
     "aml_policy": {
      "transaction_monitoring": [
       "Multiple payment instruments",
       "Unusual transactions",
       "Fraud",
       "Chargebacks",
       "Collusion",
       "Forged documents"
      ],
      "funds_transfer_rules": [
       "Prefer withdrawal using original deposit method",
       "Crypto deposits paid out in crypto",
       "Fiat deposits paid out via fiat methods",
       "Fiat-to-crypto exceptions require support approval"
      ],
      "record_keeping": "Transaction and identity records retained in line with legal obligations"
     },
     "enhanced_due_diligence": {
      "edd_triggers": [
       "Unusual activity",
       "Suspicious payments",
       "Risk-based requests for additional identity or funding evidence"
      ]
     },
     "withdrawal_restrictions": {
      "verification_before_withdrawal": "Casino may request KYC even where earlier verification was completed",
      "withdrawal_suspension": "Withdrawals may be held pending satisfactory identity checks"
     },
     "verification_failure": {
      "rejection_reasons": [
       "False data",
       "Incomplete documents",
       "Third-party funding",
       "Forged identification"
      ],
      "failure_consequences": [
       "Withdrawal refusal",
       "Account termination",
       "Potential fund forfeiture after applicable deadlines"
      ]
     },
     "additional_terms": [
      "Gifts and positive manual balance corrections restricted to legitimate player rewards",
      "Suspicious conduct must be reported to support"
     ]
    },
    "terms_conditions": {
     "terms_effective_date": "20.05.2026",
     "last_updated": "20.05.2026",
     "eligibility": {
      "minimum_age": 18,
      "residency_requirements": "Player must reside in a location where online gambling is legal",
      "legal_requirements": "Players must check local legal requirements"
     },
     "restricted_countries": {
      "real_money_deposits_and_play": [
       "USA",
       "UK",
       "China",
       "North Korea",
       "Russia",
       "Iran",
       "Sudan",
       "Syria",
       "Cuba",
       "Belarus",
       "Central African Republic",
       "Libya"
      ],
      "bonus_restriction": [
       "Sweden: bonuses and VIP rewards excluded"
      ],
      "game_specific_restrictions": [
       "NetEnt games are restricted in additional jurisdictions including Australia and multiple European countries",
       "Specific branded NetEnt games have additional territory exclusions",
       "NYX games unavailable to Canadian players"
      ]
     },
     "account_registration": [
      "One personal account per person",
      "Accurate up-to-date registration details",
      "Players cannot share their accounts"
     ],
     "account_rules": [
      "Personal non-commercial use",
      "Account holder responsible for security and activity",
      "No sale or transfer of account, deposits, claims or winnings"
     ],
     "prohibited_activities": [
      "Duplicate accounts",
      "Third-party payments",
      "Collusion and fraud",
      "Forged documents",
      "Chargebacks and false payment disputes",
      "Abusive low-risk roulette strategies",
      "Manipulation of software or game errors",
      "VPN circumvention of supplier restrictions",
      "Promotion abuse"
     ],
     "account_suspension": {
      "suspension_reasons": [
       "Fraud",
       "KYC non-compliance",
       "Account duplication",
       "Terms breaches"
      ],
      "player_funds": "Casino may void promotional winnings, withhold unauthorised payments or refund legitimate account balance net applicable fees"
     },
     "account_closure": {
      "request_method": "Contact player support",
      "balance_treatment": "Subject to legitimate balances, outstanding checks and applicable charges"
     },
     "inactive_accounts": {
      "inactivity_period": "12 consecutive months",
      "dormancy_fees": "NZ$25 per month or remaining balance, whichever is lower",
      "fee_frequency": "Beginning of the month after dormancy and monthly thereafter until reactivation or zero balance",
      "reactivation": "Log in or contact support to reactivate"
     },
     "gaming_rules": {
      "betting_rules": [
       "Players responsible for knowing game rules and RTP",
       "Provider games may be geo-restricted"
      ],
      "game_errors": [
       "Casino may cancel incorrectly accepted bets or re-settle errors",
       "Accidental credits remain casino property and may be reclaimed"
      ],
      "fair_play_rules": [
       "Do not exploit glitches",
       "Report errors immediately"
      ],
      "important_terms": [
       "Game-server records prevail over a conflicting on-screen result"
      ]
     },
     "bonus_general_terms": [
      "Promotions subject to their individual wagering and time restrictions",
      "Promotion abuse can lead to void bonuses and winnings",
      "Casino may withdraw or amend promotional offers"
     ],
     "payment_general_terms": {
      "deposit_rules": [
       "Minimum fiat deposit NZ$20",
       "Payment-method-specific maximum shown in payment flow",
       "Every deposit must be wagered 1x before eligible withdrawal"
      ],
      "withdrawal_rules": [
       "Fiat minimum NZ$20",
       "Method-specific transaction maxima",
       "Payouts may be split into instalments",
       "Aggregate maximum NZ$7,500 weekly and NZ$30,000 monthly, with VIP exceptions",
       "Progressive jackpots are paid in full"
      ],
      "payment_ownership": "Only player-owned payment sources allowed",
      "fees_and_charges": [
       "Casino advertises no standard payment fees",
       "Intermediary bank withdrawal charges may apply",
       "Player bears costs of refunds"
      ],
      "chargebacks": "May result in closure, confiscation or claims for damages",
      "currency_rules": [
       "Internal operating currency NZD",
       "Bank conversion charges may apply",
       "No exchange service or account interest"
      ]
     },
     "complaints_disputes": {
      "contact_channels": [
       "Live chat",
       "support@vegashunter.com"
      ],
      "escalation_procedure": "Escalate from support if not resolved at initial contact",
      "important_terms": [
       "Only original account holder may submit or pursue a complaint",
       "Game server records are final evidence",
       "Claims must be filed within 1 year"
      ]
     },
     "governing_law": {
      "jurisdiction": "Curaçao licensing framework",
      "liability": "Casino disclaims liability for outages, software issues and certain financial losses"
     },
     "terms_updates": {
      "modification_rights": "Casino may amend terms unilaterally",
      "notification": "Significant changes may be communicated by email; players should regularly review the terms"
     },
     "additional_terms": [
      "Refund requests normally within 24 hours of alleged transaction; 30 days for unauthorised account access claims",
      "Refunds normally processed in 5–7 banking days",
      "Bonuses and winnings deducted before calculating a refund",
      "Player may be liable to indemnify casino for losses arising from improper use",
      "Assignment or pledging of casino claims and funds is prohibited"
     ]
    }
   }
  }
 },
 "competitor_h1": [
  "Ultimate Guide to VegasHunter Casino in Australia",
  "VegasHunter Casino NZ: Kiwi Pokies, Crypto Payments & Fast Withdrawals"
 ],
 "competitor_stats": [
  {
   "url": "https://vegashunter-au.com/",
   "body_words": 2121,
   "keywords_in_total": {
    "VegasHunter": 37,
    "Vegas Hunter": 7,
    "VegasHunter casino": 10,
    "Vegas Hunter casino": 3
   },
   "keywords_in_h1": {
    "VegasHunter": 0,
    "Vegas Hunter": 0,
    "VegasHunter casino": 1,
    "Vegas Hunter casino": 0
   },
   "keywords_in_h2": {
    "VegasHunter": 6,
    "Vegas Hunter": 0,
    "VegasHunter casino": 0,
    "Vegas Hunter casino": 2
   }
  },
  {
   "url": "https://vegashunter-nz.com/",
   "body_words": 1607,
   "keywords_in_total": {
    "VegasHunter": 35,
    "Vegas Hunter": 1,
    "VegasHunter casino": 6,
    "Vegas Hunter casino": 0
   },
   "keywords_in_h1": {
    "VegasHunter": 0,
    "Vegas Hunter": 0,
    "VegasHunter casino": 1,
    "Vegas Hunter casino": 0
   },
   "keywords_in_h2": {
    "VegasHunter": 6,
    "Vegas Hunter": 0,
    "VegasHunter casino": 0,
    "Vegas Hunter casino": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 1864,
  "keyword_targets": {
   "VegasHunter": 36,
   "Vegas Hunter": 4,
   "VegasHunter casino": 8,
   "Vegas Hunter casino": 2
  }
 },
 "heading_clusters": [
  {
   "id": "k01",
   "canonical_title": "Casino Overview and Key Features",
   "topic": "Casino overview / why choose",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    4
   ],
   "avg_section_words": 61,
   "avg_position": 0.17,
   "examples": [
    "VegasHunter Online: Discover the Best Gaming Experience",
    "Vegashunter Review",
    "Why More Kiwi Bettors Are Choosing VegasHunter Today",
    "Licensed & Regulated"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Free Spins Offers",
   "topic": "Free spins",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3,
    4
   ],
   "avg_section_words": 46,
   "avg_position": 0.3,
   "examples": [
    "How to Claim 20 Free Spins Special",
    "Free Spins",
    "Free Spins on Selected Slot Games"
   ]
  },
  {
   "id": "k02",
   "canonical_title": "Licensing, Safety and Trust",
   "topic": "Safety, licence, legitimacy",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 91,
   "avg_position": 0.32,
   "examples": [
    "Comprehensive VegasHunter Casino Review: Legitimacy and Trust",
    "Is VegasHunter Legit? Safety Standards for Australian Players",
    "Licensing, Security, and Trust Features Explained"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Registration and Login Guide",
   "topic": "Registration and login",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 87,
   "avg_position": 0.32,
   "examples": [
    "Sign In on Vegas Hunter Casino Website",
    "Secure VegasHunter Casino Registration",
    "VegasHunter Online Casino Login: Step-by-Step Instructions",
    "VegasHunter 7 Login Australia: Mirror Sites and Access Tips"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Welcome Bonus and Promotions",
   "topic": "Welcome bonus and bonus overview",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3,
    4
   ],
   "avg_section_words": 36,
   "avg_position": 0.4,
   "examples": [
    "Exclusive Offers: VegasHunter No Deposit Bonus 2026",
    "VegasHunter Casino Australia Real Money Bonus Codes",
    "Discover VegasHunter Welcome Bonuses and Promotional Rewards",
    "Match Bonus"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Mobile Play and App Access",
   "topic": "Mobile app and mobile play",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3,
    4
   ],
   "avg_section_words": 51,
   "avg_position": 0.47,
   "examples": [
    "Mobile Vegas Hunter Casino on Your Device",
    "Download the Official VegasHunter App for Android and iPhone",
    "Vegas Hunter App Login: Play Your Favorite Games Anywhere",
    "Optimizing the VegasHunter Casino App Login Experience"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Games and Pokies Library",
   "topic": "Games overview and pokies",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 52,
   "avg_position": 0.48,
   "examples": [
    "VegasHunter Pokies: Top Games for Aussie Players",
    "Popular Slots on VegasHunter Site",
    "VegasHunter Online Real Money Gaming Library",
    "Top Real Money Games and Pokies Available at VegasHunter"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "What Players Say",
   "topic": "Player reviews",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 124,
   "avg_position": 0.56,
   "examples": [
    "VegasHunter Reviews: What Real Users Say in 2026",
    "What Our Clients Say"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "Banking Methods and Deposits",
   "topic": "Payments, deposits and banking methods",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3,
    4
   ],
   "avg_section_words": 28,
   "avg_position": 0.7,
   "examples": [
    "Banking Guide: VegasHunter Withdrawal and Deposits",
    "VegasHunter Payments",
    "Banking Methods, Limits, and Payout Speed",
    "Visa & Mastercard"
   ]
  },
  {
   "id": "k20",
   "canonical_title": "Frequently Asked Questions",
   "topic": "FAQ",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3,
    4
   ],
   "avg_section_words": 21,
   "avg_position": 0.91,
   "examples": [
    "VegasHunter FAQ: All Your Questions Answered",
    "What is VegasHunter and how do I start playing?",
    "Is VegasHunter casino legit for real money gambling in Australia?",
    "Where can I find the latest Vegas Hunter casino reviews?"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Bonus Terms and Wagering Requirements",
   "topic": "Bonus terms and wagering",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3,
    4
   ],
   "avg_section_words": 64,
   "avg_position": 0.27,
   "examples": [
    "Wagering",
    "Bonus Rules and Wagering Requirements"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Reload Bonuses and Cashback",
   "topic": "Reload bonuses and cashback",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 62,
   "avg_position": 0.29,
   "examples": [
    "Reload Bonuses and Cashback Deals"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Table Games",
   "topic": "Table games",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 14,
   "avg_position": 0.38,
   "examples": [
    "Table Games"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Live Dealer Games",
   "topic": "Live dealer games",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 17,
   "avg_position": 0.4,
   "examples": [
    "Live Dealer Games"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Crash and Instant Win Games",
   "topic": "Crash and instant win games",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 14,
   "avg_position": 0.43,
   "examples": [
    "Crash & Instant Win"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Loyalty and Rewards",
   "topic": "Loyalty and reward tiers",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 82,
   "avg_position": 0.47,
   "examples": [
    "VegasHunter Casino 13: Exploring Loyalty and Reward Tiers"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Crypto Banking",
   "topic": "Cryptocurrency banking",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    4
   ],
   "avg_section_words": 33,
   "avg_position": 0.54,
   "examples": [
    "Crypto Banking Benefits for New Zealand Players",
    "Bitcoin (BTC)",
    "Ethereum (ETH)",
    "USDT"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "Game Providers and RTP",
   "topic": "Game providers and RTP",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 69,
   "avg_position": 0.62,
   "examples": [
    "VegasHunter Casino Official Site: Game Providers and RTP"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "Withdrawals, Limits and Fees",
   "topic": "Withdrawals, limits and fees",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 72,
   "avg_position": 0.72,
   "examples": [
    "How to Withdraw Money from VegasHunter Quickly and Safely",
    "Understanding VegasHunter AU Transaction Limits and Fees"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Customer Support",
   "topic": "Customer support",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 48,
   "avg_position": 0.83,
   "examples": [
    "Customer Support Options and Help Services"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "Android",
   "competitors": 2
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 2
  },
  {
   "entity": "Curaçao",
   "competitors": 2
  },
  {
   "entity": "Play’n GO",
   "competitors": 2
  },
  {
   "entity": "Free Spins",
   "competitors": 2
  },
  {
   "entity": "Mastercard",
   "competitors": 2
  },
  {
   "entity": "Bitcoin",
   "competitors": 2
  },
  {
   "entity": "Phone",
   "competitors": 2
  },
  {
   "entity": "Slots",
   "competitors": 2
  },
  {
   "entity": "Visa",
   "competitors": 2
  },
  {
   "entity": "BGaming",
   "competitors": 2
  },
  {
   "entity": "Australian",
   "competitors": 1
  },
  {
   "entity": "New Zealand",
   "competitors": 1
  },
  {
   "entity": "Australia",
   "competitors": 1
  },
  {
   "entity": "AUD 10",
   "competitors": 1
  },
  {
   "entity": "Kiwi",
   "competitors": 1
  },
  {
   "entity": "PayID",
   "competitors": 1
  },
  {
   "entity": "RTP",
   "competitors": 1
  },
  {
   "entity": "Gaming",
   "competitors": 1
  },
  {
   "entity": "AUD 2",
   "competitors": 1
  },
  {
   "entity": "POLi",
   "competitors": 1
  },
  {
   "entity": "Dogecoin",
   "competitors": 1
  },
  {
   "entity": "JAZ2020-172",
   "competitors": 1
  },
  {
   "entity": "Evolution Gaming",
   "competitors": 1
  },
  {
   "entity": "GLI",
   "competitors": 1
  },
  {
   "entity": "KYC",
   "competitors": 1
  },
  {
   "entity": "AUD 1",
   "competitors": 1
  },
  {
   "entity": "AML",
   "competitors": 1
  },
  {
   "entity": "Wolf Gold",
   "competitors": 1
  },
  {
   "entity": "AUD 0",
   "competitors": 1
  },
  {
   "entity": "AUD 50",
   "competitors": 1
  },
  {
   "entity": "AUD 20",
   "competitors": 1
  },
  {
   "entity": "Stable Tech N",
   "competitors": 1
  },
  {
   "entity": "Ethereum",
   "competitors": 1
  },
  {
   "entity": "USDT",
   "competitors": 1
  },
  {
   "entity": "Litecoin",
   "competitors": 1
  },
  {
   "entity": "APK",
   "competitors": 1
  },
  {
   "entity": "Ultimate Guide",
   "competitors": 1
  },
  {
   "entity": "Best Gaming Experience",
   "competitors": 1
  },
  {
   "entity": "Trust",
   "competitors": 1
  },
  {
   "entity": "Safety Standards",
   "competitors": 1
  },
  {
   "entity": "Australian Players",
   "competitors": 1
  },
  {
   "entity": "What Real Users Say",
   "competitors": 1
  },
  {
   "entity": "Sign In",
   "competitors": 1
  },
  {
   "entity": "Step-by-Step Instructions",
   "competitors": 1
  },
  {
   "entity": "Mirror Sites",
   "competitors": 1
  },
  {
   "entity": "Access Tips",
   "competitors": 1
  },
  {
   "entity": "Your Device",
   "competitors": 1
  },
  {
   "entity": "Play Your Favorite Games Anywhere",
   "competitors": 1
  },
  {
   "entity": "Exclusive Offers",
   "competitors": 1
  },
  {
   "entity": "Claim 20 Free Spins Special",
   "competitors": 1
  },
  {
   "entity": "Exploring Loyalty",
   "competitors": 1
  },
  {
   "entity": "Reward Tiers",
   "competitors": 1
  },
  {
   "entity": "Top Games",
   "competitors": 1
  },
  {
   "entity": "Aussie Players",
   "competitors": 1
  },
  {
   "entity": "Popular Slots",
   "competitors": 1
  },
  {
   "entity": "Game Providers",
   "competitors": 1
  },
  {
   "entity": "Banking Guide",
   "competitors": 1
  },
  {
   "entity": "Deposits",
   "competitors": 1
  },
  {
   "entity": "Withdraw Money",
   "competitors": 1
  }
 ],
 "fact_table_requirements": {
  "position": "the 2nd or the 3rd block of the page, level 2, formats [\"table\"], `fact_table` rows set",
  "required_row_keys": [
   "licence",
   "welcome_bonus",
   "cashback",
   "currencies",
   "languages",
   "payment_methods",
   "support"
  ],
  "allowed_row_keys": [
   "company",
   "licence",
   "founded",
   "languages",
   "currencies",
   "payment_methods",
   "welcome_bonus",
   "cashback",
   "min_deposit",
   "support",
   "other"
  ],
  "max_rows": 14
 },
 "competitor_fact_tables": {
  "tables": [],
  "labels": []
 }
}
