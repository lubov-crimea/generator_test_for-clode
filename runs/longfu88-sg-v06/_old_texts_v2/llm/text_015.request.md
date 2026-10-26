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
Page intent: Brand-review page about the Longfu88 sportsbook and online casino for players from Singapore, written for a bettor: the fact table, sports betting with markets, bet types and live betting, the sports bonuses, betting on mobile, registration and verification, payments, then the casino side with the welcome bonus, reloads and cashback, VIP levels, games and providers, licence and safety, responsible betting, support, pros and cons, an FAQ on sports and payouts and a verdict. Page voice: plain betting vocabulary, the reader is addressed as "you", sentences of about 17 words, every section starts with the market or the bet the reader makes and ends with the condition that decides the payout; paragraphs of two to four sentences; calls to action at the sports first deposit bonus and at the casino welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Sports and Casino Review for Singapore Players (96-122 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Singapore.
b02   H2 Sports and Casino Facts (88-112 words): A fact sheet of the casino: licence, operator, welcome bonus, cashback, currencies, languages, payment methods, Sports, Sports bonus, minimum deposit, support.
b03   H2 Sports Betting at the Casino (115-146 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b04     H3 Sports Bonuses and Boosts (90-113 words): The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
b05   H2 Betting on Mobile (96-122 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b06   H2 Registration, Login and Verification (173-219 words): Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes.
b07   H2 Deposits and Withdrawals (249-316 words): Deposit methods by type with limits and speed in a table, the deposit route, then withdrawal methods, steps, timing and fees.
b08   H2 Casino Welcome Bonus and Its Terms (191-244 words): The Casino Welcome Bonus with its figures, claiming steps and alternatives, then the wagering, validity and bet limits in a table.
b09   H2 Reloads and Cashback (173-219 words): The seven reload and seasonal offers in a table, then the weekly cashback with VIP rates, the live casino cashback and the rebates.
b10   H2 VIP Programme (102-130 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b11   H2 Casino Games and Slots (154-194 words): The nine game categories and three example slots with RTP, volatility and maximum multiplier.
b12   H2 Live Casino, Other Games and Providers (218-276 words): The live dealer section with the exclusive baccarat, the other game types and the ten providers.
b13   H2 Licence and Security (173-219 words): Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected.
b14   H2 Responsible Betting and Gambling (102-130 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b15   H2 Support (70-90 words): Support channels, availability and languages.
b16   H2 Pros and Cons (53-67 words): A pros and cons table built only from facts stated elsewhere on the page.
b17   H2 Questions About Sports and Payouts (172-218 words): Short answers on sports covered, the sports bonus, minimum deposit, withdrawal time, support languages.
b18   H2 Verdict for Sports Fans (90-113 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Sports and Casino Review for Singapore Players
Longfu88 is an online casino that pairs a sportsbook with nine game areas: slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games. The platform launched in 2026 and combines casino games, live dealer games, sports betting and lottery on one site. This page is written for players from Singapore, and adult players must be at least 18 years old. The sections below move from the facts, the sportsbook and its bonuses to mobile play, payments, the licence and responsible gambling. Each section closes with the condition that decides what an offer is worth in practice.

## Sports and Casino Facts
| Parameter | Details |
|---|---|
| Licence | Jurisdiction Costa Rica, operator Lumina, registration number 000-039123-R-319326-001 |
| Operator | Lumina |
| Welcome bonus | 188% up to €2,088 + 18 Free Spins |
| Cashback | Up to 10% of weekly net casino losses, capped at €6,988 |
| Currencies | EUR, USD, MYR, THB, SGD, USDT |
| Support languages | English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese |
| Payment methods | Visa, Mastercard, Bank Transfer, Bitcoin, USDT, PayNow |
| Sports | Football, Basketball, Tennis, Badminton, Cricket, Table tennis, Volleyball, Esports, Virtual football |
| Sports bonus | Sport First Deposit Bonus, 100% up to €1,888 |
| Minimum deposit | €10 |
| Support | support@longfu88.com, 24/7 live chat |

## Sports Betting at the Casino
Football opens the list of nine sports and esports at the Longfu88 sportsbook, followed by basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football. The sportsbook offers seven bet types: single, accumulator, live, handicap, totals, outrights and Bet Builder. A single backs one outcome, an accumulator links several selections into one bet, and a Bet Builder combines selections from one event. Handicap and totals markets suit matches expected to be one-sided, while outrights are settled on the final result of a competition. Live betting adds live odds and in-play markets, so a bet can be placed while the event is running. Event availability and market selection can vary by jurisdiction, and that limit applies before any bet is placed.

### Sports Bonuses and Boosts
Select the Sport First Deposit Bonus before the qualifying deposit or in My Bonuses. All three need €50 and 8x wagering:

- **Sport First Deposit Bonus**: 100% up to €1,888, valid for 30 days
- **Sport Weekly Reload Bonus**: 50% up to €2,500
- **Sport Weekend Reload Bonus**: 50% up to €3,750

Sports Cashback returns 10% up to €2,500 of weekly eligible sports net losses, and the Unlimited Sports Rebate pays 0.70%. 2 Goals Ahead pays early on eligible football bets, Parlay Boost adds up to 100% extra winnings on accumulators of at least three legs, and Bet Builder Risk Free returns 50% of the stake up to €250. Only settled qualifying bets count: singles need odds of at least 2.00, accumulator selections 1.50, and voided or cashed-out bets do not qualify.

## Betting on Mobile
A bet from a phone runs through the responsive website, which works in smartphone and tablet browsers on Android, iOS and mobile web. Added to the home screen as a shortcut, it becomes the Longfu88 app, the home-screen version of the site with quick access to the casino and the sportsbook. The same screen gives account access, deposits, withdrawals and bonuses. On Android, the route takes three steps:

1. Open Longfu88 in Chrome.
2. Open the browser menu and choose Add to Home screen.
3. Confirm the shortcut.

On iOS, the shortcut is added from Safari:

1. Open Longfu88 in Safari.
2. Tap Share and choose Add to Home Screen.
3. Confirm Add.

## Registration, Login and Verification
Registration starts with an email address and ends with a confirmed account, and it takes five steps:

1. Open Longfu88 and select Register.
2. Enter email and create a password.
3. Confirm age and acceptance of Terms and Conditions and Privacy Policy.
4. Complete the additional personal details and residential address.
5. Select Create Account and complete any requested email confirmation.

Registration requires an email, a password, a legal name, a date of birth and a residential address, and each player may hold only one personal account. For the Longfu88 login, select Login on the website, enter the registered email and password and complete any security check. A player who forgets the password chooses Forgot Password on the login screen and follows the reset link sent by email.

The KYC verification may be required before a withdrawal, and also after unusual or high-value transactions or changes to account or payment details. Accepted documents are:

- Identity: passport, national identity card or driving licence
- Address: utility bill or bank statement
- Proof of ownership of the payment method
- Source of funds, when requested

Documents can be sent within 30 days of the request, and a complete set is normally reviewed within 10 days. Withdrawals may be held until the checks are done, and failed checks can lead to refused transactions or account restrictions.

## Deposits and Withdrawals
Every bet starts with a deposit, and one set of limits covers all methods: a minimum of €10 and a maximum of €5,000 per transaction.

| Method type | Examples | Currencies |
|---|---|---|
| Singapore methods | PayNow, PayNow QR, DBS Bank, OCBC Bank | SGD |
| Local bank and wallet methods | QRIS, DANA, OVO Wallet, Touch'n Go, DuitNow, PromptPay QR, MoMo | IDR, MYR, THB, VND |
| Cards | Visa, Mastercard | IDR, MYR, SGD, VND |
| Bank transfer | Bank Transfer | IDR, MYR, VND |
| Cryptocurrencies | Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), USDC | BTC, ETH, LTC, USDT, USDC |
| E-wallets | Neteller, Skrill | EUR |
| European methods | Sofort, Giropay | EUR |

Deposits are credited within 1-2 minutes and carry no casino processing fee, while provider or blockchain network fees may apply. Limits can differ by country, currency and method, and Neteller and Skrill deposits are excluded from the welcome bonus. The route is short: open the cashier, select Deposit, choose a method with its currency or network, enter the details, authorise the payment and wait for the balance to update.

Withdrawals go through bank transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT on three networks, Touch'n Go, DANA, MoMo, DBS Bank or Online Banking, from a minimum of €20 to a maximum of €5,000:

1. Log in to Longfu88 and open the cashier.
2. Select Withdrawal and choose a supported destination or payment method.
3. Enter the amount and the receiving bank, wallet, or blockchain address.
4. Complete identity and payment-method verification if prompted.
5. Review the request and confirm submission.
6. Wait for casino processing and any bank or network settlement before receiving funds.

The Lngfu88 withdrawal time is 1 to 3 business days for card, crypto and wallet payouts, while a bank transfer takes up to 3 business days of casino processing plus 3 to 5 business days for bank delivery. No standard withdrawal fee applies, but provider and blockchain fees may. A minimum 1x deposit turnover can apply before a withdrawal: where turnover is below the deposited amount, a 10% commission (minimum €2.25) may be charged, and some card or bank transfer funded transactions can carry 15%. Identity checks can also delay a payout.

## Casino Welcome Bonus and Its Terms
At Longfu88, the Casino Welcome Bonus is the first-deposit offer for new registered players. The Longfu88 bonus gives 188% up to €2,088 plus 18 Free Spins, that is spins on a slot with the stake paid by the casino. This bonus needs a qualifying first deposit of at least €50, and each account can take one welcome offer. Claim it in four steps:

- Register an account and complete the required personal details.
- Make the first qualifying deposit.
- Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.
- Play eligible casino games and complete the wagering before expiry.

The claiming route is the My Bonuses activation after the qualifying deposit, and no Longfu88 promo code step is part of the listed procedure. Two alternatives exist: the Live Casino Welcome Bonus (125% up to €888, minimum deposit €30) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, minimum deposit 50 USDT). The Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers.

The terms decide how much of the bonus can be withdrawn:

| Condition | Value |
|---|---|
| Wagering | 25x the deposit plus bonus amount |
| Free Spins wagering | 40x Free Spins winnings |
| Validity | 10 days from activation |
| Maximum bet | €22.5 per spin |
| Maximum cashout | 5x the initial bonus amount |

Neteller and Skrill deposits are excluded, and only one promotional bonus can be active at a time. A withdrawal request before claiming or while the bonus is active can void eligibility, cancelling forfeits bonus funds and unconverted winnings, and verification may be required before bonus winnings are paid.

## Reloads and Cashback
Reloads, a one-day special and a seasonal promotion need a deposit first:

| Offer | Reward | Min. deposit | Wagering | Validity |
|---|---|---|---|---|
| Weekly Reload | 50 Free Spins | €30 | 40x Free Spins winnings | 7 days |
| Weekly Crypto Reload | 60% up to 1,000 USDT | 20 USDT | 30x deposit plus bonus | 7 days |
| Weekend Reload | Up to €3,360 + 50 Free Spins | €50 | 30x deposit plus bonus, 40x Free Spins winnings | 7 days |
| Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 20 USDT | 30x deposit plus bonus, 40x Free Spins winnings | 7 days |
| Double Fortune | 50% up to €500 | €30 | 30x deposit plus bonus | 24 hours |
| Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | €20 | 40x Free Spins winnings | 7 days |
| Dragon Quest | €10 bonus credit | €20 | 30x promotional credit | 7 days |

Each is activated in My Bonuses, allows one claim per promotional period, cannot be combined with another active casino bonus and caps the stake at €5 per spin.

At Longfu88, the Casino Weekly Cashback returns up to 10% of weekly net casino losses, capped at €6,988, for Monday 00:00 UTC to Sunday 23:59 UTC. It needs a four-week opt-in, is credited to My Bonuses on Monday and carries 10x wagering. Rates follow the VIP tier:

| VIP tier | Cashback | Maximum |
|---|---|---|
| Bronze | 2% | €1,888 |
| Silver | 4% | €2,388 |
| Gold | 6% | €2,988 |
| Platinum | 8% | €3,988 |
| Diamond | 10% | €6,988 |

The Live Casino Cashback pays 25% up to €850. Four daily rebates add 0.9% on casino, 1.0% on live casino, 0.8% on P2P and 1.0% on lottery, each with 1x wagering. Only real-money bets count.

## VIP Programme
VIP points come from eligible real-money play and unlock numbered reward levels, 25 in total, grouped into the Bronze, Silver, Gold, Platinum and Diamond tiers. Level 1 needs 1 point and carries a level reward of €9.8, 1% cashback and a withdrawal limit of €9,800. At the top, level 25 needs 5,500 points and carries a level reward of €980, 10% cashback and a withdrawal limit of €147,000. Higher levels raise withdrawal limits and cashback and add personalised offers, and a personal VIP manager is available from level 4. Reward and withdrawal limits may differ by VIP level and currency, and the rules can change, so the current terms decide what a level is worth.

## Casino Games and Slots
Longfu 88 Casino groups its games into nine categories: slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games. At Longfu88, the online casino offers all of them beside the sportsbook. Live casino and the other categories follow in the next section, so this part stays with slots.

Slots are where RTP and volatility matter most, and three examples show the figures. Gates of Olympus from Pragmatic Play has an RTP of 96.50%, high volatility and a maximum multiplier of 5,000x. Sweet Bonanza, also from Pragmatic Play, has an RTP of 96.48%, high volatility and a maximum multiplier of 21,175x. Wanted Dead or a Wild, supplied by Hacksaw Gaming, has an RTP of 96.38%, very high volatility and a maximum multiplier of 12,500x. RTP is the share of stakes a slot pays back over a very long run, while volatility describes how large and how frequent the wins tend to be, so a high rating means longer gaps between wins.

## Live Casino, Other Games and Providers
Live dealer games form their own category in the Longfu 88 lobby, and the exclusive title there is Longfu88 Baccarat, a live or table game with baccarat gameplay. Evolution and SA Gaming are among the studios behind the live casino, alongside other providers. In a live dealer game a real person runs the round in real time, and bets must be placed before the round closes. Table games cover the classic card and table formats in which the player bets against the house.

The remaining categories differ in what the player does. Fishing games are arcade-style rounds in which the player aims at moving targets, and P2P games are played against other players instead of the casino. Fast games are built around short rounds, lottery is a draw on chosen numbers, and crash and instant games settle quickly, with the player deciding when to cash out in a crash round.

Game providers supply slots, live and table games to the casino. The list reads Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft and Hacksaw Gaming, and Pragmatic Play also stands behind the first two slots described in the previous section. Rules shown on each table or round decide how a bet is settled, so they are worth reading before the first stake is placed.

## Licence and Security
Safe play starts with the right address: players should use the Longfu 88 Official Site address and not look-alike pages, which keeps login details away from copycat sites. The online casino launched in 2026 and keeps accounts in EUR, USD, MYR, THB, SGD and USDT. Players must be at least 18, legally permitted to gamble where they live, hold one personal account and use no third-party payment methods.

The casino Longfu88 operates under a Costa Rica gambling licence held by the operator Lumina, registration number 000-039123-R-319326-001. Lumina also acts as the data controller, and the data protection officer is reached at dpo@longfu88.com. Technical and organisational safeguards protect accounts, payments and personal information. Data may be shared with payment service providers, identity verification providers, technology providers and, when required, regulators and law enforcement. Players have rights of access, rectification, erasure where legally permitted, restriction, objection, portability where applicable and withdrawal of consent. The account holder is responsible for safeguarding credentials, and the operator may suspend activity for verification or suspected abuse, which is why accurate registration details matter.

## Responsible Betting and Gambling
Players must be at least 18 and may gamble only where it is lawful. Self-exclusion is requested by e-mail to support@longfu88.com. It restricts account access and gambling for the agreed period and takes effect within 24 hours after the request is processed. Account closure is requested through customer support in four short steps: contact support, confirm the account details and preferred exclusion terms, allow the casino to restrict or close access, and seek independent support where appropriate. Self-assessment questions help players identify possible gambling-related harm before it grows. This page cannot replace independent help, which these organisations provide:

- GamCare
- Gamblers Anonymous
- Gambling Therapy

## Support
Support works through two channels: 24/7 live chat and e-mail at support@longfu88.com. Live chat is available around the clock, so a question about an open bet or a payout does not have to wait for the next working day, while e-mail suits longer requests. Customer support speaks English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese, and a player can pick the language that makes the question easiest to explain.

---

## BLOCK BRIEF
Block: b16, H2 "Pros and Cons" (under H1 "Longfu88 Sports and Casino Review for Singapore Players")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 53-67 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 67, but never beyond 80 words.
Format: table. Visual Elements: Table — 5 of 5 tables on the page
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
- Advantages [8]
- Disadvantages [8]
- Welcome Bonus [6]
- Withdrawal Fees [5]
- Payment Methods [5]
Entity Connections to state explicitly [priority]:
- Advantages → are balanced against → the conditions that come with them [7]
Summary: A pros and cons table built only from facts stated elsewhere on the page.
Copywriter Notes: A Markdown table with exactly two columns, Pros | Cons, four or five rows. Pros are facts from the page (a low general minimum deposit of €10, a large choice of payment methods including cryptocurrencies, a weekly cashback of up to 10%, a VIP programme with 25 levels, 24/7 live chat); cons are the conditions that go with them (the welcome bonus needs a €50 deposit and 25x wagering on deposit plus bonus, a 10% or 15% commission can apply to withdrawals under the turnover rule, bank withdrawals can take several business days, verification may delay the first payout). No intro sentence beyond one line, no new facts, no tracked keyword in the table. Use no tracked keyword in the body of this block.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_general.minimum_deposit: €10
- brandinfo_welcome.welcome_bonus.wagering_requirement: 25x the deposit plus bonus amount
- brandinfo_privacy_policy.terms_conditions.conditional_fees: ["Where qualifying turnover is below the deposited amount, a 10% commission may apply with minimum €2.25.", "A 15% charge can apply to some card or bank transfer funded transactions under the casino rules."]
- brandinfo_games.providers: ["Evolution", "Red Tiger", "NetEnt", "Big Time Gaming", "Pragmatic Play", "Yggdrasil", "SA Gaming", "Skywind", "Betsoft", "Hacksaw Gaming"]
- brandinfo_promotions.other_bonuses[9].reward: Up to 10% of weekly net casino losses, capped at €6,988
