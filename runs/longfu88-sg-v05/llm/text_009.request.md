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

## Reloads and Cashback
Longfu88 runs seven reload and seasonal offers:

| Offer | Reward | Validity | Min. deposit | Wagering |
|---|---|---|---|---|
| Casino Double Fortune: One-Day Reload Special | 50% up to €500 | 24 hours | €30 | 30x deposit plus bonus |
| Casino Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 7 days | 20 USDT | 30x deposit plus bonus, 40x Free Spins winnings |
| Casino Dragon Quest | €10 bonus credit | 7 days | €20 | 30x promotional credit |
| Casino Weekly Reload | 50 Free Spins | 7 days | €30 | 40x Free Spins winnings |
| Casino Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | 7 days | €20 | 40x Free Spins winnings |
| Casino Weekly Crypto Reload | 60% up to 1,000 USDT | 7 days | 20 USDT | 30x deposit plus bonus |
| Casino Weekend Reload | Up to €3,360 + 50 Free Spins | 7 days | €50 | 30x deposit plus bonus, 40x Free Spins winnings |

Each one is switched on inside My Bonuses, takes one claim per period, excludes another casino bonus and caps a spin stake at €5.

Casino Weekly Cashback returns at most 10% of net losses from casino play in a week, up to €6,988. Cycles begin Monday 00:00, ending Sunday 23:59 UTC. Opting in once covers four weeks, while Monday's credit in My Bonuses carries 10x wagering. Rates by VIP tier:

| Tier | Diamond | Platinum | Gold | Silver | Bronze |
|---|---|---|---|---|---|
| Rate | 10% | 8% | 6% | 4% | 2% |
| Cap | €6,988 | €3,988 | €2,988 | €2,388 | €1,888 |

Live Casino Cashback adds 25% up to €850. Daily rebates: P2P 0.8%, casino 0.9%, lottery 1.0% and live casino 1.0%, each at 1x wagering.

### Rewards Area
The Rewards area works like a small arcade. Challenges set qualifying tasks that bring in Coins, free spins or bonus credits, while Collections pay out Coins or bonus rewards for completed sets. Coins go towards purchases in the Coin Shop, where every item has its own price and bonus credits reach as much as €4,500. Wheel of Fortune takes an eligible spin or Coins per turn, with 7 days and 30x attached. Bonus Crab hides a prize behind each claimed pick: 7 days, 30x on bonus credit, 40x on free spin winnings. Separate wagering terms may apply.

## VIP Programme
The Longfu88 VIP Program runs on points. Eligible real-money play builds up VIP Points, which unlock each numbered reward level in turn. Twenty-five levels are grouped into five tiers: Diamond and Platinum at the top, Gold, Silver and Bronze below. Higher VIP Levels increase the cashback percentage together with the withdrawal caps, while a Personal VIP Manager and personalised offers appear starting at level 4. Six sample levels show the climb:

| Level | Points needed | Withdrawal cap | Cashback rate | Level reward |
|---|---|---|---|---|
| 25 | 5,500 | €147,000 | 10% | €980 |
| 20 | 3,600 | €117,600 | 8% | €637 |
| 15 | 2,100 | €88,200 | 6% | €392 |
| 10 | 700 | €63,700 | 4% | €147 |
| 5 | 70 | €34,300 | 2% | €24.5 |
| 1 | 1 | €9,800 | 1% | €9.8 |

The currency matters as well as the level, since rewards and withdrawal caps differ between the two, and the perks of each level may change under programme rules.

## Sports Betting
Longfu88 gives the casino a sportsbook counterpart. The Longfu sports section takes bets on basketball, volleyball, esports, badminton, cricket, football, virtual football, table tennis and tennis, so the choice stretches from team games to racket sports and gaming tournaments. Seven bet types shape the slip: handicap, totals, single, outrights, accumulator, Bet Builder and live. A single backs one outcome, an accumulator ties several selections into one stake, and a Bet Builder combines markets of one match. Live betting adds in-play markets with live odds once a match is underway. Jurisdiction matters here: the events and markets on screen may vary from one country to another.

### Sports Bonuses
| Offer | Min. deposit | Wagering | Reward |
|---|---|---|---|
| Sport Weekly Reload Bonus | €50 | 8x | 50% up to €2,500 |
| Sport First Deposit Bonus | €50 | 8x | 100% up to €1,888 |
| Sport Weekend Reload Bonus | €50 | 8x | 50% up to €3,750 |

Crypto equivalents are available. A Bet Builder Risk Free stake comes back at 50% up to €250, while Parlay Boost needs three legs for up to 100% extra, and 2 Goals Ahead settles early. Unlimited Sports Rebate stands at 0.70%. Sports Cashback gives back 10% of weekly net losses, ceiling €2,500. Qualifying odds start at 2.00 on singles and 1.50 per accumulator selection. Cashed-out or voided bets do not qualify.

---

## BLOCK BRIEF
Block: b15, H2 "Payments: Deposits and Withdrawals" (under H1 "Longfu88 Casino Games, Bonuses and Payments: Singapore Review")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 242-309 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 309, but never beyond 339 words.
Format: paragraph + list + table. Visual Elements: Bulleted/numbered list — 4 of 8 lists on the page; Table — 6 of 6 tables on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": exactly 1 time(s)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 4 time(s) in this block (one per 50 words)
- "Longfu": 0 (do not use)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Payment Methods [10]
- Bank Transfer [7]
- Cryptocurrency [7]
- E-wallets [6]
- Deposit Limits [7]
- Processing Speed [6]
- Withdrawal Time [10]
- Withdrawal Methods [8]
- Minimum Withdrawal [7]
- Withdrawal Fees [7]
Entity Connections to state explicitly [priority]:
- Deposits → show up → after 1-2 minutes [8]
- Casino → does not apply → any processing fee to deposits, but providers or networks might still add theirs [7]
- Withdrawal → wraps up in → 3 business days or less [9]
- Bank Transfer → may need → 3-5 more business days before the funds reach the account [7]
Summary: Deposit method types with limits and credit speed in a table, followed by the deposit route; then payouts: which methods, what steps, how long and at what cost.
Copywriter Notes: Single continuous section, no sub-headings, two parts with space according to weight. First part - Deposit Methods and Limits (1): a one-line opener, then a Markdown table with the columns Method type | Examples | Currencies. Row groups: cryptocurrencies (Ethereum, Bitcoin, USDC, Litecoin and the other listed coins; USDT in its TRC20, ERC20 and BEP20 variants), European methods (Sofort, Giropay), e-wallets (Neteller, Skrill), cards (Visa, Mastercard), bank transfer, local bank and wallet options. Singapore readers should see DBS Bank, PayNow QR, OCBC Bank (SGD) and PayNow highlighted, with values as supplied. Universal for all methods: transactions between €10 and €5,000 each, credit within 1-2 minutes, and no processing fee from the casino (provider or network fees may still occur). Omit limit figures quoted per currency or per market for individual methods, as those lines place euro symbols next to local-currency sums. Limits are not fixed: they depend on the player's country, the currency and the method. Deposits through Skrill or Neteller are not eligible for the welcome bonus. Give the six deposit steps one or two sentences at most, after the table. Keep brand keywords out of the table. Second part - Withdrawals and Payout Times (2): methods to list are wallets and banking (Touch'n Go, MoMo, DANA, Online Banking, DBS Bank), crypto (USDT over three networks, Litecoin, Ethereum, Bitcoin), cards (Mastercard, Visa) and bank transfer. Withdrawal limits: €20 at the low end, €5,000 at the top; then the six steps as a NUMBERED list. Payouts to cards, crypto addresses and wallets arrive after one to three business days. A bank transfer works in two steps in sequence: the casino processes for as long as 3 business days, then the bank adds 3 to 5 business days on top. In general a withdrawal request is settled within three working days. Spelling trap: the sentence giving the processing time must contain "Lngfu88 withdrawal time" verbatim, typo included. Fees: the casino itself does not apply a standard withdrawal fee, yet fees from the blockchain or the provider may come up. If the player has wagered less than the deposit, a 10% commission with a €2.25 minimum may be charged, which is why 1x deposit turnover can be required before cashing out. A 15% rate hits certain transactions that were funded by card or bank transfer. Skip minimums quoted per market for particular methods - they, too, set euro symbols beside local currency. Refer to the verification section for ID checks that can delay a payout. Use "Longfu88" exactly once and "Lngfu88 withdrawal time" (verbatim, with this spelling) exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_deposit.deposit_methods: [{"method": "Online Banking", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €10,000 per transaction"]}, {"method": "PayNow", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €10, maximum €5,000 per transaction"]}, {"method": "BCA", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Neteller", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Sofort", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "MoMo", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €30,000 per transaction"]}, {"method": "Cardano", "currencies": ["ADA"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €309, maximum €154,949 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "THB: minimum €370, maximum €182,910 per transaction"]}, {"method": "Bank Transfer", "currencies": ["VND", "MYR", "IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €100, maximum €500,000 per transaction", "MYR: minimum €50, maximum €50,000 per transaction", "IDR: minimum €25, maximum €82,000 per transaction"]}, {"method": "QRIS", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €50,000 per transaction"]}, {"method": "Mastercard", "currencies": ["VND", "MYR", "SGD", "IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €18, maximum €3,000 per transaction", "IDR: minimum €200, maximum €30,000 per transaction", "VND: minimum €320, maximum €50,000 per transaction", "MYR: minimum €50, maximum €9,000 per transaction"]}, {"method": "Skrill", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Giropay", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "USDT (BEP20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €50, maximum €23,840 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "IDR: minimum €196, maximum €98,490 per transaction"], "network": "BEP20"}, {"method": "Zalo", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €100,000 per transaction"]}, {"method": "Litecoin", "currencies": ["LTC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "THB: minimum €370, maximum €182,910 per transaction"]}, {"method": "Ripple", "currencies": ["XRP"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €309, maximum €154,949 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "IDR: minimum €196, maximum €98,490 per transaction"]}, {"method": "USDT (ERC20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €15, maximum €7,560 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "MYR: minimum €50, maximum €23,840 per transaction"], "network": "ERC20"}, {"method": "USDC", "currencies": ["USDC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €15, maximum €7,560 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "DuitNow", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €50,000 per transaction"]}, {"method": "Touch'n Go", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €5,000 per transaction"]}, {"method": "DANA", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Mandiri", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €20, maximum €40,000 per transaction"]}, {"method": "PayNow QR", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €10, maximum €5,000 per transaction"]}, {"method": "GrabPay", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €5,000 per transaction"]}, {"method": "OCBC Bank", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €50, maximum €5,000 per transaction"]}, {"method": "USDT (TRC20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"], "network": "TRC20"}, {"method": "BNI", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €20, maximum €40,000 per transaction"]}, {"method": "OVO Wallet", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €2,000 per transaction"]}, {"method": "DBS Bank", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €50, maximum €5,000 per transaction"]}, {"method": "VietQR", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €300,000 per transaction"]}, {"method": "Bitcoin Cash", "currencies": ["BCH"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "IDR: minimum €196, maximum €98,490 per transaction"]}, {"method": "ViettelPay", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €20,000 per transaction"]}, {"method": "Visa", "currencies": ["MYR", "SGD", "VND", "IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €18, maximum €3,000 per transaction", "MYR: minimum €50, maximum €9,000 per transaction", "VND: minimum €320, maximum €50,000 per transaction", "IDR: minimum €200, maximum €30,000 per transaction"]}, {"method": "Bitcoin", "currencies": ["BTC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €45, maximum €7,560 per transaction", "MYR: minimum €145, maximum €23,840 per transaction", "VND: minimum €929, maximum €154,949 per transaction", "THB: minimum €1,100, maximum €182,910 per transaction", "IDR: minimum €590, maximum €98,490 per transaction"]}, {"method": "PromptPay QR", "currencies": ["THB"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["THB: minimum €300, maximum €200,000 per transaction"]}, {"method": "Ethereum", "currencies": ["ETH"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €50, maximum €23,840 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "SGD: minimum €15, maximum €7,560 per transaction"]}]
- brandinfo_deposit.deposit_guide: ["Players open the cashier and press Deposit.", "Longfu88 account login comes first.", "Provide the amount together with payment information.", "Allow time for the funds to reach the playable balance as credit.", "Players decide on an available method of payment, then on a supported blockchain network or currency.", "Players approve the transaction, confirming and authorizing it as the provider instructs."]; keep exactly: longfu88, payment information
- brandinfo_general.minimum_deposit: €10
- brandinfo_general.currencies: ["MYR", "EUR", "SGD", "USDT", "USD", "THB"]
- brandinfo_withdrawal.withdrawal_methods: [{"method": "Online Banking", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["MYR"], "important_terms": ["Thailand: minimum €1,945 (THB market)", "Indonesia: minimum €25,000 (IDR market)", "Singapore: minimum €80 (SGD market)", "Malaysia: minimum €50 (MYR market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "DBS Bank", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["SGD"], "important_terms": ["Malaysia: minimum €50 (MYR market)", "Thailand: minimum €1,945 (THB market)", "Indonesia: minimum €25,000 (IDR market)", "Singapore: minimum €80 (SGD market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "USDT (BEP20)", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Thailand: minimum €375 (THB market)", "Singapore: minimum €15 (SGD market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Mastercard", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["SGD", "IDR", "MYR", "VND"], "important_terms": ["Singapore: minimum €80 (SGD market)", "Indonesia: minimum €25,000 (IDR market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)", "Malaysia: minimum €50 (MYR market)"]}, {"method": "Bank Transfer", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["IDR", "MYR", "VND"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Singapore: minimum €80 (SGD market)", "Malaysia: minimum €50 (MYR market)", "Vietnam: minimum €10,000 (VND market)", "Thailand: minimum €1,945 (THB market)"]}, {"method": "USDT (ERC20)", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Vietnam: minimum €308,000 (VND market)", "Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)"]}, {"method": "Bitcoin", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["BTC"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Vietnam: minimum €308,000 (VND market)", "Thailand: minimum €375 (THB market)"]}, {"method": "Ethereum", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["ETH"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "DANA", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["IDR"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "Litecoin", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["LTC"], "important_terms": ["Vietnam: minimum €308,000 (VND market)", "Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)"]}, {"method": "Visa", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["VND", "SGD", "IDR", "MYR"], "important_terms": ["Vietnam: minimum €10,000 (VND market)", "Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Thailand: minimum €1,945 (THB market)", "Singapore: minimum €80 (SGD market)"]}, {"method": "Touch'n Go", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["MYR"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "USDT (TRC20)", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)", "Singapore: minimum €15 (SGD market)"]}, {"method": "MoMo", "minimum": "€20", "maximum": "€5,000", "fee": "A fee of 10%, minimum €2.25, can be applied if rollover is inadequate, and some card-funded or bank-funded transactions can be charged 15%. The casino does not levy a standard withdrawal fee, but charges from providers and blockchains may be added.", "transaction_speed": "1–3 business days", "currencies": ["VND"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}]; keep exactly: 10, 2.25, 15
- brandinfo_withdrawal.withdrawal_guide: ["Time is needed for casino processing, plus bank or network settlement if involved, ahead of receiving funds.", "Identity verification and payment-method verification are carried out on request.", "Confirming submission follows a review of the request.", "After authentication at Longfu88, the cashier gets opened.", "Players state the amount and give details of the wallet, bank, or blockchain address receiving the funds.", "After selecting Withdrawal, a destination or payment method that is supported must be picked."]; keep exactly: longfu88
- brandinfo_privacy_policy.terms_conditions.withdrawal_terms: ["The deposit may have to be turned over at least 1x prior to withdrawing.", "Within three working days, withdrawal requests are typically dealt with.", "The operator has the option of asking for KYC documents ahead of any payment being processed.", "When funds go by bank transfer, settlement may last another 3–5 business days."]; keep exactly: 1x, 3, 5, kyc documents
- brandinfo_privacy_policy.terms_conditions.conditional_fees: ["Turnover that qualifies but stays beneath the deposit can trigger a 10% commission with a floor of €2.25.", "Casino rules provide that a 15% charge may be applied to certain transactions made by card or bank transfer."]; keep exactly: 10, 2.25, 15, bank transfer
- brandinfo_general.payment_methods.withdrawal: ["DBS Bank", "Bank Transfer", "MoMo", "USDT (ERC20)", "USDT (TRC20)", "DANA", "Ethereum", "Mastercard", "Litecoin", "Visa", "USDT (BEP20)", "Touch'n Go", "Online Banking", "Bitcoin"]
Counting warning: the facts above contain tracked keywords "Longfu88" (x2). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 1, 'Lngfu88 withdrawal time': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').
