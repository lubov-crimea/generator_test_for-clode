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
 "geo": "NO",
 "page_language": "Norwegian",
 "keywords": [
  "Cazeus",
  "Cazues casino"
 ],
 "facts_to_respect": [],
 "knowledge_base": {
  "title": "Cazeus-upd",
  "variables": {
   "brandinfo_general": {
    "brand_name": "Cazeus",
    "domain": "cazeus.com",
    "release_year": 2020,
    "minimum_age": "18+",
    "licences": [
     {
      "regulator": "PAGCOR",
      "licence_number": "IGL-24-0021",
      "operator": "Liernin Enterprises Ltd",
      "status": "Historical record; current validity is unconfirmed"
     }
    ],
    "currencies": [
     "EUR",
     "USD",
     "CAD",
     "NOK",
     "HUF",
     "PLN"
    ],
    "overview": {
     "casino_welcome_package": "Up to €1,750 + 150 Free Spins",
     "sports_welcome_bonus": "100% up to €100",
     "minimum_deposit": "€10",
     "welcome_bonus_minimum_deposit": "€20",
     "minimum_withdrawal": "€10",
     "deposit_methods": [
      "Interac",
      "Visa",
      "Mastercard",
      "Paysafecard",
      "Neteller",
      "Cash2Code",
      "MiFinity",
      "Bitcoin",
      "Dogecoin",
      "Tether USDT",
      "Ethereum",
      "Litecoin",
      "Tron",
      "USD Coin",
      "BNB",
      "Solana",
      "Cardano"
     ],
     "withdrawal_methods": [
      "Interac",
      "Visa",
      "Mastercard",
      "Paysafecard",
      "Neteller",
      "Cash2Code",
      "MiFinity",
      "Bitcoin",
      "Dogecoin",
      "Tether USDT",
      "Ethereum",
      "Litecoin",
      "Tron",
      "USD Coin",
      "BNB",
      "Solana",
      "Cardano"
     ],
     "withdrawal_processing": "Up to 3 business days for casino processing, plus payment provider processing time",
     "casino_games": [
      "Slots",
      "Table Games",
      "Live Casino",
      "Live Game Shows",
      "Jackpots",
      "Instant Games"
     ],
     "sportsbook": true,
     "live_betting": true,
     "mobile_app": "No dedicated application; mobile-optimized website",
     "vip_program": "VIP Club with 5 levels",
     "responsible_gaming": "Self-exclusion requests, account closure and external gambling-support resources"
    },
    "customer_support": {
     "email": "support@cazeus.com",
     "live_chat": true,
     "availability": "24/7",
     "help_centre": "https://cazeus.com/en/help-centre/general-information"
    }
   },
   "brandinfo_welcome": {
    "welcome_bonus": {
     "name": "Welcome Package",
     "casino_offer": "Up to €1,750 + 150 Free Spins",
     "maximum_total_bonus": "€1,750",
     "total_free_spins": 150,
     "minimum_qualifying_deposit": "€20",
     "claiming_conditions": [
      "Available to newly registered customers making their first qualifying real-money deposits.",
      "Select the casino welcome package during registration or before making the qualifying deposit.",
      "Activate eligible bonus rewards through the My Bonuses section of the player profile.",
      "Use the qualifying payment method and complete the required deposit transaction.",
      "Only one casino bonus can be active at a time."
     ],
     "wagering_requirement": "(Deposit + bonus) x35",
     "free_spins_wagering_requirement": "Free Spins winnings x40",
     "validity": "10 days from activation for each bonus wagering requirement",
     "free_spins_validity": "7 days from crediting",
     "maximum_bet_during_wagering": "€5 per bet",
     "maximum_bonus_cashout": "10x the credited bonus amount",
     "maximum_free_spins_cashout": "€100",
     "eligible_games": [
      "Eligible online slots"
     ],
     "game_contribution": {
      "slots": "100%",
      "live_games": "10%",
      "table_games": "0%",
      "video_poker": "10%",
      "plinko": "10%"
     },
     "promo_code_required": false,
     "important_terms": [
      "The package is intended for eligible new customers and cannot be claimed repeatedly by the same person, household or shared IP address.",
      "The qualifying deposit must be completed before placing bets with the deposited funds.",
      "Bonus wagering requirements must be completed within the applicable validity period.",
      "Uncompleted bonus wagering requirements result in cancellation of the remaining bonus balance and associated winnings.",
      "Activating another bonus while a casino bonus is active may cancel the existing bonus and its associated winnings.",
      "Jackpot slots, Slingo and Bingo games are excluded from bonus wagering where prohibited by the general bonus rules.",
      "The maximum permitted bet while wagering is €5.",
      "Bonus abuse, fraudulent activity and attempts to guarantee a profit through opposing bets may result in bonus cancellation.",
      "Withdrawals remain subject to account verification and the general withdrawal conditions."
     ]
    }
   },
   "brandinfo_promotions": {
    "other_bonuses": [
     {
      "name": "Weekly Reload",
      "type": "Casino Free Spins",
      "amount": "60 Free Spins",
      "minimum_deposit": "€20",
      "availability": "Monday to Thursday",
      "claiming_method": [
       "Opt in to the promotion each week.",
       "Make the first qualifying weekly deposit of at least €20 between Monday and Thursday.",
       "Activate the Free Spins in the My Bonuses section if required."
      ],
      "wagering_requirement": "Free Spins winnings x40",
      "validity": "Free Spins must be used within 7 days; wagering must be completed within 10 days",
      "maximum_cashout": "€100",
      "maximum_bet_during_wagering": "€5",
      "eligible_games": "A slot selected by the casino",
      "promo_code_required": false,
      "important_terms": [
       "The qualifying deposit must be made before placing bets with the deposited funds.",
       "Free Spins cannot be exchanged for another bonus or transferred to another game.",
       "Uncompleted wagering requirements result in cancellation of the bonus and associated winnings.",
       "The promotion cannot be combined with another active casino bonus."
      ]
     },
     {
      "name": "Weekend Reload Bonus",
      "type": "Casino Deposit Bonus",
      "bonus_percentage": "50%",
      "maximum_bonus": "€800",
      "additional_reward": "80 Free Spins",
      "minimum_deposit": "€20",
      "minimum_deposit_for_free_spins": "€50",
      "availability": "Friday to Sunday",
      "claiming_method": [
       "Opt in to the promotion during the qualifying weekend.",
       "Make the first qualifying weekly weekend deposit.",
       "Activate the promotion through the My Bonuses section."
      ],
      "wagering_requirement": "(Deposit + bonus) x35",
      "free_spins_wagering_requirement": "Free Spins winnings x40",
      "validity": "10 days for bonus wagering; 7 days for Free Spins",
      "maximum_bonus_cashout": "10x the credited bonus amount",
      "maximum_free_spins_cashout": "€100",
      "maximum_bet_during_wagering": "€5",
      "promo_code_required": false,
      "important_terms": [
       "The 50% bonus is available from a qualifying deposit of €20.",
       "The additional 80 Free Spins require a qualifying deposit of at least €50.",
       "The Free Spins are assigned to a slot selected by the casino.",
       "The wagering requirement must be completed within 10 days of activation.",
       "Only one casino bonus can be active at a time.",
       "Uncompleted wagering requirements result in forfeiture of the bonus and associated winnings."
      ]
     },
     {
      "name": "Daily Cashback",
      "type": "Casino Cashback",
      "bonus_percentage": "3%–15%",
      "maximum_bonus": "€400",
      "availability": "Daily",
      "claiming_method": [
       "Opt in to the promotion.",
       "Play eligible casino games using real money.",
       "Open My Bonuses and activate the credited cashback."
      ],
      "wagering_requirement": "Cashback x1",
      "validity": "Cashback is credited daily; activation is required before expiry",
      "eligible_vip_levels": [
       "Level 2",
       "Level 3",
       "Level 4",
       "Level 5"
      ],
      "level_rewards": {
       "Level 2": {
        "cashback_percentage": "3%",
        "maximum_cashback": "€100"
       },
       "Level 3": {
        "cashback_percentage": "5%",
        "maximum_cashback": "€200"
       },
       "Level 4": {
        "cashback_percentage": "10%",
        "maximum_cashback": "€300"
       },
       "Level 5": {
        "cashback_percentage": "15%",
        "maximum_cashback": "€400"
       }
      },
      "minimum_cashback": "€1",
      "promo_code_required": false,
      "important_terms": [
       "Cashback is calculated from real-money casino bets minus real-money winnings.",
       "Bonus funds are excluded from the cashback calculation.",
       "The promotion applies to casino games only.",
       "Cashback must be activated before expiry and wagered once before withdrawal."
      ]
     },
     {
      "name": "Live Cashback",
      "type": "Live Casino Cashback",
      "bonus_percentage": "25%",
      "maximum_bonus": "€200",
      "availability": "Weekly, Monday to Sunday",
      "claiming_method": [
       "Opt in to the promotion.",
       "Play eligible Live Casino games during the qualifying week.",
       "Open My Bonuses on Monday and activate the credited cashback."
      ],
      "wagering_requirement": "Cashback x1",
      "validity": "Weekly qualification period; credited rewards must be activated before expiry",
      "eligible_vip_levels": [
       "Level 1",
       "Level 2",
       "Level 3",
       "Level 4",
       "Level 5"
      ],
      "minimum_cashback": "€1",
      "promo_code_required": false,
      "important_terms": [
       "Cashback is calculated from real-money Live Casino bets minus real-money winnings.",
       "Bonus funds are excluded from the cashback calculation.",
       "The reward is restricted to eligible Live Casino activity.",
       "The cashback must be activated and wagered once before withdrawal."
      ]
     }
    ],
    "gamification_features": [
     {
      "name": "Challenges",
      "type": "Missions and rewards",
      "availability": [
       "One-time challenges",
       "Weekly challenges"
      ],
      "how_it_works": "Players complete eligible tasks and progress through challenge objectives to earn coins and rewards.",
      "possible_rewards": [
       "Cazeus Coins",
       "Bonus Money",
       "Free Spins",
       "Free Bets"
      ],
      "access_method": "Open the Challenges section after logging in.",
      "important_terms": [
       "Individual challenges may have separate eligibility requirements and deadlines.",
       "Rewards are subject to their individual wagering and validity conditions."
      ]
     },
     {
      "name": "Collections",
      "type": "Collection and progression system",
      "availability": "7 collections, each containing 10 collectible cards",
      "how_it_works": "Players accumulate coins, purchase collection cards and receive the reward assigned to each purchased card.",
      "completion_reward": "A cash prize assigned to the completed collection",
      "wagering_requirement": "Cash prizes x1",
      "free_spins_wagering_requirement": "Free Spins winnings x40",
      "free_spins_validity": "7 days",
      "bonus_validity": "10 days for the wagering requirement",
      "access_method": "Open Collections from the main navigation.",
      "important_terms": [
       "Coins are used to purchase collection cards.",
       "Each card has an assigned reward.",
       "Completing a collection awards its assigned cash prize.",
       "Free Spins rewards are subject to their individual maximum cashout limits."
      ]
     },
     {
      "name": "Cazeus Shop",
      "type": "Rewards store",
      "how_it_works": "Exchange accumulated Cazeus Coins for casino bonus money, bonus spins and sportsbook Free Bets.",
      "coin_earning_mechanics": [
       "Earn 1 Coin for every €10 wagered on eligible casino games.",
       "Receive Coins equivalent to 5% of each qualifying deposit.",
       "Coins may also be awarded for tournament participation and qualifying placements."
      ],
      "example_rewards": [
       {
        "reward": "€5 Bonus Money",
        "coin_cost": 300
       },
       {
        "reward": "€10 Bonus Money",
        "coin_cost": 900
       },
       {
        "reward": "€5 Sports Free Bet",
        "coin_cost": 500
       },
       {
        "reward": "€10 Sports Free Bet",
        "coin_cost": 900
       },
       {
        "reward": "€20 Sports Free Bet",
        "coin_cost": 1700
       }
      ],
      "bonus_money_wagering_requirement": "Bonus Money x40",
      "bonus_money_validity": "10 days",
      "bonus_money_maximum_cashout": "5x the original bonus amount",
      "free_spins_wagering_requirement": "Free Spins winnings x40",
      "free_spins_validity": "7 days",
      "free_bet_wagering_requirement": "Free Bet winnings x3 at minimum odds of 2.10 per selection",
      "free_bet_validity": "Activate within 24 hours and complete wagering within 30 days",
      "important_terms": [
       "Casino bonus money can only be used in the Casino section.",
       "Sports Free Bets can only be used in the Sports section.",
       "Free Bet winnings are credited to the real balance after deducting the initial Free Bet stake.",
       "Rewards are subject to their applicable wagering requirements and expiration periods."
      ]
     },
     {
      "name": "Wheel of Fortune",
      "type": "Spin-based reward game",
      "eligibility": "Registered players eligible for promotions",
      "how_it_works": "Players earn spins through eligible casino wagering. Every spin awards a reward.",
      "spin_earning_mechanics": [
       "Earn 1 spin for every €100 wagered on eligible casino games.",
       "A maximum of 3 spins can be earned per day.",
       "A maximum of 10 unused spins can be held at a time.",
       "Wagering with an active bonus does not count toward Wheel of Fortune spins."
      ],
      "possible_rewards": [
       "Cash prizes",
       "Bonus Money",
       "Free Casino Spins"
      ],
      "cash_prize_wagering_requirement": "x1",
      "bonus_money_wagering_requirement": "x40",
      "bonus_money_validity": "7 days",
      "bonus_money_maximum_cashout": "5x the original bonus amount",
      "free_spins_wagering_requirement": "Free Spins winnings x40",
      "free_spins_validity": "7 days",
      "important_terms": [
       "Spins must be activated manually.",
       "Cash prizes are credited to the real balance and require one qualifying wager before withdrawal.",
       "Bonus Money and Free Spins are subject to their respective wagering requirements.",
       "Sportsbook bets do not count toward earning spins unless the promotion explicitly states otherwise."
      ]
     },
     {
      "name": "Drops & Wins",
      "type": "Prize drops and game events",
      "availability": "Daily and weekly promotional events on selected games",
      "how_it_works": "Players participate in eligible games during promotional events for a chance to receive prizes.",
      "possible_rewards": [
       "Bonus Money",
       "Free Spins",
       "Promotional cash rewards"
      ],
      "access_method": "Open the eligible promotion or game event from the casino lobby.",
      "important_terms": [
       "Each event has its own eligible games, entry conditions and reward rules.",
       "Promotional rewards are subject to their applicable terms."
      ]
     }
    ]
   },
   "brandinfo_loyalty": {
    "loyalty_vip_program": {
     "name": "VIP Club",
     "levels": [
      {
       "name": "Level 1",
       "daily_withdrawal_limit": "€500",
       "monthly_withdrawal_limit": "€7,000",
       "benefits": [
        "Access to on-site promotions",
        "24/7 live chat support",
        "Eligibility for Live Cashback"
       ]
      },
      {
       "name": "Level 2",
       "daily_withdrawal_limit": "€500",
       "monthly_withdrawal_limit": "€10,000",
       "benefits": [
        "Access to on-site promotions",
        "24/7 live chat support",
        "Eligibility for Daily Cashback at 3% up to €100",
        "Eligibility for Live Cashback"
       ]
      },
      {
       "name": "Level 3",
       "daily_withdrawal_limit": "€800",
       "monthly_withdrawal_limit": "€12,000",
       "benefits": [
        "Higher withdrawal limits",
        "Access to on-site promotions",
        "24/7 live chat support",
        "Eligibility for Daily Cashback at 5% up to €200",
        "Eligibility for Live Cashback"
       ]
      },
      {
       "name": "Level 4",
       "daily_withdrawal_limit": "€1,000",
       "monthly_withdrawal_limit": "€15,000",
       "benefits": [
        "Personalized offers",
        "Higher withdrawal limits",
        "Personal VIP manager",
        "Access to on-site promotions",
        "Eligibility for Daily Cashback at 10% up to €300",
        "Eligibility for Live Cashback"
       ]
      },
      {
       "name": "Level 5",
       "daily_withdrawal_limit": "€1,500",
       "monthly_withdrawal_limit": "€20,000",
       "benefits": [
        "Personalized offers",
        "Highest VIP withdrawal limits",
        "Personal VIP manager",
        "Access to on-site promotions",
        "Eligibility for Daily Cashback at 15% up to €400",
        "Eligibility for Live Cashback"
       ]
      }
     ],
     "progression": {
      "evaluation_period": "90 calendar days",
      "criteria": [
       "Deposit activity",
       "Withdrawal activity",
       "Bonuses received"
      ],
      "downgrade_rule": "A player who has not actively placed bets for one month is automatically downgraded to Level 1."
     },
     "withdrawal_limits": {
      "currency": "EUR",
      "periods": [
       "Daily",
       "Monthly"
      ],
      "level_1": {
       "daily": "€500",
       "monthly": "€7,000"
      },
      "level_2": {
       "daily": "€500",
       "monthly": "€10,000"
      },
      "level_3": {
       "daily": "€800",
       "monthly": "€12,000"
      },
      "level_4": {
       "daily": "€1,000",
       "monthly": "€15,000"
      },
      "level_5": {
       "daily": "€1,500",
       "monthly": "€20,000"
      }
     },
     "general_benefits": [
      "Higher daily and monthly withdrawal limits at higher VIP levels",
      "Access to eligible on-site promotions",
      "Cashback opportunities",
      "Personalized promotional offers for higher levels",
      "Personal VIP manager at higher levels",
      "24/7 live chat access"
     ]
    }
   },
   "brandinfo_account": {
    "registration": {
     "methods": [
      "Website registration form"
     ],
     "required_information": [
      "Full name",
      "Date of birth",
      "Email address",
      "Phone number",
      "Country",
      "Gender",
      "Username",
      "Postal code",
      "Social security or equivalent identification number where required"
     ],
     "steps": [
      "Open the Cazeus website and select Register.",
      "Complete the registration form using accurate personal information.",
      "Choose the applicable account and welcome-bonus preferences.",
      "Submit the registration form.",
      "Access the player profile and complete any requested account setup steps.",
      "Make a qualifying deposit if required for the selected promotion."
     ],
     "restrictions": [
      "Players must be at least 18 years old and meet the legal age requirement in their jurisdiction.",
      "Only one account is allowed per person, household or address, phone number, email address and IP address.",
      "Accounts must be registered using the player's correct personal details.",
      "Duplicate accounts may be closed, and associated promotions and winnings may be cancelled.",
      "Residents of excluded jurisdictions cannot register or deposit.",
      "Payment methods used for deposits must belong to the account holder."
     ]
    },
    "login": {
     "method": "Use the Log In option on the website.",
     "steps": [
      "Open Cazeus.",
      "Select Log In.",
      "Enter the registered login credentials.",
      "Submit the form to access the player account."
     ],
     "password_recovery": [
      "Open the login form.",
      "Select Forgot your password?",
      "Follow the password-reset instructions provided by the website.",
      "Use the recovered or reset credentials to log in again."
     ],
     "account_access_support": "support@cazeus.com"
    },
    "verification": {
     "purpose": [
      "Age verification",
      "Identity verification",
      "Address verification",
      "Payment-method ownership verification",
      "Source-of-funds verification",
      "Anti-money-laundering and fraud-prevention checks"
     ],
     "required_documents": [
      "Passport, national identity card or driving licence",
      "Proof of residential address",
      "Proof of ownership of the payment method",
      "Bank or payment-account statements",
      "Transaction history",
      "Source-of-funds or source-of-wealth evidence when requested"
     ],
     "additional_checks": [
      "Telephone verification",
      "Face verification",
      "Additional security checks",
      "Third-party identity and fraud-prevention checks"
     ],
     "procedure": [
      "Provide the requested identity, address and payment information.",
      "Upload the requested documents using the procedure provided by the website.",
      "Complete any additional telephone, facial or security verification requested.",
      "Wait for the verification review to be completed."
     ],
     "submission_deadline": "Within 30 days of the verification request",
     "usual_processing_time": "Within 10 days after all requested information has been supplied",
     "important_terms": [
      "Additional time may be required depending on the complexity of the checks.",
      "Deposits or withdrawals may be blocked while verification remains incomplete.",
      "The casino may request verification before or after a deposit or withdrawal.",
      "Failure to provide requested documents within the applicable deadline may result in account suspension or closure and withholding of funds."
     ]
    }
   },
   "brandinfo_responsible_gaming": {
    "responsible_gaming": {
     "minimum_age": "18+",
     "general_principles": [
      "Gambling should be treated as entertainment rather than a source of income.",
      "Players should gamble only with money they can afford to lose.",
      "Players should monitor the time and money spent gambling.",
      "Players should avoid chasing losses."
     ],
     "temporary_exclusion": {
      "availability": true,
      "procedure": [
       "Contact customer support and request a temporary break from gambling.",
       "Follow the instructions provided by the support team."
      ],
      "contact": "support@cazeus.com"
     },
     "self_exclusion": {
      "availability": true,
      "request_method": "Email",
      "contact": "support@cazeus.com",
      "procedure": [
       "Send a self-exclusion request to customer support.",
       "Provide the account information needed to identify the player.",
       "Request closure of the account for gambling-related reasons.",
       "Notify the casino of any other accounts held with the same operator.",
       "Do not create additional accounts during the exclusion period."
      ],
      "processing": "The account will be closed as soon as practicable.",
      "important_terms": [
       "Players remain responsible for not opening additional accounts.",
       "The casino states that it will make reasonable efforts to prevent new accounts.",
       "The casino does not accept responsibility for losses incurred on other accounts."
      ]
     },
     "account_closure": {
      "contact": "support@cazeus.com",
      "method": "Email",
      "conditions": [
       "Ordinary account closure requires the account to have no remaining positive or negative balance and no pending withdrawal requests.",
       "The Terms state that funds may be voided if closure is requested while a positive balance or pending withdrawal request remains.",
       "For gambling-related exclusion, players should explicitly identify the request as a self-exclusion request."
      ]
     },
     "self_assessment": {
      "availability": true,
      "questions_cover": [
       "Whether gambling interferes with work or education",
       "Whether gambling is used to escape boredom or other difficulties",
       "Whether gambling sessions last for extended periods",
       "Whether other people have expressed concern",
       "Whether gambling has displaced relationships and hobbies",
       "Whether the player hides gambling expenditure or time spent gambling",
       "Whether the player borrows money to gamble or repay gambling debts",
       "Whether the player continues until all available money is lost",
       "Whether the player attempts to recover losses immediately",
       "Whether running out of gambling funds causes distress",
       "Whether negative emotions trigger gambling",
       "Whether gambling causes depression or suicidal thoughts"
      ],
      "recommended_action": "Contact a gambling-support organization if several answers indicate potential gambling-related harm."
     },
     "deposit_limits": {
      "availability": false
     },
     "loss_limits": {
      "availability": false
     },
     "session_time_limits": {
      "availability": false
     },
     "external_support": [
      {
       "name": "GamCare",
       "website": "https://www.gamcare.org.uk",
       "purpose": "Advice and support for people affected by gambling-related harm."
      },
      {
       "name": "Gamblers Anonymous",
       "website": "https://www.gamblersanonymous.org",
       "purpose": "Peer support for people experiencing gambling problems."
      },
      {
       "name": "Gambling Therapy",
       "website": "https://www.gamblingtherapy.org",
       "purpose": "Support and counselling for people affected by gambling-related harm."
      },
      {
       "name": "Net Nanny",
       "website": "https://www.netnanny.com",
       "purpose": "Parental filtering and internet access controls."
      }
     ],
     "support_contact": {
      "email": "support@cazeus.com",
      "availability": "24/7 live chat and email support"
     }
    }
   },
   "brandinfo_games": {
    "game_types": [
     "Slots",
     "Table Games",
     "Live Casino Games",
     "Live Game Shows",
     "Jackpots",
     "Instant Games",
     "Megaways",
     "Bonus Buy Games",
     "Sportsbook"
    ],
    "game_examples": [
     {
      "name": "Coin Spark",
      "provider": "CROCO Games",
      "RTP": "92% / 94% / 95% / 96%",
      "volatility": "Medium",
      "maximum_multiplier": "2,000x"
     },
     {
      "name": "Piggy Party XL",
      "provider": "CROCO Games",
      "RTP": "96%",
      "volatility": "High",
      "maximum_multiplier": "5,000x"
     },
     {
      "name": "3 Hot Chilli Peppers",
      "provider": "Iron Dog Studio (1X2 Network)",
      "RTP": "95% / 93% / 91%",
      "volatility": "High",
      "maximum_multiplier": "10,000x"
     }
    ],
    "original_games": {
     "has_original_games": false
    },
    "providers": [
     "Amusnet",
     "BGaming",
     "Play’n GO",
     "Pragmatic Play",
     "Spinomenal",
     "Gamzix",
     "Booongo",
     "EGT",
     "IGTech",
     "Playson"
    ]
   },
   "brandinfo_sportsbook": {
    "sportsbook": {
     "sports_available": [
      "Football",
      "Basketball",
      "Motorsports",
      "Tennis",
      "Baseball",
      "Table Tennis",
      "Ice Hockey",
      "American Football",
      "Esports",
      "Virtual Sports",
      "Other international sports"
     ],
     "bet_types": [
      "Single",
      "Multiple / Accumulator",
      "System",
      "Bet Builder",
      "Match Winner",
      "Handicap",
      "Totals",
      "Outright Markets",
      "Player Specials",
      "Goalscorer Markets",
      "Corners",
      "Cards",
      "Draw No Bet"
     ],
     "minimum_bet": "€1",
     "odds_format": "Decimal odds are used for settlement",
     "live_betting": {
      "available": true,
      "features": [
       "In-play betting",
       "Cash Out",
       "Bet Builder",
       "Live markets",
       "Enhanced odds on selected events",
       "Early payout on qualifying events"
      ],
      "availability": "Live betting is available throughout the day, subject to event and market availability."
     },
     "sports_bonuses": [
      {
       "name": "Sports First Deposit Bonus",
       "type": "Sportsbook Welcome Bonus",
       "bonus_percentage": "100%",
       "maximum_bonus": "€100",
       "minimum_deposit": "€20",
       "claiming_method": [
        "Register a new account.",
        "Make the first qualifying deposit.",
        "Wager the full qualifying deposit once on settled sports bets at odds of at least 1.50.",
        "The bonus is activated after the qualifying rollover is completed."
       ],
       "qualification_requirement": "The full first deposit must be wagered once at minimum odds of 1.50.",
       "wagering_requirement": "(Deposit + bonus) x6",
       "country_specific_wagering": {
        "Germany": "(Deposit + bonus) x5",
        "Norway": "(Deposit + bonus) x5",
        "Finland": "(Deposit + bonus) x5",
        "Switzerland": "(Deposit + bonus) x5",
        "Austria": "(Deposit + bonus) x5"
       },
       "eligible_bets": [
        "Settled single bets at odds of at least 2.00",
        "Settled multiple bets with each selection at odds of at least 1.50"
       ],
       "validity": "30 days from the first deposit",
       "promo_code_required": false,
       "important_terms": [
        "Only new customers who have not previously made a real-money deposit qualify.",
        "Skrill and Neteller deposits do not qualify.",
        "The first bet on an individual event is the only bet counted toward the bonus rollover.",
        "A withdrawal request before the bonus is received may invalidate eligibility.",
        "A maximum cashout of 10x the bonus amount applies to players from Thailand, Japan, Brazil, Chile and Peru."
       ]
      },
      {
       "name": "Weekly Sports Reload Bonus",
       "type": "Sportsbook Deposit Bonus",
       "bonus_percentage": "70%",
       "maximum_bonus": "€500",
       "minimum_deposit": "€20",
       "availability": "Once per week",
       "claiming_method": [
        "Make a qualifying sports deposit.",
        "Wager the full qualifying deposit once at odds of at least 1.50.",
        "Contact customer support after the qualifying bets have settled."
       ],
       "wagering_requirement": "Qualifying deposit x8",
       "country_specific_wagering": {
        "Germany": "Qualifying deposit x6",
        "Norway": "Qualifying deposit x6",
        "Finland": "Qualifying deposit x6",
        "Switzerland": "Qualifying deposit x6",
        "Austria": "Qualifying deposit x6"
       },
       "eligible_bets": [
        "Settled single sports bets at odds of at least 2.00",
        "Settled multiple bets with each selection at odds of at least 1.50"
       ],
       "validity": "30 days after the bonus is credited",
       "maximum_qualifying_stake": "€50 per bet",
       "promo_code_required": false,
       "important_terms": [
        "The bonus is available once per week.",
        "The qualifying amount is calculated using the highest eligible deposit of the week.",
        "Cashed-out, void, system and bonus-funded bets are excluded from wagering where the promotion rules prohibit them.",
        "An active withdrawal request may invalidate eligibility.",
        "The bonus is restricted to sportsbook activity."
       ]
      },
      {
       "name": "Sports Cashback Bonus",
       "type": "Sportsbook Cashback",
       "bonus_percentage": "10%",
       "maximum_bonus": "€500",
       "minimum_cashback": "€20",
       "availability": "Weekly",
       "qualification_period": "Monday 00:01 UTC to Sunday 23:59 UTC",
       "claiming_method": [
        "Opt in to the promotion during the qualifying week.",
        "Place eligible sports bets.",
        "Open My Bonuses on Monday to view and activate the credited cashback."
       ],
       "calculation": "10% of qualifying net sports losses during the weekly period",
       "wagering_requirement": "Cashback x3",
       "validity": "The credited cashback must be activated within 72 hours and wagered within 30 days.",
       "eligible_games": "Sportsbook only",
       "promo_code_required": false,
       "important_terms": [
        "The cashback is calculated from qualifying sports losses after accounting for winnings, bonuses, withdrawals and the current balance as defined by the promotion rules.",
        "Cashback funds cannot be used in Casino or Live Casino games.",
        "Uncompleted wagering requirements prevent withdrawal of the cashback and related winnings.",
        "An active withdrawal request may invalidate eligibility."
       ]
      },
      {
       "name": "Build Your Bet",
       "type": "Bet Insurance",
       "amount": "50% Risk Free up to €50",
       "minimum_qualifying_bet": "€20",
       "minimum_odds": "1.70",
       "availability": "Once per week",
       "claiming_method": [
        "Place a qualifying Bet Builder sports bet.",
        "Wait for the bet to settle.",
        "If the first qualifying bet of the day loses, contact customer support to request the applicable stakeback."
       ],
       "reward_format": "Free Bet",
       "wagering_requirement": "Free Bet winnings x3 at minimum odds of 1.50",
       "promo_code_required": false,
       "important_terms": [
        "The qualifying Bet Builder bet must meet the minimum stake and odds requirements.",
        "The reward is issued as a Free Bet rather than a cash refund.",
        "Free Bet winnings are subject to the applicable wagering requirements."
       ]
      },
      {
       "name": "Accumulator Boost",
       "type": "Enhanced Sports Winnings",
       "maximum_boost": "100%",
       "minimum_selections": 3,
       "minimum_odds_per_selection": "1.40",
       "boost_by_selections": {
        "3": "3%",
        "4": "5%",
        "5": "8%",
        "6": "10%",
        "7": "13%",
        "8": "15%",
        "9": "20%",
        "10": "30%",
        "11": "35%",
        "12": "40%",
        "13": "45%",
        "14": "50%",
        "15": "55%",
        "16": "60%",
        "17": "65%",
        "18": "70%",
        "19": "80%",
        "20": "90%",
        "21+": "100%"
       },
       "claiming_method": "The boost is automatically added after settlement of a qualifying winning accumulator.",
       "wagering_requirement": "No additional wagering for bets placed using real-money balance.",
       "promo_code_required": false,
       "important_terms": [
        "Every selection must have odds of at least 1.40.",
        "All selections must win for the accumulator to qualify.",
        "Only real-money bets qualify.",
        "Bets placed using bonus funds or Free Bet winnings do not qualify."
       ]
      },
      {
       "name": "2 Goals Payout",
       "type": "Early Payout",
       "claiming_method": "Place a qualifying pre-match 1X2 bet on a market displaying the 2 Goals Payout feature.",
       "qualifying_condition": "The selected team must take the required lead during regular time.",
       "qualifying_markets": [
        "Pre-match Home Win",
        "Pre-match Away Win"
       ],
       "sport_specific_conditions": {
        "Football": "The selected team leads by 2 goals.",
        "Baseball": "The selected team leads by 5 runs.",
        "American Football": "The selected team leads by 17 points.",
        "Basketball": "The selected team leads by 20 points.",
        "Tennis": "The selected player leads by 2 sets.",
        "Ice Hockey": "The selected team leads by 3 goals."
       },
       "wagering_requirement": "No additional wagering for bets placed using real-money balance.",
       "promo_code_required": false,
       "important_terms": [
        "The market must display the 2 Goals Payout feature.",
        "Draw selections are excluded.",
        "The feature applies to qualifying pre-match bets, not live bets.",
        "A fully cashed-out bet does not qualify.",
        "Once the bet is paid out early, it will not be paid again if the selection subsequently wins the event."
       ]
      }
     ],
     "general_betting_rules": [
      "The minimum stake is €1.",
      "The maximum stake depends on the sport and jurisdiction and is displayed when placing a bet.",
      "Single, Multiple and System bets are supported.",
      "A confirmed bet cannot be changed or cancelled; Cash Out may be available.",
      "Bets are settled using decimal odds.",
      "Winnings are credited after the result has been officially confirmed.",
      "Bets may be voided for cancelled events, material errors, fraud or other conditions covered by the betting rules."
     ]
    }
   },
   "brandinfo_deposit": {
    "deposit_methods": [
     {
      "method": "Interac",
      "minimum": "€10",
      "maximum": "€10,000",
      "fee": "No casino deposit fee; provider fees may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "CAD"
      ]
     },
     {
      "method": "Visa",
      "minimum": "€20",
      "maximum": "€4,000",
      "fee": "No casino deposit fee; card issuer fees may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR",
       "USD",
       "CAD"
      ]
     },
     {
      "method": "Mastercard",
      "minimum": "€20",
      "maximum": "€4,000",
      "fee": "No casino deposit fee; card issuer fees may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR",
       "USD",
       "CAD"
      ]
     },
     {
      "method": "Paysafecard",
      "minimum": "€15",
      "maximum": "€1,400",
      "fee": "Provider fees may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR",
       "USD"
      ]
     },
     {
      "method": "Neteller",
      "minimum": "€20",
      "maximum": "€7,800",
      "fee": "No casino deposit fee; provider fees may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR",
       "USD",
       "CAD"
      ]
     },
     {
      "method": "Cash2Code",
      "minimum": "€20",
      "maximum": "€1,500",
      "fee": "Provider fees may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR",
       "USD"
      ]
     },
     {
      "method": "MiFinity",
      "minimum": "€15",
      "maximum": "€3,750",
      "fee": "No casino deposit fee; provider fees may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR",
       "USD",
       "CAD"
      ]
     },
     {
      "method": "Bitcoin",
      "minimum": "€45",
      "maximum": "€10,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "BTC"
      ]
     },
     {
      "method": "Dogecoin",
      "minimum": "€20",
      "maximum": "€7,800",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "DOGE"
      ]
     },
     {
      "method": "Tether USDT",
      "network": "ERC20",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "USDT"
      ]
     },
     {
      "method": "Tether USDT",
      "network": "Solana",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "USDT"
      ]
     },
     {
      "method": "Tether USDT",
      "network": "BEP20",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "USDT"
      ]
     },
     {
      "method": "Tether USDT",
      "network": "TRC20",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "USDT"
      ]
     },
     {
      "method": "Ethereum",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "ETH"
      ]
     },
     {
      "method": "Litecoin",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "LTC"
      ]
     },
     {
      "method": "Tron",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "TRX"
      ]
     },
     {
      "method": "USD Coin",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "USDC"
      ]
     },
     {
      "method": "BNB",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "BNB"
      ]
     },
     {
      "method": "Solana",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "SOL"
      ]
     },
     {
      "method": "USD Coin",
      "network": "Solana",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "USDC"
      ]
     },
     {
      "method": "Cardano",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "Instant after network confirmation",
      "currencies": [
       "ADA"
      ]
     }
    ],
    "deposit_guide": [
     "Log in to your Cazeus account.",
     "Open the Cashier or Payments section.",
     "Select Deposit.",
     "Choose an available payment method.",
     "Enter the deposit amount within the limits displayed for the selected method.",
     "Enter the requested payment or wallet details.",
     "Confirm the transaction through the payment provider.",
     "Wait for the payment to be processed and the funds to appear in your account."
    ],
    "additional_payment_data": {
     "minimum_deposit": "€10",
     "maximum_deposit": "€10,000",
     "transaction_speed": "Instant for most listed methods, subject to provider and blockchain processing",
     "general_conditions": [
      "Available methods depend on the country, account currency and payment provider.",
      "The payment method must belong to the account holder.",
      "The casino may request verification before or after a deposit.",
      "The general Terms reserve the right to set individual minimum and maximum deposit amounts."
     ]
    }
   },
   "brandinfo_withdrawal": {
    "withdrawal_methods": [
     {
      "method": "Interac",
      "minimum": "€10",
      "maximum": "€10,000",
      "fee": "No casino withdrawal fee; provider fees may apply",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "CAD"
      ]
     },
     {
      "method": "Visa",
      "minimum": "€20",
      "maximum": "€4,000",
      "fee": "No casino withdrawal fee; card issuer fees may apply",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "EUR",
       "USD",
       "CAD"
      ]
     },
     {
      "method": "Mastercard",
      "minimum": "€20",
      "maximum": "€4,000",
      "fee": "No casino withdrawal fee; card issuer fees may apply",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "EUR",
       "USD",
       "CAD"
      ]
     },
     {
      "method": "Paysafecard",
      "minimum": "€15",
      "maximum": "€1,400",
      "fee": "Provider fees may apply",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "EUR",
       "USD"
      ]
     },
     {
      "method": "Neteller",
      "minimum": "€20",
      "maximum": "€7,800",
      "fee": "No casino withdrawal fee; provider fees may apply",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "EUR",
       "USD",
       "CAD"
      ]
     },
     {
      "method": "Cash2Code",
      "minimum": "€20",
      "maximum": "€1,500",
      "fee": "Provider fees may apply",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "EUR",
       "USD"
      ]
     },
     {
      "method": "MiFinity",
      "minimum": "€15",
      "maximum": "€3,750",
      "fee": "No casino withdrawal fee; provider fees may apply",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "EUR",
       "USD",
       "CAD"
      ]
     },
     {
      "method": "Bitcoin",
      "minimum": "€45",
      "maximum": "€10,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "BTC"
      ]
     },
     {
      "method": "Dogecoin",
      "minimum": "€20",
      "maximum": "€7,800",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "DOGE"
      ]
     },
     {
      "method": "Tether USDT",
      "network": "ERC20",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "USDT"
      ]
     },
     {
      "method": "Tether USDT",
      "network": "Solana",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "USDT"
      ]
     },
     {
      "method": "Tether USDT",
      "network": "BEP20",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "USDT"
      ]
     },
     {
      "method": "Tether USDT",
      "network": "TRC20",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "USDT"
      ]
     },
     {
      "method": "Ethereum",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "ETH"
      ]
     },
     {
      "method": "Litecoin",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "LTC"
      ]
     },
     {
      "method": "Tron",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "TRX"
      ]
     },
     {
      "method": "USD Coin",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "USDC"
      ]
     },
     {
      "method": "BNB",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "BNB"
      ]
     },
     {
      "method": "Solana",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "SOL"
      ]
     },
     {
      "method": "USD Coin",
      "network": "Solana",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "USDC"
      ]
     },
     {
      "method": "Cardano",
      "minimum": "€20",
      "maximum": "€8,000",
      "fee": "Blockchain network fees may apply",
      "transaction_speed": "1–3 business days after approval, plus blockchain confirmation",
      "currencies": [
       "ADA"
      ]
     }
    ],
    "withdrawal_guide": [
     "Log in to your Cazeus account.",
     "Open the Cashier or Payments section.",
     "Select Withdrawal.",
     "Choose an available withdrawal method, preferably the same method used for the deposit where possible.",
     "Enter the withdrawal amount within the limits displayed for the selected method.",
     "Provide the requested receiving-account or wallet details.",
     "Submit the withdrawal request.",
     "Complete identity, address, payment-ownership or source-of-funds verification if requested.",
     "Wait for the financial department to review and process the withdrawal.",
     "Receive the funds after the payment provider or blockchain completes processing."
    ],
    "additional_payment_data": {
     "minimum_withdrawal": "€10",
     "maximum_withdrawal": "€10,000 per transaction, subject to method and account limits",
     "withdrawal_speed": "The financial department processes requests within 3 business days when requirements and checks are complete; payment delivery may take additional time.",
     "general_conditions": [
      "Where possible, withdrawals are processed using the same payment method used for deposits.",
      "The casino may use a different payment system when necessary.",
      "A minimum deposit rollover of x1 applies before withdrawal.",
      "The casino reserves the right to decline a withdrawal if the player has not met the monthly wagering threshold of €20.",
      "If the deposited funds have not been wagered at least once, winnings may be cancelled and a payment commission may apply.",
      "Withdrawal requests are subject to account verification, financial review and fraud-prevention checks.",
      "A maximum of three withdrawal requests may remain pending at one time.",
      "VIP daily and monthly withdrawal limits apply.",
      "The casino may delay payment until required verification and compliance checks are completed."
     ]
    }
   },
   "brandinfo_app": {
    "app_information": {
     "mobile_app": "No dedicated native mobile application",
     "mobile_website": true,
     "platforms": [
      "Desktop",
      "Laptop",
      "Tablet",
      "Smartphone"
     ],
     "access_method": "Open cazeus.com in a supported web browser.",
     "installation_required": false,
     "features": [
      "Access to casino games",
      "Access to Live Casino",
      "Sportsbook and live betting",
      "Account registration and login",
      "Promotions and VIP features",
      "Deposits and withdrawals through supported payment methods",
      "Customer support through live chat and email"
     ],
     "compatibility": "Responsive website optimized for mobile browsers",
     "security": [
      "Encrypted connections",
      "Website security measures",
      "Account verification and payment-security checks"
     ]
    }
   },
   "brandinfo_privacy_policy": {
    "data_controller": {
     "entity": "The operator of the Cazeus website",
     "responsibility": "Determines the purposes and means of processing personal data.",
     "data_protection_officer": "dpo@cazeus.com"
    },
    "data_collected": {
     "registration_data": [
      "Email address",
      "Date of birth",
      "Country",
      "Phone number",
      "Gender",
      "Full name",
      "Social security or equivalent identification number",
      "Postal code",
      "Username",
      "IP address",
      "Location data"
     ],
     "due_diligence_data": [
      "Identity card number",
      "Driving licence or passport number",
      "Proof of address",
      "Source of wealth and funds",
      "Bank identification information",
      "Financial statements and details"
     ],
     "financial_information": [
      "Bank ID",
      "CPR number",
      "CPF number",
      "IBAN",
      "Payment system details",
      "Deposit and withdrawal information"
     ],
     "technical_data": [
      "IP address",
      "Operating system version",
      "Device identifiers",
      "Browser and device information",
      "Session timestamps",
      "Pages visited",
      "Searches and other website interactions",
      "Session duration",
      "Clickstream and usage logs"
     ],
     "inferred_data": [
      "Interests",
      "Game preferences",
      "Potential gambling-related risk indicators",
      "Marketing preferences"
     ]
    },
    "data_collection_methods": [
     "Information supplied directly during registration and account use",
     "Information supplied during deposits, withdrawals and verification",
     "Automatic collection through server logs and device technologies",
     "Cookies and similar tracking technologies",
     "Publicly available sources, including public and government databases",
     "Commercial databases and third-party financial institutions",
     "Fraud-prevention agencies and public authorities",
     "Publicly available social media information and linked accounts",
     "Inferences derived from website usage and gaming activity"
    ],
    "data_usage": [
     "Providing casino and sportsbook services",
     "Creating and maintaining player accounts",
     "Responding to customer enquiries and requests",
     "Testing, troubleshooting, researching and improving services",
     "Detecting and preventing fraud and illegal activity",
     "Managing security and operational risks",
     "Supporting age, identity and source-of-funds verification",
     "Promoting responsible gambling and identifying potentially harmful behaviour",
     "Sending marketing messages and personalizing promotional offers",
     "Resolving disputes and responding to legal or regulatory investigations",
     "Meeting applicable legal and regulatory obligations",
     "Maintaining website functionality and protecting systems against unauthorized access"
    ],
    "legal_basis": {
     "contract": [
      "Creating and maintaining accounts",
      "Providing services",
      "Communicating with players",
      "Performing obligations under the Terms and Conditions"
     ],
     "legal_obligation": [
      "Age and identity verification",
      "KYC and AML checks",
      "Location and jurisdiction checks",
      "Fraud prevention",
      "Responsible-gambling risk management",
      "Regulatory reporting",
      "Responding to lawful requests from authorities"
     ],
     "legitimate_interest": [
      "Website and system security",
      "Fraud prevention",
      "Product improvement",
      "Analytics and research",
      "Risk management",
      "Responsible-gambling analysis",
      "Resolving legal claims and disputes"
     ],
     "consent": [
      "Direct marketing",
      "Personalized promotional offers",
      "Targeted advertising",
      "Marketing effectiveness analysis",
      "Non-essential cookies and tracking technologies",
      "Participation in promotional and loyalty activities where consent is required"
     ]
    },
    "third_party_sharing": {
     "recipients": [
      "Authorized employees and contractors",
      "Affiliates and subsidiary companies",
      "Joint controllers",
      "Payment providers and financial institutions",
      "Customer support providers",
      "Email, SMS and telephone service providers",
      "Technology and cloud-hosting providers",
      "Marketing partners",
      "Fraud-prevention agencies",
      "Game providers",
      "Data aggregators and analytics providers",
      "Law enforcement agencies",
      "Regulatory and licensing authorities"
     ],
     "payment_provider_data": [
      "First name",
      "Last name",
      "Date of birth",
      "Email address",
      "Residential address",
      "Postal code",
      "City",
      "Country",
      "Phone number",
      "Username or alias",
      "KYC documents where required"
     ],
     "business_transactions": "Personal data may be disclosed during a merger, acquisition, financing, bankruptcy, restructuring, sale or other change in ownership or control.",
     "complaint_related_disclosures": "Relevant personal data may be disclosed to third-party review platforms or dispute-resolution bodies when necessary to investigate and respond to a complaint."
    },
    "international_transfers": {
     "outside_eu_eea": true,
     "safeguards": [
      "Transfers to countries recognized by the European Commission as providing adequate protection",
      "Standard Contractual Clauses approved by the European Commission",
      "Other legally recognized safeguards"
     ]
    },
    "data_retention": {
     "standard_period": "For the duration of the player account and as long as required to fulfil the purposes described in the Privacy Notice.",
     "extended_retention": "Personal data may be retained longer when required by AML rules or other legal and regulatory obligations.",
     "after_account_closure": "Data is deleted or anonymized once there is no longer a legal or business need to retain it."
    },
    "data_security": {
     "measures": [
      "Administrative safeguards",
      "Technical safeguards",
      "Physical safeguards",
      "Protection against unauthorized access",
      "Protection against loss, theft and misuse",
      "Measures to protect data from unauthorized disclosure, alteration and destruction",
      "Ongoing assessment and improvement of security practices"
     ],
     "security_limitation": "Absolute security of internet transmission and storage cannot be guaranteed."
    },
    "user_rights": [
     "Request access to personal data",
     "Request information about data processing",
     "Request correction of inaccurate or incomplete data",
     "Request erasure when no compelling legal or business reason requires continued processing",
     "Request restriction of processing in applicable circumstances",
     "Request data portability in a structured, commonly used and machine-readable format",
     "Object to processing based on legitimate interests or direct marketing",
     "Withdraw consent without affecting the lawfulness of prior processing",
     "Lodge a complaint with a competent supervisory authority"
    ],
    "privacy_requests": {
     "customer_support": "support@cazeus.com",
     "data_protection_officer": "dpo@cazeus.com",
     "submission_method": "Email",
     "procedure": [
      "Contact customer support or the Data Protection Officer.",
      "Identify the privacy right or request being exercised.",
      "Provide the information needed to identify the account and process the request."
     ]
    },
    "cookies_policy": {
     "technologies": [
      "Cookies",
      "Tags",
      "Pixels",
      "Web beacons",
      "Similar tracking technologies"
     ],
     "strictly_necessary_cookies": "Used for essential website operation and do not require consent.",
     "non_essential_cookies": "Consent is requested during the first visit to the website or applications.",
     "preference_management": "Cookie preferences can be managed through the website's cookie settings."
    },
    "marketing_communications": {
     "channels": [
      "Email",
      "SMS",
      "Telephone calls",
      "Website notifications",
      "Application notifications where applicable"
     ],
     "legal_basis": "Consent where required",
     "personalization": [
      "Offers based on gaming history and preferences",
      "Targeted advertising",
      "Marketing effectiveness analysis"
     ]
    },
    "automated_decision_making": {
     "machine_learning": "Gaming behaviour may be analyzed using machine-learning algorithms to recommend games and features.",
     "risk_segmentation": "Customer segmentation may be used to identify risks, potentially harmful behaviour and responsible-gambling concerns.",
     "fraud_detection": "Automated analysis may be used to detect unusual activity, unauthorized tools, cheating and potential fraud."
    },
    "privacy_complaints": {
     "internal_contact": "support@cazeus.com",
     "data_protection_contact": "dpo@cazeus.com",
     "supervisory_authority": "A competent data protection supervisory authority in the player's EU member state of residence, place of work or the location of the alleged infringement.",
     "escalation": "Players may lodge a complaint with the relevant supervisory authority if they believe their data protection rights have been infringed."
    },
    "policy_updates": {
     "effective_date": "October 2024",
     "modification_rights": "The Privacy Notice may be updated, modified or amended as technology evolves or as required by law.",
     "effective_date_rule": "The amended notice applies from the effective date published on the website.",
     "user_responsibility": "Players are responsible for reviewing the amended Privacy Notice."
    },
    "additional_terms": [
     "Personal data may be disclosed during a change in ownership or control.",
     "A new owner may use transferred personal data only in accordance with the Privacy Notice unless the player gives explicit consent for different use.",
     "Data may be used for regulatory reporting and to respond to lawful requests from public authorities.",
     "Information shared to resolve third-party complaints is restricted to what is necessary and proportionate.",
     "The Privacy Notice applies to registered players and website visitors."
    ]
   }
  }
 },
 "competitor_h1": [
  "Review of Cazeus Norway",
  "Cazeus Casino"
 ],
 "competitor_stats": [
  {
   "url": "https://www.mightytips.com/online-casinos/cazeus-no/",
   "body_words": 1256,
   "keywords_in_total": {
    "Cazeus": 24,
    "Cazues casino": 0
   },
   "keywords_in_h1": {
    "Cazeus": 1,
    "Cazues casino": 0
   },
   "keywords_in_h2": {
    "Cazeus": 2,
    "Cazues casino": 0
   }
  },
  {
   "url": "https://www.casinospesialisten.net/cazeus-casino",
   "body_words": 3750,
   "keywords_in_total": {
    "Cazeus": 23,
    "Cazues casino": 0
   },
   "keywords_in_h1": {
    "Cazeus": 1,
    "Cazues casino": 0
   },
   "keywords_in_h2": {
    "Cazeus": 3,
    "Cazues casino": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 2503,
  "keyword_targets": {
   "Cazeus": 24,
   "Cazues casino": 1
  }
 },
 "heading_clusters": [
  {
   "id": "k02",
   "canonical_title": "Spillutvalg",
   "topic": "Games overview and game library",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 247,
   "avg_position": 0.21,
   "examples": [
    "Casino games",
    "Spillutvalg på Cazeus"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Bonuser og kampanjer",
   "topic": "Welcome bonus and promotions",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 281,
   "avg_position": 0.23,
   "examples": [
    "Bonuses and promotions",
    "Velkomstbonus: opptil 5000 kroner + 200 freespins!",
    "Spesielle kampanjer og casino tilbud"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Live casino",
   "topic": "Live casino",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 98,
   "avg_position": 0.31,
   "examples": [
    "Live dealer games",
    "Live casino"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Innskudd og uttak",
   "topic": "Deposits and withdrawals",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 190,
   "avg_position": 0.5,
   "examples": [
    "Deposits and withdrawals",
    "Innskudd og uttak på Cazeus Casino Norge"
   ]
  },
  {
   "id": "k01",
   "canonical_title": "Om Cazeus casino",
   "topic": "About the casino / overview and history",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 111,
   "avg_position": 0.56,
   "examples": [
    "About Cazeus casino Norway",
    "Cazeus casino overview",
    "Om Cazeus",
    "Historien bak Cazeus"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "Mobil casino og app",
   "topic": "Mobile play and app",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 94,
   "avg_position": 0.56,
   "examples": [
    "Mobile and app experience",
    "Mobil casino og app"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "Kundesupport",
   "topic": "Customer support",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 116,
   "avg_position": 0.66,
   "examples": [
    "Customer support",
    "Kontakte kundesupport"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Ansvarlig spilling",
   "topic": "Responsible gambling",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 86,
   "avg_position": 0.77,
   "examples": [
    "Responsible gambling tools",
    "Ansvarlig spilling"
   ]
  },
  {
   "id": "k20",
   "canonical_title": "Vår vurdering",
   "topic": "Verdict / rating / conclusion",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 133,
   "avg_position": 0.86,
   "examples": [
    "Our verdict on Cazeus casino for Norway players",
    "Begrunnelse for scoren vi har gitt Cazeus",
    "Totalvurdering – 84%",
    "Skribentens kommentar"
   ]
  },
  {
   "id": "k21",
   "canonical_title": "Brukeranmeldelser og erfaringer",
   "topic": "User reviews and experience",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 88,
   "avg_position": 0.88,
   "examples": [
    "User Reviews",
    "Brukererfaring"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Bonuskode",
   "topic": "Bonus code",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 150,
   "avg_position": 0.1,
   "examples": [
    "Bonuskode"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Freespins",
   "topic": "Free spins",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 149,
   "avg_position": 0.15,
   "examples": [
    "Freespins"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "Spilleautomater",
   "topic": "Slots",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 32,
   "avg_position": 0.17,
   "examples": [
    "Slots"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Bordspill",
   "topic": "Table games",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 43,
   "avg_position": 0.22,
   "examples": [
    "Table games"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Lojalitets- og VIP-program",
   "topic": "VIP and loyalty programme",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 152,
   "avg_position": 0.25,
   "examples": [
    "Lojalitetsordning/VIP-program"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Gratisspill",
   "topic": "Free play / demo games",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 30,
   "avg_position": 0.33,
   "examples": [
    "Free games"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Sportsbook",
   "topic": "Sportsbook",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 41,
   "avg_position": 0.39,
   "examples": [
    "Sportsbook"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "Sammenligning med andre casinoer",
   "topic": "Comparison with other casinos",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 164,
   "avg_position": 0.4,
   "examples": [
    "Sammenligning"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Innskuddsmetoder",
   "topic": "Deposit methods",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 32,
   "avg_position": 0.56,
   "examples": [
    "Deposit methods"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Uttaksmetoder",
   "topic": "Withdrawal methods",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 42,
   "avg_position": 0.61,
   "examples": [
    "Withdrawal methods"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Lisens og sikkerhet",
   "topic": "Licence and security",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 90,
   "avg_position": 0.72,
   "examples": [
    "Licenses and security"
   ]
  },
  {
   "id": "k22",
   "canonical_title": "Ofte stilte spørsmål",
   "topic": "FAQ",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 84,
   "avg_position": 0.95,
   "examples": [
    "Ofte stilte spørsmål"
   ]
  },
  {
   "id": "k23",
   "canonical_title": "Flere casinoomtaler",
   "topic": "More casino reviews",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 55,
   "avg_position": 1.0,
   "examples": [
    "Flere casinoomtaler"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "Bitcoin",
   "competitors": 2
  },
  {
   "entity": "NetEnt",
   "competitors": 2
  },
  {
   "entity": "Red Tiger",
   "competitors": 2
  },
  {
   "entity": "PAGCOR",
   "competitors": 2
  },
  {
   "entity": "Mastercard",
   "competitors": 2
  },
  {
   "entity": "Revolut",
   "competitors": 2
  },
  {
   "entity": "Litecoin",
   "competitors": 2
  },
  {
   "entity": "NOK",
   "competitors": 1
  },
  {
   "entity": "Norway",
   "competitors": 1
  },
  {
   "entity": "Liernin Enterprises",
   "competitors": 1
  },
  {
   "entity": "Liernin Enterprises Limited",
   "competitors": 1
  },
  {
   "entity": "Welcome",
   "competitors": 1
  },
  {
   "entity": "Visa",
   "competitors": 1
  },
  {
   "entity": "Within 1",
   "competitors": 1
  },
  {
   "entity": "VIP-programmet",
   "competitors": 1
  },
  {
   "entity": "Les",
   "competitors": 1
  },
  {
   "entity": "Rabidi",
   "competitors": 1
  },
  {
   "entity": "Filippinene",
   "competitors": 1
  },
  {
   "entity": "Liernin",
   "competitors": 1
  },
  {
   "entity": "Join",
   "competitors": 1
  },
  {
   "entity": "Evolution",
   "competitors": 1
  },
  {
   "entity": "VIP",
   "competitors": 1
  },
  {
   "entity": "Payout",
   "competitors": 1
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 1
  },
  {
   "entity": "Live Chat",
   "competitors": 1
  },
  {
   "entity": "Live Casino",
   "competitors": 1
  },
  {
   "entity": "VIP-nivået",
   "competitors": 1
  },
  {
   "entity": "MiFinity",
   "competitors": 1
  },
  {
   "entity": "Rabidi N",
   "competitors": 1
  },
  {
   "entity": "Curacao",
   "competitors": 1
  },
  {
   "entity": "User Reviews",
   "competitors": 1
  },
  {
   "entity": "Updated 20",
   "competitors": 1
  },
  {
   "entity": "Payment Methods",
   "competitors": 1
  },
  {
   "entity": "GambleAware",
   "competitors": 1
  },
  {
   "entity": "Approx 3",
   "competitors": 1
  },
  {
   "entity": "Ygrdrassil",
   "competitors": 1
  },
  {
   "entity": "Megaways",
   "competitors": 1
  },
  {
   "entity": "Treasure Island",
   "competitors": 1
  },
  {
   "entity": "Gonzo’s Treasure Hunt",
   "competitors": 1
  },
  {
   "entity": "Pragmatic Live",
   "competitors": 1
  },
  {
   "entity": "This 100",
   "competitors": 1
  },
  {
   "entity": "Processing Time",
   "competitors": 1
  },
  {
   "entity": "Rapidi N",
   "competitors": 1
  },
  {
   "entity": "Philippine Amusement",
   "competitors": 1
  },
  {
   "entity": "Gaming Corporation",
   "competitors": 1
  },
  {
   "entity": "SSL",
   "competitors": 1
  },
  {
   "entity": "Licensing",
   "competitors": 1
  },
  {
   "entity": "Minimum",
   "competitors": 1
  },
  {
   "entity": "Payment",
   "competitors": 1
  },
  {
   "entity": "Table",
   "competitors": 1
  },
  {
   "entity": "Number",
   "competitors": 1
  },
  {
   "entity": "Software",
   "competitors": 1
  },
  {
   "entity": "Approx 96",
   "competitors": 1
  },
  {
   "entity": "Maximum",
   "competitors": 1
  },
  {
   "entity": "Customer",
   "competitors": 1
  },
  {
   "entity": "Top",
   "competitors": 1
  },
  {
   "entity": "NETELLER",
   "competitors": 1
  },
  {
   "entity": "PaysafeCard",
   "competitors": 1
  },
  {
   "entity": "Skrill",
   "competitors": 1
  },
  {
   "entity": "Credit Card",
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
  "tables": [
   {
    "competitor": 1,
    "url": "https://www.mightytips.com/online-casinos/cazeus-no/",
    "heading": "Cazeus casino overview",
    "rows": [
     [
      "🔐 Licensing",
      "PAGCOR"
     ],
     [
      "🎁 Welcome bonus",
      "100% Welcome bonus up to 5,000kr + 200 GS"
     ],
     [
      "💰 Minimum deposit",
      "100 NOK"
     ],
     [
      "💳 Payment methods",
      "Skrill, Visa, Bitcoin + 5 more"
     ],
     [
      "📈 Table limits",
      "2 NOK to 173,000 NOK"
     ],
     [
      "🎰 Number of games",
      "9,000+"
     ],
     [
      "🖥️ Software providers",
      "100 including Evolution, Red Tiger, and NetEnt"
     ],
     [
      "％ Payout percentage",
      "Approx 96%"
     ],
     [
      "⏱️ Maximum payout",
      "80,000 NOK per month"
     ],
     [
      "💸 Payout time",
      "Within 1 hour"
     ],
     [
      "💬 Customer support",
      "24/7 live chat + email"
     ],
     [
      "🔝 Top feature",
      "Selection of live casino games"
     ]
    ]
   },
   {
    "competitor": 1,
    "url": "https://www.mightytips.com/online-casinos/cazeus-no/",
    "heading": "User Reviews",
    "rows": [
     [
      "Title",
      "Cazeus"
     ],
     [
      "Website",
      "www.cazeus.com"
     ],
     [
      "Established",
      "2024"
     ],
     [
      "Phone",
      "None"
     ],
     [
      "Email",
      "support@cazeus.com"
     ],
     [
      "Payments",
      "Bitcoin , Mastercard , NETELLER , PaysafeCard , Skrill , Visa , Revolut , Credit Card , Debit Card , Litecoin"
     ],
     [
      "License",
      "PAGCOR"
     ]
    ]
   }
  ],
  "labels": [
   {
    "label": "email",
    "competitors": 1
   },
   {
    "label": "established",
    "competitors": 1
   },
   {
    "label": "license",
    "competitors": 1
   },
   {
    "label": "payments",
    "competitors": 1
   },
   {
    "label": "phone",
    "competitors": 1
   },
   {
    "label": "title",
    "competitors": 1
   },
   {
    "label": "website",
    "competitors": 1
   },
   {
    "label": "⏱️ maximum payout",
    "competitors": 1
   },
   {
    "label": "％ payout percentage",
    "competitors": 1
   },
   {
    "label": "🎁 welcome bonus",
    "competitors": 1
   },
   {
    "label": "🎰 number of games",
    "competitors": 1
   },
   {
    "label": "💬 customer support",
    "competitors": 1
   },
   {
    "label": "💰 minimum deposit",
    "competitors": 1
   },
   {
    "label": "💳 payment methods",
    "competitors": 1
   },
   {
    "label": "💸 payout time",
    "competitors": 1
   },
   {
    "label": "📈 table limits",
    "competitors": 1
   },
   {
    "label": "🔐 licensing",
    "competitors": 1
   },
   {
    "label": "🔝 top feature",
    "competitors": 1
   },
   {
    "label": "🖥️ software providers",
    "competitors": 1
   }
  ]
 }
}
