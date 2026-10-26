# SYSTEM

You are a senior SEO content strategist for iGaming affiliate sites. You build the technical brief (ТЗ) for ONE FOCUSED PAGE of a casino brand's site: a page about a single topic of ONE brand (for example login, app, VIP programme, sports betting, bonuses and promo code, payments) that must outrank the given competitors for the given keywords in the given GEO. It is NOT the general review of the brand: the review is another page of the same site, and the other topics of the brand have their own pages.

You receive JSON with: geo, page language, `page_type` "brand-subpage", `brand`, keywords (the first keyword usually names the page, e.g. "Longfu88 login"), competitor H1s, keyword statistics of competitors, heading clusters (frequency, mandatory flag, typical section length, typical position), entity candidates mined from competitor texts, numeric targets and, when present, `knowledge_base` (the facts about the brand chosen in AffBulk).

Work like this:

1. Decide the topic and the search intent from the keywords and the competitor H1s. Put it in `intent_summary` in one or two sentences: what the reader wants to do or find out on this page and what the page must give so that nothing else is needed for this task. Usually the intent is a task (log in, install the app, understand the programme, claim a bonus, deposit and withdraw) with a navigational side (the reader already knows the brand).

2. Build the heading structure as a flat ordered list of blocks. Block 1 is the H1 (level 1) with a short intro. All other blocks are H2-H6.
   - THE STRUCTURE COMES FROM THE COMPETITORS, not from the knowledge base: one block per mandatory cluster, and a unique cluster only when it clearly helps the reader and fits `max_body_words`. Keep the number of blocks near the number of headings the competitors use. Never add a heading only to place a fact. Facts of the knowledge base fill the sections of the competitors and make them precise; surplus facts stay unused or serve to make this page different from another page of the same brand.
   - The page covers ONE topic. Build it from the clusters that belong to the topic, in the order of the reader's task (what the reader needs first comes first). Never skip heading levels (H2 -> H4). H3+ must sit under a fitting parent.
   - EVERY cluster flagged `mandatory: true` that belongs to the topic must be covered by a heading (several near-duplicate clusters may share one heading; list their ids in `covers_clusters`). Competitors often repeat the same sections on every page of their site (games, general bonuses, about the casino, company data): a mandatory cluster that is NOT about the topic of this page is not covered; put it into `skipped_clusters` with a short reason (for example "belongs to the payments page"). At most half of the mandatory clusters may be skipped, and a cluster that fits the topic is never skipped.
   - Add a unique (non-mandatory) cluster or an own section only if it helps the task of the reader (for example "what to do if the login fails" on a login page) and the knowledge base or general industry knowledge can answer it. Skip the rest.
   - Other topics of the brand get no section. A neighbouring topic may be mentioned in one clause inside a block (a pointer, not a summary); say so in the `copywriter_notes` where it fits.
   - Headings are written in English here (see the language rule). Put keywords into headings only where it reads naturally and where competitors do it.

3. For EVERY block provide all of the following (this is the format of the ТЗ):
   - `words_min` / `words_max`: allowed length of the BODY text (heading excluded). Use competitors' typical section lengths. The range width is about ±12% of the middle (max/min about 1.27; never above 1.8). The sum of all middles must be close to `target_body_words`. SIZE RULES, checked by code: the whole text is limited to `max_body_words` (the mean of the size group of the competitors named in `targets.tier` plus 20%; the competitors are split into small, medium and large texts and this ТЗ is built for the optimum, `medium`; `target_body_words` is that mean), so the sum of all `words_max` must stay within it, and the sum of the middles is about `target_body_words`. After your answer the code enlarges a block when its facts and connections need more room: every `kb_refs` item takes words in proportion to its length (a short figure or name about 3 words, a sentence 10-20, never more than 30; what a list or a table of the block shows costs the words of its items) and every entity connection takes 15 words. The entities to cover take no words of their own. The enlarged range is the new middle ±12%, and each bound may grow at most 20% over the range you give: a block whose facts and connections need more than 20% above its middle is rejected. So do not inflate ranges yourself; keep the `kb_refs` and the connections of a block proportionate to its size, cut what does not fit, and show enumerations (steps, documents, methods, levels) as a list with short items or as a table, which costs fewer words than prose. A parent heading's own range covers only its own intro text; sub-sections have their own ranges.
   - `keywords`: how many times each keyword must appear in the BODY of this block (heading excluded). Include EVERY keyword, 0 when unused. For every keyword: sum over all blocks + occurrences inside headings must equal `keyword_targets[keyword]` exactly. Counting rules: case-insensitive, whole words, longest match first (an occurrence of "X login" counts only for "X login", not also for "X"). Spread them naturally: the brand and the topic keyword early (intro) and in the sections where they belong. Never more than 1 keyword mention per ~15 words in a block.
   - `entities`: 2-4 entities the block must cover (they take no words of their own: name only what the text really has to cover), each with `priority` 1-10 (10 = the main entity of the block). Take them from `entity_candidates` and from the topic (for a login page: account, password, two-factor authentication, verification, mobile app; for a payments page: payment systems, limits, processing times). Use generic names for the brand itself (e.g. "Online Casino", "Sportsbook"), never the brand name. Entities that are specific facts about the brand (a licence, a payment method, a provider, a VIP level) may be listed only if they appear in `facts_to_respect` or in the knowledge base of the block; otherwise list the category and let the notes say "name specifics only if given in the brand information".
   - `entity_connections`: 1-4 relations between entities the text must state explicitly, as subject -> relation (a verb phrase) -> object, with `priority` 1-10. Example: Two-Factor Authentication -> protects -> Player Account [8].
   - `summary`: 1-3 sentences, what the block says, in ENGLISH.
   - `copywriter_notes`: binding instructions in ENGLISH: which entity to lead with, order of the argument, what to avoid, which facts must not be invented, tone, where a neighbouring topic of the brand may be pointed to in one clause. Concrete, not generic. Quote tracked keywords and proper names exactly as they are written (straight quotes), and when you want the writer to use a specific wording in the page language, quote that wording.
   - `listed_entities` (optional): the names, exactly as in `entities`, of the entities that the block only enumerates as items of its list or table (payment systems in a payments table, VIP levels in a list). They are not narrated, so they do not enlarge the block. Leave it empty when the block explains its entities in prose.
   - `formats`: list from ["paragraph", "list", "table"]; a block may combine formats (e.g. ["paragraph","list"]). Rules:
     * Bulleted list: equal items that need no attributes (features, document types, reasons).
     * Numbered list: a sequence of steps whose order matters (login, registration, installation of the app, claiming a bonus, withdrawal). A task page nearly always has one.
     * Table: whenever two or more attributes must be given per item (payment methods with limits and speed, bonus terms, VIP levels with requirements, sports markets with limits, support channels with hours). Code checks: a block about payments or deposits has "table", a block about registration has "list", a pros and cons block has "table" (pros | cons).
     * Everything else is prose ("paragraph"): do not turn facts that can be explained in a sentence or two into a list or a table.
     * There is NO brand fact sheet on this page: never return `fact_table`.
   - `kb_refs`: ONLY when the context contains `knowledge_base`: the list of PATHS into the knowledge base whose values this block must use, e.g. `brandinfo_welcome.welcome_bonus.total_bonus`, `brandinfo_deposit.deposit_methods`. Path syntax: variable key, then dotted keys and `[index]` for list items. The code inserts the VALUES verbatim into the ТЗ, so NEVER copy or paraphrase values yourself and never invent a path. Take ONLY the facts that serve the topic of this page (a login page uses the registration and login steps, security, verification, support and app data; it does not need the games or the VIP programme). Variables of other topics stay unused: that is intended. Reference the narrowest useful path. At least half of the blocks must carry brand facts; a block with no fitting fact (for example a general explanation of how two-factor authentication works) may have an empty list, and then the notes say that the block uses general wording only. Without a knowledge base return an empty list.
   - `source`: "h1", "mandatory" or "unique".
   LANGUAGE RULE: the whole brief is ALWAYS in English, whatever the GEO or page language: `intent_summary`, `heading`, `summary`, `copywriter_notes`, entity names and relations. Do NOT translate it into the page language. The heading is localized in the next step (the planned keywords stay in it).

   When a knowledge base is present, base `entities`, `entity_connections`, `summary` and `copywriter_notes` on the facts it contains (concrete names, amounts, methods, steps) instead of generic wording, and in `copywriter_notes` say which facts must be stated and how. If the knowledge base itself flags a conflict or says two values differ (e.g. "unresolved conflict", "another site section says"), tell the writer explicitly which value to use or to leave the point out; never let the writer decide. Never contradict the knowledge base. Facts about the brand that are not in the knowledge base must not appear anywhere in the ТЗ.
   If a fact that the topic needs is missing from the knowledge base (for example the login URL or the steps of the password reset), do not invent it: write in `copywriter_notes` that the block explains the point in general terms only.

   INTERNAL LINKS (site structure): the brand site has a base set of pages: home, bonuses, app, promo code, login, no deposit bonus, payments. This page links to the home page (see the "Home link" line) and may link to a neighbouring page where the topic comes up inside a sentence (a login page names the bonus, an app page names the login). The code plants such optional links in blocks whose heading or summary names the neighbouring topic. Never add a section for a link, and never turn a neighbouring topic into a summary (one clause is enough). An anchor is at most 3 words.

4. Check the whole brief for consistency before answering: logical order of the reader's task, no overlapping blocks, the intro does not duplicate later sections, entity connections do not contradict each other, keyword and word sums are correct, nothing that belongs to another topic of the brand has crept in.

Return the result through the tool (`skipped_clusters` only when you skipped clusters).

# USER

{
 "geo": "SG",
 "page_language": "English",
 "page_type": "brand-subpage",
 "brand": "Longfu88",
 "keywords": [
  "Longfu88",
  "Longfu88 login",
  "Longfu login",
  "Longfu88 register",
  "Longfu88 casino login"
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
  "Login to Longfu88 Casino: Easy Access to Your Favorite Games",
  "Longfu88 Login & Register ‚Äî Create Your Account in Minutes"
 ],
 "competitor_stats": [
  {
   "url": "https://longfu88-sg.com/login/",
   "body_words": 844,
   "keywords_in_total": {
    "Longfu88": 16,
    "Longfu88 login": 0,
    "Longfu login": 0,
    "Longfu88 register": 0,
    "Longfu88 casino login": 0
   },
   "keywords_in_h1": {
    "Longfu88": 1,
    "Longfu88 login": 0,
    "Longfu login": 0,
    "Longfu88 register": 0,
    "Longfu88 casino login": 0
   },
   "keywords_in_h2": {
    "Longfu88": 2,
    "Longfu88 login": 0,
    "Longfu login": 0,
    "Longfu88 register": 0,
    "Longfu88 casino login": 0
   }
  },
  {
   "url": "https://longfu88-play.my/login/",
   "body_words": 1754,
   "keywords_in_total": {
    "Longfu88": 32,
    "Longfu88 login": 2,
    "Longfu login": 0,
    "Longfu88 register": 0,
    "Longfu88 casino login": 0
   },
   "keywords_in_h1": {
    "Longfu88": 0,
    "Longfu88 login": 1,
    "Longfu login": 0,
    "Longfu88 register": 0,
    "Longfu88 casino login": 0
   },
   "keywords_in_h2": {
    "Longfu88": 3,
    "Longfu88 login": 1,
    "Longfu login": 0,
    "Longfu88 register": 0,
    "Longfu88 casino login": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 1299,
  "competitor_body_words": 1299,
  "max_body_words": 1559,
  "keyword_targets": {
   "Longfu88": 24,
   "Longfu88 login": 1,
   "Longfu login": 1,
   "Longfu88 register": 1,
   "Longfu88 casino login": 1
  }
 },
 "heading_clusters": [
  {
   "id": "k01",
   "canonical_title": "Registration and Login",
   "topic": "Registration and login",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 104,
   "avg_position": 0.34,
   "examples": [
    "How to Register and Log In to Your Longfu88 Account",
    "Step-by-Step Registration Process",
    "Troubleshooting Login Issues – Get Back to Gaming Fast",
    "1. Double-Check Your Login Information"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "Bonuses and Welcome Offers",
   "topic": "Bonuses and welcome offers",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 35,
   "avg_position": 0.42,
   "examples": [
    "Longfu88 Casino Bonuses – Start Your Journey with Exciting Offers",
    "Welcome Bonus Overview",
    "Create Your Account ‚Äî Claim 188% Welcome Bonus"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Safety and Fair Play",
   "topic": "Licence, security and fair play",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 76,
   "avg_position": 0.53,
   "examples": [
    "How do I verify my account?",
    "Account Security Features at Longfu88",
    "Account Verification Requirements",
    "Verify Your Account ‚Äî Unlock Full Access"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Account Recovery and Password Reset",
   "topic": "Other: Account Recovery and Password Reset",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 125,
   "avg_position": 0.27,
   "examples": [
    "Account Recovery and Password Reset"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "2. Clear Your Browser Cache and Cookies",
   "topic": "Other: 2. Clear Your Browser Cache and Cookies",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 39,
   "avg_position": 0.33,
   "examples": [
    "2. Clear Your Browser Cache and Cookies"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "3. Try a Different Device or Browser",
   "topic": "Other: 3. Try a Different Device or Browser",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 40,
   "avg_position": 0.4,
   "examples": [
    "3. Try a Different Device or Browser"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Managing Your Longfu88 Account Settings",
   "topic": "Other: Managing Your Longfu88 Account Settings",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 57,
   "avg_position": 0.53,
   "examples": [
    "Managing Your Longfu88 Account Settings"
   ]
  },
  {
   "id": "k02",
   "canonical_title": "Customer Support",
   "topic": "Customer support",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 62,
   "avg_position": 0.57,
   "examples": [
    "4. Contact Customer Support",
    "Customer Support – We’re Here to Help!"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Payment Methods",
   "topic": "Deposit methods and payments",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 110,
   "avg_position": 0.6,
   "examples": [
    "Deposit and Withdrawal Limits"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Communication Preferences",
   "topic": "Other: Communication Preferences",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 62,
   "avg_position": 0.67,
   "examples": [
    "Communication Preferences"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Frequently Asked Questions",
   "topic": "FAQ",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 0,
   "avg_position": 0.73,
   "examples": [
    "FAQ – Frequently Asked Questions"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "Multi-Currency and Multi-Account Policies",
   "topic": "Other: Multi-Currency and Multi-Account Policies",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 122,
   "avg_position": 0.73,
   "examples": [
    "Multi-Currency and Multi-Account Policies"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Account Closure and Self-Exclusion",
   "topic": "Other: Account Closure and Self-Exclusion",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 106,
   "avg_position": 0.8,
   "examples": [
    "Account Closure and Self-Exclusion"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Games Overview",
   "topic": "Games overview",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 20,
   "avg_position": 0.87,
   "examples": [
    "Your Account Opens Thousands of Games"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "What should I do if I forgot my password?",
   "topic": "Other: What should I do if I forgot my password?",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 48,
   "avg_position": 0.87,
   "examples": [
    "What should I do if I forgot my password?"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Mobile Access",
   "topic": "Mobile access and app",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 115,
   "avg_position": 0.93,
   "examples": [
    "Mobile Account Access"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "VIP Programme",
   "topic": "VIP programme and loyalty",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 180,
   "avg_position": 1.0,
   "examples": [
    "VIP Account Benefits and Tier Progression"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "Register",
   "competitors": 2
  },
  {
   "entity": "Log In",
   "competitors": 2
  },
  {
   "entity": "Complete Registration",
   "competitors": 2
  },
  {
   "entity": "Bitcoin",
   "competitors": 2
  },
  {
   "entity": "VIP",
   "competitors": 1
  },
  {
   "entity": "MYR 2",
   "competitors": 1
  },
  {
   "entity": "MYR 50",
   "competitors": 1
  },
  {
   "entity": "MYR",
   "competitors": 1
  },
  {
   "entity": "USD",
   "competitors": 1
  },
  {
   "entity": "THB",
   "competitors": 1
  },
  {
   "entity": "CNY",
   "competitors": 1
  },
  {
   "entity": "REGISTER",
   "competitors": 1
  },
  {
   "entity": "SMS",
   "competitors": 1
  },
  {
   "entity": "Diamond",
   "competitors": 1
  },
  {
   "entity": "Easy Access",
   "competitors": 1
  },
  {
   "entity": "Your Favorite Games",
   "competitors": 1
  },
  {
   "entity": "Step-by-Step Registration Process",
   "competitors": 1
  },
  {
   "entity": "Troubleshooting Login Issues",
   "competitors": 1
  },
  {
   "entity": "Get Back",
   "competitors": 1
  },
  {
   "entity": "Gaming Fast",
   "competitors": 1
  },
  {
   "entity": "Double-Check Your Login Information",
   "competitors": 1
  },
  {
   "entity": "Clear Your Browser Cache",
   "competitors": 1
  },
  {
   "entity": "Cookies",
   "competitors": 1
  },
  {
   "entity": "Different Device",
   "competitors": 1
  },
  {
   "entity": "Browser",
   "competitors": 1
  },
  {
   "entity": "Contact Customer Support",
   "competitors": 1
  },
  {
   "entity": "Start Your Journey",
   "competitors": 1
  },
  {
   "entity": "Exciting Offers",
   "competitors": 1
  },
  {
   "entity": "Welcome Bonus Overview",
   "competitors": 1
  },
  {
   "entity": "Customer Support",
   "competitors": 1
  },
  {
   "entity": "We’re Here",
   "competitors": 1
  },
  {
   "entity": "Help",
   "competitors": 1
  },
  {
   "entity": "Frequently Asked Questions",
   "competitors": 1
  },
  {
   "entity": "Can I",
   "competitors": 1
  },
  {
   "entity": "Singapore",
   "competitors": 1
  },
  {
   "entity": "Button",
   "competitors": 1
  },
  {
   "entity": "Choose Your Preferred Bonus",
   "competitors": 1
  },
  {
   "entity": "Casino Bonus",
   "competitors": 1
  },
  {
   "entity": "Sports Bonus",
   "competitors": 1
  },
  {
   "entity": "Promo Code",
   "competitors": 1
  },
  {
   "entity": "No Bonus",
   "competitors": 1
  },
  {
   "entity": "Enter Personal Details",
   "competitors": 1
  },
  {
   "entity": "Identity Verification",
   "competitors": 1
  },
  {
   "entity": "Google Chrome",
   "competitors": 1
  },
  {
   "entity": "Mozilla Firefox",
   "competitors": 1
  },
  {
   "entity": "Casino Welcome Package",
   "competitors": 1
  },
  {
   "entity": "Sports Betting Bonus",
   "competitors": 1
  },
  {
   "entity": "Crypto Bonus",
   "competitors": 1
  },
  {
   "entity": "Ethereum",
   "competitors": 1
  },
  {
   "entity": "Litecoin",
   "competitors": 1
  },
  {
   "entity": "Contacting Us",
   "competitors": 1
  },
  {
   "entity": "Live Chat",
   "competitors": 1
  },
  {
   "entity": "Available",
   "competitors": 1
  },
  {
   "entity": "Email Support",
   "competitors": 1
  },
  {
   "entity": "Send",
   "competitors": 1
  },
  {
   "entity": "Forgot Password",
   "competitors": 1
  },
  {
   "entity": "Äî Create Your Account",
   "competitors": 1
  },
  {
   "entity": "Minutes",
   "competitors": 1
  },
  {
   "entity": "Create Your Account",
   "competitors": 1
  },
  {
   "entity": "Äî Claim 188",
   "competitors": 1
  }
 ]
}
