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
Page intent: Singaporean readers who search by brand name want to see everything before they sign up, so this extended Longfu88 casino review is ordered like an actual visit: it opens with a facts grid, moves on to the welcome offer and what it demands, then reload deals, cashback, the rewards area, the VIP scheme and sports betting, then account creation and verification, depositing and cashing out, the lobby and its studios, phone access, licence and who may play, safe-play tools, contact options, a pros-and-cons grid, an FAQ about bonuses and payouts, and a brief verdict. The voice is businesslike and comparative; each paragraph runs to three or four sentences of about 18 words, and every bonus figure is introduced together with the condition tied to it, built as context, then consequence, then contrast. Calls to action are limited to three spots: the welcome bonus, the weekly cashback and the sportsbook offer. Every claim about the brand comes from AffBulk's knowledge-base record longfu88-new, and the casino's legal position under Singapore law is not discussed at all.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Review: Bonuses, Games and Payments for Singapore (109-138 words): A brief opening: what type of casino this is, how wide its gaming offer is, when it launched, and that the page speaks to adult players based in Singapore.
b02   H2 Casino Information (88-112 words): The casino's quick-reference card: welcome bonus, wagering, lowest deposit, cashback, licence, operator, year of launch, supported currencies and languages, payment methods and the support contact.
b03   H2 The Casino Welcome Bonus (146-187 words): A full look at the Casino Welcome Bonus: its match percentage, cap, free spins and qualifying deposit; the eligible players; the four claiming steps; and two rival first-deposit packages.
b04     H3 Wagering, Validity and Maximum Bet (109-138 words): The wagering and cashout conditions of the Casino Welcome Bonus in a table, then the exclusions explained in terms of what they mean in play.
b05   H2 Reload Offers and Seasonal Campaigns (128-162 words): Repeating reload offers and one-off seasonal campaigns in a single comparison grid covering reward, minimum deposit, wagering and validity, then the terms that apply across the set.
b06     H3 Weekly Cashback and Daily Rebates (83-106 words): Weekly cashback and live casino cashback, the tier-based rates that sit behind them, and the daily rebate for each game category.
b07     H3 Bonus Crab, Wheel of Fortune and the Coin Shop (77-97 words): The entertainment side of the Rewards area: the Coin Shop, Collections, Challenges, the Wheel of Fortune and Bonus Crab.
b08   H2 VIP Programme: Points, Levels and Limits (115-146 words): Inside the VIP programme: points from real-money play, a Diamond-to-Bronze tier structure, numbered reward levels up to 25 and the benefits that grow along the way.
b09   H2 Sportsbook Offer: Markets and Bonuses (109-138 words): What the sportsbook offers: the covered sports and esports, the available bet types and live betting.
b10     H3 Sport Bonuses, Cashback and Boosts (83-106 words): Sports promotions at a glance: weekly and weekend reloads, the first deposit bonus, sports cashback, the early payout, the risk-free bet builder and the parlay boost, together with the odds condition they all have in common.
b11   H2 Registration and Login (123-157 words): Registration by e-mail as a five-step numbered route, the personal details required, the single-account rule, followed by signing in and resetting a password.
b12     H3 Verification Before the First Withdrawal (102-130 words): What triggers identity verification, which documents are accepted, the window for submitting them, how long review takes, and the outcome when checks fail.
b13   H2 Deposit Methods, Limits and Speed (133-171 words): Funding methods by type, limits and speed shared by all, the options for Singapore, and the six deposit steps.
b14     H3 Withdrawals: Steps, Timing and Fees (122-154 words): Cashing out: usable methods, the six-step procedure, processing durations, limits, and fees that apply only in particular cases.
b15   H2 Casino Lobby and Game Types (90-113 words): How wide the lobby is, category by category: jackpots and slots, live dealer and table games, lottery, fishing, P2P, fast games and crash and instant games.
b16     H3 Slots with Their RTP (102-130 words): Three example slot titles, each described by provider, RTP, volatility and maximum multiplier.
b17     H3 Live Dealer Section (96-122 words): The live dealer area examined: where it sits among the lobby categories, the exclusive baccarat title, and the live studios that the provider list contains.
b18     H3 Fishing, P2P, Fast Games and Lottery (83-106 words): The remaining game categories brought together in one section: fast games, crash and instant games, lottery, table games, fishing and P2P.
b19   H2 Software Providers (83-106 words): Who makes the games: the studios, as they appear in the provider list.
b20   H2 Mobile Access on Android and iOS (106-134 words): Mobile access via Android, iOS and the mobile web: the responsive site, the shortcut that can be saved to the home screen, and the account features that keep working.
b21   H2 Operator, Licence and Who May Play (191-244 words): First the opening facts (launch date, account currencies, eligible players), then the licence, the operating company and the protection of data and accounts.
b22   H2 Responsible Gambling and Self-Exclusion (115-146 words): The age requirement, self-exclusion, account closure on e-mail request, self-assessment questions and places to find outside help.
b23   H2 Customer Support (77-97 words): When and how support can be reached and which languages it handles.
b24   H2 Pros and Cons (53-67 words): A Pros and Cons table that builds only on facts presented earlier on the page.
b25   H2 Questions About Bonuses and Payouts (229-293 words): Short replies on how to claim the bonus, the wagering rules, weekly cashback, VIP levels, payout timing and payout fees.
b26   H2 Bottom Line on the Offer (106-134 words): A short closing note: the type of reader the offer suits, points to verify before the first deposit, and a nudge towards responsible play.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Review: Bonuses, Games and Payments for Singapore
Longfu88 is an online casino that puts together casino titles, tables with live dealers, a sportsbook and a lottery in a single lobby. Slots and jackpots sit next to crash and instant games, fast games, P2P titles and fishing, so the range reaches well beyond reels alone. The platform went live in 2026, which makes it a recent arrival rather than a long-established name. Adult players can sign up only after turning 18, and this page is written for readers who live in Singapore. It opens with a fact table, then moves through promotions, payments, the game lobby, phone access and licensing, and closes with the tools for responsible play. That order lets a visitor compare the main points before registering.

## Casino Information
=== b02 ===
| Item | Value |
|---|---|
| Welcome bonus | 188% match, capped at €2,088, with 18 free spins |
| Wagering | 25x applied to the deposit plus the bonus amount |
| Minimum deposit | €10 for the whole casino |
| Cashback | Weekly return of up to 10% on net casino losses |
| Licence | Registered in Costa Rica, operator Lumina, registration number 000-039123-R-319326-001 |
| Operator | Lumina |
| Launched | 2026 |
| Payment methods | PayNow, Mastercard, USDT (TRC20), Visa, Bitcoin, Bank Transfer and more |
| Currencies | USDT, MYR, THB, USD, EUR, SGD |
| Support languages | English, Vietnamese, Malay, Indonesian, Simplified Chinese, Thai |
| Support | support@longfu88.com, 24/7 live chat |

## The Casino Welcome Bonus
A first payment is the moment a new player picks an offer, and the Casino Welcome Bonus exists for it: it tops up the opening qualifying deposit by a percentage. The Longfu88 bonus takes the form of a 188% match worth up to €2,088, and 18 free spins come attached. Its qualifying deposit is €50, while the casino as a whole starts at €10. Each account can take one welcome offer, and only newly registered players are eligible. Two rival first-deposit packages exist, the Casino Crypto Welcome Bonus (188%, up to 2,888 USDT, qualifying with 50 USDT) and the Live Casino Welcome Bonus (125%, up to €888, qualifying with €30), but the three are mutually exclusive. At Longfu88 no code is involved. Register, deposit and claim the Casino Welcome Bonus in four steps:

- Register an account and complete the required personal details.
- Make a first deposit that meets the qualifying amount.
- Activate the Casino Welcome Bonus in My Bonuses before placing any bet.
- Finish the wagering before expiry by playing eligible casino games.

### Wagering, Validity and Maximum Bet
The wagering requirement is computed as 25 times the deposit with the bonus on top, and the bonus stays valid for 10 days counted from activation. Other limits sit in one place:

| Condition | Value |
|---|---|
| Maximum cashout | 5x the initial bonus amount |
| Maximum bet | €22.5 per spin |
| Validity | 10 days from activation |
| Free spins winnings wagering | 40x |
| General wagering | 25x deposit plus bonus |

Neteller and Skrill deposits are excluded from the offer, and only one promotional bonus can be active at a time. A withdrawal request sent before claiming, or while the bonus runs, may void eligibility, and cancelling the bonus forfeits the bonus funds along with winnings not yet converted. The operator may also ask for verification before paying out promotional winnings.

## Reload Offers and Seasonal Campaigns
Returning players compare reload deals directly, so this grid sets seven of them side by side.

| Offer | Reward | Min. deposit | Wagering | Validity |
|---|---|---|---|---|
| Casino Weekly Crypto Reload | 60% up to 1,000 USDT | 20 USDT | 30x deposit + bonus | 7 days |
| Casino Dragon Quest | €10 bonus credit | €20 | 30x credit | 7 days |
| Casino Weekend Reload | Up to €3,360 + 50 Free Spins | €50 | 30x deposit + bonus, 40x Free Spins winnings | 7 days |
| Casino Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | €20 | 40x Free Spins winnings | 7 days |
| Casino Weekly Reload | 50 Free Spins | €30 | 40x Free Spins winnings | 7 days |
| Casino Double Fortune | 50% up to €500 | €30 | 30x deposit + bonus | 24 hours |
| Casino Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 20 USDT | 30x deposit + bonus, 40x Free Spins winnings | 7 days |

All offers are switched on in My Bonuses, can be claimed once per promotional period and cannot run alongside another casino promotion still in force. Stakes are limited to €5 per spin during bonus wagering.

### Weekly Cashback and Daily Rebates
Casino Weekly Cashback returns as much as 10% of net casino losses across a week, with a ceiling of €6,988. Counting starts on Monday at 00:00 UTC and ends on Sunday at 23:59 UTC. After opt-in, the credit reaches My Bonuses each Monday with 10x wagering, and the rate follows VIP tier:

| VIP tier | Rate | Weekly ceiling |
|---|---|---|
| Diamond | 10% | €6,988 |
| Platinum | 8% | €3,988 |
| Gold | 6% | €2,988 |
| Silver | 4% | €2,388 |
| Bronze | 2% | €1,888 |

Live Casino Cashback gives 25% up to €850. Daily rebates arrive each day: live casino 1.0%, casino 0.9%, lottery 1.0%, P2P 0.8%, each with 1x wagering and counted on real-money bets only. Opt in to the weekly cashback before the week begins.

### Bonus Crab, Wheel of Fortune and the Coin Shop
The Rewards area groups five features. Bonus Crab reveals a crab reward from claimed picks, lasts 7 days and carries 40x wagering on free spin winnings and 30x on bonus credit. The Wheel of Fortune is spun with an eligible spin or Coins, also lasts 7 days and needs 30x wagering. Challenges and Collections both sit under Rewards, and finishing a challenge leads to earnings of coins, free spins and bonus credits. Coins are spent at the Coin Shop to obtain rewards and bonus credits up to €4,500, at prices that differ by item. Rewards may carry wagering of their own.

## VIP Programme: Points, Levels and Limits
VIP points are earned from real-money play on eligible games, and they give access to a series of reward levels numbered up to 25. Five tiers sit above them: Bronze is the entry rung, Silver and Gold plus Platinum follow, and Diamond is the highest. Higher VIP levels lift the percentage of cashback together with how much can be withdrawn, and from level 4 onward a personal VIP manager and personalised offers join in. Six steps show the ladder:

| VIP level | Points needed | Cashback share | Cap on withdrawals | Level reward |
|---|---|---|---|---|
| 25 | 5,500 | 10% | €147,000 | €980 |
| 20 | 3,600 | 8% | €117,600 | €637 |
| 15 | 2,100 | 6% | €88,200 | €392 |
| 10 | 700 | 4% | €63,700 | €147 |
| 5 | 70 | 2% | €34,300 | €24.5 |
| 1 | 1 | 1% | €9,800 | €9.8 |

Currency and level both shape the reward sums and withdrawal caps, and the programme rules may change, so current terms deserve a check before a player aims for a target level.

## Sportsbook Offer: Markets and Bonuses
At Longfu88, the sportsbook spans nine disciplines, from virtual football and esports to cricket, badminton and basketball, with table tennis, tennis, football and volleyball filling out the list. Seven wager types cover most preferences, from Bet Builder and outrights to totals, handicap, single and live bets, plus the accumulator. An accumulator joins several selections into one wager, a handicap evens out a gap between the sides, and totals look at the combined score of an event. Live betting includes prices that move during the event and open in-play markets, so a bet can be placed while play continues. The Longfu sports area is organised around these options, and events and markets on offer may vary by jurisdiction.

### Sport Bonuses, Cashback and Boosts
| Offer | Reward | Min. deposit | Wagering |
|---|---|---|---|
| Sport Weekend Reload Bonus | 50%, up to €3,750 | €50 | 8x |
| Sport First Deposit Bonus | 100%, up to €1,888 | €50 | 8x |
| Sport Weekly Reload Bonus | 50%, up to €2,500 | €50 | 8x |

The Sport First Deposit Bonus matches a deposit at 100% with a ceiling of €1,888 for 30 days, so claim it ahead of a first sports deposit. Sports Cashback returns 10% of net losses up to €2,500, Bet Builder Risk Free refunds half a stake up to €250, and Parlay Boost adds up to 100% from three legs. Crypto reloads reach 1,000 USDT. Single bets need odds of at least 2.00, accumulator legs 1.50.

## Registration and Login
Signing up at Longfu88 takes five numbered stages and needs an e-mail, a password, the legal name, the date of birth and a residential address:

1. Press Register on the front page of the site.
2. Type in an e-mail and choose a password.
3. Agree to the Terms and Conditions, then to the Privacy Policy, and state that the age requirement is met.
4. Supply more personal details, among them the address of residence.
5. Choose Create Account, then confirm the e-mail if the site asks for it.

The Longfu88 login works with the same e-mail and password: select Login, type the credentials from sign-up and clear the security check when it is shown. Forgot Password, found at sign-in, is the remedy for a lost password, since a link then arrives at the registered e-mail and its instructions set a fresh password. Each player may hold only one personal account, so a second registration is not allowed.

### Verification Before the First Withdrawal
Verification is asked for before the money is released, and the usual trigger is a withdrawal request. Account reviews, unusual or high-value transactions and changes to account or payment details can start it too. These documents are accepted:

- Identity: a passport, national identity card or driving licence.
- Address: a utility bill or bank statement.
- Payment method: a document tying the player to the bank account, card or e-wallet in use.
- Source of funds: proof of income or bank statements, when requested.

Files must reach the operator 30 days after the request at the latest, and review of a complete document set ends with a verdict in a maximum of 10 days. Payouts can wait for the checks. If they fail, transactions can be refused, accounts restricted or withdrawals withheld.

## Deposit Methods, Limits and Speed
Deposits reach the balance after 1-2 minutes at most, whichever Longfu88 method type is used.

| Method type | Examples | Currencies |
|---|---|---|
| Cryptocurrencies | Ethereum, Bitcoin, Litecoin, USDC, USDT (BEP20, TRC20, ERC20) | USDT, USDC, BTC, ETH, LTC |
| Cards | Mastercard, Visa | MYR, VND, IDR, SGD |
| Bank transfer | Bank Transfer, Online Banking | IDR, MYR, VND |
| E-wallets | Skrill and Neteller | EUR |
| European methods | Sofort, Giropay | EUR |
| Local banks and wallets | Local banks, QR payments and regional e-wallets | SGD, MYR, IDR, THB, VND |

For Singapore, the options are PayNow, PayNow QR, OCBC Bank and DBS Bank, all in SGD. Each method shares a €10 minimum and a ceiling of €5,000 per transaction, though limits can differ by country, currency and method. Top-ups carry no processing fee from the casino, but third-party providers or blockchain networks may charge their own. Skrill or Neteller deposits are not accepted for the welcome bonus. A deposit takes six steps: sign in, open the cashier and select Deposit, select a method plus its currency or blockchain network, enter the sum together with the payment information, and confirm following the provider's directions.

### Withdrawals: Steps, Timing and Fees
At Longfu88, a payout request is processed within at most 3 business days, and the route has six numbered stages:

1. Reach the cashier section once signed in.
2. Select Withdrawal and a supported destination.
3. Type the amount and identify the recipient.
4. Send the request once the details look right.
5. Complete ID or payment-method checks if they are requested.
6. Wait for casino, bank or network settlement.

Options include Visa, Mastercard, USDT (three networks), Bitcoin, Ethereum, Litecoin, Online Banking, DBS Bank, Bank Transfer and local wallets, with limits from €20 to €5,000. Cards, wallets and crypto addresses take 1-3 business days, whereas Bank Transfer stretches the wait by 3-5 more business days until the funds are delivered. There is no standard casino withdrawal fee, though provider and blockchain charges may apply. A 10% commission with a €2.25 floor may be due when a deposit was only partly turned over, and 15% may hit selected card or bank-funded payments. Verification may hold up a payout.

## Casino Lobby and Game Types
At Longfu 88 Casino, nine categories sit side by side in the lobby, which lets a visitor go straight to a preferred format. As an online casino, Longfu88 carries crash and instant games, fast games, P2P, fishing, lottery, live dealer and table games, and jackpots and slots. Slots and jackpots lead the list, live dealer rooms and table games suit players who like a structured round, and the remaining categories add quicker or less usual formats. The next sections look at slots, the live dealer area and the smaller categories one by one.

### Slots with Their RTP
Slot fans compare games by their statistics, and three titles illustrate the range. Gates of Olympus, from Pragmatic Play, carries 96.50% RTP alongside a 5,000x ceiling, with high volatility. Pragmatic Play also supplies Sweet Bonanza, where RTP is 96.48%, volatility is high and the top multiplier reaches 21,175x. Hacksaw Gaming is the provider of Wanted Dead or a Wild, which combines 96.38% RTP and very high volatility with a 12,500x maximum. RTP states what portion of wagered money a slot is built to return over many thousands of spins, while volatility indicates whether wins come often and small or seldom and large. The trio is a sample of the lobby, not the full catalogue.

### Live Dealer Section
Live dealer games make up one category of the lobby, aimed at players who prefer a human host to a random number generator and want to see a round played out in real time. Within that area sits the exclusive title Longfu88 Baccarat, which belongs to the live and table game group and follows the familiar baccarat gameplay. The live casino also relies on live studios including Evolution and SA Gaming, since both appear on the provider list. No particular live games or shows are attributed to either studio, so the exact choice of tables, limits and schedules should be confirmed inside the lobby itself.

### Fishing, P2P, Fast Games and Lottery
Crash and instant games run as short rounds: a player either chooses when to cash out a rising multiplier or sees an immediate result. Fast games keep the same brisk pace, with simple rules and results within moments. A lottery is a draw format in which numbers are selected and the outcome follows the draw. Table games carry classic card and wheel formats, contested against the house. Fishing games work as an arcade-style shooter, where the targets are moving creatures on the screen. P2P games are contested against other players instead. Together they show how the online casino adds extra formats beyond slots.

## Software Providers
Game providers deliver the slot, live and table content of the casino, and the roster behind Longfu 88 mixes several well-known studios. Betsoft, Evolution, Yggdrasil and Hacksaw Gaming are part of it, together with Skywind, Big Time Gaming and NetEnt. SA Gaming, Red Tiger and Pragmatic Play complete the group. Readers who follow one particular developer can look for its titles in the lobby, and the earlier slot examples already show where Hacksaw Gaming and Pragmatic Play fit in. Live tables, covered above, come from studios on the same roster.

## Mobile Access on Android and iOS
Many visits begin on a handset, so the site is built as a responsive page, usable in smartphone and tablet browsers across Android, iOS and the mobile web. What players call the Longfu88 app is the saved home-screen version of that site: a shortcut that opens the casino and the sportsbook directly on the phone. Bonuses, deposits, withdrawals and account access keep working there as they do on a desktop. On Android, the shortcut comes together in three short steps:

1. Open Longfu88 in Chrome.
2. Through the browser menu, select Add to Home screen.
3. Approve the shortcut when prompted.

The same result on iPhone and iPad takes three steps as well:

1. Open Longfu88 in Safari.
2. Tap Share, then pick Add to Home Screen.
3. Confirm with Add.

## Operator, Licence and Who May Play
Launched in 2026, the online casino keeps player accounts in six currencies: USDT, MYR, THB, USD, EUR and SGD. A visitor who wants to steer clear of lookalike pages can start from the address labelled Longfu 88 Official Site. Eligibility rests on a few conditions: the player is 18 or above, is lawfully allowed to gamble in the country of residence, registers with accurate information, keeps a maximum of one personal account and pays without any third-party payment method.

For anyone checking credibility, the licence comes first. The licence behind casino Longfu88 lists the operator Lumina, the jurisdiction Costa Rica and registration number 000-039123-R-319326-001, so it belongs to the same operator that runs the platform. Lumina is the data controller as well, and the officer responsible for data protection answers at dpo@longfu88.com. Personal information, payments and player accounts are shielded through technical and organisational measures.

Data can reach payment service providers, identity verification providers and technology providers, as well as regulators and law enforcement bodies when the law requires it. Players hold the rights of access, rectification, restriction and objection, along with withdrawal of consent, portability where applicable and erasure where legally permitted. Credentials stay in the hands of the account holder, who is responsible for protecting them, while suspicion of abuse or a need for verification entitles the operator to suspend activity.

## Responsible Gambling and Self-Exclusion
Gambling here is meant for adults: anyone under 18 is excluded, and play is limited to places where it is lawful. A player who feels control slipping can use self-exclusion, which starts with an e-mail to the support staff. Restrictions on logging in and on gambling may apply for the agreed period, beginning inside 24 hours of the request being handled. Closing an account likewise goes through customer support and follows four steps: the player makes contact, verifies the account data together with the exclusion terms wanted, the casino limits or closes access once that is allowed, and independent help is sought where appropriate. Self-assessment questions make possible gambling-related harm easier to recognise. Outside support is available from organisations such as the ones below, and nothing on this page takes the place of independent assistance:

- GamCare
- Gamblers Anonymous
- Gambling Therapy

## Customer Support
A player with a stuck withdrawal or an unclear bonus condition wants to know who answers and when. Customer support offers two channels. Live chat is open at all hours, 24/7, and suits questions that need a reply during the session. Longer messages with details to describe can be written to the address support@longfu88.com. Staff talk to players in six languages: Indonesian, Simplified Chinese, Malay, Vietnamese, Thai and English. No other contact routes are listed, so both channels also handle payments, verification, self-exclusion and account closure.

## Pros and Cons
Each advantage should be read against its terms.

| Pros | Cons |
|---|---|
| Weekly cashback up to 10% | Verification may delay the first payout |
| 25 VIP levels and 24/7 live chat | A €50 deposit starts the welcome bonus, with 25x turnover of the combined sum |
| Minimum deposit from €10 | Bank payouts may need several business days |
| Many payment methods, crypto included | Withdrawals may carry a 10% or 15% charge when turnover rules apply |

## Questions About Bonuses and Payouts
- **How is the Casino Welcome Bonus claimed, and is a Longfu88 promo code needed?** A first deposit of €50 qualifies. After it arrives, the player activates the bonus under My Bonuses ahead of any wagering, and the procedure has no code stage.
- **What are the wagering terms attached to the welcome bonus?** Free spins winnings need 40x wagering, whereas the deposit and bonus combined need 25x. Validity runs 10 days from activation, and a single spin may not exceed €22.5.
- **How does the Casino Weekly Cashback work for a player?** Cashback can reach 10% of net casino losses over a week, up to €6,988. After an opt-in, every Monday brings a credit in My Bonuses, which the player then activates.
- **How do VIP levels open for a regular player?** Real-money play on eligible games earns VIP points. Collecting them opens 25 numbered levels in the Longfu88 VIP Program, and climbing raises cashback together with the amount that can be withdrawn.
- **Which Lngfu88 withdrawal time applies to each payout method?** Wallets, crypto addresses and cards clear in 1 to 3 working days, but bank transfers add up to 3 days of casino processing plus 3 to 5 business days at the bank.
- **Which fees apply when money is withdrawn?** Standard withdrawals cost nothing at the casino, though provider or blockchain fees may apply. Low turnover may trigger 10% (minimum €2.25), and 15% may be charged on some payments funded by card or bank.

---

## BLOCK BRIEF
Block: b26, H2 "Bottom Line on the Offer" (under H1 "Longfu88 Casino Review: Bonuses, Games and Payments for Singapore")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 106-134 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 134, but never beyond 147 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 casino": exactly 1 time(s)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu": exactly 1 time(s)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Verdict [10]
- Welcome Bonus Terms [6]
- Responsible Gambling [6]
- Minimum Age [5]
Entity Connections to state explicitly [priority]:
- Player → should look at → bonus conditions and payment limits prior to a first deposit [7]
Summary: A short closing note: the type of reader the offer suits, points to verify before the first deposit, and a nudge towards responsible play.
Copywriter Notes: At the end the reader is deciding whether the casino is a match. Write three or four sentences, starting with the profile the facts fit: a player attracted by a single account for live dealer tables, a sportsbook and casino titles, funded locally or with crypto. Then the checks before depositing: 25x wagering, the €50 qualifying deposit, verification, the turnover rule on withdrawals. Finish with the 18+ age limit and reminders: gambling is no income source, chasing losses is a mistake, and budgets and breaks help. Use "Longfu88 casino" (as the name Longfu88 Casino) in the first sentence if at all. "Longfu" is only the casino's short name. No new figures, no promised winnings, no hype. There must be no hint at all that a Singaporean body granted the casino a licence, legal standing or approval (NEVER); licensing is mentioned only as the Brand Information has it. Use "Longfu88" exactly once, "Longfu88 casino" (written as the name Longfu88 Casino) exactly once and "Longfu" exactly once, and no other tracked keyword.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_general.minimum_age: 18
- brandinfo_responsible_gaming.responsible_gaming.policy: Anyone under 18 is excluded, and gambling is limited to jurisdictions where it is lawful.; keep exactly: 18
