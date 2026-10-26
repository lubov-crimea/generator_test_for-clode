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
Page intent: Brand-review page about the Longfu88 online casino for players from Singapore, led by the game lobby: the fact table, the game categories with slots, live casino and the other game types, providers, then the welcome bonus and promotions, VIP levels, sports betting, payments, registration, mobile access, licence and safety, responsible gambling, support, an FAQ and a verdict. Page voice: lively but factual, sentences of about 15 words, the reader is addressed as "you" now and then, every game category is described by what the player does in it, concrete figures (RTP, volatility, multipliers) come before adjectives, contrasts between game types; paragraphs of two to three sentences; one call to action, at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Games, Bonuses and Payments: Singapore Review (96-122 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Singapore.
b02   H2 Casino Facts (88-112 words): A fact sheet of the casino: licence, welcome bonus, cashback, operator, launch year, languages, currencies, payment methods, Game types, Game providers, support.
b03   H2 Game Lobby (90-113 words): The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.
b04     H3 Slot Games (109-138 words): Three example slots with their provider, RTP, volatility and maximum multiplier.
b05     H3 Live Dealer Games (96-122 words): The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.
b06     H3 Table, Fishing, P2P and Lottery Games (90-113 words): The remaining game categories in one block: table games, fishing, P2P, fast games, lottery and crash and instant games.
b07   H2 Game Providers (57-73 words): Which studios supply the games, named from the provider list.
b08   H2 Welcome Bonus for Casino Players (141-178 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b09     H3 Welcome Bonus Terms (102-130 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b10   H2 Reloads and Cashback (178-228 words): The seven reload and seasonal offers in a table, then the weekly cashback with VIP rates, the live casino cashback and the rebates.
b11     H3 Rewards Area (77-97 words): The gamification features of the rewards area: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop.
b12   H2 VIP Programme (109-138 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b13   H2 Sports Betting (102-130 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b14     H3 Sports Bonuses (77-97 words): The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
b15   H2 Payments: Deposits and Withdrawals (242-309 words): Deposit methods by type with limits and speed in a table, the deposit route, then withdrawal methods, steps, timing and fees.
b16   H2 Registration and Verification (173-219 words): Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes.
b17   H2 Mobile Gaming (96-122 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b18   H2 Licence and Security (173-219 words): Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected.
b19   H2 Responsible Gambling (96-122 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b20   H2 Support (70-90 words): Support channels, availability and languages.
b21   H2 Game and Account Questions (158-202 words): Short answers on minimum deposit, claiming the bonus, cryptocurrencies, the app question, currencies.
b22   H2 Verdict on the Casino (90-113 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Games, Bonuses and Payments: Singapore Review
Longfu88 is an online casino launched in 2026 that combines slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games with a sportsbook. Each of these game categories gets its own description below, based on what a player actually does in it. This review is written for players from Singapore, and adult players must be at least 18 years old to register. The remaining sections cover the fact sheet, the licence, bonuses, payments, mobile play and responsible gambling, so that the full offer can be weighed before a first deposit.

## Casino Facts
| Parameter | Details |
|---|---|
| Licence | Costa Rica, Lumina, 000-039123-R-319326-001 |
| Welcome bonus | 188% up to €2,088 + 18 Free Spins |
| Cashback | Up to 10% of weekly net casino losses |
| Operator | Lumina |
| Launched | 2026 |
| Support languages | English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese |
| Currencies | EUR, USD, MYR, THB, SGD, USDT |
| Payment methods | Visa, Mastercard, Bank Transfer, Bitcoin, USDT (TRC20), PayNow |
| Game types | Slots, Live dealer games, Table games, Jackpots, Fishing, P2P games, Fast games, Lottery, Crash & instant games |
| Game providers | Evolution, Pragmatic Play, Red Tiger, NetEnt, Hacksaw Gaming |
| Support | support@longfu88.com, 24/7 live chat |

## Game Lobby
Longfu88 sorts its games into nine categories, so a player chooses a format first and a title second. The Longfu88 Casino lobby opens with slots and live dealer games, which have their own sub-sections below, while jackpots and crash games give it a faster side. Table games and lottery cover the classic formats, and fishing, P2P and fast games are grouped in the last sub-section. The online casino offers the full set in one lobby:

- Slots
- Live dealer games
- Table games
- Jackpots
- Fishing
- P2P games
- Fast games
- Lottery
- Crash & instant games

### Slot Games
In a slot the player sets a stake, spins the reels and waits for the feature round, and three examples show how different the numbers can be. Gates of Olympus from Pragmatic Play has an RTP of 96.50%, high volatility and a maximum multiplier of 5,000x. Sweet Bonanza, also from Pragmatic Play, sits close with an RTP of 96.48% and high volatility, but its maximum multiplier is 21,175x. Hacksaw Gaming supplies Wanted Dead or a Wild, which pairs an RTP of 96.38% with very high volatility and a maximum multiplier of 12,500x. RTP is the share of stakes a slot returns over a very long run, while volatility describes how unevenly it pays: high volatility means rarer but larger hits and a balance that moves in bigger swings.

### Live Dealer Games
Live dealer games put a real host on a video stream, and the player bets from the screen while the round plays out in real time. The Longfu 88 Casino lobby treats the live casino as a category of its own. Among the tables sits the exclusive Longfu88 Baccarat, a live or table game with baccarat gameplay that belongs to this casino alone. The live casino is powered by Evolution and SA Gaming among other studios, and both names appear in the provider list. Unlike a slot, where a spin settles in seconds, a live round follows the pace of the dealer, so a session is slower and more deliberate.

### Table, Fishing, P2P and Lottery Games
Table games are the classic casino formats played against the house at a virtual table, where the player decides each bet or hand. Fishing games work differently: the player aims at moving targets on the screen and collects a reward for every hit. P2P games are played against other players rather than against the house. Fast games shorten the rounds, so bets follow one another quickly, while lottery is slower and built around picking numbers and waiting for the draw. Crash and instant games are the quickest of all: the player places a bet, watches a multiplier rise and decides when to cash out. The online casino also offers fishing, P2P, fast, lottery and crash games next to its slots and live tables.

## Game Providers
Game providers supply slots, live and table games to the casino. The studios behind the Longfu 88 lobby include Evolution, Pragmatic Play and Hacksaw Gaming, the last two already named in the slot examples above, as well as Red Tiger and NetEnt. Every name on the list is shown below:

- Evolution
- Red Tiger
- NetEnt
- Big Time Gaming
- Pragmatic Play
- Yggdrasil
- SA Gaming
- Skywind
- Betsoft
- Hacksaw Gaming

## Welcome Bonus for Casino Players
The Longfu88 bonus for new players is the Casino Welcome Bonus: 188% up to €2,088 plus 18 Free Spins on the first qualifying deposit. It is a deposit bonus, so the percentage is calculated on the amount paid in, and the free spins are added to it. The qualifying minimum deposit of this offer is €50, and each account can take one welcome offer. New registered players claim it in four steps:

- Register an account and complete the required personal details.
- Make the first qualifying deposit.
- Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.
- Play eligible casino games and complete the wagering before expiry.

The claiming route is the My Bonuses activation after the qualifying deposit, and no Longfu88 promo code step is part of the listed claiming procedure. Two alternatives exist for the first deposit: the Live Casino Welcome Bonus (125% up to €888, minimum deposit €30) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, minimum deposit 50 USDT). The Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers, so a player picks one of them. Register at Longfu88 and claim the Casino Welcome Bonus after the first deposit.

### Welcome Bonus Terms
The terms of the Casino Welcome Bonus decide how quickly the bonus can be turned into withdrawable money, so they are worth reading before the first deposit.

| Condition | Value |
|---|---|
| Wagering | 25x the deposit plus bonus amount |
| Free Spins wagering | 40x Free Spins winnings |
| Validity | 10 days from activation |
| Maximum bet | €22.5 per spin |
| Maximum cashout | 5x the initial bonus amount |

The bonus expires 10 days after activation, so the wagering has to be finished inside that window. Neteller and Skrill deposits are excluded, and only one promotional bonus can be active at a time. A withdrawal request before claiming or while the bonus is active can void eligibility, cancelling the promotion forfeits bonus funds and unconverted winnings, and verification may be required before bonus winnings are paid.

## Reloads and Cashback
The Casino Weekly Reload gives 50 Free Spins, and the weekend, crypto, one-day reload special and seasonal promotion vary in reward.

| Offer | Reward | Min. deposit | Wagering | Validity |
|---|---|---|---|---|
| Weekly Reload | 50 Free Spins | €30 | 40x winnings from Free Spins | 7 days |
| Weekly Crypto Reload | 60% up to 1,000 USDT | 20 USDT | 30x deposit plus bonus | 7 days |
| Weekend Reload | Up to €3,360 + 50 Free Spins | €50 | 30x deposit plus bonus, 40x Free Spins winnings | 7 days |
| Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 20 USDT | 30x deposit plus bonus, 40x Free Spins winnings | 7 days |
| Double Fortune | 50% up to €500 | €30 | 30x deposit plus bonus | 24 hours |
| Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | €20 | 40x Free Spins winnings | 7 days |
| Dragon Quest | €10 bonus credit | €20 | 30x promotional credit | 7 days |

Each offer is activated in My Bonuses, allows one claim per promotional period and cannot be combined with another active casino bonus. The maximum stake is €5 per spin while wagering bonus funds.

Longfu88 pays the Casino Weekly Cashback: up to 10% of weekly net casino losses, capped at €6,988, counted from Monday 00:00 UTC to Sunday 23:59 UTC. Players opt in for a four-week cycle, and the cashback reaches My Bonuses on Monday with 10x wagering. Only real-money bets count. VIP cashback rates:

| VIP tier | Cashback | Maximum |
|---|---|---|
| Bronze | 2% | €1,888 |
| Silver | 4% | €2,388 |
| Gold | 6% | €2,988 |
| Platinum | 8% | €3,988 |
| Diamond | 10% | €6,988 |

The Live Casino Cashback returns 25% up to €850. Four Unlimited Rebates are credited daily with 1x wagering: casino 0.9%, live casino 1.0%, P2P 0.8% and lottery 1.0%.

### Rewards Area
The rewards area collects the gamified extras in one place. Bonus Crab lets a player claim picks to open a crab reward, valid for 7 days with 30x wagering on bonus credit and 40x on Free Spins winnings. Wheel of Fortune costs an eligible spin or Coins and also lasts 7 days, with 30x wagering. Challenges unlock coins, free spins and bonus credits for qualifying tasks, and Collections sit next to them under Rewards. Coins are exchanged in the Coin Shop for rewards and bonus credits up to €4,500, at prices that vary by item. Rewards can carry their own wagering requirements.

## VIP Programme
The Longfu88 VIP Program turns regular play into progress: VIP points come from eligible real-money gameplay and unlock numbered reward levels. Its 25 levels are grouped into the tiers Bronze, Silver, Gold, Platinum and Diamond, and the table shows six of them from the first to the last.

| Level | Points | Reward | Cashback | Withdrawal limit |
|---|---|---|---|---|
| 1 | 1 | €9.8 | 1% | €9,800 |
| 5 | 70 | €24.5 | 2% | €34,300 |
| 10 | 700 | €147 | 4% | €63,700 |
| 15 | 2,100 | €392 | 6% | €88,200 |
| 20 | 3,600 | €637 | 8% | €117,600 |
| 25 | 5,500 | €980 | 10% | €147,000 |

Higher VIP levels raise withdrawal limits and cashback, which grows from 1% at level 1 to 10% at level 25. From level 4, at 50 points, personalised offers and a personal VIP manager join the benefits. Reward and withdrawal limits may differ by VIP level and currency, and the program rules can change.

## Sports Betting
Longfu88 runs a sportsbook next to the casino lobby, so a player can move between a slot session and a bet within one account. The sportsbook covers football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football. Seven bet types are available: single, accumulator, live, handicap, totals, outrights and Bet Builder. A single is one selection, an accumulator combines several selections into one bet, and Bet Builder joins markets from the same match. Live betting offers live odds and in-play markets, so prices move while the match is under way. The Longfu sports section is the place to see which events are open, and event availability and market selection can vary by jurisdiction.

### Sports Bonuses
The Sport First Deposit Bonus is valid for 30 days.

| Offer | Reward | Min. deposit | Wagering |
|---|---|---|---|
| Sport First Deposit Bonus | 100% up to €1,888 | €50 | 8x |
| Sport Weekly Reload Bonus | 50% up to €2,500 | €50 | 8x |
| Sport Weekend Reload Bonus | 50% up to €3,750 | €50 | 8x |

Crypto equivalents exist. Sports Cashback returns 10% up to €2,500 of weekly eligible net losses, Unlimited Sports Rebate pays 0.70%, 2 Goals Ahead pays football bets early, Parlay Boost adds up to 100% extra winnings from three legs, and Bet Builder Risk Free returns 50% of the stake up to €250. Qualifying singles need minimum odds of 2.00, accumulator selections 1.50, and voided or cashed-out bets do not count.

## Payments: Deposits and Withdrawals
Payment methods at the casino are grouped below by type, with the Singapore options listed separately.

| Method type | Examples | Currencies |
|---|---|---|
| Local banks and wallets | QRIS, DANA, GrabPay, DuitNow, MoMo, PromptPay QR | IDR, MYR, VND, THB |
| Singapore methods | PayNow, PayNow QR, DBS Bank, OCBC Bank | SGD |
| Cards | Visa, Mastercard | IDR, MYR, SGD, VND |
| Bank transfer | Bank Transfer | IDR, MYR, VND |
| Cryptocurrencies | Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), USDC | BTC, ETH, LTC, USDT, USDC |
| E-wallets | Neteller, Skrill | EUR |
| European methods | Sofort, Giropay | EUR |

Every method has a €10 minimum and a €5,000 maximum per transaction, and deposits are credited within 1-2 minutes with no casino processing fee, although provider or blockchain network fees may apply. Limits can differ by country, currency and method, and Neteller and Skrill deposits are excluded from the welcome bonus. To deposit, log in, open the cashier, select Deposit, choose a method with its currency or network, enter the amount and payment details, confirm as the provider instructs and wait for the funds to reach the playable balance.

Withdrawals go to bank transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20 and BEP20), Touch'n Go, DANA, MoMo, DBS Bank or Online Banking, with a €20 minimum and a €5,000 maximum. Six steps lead to a payout:

1. Log in to Longfu88 and open the cashier.
2. Select Withdrawal and choose a supported destination or payment method.
3. Enter the amount and the receiving bank, wallet, or blockchain address.
4. Complete identity and payment-method verification if prompted.
5. Review the request and confirm submission.
6. Wait for casino processing and any bank or network settlement before receiving funds.

The Lngfu88 withdrawal time is 1 to 3 business days for cards, crypto and wallets, while a bank transfer takes up to 3 business days of casino processing plus 3 to 5 business days for bank delivery. Requests are generally processed within three working days.

There is no standard casino withdrawal fee, but provider and blockchain fees may apply. A 10% commission (minimum €2.25) can apply where turnover is below the deposited amount, since a minimum 1x deposit turnover can apply before a withdrawal, and 15% can apply to some card or bank transfer funded transactions. Identity checks can delay a payout.

## Registration and Verification
Registration needs an email, a password, a legal name, a date of birth and a residential address, and each player may hold only one personal account. The email route has five steps:

1. Open Longfu88 and select Register.
2. Enter email and create a password.
3. Confirm age and acceptance of Terms and Conditions and Privacy Policy.
4. Complete the additional personal details and residential address.
5. Select Create Account and complete any requested email confirmation.

The Longfu88 login works with the registered email and password: select Login on the website, enter the details and complete any security check. A forgotten password is handled through Forgot Password on the login screen, which sends a reset link by email.

KYC verification is a separate step. It may be required before a withdrawal, after unusual or high-value transactions and after changes to account or payment details. The documents come in four groups:

- Identity documents: passport, national identity card or driving licence
- Proof of address: utility bill or bank statement
- Payment method: evidence of bank card or digital wallet ownership
- Source of funds, when requested: proof of income, bank statements or other supporting financial documents

Documents can be sent within 30 days of the request, and a complete set is normally reviewed within 10 days. Withdrawals may be held until the checks are done, and failed checks can lead to refused transactions or account restrictions.

## Mobile Gaming
Mobile access runs through a responsive website that works on smartphone and tablet browsers, so the lobby, the sportsbook and the account are reachable on Android, iOS and mobile web. The available functions are casino, sportsbook, account access, deposits, withdrawals and bonuses. An Add to Home Screen shortcut gives quick access to the casino and sportsbook, and no app-store download or APK file is described. On Android the shortcut takes three steps:

1. Open Longfu88 in Chrome.
2. Open browser menu and choose Add to Home screen.
3. Confirm the shortcut.

On iOS the route runs through Safari:

1. Open Longfu88 in Safari.
2. Tap Share and choose Add to Home Screen.
3. Confirm Add.

---

## BLOCK BRIEF
Block: b18, H2 "Licence and Security" (under H1 "Longfu88 Casino Games, Bonuses and Payments: Singapore Review")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 173-219 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 219, but never beyond 262 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "casino Longfu88": exactly 1 time(s)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": exactly 1 time(s)
- "Longfu": 0 (do not use)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Online Casino [10]
- Official Website [7]
- Account Currencies [5]
- Player Eligibility [6]
- Gambling Licence [10]
- Operator [8]
- Data Protection [8]
- Data Controller [6]
- Account Security [6]
Entity Connections to state explicitly [priority]:
- Online Casino → was launched → in 2026 [7]
- Players → must be → legally permitted to gamble where they live [6]
- Gambling Licence → is held by → the operator [8]
- Operator → protects → accounts, payments and personal data with technical and organisational safeguards [7]
Summary: Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected.
Copywriter Notes: This block covers several topics in ONE continuous section without sub-headings, in this order, each topic in proportion to its share of the block. (1) About the Casino: Give the launch year (2026) and the account currencies from the Brand Information (including SGD). Where "Longfu 88 Official Site" is used, put it in a natural phrase, for example that players should use the Longfu 88 Official Site address and not look-alike pages (this is advice, not a fact claim about domains). Explain who may play: 18+, legally permitted to gamble in the place of residence, one personal account, no third-party payment methods. NEVER say or imply that the casino is licensed, legal or approved in Singapore; the licence named in the Brand Information is the only licence statement. (2) Licence, Operator and Data Protection: Lead with the licence: jurisdiction Costa Rica, the operator named there (Lumina) and the registration number, exactly as in the Brand Information. The operator also acts as the data controller; the data protection officer is reached at the e-mail given in the privacy policy (print it only if it fits; it contains the tracked keyword "Longfu88", which then counts). Explain who the data may be shared with (payment service providers, identity verification providers, technology providers, regulators and law enforcement when required) and which rights the player has (access, rectification, erasure where legally permitted, restriction, objection, portability, withdrawal of consent). The account holder is responsible for safeguarding credentials. Where "casino Longfu88" is used, it sits in a natural sentence about the licence. NEVER say or imply that the casino is licensed, legal or approved in Singapore; the licence named in the Brand Information is the only licence statement. Do not claim an audit, eCOGRA, RNG certificate, SSL or any other certification: none is given. Do not repeat identity-check details (they have their own section). Use "Longfu88" exactly once, "casino Longfu88" exactly once and "Longfu 88 Official Site" exactly once, and no other tracked keyword.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_general.release_year: 2026
- brandinfo_general.currencies: ["EUR", "USD", "MYR", "THB", "SGD", "USDT"]
- brandinfo_privacy_policy.terms_conditions.eligibility: {"minimum_age": 18, "residency_requirements": "Players must be legally permitted to gamble in their place of residence.", "player_requirements": ["Register with accurate information", "Use only one personal account", "Do not use third-party payment methods"]}
- brandinfo_general.licences[0]: {"jurisdiction": "Costa Rica", "operator": "Lumina", "registration_number": "000-039123-R-319326-001"}
- brandinfo_privacy_policy.privacy_policy.data_controller: {"company_name": "Lumina", "contact_email": "dpo@longfu88.com", "contact_details": "support@longfu88.com"}
- brandinfo_privacy_policy.privacy_policy.security: Technical and organizational safeguards protect accounts, payments and personal information.
- brandinfo_privacy_policy.privacy_policy.data_sharing: ["Payment service providers", "Identity verification providers", "Technology providers", "Regulators and law enforcement when required"]
- brandinfo_privacy_policy.privacy_policy.data_subject_rights: ["Access", "Rectification", "Erasure where legally permitted", "Restriction", "Objection", "Portability where applicable", "Withdrawal of consent"]
- brandinfo_privacy_policy.terms_conditions.account_terms: ["The account holder is responsible for safeguarding credentials.", "The operator may suspend activity for verification or suspected abuse."]
Counting warning: the facts above contain tracked keywords "Longfu88" (x2). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 1, 'casino Longfu88': 1, 'Longfu 88 Official Site': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').
