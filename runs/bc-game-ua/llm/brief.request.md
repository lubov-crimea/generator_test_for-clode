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
 "geo": "UA",
 "page_language": "Ukrainian",
 "keywords": [
  "BC Game",
  "BCGame",
  "BC Games",
  "BC Game казино"
 ],
 "facts_to_respect": [],
 "knowledge_base": {
  "title": "BC game-new",
  "variables": {
   "brandinfo_general": {
    "brandinfo_general": {
     "brand_name": "BC.Game",
     "release_year": 2017,
     "minimum_age": "18+ or the higher legal gambling age applicable in the player's jurisdiction",
     "licences": [
      {
       "regulator": "Government of the Autonomous Island of Anjouan",
       "jurisdiction": "Union of the Comoros",
       "licence_number": "ALSI-202410011-FI1",
       "operator": "Twocent Technology Limited"
      }
     ],
     "operator": {
      "company_name": "Twocent Technology Limited",
      "registration_number": "41939",
      "registered_address": "Sea Urchin Street #2, San Pedro, Ambergris Caye, Belize"
     },
     "currencies": [
      "EUR",
      "USD",
      "BTC",
      "ETH",
      "BNB",
      "XRP"
     ],
     "customer_support": {
      "channels": [
       "24/7 live support"
      ],
      "availability": "24/7",
      "feedback_email": "feedback@bcgame.com",
      "security_email": "security@bcgame.com",
      "legal_compliance_email": "compliance@bcgame.com"
     },
     "overview": {
      "products": [
       "Online casino",
       "Sports betting",
       "Live casino",
       "Slots",
       "Crash and original games",
       "Poker",
       "Lottery",
       "Racing",
       "UpDown",
       "Bingo",
       "Predictions"
      ],
      "welcome_offer": "Four-stage deposit welcome package with deposit bonuses and rakeback",
      "minimum_qualifying_welcome_deposit": "€5",
      "deposit_methods": [
       "Cryptocurrency",
       "PayDo",
       "Skrill",
       "Tink",
       "Neteller"
      ],
      "withdrawal_methods": [
       "Cryptocurrency",
       "PayDo",
       "Skrill",
       "Neteller"
      ],
      "sportsbook": "Pre-match and in-play betting across football, cricket, NFL, esports and more than 80 sports",
      "mobile_access": "Progressive Web App (PWA)",
      "responsible_gambling": "Deposit, wagering and loss limits; cooling-off and self-exclusion options"
     }
    }
   },
   "brandinfo_welcome": {
    "brandinfo_welcome": {
     "welcome_bonus": {
      "name": "Four-Stage Deposit Welcome Package",
      "stages": [
       {
        "stage": "Deposit 1",
        "bonus": "180% deposit bonus + 40% rakeback",
        "minimum_qualifying_deposit": "€5"
       },
       {
        "stage": "Deposit 2",
        "bonus": "240% deposit bonus + 60% rakeback",
        "minimum_qualifying_deposit": "€9"
       },
       {
        "stage": "Deposit 3",
        "bonus": "300% deposit bonus + 100% rakeback",
        "minimum_qualifying_deposit": "€20"
       },
       {
        "stage": "Deposit 4",
        "bonus": "360% deposit bonus + 140% rakeback",
        "minimum_qualifying_deposit": "€30"
       }
      ],
      "eligibility": "Exclusive to new users; available for 24 hours only",
      "claiming_conditions": "Each bonus starts locked. After making a qualifying deposit, manually claim the locked bonus; the reward is added to the locked balance as Deposit Rakeback. Place bets as usual; the locked bonus unlocks in real time as wagers settle. Claim unlocked rewards from the Bonus page.",
      "availability_cycle": "Four deposit bonus chances each month; all four reset on the 1st day of each month at 00:00 UTC",
      "reward_withdrawal": "Unlocked rewards are described as real cash and can be withdrawn immediately; no expiration is stated for unlocked rewards"
     }
    }
   },
   "brandinfo_promotions": {
    "brandinfo_promotions": {
     "terms_status": "Promotional mechanics and wagering conditions marked as modeled are illustrative assumptions for knowledge-base completion, not verified official BC.GAME terms.",
     "promotions": [
      {
       "name": "300% Deposit Bonus",
       "type": "Deposit Bonus",
       "status": "Advertised promotion",
       "reward": {
        "bonus_percentage": 300,
        "maximum_bonus": "$500",
        "minimum_deposit": "$20",
        "maximum_qualifying_deposit": "$166.67"
       },
       "wagering_requirements": {
        "requirement": "35x bonus amount",
        "eligible_games": {
         "slots": "100%",
         "live_casino": "10%",
         "table_games": "10%",
         "sports_betting": "10%"
        },
        "maximum_bet_during_wagering": "$5"
       },
       "validity": {
        "claim_period": "24 hours after registration or within the displayed promotion period",
        "wagering_period": "7 days after bonus activation"
       },
       "claiming_guide": [
        "Register and open the Deposit or Promotions section.",
        "Select the 300% Deposit Bonus while it is available.",
        "Make a qualifying deposit of at least $20.",
        "Activate the promotion before placing eligible wagers.",
        "Complete the wagering requirement before the expiry deadline."
       ],
       "withdrawal_conditions": {
        "bonus_balance_withdrawable": false,
        "winnings_withdrawable": "After completing the wagering requirement and any required account verification",
        "maximum_withdrawable_bonus_winnings": "$5,000"
       },
       "terms_and_conditions": [
        "One welcome promotion per person and household.",
        "Only eligible deposits count toward the promotion.",
        "Deposits must originate from a payment method belonging to the player.",
        "The maximum bet restriction applies while wagering the bonus.",
        "Uncompleted wagering requirements expire at the end of the stated validity period.",
        "Bonus abuse, duplicate accounts and fraudulent activity may result in bonus cancellation."
       ]
      },
      {
       "name": "Ongoing Cashback",
       "type": "Cashback",
       "status": "Advertised promotion",
       "reward": {
        "cashback_percentage": 10,
        "calculation_basis": "Net eligible losses during the weekly calculation period",
        "maximum_cashback": "$500 per week",
        "minimum_eligible_net_loss": "$10"
       },
       "wagering_requirements": {
        "requirement": "1x cashback amount",
        "maximum_bet_during_wagering": "$100"
       },
       "schedule": {
        "calculation_period": "Monday 00:00 UTC to Sunday 23:59 UTC",
        "crediting": "Within 24 hours after the weekly calculation period ends"
       },
       "claiming_guide": [
        "Place eligible real-money wagers during the calculation period.",
        "Allow eligible winnings and losses to be included in the weekly calculation.",
        "Open the Cashback or Promotions section.",
        "Claim the cashback reward when it becomes available.",
        "Complete the wagering requirement before withdrawing the cashback amount and associated winnings."
       ],
       "terms_and_conditions": [
        "Cashback is calculated on net eligible losses, not total turnover.",
        "Cancelled bets, refunded stakes, bonus-funded wagers and excluded games do not count.",
        "Cashback cannot exceed $500 per weekly period.",
        "The reward must be claimed within 7 days of crediting.",
        "Fraudulent wagering and bonus abuse may result in forfeiture."
       ]
      },
      {
       "name": "7-Day Gift",
       "type": "Daily Task Reward",
       "status": "Advertised reward",
       "reward": {
        "maximum_total_free_spins": 120,
        "free_spins_per_completed_day": 20,
        "minimum_qualifying_deposit": "$10",
        "minimum_eligible_wager_per_day": "$10"
       },
       "wagering_requirements": {
        "requirement": "35x winnings generated by free spins",
        "maximum_bet_during_wagering": "$5",
        "maximum_convertible_winnings": "$500"
       },
       "validity": {
        "task_period": "7 consecutive days after activation",
        "free_spin_expiry": "7 days after each free-spin reward is credited",
        "displayed_end_date": "2026-10-30"
       },
       "claiming_guide": [
        "Activate the promotion during its availability period.",
        "Complete the daily qualifying task.",
        "Claim 20 free spins for each completed day.",
        "Repeat the task for up to seven days to receive a maximum of 120 free spins.",
        "Complete the wagering requirement for winnings generated by free spins."
       ],
       "terms_and_conditions": [
        "A maximum of 20 free spins can be earned per qualifying day.",
        "Incomplete daily tasks do not qualify for a reward.",
        "Unused free spins expire according to the stated validity period.",
        "Free-spin winnings are credited to a bonus balance until the wagering requirement is completed.",
        "Account verification may be required before withdrawal."
       ]
      },
      {
       "name": "Free Spins Giveaway",
       "type": "Sports Betting Promotion",
       "status": "Advertised reward",
       "reward": {
        "free_spins_per_day": 20,
        "maximum_free_spins_per_day": 20,
        "minimum_qualifying_sports_bet": "€10",
        "minimum_odds_per_selection": 1.5
       },
       "wagering_requirements": {
        "requirement": "35x free-spin winnings",
        "maximum_bet_during_wagering": "€5"
       },
       "validity": {
        "qualifying_period": "One calendar day per reward",
        "free_spin_expiry": "7 days after crediting",
        "displayed_end_date": "2026-10-22"
       },
       "claiming_guide": [
        "Place qualifying real-money sports bets totalling at least €10 during the promotion period.",
        "Ensure that the bets meet the minimum odds requirement.",
        "Claim the daily reward from the Promotions section.",
        "Use the awarded 20 free spins on the designated eligible slot.",
        "Complete the wagering requirement for any resulting winnings."
       ],
       "terms_and_conditions": [
        "Only settled qualifying bets count toward the daily threshold.",
        "Voided bets, cashed-out bets and refunded stakes are excluded.",
        "The reward is limited to 20 free spins per eligible day.",
        "The free-spin reward cannot be exchanged directly for cash.",
        "The promotion expires on the displayed end date."
       ]
      },
      {
       "name": "Daily Wagering Contest",
       "type": "Wagering Competition",
       "status": "Advertised competition",
       "eligibility": {
        "minimum_eligible_wager": "$100 per contest day",
        "ranking_basis": "Total eligible settled real-money wagering volume",
        "contest_period": "Daily, 00:00–23:59 UTC"
       },
       "rewards": {
        "prize_pool": "Variable daily pool displayed on the Contest page",
        "distribution": {
         "1st_place": "30% of the prize pool",
         "2nd_place": "20% of the prize pool",
         "3rd_place": "12% of the prize pool",
         "4th_to_10th_place": "Share the remaining 38% equally"
        }
       },
       "wagering_requirements": {
        "additional_wagering_requirement": "1x prize amount if the prize is credited as bonus funds",
        "cash_prize_requirement": "No additional wagering if credited as withdrawable cash"
       },
       "claiming_guide": [
        "Open the Contest page and review the active prize pool.",
        "Place eligible real-money wagers during the contest period.",
        "Reach the qualifying wagering threshold.",
        "Check the final leaderboard after the contest closes.",
        "Claim the awarded prize according to the displayed settlement rules."
       ],
       "terms_and_conditions": [
        "Only eligible settled wagers count toward leaderboard ranking.",
        "Voided bets, refunded stakes and promotional wagers are excluded.",
        "The prize pool varies with qualifying activity.",
        "Tied positions are resolved according to the contest rules displayed on the platform.",
        "Multiple accounts and attempts to manipulate rankings are prohibited."
       ]
      },
      {
       "name": "Weekly Raffle",
       "type": "Raffle",
       "status": "Advertised prize pool",
       "rewards": {
        "maximum_weekly_prize_pool": "$5,000",
        "first_prize": "$2,000",
        "second_prize": "$1,000",
        "third_prize": "$500",
        "remaining_prize_pool": "$1,500 distributed among eligible winning entries"
       },
       "eligibility": {
        "minimum_eligible_wager_per_ticket": "$10",
        "maximum_entries_per_player_per_week": 100,
        "entry_basis": "One raffle entry for every $10 of eligible settled real-money wagering"
       },
       "schedule": {
        "frequency": "Weekly",
        "draw_time": "Sunday at 23:59 UTC",
        "claim_deadline": "7 days after the winner announcement"
       },
       "wagering_requirements": {
        "cash_prizes": "No additional wagering requirement",
        "bonus_prizes": "35x bonus amount before withdrawal"
       },
       "claiming_guide": [
        "Open the Weekly Raffle page.",
        "Place qualifying wagers to earn raffle entries.",
        "Check the number of entries credited to the account.",
        "Wait for the weekly draw and check the winner announcement.",
        "Claim any prize within the stated claim period."
       ],
       "terms_and_conditions": [
        "The $5,000 figure represents the advertised maximum weekly prize pool, not a guaranteed individual prize.",
        "A maximum of 100 entries per player is allowed per week under these modeled conditions.",
        "Voided bets, refunded stakes and bonus-funded wagering do not qualify.",
        "Unclaimed prizes expire after the claim deadline."
       ]
      },
      {
       "name": "Referral / Refer a Friend",
       "type": "Referral Promotion",
       "status": "Advertised programme",
       "rewards": {
        "referrer_reward": "$25",
        "new_player_reward": "$10",
        "reward_type": "Bonus cash"
       },
       "eligibility": {
        "minimum_first_deposit": "$20",
        "minimum_qualifying_wager": "5x the new player's first deposit",
        "qualifying_period": "30 days after registration"
       },
       "wagering_requirements": {
        "requirement": "10x bonus amount",
        "maximum_bet_during_wagering": "$5"
       },
       "claiming_guide": [
        "Open the Referral section and copy the personal referral link.",
        "The invited player registers using the referral link.",
        "The invited player completes the first qualifying deposit.",
        "The invited player completes the required eligible wagering volume.",
        "The referral rewards are credited after eligibility checks."
       ],
       "terms_and_conditions": [
        "The invited player must be a new customer.",
        "Self-referrals, duplicate accounts and shared-account manipulation are prohibited.",
        "The referral reward is limited to one qualifying reward per invited player.",
        "Both accounts must comply with identity verification and account eligibility requirements."
       ]
      },
      {
       "name": "FIFA World Cup 2026 Hub",
       "type": "Event Promotion",
       "status": "Advertised event prize pool",
       "rewards": {
        "advertised_total_prize_pool": "$2,000,000+",
        "individual_reward": "Depends on the eligible campaign, contest or prize draw"
       },
       "eligibility": {
        "minimum_qualifying_sports_bet": "$10",
        "minimum_odds_per_selection": 1.5,
        "qualifying_markets": "Eligible FIFA World Cup 2026 match markets listed in the campaign"
       },
       "wagering_requirements": {
        "sports_bet_settlement": "Bets must settle normally to qualify",
        "bonus_prize_wagering": "35x bonus amount where a prize is credited as bonus funds",
        "cash_prize_wagering": "No additional wagering requirement for a cash prize"
       },
       "claiming_guide": [
        "Open the FIFA World Cup 2026 Hub.",
        "Select an active campaign and review its entry rules.",
        "Place eligible qualifying bets or complete the specified event task.",
        "Check campaign standings or prize-draw results.",
        "Claim the prize within the deadline stated for the individual campaign."
       ],
       "terms_and_conditions": [
        "The advertised $2 million-plus amount is the combined event prize pool and is not a guaranteed individual payout.",
        "Individual campaigns may have separate qualifying requirements, deadlines and prize limits.",
        "Only eligible settled bets count where sports wagering is required.",
        "Campaign participation is subject to account eligibility and applicable restrictions."
       ]
      },
      {
       "name": "Top 5 Leagues Combo Boost",
       "type": "Sports Betting Promotion",
       "status": "Advertised offer",
       "rewards": {
        "maximum_boost": "35% additional return",
        "advertised_shared_prize_pool": "$500,000",
        "displayed_end_date": "2026-11-10"
       },
       "eligibility": {
        "minimum_accumulator_selections": 3,
        "minimum_odds_per_selection": 1.5,
        "minimum_total_odds": 3.0,
        "minimum_stake": "$10",
        "maximum_stake": "$500"
       },
       "wagering_requirements": {
        "cash_return": "No additional wagering requirement",
        "bonus_credit": "5x bonus amount before withdrawal"
       },
       "claiming_guide": [
        "Open the Sportsbook and select eligible matches from the five leagues covered by the campaign.",
        "Build an accumulator containing at least three qualifying selections.",
        "Meet the minimum odds and stake requirements.",
        "Place the bet before the applicable event starts.",
        "Receive the applicable boost or promotion reward after settlement under the campaign rules."
       ],
       "terms_and_conditions": [
        "The 35% figure is the maximum advertised boost and may depend on the number of qualifying selections.",
        "The $500,000 amount is a shared promotional pool, not an individual guaranteed payout.",
        "Cashed-out, voided or refunded bets do not qualify.",
        "The promotion ends on the displayed deadline or when the operator withdraws the offer under its terms."
       ]
      },
      {
       "name": "Early Payout",
       "type": "Sportsbook Feature",
       "status": "Advertised feature",
       "reward": {
        "benefit": "Eligible winning bets may be settled before the sporting event officially ends",
        "displayed_end_date": "2027-01-01"
       },
       "eligibility": {
        "bet_type": "Eligible pre-match or live single bets",
        "minimum_odds": 1.5,
        "eligible_sports": "Sports and competitions explicitly marked as eligible in the sportsbook"
       },
       "settlement_conditions": [
        "The selection must satisfy the early-payout trigger displayed for the market.",
        "The bet must not have been cashed out, voided or otherwise settled previously.",
        "Only markets carrying the relevant Early Payout indication qualify.",
        "The final settlement follows the market-specific sportsbook rules."
       ],
       "claiming_guide": [
        "Open an eligible sportsbook market.",
        "Check whether the Early Payout indication is displayed.",
        "Place the qualifying bet.",
        "If the event reaches the specified trigger, the bet is settled according to the applicable early-payout rules."
       ]
      },
      {
       "name": "BC Engine",
       "type": "Token Staking and Ecosystem Rewards",
       "status": "Advertised feature",
       "rewards": {
        "reward_source": "BC ecosystem rewards",
        "reward_currency": "$BC",
        "distribution_frequency": "Daily"
       },
       "eligibility": {
        "minimum_stake": "$10 equivalent in $BC",
        "minimum_staking_period": "7 days",
        "maximum_reward_rate": "10% annualized"
       },
       "claiming_guide": [
        "Open the BC Engine section.",
        "Connect or select the eligible account and review the current staking terms.",
        "Stake the eligible amount of $BC.",
        "Keep the stake active for the applicable reward period.",
        "Claim available rewards according to the displayed programme rules."
       ],
       "terms_and_conditions": [
        "The reward rate and eligible staking assets must be checked against the active BC Engine offer.",
        "Rewards depend on the amount staked and the applicable programme rules.",
        "Unstaking may end reward accrual.",
        "Token values can fluctuate and rewards are not guaranteed investment returns."
       ]
      }
     ]
    }
   },
   "brandinfo_loyalty": {
    "brandinfo_loyalty": {
     "program_name": "BC.GAME VIP Club",
     "program_type": "Five-tier loyalty and rewards program",
     "currency": "USD equivalent",
     "progression_system": {
      "progression_basis": "Experience points (XP) earned through eligible settled wagers",
      "tier_advancement": "Players progress through Bronze, Silver, Gold, Platinum and Diamond by accumulating XP from eligible gameplay.",
      "xp_expiration": "No automatic XP expiration is assumed in this model.",
      "tier_downgrade": "VIP benefits may be reduced or status withdrawn for Terms of Service violations or prolonged inactivity where applicable."
     },
     "tiers": [
      {
       "tier": "Bronze",
       "tier_number": 1,
       "qualification": {
        "minimum_xp": 0,
        "maximum_xp": 4999,
        "entry_requirement": "Create an account and begin eligible gameplay."
       },
       "rewards": {
        "level_up_bonus": "$1-$5 per qualifying level",
        "rakeback_rate": "5% of eligible game house edge",
        "coin_drops": "Variable rewards of $0.10-$2",
        "chat_rain": "Occasional promotional coin drops",
        "secret_treasure": "Access to eligible treasure and reward events"
       },
       "rakeback": {
        "calculation": "Eligible wager x applicable game house edge x 5%",
        "claim_frequency": "Accumulates during eligible gameplay; availability depends on the active rakeback feature.",
        "wagering_requirement": "No additional wagering requirement for rakeback credited as withdrawable cash. Promotional credits follow their displayed terms."
       },
       "additional_benefits": [
        "Access to basic loyalty rewards",
        "Participation in eligible contests and community promotions",
        "Progress tracking through the VIP level system"
       ],
       "modeled_bonus_conditions": {
        "level_up_bonus_claim_period": "7 days after becoming eligible",
        "maximum_bonus_per_level": "$5",
        "bonus_wagering_requirement": "5x bonus amount",
        "maximum_bet_during_wagering": "$2"
       },
       "eligibility_and_restrictions": [
        "Only eligible settled wagers contribute to progression.",
        "Voided and refunded wagers do not qualify.",
        "Rewards must be claimed through the relevant account section when required."
       ]
      },
      {
       "tier": "Silver",
       "tier_number": 2,
       "qualification": {
        "minimum_xp": 5000,
        "maximum_xp": 49999,
        "entry_requirement": "Accumulate the required XP through eligible settled wagers."
       },
       "rewards": {
        "level_up_bonus": "$5-$25 per qualifying level",
        "rakeback_rate": "7% of eligible game house edge",
        "rakeback_booster": "Access to eligible rakeback booster promotions",
        "tips_and_rewards": "Additional account rewards and promotional offers",
        "vip_lucky_spin": "Access to eligible lucky-spin events",
        "coin_drops": "Higher-value promotional drops than the Bronze tier"
       },
       "rakeback": {
        "calculation": "Eligible wager x applicable game house edge x 7%",
        "claim_frequency": "Accumulates during eligible gameplay; claim availability depends on the active feature.",
        "wagering_requirement": "No additional wagering requirement for rakeback credited as withdrawable cash. Bonus credits follow their displayed terms."
       },
       "additional_benefits": [
        "Access to Silver-tier reward campaigns",
        "Eligibility for selected reload and cashback promotions",
        "Improved level-up rewards"
       ],
       "modeled_bonus_conditions": {
        "level_up_bonus_claim_period": "7 days after becoming eligible",
        "maximum_bonus_per_level": "$25",
        "bonus_wagering_requirement": "5x bonus amount",
        "maximum_bet_during_wagering": "$5"
       },
       "eligibility_and_restrictions": [
        "XP is awarded only for eligible settled activity.",
        "Promotional rewards may require manual activation.",
        "Rakeback and bonus rewards are calculated separately."
       ]
      },
      {
       "tier": "Gold",
       "tier_number": 3,
       "qualification": {
        "minimum_xp": 50000,
        "maximum_xp": 299999,
        "entry_requirement": "Accumulate the required XP through eligible settled wagers."
       },
       "rewards": {
        "level_up_bonus": "$25-$100 per qualifying level",
        "rakeback_rate": "10% of eligible game house edge",
        "recharge_bonus": "Reload rewards based on eligible recent wagering activity",
        "weekly_cashback": "Modeled cashback of 5% of eligible net losses, capped at $250 per week",
        "monthly_cashback": "Modeled cashback of 3% of eligible net losses, capped at $500 per month",
        "promotional_offers": "Access to selected VIP deposit, reload and cashback offers"
       },
       "rakeback": {
        "calculation": "Eligible wager x applicable game house edge x 10%",
        "claim_frequency": "Accumulates during eligible gameplay; claim frequency depends on the active rakeback feature.",
        "wagering_requirement": "No additional wagering requirement for rakeback credited as withdrawable cash."
       },
       "recharge_bonus": {
        "modeled_rate": "5%-10% of the qualifying recharge calculation",
        "calculation_basis": "Eligible wagering activity during the previous 7 days",
        "claim_frequency": "According to the active recharge schedule",
        "wagering_requirement": "5x bonus amount",
        "maximum_bet_during_wagering": "$10",
        "validity": "7 days after activation"
       },
       "cashback_conditions": {
        "calculation_basis": "Net eligible losses during the relevant weekly or monthly period",
        "minimum_eligible_net_loss": "$20",
        "weekly_claim_deadline": "7 days after crediting",
        "monthly_claim_deadline": "30 days after crediting",
        "wagering_requirement": "1x cashback amount if credited as bonus funds; none if credited as withdrawable cash"
       },
       "additional_benefits": [
        "Access to Gold-tier recharge promotions",
        "Eligibility for weekly and monthly cashback campaigns",
        "Higher level-up rewards than Silver",
        "Priority consideration for selected VIP promotions"
       ],
       "eligibility_and_restrictions": [
        "Cashback is calculated on eligible net losses, not total wager volume.",
        "Refunded bets, voided wagers and excluded promotional activity do not qualify.",
        "Recharge percentages and caps depend on the active offer."
       ]
      },
      {
       "tier": "Platinum",
       "tier_number": 4,
       "qualification": {
        "minimum_xp": 300000,
        "maximum_xp": 999999,
        "entry_requirement": "Accumulate the required XP through eligible settled wagers."
       },
       "rewards": {
        "level_up_bonus": "$100-$500 per qualifying level",
        "rakeback_rate": "12% of eligible game house edge",
        "recharge_bonus": "Modeled rate of 10%-15% of the qualifying recharge calculation",
        "weekly_cashback": "Modeled cashback of 7% of eligible net losses, capped at $1000 per week",
        "monthly_cashback": "Modeled cashback of 4% of eligible net losses, capped at $2500 per month",
        "withdrawal_benefits": "Eligibility for promotional withdrawal-fee waivers where offered",
        "vip_host": "Access to a dedicated VIP host where assigned"
       },
       "rakeback": {
        "calculation": "Eligible wager x applicable game house edge x 12%",
        "claim_frequency": "Accumulates during eligible gameplay; claim availability depends on the active rakeback feature.",
        "wagering_requirement": "No additional wagering requirement for rakeback credited as withdrawable cash."
       },
       "recharge_bonus": {
        "modeled_rate": "10%-15% of the qualifying recharge calculation",
        "calculation_basis": "Eligible wagering activity during the previous 7 days",
        "claim_frequency": "According to the active recharge schedule",
        "wagering_requirement": "5x bonus amount",
        "maximum_bet_during_wagering": "$25",
        "validity": "7 days after activation"
       },
       "cashback_conditions": {
        "calculation_basis": "Net eligible losses during the relevant weekly or monthly period",
        "minimum_eligible_net_loss": "$50",
        "weekly_claim_deadline": "7 days after crediting",
        "monthly_claim_deadline": "30 days after crediting",
        "wagering_requirement": "1x cashback amount if credited as bonus funds; none if credited as withdrawable cash"
       },
       "vip_host_services": [
        "Personalized assistance with account-related questions",
        "Help navigating eligible promotions and rewards",
        "Support with qualifying VIP requests"
       ],
       "additional_benefits": [
        "Higher modeled cashback caps than Gold",
        "Higher level-up rewards",
        "Access to selected private promotions",
        "Eligibility for withdrawal-fee benefits when explicitly offered"
       ],
       "eligibility_and_restrictions": [
        "A dedicated VIP host is subject to assignment by the operator.",
        "Fee-free withdrawals are not guaranteed for every method or jurisdiction.",
        "Cashback, reload and withdrawal benefits remain subject to their individual promotion terms."
       ]
      },
      {
       "tier": "Diamond",
       "tier_number": 5,
       "qualification": {
        "minimum_xp": 1000000,
        "maximum_xp": null,
        "entry_requirement": "Accumulate the required XP through eligible settled wagers. Higher SVIP status or personalized benefits may require a separate invitation."
       },
       "rewards": {
        "level_up_bonus": "$500-$2500 per qualifying level",
        "rakeback_rate": "15% of eligible game house edge",
        "recharge_bonus": "Modeled rate of 15%-20% of the qualifying recharge calculation",
        "weekly_cashback": "Modeled cashback of 10% of eligible net losses, capped at $5000 per week",
        "monthly_cashback": "Modeled cashback of 5% of eligible net losses, capped at $10000 per month",
        "birthday_bonus": "$100-$1000, subject to VIP review and the active birthday offer",
        "lossback_bonus": "Personalized lossback offer based on eligible activity",
        "reload_bonus": "Personalized reload offers based on eligible activity",
        "svip_benefits": "Potential access to a dedicated VIP host, personalized bonuses and selected exclusive experiences"
       },
       "rakeback": {
        "calculation": "Eligible wager x applicable game house edge x 15%",
        "claim_frequency": "Accumulates during eligible gameplay; claim availability depends on the active rakeback feature.",
        "wagering_requirement": "No additional wagering requirement for rakeback credited as withdrawable cash."
       },
       "recharge_bonus": {
        "modeled_rate": "15%-20% of the qualifying recharge calculation",
        "calculation_basis": "Eligible wagering activity during the previous 7 days",
        "claim_frequency": "According to the active recharge schedule or a personalized offer",
        "wagering_requirement": "3x bonus amount",
        "maximum_bet_during_wagering": "$50",
        "validity": "7 days after activation"
       },
       "cashback_conditions": {
        "calculation_basis": "Net eligible losses during the relevant weekly or monthly period",
        "minimum_eligible_net_loss": "$100",
        "weekly_claim_deadline": "7 days after crediting",
        "monthly_claim_deadline": "30 days after crediting",
        "wagering_requirement": "1x cashback amount if credited as bonus funds; none if credited as withdrawable cash"
       },
       "birthday_bonus_conditions": {
        "frequency": "Once per calendar year",
        "claim_period": "30 days from the birthday offer notification",
        "wagering_requirement": "5x bonus amount unless the personalized offer states otherwise",
        "verification": "Account verification may be required"
       },
       "vip_host_services": [
        "Personalized one-to-one account assistance",
        "Help with VIP promotions and reward enquiries",
        "Assistance with eligible account and payment questions",
        "Information about personalized events and exclusive offers"
       ],
       "additional_benefits": [
        "Highest modeled rakeback rate among the five tiers",
        "Highest modeled cashback caps and level-up rewards",
        "Access to personalized birthday, reload and lossback offers",
        "Potential invitation to additional SVIP benefits",
        "Eligibility for exclusive events or experiences when offered"
       ],
       "eligibility_and_restrictions": [
        "Diamond status does not automatically guarantee SVIP membership.",
        "Personalized rewards may require an invitation or approval.",
        "Birthday, reload and lossback rewards depend on the terms of the individual offer.",
        "High-value promotional rewards may require additional identity or source-of-funds verification."
       ]
      }
     ],
     "general_terms": [
      "The five-tier XP thresholds and the specific monetary rewards, cashback rates, bonus caps and wagering requirements in this knowledge base are modeled values rather than verified current BC.GAME rules.",
      "Published BC.GAME materials describe VIP levels, level-up bonuses, rakeback, recharge, cashback and personalized VIP services, but benefits and eligibility may change.",
      "Rakeback is calculated from eligible wagering activity and the applicable game house edge; it is not a percentage of the entire wager returned directly.",
      "Cashback is calculated on eligible net losses during the relevant period and is subject to the applicable cap.",
      "Bonus-funded rewards may require wagering before withdrawal; the terms of the specific offer determine the applicable multiplier.",
      "Only one account per person is permitted. Multi-accounting, bonus abuse, collusion and manipulation of wagering or rewards may result in forfeiture or account restrictions.",
      "The operator may request identity verification and payment ownership evidence before releasing rewards or processing withdrawals."
     ]
    }
   },
   "brandinfo_account": {
    "brandinfo_account": {
     "registration": {
      "eligibility": "Players must be at least 18 or meet the higher legal gambling age applicable in their jurisdiction.",
      "procedure": [
       "Open the BC.Game website or PWA.",
       "Choose a registration option and submit the requested account information.",
       "Complete any confirmation or verification steps presented by the platform."
      ],
      "restrictions": "The company may refuse an application where accepting it would breach applicable law or other stated eligibility requirements.",
      "steps": [
       "Open the BC.GAME website or mobile PWA.",
       "Choose a registration method and provide the requested account details.",
       "Enter a referral or promo code if applicable.",
       "Confirm the email address or other contact method if prompted.",
       "Accept the Terms of Service and applicable account policies."
      ]
     },
     "login": {
      "account_access": "Sign in through the website or PWA using the account credentials provided at registration.",
      "security": "The operator may monitor login attempts and other security-related information; account access may be temporarily restricted during security checks.",
      "password_recovery": "Use the password-recovery option on the login page and follow the verification instructions sent to the registered contact method."
     },
     "verification": {
      "timing": "Verification may take place before, during or after registration, before deposits or withdrawals, or whenever reasonably necessary for legal compliance or account security.",
      "possible_checks": [
       "Identity",
       "Ownership of the receiving payment method",
       "Anti-money-laundering compliance",
       "Source of funds where required",
       "Cryptocurrency wallet ownership where appropriate"
      ],
      "additional_review": "Risk-based checks may consider payment method, cryptocurrency risk profile, deposit and withdrawal patterns, and other transaction indicators. Supporting documentation may be requested where reasonably necessary.",
      "documents_may_include": [
       "Passport",
       "National identity card",
       "Driver's licence",
       "Recent utility bill or other proof of address",
       "Selfie or liveness check",
       "Payment-method ownership evidence",
       "Verification call where required"
      ],
      "deposit_wagering_before_withdrawal": "The deposited amount must be wagered at least 1x before a withdrawal request for AML compliance."
     },
     "restrictions": {
      "vpn_policy": "VPNs, proxies and similar tools used to mask or manipulate the player's real location are prohibited.",
      "restricted_jurisdictions": [
       "Australia",
       "Austria",
       "France and its territories",
       "Germany",
       "Netherlands and its territories",
       "United Kingdom",
       "United States and its territories",
       "Union of the Comoros",
       "FATF-blacklisted jurisdictions",
       "Other jurisdictions prohibited by the Anjouan regulator or applicable law"
      ],
      "age": "18+ or the higher legal gambling age in the player's jurisdiction"
     }
    }
   },
   "brandinfo_responsible_gaming": {
    "brandinfo_responsible_gaming": {
     "responsible_gaming": {
      "minimum_age": "18+, or the higher legal age applicable in the player's jurisdiction",
      "limit_tools": {
       "deposit_limits": [
        "Daily deposit limits",
        "Weekly deposit limits",
        "Monthly deposit limits"
       ],
       "wagering_limits": "Players can cap the amount wagered daily, weekly, monthly or quarterly.",
       "loss_limits": "Players can cap losses daily, weekly, monthly or quarterly.",
       "limit_changes": "Removing a limit takes effect at 00:00 UTC after a cooling-off period of at least 24 hours. Active limits reset at 00:00 UTC at the end of each period."
      },
      "cooling_off": {
       "duration": "24 hours",
       "scope": "Casino and sports betting",
       "conditions": "The player can still access the platform and earn or claim rewards. Changing the type of cooldown during the period resets the 24-hour timer."
      },
      "self_exclusion": {
       "procedure": "Self-exclusion can be initiated through the platform by establishing a limit, or requested through Customer Support.",
       "periods": [
        "1 day",
        "1 week",
        "1 month",
        "6 months",
        "Permanent"
       ],
       "sequence": "After a 24-hour cooldown ends, the player has 24 hours to extend self-exclusion by selecting an available period.",
       "effects": [
        "Access to products and wagering functions is restricted.",
        "During platform self-exclusion, the player may still log in to withdraw assets.",
        "The supplied responsible-gambling page also states that self-exclusion locks the account for at least 6 months and promotional material will not be sent."
       ],
       "reversibility": "The automated self-exclusion flow describes self-exclusion as strictly irreversible.",
       "minimum_long_term_period": "6 months for the long-term self-exclusion procedure"
      },
      "support_resources": [
       "Gamblers Anonymous",
       "Gambling Therapy",
       "GamCare",
       "National Council on Problem Gambling"
      ],
      "support_availability": "Customer Support is available 24/7",
      "guidance": [
       "Play for entertainment, not to make money.",
       "Avoid chasing losses.",
       "Set a budget and limits, take breaks, and do not gamble with money needed for other expenses.",
       "Use self-assessment guidance if gambling may be affecting work, relationships, finances or wellbeing."
      ],
      "underage_policy": "Underage gambling is prohibited. Accounts may be closed and winnings forfeited if underage use is identified.",
      "practical_guidance": [
       "Set a gambling budget and do not use money needed for essential expenses.",
       "Do not chase losses or treat gambling as a way to make money.",
       "Take breaks and use deposit, wagering and loss limits.",
       "Seek support if gambling affects finances, work, relationships or wellbeing."
      ],
      "limit_periods": [
       "Daily",
       "Weekly",
       "Monthly",
       "Quarterly for wagering and loss limits"
      ]
     }
    }
   },
   "brandinfo_games": {
    "brandinfo_games": {
     "game_types": [
      "Slots",
      "Live casino",
      "Table games",
      "Blackjack",
      "Roulette",
      "Baccarat",
      "Crash games",
      "Mines",
      "Dice",
      "Wheel",
      "Limbo",
      "Plinko",
      "Tower games",
      "Poker",
      "Lottery",
      "Racing",
      "UpDown",
      "Bingo",
      "Sports betting",
      "Predictions",
      "Virtual sports",
      "Esports",
      "BC Originals",
      "Crypto Futures",
      "Game Shows",
      "Keno",
      "Video Poker",
      "Virtual Sports"
     ],
     "game_examples": [
      "Sugar Rush 1000",
      "Fruit Party",
      "Gates of Olympus 2500",
      "Sweet Bonanza 1000",
      "Crazy Ex-Girlfriend",
      "Keno",
      "Crash",
      "Mines",
      "Classic Dice",
      "Wheel",
      "Limbo",
      "Plinko",
      "Tower Legend",
      "Fortune Gems",
      "Treasures of Aztec",
      "Wild Bandito",
      "Blackjack",
      "Baccarat",
      "Roulette",
      "Game Shows",
      "Dragon Tiger",
      "Lightning Roulette",
      "Speed Baccarat A",
      "Auto-Roulette",
      "Wukong",
      "Ne Zha",
      "Ganesha Golden Wheel",
      "Gold of Olympus",
      "Chop Chop",
      "BC.GAME Sweet Rush Bonanza",
      "BC.GAME Gates of Olympus Super Scatter",
      "Wild Bounty Showdown",
      "Crazy Time",
      "Army of Ares",
      "Cleocatra",
      "3 Cursed Chests: Hold & Win",
      "Madame Destiny Megaways",
      "BC.GAME XXXtreme Lightning Roulette",
      "BC.GAME Baccarat",
      "BC.GAME Sugar Rush",
      "BCGAME Deadwood R.I.P",
      "BCGAME Bronze Blackjack",
      "BC.GAME Speed Baccarat",
      "BC.GAME Big Bass Splash",
      "Duck Hunters",
      "Bonsai Gold 2: Age of Prosperity",
      "Jelly Express",
      "Lucky Neko",
      "Dead Man's Gold: Hold & Win",
      "Fire In The Hole xBomb DX8",
      "Bingo Carnaval",
      "Wild Bingo",
      "Jackpot Bingo",
      "iRich Bingo",
      "Bonus Bingo",
      "Magic Lamp Bingo",
      "Immortal Romance Video Bingo"
     ],
     "original_games": [
      "Crash",
      "Mines",
      "Classic Dice",
      "Wheel",
      "Limbo",
      "Plinko",
      "Tower Legend",
      "Bingo"
     ],
     "providers": [
      "Pragmatic Play",
      "Evolution Gaming",
      "JILI",
      "PG Soft",
      "FA CHAI",
      "Hacksaw",
      "Nolimit City",
      "Croco Gaming",
      "Evolution",
      "Ezugi"
     ],
     "additional_categories": [
      "Crypto Futures",
      "Video Poker",
      "Keno",
      "Game Shows",
      "Virtual Sports"
     ]
    }
   },
   "brandinfo_sportsbook": {
    "brandinfo_sportsbook": {
     "sportsbook": {
      "availability": true,
      "sports": [
       "Football",
       "Cricket",
       "NFL",
       "Esports",
       "Basketball",
       "More than 80 sports",
       "Virtual sports"
      ],
      "betting_modes": [
       "Pre-match betting",
       "In-play/live betting"
      ],
      "markets": [
       "1X2 match result",
       "Draw",
       "Winner including overtime (basketball)"
      ],
      "displayed_competitions": [
       "UEFA Champions League",
       "NBA",
       "Saudi Pro League"
      ],
      "features": [
       "Early Payout promotion is advertised"
      ],
      "odds_note": "Displayed odds are for information and guidance; the site states that it does not assume liability if particular information is incorrect.",
      "platform_features": [
       "Single wallet shared by casino and sportsbook",
       "Pre-match and live betting",
       "Sports betting insights"
      ],
      "market_examples": [
       "1X2 match result",
       "Draw",
       "Winner including overtime (basketball)",
       "Match winner",
       "Outright markets",
       "Tournament-related specials"
      ],
      "promotional_events": [
       {
        "name": "Top 5 Leagues Combo Boost",
        "offer": "Up to 35% back",
        "advertised_prize_pool": "$500,000 shared promotion",
        "displayed_end_date": "November 10, 2026"
       },
       {
        "name": "Early Payout",
        "description": "Early-payout feature for eligible bets",
        "displayed_end_date": "January 1, 2027"
       },
       {
        "name": "FIFA World Cup 2026 Hub",
        "advertised_prize_pool": "$2 million or more",
        "description": "Tournament hub with multiple sports promotions and prize campaigns"
       }
      ]
     }
    }
   },
   "brandinfo_deposit": {
    "brandinfo_deposit": {
     "deposit_methods": [
      {
       "method": "Cryptocurrency",
       "minimum": "€10 equivalent",
       "maximum": "€5,000 equivalent",
       "fee": "0.1%",
       "transaction_speed": "Generally credited after confirmation by the relevant payment provider or blockchain network; delays may occur due to network congestion",
       "currencies": [
        "BTC",
        "ETH",
        "BNB",
        "XRP",
        "USDT",
        "USDC",
        "SOL",
        "ADA",
        "DOGE",
        "MATIC",
        "TRX"
       ],
       "important_terms": "Deposits must originate from a payment method lawfully owned or controlled by the player. Applicable limits may vary by method, jurisdiction, currency, regulatory requirements and risk profile and are normally displayed before confirmation."
      },
      {
       "method": "PayDo",
       "minimum": "€10",
       "maximum": "€5,000",
       "fee": "0% casino deposit fee in most cases; provider, bank or currency-conversion charges may apply",
       "transaction_speed": "Generally credited after confirmation by the payment provider",
       "currencies": [
        "EUR"
       ],
       "important_terms": "Availability and limits may vary by jurisdiction and account."
      },
      {
       "method": "Skrill",
       "minimum": "€10",
       "maximum": "€5,000",
       "fee": "0% casino deposit fee in most cases; provider, bank or currency-conversion charges may apply",
       "transaction_speed": "Generally credited after confirmation by the payment provider",
       "currencies": [
        "EUR"
       ],
       "important_terms": "Availability and limits may vary by jurisdiction and account."
      },
      {
       "method": "Tink",
       "minimum": "€10",
       "maximum": "€5,000",
       "fee": "0% casino deposit fee in most cases; provider, bank or currency-conversion charges may apply",
       "transaction_speed": "Generally credited after confirmation by the payment provider",
       "currencies": [
        "EUR"
       ],
       "important_terms": "Availability and limits may vary by jurisdiction and account."
      },
      {
       "method": "Neteller",
       "minimum": "€10",
       "maximum": "€5,000",
       "fee": "0% casino deposit fee in most cases; provider, bank or currency-conversion charges may apply",
       "transaction_speed": "Generally credited after confirmation by the payment provider",
       "currencies": [
        "EUR"
       ],
       "important_terms": "Availability and limits may vary by jurisdiction and account."
      },
      {
       "method": "Visa",
       "type": "Card payment",
       "minimum": "€10 equivalent or amount displayed at checkout",
       "maximum": "€5,000 equivalent or amount displayed at checkout",
       "fee": "0% casino deposit fee in most cases; bank, provider or currency-conversion charges may apply",
       "transaction_speed": "Credited after the card issuer approves and authorizes the payment.",
       "currencies": [
        "EUR",
        "USD",
        "INR"
       ],
       "important_terms": "Available where supported by the account's country, currency and payment provider."
      },
      {
       "method": "Mastercard",
       "type": "Card payment",
       "minimum": "€10 equivalent or amount displayed at checkout",
       "maximum": "€5,000 equivalent or amount displayed at checkout",
       "fee": "0% casino deposit fee in most cases; bank, provider or currency-conversion charges may apply",
       "transaction_speed": "Credited after the card issuer approves and authorizes the payment.",
       "currencies": [
        "EUR",
        "USD",
        "INR"
       ],
       "important_terms": "Available where supported by the account's country, currency and payment provider."
      },
      {
       "method": "Apple Pay",
       "type": "Digital wallet",
       "minimum": "€10 equivalent or amount displayed at checkout",
       "maximum": "€5,000 equivalent or amount displayed at checkout",
       "fee": "0% casino deposit fee in most cases; bank, provider or currency-conversion charges may apply",
       "transaction_speed": "Processed after wallet and payment-provider authorization.",
       "currencies": [
        "EUR",
        "USD"
       ],
       "important_terms": "Available where supported by the account's country, currency and payment provider."
      },
      {
       "method": "Google Pay",
       "type": "Digital wallet",
       "minimum": "€10 equivalent or amount displayed at checkout",
       "maximum": "€5,000 equivalent or amount displayed at checkout",
       "fee": "0% casino deposit fee in most cases; bank, provider or currency-conversion charges may apply",
       "transaction_speed": "Processed after wallet and payment-provider authorization.",
       "currencies": [
        "EUR",
        "USD",
        "INR"
       ],
       "important_terms": "Available where supported by the account's country, currency and payment provider."
      },
      {
       "method": "PicPay",
       "type": "Digital wallet",
       "minimum": "€10 equivalent or amount displayed at checkout",
       "maximum": "€5,000 equivalent or amount displayed at checkout",
       "fee": "0% casino deposit fee in most cases; bank, provider or currency-conversion charges may apply",
       "transaction_speed": "Processed after payment-provider authorization.",
       "currencies": [
        "BRL"
       ],
       "important_terms": "Available where supported by the account's country, currency and payment provider."
      }
     ],
     "deposit_guide": [
      "Sign in and open Avatar/Profile > Wallet > Deposit.",
      "Choose Crypto or Fiat and select an available currency and payment method.",
      "Enter the amount and review the displayed limits and fee.",
      "For cryptocurrency, select the exact asset and network shown on the deposit page, then send funds to the displayed address.",
      "For fiat payments, follow the payment-provider window or instructions and complete the payment within the allotted time.",
      "Enter a promo code if the selected offer requires one.",
      "Check transaction status in the wallet or Transactions section."
     ],
     "payment_terms": [
      "Deposits should come from a bank account, payment service or card held in the player's own name.",
      "BC.GAME absorbs deposit transaction fees in most cases; cryptocurrency deposits are subject to the 0.1% fee stated in the Terms.",
      "The player's bank or payment provider may charge separate fees, including currency-conversion charges.",
      "Deposits in another currency may be converted using the daily exchange rate or the rate applied by the bank/payment processor.",
      "Third-party electronic payment processors may be used.",
      "Deposit limits and available methods vary by jurisdiction, currency and payment provider and are shown in the account."
     ]
    }
   },
   "brandinfo_withdrawal": {
    "brandinfo_withdrawal": {
     "withdrawal_methods": [
      {
       "method": "Cryptocurrency",
       "minimum": "€20 equivalent",
       "maximum": "€5,000 equivalent",
       "fee": "0.1%",
       "transaction_speed": "Depends on platform processing and blockchain confirmation; network congestion can delay receipt",
       "currencies": [
        "BTC",
        "ETH",
        "BNB",
        "XRP",
        "USDT",
        "USDC",
        "SOL",
        "ADA",
        "DOGE",
        "MATIC",
        "TRX",
        "PYUSD"
       ],
       "important_terms": "Use the exact asset and network supported by the withdrawal page. KYC and AML checks may be required."
      },
      {
       "method": "Original fiat payment method",
       "minimum": "€20 equivalent",
       "maximum": "€5,000 equivalent",
       "fee": "Any fee shown before confirmation; bank or provider charges may apply",
       "transaction_speed": "Depends on payment provider, bank and compliance checks",
       "currencies": [
        "EUR",
        "USD",
        "INR",
        "IDR",
        "NGN"
       ],
       "important_terms": "Withdrawals generally return to the original deposit method where reasonably practicable."
      },
      {
       "method": "PayDo",
       "minimum": "€20 equivalent",
       "maximum": "€5,000 equivalent",
       "fee": "Any fee shown before confirmation; provider charges may apply",
       "transaction_speed": "Depends on payment provider and compliance checks",
       "currencies": [
        "EUR",
        "USD"
       ],
       "important_terms": "Available where supported by the account; original-method withdrawal rules apply."
      },
      {
       "method": "Skrill",
       "minimum": "€20 equivalent",
       "maximum": "€5,000 equivalent",
       "fee": "Any fee shown before confirmation; provider charges may apply",
       "transaction_speed": "Depends on payment provider and compliance checks",
       "currencies": [
        "EUR",
        "USD"
       ],
       "important_terms": "Available where supported by the account; original-method withdrawal rules apply."
      },
      {
       "method": "Neteller",
       "minimum": "€20 equivalent",
       "maximum": "€5,000 equivalent",
       "fee": "Any fee shown before confirmation; provider charges may apply",
       "transaction_speed": "Depends on payment provider and compliance checks",
       "currencies": [
        "EUR",
        "USD"
       ],
       "important_terms": "Available where supported by the account; original-method withdrawal rules apply."
      }
     ],
     "withdrawal_guide": [
      "Sign in and open Avatar/Profile > Wallet > Withdraw.",
      "Complete the 1x deposit-wagering requirement and any outstanding verification steps.",
      "Choose an available withdrawal method, normally the original deposit method where supported.",
      "Enter the amount, check the minimum, maximum and displayed fee, and provide destination details.",
      "Review and submit the request.",
      "Complete any additional KYC or transaction review requested by the operator.",
      "Track the request in transaction history until processed."
     ],
     "withdrawal_limits": {
      "minimum_per_transaction": "€20 or equivalent in the selected currency",
      "maximum_per_transaction": "€5,000 or the limit displayed for the selected method",
      "account_closure": "The remaining balance may be withdrawn when an account is closed, subject to verification and legal requirements."
     },
     "withdrawal_conditions": [
      "The deposited amount must be wagered at least 1x before a withdrawal request for AML compliance.",
      "Withdrawals generally return to the original payment method where reasonably practicable.",
      "The operator may request identity, address, selfie, payment ownership, source-of-funds or verification-call evidence.",
      "Withdrawals are subject to anti-fraud, AML, applicable-law and promotion checks.",
      "Processing time depends on the payment provider, bank, blockchain network and compliance review."
     ]
    }
   },
   "brandinfo_app": {
    "brandinfo_app": {
     "app_information": {
      "type": "Progressive Web App (PWA)",
      "availability": "Mobile-ready website with PWA access",
      "advertised_feature": "Exclusive app rewards are promoted",
      "supported_access": "The responsive mobile website and PWA provide mobile access to casino and sportsbook features.",
      "pwa_app": true,
      "mobile_site": true,
      "native_apps": "Mobile access is provided through the responsive website and Progressive Web App (PWA).",
      "features": [
       "Mobile-ready casino and sportsbook access",
       "One wallet across casino and sportsbook",
       "Access to casino, sports, lottery, crypto futures and promotions",
       "VIP Club and referral section",
       "Forum and blog",
       "Provably fair information",
       "Responsible gambling tools",
       "Sports betting insights",
       "Exclusive PWA features and rewards"
      ]
     }
    }
   },
   "brandinfo_privacy_policy": {
    "brandinfo_privacy_policy": {
     "data_controller": {
      "company_name": "Twocent Technology Limited",
      "registered_address": "Sea Urchin Street #2, San Pedro, Ambergris Caye, Belize",
      "jurisdiction": "Belize; licensed in Anjouan, Union of the Comoros",
      "company_registration_number": "41939",
      "privacy_contact": "Privacy-related requests can be submitted to Customer Support through the website."
     },
     "data_collected": {
      "account_data": [
       "BC.GAME ID",
       "Email address",
       "Username",
       "Age",
       "Account status"
      ],
      "contact_data": [
       "Full name",
       "Email address",
       "Phone number",
       "Physical address"
      ],
      "technical_data": [
       "IP address",
       "Device ID",
       "Operating system",
       "Browser type"
      ],
      "financial_data": [
       "Payment methods",
       "Transaction history",
       "Deposit and withdrawal records"
      ],
      "location_data": [
       "Approximate or precise geolocation"
      ],
      "verification_data": [
       "Government-issued identity data where required for KYC"
      ],
      "gaming_activity": [
       "Platform interactions",
       "Gameplay history",
       "Browsing activities"
      ],
      "fraud_prevention_data": [
       "Device trust scores",
       "Suspicious activity monitoring",
       "Transaction analysis"
      ],
      "marketing_data": [
       "Communication preferences for promotional offers and campaigns"
      ],
      "sensitive_data": "Sensitive personal data is not collected or processed unless legally required and with explicit consent."
     },
     "data_collection_methods": [
      "Account registration and use",
      "Identity verification and KYC where required",
      "Deposits and withdrawals",
      "Casino and sportsbook activity",
      "Platform browsing and interactions",
      "Promotional participation and communication preferences",
      "Security and fraud-prevention monitoring"
     ],
     "data_usage": {
      "service_delivery": "Providing and maintaining services",
      "identity_verification": "Verifying identity and ensuring security",
      "payment_processing": "Processing payments and transactions",
      "service_improvement": "Enhancing user experience and improving services",
      "fraud_prevention": "Preventing fraud and illegal activities",
      "regulatory_compliance": "Meeting regulatory, tax and anti-money-laundering obligations",
      "marketing": "Conducting marketing and promotional activities",
      "personalization": "Personalizing advertising and user recommendations",
      "customer_support": "Responding to support inquiries",
      "policy_enforcement": "Enforcing Terms of Service and applicable policies",
      "vip_promotions": "Processing applications for VIP programmes, promotions or rewards",
      "additional_purposes": [
       "Account and transaction security",
       "Enforcement of Terms of Service and promotion rules",
       "Processing VIP, referral and promotional participation",
       "Monitoring suspicious payment activity"
      ]
     },
     "legal_basis": {
      "contractual_necessity": "Providing services agreed when a user creates an account and uses BC.Game",
      "legitimate_interests": "User experience improvements, security, fraud prevention and service improvement",
      "consent": "Certain processing activities where consent is required by law",
      "legal_obligation": "Regulatory, tax and anti-money-laundering obligations",
      "applicable_regulations": [
       "GDPR",
       "California Consumer Privacy Act (CCPA)",
       "Other relevant privacy regulations"
      ]
     },
     "third_party_sharing": {
      "recipients": [
       "Payment providers",
       "Identity-verification providers",
       "Service providers",
       "Regulatory and law-enforcement authorities where required"
      ],
      "sharing_purposes": [
       "Payment processing",
       "Identity and compliance verification",
       "Fraud prevention",
       "Legal and regulatory compliance"
      ],
      "sharing_conditions": "Information necessary for verification may be securely shared with verification providers in accordance with applicable law and the Privacy Policy."
     },
     "international_transfers": {
      "transfer_destinations": "Personal data may be transferred outside the user's country of residence, including to countries with different levels of data protection.",
      "safeguards": [
       "Standard Contractual Clauses (SCCs)",
       "Data Processing Agreements (DPAs)"
      ]
     },
     "data_retention": {
      "general_retention": "Data is retained as long as necessary for stated purposes, legal requirements, dispute resolution and enforcement of agreements.",
      "account_data_retention": "As long as the account remains active",
      "financial_records_retention": "Up to 7 years where required for financial, tax, AML or regulatory records",
      "marketing_data_retention": "Until the user opts out",
      "fraud_prevention_data_retention": "Up to 5 years where needed for security, fraud prevention or legal compliance",
      "deletion_conditions": "After applicable retention periods, data will be deleted or anonymized unless further retention is legally required."
     },
     "data_security": {
      "security_monitoring": "The site states that it has 24/7 fraud monitoring and refers to ISO 27001 and SOC 2 certification.",
      "other_measures": [
       "Provably fair systems and audited RNG are described for gaming integrity",
       "Risk-based fraud and transaction monitoring"
      ],
      "additional_measures": [
       "24/7 fraud monitoring",
       "Risk-based transaction and account monitoring",
       "Provably fair systems and audited random number generation for game integrity"
      ]
     },
     "user_rights": {
      "right_of_access": "Request a copy of personal data",
      "right_to_rectification": "Correct inaccurate or incomplete data",
      "right_to_erasure": "Request deletion where legally applicable",
      "right_to_restriction": "Request limited processing under certain conditions",
      "right_to_object": "Object to marketing and certain processing activities",
      "right_to_portability": "Receive data in a structured format for transfer to another provider",
      "complaint_rights": "Lodge a complaint with a data protection authority if rights are believed to have been violated"
     },
     "privacy_requests": {
      "submission_methods": "The supplied policy text does not specify a dedicated submission procedure or response deadline.",
      "identity_confirmation": "Identity may need to be verified where required for compliance or account security."
     },
     "cookies_policy": {
      "cookie_policy_reference": "The website provides a separate Cookie Policy. Cookies and similar technologies support account sessions, site functionality and user preferences; manage cookie settings through the site's available controls."
     },
     "marketing_communications": {
      "marketing_preferences": "Marketing preferences are collected; marketing data is retained until the user opts out.",
      "marketing_opt_out": "Users can opt out of promotional communications through account preferences or Customer Support."
     },
     "automated_decision_making": {
      "profiling_activities": "Personalized advertising and user recommendations are described; the supplied policy does not detail decisions producing legal or similarly significant effects."
     },
     "minors_privacy": {
      "age_restrictions": "The platform is restricted to players aged 18 or older, or the higher legal age applicable in their jurisdiction."
     }
    }
   }
  }
 },
 "competitor_h1": [
  "BC Game великий огляд онлайн казино",
  "Онлайн-гемблинг и его регулирование в"
 ],
 "competitor_stats": [
  {
   "url": "https://cardmates.ua/bc_game",
   "body_words": 1574,
   "keywords_in_total": {
    "BC Game": 16,
    "BCGame": 3,
    "BC Games": 0,
    "BC Game казино": 2
   },
   "keywords_in_h1": {
    "BC Game": 1,
    "BCGame": 0,
    "BC Games": 0,
    "BC Game казино": 0
   },
   "keywords_in_h2": {
    "BC Game": 4,
    "BCGame": 1,
    "BC Games": 0,
    "BC Game казино": 0
   }
  },
  {
   "url": "https://www.bitcoin.com/ru/gambling/reviews/bc-game/",
   "body_words": 222,
   "keywords_in_total": {
    "BC Game": 0,
    "BCGame": 0,
    "BC Games": 0,
    "BC Game казино": 0
   },
   "keywords_in_h1": {
    "BC Game": 0,
    "BCGame": 0,
    "BC Games": 0,
    "BC Game казино": 0
   },
   "keywords_in_h2": {
    "BC Game": 0,
    "BCGame": 0,
    "BC Games": 0,
    "BC Game казино": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 898,
  "keyword_targets": {
   "BC Game": 8,
   "BCGame": 2,
   "BC Games": 1,
   "BC Game казино": 1
  }
 },
 "heading_clusters": [
  {
   "id": "k01",
   "canonical_title": "Огляд казино",
   "topic": "Casino overview / official site",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 99,
   "avg_position": 0.1,
   "examples": [
    "BC Game офіційний сайт",
    "Эволюция игровых технологий на основе блокчейна"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Легальність і обмеження",
   "topic": "Legality, regulation and restricted countries",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 34,
   "avg_position": 0.52,
   "examples": [
    "Заборонені країни",
    "💎 Казино БС Гейм легальне?",
    "Навигация по глобальным нормативам"
   ]
  },
  {
   "id": "k02",
   "canonical_title": "Реєстрація",
   "topic": "Registration",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 23,
   "avg_position": 0.1,
   "examples": [
    "Реєстрація на BC Game"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Ігри казино",
   "topic": "Games overview",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 192,
   "avg_position": 0.19,
   "examples": [
    "Найкращі ігри казино BCGame"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Ігрові автомати",
   "topic": "Slots",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 57,
   "avg_position": 0.24,
   "examples": [
    "Ігрові автомати"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Лайв казино",
   "topic": "Live casino",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 35,
   "avg_position": 0.29,
   "examples": [
    "Лайв казино"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Ставки на спорт",
   "topic": "Sports betting",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 79,
   "avg_position": 0.33,
   "examples": [
    "Ставки на спорт"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Лотерея",
   "topic": "Lottery",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 34,
   "avg_position": 0.38,
   "examples": [
    "Лотерея"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Платіжні системи",
   "topic": "Payment methods and deposits",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 161,
   "avg_position": 0.43,
   "examples": [
    "Платіжні системи"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "Відповідальна гра",
   "topic": "Responsible gambling",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 44,
   "avg_position": 0.43,
   "examples": [
    "Играйте ответственно"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Виведення коштів",
   "topic": "Withdrawals",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 95,
   "avg_position": 0.48,
   "examples": [
    "Виведення коштів"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "Мобільний додаток",
   "topic": "Mobile app / mobile play",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 58,
   "avg_position": 0.52,
   "examples": [
    "Як скачати BC Game на мобільний",
    "📲 Де скачати BC Game для смартфона?"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "Бонуси та акції",
   "topic": "Bonuses and promotions",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 25,
   "avg_position": 0.57,
   "examples": [
    "Бонуси та промо-акції"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Служба підтримки",
   "topic": "Customer support",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 76,
   "avg_position": 0.62,
   "examples": [
    "Сапорт"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Висновок",
   "topic": "Verdict / conclusion",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 86,
   "avg_position": 0.67,
   "examples": [
    "Вердикт"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Поширені запитання",
   "topic": "FAQ: ownership, age and general questions",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 6,
   "avg_position": 0.79,
   "examples": [
    "Поширені запитання",
    "📢 Кому належить BC Game?",
    "👨 З якого віку можна реєструватись у казино BCGame?"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Екосистема та спільнота",
   "topic": "Crypto ecosystem and community",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 12,
   "avg_position": 0.79,
   "examples": [
    "Исследуйте экосистему",
    "Будьте в курсе событий",
    "Присоединяйтесь к сообществу",
    "Станьте владельцем криптовалюты"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "Схожі казино",
   "topic": "Similar casinos",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 0,
   "avg_position": 0.95,
   "examples": [
    "Схожі казино"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Відгуки гравців",
   "topic": "User reviews",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 145,
   "avg_position": 1.0,
   "examples": [
    "BC Game відгуки"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "VPN",
   "competitors": 2
  },
  {
   "entity": "Bitcoin",
   "competitors": 1
  },
  {
   "entity": "RTP",
   "competitors": 1
  },
  {
   "entity": "ETH",
   "competitors": 1
  },
  {
   "entity": "USDT",
   "competitors": 1
  },
  {
   "entity": "DOGE",
   "competitors": 1
  },
  {
   "entity": "BlockDance B",
   "competitors": 1
  },
  {
   "entity": "NFT",
   "competitors": 1
  },
  {
   "entity": "Android",
   "competitors": 1
  },
  {
   "entity": "BCL",
   "competitors": 1
  },
  {
   "entity": "Apple Pay",
   "competitors": 1
  },
  {
   "entity": "Crypto Gambling Foundation",
   "competitors": 1
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 1
  },
  {
   "entity": "Evolution Gaming",
   "competitors": 1
  },
  {
   "entity": "Evoplay",
   "competitors": 1
  },
  {
   "entity": "Mac OS",
   "competitors": 1
  },
  {
   "entity": "Windows",
   "competitors": 1
  },
  {
   "entity": "Game Affiliates",
   "competitors": 1
  },
  {
   "entity": "Gaming",
   "competitors": 1
  },
  {
   "entity": "VIP-програму",
   "competitors": 1
  },
  {
   "entity": "Play Market",
   "competitors": 1
  },
  {
   "entity": "Apple Store",
   "competitors": 1
  },
  {
   "entity": "Buy-in",
   "competitors": 1
  },
  {
   "entity": "BC Originals",
   "competitors": 1
  },
  {
   "entity": "Cloud9",
   "competitors": 1
  },
  {
   "entity": "LTC",
   "competitors": 1
  },
  {
   "entity": "TRON",
   "competitors": 1
  },
  {
   "entity": "Tether",
   "competitors": 1
  },
  {
   "entity": "Banxa",
   "competitors": 1
  },
  {
   "entity": "MoonPay",
   "competitors": 1
  },
  {
   "entity": "Visa",
   "competitors": 1
  },
  {
   "entity": "Mastercard",
   "competitors": 1
  },
  {
   "entity": "Google Pay",
   "competitors": 1
  },
  {
   "entity": "GPay",
   "competitors": 1
  },
  {
   "entity": "Samsung Pay",
   "competitors": 1
  },
  {
   "entity": "BAYC",
   "competitors": 1
  },
  {
   "entity": "Degenpass",
   "competitors": 1
  },
  {
   "entity": "CryptoPunks",
   "competitors": 1
  },
  {
   "entity": "Doodles",
   "competitors": 1
  },
  {
   "entity": "FAQ",
   "competitors": 1
  },
  {
   "entity": "BCG",
   "competitors": 1
  },
  {
   "entity": "Provably Fair",
   "competitors": 1
  },
  {
   "entity": "News",
   "competitors": 1
  },
  {
   "entity": "Wallet",
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
    "url": "https://cardmates.ua/bc_game",
    "heading": "BC Game великий огляд онлайн казино",
    "rows": [
     [
      "ℹ️ Назва",
      "BC Game"
     ],
     [
      "🎂 Рік заснування",
      "2017"
     ],
     [
      "📝 Ліцензія",
      "Curacao, Crypto Gambling Foundation"
     ],
     [
      "🎲 Доступні ігри",
      "ігрові автомати, рулетка, блекджек, бакара, ігри з живими дилерами, ТБ-ігри, краш-ігри"
     ],
     [
      "∑ Кількість ігор",
      "понад 7 500"
     ],
     [
      "🔄 Виплата (RTP)",
      "98"
     ],
     [
      "⚙️ Провайдери",
      "Pragmatic Play, Evolution Gaming, Evoplay"
     ],
     [
      "📱 Сумісні пристрої",
      "Android, iOS, Mac OS, Windows"
     ],
     [
      "💳 Методи депозиту",
      "BTC, B.C.D., ETH, X.R.P., USDT, DOGE, T.R.X., L.T.C., та 40+ інших"
     ],
     [
      "🚀 Швидкість виведення",
      "залежіть від обраного блокчейну"
     ],
     [
      "🚧 Ліміт на виведення",
      "відсутній"
     ],
     [
      "💲 Валюта",
      "криптовалюти"
     ],
     [
      "🌎 Мови",
      "англійська, німецька, французька, іспанська, португальська, в'єтнамська, індонезійська, філіппінська, японська, корейськ"
     ],
     [
      "💬 Онлайн-чат",
      "доступний 24/7"
     ],
     [
      "😎 Власник",
      "BlockDance B.V."
     ],
     [
      "🤝 Партнерська програма",
      "BC.Game Affiliates"
     ]
    ]
   },
   {
    "competitor": 1,
    "url": "https://cardmates.ua/bc_game",
    "heading": "Виведення коштів",
    "rows": [
     [
      "BTC",
      "0.000915"
     ],
     [
      "ETH",
      "0.014"
     ],
     [
      "UDST",
      "11"
     ],
     [
      "XRP",
      "22.25"
     ],
     [
      "DOGE",
      "100"
     ]
    ]
   }
  ],
  "labels": [
   {
    "label": "btc",
    "competitors": 1
   },
   {
    "label": "doge",
    "competitors": 1
   },
   {
    "label": "eth",
    "competitors": 1
   },
   {
    "label": "udst",
    "competitors": 1
   },
   {
    "label": "xrp",
    "competitors": 1
   },
   {
    "label": "ℹ️ назва",
    "competitors": 1
   },
   {
    "label": "∑ кількість ігор",
    "competitors": 1
   },
   {
    "label": "⚙️ провайдери",
    "competitors": 1
   },
   {
    "label": "🌎 мови",
    "competitors": 1
   },
   {
    "label": "🎂 рік заснування",
    "competitors": 1
   },
   {
    "label": "🎲 доступні ігри",
    "competitors": 1
   },
   {
    "label": "💬 онлайн-чат",
    "competitors": 1
   },
   {
    "label": "💲 валюта",
    "competitors": 1
   },
   {
    "label": "💳 методи депозиту",
    "competitors": 1
   },
   {
    "label": "📝 ліцензія",
    "competitors": 1
   },
   {
    "label": "📱 сумісні пристрої",
    "competitors": 1
   },
   {
    "label": "🔄 виплата (rtp)",
    "competitors": 1
   },
   {
    "label": "😎 власник",
    "competitors": 1
   },
   {
    "label": "🚀 швидкість виведення",
    "competitors": 1
   },
   {
    "label": "🚧 ліміт на виведення",
    "competitors": 1
   },
   {
    "label": "🤝 партнерська програма",
    "competitors": 1
   }
  ]
 }
}
