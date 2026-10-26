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
 "geo": "SG",
 "page_language": "English",
 "keywords": [
  "Longfu88",
  "Longfu 88",
  "Longfu88 casino",
  "Longfu88 login",
  "Longfu88 bonus",
  "Longfu88 app",
  "Longfu88 promo code",
  "Longfu 88 casino",
  "casino Longfu88",
  "Lngfu88 withdrawal time",
  "Longfu 88 Official Site",
  "Longfu",
  "Longfu sports"
 ],
 "facts_to_respect": [],
 "knowledge_base": {
  "title": "longfu88-new",
  "variables": {
   "brandinfo_general": {
    "brand_name": "Longfu88",
    "release_year": 2026,
    "minimum_age": 18,
    "licences": [
     {
      "jurisdiction": "Costa Rica",
      "operator": "Lumina",
      "registration_number": "000-039123-R-319326-001"
     }
    ],
    "currencies": [
     "EUR",
     "USD",
     "MYR",
     "THB",
     "SGD",
     "USDT"
    ],
    "customer_support": {
     "channels": [
      "24/7 live chat",
      "Email"
     ],
     "email": "support@longfu88.com",
     "languages": [
      "English",
      "Malay",
      "Simplified Chinese",
      "Thai",
      "Indonesian",
      "Vietnamese"
     ]
    },
    "minimum_deposit": "€10",
    "payment_methods": {
     "deposit": [
      "QRIS",
      "DANA",
      "OVO Wallet",
      "Mandiri",
      "BNI",
      "Bank Transfer",
      "Visa",
      "Mastercard",
      "USDT (TRC20)",
      "USDT (ERC20)",
      "USDT (BEP20)",
      "Bitcoin",
      "Ethereum",
      "Litecoin",
      "Ripple",
      "USDC",
      "Bitcoin Cash",
      "Cardano",
      "Touch'n Go",
      "GrabPay",
      "DuitNow",
      "Online Banking",
      "DBS Bank",
      "OCBC Bank",
      "PromptPay QR",
      "MoMo",
      "Zalo",
      "ViettelPay",
      "VietQR",
      "Sofort",
      "Giropay",
      "PayNow QR",
      "BCA",
      "PayNow",
      "Neteller",
      "Skrill"
     ],
     "withdrawal": [
      "Bank Transfer",
      "Visa",
      "Mastercard",
      "Bitcoin",
      "Ethereum",
      "Litecoin",
      "USDT (TRC20)",
      "USDT (ERC20)",
      "USDT (BEP20)",
      "Touch'n Go",
      "DANA",
      "MoMo",
      "DBS Bank",
      "Online Banking"
     ]
    },
    "welcome_bonus_summary": "188% up to €2,088 + 18 Free Spins; 25x deposit plus bonus, 40x Free Spins winnings."
   },
   "brandinfo_welcome": {
    "welcome_bonus": {
     "name": "Casino Welcome Bonus",
     "type": "First deposit casino bonus",
     "bonus_percentage": 188,
     "maximum_bonus": "€2,088",
     "free_spins": 18,
     "minimum_deposit": "€50",
     "wagering_requirement": "25x the deposit plus bonus amount",
     "free_spins_wagering": "40x Free Spins winnings",
     "validity": "10 days from activation",
     "maximum_bet": "€22.5 per spin",
     "maximum_cashout": "5x the initial bonus amount",
     "eligibility": "New registered players on their first qualifying deposit; one welcome offer per account.",
     "claiming_procedure": [
      "Register an account and complete the required personal details.",
      "Make the first qualifying deposit.",
      "Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.",
      "Play eligible casino games and complete the wagering before expiry."
     ],
     "important_terms": [
      "Neteller and Skrill deposits are excluded from this promotion.",
      "Free Spins winnings have separate wagering requirements.",
      "Only one promotional bonus may be active at a time.",
      "A withdrawal request before claiming or while the bonus is active can void promotional eligibility.",
      "Cancelling the promotion forfeits bonus funds and unconverted promotional winnings.",
      "Account verification may be required before payment of promotional winnings."
     ]
    }
   },
   "brandinfo_promotions": {
    "other_bonuses": [
     {
      "name": "Live Casino Welcome Bonus",
      "type": "Live casino welcome",
      "reward": "125% up to €888",
      "minimum_deposit": "€30",
      "wagering_requirement": "30x the deposit plus bonus",
      "validity": "7 days",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Registered players meeting the offer-specific qualification rules.",
      "important_terms": [
       "New players only; first qualifying deposit.",
       "Maximum bet: €25.",
       "Neteller and Skrill excluded.",
       "Must activate before wagering; cannot combine with another active bonus."
      ]
     },
     {
      "name": "Casino Crypto Welcome Bonus",
      "type": "Crypto casino welcome",
      "reward": "188% up to 2,888 USDT",
      "minimum_deposit": "50 USDT",
      "wagering_requirement": "40x deposit plus bonus",
      "validity": "10 days",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Registered players meeting the offer-specific qualification rules.",
      "important_terms": [
       "First qualifying crypto deposit only.",
       "Maximum bonus wager: 5 USDT per spin.",
       "Casino Welcome Bonus and Crypto Welcome Bonus are alternative first-deposit offers."
      ],
      "eligible_cryptocurrencies": [
       "USDT",
       "BTC",
       "BCH",
       "LTC",
       "ETH",
       "XRP",
       "USDC"
      ]
     },
     {
      "name": "Casino Weekly Reload",
      "type": "Weekly free spins",
      "reward": "50 Free Spins",
      "minimum_deposit": "€30",
      "wagering_requirement": "40x winnings from Free Spins",
      "validity": "7 days",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Registered players meeting the offer-specific qualification rules.",
      "important_terms": [
       "One claim per promotional period unless otherwise stated.",
       "Cannot be combined with another active casino bonus.",
       "Maximum stake while wagering bonus funds: €5 per spin."
      ]
     },
     {
      "name": "Casino Weekly Crypto Reload",
      "type": "Crypto weekly reload",
      "reward": "60% up to 1,000 USDT",
      "minimum_deposit": "20 USDT",
      "wagering_requirement": "30x deposit plus bonus",
      "validity": "7 days",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Registered players meeting the offer-specific qualification rules.",
      "important_terms": [
       "One claim per promotional period unless otherwise stated.",
       "Cannot be combined with another active casino bonus.",
       "Maximum stake while wagering bonus funds: €5 per spin."
      ]
     },
     {
      "name": "Casino Weekend Reload",
      "type": "Weekend deposit bonus",
      "reward": "Up to €3,360 + 50 Free Spins",
      "minimum_deposit": "€50",
      "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings",
      "validity": "7 days",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Registered players meeting the offer-specific qualification rules.",
      "important_terms": [
       "One claim per promotional period unless otherwise stated.",
       "Cannot be combined with another active casino bonus.",
       "Maximum stake while wagering bonus funds: €5 per spin."
      ]
     },
     {
      "name": "Casino Weekend Crypto Reload",
      "type": "Weekend crypto bonus",
      "reward": "75% up to 750 USDT + 100 Free Spins",
      "minimum_deposit": "20 USDT",
      "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings",
      "validity": "7 days",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Registered players meeting the offer-specific qualification rules.",
      "important_terms": [
       "One claim per promotional period unless otherwise stated.",
       "Cannot be combined with another active casino bonus.",
       "Maximum stake while wagering bonus funds: €5 per spin."
      ]
     },
     {
      "name": "Casino Double Fortune: One-Day Reload Special",
      "type": "One-day reload",
      "reward": "50% up to €500",
      "minimum_deposit": "€30",
      "wagering_requirement": "30x deposit plus bonus",
      "validity": "24 hours",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Registered players meeting the offer-specific qualification rules.",
      "important_terms": [
       "One claim per promotional period unless otherwise stated.",
       "Cannot be combined with another active casino bonus.",
       "Maximum stake while wagering bonus funds: €5 per spin."
      ]
     },
     {
      "name": "Casino Trick or Treat Pumpkin Bonanza",
      "type": "Seasonal casino promotion",
      "reward": "Up to 100 Free Spins",
      "minimum_deposit": "€20",
      "wagering_requirement": "40x Free Spins winnings",
      "validity": "7 days",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Registered players meeting the offer-specific qualification rules.",
      "important_terms": [
       "One claim per promotional period unless otherwise stated.",
       "Cannot be combined with another active casino bonus.",
       "Maximum stake while wagering bonus funds: €5 per spin."
      ]
     },
     {
      "name": "Casino Dragon Quest: Get Verified and Get Extra!",
      "type": "Verification reward",
      "reward": "€10 bonus credit",
      "minimum_deposit": "€20",
      "wagering_requirement": "30x promotional credit",
      "validity": "7 days",
      "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.",
      "eligibility": "Players who complete requested account verification during the campaign.",
      "important_terms": [
       "One claim per promotional period unless otherwise stated.",
       "Cannot be combined with another active casino bonus.",
       "Maximum stake while wagering bonus funds: €5 per spin."
      ]
     },
     {
      "name": "Casino Weekly Cashback",
      "type": "Casino cashback",
      "reward": "Up to 10% of weekly net casino losses, capped at €6,988",
      "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC",
      "minimum_cashback": "€4.5",
      "opt_in": "Opt in for a four-week cycle; active accounts can renew automatically.",
      "crediting": "Credited to My Bonuses on Monday; activation required.",
      "wagering_requirement": "10x cashback before withdrawal",
      "cashback_by_vip": [
       {
        "level": "VIP Bronze",
        "percentage": 2,
        "maximum": "€1,888"
       },
       {
        "level": "VIP Silver",
        "percentage": 4,
        "maximum": "€2,388"
       },
       {
        "level": "VIP Gold",
        "percentage": 6,
        "maximum": "€2,988"
       },
       {
        "level": "VIP Platinum",
        "percentage": 8,
        "maximum": "€3,988"
       },
       {
        "level": "VIP Diamond",
        "percentage": 10,
        "maximum": "€6,988"
       }
      ],
      "important_terms": [
       "Only real-money casino bets and winnings count; bonus funds excluded.",
       "Weekly cashback expires if it is not activated within its claim window."
      ]
     },
     {
      "name": "Live Casino Cashback",
      "type": "Live casino cashback",
      "reward": "25% up to €850",
      "minimum_cashback": "€4.5",
      "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC",
      "crediting": "Credited to My Bonuses on Monday; opt-in and activation required.",
      "wagering_requirement": "10x credited cashback",
      "important_terms": [
       "Based on real-money stakes less winnings in eligible Live Casino games.",
       "Bonus balances are excluded from cashback calculations."
      ]
     },
     {
      "name": "Unlimited Casino Rebate",
      "type": "Rebate",
      "rebate_percentage": 0.9,
      "calculation": "Qualifying settled real-money wagering on the relevant game category.",
      "crediting": "Rebate credited daily to the rewards balance.",
      "wagering_requirement": "1x credited rebate",
      "eligibility": "Registered players with qualifying settled wagers."
     },
     {
      "name": "Unlimited Live Casino Rebate",
      "type": "Rebate",
      "rebate_percentage": 1.0,
      "calculation": "Qualifying settled real-money wagering on the relevant game category.",
      "crediting": "Rebate credited daily to the rewards balance.",
      "wagering_requirement": "1x credited rebate",
      "eligibility": "Registered players with qualifying settled wagers."
     },
     {
      "name": "Unlimited P2P Rebate",
      "type": "Rebate",
      "rebate_percentage": 0.8,
      "calculation": "Qualifying settled real-money wagering on the relevant game category.",
      "crediting": "Rebate credited daily to the rewards balance.",
      "wagering_requirement": "1x credited rebate",
      "eligibility": "Registered players with qualifying settled wagers."
     },
     {
      "name": "Unlimited Lottery Rebate",
      "type": "Rebate",
      "rebate_percentage": 1.0,
      "calculation": "Qualifying settled real-money wagering on the relevant game category.",
      "crediting": "Rebate credited daily to the rewards balance.",
      "wagering_requirement": "1x credited rebate",
      "eligibility": "Registered players with qualifying settled wagers."
     }
    ],
    "gamification_features": [
     {
      "name": "Bonus Crab",
      "mechanics": "Claim qualifying picks to open a crab reward and reveal a casino prize.",
      "access": "Rewards area; qualifying activity may grant free picks.",
      "rewards": [
       "Bonus credits",
       "Free Spins",
       "Coins"
      ],
      "validity": "7 days after reward assignment",
      "wagering_requirement": "30x awarded bonus credit; 40x winnings from Free Spins"
     },
     {
      "name": "Wheel of Fortune",
      "mechanics": "Spend an eligible spin or Coins to rotate a prize wheel.",
      "access": "Rewards area",
      "rewards": [
       "Bonus credits",
       "Free Spins",
       "Coins"
      ],
      "validity": "7 days",
      "wagering_requirement": "30x bonus awards"
     },
     {
      "name": "Challenges",
      "mechanics": "Complete qualifying gambling tasks to unlock listed rewards.",
      "access": "Rewards > Challenges",
      "rewards": [
       "Coins",
       "Free Spins",
       "Bonus credits"
      ],
      "validity": "As shown for each challenge"
     },
     {
      "name": "Collections",
      "mechanics": "Collect campaign items by completing qualifying activity; redeem completed sets.",
      "access": "Rewards > Collections",
      "rewards": [
       "Coins",
       "Bonus rewards"
      ],
      "validity": "Campaign-specific"
     },
     {
      "name": "Coin Shop",
      "mechanics": "Exchange earned Coins for rewards in the Shop.",
      "access": "Rewards > Shop",
      "rewards": [
       "Reward items and bonus credits up to €4,500"
      ],
      "important_terms": [
       "Coin prices and prize availability vary by item.",
       "Rewards may carry separate wagering requirements."
      ]
     }
    ]
   },
   "brandinfo_loyalty": {
    "loyalty_vip_program": {
     "name": "Longfu88 VIP Program",
     "tiers": [
      "Bronze",
      "Silver",
      "Gold",
      "Platinum",
      "Diamond"
     ],
     "progression": "Earn VIP points through eligible real-money gameplay; points unlock numbered reward levels.",
     "levels": [
      {
       "level": 1,
       "points_required": 1,
       "level_reward": "€9.8",
       "cashback_percentage": 1,
       "withdrawal_limit": "€9,800",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat"
       ]
      },
      {
       "level": 2,
       "points_required": 15,
       "level_reward": "€14.7",
       "cashback_percentage": 1,
       "withdrawal_limit": "€17,150",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat"
       ]
      },
      {
       "level": 3,
       "points_required": 30,
       "level_reward": "€14.7",
       "cashback_percentage": 1.5,
       "withdrawal_limit": "€22,050",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback"
       ]
      },
      {
       "level": 4,
       "points_required": 50,
       "level_reward": "€19.6",
       "cashback_percentage": 1.5,
       "withdrawal_limit": "€29,400",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 5,
       "points_required": 70,
       "level_reward": "€24.5",
       "cashback_percentage": 2,
       "withdrawal_limit": "€34,300",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 6,
       "points_required": 100,
       "level_reward": "€34.3",
       "cashback_percentage": 2.5,
       "withdrawal_limit": "€39,200",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 7,
       "points_required": 150,
       "level_reward": "€49",
       "cashback_percentage": 2.5,
       "withdrawal_limit": "€44,100",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 8,
       "points_required": 300,
       "level_reward": "€73.5",
       "cashback_percentage": 3,
       "withdrawal_limit": "€49,000",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 9,
       "points_required": 500,
       "level_reward": "€98",
       "cashback_percentage": 3.5,
       "withdrawal_limit": "€53,900",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 10,
       "points_required": 700,
       "level_reward": "€147",
       "cashback_percentage": 4,
       "withdrawal_limit": "€63,700",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 11,
       "points_required": 900,
       "level_reward": "€196",
       "cashback_percentage": 4,
       "withdrawal_limit": "€68,600",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 12,
       "points_required": 1200,
       "level_reward": "€245",
       "cashback_percentage": 4.5,
       "withdrawal_limit": "€73,500",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 13,
       "points_required": 1500,
       "level_reward": "€294",
       "cashback_percentage": 5,
       "withdrawal_limit": "€78,400",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 14,
       "points_required": 1800,
       "level_reward": "€343",
       "cashback_percentage": 5.5,
       "withdrawal_limit": "€83,300",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 15,
       "points_required": 2100,
       "level_reward": "€392",
       "cashback_percentage": 6,
       "withdrawal_limit": "€88,200",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 16,
       "points_required": 2400,
       "level_reward": "€441",
       "cashback_percentage": 6,
       "withdrawal_limit": "€98,000",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 17,
       "points_required": 2700,
       "level_reward": "€490",
       "cashback_percentage": 6.5,
       "withdrawal_limit": "€102,900",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 18,
       "points_required": 3000,
       "level_reward": "€539",
       "cashback_percentage": 7,
       "withdrawal_limit": "€107,800",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 19,
       "points_required": 3300,
       "level_reward": "€588",
       "cashback_percentage": 7.5,
       "withdrawal_limit": "€112,700",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 20,
       "points_required": 3600,
       "level_reward": "€637",
       "cashback_percentage": 8,
       "withdrawal_limit": "€117,600",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 21,
       "points_required": 3900,
       "level_reward": "€686",
       "cashback_percentage": 8,
       "withdrawal_limit": "€127,400",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 22,
       "points_required": 4300,
       "level_reward": "€735",
       "cashback_percentage": 8.5,
       "withdrawal_limit": "€132,300",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 23,
       "points_required": 4700,
       "level_reward": "€833",
       "cashback_percentage": 9,
       "withdrawal_limit": "€137,200",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 24,
       "points_required": 5100,
       "level_reward": "€882",
       "cashback_percentage": 9.5,
       "withdrawal_limit": "€142,100",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      },
      {
       "level": 25,
       "points_required": 5500,
       "level_reward": "€980",
       "cashback_percentage": 10,
       "withdrawal_limit": "€147,000",
       "benefits": [
        "On-site promotions",
        "24/7 Live Chat",
        "Personalised offers",
        "Higher withdrawal limits",
        "Cashback",
        "Personal VIP Manager"
       ]
      }
     ],
     "additional_benefits": [
      "Personalised offers",
      "VIP cashback",
      "Higher withdrawal limits",
      "Personal VIP manager for eligible high tiers"
     ],
     "important_terms": [
      "Different reward and withdrawal limits may apply to VIP levels and currencies.",
      "Level-based benefits and promotion eligibility may change under program rules."
     ]
    }
   },
   "brandinfo_account": {
    "registration": {
     "methods": [
      "Email registration"
     ],
     "required_details": [
      "Email",
      "Password",
      "Legal name",
      "Date of birth",
      "Residential address"
     ],
     "steps": [
      "Open Longfu88 and select Register.",
      "Enter email and create a password.",
      "Confirm age and acceptance of Terms and Conditions and Privacy Policy.",
      "Complete the additional personal details and residential address.",
      "Select Create Account and complete any requested email confirmation."
     ],
     "eligibility": [
      "18+ and of legal gambling age in the relevant jurisdiction.",
      "Only one personal account per player."
     ]
    },
    "login": {
     "method": "Email and password",
     "steps": [
      "Select Login on the website.",
      "Enter registered email and password.",
      "Complete any security check and access the account."
     ],
     "password_recovery": [
      "Choose Forgot Password on the login screen.",
      "Request a reset link using the registered email.",
      "Follow the emailed instructions to set a new password."
     ]
    },
    "verification": {
     "triggers": [
      "Account review",
      "Before withdrawal",
      "Unusual or high-value transactions",
      "Changes to account or payment details"
     ],
     "documents": [
      "Government-issued photo ID or passport",
      "Proof of residential address",
      "Proof of ownership of a payment method",
      "Source of funds or wealth documents when requested"
     ],
     "procedure": [
      "Access the verification request in the account or follow the support instructions.",
      "Upload legible current documents matching the account profile.",
      "Complete additional telephone or face verification if requested.",
      "Wait for approval before withdrawal or other restricted activity."
     ],
     "document_submission_window": "Up to 30 days when requested",
     "typical_review_time": "Up to 10 days after a complete document set is received"
    }
   },
   "brandinfo_responsible_gaming": {
    "responsible_gaming": {
     "policy": "Players must be at least 18 years old and gamble only where lawful.",
     "self_exclusion": {
      "request_method": "Email support@longfu88.com",
      "processing_time": "Within 24 hours after the self-exclusion request is processed",
      "effect": "Account access and gambling may be restricted for the agreed period."
     },
     "account_closure": "Request account closure through customer support.",
     "self_assessment": "Self-assessment questions help players identify possible gambling-related harm.",
     "support_organizations": [
      "GamCare",
      "Gamblers Anonymous",
      "Gambling Therapy"
     ],
     "contact": "support@longfu88.com",
     "procedure": [
      "Contact support and request self-exclusion or account closure.",
      "Confirm your account details and preferred exclusion terms.",
      "Allow the casino to restrict or close access.",
      "Seek independent support where appropriate."
     ]
    }
   },
   "brandinfo_games": {
    "game_types": [
     "Slots",
     "Live dealer games",
     "Table games",
     "Jackpots",
     "Fishing",
     "P2P games",
     "Fast games",
     "Lottery",
     "Crash & instant games"
    ],
    "game_examples": [
     {
      "name": "Gates of Olympus",
      "provider": "Pragmatic Play",
      "rtp": "96.50%",
      "volatility": "High",
      "maximum_multiplier": "5,000x"
     },
     {
      "name": "Sweet Bonanza",
      "provider": "Pragmatic Play",
      "rtp": "96.48%",
      "volatility": "High",
      "maximum_multiplier": "21,175x"
     },
     {
      "name": "Wanted Dead or a Wild",
      "provider": "Hacksaw Gaming",
      "rtp": "96.38%",
      "volatility": "Very high",
      "maximum_multiplier": "12,500x"
     }
    ],
    "original_games": [
     {
      "name": "Longfu88 Baccarat",
      "category": "Exclusive live/table game",
      "features": [
       "Baccarat gameplay"
      ]
     }
    ],
    "providers": [
     "Evolution",
     "Red Tiger",
     "NetEnt",
     "Big Time Gaming",
     "Pragmatic Play",
     "Yggdrasil",
     "SA Gaming",
     "Skywind",
     "Betsoft",
     "Hacksaw Gaming"
    ]
   },
   "brandinfo_sportsbook": {
    "sportsbook": {
     "sports_available": [
      "Football",
      "Basketball",
      "Tennis",
      "Badminton",
      "Cricket",
      "Table tennis",
      "Volleyball",
      "Esports",
      "Virtual football"
     ],
     "bet_types": [
      "Single",
      "Accumulator",
      "Live",
      "Handicap",
      "Totals",
      "Outrights",
      "Bet Builder"
     ],
     "live_betting": {
      "available": true,
      "features": [
       "Live odds",
       "In-play markets"
      ]
     },
     "sports_bonuses": [
      {
       "name": "Sport First Deposit Bonus",
       "reward": "100% up to €1,888",
       "minimum_deposit": "€50",
       "wagering_requirement": "8x deposit plus bonus",
       "validity": "30 days",
       "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.",
       "important_terms": [
        "Only settled qualifying sports bets contribute to wagering.",
        "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.",
        "Voided and cashed-out bets do not qualify.",
        "One claim per stated promotional period."
       ]
      },
      {
       "name": "Sport Crypto Welcome Bonus",
       "reward": "100% up to 200 USDT",
       "minimum_deposit": "20 USDT",
       "wagering_requirement": "8x deposit plus bonus",
       "validity": "30 days",
       "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.",
       "important_terms": [
        "Only settled qualifying sports bets contribute to wagering.",
        "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.",
        "Voided and cashed-out bets do not qualify.",
        "One claim per stated promotional period."
       ]
      },
      {
       "name": "Sport Weekly Reload Bonus",
       "reward": "50% up to €2,500",
       "minimum_deposit": "€50",
       "wagering_requirement": "8x deposit plus bonus",
       "validity": "30 days",
       "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.",
       "important_terms": [
        "Only settled qualifying sports bets contribute to wagering.",
        "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.",
        "Voided and cashed-out bets do not qualify.",
        "One claim per stated promotional period."
       ]
      },
      {
       "name": "Sport Weekend Reload Bonus",
       "reward": "50% up to €3,750",
       "minimum_deposit": "€50",
       "wagering_requirement": "8x deposit plus bonus",
       "validity": "30 days",
       "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.",
       "important_terms": [
        "Only settled qualifying sports bets contribute to wagering.",
        "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.",
        "Voided and cashed-out bets do not qualify.",
        "One claim per stated promotional period."
       ]
      },
      {
       "name": "Sport Crypto Weekly Reload",
       "reward": "50% up to 500 USDT",
       "minimum_deposit": "20 USDT",
       "wagering_requirement": "8x deposit plus bonus",
       "validity": "30 days",
       "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.",
       "important_terms": [
        "Only settled qualifying sports bets contribute to wagering.",
        "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.",
        "Voided and cashed-out bets do not qualify.",
        "One claim per stated promotional period."
       ]
      },
      {
       "name": "Sport Crypto Weekend Reload",
       "reward": "50% up to 1,000 USDT",
       "minimum_deposit": "20 USDT",
       "wagering_requirement": "8x deposit plus bonus",
       "validity": "30 days",
       "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.",
       "important_terms": [
        "Only settled qualifying sports bets contribute to wagering.",
        "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.",
        "Voided and cashed-out bets do not qualify.",
        "One claim per stated promotional period."
       ]
      },
      {
       "name": "Unlimited Sports Rebate",
       "reward": "0.70% of qualifying settled sports wagers",
       "wagering_requirement": "1x credited rebate",
       "crediting": "Daily"
      },
      {
       "name": "Sports Cashback",
       "reward": "10% up to €2,500 of eligible sports net losses",
       "calculation_period": "Weekly",
       "wagering_requirement": "1x cashback",
       "eligibility": "Registered players with eligible real-money losing bets"
      },
      {
       "name": "2 Goals Ahead - Early Payout",
       "reward": "Early settlement of eligible football bets when the selected team leads by two goals",
       "important_terms": [
        "Only participating pre-match match-winner markets qualify.",
        "Settlement is subject to published event eligibility."
       ]
      },
      {
       "name": "Parlay Boost",
       "reward": "Up to 100% extra winnings on qualifying accumulators",
       "minimum_legs": 3,
       "wagering_requirement": "No additional bonus wagering on settled enhanced winnings",
       "important_terms": [
        "Boost depends on the number of qualifying selections."
       ]
      },
      {
       "name": "Bet Builder Risk Free",
       "reward": "50% risk-free stake return up to €250",
       "eligibility": "Qualifying pre-match Bet Builder selections",
       "wagering_requirement": "1x credited free-bet stake",
       "validity": "7 days"
      }
     ],
     "important_terms": [
      "Event availability and market selection can vary by jurisdiction."
     ]
    }
   },
   "brandinfo_deposit": {
    "deposit_methods": [
     {
      "method": "BCA",
      "currencies": [
       "IDR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €10, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "BNI",
      "currencies": [
       "IDR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €20, maximum €40,000 per transaction"
      ]
     },
     {
      "method": "Bank Transfer",
      "currencies": [
       "IDR",
       "MYR",
       "VND"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €25, maximum €82,000 per transaction",
       "MYR: minimum €50, maximum €50,000 per transaction",
       "VND: minimum €100, maximum €500,000 per transaction"
      ]
     },
     {
      "method": "Bitcoin",
      "currencies": [
       "BTC"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €590, maximum €98,490 per transaction",
       "MYR: minimum €145, maximum €23,840 per transaction",
       "SGD: minimum €45, maximum €7,560 per transaction",
       "THB: minimum €1,100, maximum €182,910 per transaction",
       "VND: minimum €929, maximum €154,949 per transaction"
      ]
     },
     {
      "method": "Bitcoin Cash",
      "currencies": [
       "BCH"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ]
     },
     {
      "method": "Cardano",
      "currencies": [
       "ADA"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ]
     },
     {
      "method": "DANA",
      "currencies": [
       "IDR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €10, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "DBS Bank",
      "currencies": [
       "SGD"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "SGD: minimum €50, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "DuitNow",
      "currencies": [
       "MYR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "MYR: minimum €30, maximum €50,000 per transaction"
      ]
     },
     {
      "method": "Ethereum",
      "currencies": [
       "ETH"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ]
     },
     {
      "method": "Giropay",
      "currencies": [
       "EUR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "EUR: minimum €10, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "GrabPay",
      "currencies": [
       "MYR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "MYR: minimum €30, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "Litecoin",
      "currencies": [
       "LTC"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ]
     },
     {
      "method": "Mandiri",
      "currencies": [
       "IDR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €20, maximum €40,000 per transaction"
      ]
     },
     {
      "method": "Mastercard",
      "currencies": [
       "IDR",
       "MYR",
       "SGD",
       "VND"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €200, maximum €30,000 per transaction",
       "MYR: minimum €50, maximum €9,000 per transaction",
       "SGD: minimum €18, maximum €3,000 per transaction",
       "VND: minimum €320, maximum €50,000 per transaction"
      ]
     },
     {
      "method": "MoMo",
      "currencies": [
       "VND"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "VND: minimum €50, maximum €30,000 per transaction"
      ]
     },
     {
      "method": "Neteller",
      "currencies": [
       "EUR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "EUR: minimum €10, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "OCBC Bank",
      "currencies": [
       "SGD"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "SGD: minimum €50, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "OVO Wallet",
      "currencies": [
       "IDR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €10, maximum €2,000 per transaction"
      ]
     },
     {
      "method": "Online Banking",
      "currencies": [
       "MYR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "MYR: minimum €30, maximum €10,000 per transaction"
      ]
     },
     {
      "method": "PayNow",
      "currencies": [
       "SGD"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "SGD: minimum €10, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "PayNow QR",
      "currencies": [
       "SGD"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "SGD: minimum €10, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "PromptPay QR",
      "currencies": [
       "THB"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "THB: minimum €300, maximum €200,000 per transaction"
      ]
     },
     {
      "method": "QRIS",
      "currencies": [
       "IDR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €10, maximum €50,000 per transaction"
      ]
     },
     {
      "method": "Ripple",
      "currencies": [
       "XRP"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ]
     },
     {
      "method": "Skrill",
      "currencies": [
       "EUR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "EUR: minimum €10, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "Sofort",
      "currencies": [
       "EUR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "EUR: minimum €10, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "Touch'n Go",
      "currencies": [
       "MYR"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "MYR: minimum €30, maximum €5,000 per transaction"
      ]
     },
     {
      "method": "USDC",
      "currencies": [
       "USDC"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ]
     },
     {
      "method": "USDT (BEP20)",
      "currencies": [
       "USDT"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ],
      "network": "BEP20"
     },
     {
      "method": "USDT (ERC20)",
      "currencies": [
       "USDT"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ],
      "network": "ERC20"
     },
     {
      "method": "USDT (TRC20)",
      "currencies": [
       "USDT"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €196, maximum €98,490 per transaction",
       "MYR: minimum €50, maximum €23,840 per transaction",
       "SGD: minimum €15, maximum €7,560 per transaction",
       "THB: minimum €370, maximum €182,910 per transaction",
       "VND: minimum €309, maximum €154,949 per transaction"
      ],
      "network": "TRC20"
     },
     {
      "method": "VietQR",
      "currencies": [
       "VND"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "VND: minimum €50, maximum €300,000 per transaction"
      ]
     },
     {
      "method": "ViettelPay",
      "currencies": [
       "VND"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "VND: minimum €50, maximum €20,000 per transaction"
      ]
     },
     {
      "method": "Visa",
      "currencies": [
       "IDR",
       "MYR",
       "SGD",
       "VND"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "IDR: minimum €200, maximum €30,000 per transaction",
       "MYR: minimum €50, maximum €9,000 per transaction",
       "SGD: minimum €18, maximum €3,000 per transaction",
       "VND: minimum €320, maximum €50,000 per transaction"
      ]
     },
     {
      "method": "Zalo",
      "currencies": [
       "VND"
      ],
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino processing fee; payment provider or blockchain network fees may apply",
      "transaction_speed": "1–2 minutes",
      "important_terms": [
       "VND: minimum €50, maximum €100,000 per transaction"
      ]
     }
    ],
    "deposit_guide": [
     "Log in to the Longfu88 account.",
     "Open the cashier and select Deposit.",
     "Choose an available payment method and its supported currency or blockchain network.",
     "Enter the amount and payment information.",
     "Confirm and authorize the transaction using the provider instructions.",
     "Wait for the funds to be credited to the playable balance."
    ]
   },
   "brandinfo_withdrawal": {
    "withdrawal_methods": [
     {
      "method": "Bank Transfer",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days",
      "currencies": [
       "IDR",
       "MYR",
       "VND"
      ],
      "important_terms": [
       "Indonesia: minimum €25,000 (IDR market)",
       "Malaysia: minimum €50 (MYR market)",
       "Singapore: minimum €80 (SGD market)",
       "Thailand: minimum €1,945 (THB market)",
       "Vietnam: minimum €10,000 (VND market)"
      ]
     },
     {
      "method": "Visa",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "IDR",
       "MYR",
       "SGD",
       "VND"
      ],
      "important_terms": [
       "Indonesia: minimum €25,000 (IDR market)",
       "Malaysia: minimum €50 (MYR market)",
       "Singapore: minimum €80 (SGD market)",
       "Thailand: minimum €1,945 (THB market)",
       "Vietnam: minimum €10,000 (VND market)"
      ]
     },
     {
      "method": "Mastercard",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "IDR",
       "MYR",
       "SGD",
       "VND"
      ],
      "important_terms": [
       "Indonesia: minimum €25,000 (IDR market)",
       "Malaysia: minimum €50 (MYR market)",
       "Singapore: minimum €80 (SGD market)",
       "Thailand: minimum €1,945 (THB market)",
       "Vietnam: minimum €10,000 (VND market)"
      ]
     },
     {
      "method": "Bitcoin",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "BTC"
      ],
      "important_terms": [
       "Singapore: minimum €15 (SGD market)",
       "Thailand: minimum €375 (THB market)",
       "Vietnam: minimum €308,000 (VND market)"
      ]
     },
     {
      "method": "Ethereum",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "ETH"
      ],
      "important_terms": [
       "Singapore: minimum €15 (SGD market)",
       "Thailand: minimum €375 (THB market)",
       "Vietnam: minimum €308,000 (VND market)"
      ]
     },
     {
      "method": "Litecoin",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "LTC"
      ],
      "important_terms": [
       "Singapore: minimum €15 (SGD market)",
       "Thailand: minimum €375 (THB market)",
       "Vietnam: minimum €308,000 (VND market)"
      ]
     },
     {
      "method": "USDT (TRC20)",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "USDT"
      ],
      "important_terms": [
       "Singapore: minimum €15 (SGD market)",
       "Thailand: minimum €375 (THB market)",
       "Vietnam: minimum €308,000 (VND market)"
      ]
     },
     {
      "method": "USDT (ERC20)",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "USDT"
      ],
      "important_terms": [
       "Singapore: minimum €15 (SGD market)",
       "Thailand: minimum €375 (THB market)",
       "Vietnam: minimum €308,000 (VND market)"
      ]
     },
     {
      "method": "USDT (BEP20)",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "USDT"
      ],
      "important_terms": [
       "Singapore: minimum €15 (SGD market)",
       "Thailand: minimum €375 (THB market)",
       "Vietnam: minimum €308,000 (VND market)"
      ]
     },
     {
      "method": "Touch'n Go",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "MYR"
      ],
      "important_terms": [
       "Indonesia: minimum €10,000 (IDR market)",
       "Malaysia: minimum €100 (MYR market)"
      ]
     },
     {
      "method": "DANA",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "IDR"
      ],
      "important_terms": [
       "Indonesia: minimum €10,000 (IDR market)",
       "Malaysia: minimum €100 (MYR market)"
      ]
     },
     {
      "method": "MoMo",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "1–3 business days",
      "currencies": [
       "VND"
      ],
      "important_terms": [
       "Indonesia: minimum €10,000 (IDR market)",
       "Malaysia: minimum €100 (MYR market)"
      ]
     },
     {
      "method": "DBS Bank",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days",
      "currencies": [
       "SGD"
      ],
      "important_terms": [
       "Indonesia: minimum €25,000 (IDR market)",
       "Malaysia: minimum €50 (MYR market)",
       "Singapore: minimum €80 (SGD market)",
       "Thailand: minimum €1,945 (THB market)",
       "Vietnam: minimum €10,000 (VND market)"
      ]
     },
     {
      "method": "Online Banking",
      "minimum": "€20",
      "maximum": "€5,000",
      "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.",
      "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days",
      "currencies": [
       "MYR"
      ],
      "important_terms": [
       "Indonesia: minimum €25,000 (IDR market)",
       "Malaysia: minimum €50 (MYR market)",
       "Singapore: minimum €80 (SGD market)",
       "Thailand: minimum €1,945 (THB market)",
       "Vietnam: minimum €10,000 (VND market)"
      ]
     }
    ],
    "withdrawal_guide": [
     "Log in to Longfu88 and open the cashier.",
     "Select Withdrawal and choose a supported destination or payment method.",
     "Enter the amount and the receiving bank, wallet, or blockchain address.",
     "Complete identity and payment-method verification if prompted.",
     "Review the request and confirm submission.",
     "Wait for casino processing and any bank or network settlement before receiving funds."
    ]
   },
   "brandinfo_app": {
    "app_information": {
     "platforms": [
      "Android",
      "iOS",
      "Mobile web"
     ],
     "mobile_access": "Responsive Longfu88 website usable on smartphone and tablet browsers.",
     "android_installation": [
      "Open Longfu88 in Chrome.",
      "Open browser menu and choose Add to Home screen.",
      "Confirm the shortcut."
     ],
     "ios_installation": [
      "Open Longfu88 in Safari.",
      "Tap Share and choose Add to Home Screen.",
      "Confirm Add."
     ],
     "features": [
      "Casino",
      "Sportsbook",
      "Account access",
      "Deposits",
      "Withdrawals",
      "Bonuses"
     ]
    }
   },
   "brandinfo_privacy_policy": {
    "privacy_policy": {
     "data_controller": {
      "company_name": "Lumina",
      "contact_email": "dpo@longfu88.com",
      "contact_details": "support@longfu88.com"
     },
     "effective_date": "October 2024",
     "data_collected": {
      "identity_data": [
       "Name",
       "Date of birth",
       "Identity documents"
      ],
      "contact_data": [
       "Email",
       "Telephone",
       "Residential address"
      ],
      "account_data": [
       "Registration and account identifiers"
      ],
      "financial_data": [
       "Deposits",
       "Withdrawals",
       "Payment information"
      ],
      "verification_data": [
       "KYC documents",
       "Payment method ownership evidence"
      ],
      "gaming_activity": [
       "Betting history",
       "Wins and losses",
       "Participation in bonuses"
      ],
      "technical_data": [
       "IP address",
       "Device data",
       "Browser information",
       "Cookies"
      ],
      "communication_data": [
       "Customer support correspondence"
      ],
      "marketing_data": [
       "Marketing preferences and promotions interactions"
      ]
     },
     "data_collection_methods": [
      "Registration forms",
      "Account transactions",
      "Gameplay",
      "Customer support communications",
      "Cookies and analytics",
      "Verification submissions"
     ],
     "processing_purposes": [
      "Account creation and administration",
      "Providing gambling services",
      "Payments and withdrawals",
      "KYC and AML compliance",
      "Fraud prevention and account security",
      "Customer support",
      "Marketing subject to applicable consent",
      "Service performance and analytics"
     ],
     "legal_bases": [
      "Contract performance",
      "Legal obligations",
      "Legitimate interests",
      "Consent when required"
     ],
     "data_sharing": [
      "Payment service providers",
      "Identity verification providers",
      "Technology providers",
      "Regulators and law enforcement when required"
     ],
     "data_retention": "Data is retained as needed for service delivery, regulatory compliance and dispute resolution.",
     "data_subject_rights": [
      "Access",
      "Rectification",
      "Erasure where legally permitted",
      "Restriction",
      "Objection",
      "Portability where applicable",
      "Withdrawal of consent"
     ],
     "cookies": "Necessary, preference, analytics and marketing cookies support website functions and measurement.",
     "international_transfers": "Personal data can be processed across jurisdictions subject to applicable safeguards.",
     "security": "Technical and organizational safeguards protect accounts, payments and personal information.",
     "marketing": "Players may manage direct-marketing preferences and unsubscribe from promotional communications.",
     "contact_email": "dpo@longfu88.com",
     "policy_updates": "The Privacy Notice may be amended; the updated version is published on the website."
    },
    "kyc_aml": {
     "verification_requirements": {
      "mandatory_verification": "Identity and payment checks may be required for access to withdrawals or promotional proceeds.",
      "verification_stages": [
       "Registration reviews",
       "Deposits",
       "Withdrawals",
       "Ongoing account monitoring"
      ],
      "additional_checks": [
       "Unusual transfers",
       "Large transactions",
       "Source of funds requests",
       "Changes in payment information"
      ]
     },
     "verification_triggers": [
      "First withdrawal request",
      "Suspicious account activity",
      "Compliance review",
      "Risk-based threshold checks",
      "Discrepancies in account or payment information"
     ],
     "required_documents": {
      "identity": [
       "Passport",
       "National identity card",
       "Driving licence"
      ],
      "address": [
       "Utility bill",
       "Bank statement"
      ],
      "payment_method": [
       "Bank or card ownership evidence",
       "Digital wallet ownership evidence"
      ],
      "source_of_funds": [
       "Proof of income",
       "Bank statements",
       "Other supporting financial documents"
      ]
     },
     "verification_procedure": [
      "Submit requested documentation through approved account or support channels.",
      "Ensure documents are readable, current and match registration details.",
      "Respond to further document or video/telephone checks when requested.",
      "Wait for account verification before restricted transactions proceed."
     ],
     "documentation_deadline": "Within 30 days of a document request",
     "processing_time": "Normally within 10 days of receipt of a complete document set",
     "aml_controls": [
      "Customer due diligence",
      "Enhanced verification for higher-risk activity",
      "Transaction monitoring",
      "Restrictions on third-party payments"
     ],
     "withdrawal_restrictions": "Payments may be held until identification, payment ownership and any required source-of-funds checks are complete.",
     "failure_consequences": [
      "Transaction refusal",
      "Account restrictions",
      "Withholding of withdrawals pending compliance"
     ]
    },
    "terms_conditions": {
     "version": "1.8",
     "last_updated": "2025-09-17",
     "eligibility": {
      "minimum_age": 18,
      "residency_requirements": "Players must be legally permitted to gamble in their place of residence.",
      "player_requirements": [
       "Register with accurate information",
       "Use only one personal account",
       "Do not use third-party payment methods"
      ]
     },
     "account_terms": [
      "The account holder is responsible for safeguarding credentials.",
      "The operator may suspend activity for verification or suspected abuse."
     ],
     "deposit_terms": [
      "Deposit minimums and available methods depend on country and currency.",
      "Deposits must be funded from methods the player is authorized to use."
     ],
     "withdrawal_terms": [
      "A minimum 1x deposit turnover can apply before a withdrawal.",
      "Withdrawal requests are generally processed within three working days.",
      "Bank transfers may need another 3–5 business days for settlement.",
      "The operator may request KYC documents before processing payments."
     ],
     "conditional_fees": [
      "Where qualifying turnover is below the deposited amount, a 10% commission may apply with minimum €2.25.",
      "A 15% charge can apply to some card or bank transfer funded transactions under the casino rules."
     ],
     "bonus_terms": [
      "Only one bonus may be active at a time unless the offer permits otherwise.",
      "Bonus terms and wagering restrictions apply before promotional winnings become withdrawable.",
      "Bonus misuse can lead to forfeiture."
     ],
     "complaints": "Contact customer support to request review of disputes or account decisions.",
     "inactivity": "Prolonged inactivity may trigger account review or closure under applicable terms.",
     "changes": "The operator may modify promotional and contractual terms and publish updates to the site.",
     "governing_law": "Applicable law and legally relevant jurisdictional requirements govern the agreement."
    }
   }
  }
 },
 "competitor_h1": [
  "Longfu88 Casino – Play in Singapore",
  "LongFu88 review 2026 October",
  "Longfu88 ‚Äî Best Online Casino 2026 for Real Money Gaming",
  "Longfu88 Casino Malaysia – Review, Games & Bonuses 2026",
  "Ulasan Longfu88 Casino: Panduan Pantas Untuk Pemain Malaysia"
 ],
 "competitor_stats": [
  {
   "url": "https://longfu88-sg.com/",
   "body_words": 1116,
   "keywords_in_total": {
    "Longfu88": 18,
    "Longfu 88": 2,
    "Longfu88 casino": 4,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h1": {
    "Longfu88": 0,
    "Longfu 88": 0,
    "Longfu88 casino": 1,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h2": {
    "Longfu88": 2,
    "Longfu 88": 1,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   }
  },
  {
   "url": "https://www.mightytips.com/online-casinos/longfu88/",
   "body_words": 1836,
   "keywords_in_total": {
    "Longfu88": 23,
    "Longfu 88": 0,
    "Longfu88 casino": 3,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h1": {
    "Longfu88": 1,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h2": {
    "Longfu88": 1,
    "Longfu 88": 0,
    "Longfu88 casino": 1,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   }
  },
  {
   "url": "https://longfu88-play.my/",
   "body_words": 3355,
   "keywords_in_total": {
    "Longfu88": 22,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h1": {
    "Longfu88": 1,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h2": {
    "Longfu88": 1,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   }
  },
  {
   "url": "https://longfu88-official.games/",
   "body_words": 1473,
   "keywords_in_total": {
    "Longfu88": 24,
    "Longfu 88": 0,
    "Longfu88 casino": 3,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 2,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h1": {
    "Longfu88": 0,
    "Longfu 88": 0,
    "Longfu88 casino": 1,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h2": {
    "Longfu88": 3,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   }
  },
  {
   "url": "https://longfu.net/",
   "body_words": 1957,
   "keywords_in_total": {
    "Longfu88": 7,
    "Longfu 88": 2,
    "Longfu88 casino": 6,
    "Longfu88 login": 3,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 2,
    "casino Longfu88": 2,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 10,
    "Longfu sports": 0
   },
   "keywords_in_h1": {
    "Longfu88": 0,
    "Longfu 88": 0,
    "Longfu88 casino": 1,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 0,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 0,
    "Longfu sports": 0
   },
   "keywords_in_h2": {
    "Longfu88": 1,
    "Longfu 88": 0,
    "Longfu88 casino": 1,
    "Longfu88 login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 0,
    "Longfu88 promo code": 0,
    "Longfu 88 casino": 1,
    "casino Longfu88": 0,
    "Lngfu88 withdrawal time": 0,
    "Longfu 88 Official Site": 0,
    "Longfu": 2,
    "Longfu sports": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 1836,
  "keyword_targets": {
   "Longfu88": 22,
   "Longfu 88": 1,
   "Longfu88 casino": 3,
   "Longfu88 login": 1,
   "Longfu88 bonus": 1,
   "Longfu88 app": 1,
   "Longfu88 promo code": 1,
   "Longfu 88 casino": 1,
   "casino Longfu88": 1,
   "Lngfu88 withdrawal time": 1,
   "Longfu 88 Official Site": 1,
   "Longfu": 1,
   "Longfu sports": 1
  }
 },
 "heading_clusters": [
  {
   "id": "k02",
   "canonical_title": "Games Overview",
   "topic": "Games overview",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 70,
   "avg_position": 0.36,
   "examples": [
    "Available Games at Longfu88",
    "Casino Games",
    "Casino games",
    "Game Selection and Software Providers"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Sports Betting",
   "topic": "Sports betting and esports",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 90,
   "avg_position": 0.37,
   "examples": [
    "Sports Betting – Bet on Your Favorite Sports",
    "Sportsbook",
    "Sports Betting Through SABA Sports",
    "Bet on Global Sports Events"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Bonuses and Welcome Offers",
   "topic": "Bonuses and welcome offers",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 92,
   "avg_position": 0.39,
   "examples": [
    "Bonuses – Boost Your Play with Generous Offers",
    "Bonus Crab",
    "How do I claim my bonus?",
    "Bonuses & promotions"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Live Casino",
   "topic": "Live casino",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 69,
   "avg_position": 0.45,
   "examples": [
    "Longfu 88 Live Casino",
    "Live Dealer Games",
    "Experience Live Dealer Gaming",
    "Live Casino"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Payment Methods",
   "topic": "Deposit methods and payments",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 98,
   "avg_position": 0.54,
   "examples": [
    "Deposit Methods at Longfu 88",
    "Deposits & withdrawals",
    "Deposit methods",
    "Banking Methods and Transaction Processing"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "Safety and Fair Play",
   "topic": "Licence, security and fair play",
   "frequency": 4,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 135,
   "avg_position": 0.57,
   "examples": [
    "Licensing & security",
    "Security Measures and Fair Gaming",
    "Payment Security and Fraud Prevention",
    "Is Longfu88 Safe? Security and Fair Play"
   ]
  },
  {
   "id": "k20",
   "canonical_title": "Responsible Gambling",
   "topic": "Responsible gambling",
   "frequency": 4,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 103,
   "avg_position": 0.69,
   "examples": [
    "Responsible gambling tools",
    "Responsible Gambling Tools",
    "Responsible Gambling",
    "Sokongan Pemain & Permainan Bertanggungjawab"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Mobile Access",
   "topic": "Mobile access and app",
   "frequency": 4,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 101,
   "avg_position": 0.71,
   "examples": [
    "Mobile & app experience",
    "Mobile Gaming Experience",
    "Mobile Access",
    "Pengalaman Mudah Alih (Mobile UX) Tanpa Aplikasi Berat"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "Slots",
   "topic": "Slots",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 94,
   "avg_position": 0.33,
   "examples": [
    "Slots",
    "Slots",
    "Slot: Dunia Gulungan Untuk Semua Gaya",
    "Variasi Mesin Slot & Rahsia Pusingan Pertaruhan (TO)"
   ]
  },
  {
   "id": "k01",
   "canonical_title": "About the Casino",
   "topic": "Platform overview / about the casino",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 88,
   "avg_position": 0.43,
   "examples": [
    "About LongFu88",
    "LongFu88 overview",
    "Platform Overview",
    "Sorotan Menyeluruh: Permainan, Bonus, Pembayaran & Kebolehpercayaan"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "VIP Programme",
   "topic": "VIP programme and loyalty",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 115,
   "avg_position": 0.46,
   "examples": [
    "VIP Program and Loyalty Rewards",
    "VIP Programme – Bronze to Diamond",
    "Butiran Program VIP",
    "Keistimewaan Ahli VIP & Keutamaan Pengeluaran (Cuci)"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Ongoing Promotions",
   "topic": "Ongoing promotions and tournaments",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 109,
   "avg_position": 0.49,
   "examples": [
    "Ongoing Promotions",
    "Tournament Competitions and Promotions",
    "Ganjaran Berterusan Untuk Pemain Sedia Ada"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Customer Support",
   "topic": "Customer support",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 135,
   "avg_position": 0.71,
   "examples": [
    "Customer Support",
    "Customer support",
    "Customer Support Channels"
   ]
  },
  {
   "id": "k21",
   "canonical_title": "Verdict",
   "topic": "Verdict and conclusion",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 178,
   "avg_position": 0.85,
   "examples": [
    "Our verdict on LongFu88",
    "Should You Play at Longfu88?",
    "Ringkasan: Mengapa Memilih Longfu 88 Casino?",
    "Kesimpulan: Platform Stabil Dengan Proses Kewangan Pantas"
   ]
  },
  {
   "id": "k22",
   "canonical_title": "Frequently Asked Questions",
   "topic": "FAQ",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 26,
   "avg_position": 0.85,
   "examples": [
    "FAQs – Your Questions Answered",
    "FAQ",
    "Soalan Lazim (FAQ) - Longfu88"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Instant and Specialty Games",
   "topic": "Fishing, P2P, fast and free games",
   "frequency": 2,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 50,
   "avg_position": 0.27,
   "examples": [
    "Dive into Fishing",
    "P2P – Play Against Other Players",
    "Fast Games – Quick, Instant Wins",
    "Free games"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Table Games",
   "topic": "Table games and video poker",
   "frequency": 2,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 42,
   "avg_position": 0.3,
   "examples": [
    "Table games",
    "Permainan Meja & Video Poker"
   ]
  },
  {
   "id": "k23",
   "canonical_title": "Pros and Cons",
   "topic": "Pros and cons",
   "frequency": 2,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 50,
   "avg_position": 0.5,
   "examples": [
    "Longfu88 Review – What Works and What to Know",
    "Strengths",
    "Worth knowing before you deposit",
    "Kelebihan & Kekurangan Longfu Casino"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Withdrawals",
   "topic": "Withdrawals and payout speed",
   "frequency": 2,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 102,
   "avg_position": 0.63,
   "examples": [
    "Withdrawal methods",
    "Ujian Pembayaran: Berapa Cepat Boleh \"Cuci\"?"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Registration and Login",
   "topic": "Registration and login",
   "frequency": 2,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 76,
   "avg_position": 0.68,
   "examples": [
    "Easy Registration and Seamless Login – Getting Started at Longfu88",
    "Steps to Register:",
    "How do I register at Longfu88?",
    "Akses Link Rasmi & Sistem Log Masuk Auto"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "Crypto Payments",
   "topic": "Cryptocurrency payments",
   "frequency": 2,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 37,
   "avg_position": 0.87,
   "examples": [
    "Can I use cryptocurrency to deposit?",
    "Era Baharu Pembayaran Kripto"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Lottery",
   "topic": "Lottery",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 30,
   "avg_position": 0.4,
   "examples": [
    "Lottery"
   ]
  },
  {
   "id": "k26",
   "canonical_title": "Hands-on Experience",
   "topic": "Hands-on experience: access and payout test",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 65,
   "avg_position": 0.58,
   "examples": [
    "Pengalaman Sebenar: Akses Pantas & Ujian Sistem Pembayaran"
   ]
  },
  {
   "id": "k25",
   "canonical_title": "Quick Links",
   "topic": "Quick links",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 48,
   "avg_position": 0.65,
   "examples": [
    "Quick Links"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Game Providers",
   "topic": "Software providers",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 204,
   "avg_position": 0.83,
   "examples": [
    "Game Provider Partnerships"
   ]
  },
  {
   "id": "k24",
   "canonical_title": "User Reviews",
   "topic": "User reviews",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 66,
   "avg_position": 1.0,
   "examples": [
    "User Reviews"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "VIP",
   "competitors": 4
  },
  {
   "entity": "USDT",
   "competitors": 4
  },
  {
   "entity": "Olympus",
   "competitors": 4
  },
  {
   "entity": "Free Spins",
   "competitors": 4
  },
  {
   "entity": "Sweet Bonanza",
   "competitors": 4
  },
  {
   "entity": "Gates",
   "competitors": 4
  },
  {
   "entity": "Megaways",
   "competitors": 4
  },
  {
   "entity": "MYR",
   "competitors": 3
  },
  {
   "entity": "Malaysia",
   "competitors": 3
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 3
  },
  {
   "entity": "DuitNow",
   "competitors": 3
  },
  {
   "entity": "Bitcoin",
   "competitors": 3
  },
  {
   "entity": "Baccarat",
   "competitors": 3
  },
  {
   "entity": "GrabPay",
   "competitors": 3
  },
  {
   "entity": "Ethereum",
   "competitors": 3
  },
  {
   "entity": "Mastercard",
   "competitors": 3
  },
  {
   "entity": "Diamond",
   "competitors": 3
  },
  {
   "entity": "Visa",
   "competitors": 3
  },
  {
   "entity": "SSL",
   "competitors": 3
  },
  {
   "entity": "Asian",
   "competitors": 3
  },
  {
   "entity": "Sic Bo",
   "competitors": 3
  },
  {
   "entity": "Dota 2",
   "competitors": 3
  },
  {
   "entity": "Gambling Therapy",
   "competitors": 3
  },
  {
   "entity": "Wallet",
   "competitors": 2
  },
  {
   "entity": "Touch",
   "competitors": 2
  },
  {
   "entity": "MYR 2",
   "competitors": 2
  },
  {
   "entity": "Singapore",
   "competitors": 2
  },
  {
   "entity": "Live Casino",
   "competitors": 2
  },
  {
   "entity": "Register",
   "competitors": 2
  },
  {
   "entity": "Hacksaw Gaming",
   "competitors": 2
  },
  {
   "entity": "Cardano",
   "competitors": 2
  },
  {
   "entity": "Bank Transfer",
   "competitors": 2
  },
  {
   "entity": "RTP",
   "competitors": 2
  },
  {
   "entity": "Android",
   "competitors": 2
  },
  {
   "entity": "Roulette",
   "competitors": 2
  },
  {
   "entity": "Malaysian",
   "competitors": 2
  },
  {
   "entity": "Gold",
   "competitors": 2
  },
  {
   "entity": "KYC",
   "competitors": 2
  },
  {
   "entity": "Blackjack",
   "competitors": 2
  },
  {
   "entity": "Neteller",
   "competitors": 2
  },
  {
   "entity": "Skrill",
   "competitors": 2
  },
  {
   "entity": "Evolution",
   "competitors": 2
  },
  {
   "entity": "Crazy Time",
   "competitors": 2
  },
  {
   "entity": "Online Banking",
   "competitors": 2
  },
  {
   "entity": "Tether",
   "competitors": 2
  },
  {
   "entity": "RNG",
   "competitors": 2
  },
  {
   "entity": "Silver",
   "competitors": 2
  },
  {
   "entity": "Platinum",
   "competitors": 2
  },
  {
   "entity": "Bronze",
   "competitors": 2
  },
  {
   "entity": "MYR 1",
   "competitors": 2
  },
  {
   "entity": "MYR 30",
   "competitors": 2
  },
  {
   "entity": "Casino Games",
   "competitors": 2
  },
  {
   "entity": "Customer Support",
   "competitors": 2
  },
  {
   "entity": "Lottery",
   "competitors": 2
  },
  {
   "entity": "Payment Methods",
   "competitors": 2
  },
  {
   "entity": "Starburst",
   "competitors": 2
  },
  {
   "entity": "Minimum Deposit",
   "competitors": 2
  },
  {
   "entity": "Live Chat",
   "competitors": 2
  },
  {
   "entity": "Responsible Gambling Tools",
   "competitors": 2
  },
  {
   "entity": "Gaming",
   "competitors": 2
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
    "url": "https://www.mightytips.com/online-casinos/longfu88/",
    "heading": "LongFu88 overview",
    "rows": [
     [
      "üîê Licensing",
      "Undisclosed"
     ],
     [
      "üéÅ Welcome bonus",
      "200% Welcome Bonus and 60 Free Spins"
     ],
     [
      "üí∞ Minimum deposit",
      "30 MYR / 300 THB"
     ],
     [
      "üí≥ Payment methods",
      "Mastercard, QR, Touch&Go, Bitcoin, Litecoin"
     ],
     [
      "üìà Table limits",
      "0.5 MYR - 1,000 MYR / 200 THB - 100,000 THB (Limit will vary between tables)"
     ],
     [
      "üé∞ Number of games",
      "7,500+"
     ],
     [
      "üñ•Ô∏èSoftware providers",
      "NetEnt, Hacksaw Gaming, Pragmatic Play, Spinomenal, 1x2 Gaming"
     ],
     [
      "ÔºÖ Payout percentage",
      "Not specified"
     ],
     [
      "‚è±Ô∏è Payout time",
      "Cryptocurrency - Under 60 minutes Fiat Methods - 24-72 hours"
     ],
     [
      "üí∏ Maximum payout",
      "184,000 THB / 30,000 MYR"
     ],
     [
      "üí¨ Customer support",
      "24/7 live chat, email"
     ],
     [
      "üîù Top feature",
      "Weekly Tournaments and Challenges"
     ]
    ]
   },
   {
    "competitor": 1,
    "url": "https://www.mightytips.com/online-casinos/longfu88/",
    "heading": "User Reviews",
    "rows": [
     [
      "Title",
      "LongFu88"
     ],
     [
      "Website",
      "www.longfu88.com"
     ],
     [
      "Established",
      "2025"
     ],
     [
      "Phone",
      "None"
     ],
     [
      "Email",
      "support@longfu88.com"
     ],
     [
      "Payments",
      "Bitcoin , Mastercard , Visa , Credit Card , Debit Card , Ethereum, Litecoin, Tether, Ripple, Bitcoin Cash, Cardano, Bank"
     ]
    ]
   },
   {
    "competitor": 3,
    "url": "https://longfu88-play.my/",
    "heading": "Platform Overview",
    "rows": [
     [
      "Detail",
      "Value"
     ],
     [
      "Established",
      "2020"
     ],
     [
      "Licence",
      "Curacao eGaming"
     ],
     [
      "Welcome Offer",
      "188% up to $2,088 + 18 Free Spins"
     ],
     [
      "Minimum Deposit",
      "$20"
     ],
     [
      "Withdrawal Speed",
      "12-24 hours (e-wallets), 2-5 days (bank transfer)"
     ],
     [
      "Top Games",
      "Gates of Olympus, Sweet Bonanza, Crazy Time, Mega Moolah, Book of Dead"
     ],
     [
      "Mobile Platform",
      "Responsive web design (iOS & Android)"
     ],
     [
      "Customer Support",
      "24/7 Live Chat, Email, Phone"
     ],
     [
      "Payment Methods",
      "Visa, Mastercard, Bank Transfer, Skrill, Neteller, Bitcoin, Ethereum, USDT"
     ],
     [
      "Software Providers",
      "Pragmatic Play, Evolution Gaming, NetEnt, Microgaming, Play'n GO, Red Tiger, SABA Sports, 30+ total"
     ]
    ]
   }
  ],
  "labels": [
   {
    "label": "established",
    "competitors": 2
   },
   {
    "label": "customer support",
    "competitors": 1
   },
   {
    "label": "detail",
    "competitors": 1
   },
   {
    "label": "email",
    "competitors": 1
   },
   {
    "label": "licence",
    "competitors": 1
   },
   {
    "label": "minimum deposit",
    "competitors": 1
   },
   {
    "label": "mobile platform",
    "competitors": 1
   },
   {
    "label": "payment methods",
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
    "label": "software providers",
    "competitors": 1
   },
   {
    "label": "title",
    "competitors": 1
   },
   {
    "label": "top games",
    "competitors": 1
   },
   {
    "label": "website",
    "competitors": 1
   },
   {
    "label": "welcome offer",
    "competitors": 1
   },
   {
    "label": "withdrawal speed",
    "competitors": 1
   },
   {
    "label": "ôºö payout percentage",
    "competitors": 1
   },
   {
    "label": "‚è±ô∏è payout time",
    "competitors": 1
   },
   {
    "label": "üéå welcome bonus",
    "competitors": 1
   },
   {
    "label": "üé∞ number of games",
    "competitors": 1
   },
   {
    "label": "üìà table limits",
    "competitors": 1
   },
   {
    "label": "üí¨ customer support",
    "competitors": 1
   },
   {
    "label": "üí∏ maximum payout",
    "competitors": 1
   },
   {
    "label": "üí∞ minimum deposit",
    "competitors": 1
   },
   {
    "label": "üí≥ payment methods",
    "competitors": 1
   },
   {
    "label": "üîê licensing",
    "competitors": 1
   },
   {
    "label": "üîù top feature",
    "competitors": 1
   },
   {
    "label": "üñ•ô∏èsoftware providers",
    "competitors": 1
   }
  ]
 }
}

Your previous answer had these problems, fix them all:
- keyword "Longfu88 casino": blocks+headings sum to 4, target 3
- knowledge base: b03: path not found: brandinfo_privacy_policy.privacy_policy.terms_conditions.eligibility (stopped after ".brandinfo_privacy_policy.privacy_policy")

Previous answer:
{"intent_summary": "Brand-related (navigational and informational) review page about the Longfu88 online casino for players from Singapore: what the casino is, key facts, licence and data protection, registration, login and verification, welcome bonus and its terms, reloads, cashback and rewards, VIP programme, games and providers, sports betting, payments and withdrawals, mobile access, responsible gambling, support, pros and cons, FAQ and verdict. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore.", "blocks": [{"level": 1, "heading": "Longfu88 Casino Review for Singapore Players", "source": "h1", "covers_clusters": [], "kb_refs": ["brandinfo_general.release_year", "brandinfo_general.minimum_age", "brandinfo_games.game_types"], "words_min": 66, "words_max": 84, "keywords": {"Longfu88": 2, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Online Casino", "priority": 10}, {"name": "Players from Singapore", "priority": 8}, {"name": "Game Categories", "priority": 7}, {"name": "Sportsbook", "priority": 6}], "entity_connections": [{"subject": "Online Casino", "relation": "combines", "object": "casino games, live dealer games, sports betting and lottery", "priority": 8}, {"subject": "Adult Players", "relation": "must be at least", "object": "18 years old", "priority": 7}], "summary": "Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Singapore.", "copywriter_notes": "Open with the keyword \"Longfu88\" as the subject of the first sentence, followed by a definition of the online casino by its game areas (slots, live dealer games, table games, jackpots, fishing, P2P, fast games, lottery, crash and instant games) and a sportsbook, and the launch year from the Brand Information. State the 18+ age limit once. Say that the page is written for players from Singapore. NEVER say or imply that the casino is licensed, legal or approved in Singapore; the licence named in the Brand Information is the only licence statement. Use \"Longfu88\" exactly twice and no other tracked keyword. No bonus amounts, payment or registration details here; only signpost the topics of the page (facts, licence, bonuses, games, payments, mobile play, responsible gambling). Neutral-positive tone, no promises of winnings.", "id": "b01", "words": 75, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 1, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_general.release_year", "value": 2026}, {"path": "brandinfo_general.minimum_age", "value": 18}, {"path": "brandinfo_games.game_types", "value": ["Slots", "Live dealer games", "Table games", "Jackpots", "Fishing", "P2P games", "Fast games", "Lottery", "Crash & instant games"]}]}, {"level": 2, "heading": "Casino Facts at a Glance", "source": "unique", "covers_clusters": [], "kb_refs": ["brandinfo_privacy_policy.privacy_policy.data_controller.company_name", "brandinfo_general.licences[0]", "brandinfo_general.release_year", "brandinfo_general.customer_support.languages", "brandinfo_general.currencies", "brandinfo_general.payment_methods.deposit", "brandinfo_general.welcome_bonus_summary", "brandinfo_promotions.other_bonuses[9].reward", "brandinfo_general.minimum_deposit", "brandinfo_general.customer_support.email", "brandinfo_general.customer_support.channels"], "words_min": 75, "words_max": 95, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["table"], "entities": [{"name": "Operator", "priority": 8}, {"name": "Gambling Licence", "priority": 8}, {"name": "Welcome Bonus", "priority": 7}, {"name": "Payment Methods", "priority": 6}, {"name": "Currencies", "priority": 5}, {"name": "Customer Support", "priority": 5}], "entity_connections": [{"subject": "Gambling Licence", "relation": "belongs to", "object": "the Online Casino", "priority": 7}, {"subject": "Welcome Bonus", "relation": "is offered by", "object": "the Online Casino", "priority": 6}], "summary": "A compact fact sheet of the casino: operator, licence, launch year, support languages, currencies, payment methods, welcome bonus, cashback, minimum deposit and support e-mail.", "copywriter_notes": "The table has exactly the rows of the Fact Table list, in this order, nothing else; the left cell is the row label, the right cell a short fact (a figure, a name or a comma-separated list, at most 20 words), no sentences. Licence = jurisdiction, operator and registration number as given. Welcome bonus = the summary line as given, shortened to the percentage, the maximum amount and the number of free spins. Cashback = the percentage and its base only (weekly net casino losses). Minimum deposit = the general minimum deposit of the casino (€10); do not use the €50 of the welcome bonus here. Payment methods = five or six well-known names taken from the list (for example Visa, Mastercard, Bank Transfer, Bitcoin, USDT, PayNow), not the whole list. Currencies and support languages = names only. Support = the e-mail address exactly as given plus the live chat: the e-mail contains the tracked keyword \"Longfu88\", which is the one occurrence this block allows; no other tracked keyword here. Do not add a lead-in sentence or closing text.", "listed_entities": ["Operator", "Gambling Licence", "Welcome Bonus", "Payment Methods", "Currencies", "Customer Support"], "fact_table": [{"key": "company", "label": "Operator", "kb_refs": ["brandinfo_privacy_policy.privacy_policy.data_controller.company_name"], "values": [{"path": "brandinfo_privacy_policy.privacy_policy.data_controller.company_name", "value": "Lumina"}]}, {"key": "licence", "label": "Licence", "kb_refs": ["brandinfo_general.licences[0]"], "values": [{"path": "brandinfo_general.licences[0]", "value": {"jurisdiction": "Costa Rica", "operator": "Lumina", "registration_number": "000-039123-R-319326-001"}}]}, {"key": "founded", "label": "Launched", "kb_refs": ["brandinfo_general.release_year"], "values": [{"path": "brandinfo_general.release_year", "value": 2026}]}, {"key": "languages", "label": "Support languages", "kb_refs": ["brandinfo_general.customer_support.languages"], "values": [{"path": "brandinfo_general.customer_support.languages", "value": ["English", "Malay", "Simplified Chinese", "Thai", "Indonesian", "Vietnamese"]}]}, {"key": "currencies", "label": "Currencies", "kb_refs": ["brandinfo_general.currencies"], "values": [{"path": "brandinfo_general.currencies", "value": ["EUR", "USD", "MYR", "THB", "SGD", "USDT"]}]}, {"key": "payment_methods", "label": "Payment methods", "kb_refs": ["brandinfo_general.payment_methods.deposit"], "values": [{"path": "brandinfo_general.payment_methods.deposit", "value": ["QRIS", "DANA", "OVO Wallet", "Mandiri", "BNI", "Bank Transfer", "Visa", "Mastercard", "USDT (TRC20)", "USDT (ERC20)", "USDT (BEP20)", "Bitcoin", "Ethereum", "Litecoin", "Ripple", "USDC", "Bitcoin Cash", "Cardano", "Touch'n Go", "GrabPay", "DuitNow", "Online Banking", "DBS Bank", "OCBC Bank", "PromptPay QR", "MoMo", "Zalo", "ViettelPay", "VietQR", "Sofort", "Giropay", "PayNow QR", "BCA", "PayNow", "Neteller", "Skrill"]}]}, {"key": "welcome_bonus", "label": "Welcome bonus", "kb_refs": ["brandinfo_general.welcome_bonus_summary"], "values": [{"path": "brandinfo_general.welcome_bonus_summary", "value": "188% up to €2,088 + 18 Free Spins; 25x deposit plus bonus, 40x Free Spins winnings."}]}, {"key": "cashback", "label": "Cashback", "kb_refs": ["brandinfo_promotions.other_bonuses[9].reward"], "values": [{"path": "brandinfo_promotions.other_bonuses[9].reward", "value": "Up to 10% of weekly net casino losses, capped at €6,988"}]}, {"key": "min_deposit", "label": "Minimum deposit", "kb_refs": ["brandinfo_general.minimum_deposit"], "values": [{"path": "brandinfo_general.minimum_deposit", "value": "€10"}]}, {"key": "support", "label": "Support", "kb_refs": ["brandinfo_general.customer_support.email", "brandinfo_general.customer_support.channels"], "values": [{"path": "brandinfo_general.customer_support.email", "value": "support@longfu88.com"}, {"path": "brandinfo_general.customer_support.channels", "value": ["24/7 live chat", "Email"]}]}], "id": "b02", "words": 85, "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_privacy_policy.privacy_policy.data_controller.company_name", "value": "Lumina"}, {"path": "brandinfo_general.licences[0]", "value": {"jurisdiction": "Costa Rica", "operator": "Lumina", "registration_number": "000-039123-R-319326-001"}}, {"path": "brandinfo_general.release_year", "value": 2026}, {"path": "brandinfo_general.customer_support.languages", "value": ["English", "Malay", "Simplified Chinese", "Thai", "Indonesian", "Vietnamese"]}, {"path": "brandinfo_general.currencies", "value": ["EUR", "USD", "MYR", "THB", "SGD", "USDT"]}, {"path": "brandinfo_general.payment_methods.deposit", "value": ["QRIS", "DANA", "OVO Wallet", "Mandiri", "BNI", "Bank Transfer", "Visa", "Mastercard", "USDT (TRC20)", "USDT (ERC20)", "USDT (BEP20)", "Bitcoin", "Ethereum", "Litecoin", "Ripple", "USDC", "Bitcoin Cash", "Cardano", "Touch'n Go", "GrabPay", "DuitNow", "Online Banking", "DBS Bank", "OCBC Bank", "PromptPay QR", "MoMo", "Zalo", "ViettelPay", "VietQR", "Sofort", "Giropay", "PayNow QR", "BCA", "PayNow", "Neteller", "Skrill"]}, {"path": "brandinfo_general.welcome_bonus_summary", "value": "188% up to €2,088 + 18 Free Spins; 25x deposit plus bonus, 40x Free Spins winnings."}, {"path": "brandinfo_promotions.other_bonuses[9].reward", "value": "Up to 10% of weekly net casino losses, capped at €6,988"}, {"path": "brandinfo_general.minimum_deposit", "value": "€10"}, {"path": "brandinfo_general.customer_support.email", "value": "support@longfu88.com"}, {"path": "brandinfo_general.customer_support.channels", "value": ["24/7 live chat", "Email"]}]}, {"level": 2, "heading": "Longfu88 Casino Overview", "source": "mandatory", "covers_clusters": ["k01"], "kb_refs": ["brandinfo_general.release_year", "brandinfo_general.currencies", "brandinfo_privacy_policy.privacy_policy.terms_conditions.eligibility"], "words_min": 53, "words_max": 67, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 1, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Online Casino", "priority": 10}, {"name": "Official Website", "priority": 7}, {"name": "Account Currencies", "priority": 5}, {"name": "Player Eligibility", "priority": 6}], "entity_connections": [{"subject": "Online Casino", "relation": "was launched", "object": "in 2026", "priority": 7}, {"subject": "Players", "relation": "must be", "object": "legally permitted to gamble where they live", "priority": 6}], "summary": "What the casino is for a player from Singapore: launch year, account currencies, the official website and who may play.", "copywriter_notes": "Give the launch year (2026) and the account currencies from the Brand Information (including SGD). Mention the official website once with the keyword \"Longfu 88 Official Site\" in a natural phrase, for example that players should use the Longfu 88 Official Site address and not look-alike pages (this is advice, not a fact claim about domains). Explain who may play: 18+, legally permitted to gamble in the place of residence, one personal account, no third-party payment methods. NEVER say or imply that the casino is licensed, legal or approved in Singapore; the licence named in the Brand Information is the only licence statement. Use \"Longfu88\" exactly once and \"Longfu 88 Official Site\" exactly once, and no other tracked keyword. Do not repeat the licence or bonus details (later sections).", "id": "b03", "words": 60, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 1, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_general.release_year", "value": 2026}, {"path": "brandinfo_general.currencies", "value": ["EUR", "USD", "MYR", "THB", "SGD", "USDT"]}]}, {"level": 2, "heading": "Licence, Operator and Data Protection", "source": "mandatory", "covers_clusters": ["k18"], "kb_refs": ["brandinfo_general.licences[0]", "brandinfo_privacy_policy.privacy_policy.data_controller", "brandinfo_privacy_policy.privacy_policy.security", "brandinfo_privacy_policy.privacy_policy.data_sharing", "brandinfo_privacy_policy.privacy_policy.data_subject_rights", "brandinfo_privacy_policy.terms_conditions.account_terms"], "words_min": 92, "words_max": 118, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 1, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Gambling Licence", "priority": 10}, {"name": "Operator", "priority": 8}, {"name": "Data Protection", "priority": 8}, {"name": "Data Controller", "priority": 6}, {"name": "Account Security", "priority": 6}], "entity_connections": [{"subject": "Gambling Licence", "relation": "is held by", "object": "the operator", "priority": 8}, {"subject": "Operator", "relation": "protects", "object": "accounts, payments and personal data with technical and organisational safeguards", "priority": 7}], "summary": "Who licenses and runs the casino (jurisdiction, operator, registration number) and how personal data and accounts are protected.", "copywriter_notes": "Lead with the licence: jurisdiction Costa Rica, the operator named there (Lumina) and the registration number, exactly as in the Brand Information. The operator also acts as the data controller; the data protection officer is reached at the e-mail given in the privacy policy (print it only if it fits; it contains the tracked keyword \"Longfu88\", which then counts). Explain what data is collected in one sentence, who it may be shared with (payment service providers, identity verification providers, technology providers, regulators and law enforcement when required) and which rights the player has (access, rectification, erasure where legally permitted, restriction, objection, portability, withdrawal of consent). The account holder is responsible for safeguarding credentials. Use the phrase \"casino Longfu88\" exactly once, in a natural sentence about the licence. NEVER say or imply that the casino is licensed, legal or approved in Singapore; the licence named in the Brand Information is the only licence statement. Do not claim an audit, eCOGRA, RNG certificate, SSL or any other certification: none is given. Use \"Longfu88\" exactly once and \"casino Longfu88\" exactly once and no other tracked keyword. Do not repeat identity-check details (next section).", "id": "b04", "words": 105, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_general.licences[0]", "value": {"jurisdiction": "Costa Rica", "operator": "Lumina", "registration_number": "000-039123-R-319326-001"}}, {"path": "brandinfo_privacy_policy.privacy_policy.data_controller", "value": {"company_name": "Lumina", "contact_email": "dpo@longfu88.com", "contact_details": "support@longfu88.com"}}, {"path": "brandinfo_privacy_policy.privacy_policy.security", "value": "Technical and organizational safeguards protect accounts, payments and personal information."}, {"path": "brandinfo_privacy_policy.privacy_policy.data_sharing", "value": ["Payment service providers", "Identity verification providers", "Technology providers", "Regulators and law enforcement when required"]}, {"path": "brandinfo_privacy_policy.privacy_policy.data_subject_rights", "value": ["Access", "Rectification", "Erasure where legally permitted", "Restriction", "Objection", "Portability where applicable", "Withdrawal of consent"]}, {"path": "brandinfo_privacy_policy.terms_conditions.account_terms", "value": ["The account holder is responsible for safeguarding credentials.", "The operator may suspend activity for verification or suspected abuse."]}]}, {"level": 2, "heading": "Registration and Login", "source": "unique", "covers_clusters": ["k13"], "kb_refs": ["brandinfo_account.registration", "brandinfo_account.login"], "words_min": 88, "words_max": 112, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 1, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "list"], "entities": [{"name": "Registration", "priority": 10}, {"name": "Login", "priority": 8}, {"name": "Password Recovery", "priority": 6}, {"name": "Two Accounts Rule", "priority": 5}, {"name": "Email Confirmation", "priority": 5}], "entity_connections": [{"subject": "Registration", "relation": "requires", "object": "email, password, legal name, date of birth and residential address", "priority": 8}, {"subject": "Player", "relation": "may hold", "object": "only one personal account", "priority": 7}], "summary": "How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.", "copywriter_notes": "One lead-in sentence, then a NUMBERED list with the five registration steps in order as given in the Brand Information, then a short paragraph on login (select Login, enter registered email and password, complete any security check) and password recovery (Forgot Password on the login screen, reset link by email). Mention the required details (email, password, legal name, date of birth, residential address) and the rule of one personal account per player. Use the keyword \"Longfu88 login\" exactly once, in the login paragraph. Use \"Longfu88\" exactly once and no other tracked keyword besides those named; do not put tracked keywords into list items unless the verbatim step contains the brand. Do not mention the identity-document check here (next sub-section).", "id": "b05", "words": 100, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_account.registration", "value": {"methods": ["Email registration"], "required_details": ["Email", "Password", "Legal name", "Date of birth", "Residential address"], "steps": ["Open Longfu88 and select Register.", "Enter email and create a password.", "Confirm age and acceptance of Terms and Conditions and Privacy Policy.", "Complete the additional personal details and residential address.", "Select Create Account and complete any requested email confirmation."], "eligibility": ["18+ and of legal gambling age in the relevant jurisdiction.", "Only one personal account per player."]}}, {"path": "brandinfo_account.login", "value": {"method": "Email and password", "steps": ["Select Login on the website.", "Enter registered email and password.", "Complete any security check and access the account."], "password_recovery": ["Choose Forgot Password on the login screen.", "Request a reset link using the registered email.", "Follow the emailed instructions to set a new password."]}}]}, {"level": 3, "heading": "Identity Verification Before Withdrawals", "source": "unique", "covers_clusters": [], "kb_refs": ["brandinfo_account.verification", "brandinfo_privacy_policy.kyc_aml.required_documents", "brandinfo_privacy_policy.kyc_aml.processing_time", "brandinfo_privacy_policy.kyc_aml.failure_consequences"], "words_min": 62, "words_max": 78, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "list"], "entities": [{"name": "KYC Verification", "priority": 10}, {"name": "Identity Documents", "priority": 8}, {"name": "Proof of Address", "priority": 6}, {"name": "Source of Funds", "priority": 5}], "entity_connections": [{"subject": "Verification", "relation": "may be required", "object": "before a withdrawal", "priority": 8}, {"subject": "Complete Document Set", "relation": "is reviewed within", "object": "10 days", "priority": 7}], "summary": "When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.", "copywriter_notes": "State the triggers (before withdrawal, unusual or high-value transactions, changes to account or payment details), give the document types as a compact bulleted list (identity: passport, national identity card or driving licence; address: utility bill or bank statement; proof of payment-method ownership; source of funds when requested), the 30-day window to send documents and the review time of up to 10 days after a complete set. Say that withdrawals may be held until the checks are done and that failed checks can mean refused transactions or restrictions. Use \"Longfu88\" exactly once and no other tracked keyword.", "id": "b06", "words": 70, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_account.verification", "value": {"triggers": ["Account review", "Before withdrawal", "Unusual or high-value transactions", "Changes to account or payment details"], "documents": ["Government-issued photo ID or passport", "Proof of residential address", "Proof of ownership of a payment method", "Source of funds or wealth documents when requested"], "procedure": ["Access the verification request in the account or follow the support instructions.", "Upload legible current documents matching the account profile.", "Complete additional telephone or face verification if requested.", "Wait for approval before withdrawal or other restricted activity."], "document_submission_window": "Up to 30 days when requested", "typical_review_time": "Up to 10 days after a complete document set is received"}}, {"path": "brandinfo_privacy_policy.kyc_aml.required_documents", "value": {"identity": ["Passport", "National identity card", "Driving licence"], "address": ["Utility bill", "Bank statement"], "payment_method": ["Bank or card ownership evidence", "Digital wallet ownership evidence"], "source_of_funds": ["Proof of income", "Bank statements", "Other supporting financial documents"]}}, {"path": "brandinfo_privacy_policy.kyc_aml.processing_time", "value": "Normally within 10 days of receipt of a complete document set"}, {"path": "brandinfo_privacy_policy.kyc_aml.failure_consequences", "value": ["Transaction refusal", "Account restrictions", "Withholding of withdrawals pending compliance"]}]}, {"level": 2, "heading": "Welcome Bonus", "source": "mandatory", "covers_clusters": ["k10"], "kb_refs": ["brandinfo_welcome.welcome_bonus.name", "brandinfo_welcome.welcome_bonus.type", "brandinfo_welcome.welcome_bonus.bonus_percentage", "brandinfo_welcome.welcome_bonus.maximum_bonus", "brandinfo_welcome.welcome_bonus.free_spins", "brandinfo_welcome.welcome_bonus.minimum_deposit", "brandinfo_welcome.welcome_bonus.eligibility", "brandinfo_welcome.welcome_bonus.claiming_procedure", "brandinfo_promotions.other_bonuses[0]", "brandinfo_promotions.other_bonuses[1]"], "words_min": 88, "words_max": 112, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 1, "Longfu88 app": 0, "Longfu88 promo code": 1, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "list"], "entities": [{"name": "Casino Welcome Bonus", "priority": 10}, {"name": "Deposit Bonus", "priority": 8}, {"name": "Free Spins", "priority": 7}, {"name": "Minimum Deposit", "priority": 6}, {"name": "My Bonuses", "priority": 5}], "entity_connections": [{"subject": "Casino Welcome Bonus", "relation": "gives", "object": "188% up to €2,088 plus 18 free spins", "priority": 9}, {"subject": "Casino Welcome Bonus", "relation": "is activated", "object": "in My Bonuses before any wager", "priority": 7}], "summary": "The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.", "copywriter_notes": "Name the offer \"Casino Welcome Bonus\" and give 188% up to €2,088 plus 18 Free Spins exactly as in the Brand Information. It is for new registered players on the first qualifying deposit, one welcome offer per account; the qualifying minimum deposit of THIS bonus is €50 (this is not the general minimum deposit of the casino, which is €10: never mix the two). Give the four claiming steps as a short bulleted list (register, make the first qualifying deposit, activate the bonus in My Bonuses before placing any wagers, play eligible games and finish the wagering before expiry). PROMO CODE: the claiming steps contain no code. Use the keyword \"Longfu88 promo code\" exactly once in a sentence that says the claiming route is the My Bonuses activation after the qualifying deposit and that no promo code step is part of the listed claiming procedure; never invent, name or hint at a code. Name the two alternatives in one sentence: the Live Casino Welcome Bonus (125% up to €888, minimum deposit €30) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, minimum deposit 50 USDT); say the Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers. Use the keyword \"Longfu88 bonus\" exactly once. Use \"Longfu88\" exactly once and no other tracked keyword. Do not explain wagering, maximum bet or validity here (next sub-section).", "id": "b07", "words": 100, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_welcome.welcome_bonus.name", "value": "Casino Welcome Bonus"}, {"path": "brandinfo_welcome.welcome_bonus.type", "value": "First deposit casino bonus"}, {"path": "brandinfo_welcome.welcome_bonus.bonus_percentage", "value": 188}, {"path": "brandinfo_welcome.welcome_bonus.maximum_bonus", "value": "€2,088"}, {"path": "brandinfo_welcome.welcome_bonus.free_spins", "value": 18}, {"path": "brandinfo_welcome.welcome_bonus.minimum_deposit", "value": "€50"}, {"path": "brandinfo_welcome.welcome_bonus.eligibility", "value": "New registered players on their first qualifying deposit; one welcome offer per account."}, {"path": "brandinfo_welcome.welcome_bonus.claiming_procedure", "value": ["Register an account and complete the required personal details.", "Make the first qualifying deposit.", "Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.", "Play eligible casino games and complete the wagering before expiry."]}, {"path": "brandinfo_promotions.other_bonuses[0]", "value": {"name": "Live Casino Welcome Bonus", "type": "Live casino welcome", "reward": "125% up to €888", "minimum_deposit": "€30", "wagering_requirement": "30x the deposit plus bonus", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["New players only; first qualifying deposit.", "Maximum bet: €25.", "Neteller and Skrill excluded.", "Must activate before wagering; cannot combine with another active bonus."]}}, {"path": "brandinfo_promotions.other_bonuses[1]", "value": {"name": "Casino Crypto Welcome Bonus", "type": "Crypto casino welcome", "reward": "188% up to 2,888 USDT", "minimum_deposit": "50 USDT", "wagering_requirement": "40x deposit plus bonus", "validity": "10 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["First qualifying crypto deposit only.", "Maximum bonus wager: 5 USDT per spin.", "Casino Welcome Bonus and Crypto Welcome Bonus are alternative first-deposit offers."], "eligible_cryptocurrencies": ["USDT", "BTC", "BCH", "LTC", "ETH", "XRP", "USDC"]}}]}, {"level": 3, "heading": "Wagering, Validity and Bet Limits", "source": "unique", "covers_clusters": [], "kb_refs": ["brandinfo_welcome.welcome_bonus.wagering_requirement", "brandinfo_welcome.welcome_bonus.free_spins_wagering", "brandinfo_welcome.welcome_bonus.validity", "brandinfo_welcome.welcome_bonus.maximum_bet", "brandinfo_welcome.welcome_bonus.maximum_cashout", "brandinfo_welcome.welcome_bonus.important_terms"], "words_min": 62, "words_max": 78, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "table"], "entities": [{"name": "Wagering Requirement", "priority": 10}, {"name": "Maximum Bet", "priority": 7}, {"name": "Maximum Cashout", "priority": 7}, {"name": "Bonus Validity", "priority": 6}, {"name": "Free Spins Winnings", "priority": 6}], "entity_connections": [{"subject": "Wagering Requirement", "relation": "is 25 times", "object": "the deposit plus the bonus amount", "priority": 9}, {"subject": "Bonus", "relation": "expires", "object": "10 days after activation", "priority": 7}], "summary": "The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.", "copywriter_notes": "One lead-in sentence, then a Markdown table Condition | Value with the rows: wagering (25x the deposit plus bonus amount), free spins wagering (40x Free Spins winnings), validity (10 days from activation), maximum bet (€22.5 per spin), maximum cashout (5x the initial bonus amount). After the table, one or two sentences on the exclusions and rules: Neteller and Skrill deposits are excluded, only one promotional bonus can be active at a time, a withdrawal request before claiming or while the bonus is active can void eligibility, cancelling forfeits bonus funds and unconverted winnings, verification may be required before bonus winnings are paid. Use \"Longfu88\" exactly once and no other tracked keyword. Keep tracked keywords out of table cells.", "listed_entities": ["Wagering Requirement", "Maximum Bet", "Maximum Cashout", "Bonus Validity", "Free Spins Winnings"], "id": "b08", "words": 70, "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_welcome.welcome_bonus.wagering_requirement", "value": "25x the deposit plus bonus amount"}, {"path": "brandinfo_welcome.welcome_bonus.free_spins_wagering", "value": "40x Free Spins winnings"}, {"path": "brandinfo_welcome.welcome_bonus.validity", "value": "10 days from activation"}, {"path": "brandinfo_welcome.welcome_bonus.maximum_bet", "value": "€22.5 per spin"}, {"path": "brandinfo_welcome.welcome_bonus.maximum_cashout", "value": "5x the initial bonus amount"}, {"path": "brandinfo_welcome.welcome_bonus.important_terms", "value": ["Neteller and Skrill deposits are excluded from this promotion.", "Free Spins winnings have separate wagering requirements.", "Only one promotional bonus may be active at a time.", "A withdrawal request before claiming or while the bonus is active can void promotional eligibility.", "Cancelling the promotion forfeits bonus funds and unconverted promotional winnings.", "Account verification may be required before payment of promotional winnings."]}]}, {"level": 2, "heading": "Reloads and Seasonal Promotions", "source": "mandatory", "covers_clusters": ["k11"], "kb_refs": ["brandinfo_promotions.other_bonuses[2]", "brandinfo_promotions.other_bonuses[3]", "brandinfo_promotions.other_bonuses[4]", "brandinfo_promotions.other_bonuses[5]", "brandinfo_promotions.other_bonuses[6]", "brandinfo_promotions.other_bonuses[7]", "brandinfo_promotions.other_bonuses[8]"], "words_min": 75, "words_max": 95, "keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "table"], "entities": [{"name": "Weekly Reload", "priority": 9}, {"name": "Weekend Reload", "priority": 8}, {"name": "Crypto Reload", "priority": 7}, {"name": "One-Day Reload Special", "priority": 5}, {"name": "Seasonal Promotion", "priority": 5}, {"name": "Free Spins", "priority": 5}], "entity_connections": [{"subject": "Weekly Reload", "relation": "gives", "object": "50 Free Spins", "priority": 7}, {"subject": "Promotions", "relation": "cannot be combined with", "object": "another active casino bonus", "priority": 8}], "summary": "The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.", "copywriter_notes": "One lead-in sentence, then a Markdown table Offer | Reward | Min. deposit | Wagering | Validity for the seven offers as given: Casino Weekly Reload, Casino Weekly Crypto Reload, Casino Weekend Reload, Casino Weekend Crypto Reload, Casino Double Fortune (one-day reload special), Casino Trick or Treat Pumpkin Bonanza, Casino Dragon Quest (verification reward). After the table state the shared rules once: activation in My Bonuses, one claim per promotional period, no combination with another active casino bonus, maximum stake €5 per spin while wagering bonus funds. Use no tracked keyword in the body of this block.", "listed_entities": ["Weekly Reload", "Weekend Reload", "Crypto Reload", "One-Day Reload Special", "Seasonal Promotion"], "id": "b09", "words": 85, "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_promotions.other_bonuses[2]", "value": {"name": "Casino Weekly Reload", "type": "Weekly free spins", "reward": "50 Free Spins", "minimum_deposit": "€30", "wagering_requirement": "40x winnings from Free Spins", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}}, {"path": "brandinfo_promotions.other_bonuses[3]", "value": {"name": "Casino Weekly Crypto Reload", "type": "Crypto weekly reload", "reward": "60% up to 1,000 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}}, {"path": "brandinfo_promotions.other_bonuses[4]", "value": {"name": "Casino Weekend Reload", "type": "Weekend deposit bonus", "reward": "Up to €3,360 + 50 Free Spins", "minimum_deposit": "€50", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}}, {"path": "brandinfo_promotions.other_bonuses[5]", "value": {"name": "Casino Weekend Crypto Reload", "type": "Weekend crypto bonus", "reward": "75% up to 750 USDT + 100 Free Spins", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}}, {"path": "brandinfo_promotions.other_bonuses[6]", "value": {"name": "Casino Double Fortune: One-Day Reload Special", "type": "One-day reload", "reward": "50% up to €500", "minimum_deposit": "€30", "wagering_requirement": "30x deposit plus bonus", "validity": "24 hours", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}}, {"path": "brandinfo_promotions.other_bonuses[7]", "value": {"name": "Casino Trick or Treat Pumpkin Bonanza", "type": "Seasonal casino promotion", "reward": "Up to 100 Free Spins", "minimum_deposit": "€20", "wagering_requirement": "40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}}, {"path": "brandinfo_promotions.other_bonuses[8]", "value": {"name": "Casino Dragon Quest: Get Verified and Get Extra!", "type": "Verification reward", "reward": "€10 bonus credit", "minimum_deposit": "€20", "wagering_requirement": "30x promotional credit", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Players who complete requested account verification during the campaign.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}}]}, {"level": 3, "heading": "Cashback and Rebates", "source": "unique", "covers_clusters": [], "kb_refs": ["brandinfo_promotions.other_bonuses[9]", "brandinfo_promotions.other_bonuses[10]", "brandinfo_promotions.other_bonuses[11]", "brandinfo_promotions.other_bonuses[12]", "brandinfo_promotions.other_bonuses[13]", "brandinfo_promotions.other_bonuses[14]"], "words_min": 48, "words_max": 62, "keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "table"], "entities": [{"name": "Weekly Cashback", "priority": 10}, {"name": "Live Casino Cashback", "priority": 8}, {"name": "Unlimited Rebate", "priority": 7}, {"name": "VIP Cashback Rates", "priority": 6}], "entity_connections": [{"subject": "Weekly Cashback", "relation": "returns", "object": "up to 10% of weekly net casino losses", "priority": 9}, {"subject": "Rebates", "relation": "are credited", "object": "daily", "priority": 7}], "summary": "Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.", "copywriter_notes": "Cover the Casino Weekly Cashback (up to 10% of weekly net casino losses, capped at €6,988; period Monday 00:00 UTC to Sunday 23:59 UTC; opt-in for a four-week cycle; credited to My Bonuses on Monday; 10x wagering of the cashback; the rate depends on the VIP tier: Bronze 2%, Silver 4%, Gold 6%, Platinum 8%, Diamond 10%, shown as a compact table of tier, percentage and maximum) and the Live Casino Cashback (25% up to €850). Mention the four daily rebates in one sentence (casino 0.9%, live casino 1.0%, P2P 0.8%, lottery 1.0%, each with 1x wagering). Only real-money bets count, bonus funds do not. The tier percentages here belong to the weekly cashback; do not mix them with the VIP level percentages of the VIP section. Use no tracked keyword in the body of this block.", "id": "b10", "words": 55, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_promotions.other_bonuses[9]", "value": {"name": "Casino Weekly Cashback", "type": "Casino cashback", "reward": "Up to 10% of weekly net casino losses, capped at €6,988", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "minimum_cashback": "€4.5", "opt_in": "Opt in for a four-week cycle; active accounts can renew automatically.", "crediting": "Credited to My Bonuses on Monday; activation required.", "wagering_requirement": "10x cashback before withdrawal", "cashback_by_vip": [{"level": "VIP Bronze", "percentage": 2, "maximum": "€1,888"}, {"level": "VIP Silver", "percentage": 4, "maximum": "€2,388"}, {"level": "VIP Gold", "percentage": 6, "maximum": "€2,988"}, {"level": "VIP Platinum", "percentage": 8, "maximum": "€3,988"}, {"level": "VIP Diamond", "percentage": 10, "maximum": "€6,988"}], "important_terms": ["Only real-money casino bets and winnings count; bonus funds excluded.", "Weekly cashback expires if it is not activated within its claim window."]}}, {"path": "brandinfo_promotions.other_bonuses[10]", "value": {"name": "Live Casino Cashback", "type": "Live casino cashback", "reward": "25% up to €850", "minimum_cashback": "€4.5", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "crediting": "Credited to My Bonuses on Monday; opt-in and activation required.", "wagering_requirement": "10x credited cashback", "important_terms": ["Based on real-money stakes less winnings in eligible Live Casino games.", "Bonus balances are excluded from cashback calculations."]}}, {"path": "brandinfo_promotions.other_bonuses[11]", "value": {"name": "Unlimited Casino Rebate", "type": "Rebate", "rebate_percentage": 0.9, "calculation": "Qualifying settled real-money wagering on the relevant game category.", "crediting": "Rebate credited daily to the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Registered players with qualifying settled wagers."}}, {"path": "brandinfo_promotions.other_bonuses[12]", "value": {"name": "Unlimited Live Casino Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Qualifying settled real-money wagering on the relevant game category.", "crediting": "Rebate credited daily to the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Registered players with qualifying settled wagers."}}, {"path": "brandinfo_promotions.other_bonuses[13]", "value": {"name": "Unlimited P2P Rebate", "type": "Rebate", "rebate_percentage": 0.8, "calculation": "Qualifying settled real-money wagering on the relevant game category.", "crediting": "Rebate credited daily to the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Registered players with qualifying settled wagers."}}, {"path": "brandinfo_promotions.other_bonuses[14]", "value": {"name": "Unlimited Lottery Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Qualifying settled real-money wagering on the relevant game category.", "crediting": "Rebate credited daily to the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Registered players with qualifying settled wagers."}}]}, {"level": 3, "heading": "Rewards Hub: Bonus Crab, Wheel and Coin Shop", "source": "unique", "covers_clusters": [], "kb_refs": ["brandinfo_promotions.gamification_features"], "words_min": 48, "words_max": 62, "keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Bonus Crab", "priority": 8}, {"name": "Wheel of Fortune", "priority": 7}, {"name": "Challenges", "priority": 6}, {"name": "Collections", "priority": 5}, {"name": "Coin Shop", "priority": 6}], "entity_connections": [{"subject": "Coins", "relation": "are exchanged in", "object": "the Coin Shop for rewards", "priority": 7}, {"subject": "Challenges", "relation": "unlock", "object": "coins, free spins and bonus credits", "priority": 6}], "summary": "The gamification features of the rewards area: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop.", "copywriter_notes": "Describe the five features in short sentences as given: Bonus Crab (claim picks to open a crab reward, valid 7 days, 30x on bonus credit and 40x on free spin winnings), Wheel of Fortune (spend an eligible spin or Coins, 7 days, 30x), Challenges and Collections (found under Rewards), Coin Shop (exchange Coins for rewards and bonus credits up to €4,500, prices vary by item, separate wagering may apply). Say that rewards can carry their own wagering requirements. Use no tracked keyword in the body of this block.", "id": "b11", "words": 55, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_promotions.gamification_features", "value": [{"name": "Bonus Crab", "mechanics": "Claim qualifying picks to open a crab reward and reveal a casino prize.", "access": "Rewards area; qualifying activity may grant free picks.", "rewards": ["Bonus credits", "Free Spins", "Coins"], "validity": "7 days after reward assignment", "wagering_requirement": "30x awarded bonus credit; 40x winnings from Free Spins"}, {"name": "Wheel of Fortune", "mechanics": "Spend an eligible spin or Coins to rotate a prize wheel.", "access": "Rewards area", "rewards": ["Bonus credits", "Free Spins", "Coins"], "validity": "7 days", "wagering_requirement": "30x bonus awards"}, {"name": "Challenges", "mechanics": "Complete qualifying gambling tasks to unlock listed rewards.", "access": "Rewards > Challenges", "rewards": ["Coins", "Free Spins", "Bonus credits"], "validity": "As shown for each challenge"}, {"name": "Collections", "mechanics": "Collect campaign items by completing qualifying activity; redeem completed sets.", "access": "Rewards > Collections", "rewards": ["Coins", "Bonus rewards"], "validity": "Campaign-specific"}, {"name": "Coin Shop", "mechanics": "Exchange earned Coins for rewards in the Shop.", "access": "Rewards > Shop", "rewards": ["Reward items and bonus credits up to €4,500"], "important_terms": ["Coin prices and prize availability vary by item.", "Rewards may carry separate wagering requirements."]}]}]}, {"level": 2, "heading": "Longfu88 VIP Programme", "source": "mandatory", "covers_clusters": ["k12"], "kb_refs": ["brandinfo_loyalty.loyalty_vip_program.name", "brandinfo_loyalty.loyalty_vip_program.tiers", "brandinfo_loyalty.loyalty_vip_program.progression", "brandinfo_loyalty.loyalty_vip_program.levels[0]", "brandinfo_loyalty.loyalty_vip_program.levels[4]", "brandinfo_loyalty.loyalty_vip_program.levels[9]", "brandinfo_loyalty.loyalty_vip_program.levels[14]", "brandinfo_loyalty.loyalty_vip_program.levels[19]", "brandinfo_loyalty.loyalty_vip_program.levels[24]", "brandinfo_loyalty.loyalty_vip_program.additional_benefits", "brandinfo_loyalty.loyalty_vip_program.important_terms"], "words_min": 66, "words_max": 84, "keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "table"], "entities": [{"name": "VIP Programme", "priority": 10}, {"name": "VIP Points", "priority": 8}, {"name": "VIP Levels", "priority": 8}, {"name": "Withdrawal Limits", "priority": 6}, {"name": "Personal VIP Manager", "priority": 5}], "entity_connections": [{"subject": "VIP Points", "relation": "unlock", "object": "numbered reward levels", "priority": 8}, {"subject": "Higher VIP Levels", "relation": "raise", "object": "withdrawal limits and cashback", "priority": 7}], "summary": "How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.", "copywriter_notes": "Explain that VIP points come from eligible real-money play and unlock numbered reward levels (25 levels grouped into the tiers Bronze, Silver, Gold, Platinum and Diamond). Show a compact table Level | Points | Reward | Cashback | Withdrawal limit for levels 1, 5, 10, 15, 20 and 25 exactly as given in the Brand Information (level 1: 1 point, €9.8, 1%, €9,800; level 25: 5,500 points, €980, 10%, €147,000). Say what higher levels add: personalised offers, cashback, higher withdrawal limits and a personal VIP manager from level 4. Reward and withdrawal limits may differ by VIP level and currency and the rules can change. The programme name is \"Longfu88 VIP Program\" as given: it contains the tracked keyword \"Longfu88\", and the page heading already uses it, so write \"the VIP programme\" in the body. Use no tracked keyword in the body of this block. Do not repeat the weekly cashback tier table (cashback section).", "listed_entities": ["VIP Levels"], "id": "b12", "words": 75, "fact_table": [], "heading_keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_loyalty.loyalty_vip_program.name", "value": "Longfu88 VIP Program"}, {"path": "brandinfo_loyalty.loyalty_vip_program.tiers", "value": ["Bronze", "Silver", "Gold", "Platinum", "Diamond"]}, {"path": "brandinfo_loyalty.loyalty_vip_program.progression", "value": "Earn VIP points through eligible real-money gameplay; points unlock numbered reward levels."}, {"path": "brandinfo_loyalty.loyalty_vip_program.levels[0]", "value": {"level": 1, "points_required": 1, "level_reward": "€9.8", "cashback_percentage": 1, "withdrawal_limit": "€9,800", "benefits": ["On-site promotions", "24/7 Live Chat"]}}, {"path": "brandinfo_loyalty.loyalty_vip_program.levels[4]", "value": {"level": 5, "points_required": 70, "level_reward": "€24.5", "cashback_percentage": 2, "withdrawal_limit": "€34,300", "benefits": ["On-site promotions", "24/7 Live Chat", "Personalised offers", "Higher withdrawal limits", "Cashback", "Personal VIP Manager"]}}, {"path": "brandinfo_loyalty.loyalty_vip_program.levels[9]", "value": {"level": 10, "points_required": 700, "level_reward": "€147", "cashback_percentage": 4, "withdrawal_limit": "€63,700", "benefits": ["On-site promotions", "24/7 Live Chat", "Personalised offers", "Higher withdrawal limits", "Cashback", "Personal VIP Manager"]}}, {"path": "brandinfo_loyalty.loyalty_vip_program.levels[14]", "value": {"level": 15, "points_required": 2100, "level_reward": "€392", "cashback_percentage": 6, "withdrawal_limit": "€88,200", "benefits": ["On-site promotions", "24/7 Live Chat", "Personalised offers", "Higher withdrawal limits", "Cashback", "Personal VIP Manager"]}}, {"path": "brandinfo_loyalty.loyalty_vip_program.levels[19]", "value": {"level": 20, "points_required": 3600, "level_reward": "€637", "cashback_percentage": 8, "withdrawal_limit": "€117,600", "benefits": ["On-site promotions", "24/7 Live Chat", "Personalised offers", "Higher withdrawal limits", "Cashback", "Personal VIP Manager"]}}, {"path": "brandinfo_loyalty.loyalty_vip_program.levels[24]", "value": {"level": 25, "points_required": 5500, "level_reward": "€980", "cashback_percentage": 10, "withdrawal_limit": "€147,000", "benefits": ["On-site promotions", "24/7 Live Chat", "Personalised offers", "Higher withdrawal limits", "Cashback", "Personal VIP Manager"]}}, {"path": "brandinfo_loyalty.loyalty_vip_program.additional_benefits", "value": ["Personalised offers", "VIP cashback", "Higher withdrawal limits", "Personal VIP manager for eligible high tiers"]}, {"path": "brandinfo_loyalty.loyalty_vip_program.important_terms", "value": ["Different reward and withdrawal limits may apply to VIP levels and currencies.", "Level-based benefits and promotion eligibility may change under program rules."]}]}, {"level": 2, "heading": "Games Overview", "source": "mandatory", "covers_clusters": ["k02"], "kb_refs": ["brandinfo_games.game_types"], "words_min": 53, "words_max": 67, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 1, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Game Categories", "priority": 10}, {"name": "Slots", "priority": 7}, {"name": "Live Dealer Games", "priority": 7}, {"name": "Jackpots", "priority": 5}, {"name": "Crash Games", "priority": 5}], "entity_connections": [{"subject": "Online Casino", "relation": "offers", "object": "slots, live dealer games, table games, jackpots, fishing, P2P, fast games, lottery and crash games", "priority": 8}], "summary": "The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.", "copywriter_notes": "Name the nine categories of the Brand Information in flowing text and lead into the sub-sections on slots, live casino and the other categories without retelling their facts. Do not state a number of games or providers: none is given. Use \"Longfu88 casino\" (the name Longfu88 Casino) exactly once and \"Longfu88\" exactly once, and no other tracked keyword.", "id": "b13", "words": 60, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_games.game_types", "value": ["Slots", "Live dealer games", "Table games", "Jackpots", "Fishing", "P2P games", "Fast games", "Lottery", "Crash & instant games"]}]}, {"level": 3, "heading": "Slots", "source": "mandatory", "covers_clusters": ["k03"], "kb_refs": ["brandinfo_games.game_examples"], "words_min": 62, "words_max": 78, "keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Slots", "priority": 10}, {"name": "Gates of Olympus", "priority": 7}, {"name": "Sweet Bonanza", "priority": 7}, {"name": "Wanted Dead or a Wild", "priority": 7}, {"name": "RTP", "priority": 6}, {"name": "Volatility", "priority": 5}], "entity_connections": [{"subject": "Gates of Olympus", "relation": "has", "object": "an RTP of 96.50% and a maximum multiplier of 5,000x", "priority": 7}, {"subject": "Hacksaw Gaming", "relation": "supplies", "object": "Wanted Dead or a Wild", "priority": 6}], "summary": "Three example slots with their provider, RTP, volatility and maximum multiplier.", "copywriter_notes": "Name the three example slots with the figures exactly as in the Brand Information: Gates of Olympus (Pragmatic Play, RTP 96.50%, high volatility, 5,000x), Sweet Bonanza (Pragmatic Play, RTP 96.48%, high volatility, 21,175x) and Wanted Dead or a Wild (Hacksaw Gaming, RTP 96.38%, very high volatility, 12,500x). Explain in one sentence what RTP and volatility mean for the player. Do not claim that these are the only or the most popular slots and name no other title. Use no tracked keyword in the body of this block.", "id": "b14", "words": 70, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_games.game_examples", "value": [{"name": "Gates of Olympus", "provider": "Pragmatic Play", "rtp": "96.50%", "volatility": "High", "maximum_multiplier": "5,000x"}, {"name": "Sweet Bonanza", "provider": "Pragmatic Play", "rtp": "96.48%", "volatility": "High", "maximum_multiplier": "21,175x"}, {"name": "Wanted Dead or a Wild", "provider": "Hacksaw Gaming", "rtp": "96.38%", "volatility": "Very high", "maximum_multiplier": "12,500x"}]}]}, {"level": 3, "heading": "Live Casino", "source": "mandatory", "covers_clusters": ["k04"], "kb_refs": ["brandinfo_games.original_games", "brandinfo_games.providers[0]", "brandinfo_games.providers[6]"], "words_min": 57, "words_max": 73, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 1, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Live Dealer Games", "priority": 10}, {"name": "Evolution", "priority": 7}, {"name": "SA Gaming", "priority": 6}, {"name": "Longfu88 Baccarat", "priority": 6}], "entity_connections": [{"subject": "Live Casino", "relation": "includes", "object": "the exclusive Longfu88 Baccarat", "priority": 7}, {"subject": "Live Casino", "relation": "is powered by", "object": "Evolution and SA Gaming among other studios", "priority": 6}], "summary": "The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.", "copywriter_notes": "Describe the live dealer section as a category of the lobby, name the exclusive game \"Longfu88 Baccarat\" exactly as given (an exclusive live or table game with baccarat gameplay; the name is the one occurrence of \"Longfu88\" of this block) and name Evolution and SA Gaming from the provider list as live studios only if the sentence stays factual (they are in the provider list; do not say which live games each one supplies). Do not name any other live game or show. Use \"Longfu 88 casino\" exactly once, written in a natural sentence, and no other tracked keyword.", "id": "b15", "words": 65, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_games.original_games", "value": [{"name": "Longfu88 Baccarat", "category": "Exclusive live/table game", "features": ["Baccarat gameplay"]}]}, {"path": "brandinfo_games.providers[0]", "value": "Evolution"}, {"path": "brandinfo_games.providers[6]", "value": "SA Gaming"}]}, {"level": 3, "heading": "Table, Fishing, P2P, Fast Games and Lottery", "source": "unique", "covers_clusters": ["k05", "k06", "k09"], "kb_refs": ["brandinfo_games.game_types"], "words_min": 53, "words_max": 67, "keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Table Games", "priority": 8}, {"name": "Fishing Games", "priority": 6}, {"name": "P2P Games", "priority": 6}, {"name": "Fast Games", "priority": 6}, {"name": "Lottery", "priority": 6}, {"name": "Crash Games", "priority": 5}], "entity_connections": [{"subject": "Online Casino", "relation": "also offers", "object": "fishing, P2P, fast, lottery and crash games", "priority": 6}], "summary": "The remaining game categories in one block: table games, fishing, P2P, fast games, lottery and crash and instant games.", "copywriter_notes": "Describe each category in a sentence as a type of game only (what the player does): table games, fishing, P2P (play against other players), fast games, lottery, crash and instant games. Name no titles, no providers per category and no numbers; none are given. Use no tracked keyword in the body of this block.", "id": "b16", "words": 60, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_games.game_types", "value": ["Slots", "Live dealer games", "Table games", "Jackpots", "Fishing", "P2P games", "Fast games", "Lottery", "Crash & instant games"]}]}, {"level": 2, "heading": "Game Providers", "source": "unique", "covers_clusters": ["k07"], "kb_refs": ["brandinfo_games.providers"], "words_min": 48, "words_max": 62, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Game Providers", "priority": 10}, {"name": "Evolution", "priority": 7}, {"name": "Pragmatic Play", "priority": 7}, {"name": "Hacksaw Gaming", "priority": 6}, {"name": "Red Tiger", "priority": 5}, {"name": "NetEnt", "priority": 5}], "entity_connections": [{"subject": "Game Providers", "relation": "supply", "object": "slots, live and table games to the casino", "priority": 7}], "summary": "Which studios supply the games, named from the provider list.", "copywriter_notes": "Name the ten providers of the Brand Information in a running sentence or two, exactly as given: Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft, Hacksaw Gaming. Do not say how many studios there are in total and which game each supplies, except what the slots section states. Use \"Longfu88\" exactly once and no other tracked keyword.", "listed_entities": ["Evolution", "Pragmatic Play", "Hacksaw Gaming", "Red Tiger", "NetEnt"], "id": "b17", "words": 55, "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_games.providers", "value": ["Evolution", "Red Tiger", "NetEnt", "Big Time Gaming", "Pragmatic Play", "Yggdrasil", "SA Gaming", "Skywind", "Betsoft", "Hacksaw Gaming"]}]}, {"level": 2, "heading": "Sports Betting", "source": "mandatory", "covers_clusters": ["k08"], "kb_refs": ["brandinfo_sportsbook.sportsbook.sports_available", "brandinfo_sportsbook.sportsbook.bet_types", "brandinfo_sportsbook.sportsbook.live_betting", "brandinfo_sportsbook.sportsbook.important_terms"], "words_min": 66, "words_max": 84, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 1}, "formats": ["paragraph"], "entities": [{"name": "Sportsbook", "priority": 10}, {"name": "Football", "priority": 7}, {"name": "Esports", "priority": 6}, {"name": "Live Betting", "priority": 7}, {"name": "Bet Builder", "priority": 5}, {"name": "Accumulator", "priority": 5}], "entity_connections": [{"subject": "Sportsbook", "relation": "covers", "object": "football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football", "priority": 8}, {"subject": "Live Betting", "relation": "offers", "object": "live odds and in-play markets", "priority": 7}], "summary": "The sportsbook: the sports and esports covered, the bet types and live betting.", "copywriter_notes": "Give the nine sports and esports as listed (football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports, virtual football), the seven bet types (single, accumulator, live, handicap, totals, outrights, Bet Builder) and live betting with live odds and in-play markets. Use the keyword \"Longfu sports\" exactly once as a natural phrase for the sports section (for example the Longfu sports section), and \"Longfu88\" exactly once. Event availability and market selection can vary by jurisdiction. Name no sports league or event and no sportsbook platform. Use no other tracked keyword.", "id": "b18", "words": 75, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_sportsbook.sportsbook.sports_available", "value": ["Football", "Basketball", "Tennis", "Badminton", "Cricket", "Table tennis", "Volleyball", "Esports", "Virtual football"]}, {"path": "brandinfo_sportsbook.sportsbook.bet_types", "value": ["Single", "Accumulator", "Live", "Handicap", "Totals", "Outrights", "Bet Builder"]}, {"path": "brandinfo_sportsbook.sportsbook.live_betting", "value": {"available": true, "features": ["Live odds", "In-play markets"]}}, {"path": "brandinfo_sportsbook.sportsbook.important_terms", "value": ["Event availability and market selection can vary by jurisdiction."]}]}, {"level": 3, "heading": "Sports Bonuses and Promotions", "source": "unique", "covers_clusters": [], "kb_refs": ["brandinfo_sportsbook.sportsbook.sports_bonuses"], "words_min": 48, "words_max": 62, "keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "table"], "entities": [{"name": "Sport First Deposit Bonus", "priority": 10}, {"name": "Sports Cashback", "priority": 7}, {"name": "Parlay Boost", "priority": 6}, {"name": "Bet Builder Risk Free", "priority": 5}, {"name": "Minimum Odds", "priority": 6}], "entity_connections": [{"subject": "Sport First Deposit Bonus", "relation": "gives", "object": "100% up to €1,888", "priority": 8}, {"subject": "Qualifying Bets", "relation": "need", "object": "minimum odds of 2.00 for singles", "priority": 7}], "summary": "The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.", "copywriter_notes": "Give a compact table Offer | Reward | Min. deposit | Wagering for the Sport First Deposit Bonus (100% up to €1,888, €50, 8x, 30 days), the Sport Weekly Reload Bonus (50% up to €2,500, €50, 8x) and the Sport Weekend Reload Bonus (50% up to €3,750, €50, 8x); then name the crypto equivalents, Sports Cashback (10% up to €2,500 of eligible sports net losses, weekly), Unlimited Sports Rebate (0.70%), 2 Goals Ahead early payout, Parlay Boost (up to 100% extra winnings, at least three legs) and Bet Builder Risk Free (50% stake return up to €250) in prose. Rules that apply: only settled qualifying sports bets count, single bets need odds of at least 2.00 and each accumulator selection at least 1.50, voided and cashed-out bets do not qualify. Do not mix these with the casino bonuses. Use no tracked keyword in the body of this block.", "listed_entities": ["Sport First Deposit Bonus"], "id": "b19", "words": 55, "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_sportsbook.sportsbook.sports_bonuses", "value": [{"name": "Sport First Deposit Bonus", "reward": "100% up to €1,888", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Welcome Bonus", "reward": "100% up to 200 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Weekly Reload Bonus", "reward": "50% up to €2,500", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Weekend Reload Bonus", "reward": "50% up to €3,750", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Weekly Reload", "reward": "50% up to 500 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Weekend Reload", "reward": "50% up to 1,000 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Unlimited Sports Rebate", "reward": "0.70% of qualifying settled sports wagers", "wagering_requirement": "1x credited rebate", "crediting": "Daily"}, {"name": "Sports Cashback", "reward": "10% up to €2,500 of eligible sports net losses", "calculation_period": "Weekly", "wagering_requirement": "1x cashback", "eligibility": "Registered players with eligible real-money losing bets"}, {"name": "2 Goals Ahead - Early Payout", "reward": "Early settlement of eligible football bets when the selected team leads by two goals", "important_terms": ["Only participating pre-match match-winner markets qualify.", "Settlement is subject to published event eligibility."]}, {"name": "Parlay Boost", "reward": "Up to 100% extra winnings on qualifying accumulators", "minimum_legs": 3, "wagering_requirement": "No additional bonus wagering on settled enhanced winnings", "important_terms": ["Boost depends on the number of qualifying selections."]}, {"name": "Bet Builder Risk Free", "reward": "50% risk-free stake return up to €250", "eligibility": "Qualifying pre-match Bet Builder selections", "wagering_requirement": "1x credited free-bet stake", "validity": "7 days"}]}]}, {"level": 2, "heading": "Deposit Methods and Limits", "source": "mandatory", "covers_clusters": ["k14", "k16"], "kb_refs": ["brandinfo_deposit.deposit_methods", "brandinfo_deposit.deposit_guide", "brandinfo_general.minimum_deposit", "brandinfo_general.currencies"], "words_min": 79, "words_max": 101, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "table"], "entities": [{"name": "Payment Methods", "priority": 10}, {"name": "Bank Transfer", "priority": 7}, {"name": "Cryptocurrency", "priority": 7}, {"name": "E-wallets", "priority": 6}, {"name": "Deposit Limits", "priority": 7}, {"name": "Processing Speed", "priority": 6}], "entity_connections": [{"subject": "Deposits", "relation": "are credited", "object": "within 1-2 minutes", "priority": 8}, {"subject": "Casino", "relation": "charges", "object": "no processing fee on deposits, while provider or network fees may apply", "priority": 7}], "summary": "Deposit methods grouped by type with the general limits and speed, the local options for Singapore and the six-step deposit route.", "copywriter_notes": "One lead-in sentence, then a Markdown table Method type | Examples | Currencies with the groups: local bank and wallet methods, cards (Visa, Mastercard), bank transfer, cryptocurrencies (Bitcoin, Ethereum, Litecoin, USDT in TRC20, ERC20 and BEP20, USDC and others from the list), e-wallets (Neteller, Skrill) and the European methods (Sofort, Giropay). For Singapore highlight PayNow, PayNow QR, DBS Bank and OCBC Bank (SGD) as given. General limits for every method: minimum €10, maximum €5,000 per transaction, speed 1-2 minutes, no casino processing fee, provider or blockchain network fees may apply. Do NOT quote the per-currency limit lines of single methods (they mix euro signs with local-currency amounts) and say that the limits can differ by country, currency and method. Neteller and Skrill deposits are excluded from the welcome bonus. After the table, the six deposit steps in one flowing sentence or two. Use \"Longfu88\" exactly once and no other tracked keyword; keep it out of the table.", "listed_entities": ["Bank Transfer", "Cryptocurrency", "E-wallets"], "id": "b20", "words": 90, "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_deposit.deposit_methods", "value": [{"method": "BCA", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €5,000 per transaction"]}, {"method": "BNI", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €20, maximum €40,000 per transaction"]}, {"method": "Bank Transfer", "currencies": ["IDR", "MYR", "VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €25, maximum €82,000 per transaction", "MYR: minimum €50, maximum €50,000 per transaction", "VND: minimum €100, maximum €500,000 per transaction"]}, {"method": "Bitcoin", "currencies": ["BTC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €590, maximum €98,490 per transaction", "MYR: minimum €145, maximum €23,840 per transaction", "SGD: minimum €45, maximum €7,560 per transaction", "THB: minimum €1,100, maximum €182,910 per transaction", "VND: minimum €929, maximum €154,949 per transaction"]}, {"method": "Bitcoin Cash", "currencies": ["BCH"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "Cardano", "currencies": ["ADA"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "DANA", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €5,000 per transaction"]}, {"method": "DBS Bank", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €50, maximum €5,000 per transaction"]}, {"method": "DuitNow", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €50,000 per transaction"]}, {"method": "Ethereum", "currencies": ["ETH"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "Giropay", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "GrabPay", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €5,000 per transaction"]}, {"method": "Litecoin", "currencies": ["LTC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "Mandiri", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €20, maximum €40,000 per transaction"]}, {"method": "Mastercard", "currencies": ["IDR", "MYR", "SGD", "VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €200, maximum €30,000 per transaction", "MYR: minimum €50, maximum €9,000 per transaction", "SGD: minimum €18, maximum €3,000 per transaction", "VND: minimum €320, maximum €50,000 per transaction"]}, {"method": "MoMo", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €30,000 per transaction"]}, {"method": "Neteller", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "OCBC Bank", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €50, maximum €5,000 per transaction"]}, {"method": "OVO Wallet", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €2,000 per transaction"]}, {"method": "Online Banking", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €10,000 per transaction"]}, {"method": "PayNow", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €10, maximum €5,000 per transaction"]}, {"method": "PayNow QR", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €10, maximum €5,000 per transaction"]}, {"method": "PromptPay QR", "currencies": ["THB"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["THB: minimum €300, maximum €200,000 per transaction"]}, {"method": "QRIS", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €50,000 per transaction"]}, {"method": "Ripple", "currencies": ["XRP"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "Skrill", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Sofort", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Touch'n Go", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €5,000 per transaction"]}, {"method": "USDC", "currencies": ["USDC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "USDT (BEP20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"], "network": "BEP20"}, {"method": "USDT (ERC20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"], "network": "ERC20"}, {"method": "USDT (TRC20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"], "network": "TRC20"}, {"method": "VietQR", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €300,000 per transaction"]}, {"method": "ViettelPay", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €20,000 per transaction"]}, {"method": "Visa", "currencies": ["IDR", "MYR", "SGD", "VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €200, maximum €30,000 per transaction", "MYR: minimum €50, maximum €9,000 per transaction", "SGD: minimum €18, maximum €3,000 per transaction", "VND: minimum €320, maximum €50,000 per transaction"]}, {"method": "Zalo", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €100,000 per transaction"]}]}, {"path": "brandinfo_deposit.deposit_guide", "value": ["Log in to the Longfu88 account.", "Open the cashier and select Deposit.", "Choose an available payment method and its supported currency or blockchain network.", "Enter the amount and payment information.", "Confirm and authorize the transaction using the provider instructions.", "Wait for the funds to be credited to the playable balance."]}, {"path": "brandinfo_general.minimum_deposit", "value": "€10"}, {"path": "brandinfo_general.currencies", "value": ["EUR", "USD", "MYR", "THB", "SGD", "USDT"]}]}, {"level": 3, "heading": "Withdrawals and Payout Times", "source": "unique", "covers_clusters": ["k15"], "kb_refs": ["brandinfo_withdrawal.withdrawal_methods", "brandinfo_withdrawal.withdrawal_guide", "brandinfo_privacy_policy.terms_conditions.withdrawal_terms", "brandinfo_privacy_policy.terms_conditions.conditional_fees", "brandinfo_general.payment_methods.withdrawal"], "words_min": 70, "words_max": 90, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 1, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "list"], "entities": [{"name": "Withdrawal Time", "priority": 10}, {"name": "Withdrawal Methods", "priority": 8}, {"name": "Minimum Withdrawal", "priority": 7}, {"name": "Withdrawal Fees", "priority": 7}, {"name": "Deposit Turnover", "priority": 6}], "entity_connections": [{"subject": "Withdrawal", "relation": "is processed within", "object": "up to 3 business days", "priority": 9}, {"subject": "Bank Transfer", "relation": "may need", "object": "3-5 more business days for delivery", "priority": 7}], "summary": "How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.", "copywriter_notes": "Give the methods as listed (bank transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT in three networks, Touch'n Go, DANA, MoMo, DBS Bank, Online Banking), the minimum €20 and maximum €5,000, the six steps as a NUMBERED list, and the processing time: card, crypto and wallet withdrawals take 1 to 3 business days; bank transfer takes up to 3 business days for casino processing plus 3 to 5 business days for bank delivery; requests are generally processed within three working days. Use the keyword \"Lngfu88 withdrawal time\" exactly once, verbatim with this spelling, in the sentence that gives the processing time. Fees: no standard casino withdrawal fee, provider and blockchain fees may apply; a 10% commission (minimum €2.25) can apply where turnover is below the deposited amount (a minimum 1x deposit turnover can apply before a withdrawal) and 15% on some card or bank transfer funded transactions. Do NOT quote the per-market minimum lines of single methods (they mix euro signs with local-currency amounts). Identity checks can delay a payout (see the verification section). Use \"Longfu88\" exactly once and no other tracked keyword.", "id": "b21", "words": 80, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_withdrawal.withdrawal_methods", "value": [{"method": "Bank Transfer", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["IDR", "MYR", "VND"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "Visa", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["IDR", "MYR", "SGD", "VND"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "Mastercard", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["IDR", "MYR", "SGD", "VND"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "Bitcoin", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["BTC"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Ethereum", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["ETH"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Litecoin", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["LTC"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "USDT (TRC20)", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "USDT (ERC20)", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "USDT (BEP20)", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Touch'n Go", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["MYR"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "DANA", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["IDR"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "MoMo", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["VND"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "DBS Bank", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["SGD"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "Online Banking", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["MYR"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}]}, {"path": "brandinfo_withdrawal.withdrawal_guide", "value": ["Log in to Longfu88 and open the cashier.", "Select Withdrawal and choose a supported destination or payment method.", "Enter the amount and the receiving bank, wallet, or blockchain address.", "Complete identity and payment-method verification if prompted.", "Review the request and confirm submission.", "Wait for casino processing and any bank or network settlement before receiving funds."]}, {"path": "brandinfo_privacy_policy.terms_conditions.withdrawal_terms", "value": ["A minimum 1x deposit turnover can apply before a withdrawal.", "Withdrawal requests are generally processed within three working days.", "Bank transfers may need another 3–5 business days for settlement.", "The operator may request KYC documents before processing payments."]}, {"path": "brandinfo_privacy_policy.terms_conditions.conditional_fees", "value": ["Where qualifying turnover is below the deposited amount, a 10% commission may apply with minimum €2.25.", "A 15% charge can apply to some card or bank transfer funded transactions under the casino rules."]}, {"path": "brandinfo_general.payment_methods.withdrawal", "value": ["Bank Transfer", "Visa", "Mastercard", "Bitcoin", "Ethereum", "Litecoin", "USDT (TRC20)", "USDT (ERC20)", "USDT (BEP20)", "Touch'n Go", "DANA", "MoMo", "DBS Bank", "Online Banking"]}]}, {"level": 2, "heading": "Mobile Access", "source": "mandatory", "covers_clusters": ["k17"], "kb_refs": ["brandinfo_app.app_information"], "words_min": 62, "words_max": 78, "keywords": {"Longfu88": 2, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 1, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "list"], "entities": [{"name": "Mobile Access", "priority": 10}, {"name": "Add to Home Screen", "priority": 8}, {"name": "Android", "priority": 6}, {"name": "iOS", "priority": 6}, {"name": "Responsive Website", "priority": 7}], "entity_connections": [{"subject": "Responsive Website", "relation": "works on", "object": "smartphone and tablet browsers", "priority": 8}, {"subject": "Home Screen Shortcut", "relation": "gives", "object": "quick access to the casino and sportsbook", "priority": 6}], "summary": "Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.", "copywriter_notes": "Explain that the casino runs as a responsive website on smartphone and tablet browsers (platforms Android, iOS and mobile web) and can be added to the home screen as a shortcut; give the Android route (Chrome, browser menu, Add to Home screen, confirm) and the iOS route (Safari, Share, Add to Home Screen, Add) as two short numbered lists, each preceded by one sentence. Name the available functions (casino, sportsbook, account access, deposits, withdrawals, bonuses). Use the keyword \"Longfu88 app\" exactly once, in a sentence that makes clear it is the home-screen version of the site; do NOT claim a download from an app store or an APK file: none is given. Step one of the Android list and of the iOS list names the brand as in the Brand Information (\"Open Longfu88 in Chrome\" and \"Open Longfu88 in Safari\"); these two occurrences of \"Longfu88\" are part of the exact count of this block, the rest goes into running text as \"the casino\". Use no other tracked keyword.", "id": "b22", "words": 70, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_app.app_information", "value": {"platforms": ["Android", "iOS", "Mobile web"], "mobile_access": "Responsive Longfu88 website usable on smartphone and tablet browsers.", "android_installation": ["Open Longfu88 in Chrome.", "Open browser menu and choose Add to Home screen.", "Confirm the shortcut."], "ios_installation": ["Open Longfu88 in Safari.", "Tap Share and choose Add to Home Screen.", "Confirm Add."], "features": ["Casino", "Sportsbook", "Account access", "Deposits", "Withdrawals", "Bonuses"]}}]}, {"level": 2, "heading": "Responsible Gambling", "source": "mandatory", "covers_clusters": ["k20"], "kb_refs": ["brandinfo_responsible_gaming.responsible_gaming"], "words_min": 66, "words_max": 84, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph", "list"], "entities": [{"name": "Responsible Gambling", "priority": 10}, {"name": "Self-Exclusion", "priority": 8}, {"name": "Account Closure", "priority": 6}, {"name": "Self-Assessment", "priority": 5}, {"name": "GamCare", "priority": 5}, {"name": "Gambling Therapy", "priority": 5}], "entity_connections": [{"subject": "Self-Exclusion", "relation": "is requested", "object": "by e-mail to customer support", "priority": 8}, {"subject": "Players", "relation": "can seek help from", "object": "GamCare, Gamblers Anonymous and Gambling Therapy", "priority": 7}], "summary": "Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.", "copywriter_notes": "State that players must be at least 18 and gamble only where lawful. Explain self-exclusion (requested by e-mail to customer support, restricts access and gambling for the agreed period, processed within 24 hours after the request is processed) and account closure through customer support, the four-step procedure in short, and self-assessment questions that help to spot harm. Give the organisations GamCare, Gamblers Anonymous and Gambling Therapy as a short bulleted list. Say that the page cannot replace independent help. Use \"Longfu88\" exactly once, in the sentence about self-exclusion (for example by printing the support e-mail address exactly as given, which contains it), and no other tracked keyword.", "id": "b23", "words": 75, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_responsible_gaming.responsible_gaming", "value": {"policy": "Players must be at least 18 years old and gamble only where lawful.", "self_exclusion": {"request_method": "Email support@longfu88.com", "processing_time": "Within 24 hours after the self-exclusion request is processed", "effect": "Account access and gambling may be restricted for the agreed period."}, "account_closure": "Request account closure through customer support.", "self_assessment": "Self-assessment questions help players identify possible gambling-related harm.", "support_organizations": ["GamCare", "Gamblers Anonymous", "Gambling Therapy"], "contact": "support@longfu88.com", "procedure": ["Contact support and request self-exclusion or account closure.", "Confirm your account details and preferred exclusion terms.", "Allow the casino to restrict or close access.", "Seek independent support where appropriate."]}}]}, {"level": 2, "heading": "Customer Support", "source": "mandatory", "covers_clusters": ["k19"], "kb_refs": ["brandinfo_general.customer_support"], "words_min": 48, "words_max": 62, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Customer Support", "priority": 10}, {"name": "Live Chat", "priority": 8}, {"name": "Email Support", "priority": 7}, {"name": "Support Languages", "priority": 6}], "entity_connections": [{"subject": "Live Chat", "relation": "is available", "object": "24/7", "priority": 8}, {"subject": "Customer Support", "relation": "speaks", "object": "English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese", "priority": 6}], "summary": "Support channels, availability and languages.", "copywriter_notes": "Give the two channels (24/7 live chat and e-mail), the e-mail address exactly as given (it contains the tracked keyword \"Longfu88\" and is the one occurrence of \"Longfu88\" of this block) and the six support languages (English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese). Do not mention a phone line, a ticket system, an average response time or a social account: none is given.", "id": "b24", "words": 55, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_general.customer_support", "value": {"channels": ["24/7 live chat", "Email"], "email": "support@longfu88.com", "languages": ["English", "Malay", "Simplified Chinese", "Thai", "Indonesian", "Vietnamese"]}}]}, {"level": 2, "heading": "Pros and Cons", "source": "unique", "covers_clusters": ["k23"], "kb_refs": ["brandinfo_general.minimum_deposit", "brandinfo_welcome.welcome_bonus.wagering_requirement", "brandinfo_privacy_policy.terms_conditions.conditional_fees", "brandinfo_games.providers", "brandinfo_promotions.other_bonuses[9].reward"], "words_min": 48, "words_max": 62, "keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["table"], "entities": [{"name": "Advantages", "priority": 8}, {"name": "Disadvantages", "priority": 8}, {"name": "Welcome Bonus", "priority": 6}, {"name": "Withdrawal Fees", "priority": 5}, {"name": "Payment Methods", "priority": 5}], "entity_connections": [{"subject": "Advantages", "relation": "are balanced against", "object": "the conditions that come with them", "priority": 7}], "summary": "A pros and cons table built only from facts stated elsewhere on the page.", "copywriter_notes": "A Markdown table with exactly two columns, Pros | Cons, four or five rows. Pros are facts from the page (a low general minimum deposit of €10, a large choice of payment methods including cryptocurrencies, a weekly cashback of up to 10%, a VIP programme with 25 levels, 24/7 live chat); cons are the conditions that go with them (the welcome bonus needs a €50 deposit and 25x wagering on deposit plus bonus, a 10% or 15% commission can apply to withdrawals under the turnover rule, bank withdrawals can take several business days, verification may delay the first payout). No intro sentence beyond one line, no new facts, no tracked keyword in the table.", "id": "b25", "words": 55, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_general.minimum_deposit", "value": "€10"}, {"path": "brandinfo_welcome.welcome_bonus.wagering_requirement", "value": "25x the deposit plus bonus amount"}, {"path": "brandinfo_privacy_policy.terms_conditions.conditional_fees", "value": ["Where qualifying turnover is below the deposited amount, a 10% commission may apply with minimum €2.25.", "A 15% charge can apply to some card or bank transfer funded transactions under the casino rules."]}, {"path": "brandinfo_games.providers", "value": ["Evolution", "Red Tiger", "NetEnt", "Big Time Gaming", "Pragmatic Play", "Yggdrasil", "SA Gaming", "Skywind", "Betsoft", "Hacksaw Gaming"]}, {"path": "brandinfo_promotions.other_bonuses[9].reward", "value": "Up to 10% of weekly net casino losses, capped at €6,988"}]}, {"level": 2, "heading": "Frequently Asked Questions", "source": "mandatory", "covers_clusters": ["k22"], "kb_refs": ["brandinfo_account.login.password_recovery", "brandinfo_general.minimum_deposit", "brandinfo_welcome.welcome_bonus.claiming_procedure"], "words_min": 53, "words_max": 67, "keywords": {"Longfu88": 1, "Longfu 88": 1, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "formats": ["list"], "entities": [{"name": "Frequently Asked Questions", "priority": 8}, {"name": "Promo Code", "priority": 7}, {"name": "Minimum Deposit", "priority": 7}, {"name": "Withdrawal Time", "priority": 7}, {"name": "Password Recovery", "priority": 6}], "entity_connections": [{"subject": "Frequently Asked Questions", "relation": "cover", "object": "bonus claiming, minimum deposit, withdrawal time and password recovery", "priority": 6}], "summary": "Four short answers: how to claim the bonus, the minimum deposit, how long a withdrawal takes and how to recover a password.", "copywriter_notes": "A bulleted list of exactly four items, each a bold question followed by a short answer of 20-30 words, in this order: (1) how to claim the welcome bonus (activate it in My Bonuses after the first qualifying deposit of €50; no code step is part of the procedure); (2) what is the minimum deposit (€10 in general, €50 for the welcome bonus); (3) how long a withdrawal takes (up to 3 business days of casino processing, then bank or network time; wording must differ from the withdrawals section); (4) how to recover the password (Forgot Password on the login screen, reset link by e-mail): the question must contain the keyword \"Longfu 88\" in the form \"my Longfu 88 account\" (exactly once in the block). \"Longfu88\" goes into one answer, not into a question. These are the only questions on the page; the questions are the one place where question form is allowed. Use \"Longfu 88\" exactly once and \"Longfu88\" exactly once.", "id": "b26", "words": 60, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_account.login.password_recovery", "value": ["Choose Forgot Password on the login screen.", "Request a reset link using the registered email.", "Follow the emailed instructions to set a new password."]}, {"path": "brandinfo_general.minimum_deposit", "value": "€10"}, {"path": "brandinfo_welcome.welcome_bonus.claiming_procedure", "value": ["Register an account and complete the required personal details.", "Make the first qualifying deposit.", "Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.", "Play eligible casino games and complete the wagering before expiry."]}]}, {"level": 2, "heading": "Verdict", "source": "mandatory", "covers_clusters": ["k21"], "kb_refs": ["brandinfo_general.minimum_age", "brandinfo_responsible_gaming.responsible_gaming.policy"], "words_min": 62, "words_max": 78, "keywords": {"Longfu88": 1, "Longfu 88": 0, "Longfu88 casino": 1, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 1, "Longfu sports": 0}, "formats": ["paragraph"], "entities": [{"name": "Verdict", "priority": 10}, {"name": "Welcome Bonus Terms", "priority": 6}, {"name": "Responsible Gambling", "priority": 6}, {"name": "Minimum Age", "priority": 5}], "entity_connections": [{"subject": "Player", "relation": "should check", "object": "the bonus terms and payment limits before depositing", "priority": 7}], "summary": "A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.", "copywriter_notes": "Close with three or four sentences: which kind of player the facts fit (someone who wants casino, live and sports betting in one account with local and crypto payments), what to check before depositing (the €50 qualifying deposit, 25x wagering, the withdrawal turnover rule and verification), then the 18+ limit with the reminders that gambling is not a source of income, that losses should not be chased and that a budget and breaks help. Put \"Longfu88 casino\" (the name Longfu88 Casino) into the first sentence, use the short name \"Longfu\" exactly once and \"Longfu88\" exactly once. Repeat no figures, make no promises of winnings, no hype. NEVER say or imply that the casino is licensed, legal or approved in Singapore; the licence named in the Brand Information is the only licence statement. Use no other tracked keyword.", "id": "b27", "words": 70, "listed_entities": [], "fact_table": [], "heading_keywords": {"Longfu88": 0, "Longfu 88": 0, "Longfu88 casino": 0, "Longfu88 login": 0, "Longfu88 bonus": 0, "Longfu88 app": 0, "Longfu88 promo code": 0, "Longfu 88 casino": 0, "casino Longfu88": 0, "Lngfu88 withdrawal time": 0, "Longfu 88 Official Site": 0, "Longfu": 0, "Longfu sports": 0}, "brand_info": [{"path": "brandinfo_general.minimum_age", "value": 18}, {"path": "brandinfo_responsible_gaming.responsible_gaming.policy", "value": "Players must be at least 18 years old and gamble only where lawful."}]}], "kb_unresolved": ["b03: path not found: brandinfo_privacy_policy.privacy_policy.terms_conditions.eligibility (stopped after \".brandinfo_privacy_policy.privacy_policy\")"]}
