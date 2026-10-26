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
Page intent: Singapore-focused write-up on Longfu88, the online casino, for the regular player, built as a guided walk: it begins with the fact sheet, moves through the VIP programme, weekly cashback and daily rebates, reloads and reward features, then the welcome bonus as the entry point and the sportsbook rewards, goes on to payments and withdrawal limits, the game lobby, mobile access, registration and verification, licensing and data protection, responsible play and support, and closes with pros and cons, a compact FAQ and a verdict. Voice: measured and numerate, sentences around 19 words, each paragraph running three or four sentences; after each reward say first what earns it and next what it is worth across a month of play, and set offers of one kind side by side; a call to action belongs only at the welcome bonus. The AffBulk knowledge base longfu88-new is the sole source of brand facts, while Singapore legality is something the page never asserts.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Rewards Review: Cashback, Reloads and VIP Levels for Singapore (102-130 words): A brief opening that tells what the online casino is, lists the game areas it spans, gives the launch year and states that adult players from Singapore are the audience.
b02   H2 Rewards and Brand Facts (88-112 words): A compact fact sheet of the casino: licence, operator, launch year, welcome bonus, cashback, VIP tiers, the smallest deposit, payment options, accepted currencies, support languages and contact details.
b03   H2 How the VIP Programme Pays Back (122-154 words): The VIP programme step by step: how real-money play turns into points, the five tiers, the ladder of 25 levels and what each step improves.
b04   H2 Weekly Cashback and Daily Rebates (96-122 words): Weekly cashback and live casino cashback with their VIP rates, followed by the daily rebates sorted by game category.
b05   H2 Reloads, Weekend Offers and Seasonal Drops (128-162 words): Reload offers that recur and special one-time campaigns, set out for comparison on reward, smallest deposit, wagering and validity, followed by the rules common to all.
b06     H3 Bonus Crab, Wheel of Fortune and Coin Shop (77-97 words): The playful extras inside Rewards: the Bonus Crab, Wheel of Fortune, Challenges, Collections and Coin Shop.
b07   H2 Welcome Bonus for New Accounts (133-171 words): The Casino Welcome Bonus in sequence: percentage, cap, free spins, qualifying deposit, eligible claimants, the four claiming stages and finally the two alternative first-deposit offers.
b08     H3 What the Welcome Bonus Asks in Return (102-130 words): A table of the Casino Welcome Bonus terms, then the practical effect of its exclusions.
b09   H2 Sportsbook Rewards and Markets (109-138 words): A sportsbook overview: sports and esports covered, the kinds of bet available and the live betting side.
b10     H3 Sports Bonuses, Cashback and Boosts (83-106 words): Sportsbook promotions one by one: the sport first-deposit offer, the weekly and weekend reloads, the parlay boost, early payout, cashback and the risk-free bet builder, ending on the odds requirement they all share.
b11   H2 Payments, Limits and Withdrawal Caps (133-171 words): Deposit methods in groups, the limits and crediting speed they have in common, the options meant for Singapore players and the deposit route in six steps.
b12     H3 Withdrawal Steps, Fees and Timing (122-154 words): Withdrawal start to finish: methods, the route in six steps, how long processing lasts, limits and fees that depend on circumstances.
b13   H2 Where the Rewards Are Played: the Game Lobby (242-309 words): A walk through the lobby: nine game categories, three sample slots and their RTP, the live area and its exclusive baccarat, the other categories and the ten providers.
b14   H2 Mobile Access for Regular Players (102-130 words): Mobile access: responsive pages on Android, iOS and mobile web; home-screen pinning; main account functions one tap away.
b15   H2 Registration, Login and Verification (173-219 words): Registration in five numbered steps, login and password recovery, then the moments when documents are requested, which ones, and the review time.
b16   H2 Licence, Operator and Data Safety (173-219 words): Launch date, account currencies and eligibility open the section; the licence, the operator and data/account protection follow.
b17   H2 Responsible Gambling and Limits (102-130 words): Age limit, self-exclusion and account closure through e-mail requests, self-assessment questions and where to find outside help.
b18   H2 Customer Support (70-90 words): Support: which channels exist, their hours and the languages they work in.
b19   H2 Pros and Cons for Regular Players (53-67 words): Pros and Cons in a table, assembled only from facts that earlier sections already state.
b20   H2 Questions About Rewards (194-246 words): Quick answers on VIP levels, weekly cashback, claiming the bonus, wagering and the minimum deposit.
b21   H2 Verdict for Regular Players (96-122 words): A short verdict: the kind of player this suits, what to check ahead of a first deposit, closing with a responsible-gambling note.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Rewards Review: Cashback, Reloads and VIP Levels for Singapore
Longfu88 runs as an online casino, live since 2026, that keeps live dealer tables, crash and instant titles, fast games, lottery, P2P games, fishing, table games, jackpots and slots in one lobby, with a sportsbook running next to them. The platform brings together lottery, sports betting, live dealer games and casino games under a single account, so a player moves between them without opening anything new. Sign-up is open to people from 18 years of age. The text is written for readers based in Singapore who wish to weigh up the offer before a first deposit. Ahead come mobile access, payments, the game lobby, promotions, licensing, key facts and safer play.

## Rewards and Brand Facts
| Field | Content |
|---|---|
| Licence | Costa Rica jurisdiction, number 000-039123-R-319326-001, holder Lumina |
| Operator | Lumina |
| Launch year | 2026 |
| Welcome bonus | 188% match with a €2,088 cap and 18 free spins |
| Cashback | Up to 10% of weekly net casino losses, capped at €6,988 |
| VIP programme | Bronze, Silver, Gold and Platinum, topped by Diamond |
| Minimum deposit | €10 across the casino |
| Payment methods | PayNow, Bitcoin, Mastercard, USDT (TRC20), Visa, Bank Transfer |
| Currencies | USD, SGD, MYR, THB, USDT, EUR |
| Support languages | Thai, Malay, English, Vietnamese, Indonesian, Simplified Chinese |
| Support | E-mail support@longfu88.com and 24/7 live chat |

## How the VIP Programme Pays Back
Play with real money on eligible games fills a VIP points meter, and each threshold on that meter opens the next numbered level. VIP points carry a player up the ladder of 25 reward levels, which are grouped into five tiers: Bronze opens the climb, Silver, Gold and Platinum follow, and Diamond closes it. The Longfu88 VIP Program therefore favours steady activity over one large session. Higher VIP levels raise cashback and withdrawal limits, and from level 4 a personal VIP manager is assigned along with personalised offers. Selected steps are listed below, starting from the top. Both the sums and the caps shift with the player's level and with the account currency, and the programme terms may change.

| Level | Points | Reward | Cashback | Withdrawal limit |
|---|---|---|---|---|
| 25 | 5,500 | €980 | 10% | €147,000 |
| 20 | 3,600 | €637 | 8% | €117,600 |
| 15 | 2,100 | €392 | 6% | €88,200 |
| 10 | 700 | €147 | 4% | €63,700 |
| 5 | 70 | €24.5 | 2% | €34,300 |
| 1 | 1 | €9.8 | 1% | €9,800 |

## Weekly Cashback and Daily Rebates
Weekly cashback pays back no more than 10% of the net losses on casino play, with a ceiling of €6,988. Each week runs from Monday 00:00 UTC to Sunday 23:59 UTC, and a player opts in once per cycle of four weeks. The money arrives in My Bonuses on the next Monday under a 10x wagering requirement, and only real-money bets enter the calculation, never bonus funds. Rates rise with the VIP tier, as the table shows. Live Casino Cashback is a separate offer at 25% up to €850. Rebates reach the account every day: P2P 0.8%, lottery 1.0%, casino 0.9% and live casino 1.0%, each needing 1x wagering.

| Tier | Percentage | Maximum |
|---|---|---|
| Bronze | 2% | €1,888 |
| Silver | 4% | €2,388 |
| Gold | 6% | €2,988 |
| Platinum | 8% | €3,988 |
| Diamond | 10% | €6,988 |

## Reloads, Weekend Offers and Seasonal Drops
Weekly offers come first below, then weekend and one-off ones.

- **Casino Weekly Reload**: from €30, 40x Free Spins winnings, 7 days, 50 Free Spins
- **Casino Weekly Crypto Reload**: from 20 USDT, 30x deposit plus bonus, 7 days, 60% up to 1,000 USDT
- **Casino Weekend Reload**: from €50, 30x deposit plus bonus and 40x Free Spins winnings, 7 days, up to €3,360 + 50 Free Spins
- **Casino Weekend Crypto Reload**: from 20 USDT, 30x deposit plus bonus and 40x Free Spins winnings, 7 days, 75% up to 750 USDT + 100 Free Spins
- **Casino Trick or Treat Pumpkin Bonanza**: from €20, 40x Free Spins winnings, 7 days, up to 100 Free Spins
- **Casino Double Fortune: One-Day Reload Special**: from €30, 30x deposit plus bonus, 24 hours, 50% up to €500
- **Casino Dragon Quest**: from €20, 30x promotional credit, 7 days, €10 bonus credit

Each offer is activated in My Bonuses, with one claim per promotional period. Promotions rule out a second casino bonus active at the same time, and a €5 stake ceiling per spin applies to bonus funds.

### Bonus Crab, Wheel of Fortune and Coin Shop
In the rewards area, the Bonus Crab asks a player to pick a crab, and the prize expires after 7 days, with 30x wagering on bonus credit or 40x on Free Spins winnings. The Wheel of Fortune turns for Coins or an eligible spin, also lasting 7 days under 30x. Challenges and Collections sit alongside, since completed tasks pay coins, free spins and bonus credits. Coins can be traded at the Coin Shop for rewards such as bonus credit of up to €4,500, priced per item. Wagering terms may follow any reward.

## Welcome Bonus for New Accounts
The Casino Welcome Bonus at Longfu88 bundles 18 Free Spins with bonus credit of 188%, up to €2,088. It targets freshly registered players making a first qualifying deposit, with one welcome bonus per account. The deposit for this package must reach €50, a different figure from the €10 that the casino as a whole sets as the lowest. Four stages follow:

- Open the account and complete the compulsory personal details.
- Fund it through a first payment that satisfies the qualifying rule.
- Before the first wager, the Casino Welcome Bonus has to be activated in My Bonuses.
- Wager on eligible casino games and clear the requirement before the bonus lapses.

The route carries no Longfu88 promo code: activating the offer after the qualifying payment is what delivers the bonus, and no stage asks for a code. Claim the Casino Welcome Bonus once the first deposit is in. Two other first-deposit options sit next to it: the Live Casino Welcome Bonus (125% up to €888, €30 minimum deposit) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, 50 USDT minimum deposit).

### What the Welcome Bonus Asks in Return
The terms of the Casino Welcome Bonus come down to five conditions.

| Condition | Value |
|---|---|
| Wagering | Multiple of 25 on deposit and bonus together |
| Free spin play | 40x applied to Free Spins winnings |
| Maximum bet | €22.5 per spin |
| Maximum cashout | Ceiling of 5x the initial bonus amount |
| Validity | 10 days counted from activation |

These exclusions have a direct effect on play. Only one promotional bonus may be live at once, and Neteller and Skrill are barred as funding methods. Eligibility may be voided by a cash-out request that precedes the claim or lands mid-promotion. If the promotion is cancelled, bonus funds are lost along with winnings still waiting to be converted, and account verification may come before any bonus winnings are paid.

## Sportsbook Rewards and Markets
Longfu88 runs a sportsbook that spans nine disciplines: virtual football, football, cricket, badminton, tennis, table tennis, volleyball, basketball and esports. Football and esports share one account with the racket and net sports, so traditional and virtual fixtures sit in the same place. Readers who want to see current events can look for the Longfu sports area on the website. Seven bet types are offered: live, outrights, totals, handicap, single, accumulator and Bet Builder. Bet Builder joins several selections from one match into a single wager, while the accumulator chains separate matches. Live betting brings in-play markets and live odds, so prices follow the action as it unfolds. Which events appear and how deep the markets run can depend on the jurisdiction.

### Sports Bonuses, Cashback and Boosts
The Sport First Deposit Bonus can be worth up to €1,888 at a 100% match, from €50, with 8x wagering over 30 days. Sport Weekly and Weekend Reload Bonuses ask for €50 and 8x too, at 50% up to €2,500 and €3,750, each with a crypto version. Beyond deposits come the 2 Goals Ahead early payout, the Unlimited Sports Rebate at 0.70%, Bet Builder Risk Free (50% of the stake back, up to €250), the Parlay Boost (up to 100% extra on parlays of three or more legs) and weekly cashback of 10% on net losses, capped at €2,500. Qualifying bets need odds of 2.00 or more on singles and 1.50 on each accumulator selection.

## Payments, Limits and Withdrawal Caps
Deposits can be made through several families of methods, grouped below with the currencies they handle.

| Method type | Examples | Currencies |
|---|---|---|
| European options | Giropay, Sofort | EUR |
| Wallets | Neteller, Skrill | EUR |
| Coins | Bitcoin, Ethereum, Litecoin, USDC, USDT (TRC20, ERC20, BEP20) | BTC, ETH, LTC, USDC, USDT |
| Cards | Visa, Mastercard | SGD, VND, MYR, IDR |
| Bank transfer | Bank Transfer | IDR, MYR, VND |
| For Singapore | OCBC Bank, DBS Bank, PayNow, PayNow QR | SGD |

Every method shares a range of €10 to €5,000 per transaction, and deposits reflect in the balance after a wait of 1-2 minutes. The casino keeps processing free of charge, yet the payment provider or the network can add a fee on top. Limits differ by method, currency and country, while the welcome bonus is not triggered by a Neteller or Skrill deposit. Six steps make up the route: logging in to the Longfu88 account, entering the Deposit section of the cashier, choosing a method together with a currency or network it supports, typing in the amount and the payment information, confirming the payment, and waiting for the funds to land in the playable balance.

### Withdrawal Steps, Fees and Timing
Payout channels are bank transfer, Mastercard, Visa, USDT on three networks, Bitcoin, Ethereum, Litecoin, Touch'n Go, DANA, MoMo, DBS Bank and Online Banking, each between €20 and €5,000. On the casino side, the Lngfu88 withdrawal time is no more than 3 business days. Card, crypto and wallet requests take 1-3 business days, while a bank transfer afterwards spends 3-5 more business days at the bank. The casino charges no standard fee, but providers and networks might. A 10% commission (at least €2.25) can apply when the deposit was not turned over, and a 15% charge to some payouts tied to card or bank funding. Identity checks (see the verification section) may hold a payout.

1. Log in at Longfu88 and click Withdrawal.
2. Pick a destination or a supported payment method.
3. Enter the amount and the recipient: blockchain address, bank or wallet.
4. Review the request and confirm its submission.
5. Finish the identity and payment-method checks if a prompt appears.
6. Await the casino review, followed by settlement via the bank or network.

## Where the Rewards Are Played: the Game Lobby
Longfu88 Casino sorts its lobby into nine game categories: slots, lottery, fishing, jackpots, live dealer games, P2P games, table games, crash and instant games, and fast games. This online casino therefore covers lottery, crash games, P2P, fast games, fishing, jackpots, table games, live dealer games and slots under one account. Slots tend to be the first stop for regulars, and three of them make the figures concrete. Wanted Dead or a Wild, built by Hacksaw Gaming, carries RTP 96.38%, very high volatility and 12,500x as the maximum multiplier. Sweet Bonanza by Pragmatic Play shows 96.48% RTP, high volatility and 21,175x at the top end. A second Pragmatic Play slot, Gates of Olympus, is rated at RTP 96.50% with a 5,000x maximum multiplier and high volatility. RTP stands for return to player, the portion of wagers returned to players when a slot is judged over a long run of rounds, and volatility describes how evenly or unevenly payouts are spread.

The live dealer area forms one category of the lobby. Its exclusive title is Longfu88 Baccarat, a version of the card game that can be played live or at a table. Evolution and SA Gaming run live studios and sit among the providers. The other categories each suit a different habit. Fishing games are arcade rounds where the player takes aim at targets on the screen. In P2P games, players compete with one another and not with the house. Crash and instant games resolve within seconds, so a session can be quick. Lottery means picking numbers for a draw, table games cover the familiar card and wheel formats, and fast games keep every round brief. A visitor to Longfu 88 reaches all of these areas from the same account.

Game providers deliver table games, live games and slots for the casino. Longfu 88 Casino works with ten of them: Skywind, Yggdrasil, NetEnt, Betsoft, Red Tiger, Evolution, SA Gaming, Hacksaw Gaming, Pragmatic Play and Big Time Gaming.

## Mobile Access for Regular Players
The casino works as a mobile-friendly website: its responsive pages are delivered through whichever browser a smartphone or tablet carries, with Android, iOS and mobile web all covered. What is called the Longfu88 app here is the shortcut version of that site pinned to the home screen, which gives direct access to the casino and the sportsbook. On iOS, the shortcut takes four steps:

1. Open Longfu88 in Safari.
2. Tap Share.
3. Select Add to Home Screen.
4. Tap Add.

On Android, the route runs along similar lines:

1. Open Longfu88 in Chrome.
2. Open the browser menu.
3. Select Add to Home screen.
4. Confirm the shortcut.

Once the icon is on the screen, bonuses, deposits, withdrawals, account login, the sportsbook and the casino are each one tap away.

## Registration, Login and Verification
Signing up needs an email address and five steps. Each person is allowed a single personal account.

1. Open Longfu88 and click Register.
2. Type in an email and invent a password.
3. Confirm adulthood, then accept both the Privacy Policy and the Terms and Conditions.
4. Enter the residential address along with other personal data requested.
5. Finish any email confirmation that is asked for, then select Create Account.

Registration collects date of birth, email, legal name, password and residential address. Reaching 18 is mandatory, in addition to being of lawful gambling age under the rules of the player's home country. Returning visitors use the Longfu88 login: Login, then the registered email and password, then the security check. Lost passwords are handled through Forgot Password on the sign-in form: type the registered email, then open the link that arrives in the inbox.

Documents are requested if the account or payment method is altered, if a transaction looks odd or large, and ahead of every withdrawal. The checklist:

- Address: utility bill or bank statement
- Identity: driving licence, national identity card or passport
- Payment method: ownership evidence for the bank, card or wallet used
- Source of funds, when requested

A requested set has to be submitted within 30 days, and reviewers need up to 10 days once it is complete. Withdrawals can be paused while checks are open, and a failed check can lead to declined transactions or limits on the account.

## Licence, Operator and Data Safety
Since its 2026 launch, the online casino has let players keep accounts in USD, SGD, MYR, THB, USDT or EUR. Anyone planning to register should visit only the genuine Longfu 88 Official Site and ignore lookalike pages. Four conditions define who may play: the person is at least 18, gambling is legal where he or she is located, a single personal account is used, and every payment method is registered to the account holder. Players may gamble only with legal permission under the law of their home jurisdiction.

Turning to the licence, casino Longfu88 operates under a Costa Rica licence with registration number 000-039123-R-319326-001, which is in the name of the operator Lumina. Lumina doubles as data controller, with its data protection officer contactable via dpo@longfu88.com. Technical and organisational safeguards cover accounts, payments and personal information. Recipients of data can include technology providers, payment service providers, identity verification providers and, where the law demands it, regulators and law enforcement authorities. A player's rights cover access, rectification, objection, restriction, withdrawal of consent, erasure where legally permitted and portability where applicable. The account holder is responsible for keeping login credentials safe, and the operator may freeze activity in the event of suspected abuse or pending verification.

## Responsible Gambling and Limits
Only adults of 18 years and above may hold an account, and betting in places where it is unlawful is barred. Anyone seeking to pause play can request self-exclusion through an e-mail to customer support at support@longfu88.com. For the period agreed, account access and gambling are limited, and the measure starts within 24 hours of the request being processed. Closing an account is likewise handled by customer support, in four moves: reach out to the team, state the terms and account details wanted, allow the casino to cut off access, and look for independent assistance when suitable. Self-assessment questions help players recognise signs of gambling-related harm. Outside help comes from these organisations:

- Gamblers Anonymous
- Gambling Therapy
- GamCare

This page is no replacement for independent help.

## Customer Support
There are two ways to contact the team. Live chat is staffed at all hours, 24/7, a good fit for matters that arise during play, for example a pending deposit or a bonus condition. E-mail goes to support@longfu88.com and fits matters that benefit from a written trail, for instance documents or an account closure request. Customer support answers customers in Malay, English, Simplified Chinese, Vietnamese, Thai and Indonesian, so a player can write in the language that feels most familiar.

## Pros and Cons for Regular Players
| Pros | Cons |
|---|---|
| Deposits start at €10 | Bank withdrawals take several business days |
| Many payment options, crypto among them | A turnover shortfall can bring a 10% or 15% commission |
| Cashback each week reaching 10% | Welcome bonus wagering of 25x after a €50 deposit |
| 25-level VIP programme and 24/7 live chat | Verification can delay the first payout |

---

## BLOCK BRIEF
Block: b20, H2 "Questions About Rewards" (under H1 "Longfu88 Casino Rewards Review: Cashback, Reloads and VIP Levels for Singapore")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 194-246 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 246, but never beyond 270 words.
Format: list. Visual Elements: Bulleted/numbered list — 7 of 7 lists on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 bonus": exactly 1 time(s)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu": 0 (do not use)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Frequently Asked Questions [8]
- Vip levels [6]
- Weekly cashback [6]
- Claiming the bonus [6]
- Wagering [6]
Entity Connections to state explicitly [priority]:
- Frequently Asked Questions → answer short questions on → VIP levels, weekly cashback, claiming the bonus, wagering and minimum deposit [6]
Summary: Quick answers on VIP levels, weekly cashback, claiming the bonus, wagering and the minimum deposit.
Copywriter Notes: Exactly five bullets, ordered as follows, each one a bold question and a reply of 20-30 words. Bullet 1, VIP levels: qualifying real-money wagering produces VIP points that unlock 25 numbered levels; the answer contains "Longfu88" verbatim once. Bullet 2, Casino Weekly Cashback: up to 10% of the week's net casino losses comes back, limit €6,988, opt-in required, arriving in My Bonuses on Monday where activation is needed. Bullet 3, Casino Welcome Bonus claim: activate it in My Bonuses once €50 has been deposited as the qualifying first deposit; the question includes "Longfu88 bonus" verbatim, once; no promo-code stage exists in the listed route. Bullet 4, wagering on the welcome bonus: 25x applies to the deposit and the bonus taken together, 40x to free spin winnings, 10 days to complete, maximum bet €22.5 per spin. Bullet 5, smallest deposit: for the Casino Welcome Bonus it is €50; for the casino in general it is €10. In answers the brand "Longfu88" is fine; in questions it is not. The page has no questions except these bullets. Use "Longfu88" exactly once and "Longfu88 bonus" exactly once, and no other tracked keyword.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_general.minimum_deposit: €10
- brandinfo_welcome.welcome_bonus.claiming_procedure: ["Fill in the mandatory personal details while registering the account.", "Next, the initial deposit, which has to qualify, is paid in.", "Activating the Casino Welcome Bonus inside My Bonuses must precede all wagering.", "Finishing the wagering prior to expiry requires play on eligible casino games."]; keep exactly: casino welcome bonus, my bonuses
- brandinfo_loyalty.loyalty_vip_program.progression: Points in the VIP scheme are earned from eligible real-money gameplay, and they open numbered reward levels.; keep exactly: vip
- brandinfo_promotions.other_bonuses[9].reward: Up to 10% of weekly net casino losses, capped at €6,988
- brandinfo_promotions.other_bonuses[9].crediting: Crediting takes place on Monday, into My Bonuses, and activation is a requirement.; keep exactly: my bonuses, monday
- brandinfo_welcome.welcome_bonus.minimum_deposit: €50
- brandinfo_welcome.welcome_bonus.wagering_requirement: 25x the deposit plus bonus amount
- brandinfo_welcome.welcome_bonus.free_spins_wagering: 40x Free Spins winnings
- brandinfo_welcome.welcome_bonus.validity: 10 days from activation
- brandinfo_welcome.welcome_bonus.maximum_bet: €22.5 per spin
