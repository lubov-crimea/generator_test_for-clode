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
- `## BLOCK BRIEF`: the brief for your block: word count, format, keywords with exact counts, entities with priorities, entity connections, summary, copywriter notes and "Brand Information" (verbatim brand facts for exactly this section, each line is `path: value`). A block may also carry an "Internal links" line: it names pages of the same site that the block points to. Work the topic into a sentence of the body as a short phrase of at most 3 words (the page builder turns that phrase into the link); never put it in a list, a table or a heading, and never write a sentence only to carry the link.

# PRIORITIES (apply in strict order)

1. Style: natural, readable editorial text in the voice described in STYLE. A block that reads as a list of facts fails this priority.
2. Factual integrity: nothing invented, nothing promised; brand facts exactly as given in the Brand Information.
3. Hard constraints of the BLOCK BRIEF: language, keyword counts, allowed formats, word range.
4. Coverage: the summary, all entities and all entity connections.
5. Reader value and consistency with the rest of the page.

Style never overrides priority 2, the compliance rules of FACTS AND INTEGRITY or the output language. If the facts, the entities and a natural style do not fit into the word range, go over it: up to 10% above the maximum (the BLOCK BRIEF names the exact cap), never beyond. Keyword counts and formats are checked by code: meet them inside the style, not instead of it.

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

- Aim for the middle of the word range of the brief. The range counts all visible body words: sentences, list items and table cell text; it excludes the heading and markdown symbols. The minimum is binding. If the facts, the entities and a natural style need more room, you may go over the maximum by up to 10% (the BLOCK BRIEF gives the cap).
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
Page intent: Editor's take on the Longfu88 online casino for readers in Singapore. Open on the game lobby: a fact table starts the page, after it come the game categories (slots, live casino and the other game types), providers, the welcome bonus and promotions, VIP levels, sports betting, payments, registration, mobile access, licence and safety, responsible gambling, support, an FAQ and a verdict. Voice: lively, still factual. Sentences around 15 words, a "you" here and there. Describe every game category through the actions a player takes inside it. Hard numbers (RTP, volatility, multipliers) go before adjectives, and game types get contrasted with one another. Paragraphs: two to three sentences. One call to action only, attached to the welcome bonus. Facts about the brand are taken exclusively from the AffBulk knowledge base longfu88-new. Keep Singapore's legal view of the casino out of the text altogether.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Games, Bonuses and Payments: Singapore Review (96-122 words): Intro: a short identity statement for the casino, the range of game areas it covers, the launch year, and a remark that the readers are adults in Singapore.
b02   H2 Casino Facts (88-112 words): Quick-reference sheet: licence, welcome bonus, cashback, operator, year of launch, languages, currencies, payment methods, Game types, Game providers and support.
b03   H2 Game Lobby (90-113 words): Lobby size measured in categories: fast games, P2P, fishing, jackpots, lottery, crash and instant games, table games, live dealer and slots.
b04     H3 Slot Games (109-138 words): Three sample slots with provider, RTP, volatility and top multiplier.
b05     H3 Live Dealer Games (96-122 words): Live dealer corner: what players find there, the house baccarat table and the studios behind live play.
b06     H3 Table, Fishing, P2P and Lottery Games (90-113 words): Whatever remains of the lobby in one block: P2P, fishing, lottery, table games, fast games, crash and instant titles.
b07   H2 Game Providers (57-73 words): The studios behind the games, as named in the provider list.
b08   H2 Welcome Bonus for Casino Players (141-178 words): Casino Welcome Bonus in detail: percentage, cap, free spins, qualifying deposit, eligibility and the four claim steps, followed by the remaining pair of opening-deposit offers.
b09     H3 Welcome Bonus Terms (102-130 words): The Casino Welcome Bonus conditions in tabular form, with the exclusions explained in practical terms after the table.
b10   H2 Reloads and Cashback (178-228 words): Table with seven reload and seasonal promotions, after which come weekly cashback (rates by VIP tier), the live casino cashback and the daily rebates.
b11     H3 Rewards Area (77-97 words): Game-style extras inside the rewards area: the Coin Shop, Collections, Challenges, Wheel of Fortune and Bonus Crab.
b12   H2 VIP Programme (109-138 words): How the VIP scheme works: points from eligible real-money play, 25 reward levels grouped into five tiers, and the benefits that expand at each stage.
b13   H2 Sports Betting (102-130 words): Sportsbook snapshot: which sports and esports can be bet on, the bet formats, and live betting.
b14     H3 Sports Bonuses (77-97 words): Sports betting promotions: reloads weekly and on weekends, the first deposit bonus, cashback, a risk-free Bet Builder, parlay boost and early payout, and the minimum odds rule they all follow.
b15   H2 Payments: Deposits and Withdrawals (242-309 words): Deposit method types with limits and credit speed in a table, followed by the deposit route; then payouts: which methods, what steps, how long and at what cost.
b16   H2 Registration and Verification (173-219 words): Five numbered registration steps, how to log in and recover a password, followed by when documents are requested, what kinds, and how long review takes.
b17   H2 Mobile Gaming (96-122 words): Using the casino on a phone: Android, iOS and mobile web, the responsive layout, the shortcut on the home screen and what an account can do from there.
b18   H2 Licence and Security (173-219 words): Launch year, currencies and who may play first; then the licence, the operating company and the protection of personal data and accounts.
b19   H2 Responsible Gambling (96-122 words): Minimum age, how to self-exclude or close an account by e-mail, self-assessment questions and where to find help.
b20   H2 Support (70-90 words): Ways to contact support, the hours, and the languages covered.
b21   H2 Game and Account Questions (158-202 words): Brief answers about the minimum deposit, bonus claiming, crypto options, the app question and account currencies.
b22   H2 Verdict on the Casino (90-113 words): Final verdict: which readers the casino suits, what deserves a second look before the first deposit, plus a responsible-gambling note.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Games, Bonuses and Payments: Singapore Review
Longfu88 launched in 2026 as an online casino that pulls slots, dealer-led live tables, table games, jackpots, fishing, P2P and lottery draws into one lobby. Crash and instant titles, fast games and a sportsbook complete the catalogue, so a single account reaches every game area. Reels, cards and sports markets sit side by side rather than in separate corners.

This review speaks to players from Singapore, and only adults who have turned 18 at minimum should read on with a deposit in mind. The sections that follow cover the facts table, game categories, bonuses, payments, mobile play, licence details and responsible gambling, in that order.

## Casino Facts
| Feature | Summary |
|---|---|
| Licence | Costa Rica, Lumina, 000-039123-R-319326-001 |
| Welcome bonus | 188% up to €2,088 plus 18 free spins |
| Cashback | 10% of weekly net casino losses, up to €6,988 |
| Operator | Lumina |
| Launched | 2026 |
| Support languages | English, Indonesian, Simplified Chinese, Thai, Malay, Vietnamese |
| Currencies | SGD, MYR, EUR, USD, USDT, THB |
| Payment methods | PayNow, Mastercard, Visa, Bank Transfer, Bitcoin, USDT |
| Game types | Slots, Live dealer games, Table games, Fishing, P2P games, Jackpots, Lottery, Fast games, Crash & instant games |
| Game providers | Evolution, Pragmatic Play, Red Tiger, SA Gaming, Yggdrasil, Skywind, Betsoft, NetEnt, Hacksaw Gaming, Big Time Gaming |
| Support | 24/7 live chat, support@longfu88.com |

## Game Lobby
Longfu88 Casino is an online casino that holds slots, live dealer games, table games, fast games and crash games next to fishing, P2P, jackpots and lottery. On Longfu88 the size of the lobby is measured in categories rather than a headline game count, so a player picks a format first and a title second. Nine areas make up the catalogue:

- Slots
- Live dealer tables
- Table games
- Fast games
- Crash and instant titles
- P2P games
- Fishing games
- Jackpots
- Lottery draws

The sub-sections below take slots, live casino and the remaining categories one by one.

### Slot Games
Slots are the category where numbers do the talking, and three titles show the spread. Gates of Olympus from Pragmatic Play offers an RTP of 96.50% and a maximum multiplier of 5,000x at high volatility. Sweet Bonanza, also from Pragmatic Play, returns 96.48% at high volatility, yet its top multiplier climbs to 21,175x. The wildest of the three is Wanted Dead or a Wild, developed by Hacksaw Gaming: very high volatility, an RTP of 96.38% and a ceiling of 12,500x.

A quick primer for newcomers: RTP is the share of stakes a slot pays back over a very long run, while volatility describes how uneven the payouts are, with higher volatility meaning rarer but larger hits. These three games illustrate the category and are not the full catalogue.

### Live Dealer Games
Dealer-led play has its own corner at Longfu 88 Casino, where a live host runs each table and the player follows the round on screen. The house table is Longfu88 Baccarat, a game exclusive to the casino that plays like baccarat, which suits anyone who wants a familiar format at a table they will not find elsewhere. Live content also draws on studios such as Evolution and SA Gaming, both named on the provider list. The live casino therefore mixes one in-house table with the work of established studios, and the rest of the lobby, from slots to lottery, is covered in the neighbouring sections.

### Table, Fishing, P2P and Lottery Games
Beyond slots and live tables, the online casino adds on top fishing, P2P, lottery, fast games and crash games. Fishing games put the player behind an on-screen shooter, aiming at moving targets to collect rewards. P2P games set players against one another instead of against the house. Lottery means picking a ticket and waiting for the draw, with nothing to do in between.

Table games bring the classic card and wheel formats, where the player decides each bet and move. Fast games are built for short rounds that finish within moments. Crash and instant titles ask for a stake and a decision: cash out before the multiplier stops, or see the outcome at once.

## Game Providers
Game providers stand behind the slots, live tables and table games of Longfu 88, and ten studios appear on the roster. Pragmatic Play and Hacksaw Gaming are already familiar from the slot examples above, while Evolution and SA Gaming supply live play. The full set in the provider list reads as follows:

- Evolution
- Pragmatic Play
- Hacksaw Gaming
- SA Gaming
- Red Tiger
- NetEnt
- Yggdrasil
- Skywind
- Betsoft
- Big Time Gaming

## Welcome Bonus for Casino Players
The Longfu88 bonus aimed at newcomers is the Casino Welcome Bonus, a first deposit casino bonus worth 188% on the deposit up to a ceiling of €2,088, plus 18 Free Spins. Newly registered players qualify once the first deposit meets the requirement, and each account gets this welcome offer a single time. The offer carries its own minimum deposit of €50.

No Longfu88 promo code is typed anywhere: the bonus is claimed by activating it in My Bonuses after the qualifying deposit, so the process has no code entry. Four short steps lead there:

- Sign up at Longfu88 and complete the mandatory profile fields.
- Pay in the qualifying first deposit.
- Open My Bonuses and switch on the Casino Welcome Bonus, with no bets placed beforehand.
- Work through the wagering in eligible casino titles until the offer runs out.

Two further opening-deposit offers exist. Live Casino Welcome Bonus pays 125% up to €888 from a €30 deposit, whereas Casino Crypto Welcome Bonus pays 188% up to 2,888 USDT from 50 USDT. Casino Crypto Welcome Bonus is an alternative to Casino Welcome Bonus, so a first deposit goes to one or the other.

### Welcome Bonus Terms
All conditions of the Casino Welcome Bonus fit into five lines, and wagering comes first.

| Condition | Value |
|---|---|
| General wagering | 25x the deposit and bonus combined |
| Free Spins winnings wagering | 40x |
| Maximum cashout | 5x the initial bonus amount |
| Validity | 10 days from activation |
| Maximum bet | €22.5 per spin |

In practice the wagering requirement asks for turnover of 25x on deposit and bonus added together, while free spins winnings carry their own 40x. Skrill and Neteller deposits are excluded from the promotion. Stacking a second promotional bonus on top is not permitted. Asking for a withdrawal before claiming or during the bonus may void eligibility, and cancelling forfeits the bonus funds plus any winnings not yet converted. ID verification may be requested before bonus winnings are paid out.

---

## SECTION
Write the blocks b10, b11 in ONE answer, in this order. They are one continuous section of the page: the sub-sections continue the parent, so the text must flow from block to block without repeating itself. Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts.

---

## BLOCK BRIEF
Block: b10, H2 "Reloads and Cashback" (under H1 "Longfu88 Casino Games, Bonuses and Payments: Singapore Review")
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): b11 H3 "Rewards Area"
Word Count: 178-228 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 228, but never beyond 250 words.
Format: paragraph + table. Visual Elements: Table — 3 of 6 tables on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu": 0 (do not use)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Weekly Reload [9]
- Weekend Reload [8]
- Crypto Reload [7]
- One-Day Reload Special [5]
- Seasonal Promotion [5]
- Free Spins [5]
- Weekly Cashback [10]
- Live Casino Cashback [8]
- Unlimited Rebate [7]
- VIP Cashback Rates [6]
Entity Connections to state explicitly [priority]:
- Weekly Reload → credits players with → 50 free spins [7]
- Promotions → is incompatible with → another casino bonus already in progress [8]
- Weekly Cashback → returns → no more than 10% of net casino losses accumulated during the week [9]
- Rebates → arrive → every day [7]
Summary: Table with seven reload and seasonal promotions, after which come weekly cashback (rates by VIP tier), the live casino cashback and the daily rebates.
Copywriter Notes: Write it as one continuous section without sub-headings and with two parts, the first getting space according to weight. Part (1), Reloads and Seasonal Promotions: lead in with a sentence, then a Markdown table whose columns are Offer, Reward, Validity, Min. deposit, Wagering. Seven rows, values as supplied: Casino Double Fortune (one-day reload special), Casino Weekend Crypto Reload, Casino Dragon Quest (reward for verification), Casino Weekly Reload, Casino Trick or Treat Pumpkin Bonanza, Casino Weekly Crypto Reload, Casino Weekend Reload. Under the table, state the shared rules once: every offer is activated in My Bonuses; each promotional period allows one claim; no offer combines with another live casino bonus; the stake limit is €5 per spin while bonus funds are wagered. Part (2), Cashback and Rebates: Casino Weekly Cashback is worth at most 10% of the net casino losses of the week, with a €6,988 cap. Calendar: Monday 00:00 UTC opens the week and Sunday 23:59 UTC ends it; opt-in covers a four-week cycle; the payout lands in My Bonuses on Monday; wagering on the cashback is 10x. The rate depends on VIP tier: Silver 4%, Bronze 2%, Gold 6%, Diamond 10% and Platinum 8%; show tier, percentage and maximum in a small table. Live Casino Cashback adds a separate 25% up to €850. The four daily rebates fit in one sentence: P2P 0.8%, casino 0.9%, lottery 1.0% and live casino 1.0%, each at 1x wagering. Only stakes made with real money count; stakes from bonus funds do not. The tier percentages belong solely to the weekly cashback; they are distinct from the VIP level percentages. Use "Longfu88" exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_promotions.other_bonuses[2]: {"name": "Casino Weekly Reload", "type": "Weekly free spins", "reward": "50 Free Spins", "minimum_deposit": "€30", "wagering_requirement": "40x winnings from Free Spins", "validity": "7 days", "claiming_method": "Activation takes place in My Bonuses, and only once the offer's eligibility and deposit conditions are fulfilled.", "eligibility": "Players who are registered and who comply with qualification rules particular to the offer.", "important_terms": ["Each promotional period has a one-claim limit unless otherwise stated.", "Wagering bonus funds limits each spin to a €5 stake at most.", "Stacking with an active casino bonus from another offer is not permitted."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[3]: {"name": "Casino Weekly Crypto Reload", "type": "Crypto weekly reload", "reward": "60% up to 1,000 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus", "validity": "7 days", "claiming_method": "Activation takes place in My Bonuses, and only once the offer's eligibility and deposit conditions are fulfilled.", "eligibility": "Players who are registered and who comply with qualification rules particular to the offer.", "important_terms": ["Each promotional period has a one-claim limit unless otherwise stated.", "Stacking with an active casino bonus from another offer is not permitted.", "Wagering bonus funds limits each spin to a €5 stake at most."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[4]: {"name": "Casino Weekend Reload", "type": "Weekend deposit bonus", "reward": "Up to €3,360 + 50 Free Spins", "minimum_deposit": "€50", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activation takes place in My Bonuses, and only once the offer's eligibility and deposit conditions are fulfilled.", "eligibility": "Players who are registered and who comply with qualification rules particular to the offer.", "important_terms": ["Wagering bonus funds limits each spin to a €5 stake at most.", "Each promotional period has a one-claim limit unless otherwise stated.", "Stacking with an active casino bonus from another offer is not permitted."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[5]: {"name": "Casino Weekend Crypto Reload", "type": "Weekend crypto bonus", "reward": "75% up to 750 USDT + 100 Free Spins", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activation takes place in My Bonuses, and only once the offer's eligibility and deposit conditions are fulfilled.", "eligibility": "Players who are registered and who comply with qualification rules particular to the offer.", "important_terms": ["Stacking with an active casino bonus from another offer is not permitted.", "Each promotional period has a one-claim limit unless otherwise stated.", "Wagering bonus funds limits each spin to a €5 stake at most."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[6]: {"name": "Casino Double Fortune: One-Day Reload Special", "type": "One-day reload", "reward": "50% up to €500", "minimum_deposit": "€30", "wagering_requirement": "30x deposit plus bonus", "validity": "24 hours", "claiming_method": "Activation takes place in My Bonuses, and only once the offer's eligibility and deposit conditions are fulfilled.", "eligibility": "Players who are registered and who comply with qualification rules particular to the offer.", "important_terms": ["Stacking with an active casino bonus from another offer is not permitted.", "Each promotional period has a one-claim limit unless otherwise stated.", "Wagering bonus funds limits each spin to a €5 stake at most."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[7]: {"name": "Casino Trick or Treat Pumpkin Bonanza", "type": "Seasonal casino promotion", "reward": "Up to 100 Free Spins", "minimum_deposit": "€20", "wagering_requirement": "40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activation takes place in My Bonuses, and only once the offer's eligibility and deposit conditions are fulfilled.", "eligibility": "Players who are registered and who comply with qualification rules particular to the offer.", "important_terms": ["Wagering bonus funds limits each spin to a €5 stake at most.", "Each promotional period has a one-claim limit unless otherwise stated.", "Stacking with an active casino bonus from another offer is not permitted."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[8]: {"name": "The Dragon Quest campaign carries the tagline Get Verified and Get Extra", "type": "Verification reward", "reward": "€10 bonus credit", "minimum_deposit": "€20", "wagering_requirement": "30x promotional credit", "validity": "7 days", "claiming_method": "Activation takes place in My Bonuses, and only once the offer's eligibility and deposit conditions are fulfilled.", "eligibility": "Participation is open to those who carry out requested account verification in the course of the campaign.", "important_terms": ["Each promotional period has a one-claim limit unless otherwise stated.", "Wagering bonus funds limits each spin to a €5 stake at most.", "Stacking with an active casino bonus from another offer is not permitted."]}; keep exactly: 5, dragon quest, get verified and get extra, my bonuses
- brandinfo_promotions.other_bonuses[9]: {"name": "Casino Weekly Cashback", "type": "Casino cashback", "reward": "Up to 10% of weekly net casino losses, capped at €6,988", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "minimum_cashback": "€4.5", "opt_in": "Active accounts can be renewed without action once a four-week cycle has been opted into.", "crediting": "A credit arrives in My Bonuses on Monday, but activation is still required.", "wagering_requirement": "10x cashback before withdrawal", "cashback_by_vip": [{"level": "VIP Bronze", "percentage": 2, "maximum": "€1,888"}, {"level": "VIP Silver", "percentage": 4, "maximum": "€2,388"}, {"level": "VIP Gold", "percentage": 6, "maximum": "€2,988"}, {"level": "VIP Platinum", "percentage": 8, "maximum": "€3,988"}, {"level": "VIP Diamond", "percentage": 10, "maximum": "€6,988"}], "important_terms": ["The count takes in winnings and bets placed in the casino with real money, and nothing from bonus funds.", "Expiry applies to weekly cashback that is left unactivated beyond the claim window."]}; keep exactly: my bonuses, monday
- brandinfo_promotions.other_bonuses[10]: {"name": "Live Casino Cashback", "type": "Live casino cashback", "reward": "25% up to €850", "minimum_cashback": "€4.5", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "crediting": "Players have to opt in and activate the credit that lands in My Bonuses on Monday.", "wagering_requirement": "10x credited cashback", "important_terms": ["Only eligible Live Casino games feed into it, using real-money stakes reduced by winnings.", "Cashback is worked out without any bonus balances."]}; keep exactly: my bonuses, monday, live casino
- brandinfo_promotions.other_bonuses[11]: {"name": "Unlimited Casino Rebate", "type": "Rebate", "rebate_percentage": 0.9, "calculation": "Only settled bets made with real money count, provided they relate to the relevant game category.", "crediting": "Rewards balance gets topped up with the rebate daily.", "wagering_requirement": "1x credited rebate", "eligibility": "Those who hold a registration and have qualifying wagers that are settled."}
- brandinfo_promotions.other_bonuses[12]: {"name": "Unlimited Live Casino Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Only settled bets made with real money count, provided they relate to the relevant game category.", "crediting": "Rewards balance gets topped up with the rebate daily.", "wagering_requirement": "1x credited rebate", "eligibility": "Those who hold a registration and have qualifying wagers that are settled."}
- brandinfo_promotions.other_bonuses[13]: {"name": "Unlimited P2P Rebate", "type": "Rebate", "rebate_percentage": 0.8, "calculation": "Only settled bets made with real money count, provided they relate to the relevant game category.", "crediting": "Rewards balance gets topped up with the rebate daily.", "wagering_requirement": "1x credited rebate", "eligibility": "Those who hold a registration and have qualifying wagers that are settled."}
- brandinfo_promotions.other_bonuses[14]: {"name": "Unlimited Lottery Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Only settled bets made with real money count, provided they relate to the relevant game category.", "crediting": "Rewards balance gets topped up with the rebate daily.", "wagering_requirement": "1x credited rebate", "eligibility": "Those who hold a registration and have qualifying wagers that are settled."}

---

## BLOCK BRIEF
Block: b11, H3 "Rewards Area" (under H2 "Reloads and Cashback")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 77-97 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 97, but never beyond 106 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu": 0 (do not use)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Bonus Crab [8]
- Wheel of Fortune [7]
- Challenges [6]
- Collections [5]
- Coin Shop [6]
Entity Connections to state explicitly [priority]:
- Coins → go towards purchases in → the Coin Shop [7]
- Challenges → bring in → Coins, free spins or bonus credits [6]
Summary: Game-style extras inside the rewards area: the Coin Shop, Collections, Challenges, Wheel of Fortune and Bonus Crab.
Copywriter Notes: Treat five features briefly, with one or two short sentences for each. Coin Shop: spend Coins on rewards, bonus credits worth as much as €4,500 among them; every item has its own price and extra wagering might attach. Wheel of Fortune: an eligible spin or Coins required, 7 days, 30x. Bonus Crab: picks that you claim reveal a crab reward; valid 7 days; 30x wagering on bonus credit, 40x on free spin winnings. Challenges and Collections are in the Rewards area. Mention that rewards can have separate wagering terms. Use no tracked keyword in the body of this block.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_promotions.gamification_features: [{"name": "Wheel of Fortune", "mechanics": "To rotate a prize wheel, one spends an eligible spin or else Coins.", "access": "Rewards area", "rewards": ["Free Spins", "Bonus credits", "Coins"], "validity": "7 days", "wagering_requirement": "30x bonus awards"}, {"name": "Collections", "mechanics": "Redemption applies to completed sets, with the campaign items gathered by completing qualifying activity.", "access": "Rewards > Collections", "rewards": ["Coins", "Bonus rewards"], "validity": "Campaign-specific"}, {"name": "Bonus Crab", "mechanics": "Picks that qualify can be claimed, and they open a crab reward showing a casino prize.", "access": "The rewards area covers free picks that qualifying activity may grant.", "rewards": ["Free Spins", "Bonus credits", "Coins"], "validity": "7 days after reward assignment", "wagering_requirement": "30x awarded bonus credit; 40x winnings from Free Spins"}, {"name": "Coin Shop", "mechanics": "Coins that were earned are swapped for rewards at the Shop.", "access": "Rewards > Shop", "rewards": ["Reward items and bonus credits up to €4,500"], "important_terms": ["Item by item, coin prices and what prizes are available are different.", "Rewards might be subject to wagering requirements that are separate."]}, {"name": "Challenges", "mechanics": "Unlocking the listed rewards depends on completing qualifying gambling tasks.", "access": "Rewards > Challenges", "rewards": ["Free Spins", "Coins", "Bonus credits"], "validity": "As shown for each challenge"}]; keep exactly: rewards area, coins
