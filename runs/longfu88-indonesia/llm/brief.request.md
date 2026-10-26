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
 "geo": "Indonesia",
 "page_language": "Indonesian",
 "keywords": [
  "Longfu88",
  "Longfu 88",
  "Longfu88 casino",
  "Longfu88 login",
  "Longfu caino login",
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
  "LongFu88 review 2026 October",
  "LongFu88 review 2026",
  "Longfu88 Casino Malaysia – Review, Games & Bonuses 2026",
  "longfu88 ‚Äî Live Tables, Slots and More, Built for Malaysia",
  "Longfu88 Indonesia Casino ‚Äî Play in IDR & Claim Your Bonus",
  "",
  "Ulasan Longfu88 Casino: Panduan Pantas Untuk Pemain Malaysia",
  "longfu88 Casino, Slots dan Sportsbook untuk Malaysia",
  "longfu88 — Kasino & Sportsbook untuk Malaysia"
 ],
 "competitor_stats": [
  {
   "url": "https://www.mightytips.com/online-casinos/longfu88/",
   "body_words": 1836,
   "keywords_in_total": {
    "Longfu88": 23,
    "Longfu 88": 0,
    "Longfu88 casino": 3,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
   "url": "https://www.mightytips.com/bookmakers/longfu88/",
   "body_words": 2627,
   "keywords_in_total": {
    "Longfu88": 56,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 1,
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
    "Longfu caino login": 0,
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
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
    "Longfu88 bonus": 0,
    "Longfu88 app": 1,
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
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
   "url": "https://longfu88.vin/",
   "body_words": 2111,
   "keywords_in_total": {
    "Longfu88": 14,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
    "Longfu88": 5,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
   "url": "https://longfu88-play.my/en-id/",
   "body_words": 3181,
   "keywords_in_total": {
    "Longfu88": 21,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
   "url": "https://lf12--longfu88.com/ib/",
   "body_words": 0,
   "keywords_in_total": {
    "Longfu88": 0,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
    "Longfu88": 0,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
  },
  {
   "url": "https://longfu88.bid/",
   "body_words": 1135,
   "keywords_in_total": {
    "Longfu88": 12,
    "Longfu 88": 0,
    "Longfu88 casino": 1,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
    "Longfu88": 5,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
   "url": "https://longfu88.best/",
   "body_words": 1222,
   "keywords_in_total": {
    "Longfu88": 20,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
    "Longfu caino login": 0,
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
    "Longfu88": 11,
    "Longfu 88": 0,
    "Longfu88 casino": 0,
    "Longfu88 login": 0,
    "Longfu caino login": 0,
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
  }
 ],
 "targets": {
  "target_body_words": 1836,
  "keyword_targets": {
   "Longfu88": 20,
   "Longfu 88": 1,
   "Longfu88 casino": 1,
   "Longfu88 login": 1,
   "Longfu caino login": 1,
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
   "frequency": 8,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 34,
   "avg_position": 0.44,
   "examples": [
    "Casino games",
    "Selection of casino games",
    "What games does longfu88 casino have?",
    "How to Open Your Account and Reach the Games"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Payment Methods",
   "topic": "Deposit methods and payments",
   "frequency": 8,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 71,
   "avg_position": 0.52,
   "examples": [
    "Deposit methods",
    "Payment methods",
    "Deposit methods",
    "Deposit and withdrawal limits in Singapore"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "Safety and Fair Play",
   "topic": "Licence, security and fair play",
   "frequency": 8,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 69,
   "avg_position": 0.57,
   "examples": [
    "Licensing & security",
    "Licensing & security information",
    "Is Longfu88 Safe? Security and Fair Play",
    "Is longfu88 casino safe to play at?"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Sports Betting",
   "topic": "Sports betting and esports",
   "frequency": 7,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 60,
   "avg_position": 0.58,
   "examples": [
    "Sportsbook",
    "Sports betting overview",
    "Sports coverage (20+)",
    "Sports odds"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Bonuses and Welcome Offers",
   "topic": "Bonuses and welcome offers",
   "frequency": 6,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 114,
   "avg_position": 0.27,
   "examples": [
    "Bonuses & promotions",
    "Bonus offers and promotions",
    "Welcome bonus",
    "Other promotions"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Mobile Access",
   "topic": "Mobile access and app",
   "frequency": 6,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 71,
   "avg_position": 0.44,
   "examples": [
    "Mobile & app experience",
    "LongFu88 App",
    "Games and Providers – 7,500 Titles from 50+ Studios",
    "Mobile Access"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "Slots",
   "topic": "Slots",
   "frequency": 6,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 57,
   "avg_position": 0.49,
   "examples": [
    "Slots",
    "Slots",
    "Fan-Favourite Slots You Can Open Right Now",
    "Slot: Dunia Gulungan Untuk Semua Gaya"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Customer Support",
   "topic": "Customer support",
   "frequency": 6,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 55,
   "avg_position": 0.57,
   "examples": [
    "Customer support",
    "Customer service",
    "Three Ways to Reach Our Support Team",
    "24-Hour Support Coverage"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Withdrawals",
   "topic": "Withdrawals and payout speed",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 56,
   "avg_position": 0.53,
   "examples": [
    "Deposits & withdrawals",
    "Withdrawal methods",
    "Withdrawal methods",
    "Withdrawal Audit Trail"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "Registration and Login",
   "topic": "Registration and login",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 59,
   "avg_position": 0.57,
   "examples": [
    "Registration at LongFu88",
    "Encrypted Login",
    "Akses Link Rasmi & Sistem Log Masuk Auto",
    "Kemudahan Navigasi Selepas Mendaftar"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Live Casino",
   "topic": "Live casino",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 46,
   "avg_position": 0.61,
   "examples": [
    "Live Dealer Games",
    "Live dealer games",
    "Live Casino",
    "Experience Live Dealer Gaming"
   ]
  },
  {
   "id": "k21",
   "canonical_title": "Frequently Asked Questions",
   "topic": "FAQ",
   "frequency": 5,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 23,
   "avg_position": 0.82,
   "examples": [
    "FAQ",
    "Frequently Asked Questions About longfu88",
    "Soalan Lazim (FAQ) - Longfu88",
    "FAQ"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Table Games",
   "topic": "Table games and video poker",
   "frequency": 4,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 37,
   "avg_position": 0.27,
   "examples": [
    "Table games",
    "Classic Blackjack",
    "French Roulette",
    "Baccarat, Roulette and Dragon Tiger ‚Äî Streamed Live"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "VIP Programme",
   "topic": "VIP programme and loyalty",
   "frequency": 4,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 115,
   "avg_position": 0.39,
   "examples": [
    "Rewards and loyalty programs at LongFu88",
    "VIP Programme – Bronze to Diamond",
    "VIP Program and Loyalty Rewards",
    "Butiran Program VIP"
   ]
  },
  {
   "id": "k01",
   "canonical_title": "About the Casino",
   "topic": "Platform overview / about the casino",
   "frequency": 4,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 68,
   "avg_position": 0.49,
   "examples": [
    "About LongFu88",
    "LongFu88 overview",
    "Usability and user experience",
    "Navigation"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Instant and Specialty Games",
   "topic": "Fishing, P2P, fast and free games",
   "frequency": 4,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 69,
   "avg_position": 0.52,
   "examples": [
    "Free games",
    "Crash X, Aviator and Fast-Round Arcade Titles",
    "Thunder Fishing, Fish Rooms and Sportsbook Markets",
    "Slot Themes, Live Rooms and Arcade Formats ‚Äî All in One Place"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Game Providers",
   "topic": "Software providers",
   "frequency": 4,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 96,
   "avg_position": 0.52,
   "examples": [
    "Software providers",
    "Game Selection and Software Providers",
    "Game Provider Partnerships",
    "Studio dalam longfu88"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Responsible Gambling",
   "topic": "Responsible gambling",
   "frequency": 4,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 103,
   "avg_position": 0.69,
   "examples": [
    "Responsible gambling tools",
    "Responsible Gambling",
    "Responsible Gambling Tools",
    "Sokongan Pemain & Permainan Bertanggungjawab"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Verdict",
   "topic": "Verdict and conclusion",
   "frequency": 3,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 108,
   "avg_position": 0.84,
   "examples": [
    "Our verdict on LongFu88",
    "Conclusion",
    "Ringkasan: Mengapa Memilih Longfu 88 Casino?",
    "Kesimpulan: Platform Stabil Dengan Proses Kewangan Pantas"
   ]
  },
  {
   "id": "k20",
   "canonical_title": "Pros and Cons",
   "topic": "Pros and cons",
   "frequency": 2,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 46,
   "avg_position": 0.48,
   "examples": [
    "Longfu88 Review – What Works and What to Know",
    "Strengths",
    "Kelebihan & Kekurangan Longfu Casino"
   ]
  },
  {
   "id": "k28",
   "canonical_title": "What You Find When You Open longfu88",
   "topic": "Other: What You Find When You Open longfu88",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 123,
   "avg_position": 0.02,
   "examples": [
    "What You Find When You Open longfu88"
   ]
  },
  {
   "id": "k46",
   "canonical_title": "Nombor ringkas di longfu88",
   "topic": "Other: Nombor ringkas di longfu88",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 0,
   "avg_position": 0.02,
   "examples": [
    "Nombor ringkas di longfu88"
   ]
  },
  {
   "id": "k81",
   "canonical_title": "Perkara Pertama yang Perlu Anda Ketahui",
   "topic": "Other: Perkara Pertama yang Perlu Anda Ketahui",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 26,
   "avg_position": 0.02,
   "examples": [
    "Perkara Pertama yang Perlu Anda Ketahui"
   ]
  },
  {
   "id": "k82",
   "canonical_title": "Apa yang Menanti di Dalam Lobi longfu88",
   "topic": "Other: Apa yang Menanti di Dalam Lobi longfu88",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 27,
   "avg_position": 0.04,
   "examples": [
    "Apa yang Menanti di Dalam Lobi longfu88"
   ]
  },
  {
   "id": "k47",
   "canonical_title": "Andar Bahar",
   "topic": "Other: Andar Bahar",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 23,
   "avg_position": 0.06,
   "examples": [
    "Andar Bahar"
   ]
  },
  {
   "id": "k83",
   "canonical_title": "Fish Hunter",
   "topic": "Other: Fish Hunter",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 21,
   "avg_position": 0.06,
   "examples": [
    "Fish Hunter"
   ]
  },
  {
   "id": "k48",
   "canonical_title": "Secrets of Cleopatra",
   "topic": "Other: Secrets of Cleopatra",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 24,
   "avg_position": 0.07,
   "examples": [
    "Secrets of Cleopatra"
   ]
  },
  {
   "id": "k49",
   "canonical_title": "Lucky Twins",
   "topic": "Other: Lucky Twins",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 24,
   "avg_position": 0.09,
   "examples": [
    "Lucky Twins"
   ]
  },
  {
   "id": "k84",
   "canonical_title": "Sugar Rush 1000",
   "topic": "Other: Sugar Rush 1000",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 21,
   "avg_position": 0.09,
   "examples": [
    "Sugar Rush 1000"
   ]
  },
  {
   "id": "k50",
   "canonical_title": "The Dog House Megaways",
   "topic": "Other: The Dog House Megaways",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 22,
   "avg_position": 0.11,
   "examples": [
    "The Dog House Megaways"
   ]
  },
  {
   "id": "k29",
   "canonical_title": "Ocean Fortune",
   "topic": "Other: Ocean Fortune",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 22,
   "avg_position": 0.12,
   "examples": [
    "Ocean Fortune"
   ]
  },
  {
   "id": "k85",
   "canonical_title": "Caishen Wins",
   "topic": "Other: Caishen Wins",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 21,
   "avg_position": 0.13,
   "examples": [
    "Caishen Wins"
   ]
  },
  {
   "id": "k30",
   "canonical_title": "Halloween Fortune",
   "topic": "Other: Halloween Fortune",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 23,
   "avg_position": 0.14,
   "examples": [
    "Halloween Fortune"
   ]
  },
  {
   "id": "k86",
   "canonical_title": "Aztec Gems",
   "topic": "Other: Aztec Gems",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 23,
   "avg_position": 0.15,
   "examples": [
    "Aztec Gems"
   ]
  },
  {
   "id": "k31",
   "canonical_title": "Wild Walker",
   "topic": "Other: Wild Walker",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 26,
   "avg_position": 0.16,
   "examples": [
    "Wild Walker"
   ]
  },
  {
   "id": "k32",
   "canonical_title": "Fortune Mouse",
   "topic": "Other: Fortune Mouse",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 25,
   "avg_position": 0.19,
   "examples": [
    "Fortune Mouse"
   ]
  },
  {
   "id": "k45",
   "canonical_title": "Ganjaran Berterusan Untuk Pemain Sedia Ada",
   "topic": "Other: Ganjaran Berterusan Untuk Pemain Sedia Ada",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 73,
   "avg_position": 0.19,
   "examples": [
    "Ganjaran Berterusan Untuk Pemain Sedia Ada"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Lottery",
   "topic": "Lottery",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 67,
   "avg_position": 0.2,
   "examples": [
    "Sports, E-sports and Lottery"
   ]
  },
  {
   "id": "k51",
   "canonical_title": "Lima kawasan tahan lama",
   "topic": "Other: Lima kawasan tahan lama",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 32,
   "avg_position": 0.2,
   "examples": [
    "Lima kawasan tahan lama"
   ]
  },
  {
   "id": "k52",
   "canonical_title": "Pusat profil",
   "topic": "Other: Pusat profil",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 16,
   "avg_position": 0.22,
   "examples": [
    "Pusat profil"
   ]
  },
  {
   "id": "k53",
   "canonical_title": "Rekod transaksi",
   "topic": "Other: Rekod transaksi",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 16,
   "avg_position": 0.26,
   "examples": [
    "Rekod transaksi"
   ]
  },
  {
   "id": "k87",
   "canonical_title": "Kawalan Akaun dan Privasi Data",
   "topic": "Other: Kawalan Akaun dan Privasi Data",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 19,
   "avg_position": 0.28,
   "examples": [
    "Kawalan Akaun dan Privasi Data"
   ]
  },
  {
   "id": "k88",
   "canonical_title": "Hubungi Kami — Saluran dan Jam Operasi",
   "topic": "Other: Hubungi Kami — Saluran dan Jam Operasi",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 19,
   "avg_position": 0.3,
   "examples": [
    "Hubungi Kami — Saluran dan Jam Operasi"
   ]
  },
  {
   "id": "k54",
   "canonical_title": "Touch 'n Go",
   "topic": "Other: Touch 'n Go",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 0,
   "avg_position": 0.33,
   "examples": [
    "Touch 'n Go"
   ]
  },
  {
   "id": "k89",
   "canonical_title": "Touch 'n Go eWallet",
   "topic": "Other: Touch 'n Go eWallet",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 0,
   "avg_position": 0.33,
   "examples": [
    "Touch 'n Go eWallet"
   ]
  },
  {
   "id": "k55",
   "canonical_title": "GrabPay",
   "topic": "Other: GrabPay",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 0,
   "avg_position": 0.35,
   "examples": [
    "GrabPay"
   ]
  },
  {
   "id": "k90",
   "canonical_title": "GrabPay",
   "topic": "Other: GrabPay",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 0,
   "avg_position": 0.35,
   "examples": [
    "GrabPay"
   ]
  },
  {
   "id": "k33",
   "canonical_title": "Ocean Fortune",
   "topic": "Other: Ocean Fortune",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 22,
   "avg_position": 0.37,
   "examples": [
    "Ocean Fortune"
   ]
  },
  {
   "id": "k56",
   "canonical_title": "Boost",
   "topic": "Other: Boost",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 0,
   "avg_position": 0.37,
   "examples": [
    "Boost"
   ]
  },
  {
   "id": "k91",
   "canonical_title": "Boost",
   "topic": "Other: Boost",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 0,
   "avg_position": 0.37,
   "examples": [
    "Boost"
   ]
  },
  {
   "id": "k57",
   "canonical_title": "FPX",
   "topic": "Other: FPX",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 0,
   "avg_position": 0.39,
   "examples": [
    "FPX"
   ]
  },
  {
   "id": "k92",
   "canonical_title": "FPX",
   "topic": "Other: FPX",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 0,
   "avg_position": 0.39,
   "examples": [
    "FPX"
   ]
  },
  {
   "id": "k34",
   "canonical_title": "Halloween Fortune",
   "topic": "Other: Halloween Fortune",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 28,
   "avg_position": 0.4,
   "examples": [
    "Halloween Fortune"
   ]
  },
  {
   "id": "k35",
   "canonical_title": "Wild Walker",
   "topic": "Other: Wild Walker",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 26,
   "avg_position": 0.42,
   "examples": [
    "Wild Walker"
   ]
  },
  {
   "id": "k93",
   "canonical_title": "Hubungi Kami — Cara Terbaik untuk Anda",
   "topic": "Other: Hubungi Kami — Cara Terbaik untuk Anda",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 41,
   "avg_position": 0.43,
   "examples": [
    "Hubungi Kami — Cara Terbaik untuk Anda"
   ]
  },
  {
   "id": "k36",
   "canonical_title": "Fortune Mouse",
   "topic": "Other: Fortune Mouse",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 30,
   "avg_position": 0.44,
   "examples": [
    "Fortune Mouse"
   ]
  },
  {
   "id": "k58",
   "canonical_title": "Email",
   "topic": "Other: Email",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 20,
   "avg_position": 0.44,
   "examples": [
    "Email"
   ]
  },
  {
   "id": "k94",
   "canonical_title": "Chat Langsung",
   "topic": "Other: Chat Langsung",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 22,
   "avg_position": 0.44,
   "examples": [
    "Chat Langsung"
   ]
  },
  {
   "id": "k59",
   "canonical_title": "Bantuan mudah alih",
   "topic": "Other: Bantuan mudah alih",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 18,
   "avg_position": 0.46,
   "examples": [
    "Bantuan mudah alih"
   ]
  },
  {
   "id": "k60",
   "canonical_title": "Lobi lancar pada telefon",
   "topic": "Other: Lobi lancar pada telefon",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 28,
   "avg_position": 0.48,
   "examples": [
    "Lobi lancar pada telefon"
   ]
  },
  {
   "id": "k37",
   "canonical_title": "Four Reasons Your Account Works Better Here",
   "topic": "Other: Four Reasons Your Account Works Better Here",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 26,
   "avg_position": 0.49,
   "examples": [
    "Four Reasons Your Account Works Better Here"
   ]
  },
  {
   "id": "k61",
   "canonical_title": "Cara kami bina keyakinan",
   "topic": "Other: Cara kami bina keyakinan",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 32,
   "avg_position": 0.5,
   "examples": [
    "Cara kami bina keyakinan"
   ]
  },
  {
   "id": "k95",
   "canonical_title": "Tanda-tanda E-E-A-T longfu88",
   "topic": "Other: Tanda-tanda E-E-A-T longfu88",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 24,
   "avg_position": 0.5,
   "examples": [
    "Tanda-tanda E-E-A-T longfu88"
   ]
  },
  {
   "id": "k62",
   "canonical_title": "Struktur boleh disemak",
   "topic": "Other: Struktur boleh disemak",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 20,
   "avg_position": 0.52,
   "examples": [
    "Struktur boleh disemak"
   ]
  },
  {
   "id": "k38",
   "canonical_title": "Continuous Live Streams",
   "topic": "Other: Continuous Live Streams",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 25,
   "avg_position": 0.53,
   "examples": [
    "Continuous Live Streams"
   ]
  },
  {
   "id": "k63",
   "canonical_title": "Akses polisi",
   "topic": "Other: Akses polisi",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 20,
   "avg_position": 0.54,
   "examples": [
    "Akses polisi"
   ]
  },
  {
   "id": "k39",
   "canonical_title": "Single Account Balance",
   "topic": "Other: Single Account Balance",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 27,
   "avg_position": 0.56,
   "examples": [
    "Single Account Balance"
   ]
  },
  {
   "id": "k25",
   "canonical_title": "Limits",
   "topic": "Other: Limits",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 68,
   "avg_position": 0.57,
   "examples": [
    "Limits"
   ]
  },
  {
   "id": "k64",
   "canonical_title": "Semakan transaksi",
   "topic": "Other: Semakan transaksi",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 20,
   "avg_position": 0.57,
   "examples": [
    "Semakan transaksi"
   ]
  },
  {
   "id": "k96",
   "canonical_title": "Keterlibatan Komunitas Jangka Panjang",
   "topic": "Other: Keterlibatan Komunitas Jangka Panjang",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 20,
   "avg_position": 0.57,
   "examples": [
    "Keterlibatan Komunitas Jangka Panjang"
   ]
  },
  {
   "id": "k65",
   "canonical_title": "longfu88 berbanding carian berselerak",
   "topic": "Other: longfu88 berbanding carian berselerak",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 28,
   "avg_position": 0.59,
   "examples": [
    "longfu88 berbanding carian berselerak"
   ]
  },
  {
   "id": "k66",
   "canonical_title": "Akses Malaysia secara setempat",
   "topic": "Other: Akses Malaysia secara setempat",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 63,
   "avg_position": 0.61,
   "examples": [
    "Akses Malaysia secara setempat"
   ]
  },
  {
   "id": "k97",
   "canonical_title": "longfu88 untuk Pemain Malaysia",
   "topic": "Other: longfu88 untuk Pemain Malaysia",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 68,
   "avg_position": 0.61,
   "examples": [
    "longfu88 untuk Pemain Malaysia"
   ]
  },
  {
   "id": "k27",
   "canonical_title": "Quick Links",
   "topic": "Other: Quick Links",
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
   "id": "k67",
   "canonical_title": "Langkah pertama",
   "topic": "Other: Langkah pertama",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 19,
   "avg_position": 0.65,
   "examples": [
    "Langkah pertama"
   ]
  },
  {
   "id": "k98",
   "canonical_title": "Panduan Menavigasi longfu88",
   "topic": "Other: Panduan Menavigasi longfu88",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 31,
   "avg_position": 0.65,
   "examples": [
    "Panduan Menavigasi longfu88"
   ]
  },
  {
   "id": "k40",
   "canonical_title": "RNG Certification",
   "topic": "Other: RNG Certification",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 17,
   "avg_position": 0.67,
   "examples": [
    "RNG Certification"
   ]
  },
  {
   "id": "k68",
   "canonical_title": "Selepas akaun dibuka",
   "topic": "Other: Selepas akaun dibuka",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 18,
   "avg_position": 0.67,
   "examples": [
    "Selepas akaun dibuka"
   ]
  },
  {
   "id": "k69",
   "canonical_title": "Sebelum transaksi",
   "topic": "Other: Sebelum transaksi",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 18,
   "avg_position": 0.69,
   "examples": [
    "Sebelum transaksi"
   ]
  },
  {
   "id": "k70",
   "canonical_title": "Jika tersekat",
   "topic": "Other: Jika tersekat",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 19,
   "avg_position": 0.7,
   "examples": [
    "Jika tersekat"
   ]
  },
  {
   "id": "k99",
   "canonical_title": "Langkah 3: Penjelajahan Lobi Pertama",
   "topic": "Other: Langkah 3: Penjelajahan Lobi Pertama",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 25,
   "avg_position": 0.7,
   "examples": [
    "Langkah 3: Penjelajahan Lobi Pertama"
   ]
  },
  {
   "id": "k22",
   "canonical_title": "Ongoing Promotions",
   "topic": "Ongoing promotions and tournaments",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 231,
   "avg_position": 0.72,
   "examples": [
    "Tournament Competitions and Promotions"
   ]
  },
  {
   "id": "k41",
   "canonical_title": "Two-Factor Option",
   "topic": "Other: Two-Factor Option",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 10,
   "avg_position": 0.72,
   "examples": [
    "Two-Factor Option"
   ]
  },
  {
   "id": "k100",
   "canonical_title": "Langkah 4: Mengelola Akaun Anda",
   "topic": "Other: Langkah 4: Mengelola Akaun Anda",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 24,
   "avg_position": 0.72,
   "examples": [
    "Langkah 4: Mengelola Akaun Anda"
   ]
  },
  {
   "id": "k71",
   "canonical_title": "Empat perkara anda semak dahulu",
   "topic": "Other: Empat perkara anda semak dahulu",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 34,
   "avg_position": 0.74,
   "examples": [
    "Empat perkara anda semak dahulu"
   ]
  },
  {
   "id": "k101",
   "canonical_title": "Angka yang Menentukan longfu88",
   "topic": "Other: Angka yang Menentukan longfu88",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 0,
   "avg_position": 0.74,
   "examples": [
    "Angka yang Menentukan longfu88"
   ]
  },
  {
   "id": "k72",
   "canonical_title": "Bacaan kadar dan kategori",
   "topic": "Other: Bacaan kadar dan kategori",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 32,
   "avg_position": 0.76,
   "examples": [
    "Bacaan kadar dan kategori"
   ]
  },
  {
   "id": "k102",
   "canonical_title": "Kasino Langsung",
   "topic": "Other: Kasino Langsung",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 22,
   "avg_position": 0.81,
   "examples": [
    "Kasino Langsung"
   ]
  },
  {
   "id": "k42",
   "canonical_title": "longfu88 in Malaysia ‚Äî Availability and Access",
   "topic": "Other: longfu88 in Malaysia ‚Äî Availability and Access",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 141,
   "avg_position": 0.84,
   "examples": [
    "longfu88 in Malaysia ‚Äî Availability and Access"
   ]
  },
  {
   "id": "k23",
   "canonical_title": "Crypto Payments",
   "topic": "Cryptocurrency payments",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 63,
   "avg_position": 0.85,
   "examples": [
    "Era Baharu Pembayaran Kripto"
   ]
  },
  {
   "id": "k73",
   "canonical_title": "Bingo",
   "topic": "Other: Bingo",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 20,
   "avg_position": 0.85,
   "examples": [
    "Bingo"
   ]
  },
  {
   "id": "k74",
   "canonical_title": "Kawalan akaun dan akses",
   "topic": "Other: Kawalan akaun dan akses",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 34,
   "avg_position": 0.87,
   "examples": [
    "Kawalan akaun dan akses"
   ]
  },
  {
   "id": "k103",
   "canonical_title": "Bingo",
   "topic": "Other: Bingo",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 23,
   "avg_position": 0.87,
   "examples": [
    "Bingo"
   ]
  },
  {
   "id": "k75",
   "canonical_title": "Enam tanda longfu88",
   "topic": "Other: Enam tanda longfu88",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 26,
   "avg_position": 0.89,
   "examples": [
    "Enam tanda longfu88"
   ]
  },
  {
   "id": "k76",
   "canonical_title": "Lobi gabungan",
   "topic": "Other: Lobi gabungan",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 21,
   "avg_position": 0.91,
   "examples": [
    "Lobi gabungan"
   ]
  },
  {
   "id": "k104",
   "canonical_title": "Lobi yang Tertata dengan Baik",
   "topic": "Other: Lobi yang Tertata dengan Baik",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 19,
   "avg_position": 0.91,
   "examples": [
    "Lobi yang Tertata dengan Baik"
   ]
  },
  {
   "id": "k43",
   "canonical_title": "No Wallet Lock-In",
   "topic": "Other: No Wallet Lock-In",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 31,
   "avg_position": 0.93,
   "examples": [
    "No Wallet Lock-In"
   ]
  },
  {
   "id": "k77",
   "canonical_title": "Tajuk dikenali",
   "topic": "Other: Tajuk dikenali",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 20,
   "avg_position": 0.93,
   "examples": [
    "Tajuk dikenali"
   ]
  },
  {
   "id": "k105",
   "canonical_title": "Penyaring dan Pencarian Cepat",
   "topic": "Other: Penyaring dan Pencarian Cepat",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 23,
   "avg_position": 0.93,
   "examples": [
    "Penyaring dan Pencarian Cepat"
   ]
  },
  {
   "id": "k78",
   "canonical_title": "Pilihan Malaysia",
   "topic": "Other: Pilihan Malaysia",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 19,
   "avg_position": 0.96,
   "examples": [
    "Pilihan Malaysia"
   ]
  },
  {
   "id": "k106",
   "canonical_title": "Saldo dan Laporan Real-Time",
   "topic": "Other: Saldo dan Laporan Real-Time",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 21,
   "avg_position": 0.96,
   "examples": [
    "Saldo dan Laporan Real-Time"
   ]
  },
  {
   "id": "k79",
   "canonical_title": "Kawalan akses",
   "topic": "Other: Kawalan akses",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 17,
   "avg_position": 0.98,
   "examples": [
    "Kawalan akses"
   ]
  },
  {
   "id": "k107",
   "canonical_title": "Pengaturan Akaun yang Dapat Dipersonalisasi",
   "topic": "Other: Pengaturan Akaun yang Dapat Dipersonalisasi",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 19,
   "avg_position": 0.98,
   "examples": [
    "Pengaturan Akaun yang Dapat Dipersonalisasi"
   ]
  },
  {
   "id": "k24",
   "canonical_title": "User Reviews",
   "topic": "Other: User Reviews",
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
  },
  {
   "id": "k26",
   "canonical_title": "User Reviews",
   "topic": "Other: User Reviews",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 270,
   "avg_position": 1.0,
   "examples": [
    "User Reviews"
   ]
  },
  {
   "id": "k44",
   "canonical_title": "Join Longfu88 Today",
   "topic": "Other: Join Longfu88 Today",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 262,
   "avg_position": 1.0,
   "examples": [
    "Join Longfu88 Today"
   ]
  },
  {
   "id": "k80",
   "canonical_title": "Bantuan tersusun",
   "topic": "Other: Bantuan tersusun",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 19,
   "avg_position": 1.0,
   "examples": [
    "Bantuan tersusun"
   ]
  },
  {
   "id": "k108",
   "canonical_title": "Akses Responsif Lintas Perangkat",
   "topic": "Other: Akses Responsif Lintas Perangkat",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 21,
   "avg_position": 1.0,
   "examples": [
    "Akses Responsif Lintas Perangkat"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "Malaysia",
   "competitors": 7
  },
  {
   "entity": "GrabPay",
   "competitors": 7
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 6
  },
  {
   "entity": "VIP",
   "competitors": 5
  },
  {
   "entity": "Touch",
   "competitors": 5
  },
  {
   "entity": "USDT",
   "competitors": 5
  },
  {
   "entity": "Olympus",
   "competitors": 5
  },
  {
   "entity": "Megaways",
   "competitors": 5
  },
  {
   "entity": "MYR",
   "competitors": 4
  },
  {
   "entity": "FPX",
   "competitors": 4
  },
  {
   "entity": "DuitNow",
   "competitors": 4
  },
  {
   "entity": "Boost",
   "competitors": 4
  },
  {
   "entity": "Evolution",
   "competitors": 4
  },
  {
   "entity": "Dota 2",
   "competitors": 4
  },
  {
   "entity": "Gates",
   "competitors": 4
  },
  {
   "entity": "SSL",
   "competitors": 4
  },
  {
   "entity": "Sic Bo",
   "competitors": 4
  },
  {
   "entity": "Wallet",
   "competitors": 3
  },
  {
   "entity": "Malaysian",
   "competitors": 3
  },
  {
   "entity": "RTP",
   "competitors": 3
  },
  {
   "entity": "MYR 2",
   "competitors": 3
  },
  {
   "entity": "Live Casino",
   "competitors": 3
  },
  {
   "entity": "RNG",
   "competitors": 3
  },
  {
   "entity": "Hacksaw Gaming",
   "competitors": 3
  },
  {
   "entity": "Mastercard",
   "competitors": 3
  },
  {
   "entity": "Cardano",
   "competitors": 3
  },
  {
   "entity": "Bank Transfer",
   "competitors": 3
  },
  {
   "entity": "PG Soft",
   "competitors": 3
  },
  {
   "entity": "Android",
   "competitors": 3
  },
  {
   "entity": "Visa",
   "competitors": 3
  },
  {
   "entity": "Ethereum",
   "competitors": 3
  },
  {
   "entity": "Roulette",
   "competitors": 3
  },
  {
   "entity": "Diamond",
   "competitors": 3
  },
  {
   "entity": "Slots",
   "competitors": 3
  },
  {
   "entity": "Sweet Bonanza",
   "competitors": 3
  },
  {
   "entity": "Free Spins",
   "competitors": 3
  },
  {
   "entity": "Online Banking",
   "competitors": 3
  },
  {
   "entity": "Tether",
   "competitors": 3
  },
  {
   "entity": "MYR 1",
   "competitors": 3
  },
  {
   "entity": "MYR 30",
   "competitors": 3
  },
  {
   "entity": "Pragmatic Play Live",
   "competitors": 3
  },
  {
   "entity": "Payment Methods",
   "competitors": 3
  },
  {
   "entity": "Asian",
   "competitors": 3
  },
  {
   "entity": "Gambling Therapy",
   "competitors": 3
  },
  {
   "entity": "Dragon Tiger",
   "competitors": 3
  },
  {
   "entity": "Lottery",
   "competitors": 3
  },
  {
   "entity": "Dog House Megaways",
   "competitors": 3
  },
  {
   "entity": "Asia",
   "competitors": 3
  },
  {
   "entity": "THB",
   "competitors": 2
  },
  {
   "entity": "Äôs",
   "competitors": 2
  },
  {
   "entity": "Äôt",
   "competitors": 2
  },
  {
   "entity": "Äôll",
   "competitors": 2
  },
  {
   "entity": "Bitcoin",
   "competitors": 2
  },
  {
   "entity": "Baccarat",
   "competitors": 2
  },
  {
   "entity": "Thailand",
   "competitors": 2
  },
  {
   "entity": "Habanero",
   "competitors": 2
  },
  {
   "entity": "Kasino Langsung",
   "competitors": 2
  },
  {
   "entity": "Crash",
   "competitors": 2
  },
  {
   "entity": "Join",
   "competitors": 2
  },
  {
   "entity": "Singapore",
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
    "competitor": 2,
    "url": "https://www.mightytips.com/bookmakers/longfu88/",
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
     ],
     [
      "Types of Bets",
      "Snooker , Tour de France, X Factor , Eurovision , The Voice , Premier League , UEFA Europa League , UEFA Champions Leagu"
     ]
    ]
   },
   {
    "competitor": 4,
    "url": "https://longfu88.vin/",
    "heading": "Crash X, Aviator and Fast-Round Arcade Titles",
    "rows": [
     [
      "Classic Blackjack",
      "Spribe's crash game displays a rising multiplier on a flight curve. You cash out before the plane flies away ‚Äî timing "
     ],
     [
      "French Roulette",
      "A high-volatility crash title with a visual multiplier graph. Early cash-outs yield smaller returns; riding the curve lo"
     ],
     [
      "Ocean Fortune",
      "A grid-based instant game where you reveal tiles to accumulate a multiplier. Hitting a mine ends the round, so you choos"
     ],
     [
      "Halloween Fortune",
      "A fast card-prediction game. You decide whether the next card is higher or lower than the current one, with the multipli"
     ],
     [
      "Wild Walker",
      "A ball-drop instant game with a peg board. Ball position at the bottom slot determines the multiplier ‚Äî risk level adj"
     ],
     [
      "Fortune Mouse",
      "A number-draw instant game where you mark a selection of numbers before the draw. Payout scales with how many of your ch"
     ]
    ]
   },
   {
    "competitor": 5,
    "url": "https://longfu88-play.my/en-id/",
    "heading": "Key Platform Features",
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
      "Cura√ßao Gaming Authority (CGA) ‚Äî offshore framework"
     ],
     [
      "Welcome Offer",
      "188% up to Rp 31,000,000 + 18 Free Spins"
     ],
     [
      "Minimum Deposit",
      "Rp 300,000"
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
    "competitors": 3
   },
   {
    "label": "email",
    "competitors": 2
   },
   {
    "label": "payments",
    "competitors": 2
   },
   {
    "label": "phone",
    "competitors": 2
   },
   {
    "label": "title",
    "competitors": 2
   },
   {
    "label": "website",
    "competitors": 2
   },
   {
    "label": "classic blackjack",
    "competitors": 1
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
    "label": "fortune mouse",
    "competitors": 1
   },
   {
    "label": "french roulette",
    "competitors": 1
   },
   {
    "label": "halloween fortune",
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
    "label": "ocean fortune",
    "competitors": 1
   },
   {
    "label": "payment methods",
    "competitors": 1
   },
   {
    "label": "software providers",
    "competitors": 1
   },
   {
    "label": "top games",
    "competitors": 1
   },
   {
    "label": "types of bets",
    "competitors": 1
   },
   {
    "label": "welcome offer",
    "competitors": 1
   },
   {
    "label": "wild walker",
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
   }
  ]
 }
}
