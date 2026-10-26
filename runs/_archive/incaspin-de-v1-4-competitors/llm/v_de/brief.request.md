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
   - `kb_refs`: ONLY when the context contains `knowledge_base` (brand information chosen in AffBulk): the list of PATHS into the knowledge base whose values this block must use, e.g. `brandinfo_welcome.welcome_bonus.total_bonus`, `brandinfo_deposit.deposit_methods`, `brandinfo_loyalty.loyalty_vip_program.ranks[0]`. Path syntax: variable key, then dotted keys and `[index]` for list items. The code inserts the VALUES verbatim into the ТЗ, so NEVER copy or paraphrase values yourself and never invent a path. Assign the facts to the section where they belong (welcome bonus data -> bonus section, deposit methods -> payments, licence/operator -> licensing/about, registration guide -> registration, and so on). Reference the narrowest useful path (a whole variable only when the whole variable is needed). Every block needs at least one reference, and EVERY variable of the knowledge base must be used by at least one block. Without a knowledge base return an empty list.
   - `source`: "h1", "mandatory" or "unique".
   Write `summary`, `copywriter_notes` and entity/relation names in the PAGE LANGUAGE (like a real ТЗ for a writer in that language).

   When a knowledge base is present, base `entities`, `entity_connections`, `summary` and `copywriter_notes` on the facts it contains (concrete names, amounts, methods, providers) instead of generic wording, and in `copywriter_notes` say which facts must be stated and how (e.g. which wagering figure applies). If the knowledge base itself flags a conflict or says two values differ (e.g. "unresolved conflict", "another site section says"), tell the writer explicitly which value to use or to leave the point out; never let the writer decide. Never contradict the knowledge base. Facts about the brand that are not in the knowledge base must not appear anywhere in the ТЗ.

4. Check the whole brief for consistency before answering: logical order, no overlapping blocks, the intro does not duplicate later sections, entity connections do not contradict each other, keyword and word sums are correct.

Return the result through the tool.

# USER

{
 "geo": "DE",
 "page_language": "German",
 "keywords": [
  "Incaspin",
  "Incaspin casino",
  "Inca Spin"
 ],
 "facts_to_respect": [],
 "knowledge_base": {
  "title": "incaspin-new",
  "variables": {
   "brandinfo_general": {
    "brand_name": "Incaspin",
    "domain": "incaspin.com",
    "release_year": 2025,
    "minimum_age": 18,
    "operator": {
     "company_name": "Legasta Technologies SRL",
     "company_number": "3-102-921383",
     "jurisdiction": "Costa Rica",
     "registered_address": "Province 01 San Jose, Canton 01 San Jose, Cathedral District, Tenth Avenue, Thirty-Three and Thirty-Five Streets, Office 3335"
    },
    "payment_agent": {
     "company_name": "OptaStream Innovations Limited",
     "registration_number": "HE 472273",
     "jurisdiction": "Cyprus",
     "registered_address": "Souliou, 18, 2018, Strovolos, Nicosia, Cyprus"
    },
    "licences": [
     {
      "authority": "Tobique Gaming Commission",
      "licence_number": "0000158",
      "jurisdiction": "Tobique"
     }
    ],
    "currencies": [
     "EUR",
     "BRL",
     "CAD",
     "AUD",
     "BTC",
     "ETH"
    ],
    "customer_support": {
     "channels": [
      "24/7 live chat",
      "Email",
      "FAQ"
     ],
     "email": "support@incaspin.com",
     "availability": "24/7",
     "languages": [
      "English",
      "Multiple languages"
     ]
    },
    "business_overview": {
     "categories": [
      "Online casino",
      "Live casino",
      "Sportsbook",
      "Esports betting"
     ],
     "games": "More than 6,000 casino games are advertised",
     "welcome_bonus": "Up to €2,750 + 275 Free Spins",
     "minimum_deposit": "€20 for the detailed first-deposit casino offer and the sportsbook welcome offer; previously recorded standard deposit minimum €15 for select other payment options.",
     "payment_methods_overview": [
      "Visa",
      "Mastercard",
      "Apple Pay",
      "Google Pay",
      "Skrill",
      "Neteller",
      "Cryptocurrency",
      "Bank transfer"
     ],
     "security": "HTTPS/TLS 1.3, SSL certificates, WAF and DDoS protection; identity checks and responsible-gaming controls"
    }
   },
   "brandinfo_welcome": {
    "welcome_bonus": {
     "name": "Casino Welcome Package",
     "total_bonus": "Up to €2,750",
     "total_free_spins": 275,
     "wagering": "35x bonus on the detailed second and third deposit promotional cards; general bonus rules specify 40x unless stated otherwise",
     "minimum_deposit": "€20 on the detailed first-deposit promotional card; deposit tiers of €20, €50 and €300 are displayed.",
     "validity": "7 days for Welcome Package bonuses",
     "max_bet": "€5 for slots and €10 for live games while wagering, subject to specific terms",
     "promo_code_required": false,
     "claiming": "Welcome Package bonuses are credited automatically; entering a promo code for a Welcome Package bonus makes the player ineligible for that package bonus",
     "free_spins_games": [
      "Gates of Olympus",
      "Aztec Magic",
      "Aztec Magic Deluxe",
      "Johnny Cash",
      "Platinum Lightning",
      "Platinum Lightning Deluxe"
     ],
     "free_spins_delivery": "The detailed terms describe 50 Free Spins daily for five days after the first deposit; activation is available for 3 days and Free Spins/results have 7-day validity",
     "important_terms": [
      "Welcome bonus presentation lists first deposit up to €1,000 + 200 Free Spins, second deposit 100% up to €1,000, and third deposit 75% up to €750 + 75 Free Spins.",
      "Second-deposit promotion card displays code INC2 and third-deposit card displays INC3, while the general Welcome Package terms state bonuses are automatic and promo codes disqualify them; this is an unresolved conflict within the supplied site text.",
      "Only one bonus may be active at a time; active bonuses can be paused but their expiry timers continue.",
      "Bonus winnings can be withdrawn only after the relevant wagering requirements are met.",
      "Slots contribute 100% to wagering; card games, roulette, poker and video poker 5%; live-dealer games 0%, as listed in the bonus FAQ.",
      "Bonuses are sticky and the real-money balance is played first.",
      "The maximum winnings from sign-up Free Spins are €50 unless an offer states otherwise."
     ]
    }
   },
   "brandinfo_promotions": {
    "other_bonuses": [
     {
      "name": "Highroller Bonus",
      "type": "Deposit reload",
      "bonus": "50% up to €500",
      "minimum_deposit": "€300",
      "wagering": "40x bonus",
      "validity": "30 days between eligible offers",
      "eligibility": "Players who have used all casino Welcome Package bonuses; excluded for Finnish players",
      "important_terms": [
       "The highroller offer may be used every 30 days.",
       "General bonus maximum bet rules apply unless specific terms override them."
      ]
     },
     {
      "name": "Sunday Reload",
      "type": "Weekly deposit bonus",
      "bonus": "25% up to €100",
      "minimum_deposit": "€15",
      "wagering": "40x",
      "validity": "14 days under the earlier bonus schedule",
      "availability": "Sunday"
     },
     {
      "name": "Weekly Cashback",
      "type": "Casino cashback",
      "cashback": "Up to 25% of weekly net losses",
      "important_terms": [
       "The amount depends on player activity and loyalty status."
      ]
     }
    ],
    "gamification_features": [
     {
      "name": "Wheel of Fortune",
      "mechanics": "Spin the wheel to win prizes",
      "rewards": [
       "Prizes"
      ]
     },
     {
      "name": "Missions",
      "mechanics": "Complete daily, weekly and lifetime missions",
      "rewards": [
       "Boomerang Points and other mission rewards"
      ],
      "important_terms": [
       "Daily missions reset each day.",
       "Lifetime missions can award up to 100,000 BP."
      ]
     },
     {
      "name": "Reward Chests",
      "mechanics": "Spend Boomerang Points to open chests with randomized rewards",
      "possible_rewards": [
       "Cash bonuses",
       "Free Spins",
       "Boomerang Points",
       "iPhone 17",
       "Rolex",
       "100 g gold bar",
       "MacBook Pro M5",
       "Porsche 911 Turbo S"
      ],
      "examples": [
       "€10 cash",
       "€50 cash",
       "5 Free Spins",
       "10 Free Spins",
       "50 BP",
       "100 BP",
       "250 BP"
      ],
      "special_chests": [
       {
        "name": "Inca Chest",
        "displayed_price": "1,000 BP"
       },
       {
        "name": "Paititi Treasure",
        "displayed_price": "1,000,000 BP"
       }
      ]
     },
     {
      "name": "Points Store",
      "mechanics": "Redeem earned Boomerang Points for rewards"
     }
    ]
   },
   "brandinfo_loyalty": {
    "loyalty_vip_program": {
     "program_name": "Boomerang",
     "currency": "Boomerang Points (BP)",
     "progression": "Earn BP through real-money slots activity; cumulative lifetime BP determines rank and spendable BP can be redeemed for chests",
     "points_earning": "Per €10 of real-money slots stakes: Scout 100 BP; Shaman 150 BP; Chief 200 BP; Emperor 300 BP; Legend 400 BP; Inca 500 BP",
     "ranks": [
      {
       "name": "Scout",
       "rank_number": 1,
       "points_to_unlock": 0,
       "bp_per_10_eur_slot_stake": 100
      },
      {
       "name": "Shaman",
       "rank_number": 2,
       "points_to_unlock": 25000,
       "bp_per_10_eur_slot_stake": 150
      },
      {
       "name": "Chief",
       "rank_number": 3,
       "points_to_unlock": 150000,
       "bp_per_10_eur_slot_stake": 200
      },
      {
       "name": "Emperor",
       "rank_number": 4,
       "points_to_unlock": 1500000,
       "bp_per_10_eur_slot_stake": 300
      },
      {
       "name": "Legend",
       "rank_number": 5,
       "points_to_unlock": 10000000,
       "bp_per_10_eur_slot_stake": 400
      },
      {
       "name": "Inca",
       "rank_number": 6,
       "points_to_unlock": 60000000,
       "bp_per_10_eur_slot_stake": 500
      }
     ],
     "rewards": [
      "Boomerang Points",
      "Reward chests",
      "Free Spins",
      "Cash bonuses",
      "Prizes from reward chests"
     ],
     "missions": [
      "Daily",
      "Weekly",
      "Lifetime"
     ],
     "additional_loyalty_structure": {
      "name": "Bronze–Platinum loyalty/VIP model also described in the site text",
      "tiers": [
       {
        "name": "Bronze"
       },
       {
        "name": "Silver",
        "extra_cashback": "+1%"
       },
       {
        "name": "Gold",
        "extra_cashback": "+2%",
        "vip_access": "VIP Club access"
       },
       {
        "name": "Platinum",
        "extra_cashback": "+3%"
       }
      ],
      "vip_benefits": [
       "Additional VIP awards",
       "Higher limits",
       "Personalized service"
      ]
     },
     "important_terms": [
      "The site text contains two differently named rank models (Boomerang and Bronze–Platinum), and does not establish their exact relationship.",
      "Loyalty rank may increase withdrawal limits."
     ]
    }
   },
   "brandinfo_account": {
    "registration": {
     "methods": [
      "Email registration"
     ],
     "guide": [
      "Open incaspin.com and choose Sign up.",
      "Enter an email address.",
      "Create a password.",
      "Confirm that you are at least 18 years old.",
      "Submit the registration form."
     ],
     "restrictions": [
      "Only one account per person.",
      "One account per household, IP address and computer.",
      "Duplicate accounts may be suspended, closed and their wagers, bonuses or winnings voided."
     ]
    },
    "login": {
     "methods": [
      "Email and password"
     ],
     "guide": [
      "Select Log in.",
      "Enter the registered email and password.",
      "Submit to access the account."
     ],
     "password_recovery": "Use Forgot Password on the login screen and follow the emailed reset instructions.",
     "security": "Two-factor authentication can be activated in account settings.",
     "account_management": [
      "Profile details and currency preferences",
      "Payment methods",
      "Betting and gaming history",
      "Bonus progress",
      "Responsible-gaming limits"
     ]
    },
    "verification": {
     "required": "Identity verification may be required before the first withdrawal and during deposit checks; no withdrawals are processed until the account is fully verified.",
     "documents": [
      "Passport or national identity card or driving licence",
      "Recent utility bill or bank statement",
      "Evidence of the payment method used",
      "Selfie with identity document or live identity check"
     ],
     "additional_checks": [
      "Video verification where required documents cannot be supplied in Latin or Cyrillic alphabets",
      "Telephone verification when required by the casino"
     ],
     "processing_time": "Most document reviews take a few hours to one day according to the website overview.",
     "important_terms": [
      "Documents must be authentic.",
      "False or fraudulent documentation may result in seizure of deposited funds and winnings."
     ]
    }
   },
   "brandinfo_responsible_gaming": {
    "responsible_gaming": {
     "minimum_age": 18,
     "deposit_limits": {
      "periods": [
       "Daily (rolling 24 hours)",
       "Weekly (rolling 168 hours)",
       "Monthly (rolling 720 hours)"
      ],
      "how_to_set": "My Account > Responsible Gaming > Daily Limit, Weekly Limit or Monthly Limit",
      "decreasing_limits": "Immediately",
      "increasing_or_removing_limits": "24-hour delay",
      "interaction": "A lower weekly or monthly cap can supersede higher shorter-period caps; rolling-window deposits count toward limits."
     },
     "other_limits": [
      "Wagering limits",
      "Loss caps mentioned in the site overview",
      "Session-time limits mentioned in the site overview"
     ],
     "activity_tracking": "Account records allow users to review bets and activity.",
     "self_exclusion": {
      "duration": "3 months to 5 years or indefinite",
      "default_if_not_specified": "6 months",
      "request_procedure": [
       "Select self-exclusion from account controls.",
       "Choose a period.",
       "Confirm and submit the request.",
       "Receive confirmation by email."
      ],
      "during_exclusion": [
       "Account access blocked",
       "No new deposits or withdrawals during exclusion",
       "No casino promotional messages from the operator"
      ],
      "reactivation": "No automatic reactivation after a fixed exclusion; contact support. Early cancellation of fixed exclusion requires internal review and at least 24 hours' cool-off. An indefinite self-exclusion cancellation request has a 7-day waiting period.",
      "balance": "Indefinite exclusions are paid subject to limits; for time-limited exclusions remaining balance may be paid after the exclusion period."
     },
     "support": [
      "Live chat",
      "Email",
      "Gambling Therapy",
      "Gamblers Anonymous",
      "BeGambleAware self-assessment"
     ],
     "minors_protection": [
      "Do not share login details or bank cards with minors",
      "Use parental-control or filtering software"
     ],
     "warnings": [
      "Gambling should not be considered income.",
      "Avoid chasing losses and betting while under the influence.",
      "Set and keep budgets and take breaks."
     ]
    }
   },
   "brandinfo_games": {
    "game_types": [
     "Slots",
     "Live casino",
     "Roulette",
     "Blackjack",
     "Baccarat",
     "Poker",
     "Table games",
     "Instant win",
     "Crash games",
     "Bonus Buy",
     "Jackpots",
     "Original games",
     "Books",
     "Drops & Wins Slots"
    ],
    "game_count": "More than 6,000 games advertised; another site section says 5,000+",
    "game_examples": {
     "slots": [
      "Diamond Strike: Lucky Reels",
      "Burning Chilli X",
      "Mad Jesters: Hold & Win",
      "Gates of Olympus 2500",
      "Obsidian Rush",
      "Big Bass Splash",
      "Gates of Olympus",
      "Book of Khonsu",
      "Book of Hidden Tombs",
      "Coin Strike Hold and Win",
      "Double Dragon Gold: Hold & Win"
     ],
     "live_games": [
      "Lightning Roulette",
      "Crazy Time",
      "Sweet Bonanza CandyLand",
      "Ice Fishing",
      "Sic Bo",
      "Speed Baccarat",
      "Disco Balls",
      "Red Door Roulette",
      "Gates of Olympus Roulette",
      "Dragon Tiger"
     ],
     "instant_and_crash": [
      "Chicken Road",
      "Chicken Road 2",
      "Plinko",
      "Plinko 2",
      "Golden Plinko",
      "Tower Rush",
      "Aviamasters"
     ],
     "jackpots": [
      "Break The Piggy Bank",
      "Crown of Fire Jackpot Play",
      "Shining Hot 40 Jackpot Play",
      "Triple Money Jackpot Spicy!",
      "Halloween Jackpot",
      "Triple Money Jackpot Gold!"
     ]
    },
    "original_games": {
     "provider": "Incaspin Originals",
     "examples": [
      "Chicken Road 2",
      "Dragon Pots",
      "Chicken Road",
      "MegaBlock",
      "Chicken Coin",
      "Joker's Clash",
      "Plinko1000"
     ],
     "category_count_displayed": 76
    },
    "providers": [
     "Pragmatic Play",
     "Playson",
     "Penguin King",
     "Amiry Games",
     "BGaming",
     "Endorphina",
     "Booongo",
     "Evolution",
     "Original Games",
     "Gamzix",
     "NetGame",
     "Spinomenal",
     "Pragmatic Play Live",
     "GameBeat",
     "Novomatic",
     "Belatra",
     "Hacksaw Gaming",
     "1spin4win",
     "Platipus",
     "PG Soft",
     "Evoplay",
     "SmartSoft",
     "Clawbuster",
     "RetroGames",
     "Tom Horn Native",
     "Gaming Corps",
     "Apparat",
     "Slotopia",
     "BSG",
     "GameArt",
     "Onlyplay",
     "Push Gaming",
     "Playtech",
     "MGA Games",
     "Bang Bang Games",
     "Aviator",
     "LuckyStreak",
     "Zillion",
     "Spadegaming",
     "Jacks",
     "Mascot",
     "KA Gaming",
     "Big Time Gaming",
     "Max Win Gaming",
     "Felix Gaming",
     "Popiplay",
     "100HP Gaming",
     "Red Tiger",
     "NetEnt",
     "Aviatrix",
     "RubyPlay",
     "Yggdrasil",
     "Reflex Gaming",
     "ReelPlay",
     "4ThePlayer",
     "TrueLab",
     "Mancala",
     "ICONIC21",
     "Voltent",
     "Turbo Games",
     "Thunderkick",
     "Swintt",
     "AvatarUX",
     "Microgaming",
     "Peter & Sons",
     "The Originals",
     "GameTimeTec",
     "Mirror Image Gaming",
     "Galaxsys",
     "EXCO",
     "PatePlay",
     "VA Gaming",
     "Nolimit City",
     "Happy Duck",
     "Koala",
     "Betora",
     "Fazi",
     "Shady Lady",
     "King Midas",
     "Boomerang Studios",
     "GoodLuck Games",
     "Alfa Games",
     "Booming Games",
     "OneFiveFive",
     "Animo",
     "XStudio",
     "Maybrix",
     "Toucan Royale",
     "SpinLogic",
     "Hazzo",
     "Gamevy",
     "Dijoker",
     "Torro Games",
     "Spartix",
     "Optiplay",
     "Big Daddy Gaming"
    ]
   },
   "brandinfo_sportsbook": {
    "sportsbook": {
     "has_sportsbook": true,
     "navigation": [
      "Popular",
      "Live",
      "Upcoming",
      "Predictions",
      "Bets Feed",
      "SlotBets",
      "Sports",
      "Esports",
      "Racing"
     ],
     "sports": [
      "Football",
      "Tennis",
      "Basketball",
      "Ice hockey",
      "Cricket",
      "Volleyball",
      "Baseball",
      "Snooker",
      "Handball",
      "Table tennis",
      "American football",
      "Chess",
      "Formula 1",
      "Horse racing",
      "Boxing",
      "Australian football",
      "Rugby league",
      "Rugby union",
      "MMA",
      "Darts",
      "Futsal",
      "Badminton",
      "Bandy",
      "Water polo",
      "Cross-country skiing",
      "Floorball",
      "Golf",
      "Cycling",
      "Bowls",
      "Alpine skiing",
      "Biathlon",
      "Ski jumping",
      "NASCAR",
      "Sailing",
      "Surfing",
      "Sumo",
      "Kabaddi",
      "Touring car racing",
      "Formula 2"
     ],
     "esports": [
      "Counter-Strike",
      "eFootball",
      "eBasketball",
      "eFootball: Penalty",
      "eHorse Racing",
      "eSoccer: Volta",
      "eFighting",
      "eTennis",
      "eCricket"
     ],
     "sports_leagues_shown": [
      "UEFA Champions League",
      "English Premier League",
      "Italian Serie A",
      "German Bundesliga",
      "Spanish LaLiga",
      "Portuguese Primeira Liga",
      "Turkish Super Lig",
      "Saudi Pro League",
      "Argentinian Liga Profesional",
      "English FA Cup"
     ],
     "bet_types": [
      "1x2 / three-way result",
      "Double chance",
      "Totals (over/under)",
      "Handicap",
      "Early Payout 1x2",
      "Accumulators/combinations",
      "Live bets"
     ],
     "betting_features": [
      "Quick Bet mode allows immediate placement by clicking a selection",
      "BetSlip with stake presets of 10, 30, 50 and 100",
      "Hot Combos with combined selections",
      "Comboboost displayed as x1.15 on an example selection",
      "Top Events cards with countdowns",
      "Match favorites",
      "My Bets/history",
      "Live and upcoming markets"
     ],
     "screenshots_notes": "Sportsbook interface and available markets are evidenced by the five user-provided screenshots. Example fixture odds and match times fluctuate and are not treated as permanent facts.",
     "welcome_bonus": {
      "name": "Sportsbook Welcome Package",
      "total_bonus": "Up to €450",
      "eligibility": "Newly registered players, first three qualifying sports deposits",
      "bonuses": [
       {
        "name": "First Sports Deposit Bonus",
        "match": "100% up to €100"
       },
       {
        "name": "Second Sports Deposit Bonus",
        "match": "75% up to €150"
       },
       {
        "name": "Third Sports Deposit Bonus",
        "match": "50% up to €200"
       }
      ],
      "minimum_deposit": "€20",
      "activation": "Choose the sports bonus before depositing",
      "wagering": "5x sportsbook bonus",
      "validity": "14 days",
      "eligible_bets": "Accumulator wagers containing at least 3 events, each selection at odds of at least 1.40",
      "excluded_bets": [
       "Voided bets",
       "Cashed-out bets"
      ],
      "settlement": "Bonus-funded bets must settle before the balance can transfer to real money; unused bonus funds and winnings expire after 14 days",
      "balance_rules": "The bonus balance may fund bets when real money is insufficient, with differences taken from real money as described in the terms"
     },
     "reload_bonus": {
      "name": "Sunday Sports Reload",
      "eligibility": "At least 3 prior deposits; activate the promotion code specified on the offer card before funding",
      "availability": "Every Sunday 00:00–23:59 UTC",
      "wagering": "5x",
      "min_accumulator_odds": 2.74,
      "minimum_events": 3,
      "minimum_odds_per_event": 1.4,
      "validity": "7 days",
      "important_terms": [
       "A no-risk bet is limited to one per player during the promotional period."
      ]
     },
     "weekly_sports_cashback": {
      "name": "Weekly Sports Cashback",
      "qualifying_stake": "At least €10",
      "bets": [
       "Singles",
       "Multiples"
      ],
      "calculation": "Weekly net loss compared with total deposits; no cashback if weekly deposits are less than net loss",
      "period": "Monday 01:00 UTC to Sunday 23:59 UTC",
      "levels": [
       {
        "name": "Bronze",
        "cashback": "6%",
        "maximum": "€300"
       },
       {
        "name": "Silver",
        "cashback": "7%",
        "maximum": "€1,000"
       },
       {
        "name": "Gold",
        "cashback": "8%",
        "maximum": "€2,000"
       },
       {
        "name": "Platinum",
        "cashback": "10%",
        "maximum": "€5,000"
       }
      ],
      "reward": "Bonus with 1x wagering",
      "wagering_window": "7 days",
      "minimum_accumulator_odds": 2.74,
      "minimum_events": 3,
      "min_odds_each": 1.4
     }
    }
   },
   "brandinfo_deposit": {
    "deposit_methods": [
     {
      "method": "Visa",
      "minimum": "€15",
      "maximum": "€4,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Mastercard",
      "minimum": "€15",
      "maximum": "€4,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Revolut",
      "minimum": "€15",
      "maximum": "€4,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Skrill",
      "minimum": "€15",
      "maximum": "€4,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Paysafecard",
      "minimum": "€15",
      "maximum": "€1,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Neteller",
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Jeton",
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Apple Pay",
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Google Pay",
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Bank Transfer",
      "minimum": "€10",
      "maximum": "€5,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Same day to 1–3 business days",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Bitcoin (BTC)",
      "minimum": "€15 equivalent",
      "maximum": "€5,000 equivalent",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant on the overview; transaction confirmation may vary",
      "currencies": [
       "BTC"
      ]
     },
     {
      "method": "Ethereum (ETH)",
      "minimum": "€15 equivalent",
      "maximum": "€5,000 equivalent",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant on the overview; transaction confirmation may vary",
      "currencies": [
       "ETH"
      ]
     },
     {
      "method": "Litecoin (LTC)",
      "minimum": "€15 equivalent",
      "maximum": "€5,000 equivalent",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant on the overview; transaction confirmation may vary",
      "currencies": [
       "LTC"
      ]
     },
     {
      "method": "Dogecoin (DOGE)",
      "minimum": "€10 equivalent",
      "maximum": "€5,000 equivalent",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Instant on the overview; transaction confirmation may vary",
      "currencies": [
       "DOGE"
      ]
     }
    ],
    "deposit_guide": [
     "Log in to your Incaspin account.",
     "Open the Deposit section or cashier.",
     "Choose an available payment method.",
     "Enter the desired amount and check that method-specific limits are met.",
     "Follow the payment-provider instructions and confirm the transaction.",
     "Check the account balance after the deposit is credited."
    ]
   },
   "brandinfo_withdrawal": {
    "withdrawal_methods": [
     {
      "method": "Visa OCT",
      "minimum": "€50–€120 depending on residence/payment option",
      "maximum": "€15,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing; site overview describes instant to a few hours after processing",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Mastercard Payment Transfer",
      "minimum": "€50–€120 depending on residence/payment option",
      "maximum": "€15,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing; site overview describes instant to a few hours after processing",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Skrill",
      "minimum": "€50–€120 depending on residence/payment option",
      "maximum": "€5,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing, plus provider time",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Neteller",
      "minimum": "€50–€120 depending on residence/payment option",
      "maximum": "€5,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing, plus provider time",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Jeton",
      "minimum": "€50–€120 depending on residence/payment option",
      "maximum": "€5,000",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing, plus provider time",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Bank Transfer",
      "minimum": "€50–€120 depending on residence/payment option",
      "maximum": "€15,000",
      "fee": "No casino fee; intermediary bank charges may apply up to €16",
      "transaction_speed": "Up to 72 hours internal processing plus bank transfer time of 1–5 business days",
      "currencies": [
       "EUR"
      ]
     },
     {
      "method": "Bitcoin (BTC)",
      "minimum": "€50–€120 equivalent",
      "maximum": "€15,000 equivalent",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing plus blockchain confirmation",
      "currencies": [
       "BTC"
      ]
     },
     {
      "method": "Ethereum (ETH)",
      "minimum": "€50–€120 equivalent",
      "maximum": "€15,000 equivalent",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing plus blockchain confirmation",
      "currencies": [
       "ETH"
      ]
     },
     {
      "method": "Litecoin (LTC)",
      "minimum": "€50–€120 equivalent",
      "maximum": "€15,000 equivalent",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing plus blockchain confirmation",
      "currencies": [
       "LTC"
      ]
     },
     {
      "method": "Dogecoin (DOGE)",
      "minimum": "€50–€120 equivalent",
      "maximum": "€5,000 equivalent",
      "fee": "No casino fee; external provider charges may apply",
      "transaction_speed": "Up to 72 hours internal processing plus blockchain confirmation",
      "currencies": [
       "DOGE"
      ]
     }
    ],
    "withdrawal_guide": [
     "Sign in and open the account cashier or Withdraw section.",
     "Choose an available withdrawal method, preferably the original deposit method where applicable.",
     "Enter the withdrawal amount and check your personal limit.",
     "Complete any required identity or payment verification.",
     "Confirm the withdrawal request.",
     "Allow up to 72 hours for internal processing, followed by the payment provider settlement period."
    ],
    "important_terms": [
     "A withdrawal minimum between €50 and €120 depends on country or payment method.",
     "Deposited funds must be wagered at least three times before withdrawal.",
     "No withdrawals are processed until full account verification.",
     "Maximum withdrawal limits may depend on loyalty rank and are visible in the cashier.",
     "The detailed terms allow monthly installments of up to €10,000 for winnings exceeding €10,000, overriding the older stored €15,000 installment rule.",
     "A cryptocurrency sent to a wrong network address may be considered for recovery only above €5,000, with a 0.1 BTC recovery charge and no guarantee of success.",
     "External bank or payment-provider costs may apply despite zero casino fees."
    ]
   },
   "brandinfo_app": {
    "app_information": {
     "type": "Progressive Web App (PWA)",
     "mobile_web": true,
     "ios_available": true,
     "android_available": true,
     "distribution": "Install directly from the website/browser, without using an app store",
     "ios_guide": [
      "Open Incaspin in Safari on iPhone or iPad.",
      "Tap Share.",
      "Select Add to Home Screen.",
      "Choose a name and tap Add."
     ],
     "android_guide": [
      "Open Incaspin in the mobile browser.",
      "Select Install App or Add to Home Screen.",
      "Confirm installation.",
      "Launch from the home-screen icon."
     ],
     "sections": [
      "Casino",
      "Live Casino",
      "Sports",
      "Esports",
      "Bonuses",
      "Promotions",
      "Wheel of Fortune",
      "Loyalty",
      "Missions"
     ]
    }
   },
   "brandinfo_privacy_policy": {
    "privacy_policy": {
     "data_controller": {
      "company_name": "Legasta Technologies SRL",
      "jurisdiction": "Costa Rica",
      "registered_address": "Province 01 San Jose, Canton 01 San Jose, Cathedral District, Tenth Avenue, Thirty-Three and Thirty-Five Streets, Office 3335"
     },
     "data_collected": {
      "registration": [
       "Email address",
       "Account details"
      ],
      "verification": [
       "Identity document",
       "Proof of address",
       "Payment method documents",
       "Selfie or live identity check where requested"
      ],
      "financial": [
       "Deposit and withdrawal information",
       "Payment method details"
      ],
      "gaming_activity": [
       "Wagering and betting history",
       "Bonus history"
      ],
      "security": [
       "Account authentication information"
      ]
     },
     "data_collection_methods": [
      "Registration",
      "Identity verification",
      "Deposits and withdrawals",
      "Casino and sportsbook betting",
      "Account activity and customer support"
     ],
     "data_usage": {
      "account_management": "Account creation, authentication and management",
      "identity_verification": "Know Your Customer and age/identity checks",
      "payment_processing": "Handling and verifying financial transactions",
      "gaming_services": "Maintaining gaming and betting account records",
      "regulatory_compliance": "Anti-money laundering checks",
      "security": "Protecting accounts and personal documents",
      "customer_support": "Responding to account and payment inquiries"
     },
     "third_party_sharing": {
      "payment_agent": "OptaStream Innovations Limited handles payment-related operations as named in earlier accepted brand data",
      "regulatory_compliance": "The site describes identity and payment verification carried out for compliance"
     },
     "data_security": {
      "encryption": "TLS 1.3 / HTTPS / SSL protection stated in the supplied site overview",
      "infrastructure": [
       "Web Application Firewall",
       "DDoS protection"
      ],
      "verification_documents": "The site states that verification documents are encrypted and processed securely"
     },
     "user_rights": {
      "account_updates": "Players can amend personal profile information in account settings"
     },
     "minors_privacy": {
      "age_restrictions": "Players must be at least 18 years old"
     }
    }
   }
  }
 },
 "competitor_h1": [
  "Incaspin Casino",
  "IncaSpin Online Casino",
  "IncaSpin Casino – hebe den Inka-Goldschatz"
 ],
 "competitor_stats": [
  {
   "url": "https://inca-spin.de/de",
   "body_words": 1836,
   "keywords_in_total": {
    "Incaspin": 1,
    "Incaspin casino": 20,
    "Inca Spin": 0
   },
   "keywords_in_h1": {
    "Incaspin": 0,
    "Incaspin casino": 1,
    "Inca Spin": 0
   },
   "keywords_in_h2": {
    "Incaspin": 0,
    "Incaspin casino": 6,
    "Inca Spin": 0
   }
  },
  {
   "url": "https://incaaspin.com/",
   "body_words": 1893,
   "keywords_in_total": {
    "Incaspin": 27,
    "Incaspin casino": 0,
    "Inca Spin": 13
   },
   "keywords_in_h1": {
    "Incaspin": 1,
    "Incaspin casino": 0,
    "Inca Spin": 0
   },
   "keywords_in_h2": {
    "Incaspin": 4,
    "Incaspin casino": 0,
    "Inca Spin": 1
   }
  },
  {
   "url": "https://incaspin.casino/de/",
   "body_words": 2896,
   "keywords_in_total": {
    "Incaspin": 16,
    "Incaspin casino": 22,
    "Inca Spin": 0
   },
   "keywords_in_h1": {
    "Incaspin": 0,
    "Incaspin casino": 1,
    "Inca Spin": 0
   },
   "keywords_in_h2": {
    "Incaspin": 0,
    "Incaspin casino": 3,
    "Inca Spin": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 1893,
  "keyword_targets": {
   "Incaspin": 16,
   "Incaspin casino": 20,
   "Inca Spin": 1
  }
 },
 "heading_clusters": [
  {
   "id": "k07",
   "canonical_title": "Spiele im Überblick",
   "topic": "Games overview and game library",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 36,
   "avg_position": 0.35,
   "examples": [
    "Spiele im Incaspin Casino",
    "Ons Spellenassortiment",
    "Beliebte Spiele",
    "Top-Spiele"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Registrierung Schritt für Schritt",
   "topic": "Registration",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 154,
   "avg_position": 0.38,
   "examples": [
    "Incaspin Casino Registrierung",
    "Hoe je account aanmaken bij IncaSpin",
    "In wenigen Schritten registriert"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Slots",
   "topic": "Slots",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3,
    4
   ],
   "avg_section_words": 67,
   "avg_position": 0.38,
   "examples": [
    "Top Slots",
    "Slots",
    "Gokkasten en Progressieve Jackpots",
    "Slots in allen Variationen"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "Willkommensbonus und Bonusangebote",
   "topic": "Welcome bonus and bonus overview",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 65,
   "avg_position": 0.4,
   "examples": [
    "Alle Bonusangebote im Überblick",
    "Incaspin Casino Bonuses",
    "Willkommenspaket",
    "First Deposit Bonus"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Live Casino",
   "topic": "Live casino",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3,
    4
   ],
   "avg_section_words": 91,
   "avg_position": 0.43,
   "examples": [
    "Live",
    "Live Games",
    "Live Casino",
    "Live-Casino mit echten Dealern"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Zahlungsmethoden und Einzahlungen",
   "topic": "Payments and deposits",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 86,
   "avg_position": 0.51,
   "examples": [
    "Zahlungen",
    "Betalingsmethoden bij IncaSpin",
    "Stortingsmethoden",
    "Zahlungen und schnelle Auszahlungen"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Tischspiele und Jackpots",
   "topic": "Table games, instant games and jackpots",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    3,
    4
   ],
   "avg_section_words": 117,
   "avg_position": 0.57,
   "examples": [
    "Table Games",
    "Tafelspellen en Instantspellen",
    "Jackpots und Tischspiele"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Auszahlungen",
   "topic": "Withdrawals: methods and processing time",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 50,
   "avg_position": 0.57,
   "examples": [
    "Opnamemethoden en Verwerkingstijden",
    "Schnelle Auszahlungen",
    "Wie zahle ich im Incaspin Casino Gewinne aus?",
    "Hoe lang duurt een uitbetaling bij IncaSpin?"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "App und mobiles Spielen",
   "topic": "Mobile app / mobile play",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 70,
   "avg_position": 0.73,
   "examples": [
    "Incaspin Casino App",
    "Kann ich das Incaspin Casino auf dem Handy nutzen?",
    "Mobiel Spelen bij IncaSpin",
    "Kan ik IncaSpin op mijn mobiel spelen?"
   ]
  },
  {
   "id": "k21",
   "canonical_title": "Häufige Fragen",
   "topic": "FAQ",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 72,
   "avg_position": 0.86,
   "examples": [
    "FAQ",
    "Veelgestelde Vragen",
    "Häufige Fragen zu IncaSpin Casino"
   ]
  },
  {
   "id": "k02",
   "canonical_title": "Warum Incaspin Casino",
   "topic": "Why choose / what makes the casino special",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 72,
   "avg_position": 0.41,
   "examples": [
    "Waarom Kiezen voor IncaSpin?",
    "Das macht IncaSpin Casino besonders"
   ]
  },
  {
   "id": "k01",
   "canonical_title": "Incaspin Casino im Überblick",
   "topic": "Casino overview / information",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 186,
   "avg_position": 0.51,
   "examples": [
    "Incaspin Casino Informationen",
    "IncaSpin Casino – dein Abenteuer rund um den Inka-Goldschatz",
    "Für wen ist IncaSpin Casino gedacht?"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "VIP- und Treueprogramm",
   "topic": "VIP and loyalty programme",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 112,
   "avg_position": 0.52,
   "examples": [
    "Onze Trouwheidsprogramma en VIP-voordelen",
    "VIP-Treueprogramm",
    "Der VIP-Club und unser Treueprogramm"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Sicherheit und Lizenz",
   "topic": "Safety, licence and fairness",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 100,
   "avg_position": 0.55,
   "examples": [
    "Veiligheid en Licentie",
    "Is IncaSpin een betrouwbaar casino?",
    "Sicherheit und Fairness"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Kundensupport",
   "topic": "Customer support",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 54,
   "avg_position": 0.71,
   "examples": [
    "Klantenservice bij Inca Spin",
    "Hoe neem ik contact op met de klantenservice van IncaSpin?",
    "Support rund um die Uhr",
    "Support rund um die Uhr"
   ]
  },
  {
   "id": "k23",
   "canonical_title": "Fazit",
   "topic": "Conclusion / call to action",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 122,
   "avg_position": 0.83,
   "examples": [
    "Conclusie",
    "Bereit für dein Abenteuer?"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Crash- und Instant-Spiele",
   "topic": "Crash and instant games",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 20,
   "avg_position": 0.08,
   "examples": [
    "Crash & Instant"
   ]
  },
  {
   "id": "k24",
   "canonical_title": "Letzte Gewinne",
   "topic": "Latest wins widget",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 214,
   "avg_position": 0.41,
   "examples": [
    "Letzte Gewinne"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "Spieleanbieter",
   "topic": "Game providers",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 160,
   "avg_position": 0.43,
   "examples": [
    "Onze Softwareleveranciers"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Weitere Aktionen und Cashback",
   "topic": "Other promotions: highroller bonus and cashback",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 37,
   "avg_position": 0.5,
   "examples": [
    "Highroller Bonus",
    "Cashback-Aktion – Wöchentliche Rückzahlungen auf Nettoverluste"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Promo-Code",
   "topic": "Promo code",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 197,
   "avg_position": 0.58,
   "examples": [
    "Promo-Code im Incaspin Casino: So nutzen Sie exklusive Angebote"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Verifizierung",
   "topic": "Verification",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    4
   ],
   "avg_section_words": 58,
   "avg_position": 0.69,
   "examples": [
    "Sichere Verifizierung"
   ]
  },
  {
   "id": "k20",
   "canonical_title": "Verantwortungsvolles Spielen",
   "topic": "Responsible gambling",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 163,
   "avg_position": 0.83,
   "examples": [
    "Verantwortungsvolles Spielen"
   ]
  },
  {
   "id": "k22",
   "canonical_title": "Kostenlos spielen",
   "topic": "Free play / demo mode",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 28,
   "avg_position": 0.88,
   "examples": [
    "Kann ich im Incaspin Casino kostenlos spielen?"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "Android",
   "competitors": 3
  },
  {
   "entity": "Visa",
   "competitors": 3
  },
  {
   "entity": "Freispiele",
   "competitors": 2
  },
  {
   "entity": "Auszahlungen",
   "competitors": 2
  },
  {
   "entity": "Spiele",
   "competitors": 2
  },
  {
   "entity": "Spielen",
   "competitors": 2
  },
  {
   "entity": "Bonus",
   "competitors": 2
  },
  {
   "entity": "Spieler",
   "competitors": 2
  },
  {
   "entity": "Slots",
   "competitors": 2
  },
  {
   "entity": "Willkommenspaket",
   "competitors": 2
  },
  {
   "entity": "Konto",
   "competitors": 2
  },
  {
   "entity": "Einzahlungen",
   "competitors": 2
  },
  {
   "entity": "Aktionen",
   "competitors": 2
  },
  {
   "entity": "Spiel",
   "competitors": 2
  },
  {
   "entity": "Auswahl",
   "competitors": 2
  },
  {
   "entity": "Browser",
   "competitors": 2
  },
  {
   "entity": "Tobique Gaming Commission",
   "competitors": 2
  },
  {
   "entity": "Freispielen",
   "competitors": 2
  },
  {
   "entity": "Support",
   "competitors": 2
  },
  {
   "entity": "Daten",
   "competitors": 2
  },
  {
   "entity": "Einzahlung",
   "competitors": 2
  },
  {
   "entity": "Evolution",
   "competitors": 2
  },
  {
   "entity": "Verfügung",
   "competitors": 2
  },
  {
   "entity": "Überblick",
   "competitors": 2
  },
  {
   "entity": "Umsatzbedingungen",
   "competitors": 2
  },
  {
   "entity": "Regel",
   "competitors": 2
  },
  {
   "entity": "Jahren",
   "competitors": 2
  },
  {
   "entity": "E-Mail",
   "competitors": 2
  },
  {
   "entity": "E-Mail-Adresse",
   "competitors": 2
  },
  {
   "entity": "Limits",
   "competitors": 2
  },
  {
   "entity": "Lobby",
   "competitors": 2
  },
  {
   "entity": "BTC",
   "competitors": 2
  },
  {
   "entity": "LTC",
   "competitors": 2
  },
  {
   "entity": "Skrill",
   "competitors": 2
  },
  {
   "entity": "Live-Chat",
   "competitors": 2
  },
  {
   "entity": "Passwort",
   "competitors": 2
  },
  {
   "entity": "Bedingungen",
   "competitors": 2
  },
  {
   "entity": "Boni",
   "competitors": 2
  },
  {
   "entity": "Kassenbereich",
   "competitors": 2
  },
  {
   "entity": "NetEnt",
   "competitors": 2
  },
  {
   "entity": "Titel",
   "competitors": 2
  },
  {
   "entity": "Multiplikatoren",
   "competitors": 2
  },
  {
   "entity": "Dealer",
   "competitors": 2
  },
  {
   "entity": "Guthaben",
   "competitors": 2
  },
  {
   "entity": "Mastercard",
   "competitors": 2
  },
  {
   "entity": "Angebote",
   "competitors": 2
  },
  {
   "entity": "Willkommensbonus",
   "competitors": 2
  },
  {
   "entity": "Crazy Time",
   "competitors": 2
  },
  {
   "entity": "Legasta Technologies SRL",
   "competitors": 2
  },
  {
   "entity": "Name",
   "competitors": 2
  },
  {
   "entity": "Geburtsdatum",
   "competitors": 2
  },
  {
   "entity": "Gewinne",
   "competitors": 2
  },
  {
   "entity": "Woche",
   "competitors": 2
  },
  {
   "entity": "Teil",
   "competitors": 2
  },
  {
   "entity": "Jackpots",
   "competitors": 2
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 2
  },
  {
   "entity": "Runden",
   "competitors": 2
  },
  {
   "entity": "Ziel",
   "competitors": 2
  },
  {
   "entity": "Zahlungsmethoden",
   "competitors": 2
  },
  {
   "entity": "Betrag",
   "competitors": 2
  }
 ]
}
