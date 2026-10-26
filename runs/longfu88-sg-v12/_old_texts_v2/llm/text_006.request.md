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
Page intent: Brand-review page about the Longfu88 online casino for crypto-friendly players from Singapore: the fact sheet, deposit methods with the cryptocurrencies and networks, crypto and fiat withdrawals with fees, the crypto welcome bonus and its alternatives, crypto reloads and the other weekly offers, sports offers, VIP levels, verification before payouts, registration, games and providers, mobile access, licence and data safety, responsible gambling, support, an FAQ on crypto questions and a verdict. Page voice: technical and plain, sentences of about 16 words, paragraphs of two to four sentences, every crypto figure comes with its currency or network and its condition, fiat and crypto offers are always kept apart and never mixed in one sum; one call to action, at the crypto welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino for Crypto Players in Singapore: Review (102-130 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Singapore.
b02   H2 Casino and Crypto Facts (81-103 words): A fact sheet of the casino: licence, operator, payment methods, currencies, Crypto bonus, welcome bonus, minimum deposit, cashback, languages, support.
b03   H2 Deposit Methods: Crypto Networks and Local Options (141-179 words): Deposit methods grouped by type with the general limits and speed, the local options for Singapore and the six-step deposit route.
b04     H3 Crypto and Fiat Withdrawals: Timing and Fees (128-162 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b05   H2 Crypto Welcome Bonus and the Alternatives (146-187 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b06     H3 Wagering and Caps of the Fiat Welcome Bonus (102-130 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b07   H2 Crypto Reloads and Weekly Offers (128-162 words): The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
b08     H3 Cashback and Rebates (83-106 words): Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
b09   H2 Sports Betting with Crypto Offers (160-203 words): Sports and bet types, live betting and the sports bonuses with the shared odds rule, including the crypto equivalents.
b10   H2 VIP Programme and Withdrawal Limits (109-138 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b11   H2 Verification Before Crypto and Card Payouts (109-138 words): When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.
b12   H2 Registration and Login (123-157 words): How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.
b13   H2 Games and Providers (242-309 words): The nine game categories, three example slots with RTP, the live section with the exclusive baccarat, the other categories and the ten providers.
b14   H2 Mobile Access (96-122 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b15   H2 Licence, Operator and Data Protection (173-219 words): Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected.
b16   H2 Responsible Gambling (96-122 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b17   H2 Support Channels (70-90 words): Support channels, availability and languages.
b18   H2 Crypto Questions (172-218 words): Short answers on cryptocurrencies, the crypto welcome bonus, minimum deposit, withdrawal time, withdrawal fees.
b19   H2 Verdict for Crypto Users (90-113 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino for Crypto Players in Singapore: Review
Longfu88 is an online casino launched in 2026 that combines casino games, live dealer games, sports betting and lottery under one account. The casino lobby is split into nine game categories: slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games. A sportsbook sits beside them for players who prefer to bet on matches.

This page is written for players from Singapore and follows the order in which a newcomer meets the platform: the fact sheet, licence and operator, payments, bonuses, games, mobile play and responsible gambling. Adult players must be at least 18 years old to register and play.

## Casino and Crypto Facts
=== b02 ===
| Parameter | Details |
|---|---|
| Licence | Jurisdiction of Costa Rica, operator Lumina, registration number 000-039123-R-319326-001 |
| Operator | Lumina, the licence holder and data controller |
| Payment methods | Visa, Mastercard, Bank Transfer, Bitcoin, USDT, PayNow |
| Currencies | EUR, USD, MYR, THB, SGD, USDT |
| Crypto bonus | 188% up to 2,888 USDT on the first crypto deposit |
| Welcome bonus | 188% up to €2,088 + 18 Free Spins |
| Minimum deposit | €10, the general minimum of the casino |
| Cashback | Up to 10% of weekly net casino losses |
| Support languages | English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese |
| Support | support@longfu88.com, 24/7 live chat |

## Deposit Methods: Crypto Networks and Local Options
The cashier groups its options by type, led by the cryptocurrencies and the three USDT networks, with local and card methods after them.

| Method type | Examples | Currencies |
|---|---|---|
| Cryptocurrencies | Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), USDC, Bitcoin Cash, Cardano, Ripple | BTC, ETH, LTC, USDT, USDC, BCH, ADA, XRP |
| Singapore options | PayNow, PayNow QR, DBS Bank, OCBC Bank | SGD |
| Cards | Visa, Mastercard | IDR, MYR, SGD, VND |
| Bank transfer | Bank Transfer | IDR, MYR, VND |
| Local banks and wallets | QRIS, DANA, OVO Wallet, Mandiri, BNI, BCA, Touch'n Go, GrabPay, DuitNow, MoMo | IDR, MYR, VND |
| E-wallets | Neteller, Skrill | EUR |
| European methods | Sofort, Giropay | EUR |

Every method shares the same general terms: a minimum of €10, a maximum of €5,000 per transaction and crediting within 1-2 minutes. The casino charges no processing fee on deposits, while payment provider or blockchain network fees may apply. Limits can differ by country, currency and method, and Neteller and Skrill deposits are excluded from the welcome bonus. To deposit, log in to the Longfu88 account, open the cashier, select Deposit and choose a method with its currency or network. Then enter the amount and payment details, confirm the transaction as the provider instructs and wait for the funds to reach the playable balance.

### Crypto and Fiat Withdrawals: Timing and Fees
Longfu88 pays out to fourteen destinations: Bank Transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT on TRC20, ERC20 and BEP20, Touch'n Go, DANA, MoMo, DBS Bank and Online Banking. Each request must be between €20 and €5,000. The Lngfu88 withdrawal time is 1 to 3 business days for card, crypto and wallet requests, while a bank transfer takes up to 3 business days for casino processing plus 3 to 5 business days for bank delivery.

No standard casino withdrawal fee applies, but provider and blockchain fees may. A 10% commission (minimum €2.25) can apply where turnover is below the deposited amount, because a minimum 1x deposit turnover can apply before a withdrawal. Some card or bank transfer funded transactions may carry 15%. The route has six steps, and identity checks can delay a payout (see the verification section):

1. Log in and open the cashier.
2. Select Withdrawal and choose a supported destination or payment method.
3. Enter the amount and the receiving bank, wallet or blockchain address.
4. Complete identity and payment-method verification if prompted.
5. Review the request and confirm submission.
6. Wait for casino processing and any bank or network settlement before the funds arrive.

## Crypto Welcome Bonus and the Alternatives
Crypto players start with the Casino Crypto Welcome Bonus at Longfu88: a deposit bonus of 188% up to 2,888 USDT on the first qualifying crypto deposit, with a minimum deposit of 50 USDT. Wagering is 40x the deposit plus bonus within 10 days, and the maximum bonus wager is 5 USDT per spin. Eligible cryptocurrencies are USDT, BTC, BCH, LTC, ETH, XRP and USDC. Claim this offer with the first deposit in one of these coins.

The fiat route is the Casino Welcome Bonus. A first deposit casino bonus, the Longfu88 bonus gives 188% up to €2,088 plus 18 Free Spins to new registered players, with one welcome offer per account. Its qualifying minimum deposit is €50, not the general €10 of the casino. Another fiat option is the Live Casino Welcome Bonus, 125% up to €888 with a minimum deposit of €30. The Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers, so a player picks one. Claiming runs through the My Bonuses activation after the qualifying deposit, and no Longfu88 promo code step is part of the listed procedure:

- Register an account and complete the required personal details.
- Make the first qualifying deposit.
- Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.
- Play eligible casino games and complete the wagering before expiry.

### Wagering and Caps of the Fiat Welcome Bonus
The wagering requirement of the fiat Casino Welcome Bonus is 25 times the deposit plus the bonus amount, and the Free Spins winnings are wagered separately.

| Condition | Value |
|---|---|
| Wagering | 25x the deposit plus bonus amount |
| Free Spins wagering | 40x Free Spins winnings |
| Validity | 10 days from activation |
| Maximum bet | €22.5 per spin |
| Maximum cashout | 5x the initial bonus amount |

Neteller and Skrill deposits are excluded, and only one promotional bonus can be active at a time. A withdrawal request before claiming or while the bonus is active can void eligibility, and cancelling forfeits bonus funds and unconverted winnings, so the wagering should be finished before a cash-out is requested. Verification may be required before bonus winnings are paid.

## Crypto Reloads and Weekly Offers
Crypto reloads come first in the table, followed by the fiat reloads, the one-day special, the seasonal offer and the verification reward.

| Offer | Reward | Min. deposit | Wagering | Validity |
|---|---|---|---|---|
| Casino Weekly Crypto Reload | 60% up to 1,000 USDT | 20 USDT | 30x deposit plus bonus | 7 days |
| Casino Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 20 USDT | 30x deposit plus bonus, 40x Free Spins winnings | 7 days |
| Casino Weekly Reload | 50 Free Spins | €30 | 40x winnings from Free Spins | 7 days |
| Casino Weekend Reload | Up to €3,360 + 50 Free Spins | €50 | 30x deposit plus bonus, 40x Free Spins winnings | 7 days |
| Casino Double Fortune: One-Day Reload Special | 50% up to €500 | €30 | 30x deposit plus bonus | 24 hours |
| Casino Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | €20 | 40x Free Spins winnings | 7 days |
| Casino Dragon Quest | €10 bonus credit | €20 | 30x promotional credit | 7 days |

All seven offers are activated in My Bonuses and claimed once per promotional period, and none can be combined with another active casino bonus. The maximum stake while wagering bonus funds is €5 per spin.

### Cashback and Rebates
The Casino Weekly Cashback returns up to 10% of weekly net casino losses, capped at €6,988, for the period from Monday 00:00 UTC to Sunday 23:59 UTC. Players opt in for a four-week cycle, and the amount is credited to My Bonuses on Monday with 10x wagering. The rate follows the VIP tier: Bronze 2% up to €1,888, Silver 4% up to €2,388, Gold 6% up to €2,988, Platinum 8% up to €3,988 and Diamond 10% up to €6,988. A separate Live Casino Cashback pays 25% up to €850. Unlimited Rebate comes in four versions that are credited daily with 1x wagering: casino 0.9%, live casino 1.0%, P2P 0.8% and lottery 1.0%. Only real-money bets count, bonus funds do not.

---

## BLOCK BRIEF
Block: b09, H2 "Sports Betting with Crypto Offers" (under H1 "Longfu88 Casino for Crypto Players in Singapore: Review")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 160-203 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 203, but never beyond 243 words.
Format: paragraph + table. Visual Elements: Table — 5 of 5 tables on the page
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
- "Longfu sports": exactly 1 time(s)
Entities to cover [priority 1-10]:
- Sportsbook [10]
- Football [7]
- Esports [6]
- Live Betting [7]
- Bet Builder [5]
- Accumulator [5]
- Sport First Deposit Bonus [10]
- Sports Cashback [7]
- Parlay Boost [6]
- Minimum Odds [6]
Entity Connections to state explicitly [priority]:
- Sportsbook → covers → football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football [8]
- Live Betting → offers → live odds and in-play markets [7]
- Sport First Deposit Bonus → gives → 100% up to €1,888 [8]
- Qualifying Bets → need → minimum odds of 2.00 for singles [7]
Summary: Sports and bet types, live betting and the sports bonuses with the shared odds rule, including the crypto equivalents.
Copywriter Notes: This block covers several topics in ONE continuous section without sub-headings, in this order, each topic in proportion to its share of the block. (1) Sports Betting: Give the nine sports and esports as listed (football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports, virtual football), the seven bet types (single, accumulator, live, handicap, totals, outrights, Bet Builder) and live betting with live odds and in-play markets. Where "Longfu sports" is used, write it as a natural phrase for the sports section (for example the Longfu sports section). Event availability and market selection can vary by jurisdiction. Name no sports league or event and no sportsbook platform. (2) Sports Bonuses and Promotions: Give a compact table Offer | Reward | Min. deposit | Wagering for the Sport First Deposit Bonus (100% up to €1,888, €50, 8x, 30 days), the Sport Weekly Reload Bonus (50% up to €2,500, €50, 8x) and the Sport Weekend Reload Bonus (50% up to €3,750, €50, 8x); then name the crypto equivalents, Sports Cashback (10% up to €2,500 of eligible sports net losses, weekly), Unlimited Sports Rebate (0.70%), 2 Goals Ahead early payout, Parlay Boost (up to 100% extra winnings, at least three legs) and Bet Builder Risk Free (50% stake return up to €250) in prose. Rules that apply: only settled qualifying sports bets count, single bets need odds of at least 2.00 and each accumulator selection at least 1.50, voided and cashed-out bets do not qualify. Do not mix these with the casino bonuses. Variant direction: Name the Sport Crypto Welcome Bonus, the Sport Crypto Weekly Reload and the Sport Crypto Weekend Reload in the sports bonus part. Use "Longfu88" exactly once and "Longfu sports" exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_sportsbook.sportsbook.sports_available: ["Football", "Basketball", "Tennis", "Badminton", "Cricket", "Table tennis", "Volleyball", "Esports", "Virtual football"]
- brandinfo_sportsbook.sportsbook.bet_types: ["Single", "Accumulator", "Live", "Handicap", "Totals", "Outrights", "Bet Builder"]
- brandinfo_sportsbook.sportsbook.live_betting: {"available": true, "features": ["Live odds", "In-play markets"]}
- brandinfo_sportsbook.sportsbook.important_terms: ["Event availability and market selection can vary by jurisdiction."]
- brandinfo_sportsbook.sportsbook.sports_bonuses: [{"name": "Sport First Deposit Bonus", "reward": "100% up to €1,888", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Welcome Bonus", "reward": "100% up to 200 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Weekly Reload Bonus", "reward": "50% up to €2,500", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Weekend Reload Bonus", "reward": "50% up to €3,750", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Weekly Reload", "reward": "50% up to 500 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Weekend Reload", "reward": "50% up to 1,000 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Unlimited Sports Rebate", "reward": "0.70% of qualifying settled sports wagers", "wagering_requirement": "1x credited rebate", "crediting": "Daily"}, {"name": "Sports Cashback", "reward": "10% up to €2,500 of eligible sports net losses", "calculation_period": "Weekly", "wagering_requirement": "1x cashback", "eligibility": "Registered players with eligible real-money losing bets"}, {"name": "2 Goals Ahead - Early Payout", "reward": "Early settlement of eligible football bets when the selected team leads by two goals", "important_terms": ["Only participating pre-match match-winner markets qualify.", "Settlement is subject to published event eligibility."]}, {"name": "Parlay Boost", "reward": "Up to 100% extra winnings on qualifying accumulators", "minimum_legs": 3, "wagering_requirement": "No additional bonus wagering on settled enhanced winnings", "important_terms": ["Boost depends on the number of qualifying selections."]}, {"name": "Bet Builder Risk Free", "reward": "50% risk-free stake return up to €250", "eligibility": "Qualifying pre-match Bet Builder selections", "wagering_requirement": "1x credited free-bet stake", "validity": "7 days"}]
