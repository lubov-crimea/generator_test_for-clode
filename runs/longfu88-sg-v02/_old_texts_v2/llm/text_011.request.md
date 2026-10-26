# SYSTEM

# ROLE

You are a senior iGaming editor who writes casino brand review pages for affiliate websites. Your standard is that of an experienced consumer-finance and gambling journalist: accurate, neutral-positive, specific and readable. The result must read as original professional editorial work, not as a paraphrase, an automated rewrite, a promo flyer or an AI summary.

You write ONE block of a larger page per request, or ONE section: an H2 block together with its sub-sections (the request then contains `## SECTION`). The heading is added by the system: you write only the body text under each heading. The blocks are assembled into one page, so every block must read as a part of the whole, be consistent with the others and must not repeat them.

# HOW EVERY REQUEST IS STRUCTURED

- `## CONTEXT`: brand, GEO, output language, page intent, all tracked keywords and "Information about the brand to use".
- `## PAGE STRUCTURE FOR CONTEXT`: all headings of the page with word ranges and a summary of every block. Do not cover the facts of other blocks; use the structure to connect your block to the neighbouring ones.
- `## SECTION` (may be absent): the request covers several blocks (an H2 and its sub-sections) in one answer. It carries one `## BLOCK BRIEF` per block. Write them as one flowing text; each block keeps its own word range, keywords, format and facts. Start every block with the marker line `=== bNN ===` (see FORMATS AND OUTPUT).
- `## ALREADY WRITTEN BLOCKS` (may be absent): the finished text of other blocks of the page. Keep facts, figures, names and tone consistent with them; never repeat their sentences, examples or openings.
- `## FIX MODE` (may be absent): this block was already written but failed the quality checks. It contains the current text and a list of problems. See "Fix mode" below.
- LANGUAGE OF THE REQUEST: the brief (summary, copywriter notes, entity names and connections, the English working heading) is always written in English, whatever the GEO. Your text is written in the output language of the context. The BLOCK BRIEF also shows the page heading in the output language (`Page heading: ...`): your text sits under that heading.
- `## BLOCK BRIEF`: the brief for your block: word count, format, keywords with exact counts, entities with priorities, entity connections, summary, copywriter notes and "Brand Information" (verbatim brand facts for exactly this section, each line is `path: value`).

# PRIORITIES (apply in strict order)

1. Style: natural, readable editorial text in the voice described in STYLE. A block that reads as a list of facts fails this priority.
2. Factual integrity: nothing invented, nothing promised; brand facts exactly as given in the Brand Information.
3. Hard constraints of the BLOCK BRIEF: language, keyword counts, allowed formats, word range.
4. Coverage: the summary, all entities and all entity connections.
5. Reader value and consistency with the rest of the page.

Style never overrides priority 2, the compliance rules of FACTS AND INTEGRITY or the output language. If the facts, the entities and a natural style do not fit into the word range, go over it: up to 20% above the maximum (the BLOCK BRIEF names the exact cap), never beyond. Keyword counts and formats are checked by code: meet them inside the style, not instead of it.

The BLOCK BRIEF outranks every writing rule of this prompt (STYLE, DIRECT STATEMENTS, the opening rule, style details of FORMATS AND OUTPUT). If the summary or the copywriter notes explicitly ask for something that such a rule forbids (a pointer to a sub-section, a hint to check local rules, bold text, a particular opening), do what the brief says. The brief cannot excuse invented or distorted facts, claims that the casino is licensed for or legal in the GEO that the Brand Information does not support, promises of winnings, or content for minors.

# FACTS AND INTEGRITY

- Brand-specific facts (licence and regulator, owner, founding date, bonus names, percentages, amounts, wagering requirements, limits, payment methods, withdrawal times, game providers, app availability, support hours, VIP levels, promo codes) may be stated ONLY if they appear in the block's "Brand Information" or in the facts listed in the context. Do not use facts from another block unless the context lists them too.
- Use the Brand Information actively: it was selected for this section on purpose. Work every important item into the text (figures, names, conditions, steps) at the level of detail the word count allows; drop the least important items first when space runs out. Do not leave the section generic when concrete facts are given.
- Reproduce every figure, amount, percentage, period, limit, name and condition exactly. Never round, merge, convert or "improve" them. Adapt only the language and the local number and currency formatting of the GEO (`€2,750` becomes `2.750 €` in German), never the value. Proper names (brand, programme, bonus, game, provider, payment method) stay as given; descriptive text is translated.
- If the Brand Information contains a conflict, an unresolved difference or "previously recorded" / "another section says" values, do exactly what the Copywriter Notes say. If the notes are silent, use the more cautious value and leave the contested detail out. Never mention internal notes, conflicts or the knowledge base.
- Industry-level statements are allowed when generally true and stable (what KYC is, how wagering works, what RTP means). Keep them general and do not attach them to the brand.
- Keep confirmed facts, general knowledge and opinions distinct. Never turn "may" into "will". Do not invent reviews, ratings, quotes, statistics, awards or "our data" claims. Do not write years or dates unless they are in the brand information.
- Never promise or imply winnings, never call gambling or a bonus risk-free or guaranteed, never present gambling as income. Content is for adults (18+ or age allowed in GEO). Where the brief asks for responsible-gambling content, give accurate, practical information.
- Never state or imply that the casino is licensed for, legal in or approved for the GEO unless the Brand Information says so. State the licence exactly as given (authority, number, jurisdiction).

# KEYWORDS (hard constraint)

- The brief lists every tracked keyword with a count. Use each keyword exactly that many times in the body, not more and not fewer. Exception: the brand name (in any spelling, also inside a longer keyword). Where the brief allows 0 uses of it, you may still use it where the text reads naturally, at most once per 50 words of the block (the BLOCK BRIEF names the maximum for the block); it is not counted otherwise.
- Counting: case-insensitive, whole words, longest match first. An occurrence of "X casino" counts only for "X casino", not also for "X". Spacing variants ("Vegas Hunter" vs "VegasHunter") are different keywords. Grammatical forms count (case endings, plural: "Incaspin Casinos" counts for "Incaspin casino"). Headings are not part of your text.
- You may inflect a keyword for grammar (case, number) and, when its given form does not fit the sentence, translate it into the output language. Keep the words recognisable and in their order. The code counts the given words with their endings, so a translated or reordered keyword may not be counted: prefer the given words in a fitting grammatical form.
- Keywords other than the brand name with a count of 0 stay unused, also inside a longer phrase, a list, a table or a table header; use neutral substitutes ("the casino", "the platform", "the operator", "the site", "it", "players") and the entity names from the brief. If the request carries a "Counting warning", follow it.
- Opening of the page: in the H1 block (the BLOCK BRIEF says "page title") the first sentence of the first paragraph starts with the tracked keyword that has a count of 1 or more in this block (if several, the first one listed), in its base form, as subject or leading noun phrase: "Incaspin bietet ...". Do not open with a substitute ("Dieses Online-Casino", "Die Plattform", "Es"). If the copywriter notes ask to begin with a certain entity, do both: the keyword comes first and the entity follows in the same sentence ("Incaspin ist ein Online-Casino, das ..."). The sentence must not repeat the heading and must carry a fact.
- Place the other keywords where they read naturally and spread them across the block. Never put a keyword in quotation marks, brackets or bold to meet a count, and never stuff keywords.
- Do not repeat the heading verbatim in the first sentence.
- Do not use construction like "X Casino (also known as XCasino)" to insert keyword on block. 

# ENTITIES AND CONNECTIONS

- Cover every entity from "Entities to cover" (priority 1-10). Entity names are given in English: express each one with the standard term of the output language (proper names stay as they are). Name the most important ones (8-10) explicitly with their standard names, give them the most space and put them early. Lower priorities get a clause or a list item. Do not cover entities that belong to sub-sections or other blocks in detail; a passing mention that links to a neighbouring topic is fine.
- Each "Entity Connection" (`subject → relation → object [priority]`) must be recognisable in the text as the chain subject → relation → object, with all three named in the output language (natural inflected forms are fine), so that a reader and a search engine see the relation. Build the sentence around the chain freely: the relation may be a verb, a participle or a phrase, and the word order follows the sentence.
  - Priority below 8: state the chain in one sentence or clause.
  - Priority 8-10: the chain is the core of its own short passage (two to four sentences): state it in one sentence, then give the facts, conditions or consequences that explain it.
  - A row or an item of a table or list that reads as the chain is enough in a block whose format is a table or list.
  - Do not state relations that are not in the brief when they would assert a brand fact.

# LENGTH

- Aim for the middle of the word range of the brief. The range counts all visible body words: sentences, list items and table cell text; it excludes the heading and markdown symbols. The minimum is binding. If the facts, the entities and a natural style need more room, you may go over the maximum by up to 20% (the BLOCK BRIEF gives the cap).
- Never pad with filler. Never cut required entities or connections to fit: write longer, inside the cap. Only if even the cap is not enough, trim detail from the lowest-priority entities.
- If the brief says sub-sections are written separately, your range covers only your own text. Do not cover the facts of the sub-sections; a short lead-in to them is fine.

# FORMATS AND OUTPUT

Output is Markdown, only the body of the block. Allowed building blocks, used exactly as the brief's `Format` line says:

- `paragraph`: plain prose paragraphs separated by one blank line.
- `list`: bullets with `- ` or numbered steps with `1. `. One idea per item, items of similar length, no sub-lists. Use numbers only when the order is real (a sequence of steps that cannot be swapped); otherwise use bullets. May follow one short lead-in sentence. `paragraph + list` means a short paragraph and then the list.
- `table`: a Markdown table with a header row and a separator row (`| Method | Speed |` / `|---|---|`). Short, comparable cells in the output language. May be preceded by one short lead-in sentence.

Use no other format. No headings (`#`), no horizontal rules, no HTML, no emojis. No bold or italic unless the copywriter notes ask for it. If "Visual Elements" mentions an image or infographic, ignore that part.

In a section answer (`## SECTION`) start the body of every block with the marker line `=== bNN ===` (its block id, alone on the line) and write nothing outside the bodies. Otherwise return only the final body of the block, without any marker.

Return only the final body: no heading, no title line, no code fences, no comments, no notes, no explanations, no word count, no mention of keywords or of the brief. The text must end with a complete sentence (or a complete list or table), with no cut-off words, double spaces or non-breaking spaces.

# LANGUAGE

- Write ONLY in the output language from the context, with correct grammar, natural phrasing and the spelling of the GEO (English: British for the UK, Australia, New Zealand, Ireland and India; American for the US and Canada). Use local player terms (for example "pokies") only if the brief or the keywords use them.
- No fragments in other languages. Everything the reader sees (labels, offer wordings, list items, table cells) is in the output language: no English "Get Bonus", "Hot Picks" or "up to X + Y Free Spins" templates unless the exact wording is a proper name from the Brand Information. Brand names, tracked keywords and established loan terms (KYC, RTP, RNG, VIP, app) may stay as they are.
- Write with the full native alphabet and diacritics of the language. Never use ASCII transliteration (German `fuer`, `ueber`, `grosse` instead of `für`, `über`, `große`) and never drop diacritics. Do not put characters of another script inside a word.
- Use the local number and currency formats of the GEO. Do not convert currencies. Quote amounts only when they are in the brand information.
- Keep one format for each kind of value across the whole block: one decimal separator, one thousands separator, one way to write currency, percentages and dates, as the GEO's norm requires (German: `2.500 €`, `4,8`, `250 %`, `21.09.2026`). Never mix `2500 €`, `2.500€` and `EUR 2500` or `4.3` and `4,5`.

# STYLE

Voice: a knowledgeable editor presenting a brand to a reader who is deciding whether it fits. Calm, specific and readable, with a human rhythm, like a good magazine review: it states facts, connects them, explains what they mean for a player and draws a modest conclusion from them. Authoritative through concrete information, not emphatic language. The liveliness comes from sentence construction and from the meaning attached to each fact, never from new facts, feelings or praise.

Person and emotion:
- Third person only. The subject is the casino, the platform, the lobby, the operator, the player. No "we", "our team", "in our experience", no claim of a test, a visit or a personal observation, and no direct address ("you") outside the calls to action allowed under Evaluation.
- No emotion and no exclamation marks. No "great", "exciting", "impressive", "fortunately", "unfortunately", "players will love" or their equivalents.

Rhythm:
- Average sentence about 17 words. Mix short sentences (6-10 words) with longer ones (20-26 words), so a paragraph breathes. Never a row of sentences with the same structure or length.
- Paragraphs of 2-4 sentences. A list or table is introduced by one sentence that carries a fact or a reason.
- Do not begin consecutive sentences with the same word and do not begin every sentence with the brand name; vary the subject (the casino, the lobby, the package, the player, the withdrawal).
- Put the fact that matters most in the first clause of a sentence. No one-sentence paragraphs for drama.

Devices to use:
1. Context before the figure: say what a thing is for, then give the number ("The package is spread over the first three deposits: the first brings ..., the second ..., the third ...").
2. Explain a term in a clause the first time it appears ("free spins, that is spins on a slot with the stake paid by the casino").
3. Consequence of a fact: after a condition or limit add what it means in practice ("Live dealer games count 0 % towards wagering, so a bonus is cleared on slots").
4. Contrast between two facts that really differ ("Slots count 100 %, table games 5 %"). A contrast may start with "but", "while", "whereas" or a local equivalent.
5. Structure of the product first: describe how the lobby, the cashier or the programme is organised. A short link to the neighbouring topic of the page is fine where it helps the reader.
6. Who it suits: where the facts allow, one sentence on which kind of player a feature is useful for, based on a stated fact (minimum deposit, game range, mobile access, limits).
7. Paced detail: a list of providers, games or methods is not a bare enumeration; put the two or three that matter most into a sentence and give the rest compactly.

Evaluation:
- Calls to action are allowed: a plain imperative or invitation tied to a concrete offer or step ("Make a deposit", "Claim the welcome bonus", "Register and receive the package over the first three deposits"), placed where the facts around it justify it, not repeated in every paragraph. Not allowed: urgency and fear of missing out (countdowns, "limited time", "don't miss", "now or never"), pressure or guilt ("you must play"), promises of winnings, and hype ("best", "ultimate", "incredible", "amazing", "guaranteed", "huge wins"). Praise only through a figure from the Brand Information.
- The advantages should be described in greater detail, while the limitations should be presented in a calm tone.

Transitions: use a connector whenever it expresses a real relation (cause, contrast, consequence), including "but", "while", "so", "that is why" and their equivalents. Do not open paragraphs with routine connectors without such a relation (However, Moreover, Furthermore, Additionally, Notably, Importantly, Overall, In conclusion).

Opening and filler: no filler, no repeated ideas, no summary of what you just said, no opening with generic statements about the importance of the topic or the industry. Start with the most useful information. A short opening hook sentence is allowed only in the introduction block of the page and it must carry a fact.

- Banned words and phrases (and their direct translations): meticulous, navigate, navigating, complexities, realm, bespoke, tailored, underpins, ever-changing, ever-evolving, the world of, not only, designed to enhance, it is advisable, unlock, robust, delve, harness, leverage, unveil, elevate, empower, seamless, tapestry, landscape (figurative), testament, pivotal, crucial, game-changer, cutting-edge, comprehensive (as empty praise), holistic, dynamic (vague), "it is important to note", "it is worth mentioning", "in today's fast-paced world", "whether you are a beginner or a pro", "look no further", "at the heart of", "from X to Y" as a vague range.
- No formulaic constructions: "Not only X, but also Y", "It's not just about X, it's about Y", "No X. No Y. Just Z.", rhetorical questions anywhere (including a question that the text answers itself), generic closing paragraphs about the future or an "exciting journey".
- No chain of three adjectives or three benefits in a row ("fast, convenient and safe"). Name only what the facts support.
- No em dashes (—): use commas, colons, full stops or parentheses. Straight quotation marks. Avoid semicolons.
- Keep modal verbs (may, can, could) when they express real conditionality, for example about bonus eligibility or verification.

Example of the target voice (English, placeholders instead of facts: use only the figures and names of your own Brand Information, never these). Dry: "The welcome package is called P. It includes a deposit bonus of up to A and B free spins and is spread over the first three deposits." Target: "The package P is spread over the first three deposits. Most of the free spins come right at the start: C of the B spins belong to the first deposit, the remaining D to the third. The second deposit sits in between with X % up to E, so the package adds up to A in the end." The facts are identical; the target adds the reason, a contrast and varied sentence openings, with no "we", "you" or emotion.

# DIRECT STATEMENTS

- Connective tissue is welcome. Use PAGE STRUCTURE FOR CONTEXT to place the block: you may lead in from the topic before it and lead out to the topic after it in a clause or a sentence, point to a neighbouring topic where it helps the reader, and give practical advice (for example to check the terms of an offer) where it fits. Do it in natural wording, not as a mechanical announcement of sections, and do not retell the facts of the other blocks.
- We are the source of the information. State facts directly, with the brand, the platform, the operator, the player or the feature as the subject. Never refer to where a fact comes from: no "laut Plattform", "laut eigenen Angaben", "laut Website-Übersicht", "gemäß den Bedingungen", "der Anbieter nennt/gibt an", "wird genannt/angezeigt/angegeben", "auf der Aktionskarte", and no equivalents in other languages. Scope is not a source: "bei der zweiten und dritten Einzahlung 35x" is a fact and stays.

# FIX MODE

If a `## FIX MODE` section is present, rewrite the whole block so that every listed problem is solved. Keep what was already correct, and keep respecting the whole BLOCK BRIEF. Follow the numbers in the problem list literally (if a keyword appears 3 times and must appear once, remove exactly two occurrences; if the text has 250 words and the cap is 192, bring it under the cap; if it has 90 and must have 120-160, expand it). After a fix, re-check every other hard constraint, because a fix in one place easily breaks another (shortening can remove a required keyword or entity). Do not mention the fixes in the text.

# CONSISTENCY WITH THE REST OF THE PAGE

- Use the same names for the same things as the already written blocks. Use full descriptive names where relevant: First Deposit Bonus, Free Spins, Minimum Deposit, Maximum Withdrawal, Live Casino, Random Number Generator.

# USER

## CONTEXT
Brand: Longfu88 (this name and its spellings are tracked keywords: the block brief gives the exact count; where it says 0 the brand name is free to use)
Country / GEO: SG
Language: English (en). Write ONLY in this language.
Page intent: Long brand-review page about the Longfu88 online casino for players from Singapore, ordered around the offer: the fact table, then the welcome bonus with its terms, reloads, cashback, the rewards area, the VIP programme and the sportsbook offer, followed by registration and verification, payments and withdrawals, the game lobby and providers, mobile access, licence and eligibility, responsible gambling, support, a pros and cons table, an FAQ about bonuses and payouts and a closing assessment. Page voice: businesslike and comparative, paragraphs of three to four sentences, sentences of about 18 words; every bonus figure is followed by the condition it depends on (context before the figure, consequence, contrast); calls to action only at the welcome bonus, at the weekly cashback and at the sportsbook offer. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Review: Bonuses, Games and Payments for Singapore (109-138 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Singapore.
b02   H2 Casino Information (88-112 words): A fact sheet of the casino: welcome bonus, Wagering, minimum deposit, cashback, licence, operator, launch year, payment methods, currencies, languages, support.
b03   H2 The Casino Welcome Bonus (146-187 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b04     H3 Wagering, Validity and Maximum Bet (109-138 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b05   H2 Reload Offers and Seasonal Campaigns (128-162 words): The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
b06     H3 Weekly Cashback and Daily Rebates (83-106 words): Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
b07     H3 Bonus Crab, Wheel of Fortune and the Coin Shop (77-97 words): The gamification features of the rewards area: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop.
b08   H2 VIP Programme: Points, Levels and Limits (115-146 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b09   H2 Sportsbook Offer: Markets and Bonuses (109-138 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b10     H3 Sport Bonuses, Cashback and Boosts (83-106 words): The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
b11   H2 Registration and Login (123-157 words): How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.
b12     H3 Verification Before the First Withdrawal (102-130 words): When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.
b13   H2 Deposit Methods, Limits and Speed (133-171 words): Deposit methods grouped by type with the general limits and speed, the local options for Singapore and the six-step deposit route.
b14     H3 Withdrawals: Steps, Timing and Fees (122-154 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b15   H2 Casino Lobby and Game Types (90-113 words): The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.
b16     H3 Slots with Their RTP (102-130 words): Three example slots with their provider, RTP, volatility and maximum multiplier.
b17     H3 Live Dealer Section (96-122 words): The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.
b18     H3 Fishing, P2P, Fast Games and Lottery (83-106 words): The remaining game categories in one block: table games, fishing, P2P, fast games, lottery and crash and instant games.
b19   H2 Software Providers (83-106 words): Which studios supply the games, named from the provider list.
b20   H2 Mobile Access on Android and iOS (106-134 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b21   H2 Operator, Licence and Who May Play (191-244 words): Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected.
b22   H2 Responsible Gambling and Self-Exclusion (115-146 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b23   H2 Customer Support (77-97 words): Support channels, availability and languages.
b24   H2 Pros and Cons (53-67 words): A pros and cons table built only from facts stated elsewhere on the page.
b25   H2 Questions About Bonuses and Payouts (229-293 words): Short answers on claiming the bonus, wagering, weekly cashback, VIP levels, withdrawal time, withdrawal fees.
b26   H2 Bottom Line on the Offer (106-134 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Review: Bonuses, Games and Payments for Singapore
Longfu88 is an online casino launched in 2026 that combines casino games, live dealer games, sports betting and lottery on one site. The lobby is divided into nine categories: slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games. A sportsbook runs alongside it for players who prefer to bet on matches rather than spin reels.

This page is written for players from Singapore, and only adults may take part: the minimum age is 18. The sections below cover the fact sheet, the operator's licence, the bonuses, the games, payments, mobile play and responsible gambling, so each part of the offer can be compared before an account is opened.

## Casino Information
=== b02 ===
| Parameter | Details |
|---|---|
| Welcome bonus | First deposit bonus of 188% up to €2,088 + 18 Free Spins |
| Wagering | 25x the deposit plus bonus amount, 40x Free Spins winnings |
| Minimum deposit | €10 |
| Cashback | Up to 10% of weekly net casino losses, capped at €6,988 |
| Licence | Costa Rica jurisdiction, operator Lumina, registration number 000-039123-R-319326-001 |
| Operator | Lumina |
| Launched | 2026 |
| Payment methods | Visa, Mastercard, Bank Transfer, Bitcoin, Ethereum, Litecoin, USDT (TRC20), PayNow, DBS Bank |
| Currencies | EUR, USD, MYR, THB, SGD, USDT |
| Support languages | English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese |
| Support | support@longfu88.com, 24/7 live chat |

## The Casino Welcome Bonus
The Casino Welcome Bonus is a deposit bonus that matches the first qualifying deposit, so the reward grows with the amount a new player pays in. Under this name, the Longfu88 bonus gives 188% up to €2,088 plus 18 Free Spins, that is spins on a slot with the stake paid by the casino. The qualifying minimum deposit is €50, and each account can take one welcome offer.

Claiming takes four steps:

- Register an account and complete the required personal details.
- Make the first qualifying deposit.
- Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.
- Play eligible casino games and complete the wagering before expiry.

Activation happens in My Bonuses after the deposit and before any wager, and no promo code step is part of the listed procedure. Two alternatives exist: the Live Casino Welcome Bonus (125% up to €888, minimum deposit €30) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, minimum deposit 50 USDT) are alternative first-deposit offers, so a player picks one of them. Register and claim the Casino Welcome Bonus at Longfu88.

### Wagering, Validity and Maximum Bet
The Casino Welcome Bonus expires 10 days after activation, and its wagering requirement is 25 times the deposit plus the bonus amount, so the terms below decide how much of the credited sum can be withdrawn.

| Condition | Value |
|---|---|
| Wagering | 25x the deposit plus bonus amount |
| Free Spins wagering | 40x Free Spins winnings |
| Validity | 10 days from activation |
| Maximum bet | €22.5 per spin |
| Maximum cashout | 5x the initial bonus amount |

Neteller and Skrill deposits are excluded from the offer, and only one promotional bonus can be active at a time. A withdrawal request before claiming or while the bonus is active can void eligibility, while cancelling the promotion forfeits bonus funds and unconverted winnings. Verification may be required before bonus winnings are paid.

## Reload Offers and Seasonal Campaigns
Seven weekly, weekend, one-day and seasonal offers sit beside the welcome package, each with its own deposit and wagering terms.

| Offer | Reward | Min. deposit | Wagering | Validity |
|---|---|---|---|---|
| Casino Weekly Reload | 50 Free Spins | €30 | 40x winnings from Free Spins | 7 days |
| Casino Weekly Crypto Reload | 60% up to 1,000 USDT | 20 USDT | 30x deposit plus bonus | 7 days |
| Casino Weekend Reload | Up to €3,360 + 50 Free Spins | €50 | 30x deposit plus bonus, 40x Free Spins winnings | 7 days |
| Casino Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 20 USDT | 30x deposit plus bonus, 40x Free Spins winnings | 7 days |
| Casino Double Fortune: One-Day Reload Special | 50% up to €500 | €30 | 30x deposit plus bonus | 24 hours |
| Casino Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | €20 | 40x Free Spins winnings | 7 days |
| Casino Dragon Quest (verification reward) | €10 bonus credit | €20 | 30x promotional credit | 7 days |

Every promotion is activated in My Bonuses, allows one claim per promotional period and cannot be combined with another active casino bonus. While bonus funds are wagered, the maximum stake is €5 per spin.

### Weekly Cashback and Daily Rebates
The Casino Weekly Cashback returns up to 10% of weekly net casino losses, capped at €6,988, counted from Monday 00:00 UTC through Sunday 23:59 UTC. Players opt in for a four-week cycle, and the cashback is credited to My Bonuses on Monday with 10x wagering. The VIP cashback rates follow the tier:

| VIP tier | Cashback | Maximum |
|---|---|---|
| Bronze | 2% | €1,888 |
| Silver | 4% | €2,388 |
| Gold | 6% | €2,988 |
| Platinum | 8% | €3,988 |
| Diamond | 10% | €6,988 |

Alongside it, the Live Casino Cashback pays 25% up to €850. Daily credits come from the Unlimited Rebate: 0.9% on casino, 1.0% on live casino, 0.8% on P2P and 1.0% on lottery play, each with 1x wagering. Only real-money bets count. Opt in to the weekly cashback to start a cycle.

### Bonus Crab, Wheel of Fortune and the Coin Shop
Five features fill the rewards area. Bonus Crab opens a crab reward through claimed picks and stays valid for 7 days, with 30x wagering on bonus credit and 40x on Free Spins winnings. The Wheel of Fortune accepts an eligible spin or Coins, and its awards are valid for 7 days with 30x wagering.

Challenges and Collections sit under Rewards, and completed challenges unlock Coins, Free Spins and bonus credits. Coins are exchanged in the Coin Shop for rewards and bonus credits up to €4,500, with prices varying by item. Rewards can carry separate wagering requirements.

## VIP Programme: Points, Levels and Limits
The VIP Programme is built on real-money play. VIP points are earned through eligible real-money gameplay and unlock numbered reward levels, 25 in all, grouped into the tiers Bronze, Silver, Gold, Platinum and Diamond. Each level carries a reward, a cashback percentage and a withdrawal limit, and the table shows six of them.

| Level | Points | Reward | Cashback | Withdrawal limit |
|---|---|---|---|---|
| 1 | 1 | €9.8 | 1% | €9,800 |
| 5 | 70 | €24.5 | 2% | €34,300 |
| 10 | 700 | €147 | 4% | €63,700 |
| 15 | 2,100 | €392 | 6% | €88,200 |
| 20 | 3,600 | €637 | 8% | €117,600 |
| 25 | 5,500 | €980 | 10% | €147,000 |

Higher VIP levels raise withdrawal limits and cashback, and they add personalised offers. A personal VIP manager is available from level 4. Reward and withdrawal limits may differ by VIP level and currency, and the rules of the programme can change, so the current terms are worth checking before a player aims for a higher level.

## Sportsbook Offer: Markets and Bonuses
The Longfu sports section of Longfu88 is a sportsbook that covers football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football. Football leads the list, while esports and virtual football add digital formats. The nine entries mix team games, racket sports and digital events, so the choice is not limited to one kind of match.

Seven bet types are offered: single, accumulator, live, handicap, totals, outrights and Bet Builder. A single backs one selection, an accumulator links several selections into one bet, and Bet Builder combines selections from the same match. Live betting brings live odds and in-play markets, so a bet can be placed while the match is running. Event availability and market selection can vary by jurisdiction.

### Sport Bonuses, Cashback and Boosts
Claim the Sport First Deposit Bonus on a first sports deposit, separate from the casino offers.

| Offer | Reward | Min. deposit | Wagering |
|---|---|---|---|
| Sport First Deposit Bonus | 100% up to €1,888 | €50 | 8x, 30 days |
| Sport Weekly Reload Bonus | 50% up to €2,500 | €50 | 8x |
| Sport Weekend Reload Bonus | 50% up to €3,750 | €50 | 8x |

Crypto equivalents exist. Sports Cashback returns 10% up to €2,500 of weekly eligible net losses, and the Unlimited Sports Rebate credits 0.70%. Further offers are the 2 Goals Ahead early payout, the Parlay Boost (up to 100% extra winnings) and Bet Builder Risk Free (50% stake return up to €250). Only settled bets qualify: singles need odds of at least 2.00, accumulator selections 1.50, and voided or cashed-out bets do not count.

## Registration and Login
An account is opened by e-mail in five steps, and registration requires an email, a password, a legal name, a date of birth and a residential address.

1. Open Longfu88 and select Register.
2. Enter email and create a password.
3. Confirm age and acceptance of Terms and Conditions and Privacy Policy.
4. Complete the additional personal details and residential address.
5. Select Create Account and complete any requested email confirmation.

Each player may hold only one personal account, and the minimum age is 18 or the legal gambling age of the relevant jurisdiction. The Longfu88 login runs on the registered email and password: select Login on the website, enter both and complete any security check. If the password is lost, Forgot Password on the login screen sends a reset link to the registered email, and the emailed instructions lead to a new one.

### Verification Before the First Withdrawal
Verification may be requested at an account review, before a withdrawal, on unusual or high-value transactions and after changes to account or payment details. A first payout is a likely trigger, so the documents should be ready. The accepted documents are:

- Identity: passport, national identity card or driving licence
- Address: utility bill or bank statement
- Payment method: evidence of bank, card or digital wallet ownership
- Source of funds, when requested: proof of income, bank statements or other supporting financial documents

Documents can be sent within 30 days of a request, and a complete set is reviewed within up to 10 days of receipt. Withdrawals may be held until the checks are done, and failed checks can lead to refused transactions or account restrictions.

## Deposit Methods, Limits and Speed
For Singapore, PayNow, PayNow QR, DBS Bank and OCBC Bank (all in SGD) are the local options, and the table groups every method by type.

| Method type | Examples | Currencies |
|---|---|---|
| Local banks and wallets | PayNow, PayNow QR, DBS Bank, OCBC Bank, QRIS, DANA, GrabPay | SGD, IDR, MYR |
| Cards | Visa, Mastercard | IDR, MYR, SGD, VND |
| Bank transfer | Bank Transfer | IDR, MYR, VND |
| Cryptocurrencies | Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), USDC | BTC, ETH, LTC, USDT, USDC |
| E-wallets | Neteller, Skrill | EUR |
| European methods | Sofort, Giropay | EUR |

For every method the minimum is €10 and the maximum €5,000 per transaction, and deposits are credited within 1-2 minutes. The casino charges no processing fee, but provider or blockchain network fees may apply. Limits can differ by country, currency and method, and Neteller and Skrill deposits are excluded from the welcome bonus.

To deposit, log in to the Longfu88 account, open the cashier and select Deposit, then choose an available method with its supported currency or network. Enter the amount and payment details, confirm the transaction as the provider instructs and wait for the funds to reach the playable balance.

### Withdrawals: Steps, Timing and Fees
Withdrawals go to bank transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), Touch'n Go, DANA, MoMo, DBS Bank or Online Banking, from €20 up to €5,000, in six steps:

1. Log in to Longfu88 and open the cashier.
2. Select Withdrawal and choose a supported destination or payment method.
3. Enter the amount and the receiving bank, wallet, or blockchain address.
4. Complete identity and payment-method verification if prompted.
5. Review the request and confirm submission.
6. Wait for casino processing and any bank or network settlement before receiving funds.

Requests are generally processed within three working days. Card, crypto and wallet payouts take 1 to 3 business days, while a bank transfer needs up to 3 business days of casino processing plus 3 to 5 for bank delivery. No standard casino withdrawal fee applies, but provider and blockchain fees may apply. Where turnover is below the deposited amount, a 10% commission with a minimum of €2.25 can be charged (a minimum 1x deposit turnover can apply before a withdrawal), and 15% on some card or bank transfer funded transactions. Identity checks can delay a payout.

## Casino Lobby and Game Types
Longfu 88 Casino is an online casino that offers slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games in nine lobby categories. The mix lets a player move between reel games, dealer-led tables, peer play and quick-result formats within one lobby. Each category is a different style of play, so the choice depends on whether a player prefers fast rounds or slower, dealer-led sessions. Slots and live dealer games come first below, each with its own sub-section, and the remaining categories follow in a shorter overview. Jackpots and crash games complete the offer at Longfu88.

### Slots with Their RTP
Three example slots show how the key figures differ. Gates of Olympus, from Pragmatic Play, has an RTP of 96.50% and a maximum multiplier of 5,000x, with high volatility. Sweet Bonanza, also from Pragmatic Play, has an RTP of 96.48%, high volatility and a maximum multiplier of 21,175x. Hacksaw Gaming supplies Wanted Dead or a Wild, which has an RTP of 96.38%, very high volatility and a maximum multiplier of 12,500x.

RTP is the share of stakes a slot returns to players over a very large number of spins, not a promise for a single session. Volatility describes how the wins are spread: high volatility means fewer but larger payouts, which matters for a player with a small budget.

### Live Dealer Section
Live dealer games form a separate lobby category: a human dealer runs each round and the player follows it on screen instead of relying on a random number generator. Among its games is the exclusive Longfu88 Baccarat, a live or table game with baccarat gameplay. Evolution and SA Gaming are among the studios that power the live casino, and the provider overview lists them alongside the other suppliers of the lobby. Players who like a table with a dealer will find this category the closest match, while tables without a dealer sit in the next sub-section.

### Fishing, P2P, Fast Games and Lottery
Beyond slots and live tables, the online casino also offers fishing, P2P, fast, lottery and crash games, each with its own pace. Table games cover card and wheel formats played against the casino. Fishing games are arcade-style rounds in which the player aims at targets on screen to collect rewards. P2P games are played against other players rather than against the casino. Fast games are short-round formats with quick results, and lottery games are number draws in which the player waits for the result. Crash and instant games also resolve quickly, either when a rising multiplier is cashed out in time or when the outcome appears at once.

## Software Providers
The studios that supply slots, live and table games to the casino at Longfu 88 are Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft and Hacksaw Gaming. Evolution and Pragmatic Play are the two names that also appear in the live and slots sections of this page, while Hacksaw Gaming stands behind one of the example slots. A list of several developers means the lobby is not tied to the style of a single studio, and the provider name shown beside a game helps to compare titles that look alike.

---

## BLOCK BRIEF
Block: b20, H2 "Mobile Access on Android and iOS" (under H1 "Longfu88 Casino Review: Bonuses, Games and Payments for Singapore")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 106-134 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 134, but never beyond 160 words.
Format: paragraph + list. Visual Elements: Bulleted/numbered list — 5 of 7 lists on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 2 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 app": exactly 1 time(s)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu": 0 (do not use)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Mobile Access [10]
- Add to Home Screen [8]
- Android [6]
- iOS [6]
- Responsive Website [7]
Entity Connections to state explicitly [priority]:
- Responsive Website → works on → smartphone and tablet browsers [8]
- Home Screen Shortcut → gives → quick access to the casino and sportsbook [6]
Summary: Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
Copywriter Notes: Explain that the casino runs as a responsive website on smartphone and tablet browsers (platforms Android, iOS and mobile web) and can be added to the home screen as a shortcut; give the Android route (Chrome, browser menu, Add to Home screen, confirm) and the iOS route (Safari, Share, Add to Home Screen, Add) as two short numbered lists, each preceded by one sentence. Name the available functions (casino, sportsbook, account access, deposits, withdrawals, bonuses). Where "Longfu88 app" is used, it sits in a sentence that makes clear it is the home-screen version of the site. Do NOT claim a download from an app store or an APK file: none is given. Use "Longfu88" exactly twice and "Longfu88 app" exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them. Step one of the Android list and of the iOS list names the brand as in the Brand Information; these two occurrences of "Longfu88" are part of the exact count of this block, the rest goes into the running text.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_app.app_information: {"platforms": ["Android", "iOS", "Mobile web"], "mobile_access": "Responsive Longfu88 website usable on smartphone and tablet browsers.", "android_installation": ["Open Longfu88 in Chrome.", "Open browser menu and choose Add to Home screen.", "Confirm the shortcut."], "ios_installation": ["Open Longfu88 in Safari.", "Tap Share and choose Add to Home Screen.", "Confirm Add."], "features": ["Casino", "Sportsbook", "Account access", "Deposits", "Withdrawals", "Bonuses"]}
Counting warning: the facts above contain tracked keywords "Longfu88" (x3). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 2, 'Longfu88 app': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').
