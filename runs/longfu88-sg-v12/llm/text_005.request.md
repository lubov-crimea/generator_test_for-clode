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
Page intent: Written for Singapore players who favour crypto: an editorial look at the Longfu88 online casino. Covered in order: fact sheet, deposits with the cryptocurrencies and networks, crypto and fiat withdrawals with fees, the crypto welcome bonus and its alternatives, crypto reloads and other weekly offers, sports offers, VIP levels, verification ahead of payouts, registration, games and providers, mobile access, the licence together with data safety, then responsible-gambling tools, support, a crypto FAQ and a verdict. Voice: technical and plain; sentences near 16 words, paragraphs of two to four sentences; each crypto figure is paired with its currency or network and its condition; fiat and crypto offers stay apart and are never merged into a single sum; the page carries a single call to action, placed at the crypto welcome bonus. Facts about the brand are drawn solely from the AffBulk knowledge base longfu88-new; the page stays silent on the standing of the casino under Singapore law.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino for Crypto Players in Singapore: Review (102-130 words): Opening overview: what the casino is, its game areas, the launch year and the adult Singapore audience of the page.
b02   H2 Casino and Crypto Facts (81-103 words): Fact table: licence, operator, payment methods, currencies, Crypto bonus, welcome bonus, minimum deposit, cashback, languages and support.
b03   H2 Deposit Methods: Crypto Networks and Local Options (141-179 words): Deposit methods grouped by type, limits and speed common to all of them, local Singapore options and the six-step deposit path.
b04     H3 Crypto and Fiat Withdrawals: Timing and Fees (128-162 words): Cash-out mechanics: choice of channels, a six-step path, waiting period, floor and ceiling per request, and charges that apply under certain conditions.
b05   H2 Crypto Welcome Bonus and the Alternatives (146-187 words): Casino Welcome Bonus: percentage, maximum, free spins, qualifying deposit, eligible players and the four claiming steps, plus the pair of other first-deposit offers.
b06     H3 Wagering and Caps of the Fiat Welcome Bonus (102-130 words): Table of the Casino Welcome Bonus terms, followed by the restrictions and the way they work out for the player.
b07   H2 Crypto Reloads and Weekly Offers (128-162 words): Recurring reloads and special campaigns in a comparison table (reward, minimum deposit, wagering, validity), with the rules they share.
b08     H3 Cashback and Rebates (83-106 words): Weekly and live casino cashback including the VIP rates, plus the daily rebates per game category.
b09   H2 Sports Betting with Crypto Offers (160-203 words): Sports and bet types, live betting, then bonuses for sports, which share one odds rule, crypto equivalents included.
b10   H2 VIP Programme and Withdrawal Limits (109-138 words): VIP programme mechanics: points from real-money play, five tiers, a total of 25 reward levels, numbered, and what gets better towards the top.
b11   H2 Verification Before Crypto and Card Payouts (109-138 words): Verification: when it is requested, the accepted documents, the submission deadline, the review time and the consequence of failed checks.
b12   H2 Registration and Login (123-157 words): Registration with an e-mail address in five steps, listed by number; plus the required details, the one-account rule, login and password recovery.
b13   H2 Games and Providers (242-309 words): Slots with RTP (three examples) and an overview of all nine game categories; the live lobby with its exclusive baccarat game; the other categories; ten providers.
b14   H2 Mobile Access (96-122 words): Android, iOS and mobile web play: how the responsive site behaves, how a shortcut reaches the home screen, which account functions are on hand.
b15   H2 Licence, Operator and Data Protection (173-219 words): Year of launch, account currencies and player eligibility; then the licence, who runs the casino, and what protects personal data and accounts.
b16   H2 Responsible Gambling (96-122 words): Minimum age, self-exclusion and account closure via an e-mail request, a self-check and support organisations.
b17   H2 Support Channels (70-90 words): Ways to get in touch, when they are available and which languages support speaks.
b18   H2 Crypto Questions (172-218 words): Brief answers on cryptocurrencies, the crypto welcome bonus, the minimum deposit, withdrawal time and withdrawal fees.
b19   H2 Verdict for Crypto Users (90-113 words): Closing verdict: the kind of player it fits, items worth checking ahead of the first payment, and a responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino for Crypto Players in Singapore: Review
Longfu88 runs as a single online casino that combines a sportsbook, a casino game library, live croupier tables and a lottery under one roof. Its game areas include slots, live dealer games, table games, jackpot titles, fishing and P2P games, fast games, and crash and instant titles. Launch year: 2026. This review is aimed at Singapore-based players who have reached 18, the minimum age. A crypto user checks certain things first, and the page follows that order: payments, mobile play, games, bonus offers, the licence and brand facts. It ends with a section on responsible gambling, since no outcome at the tables can ever be promised.

## Casino and Crypto Facts
| Subject | Overview |
|---|---|
| Licence | Registered as 000-039123-R-319326-001 in Costa Rica, holder Lumina |
| Operator | Lumina |
| Payment methods | Visa, Mastercard, Bitcoin, USDT (TRC20), PayNow, Bank Transfer |
| Currencies | Six account currencies: THB, MYR, EUR, USD, USDT, SGD |
| Crypto bonus | 188% up to 2,888 USDT |
| Welcome bonus | 188% match, ceiling €2,088, 18 free spins |
| Minimum deposit | €10 across the casino in general |
| Cashback | Rate up to 10%, base weekly net casino losses |
| Support languages | English, Simplified Chinese, Malay, Indonesian, Thai, Vietnamese |
| Support | Live chat 24/7, email address support@longfu88.com |

## Deposit Methods: Crypto Networks and Local Options
Deposit methods fall into several types, with crypto listed first and the local and card options after it.

| Method type | Examples | Currencies |
|---|---|---|
| Cryptocurrencies | Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), USDC, Bitcoin Cash, Ripple, Cardano | BTC, ETH, LTC, USDT, USDC, BCH, XRP, ADA |
| Cards | Visa, Mastercard | IDR, SGD, MYR, VND |
| Singapore banking and QR | DBS Bank, OCBC Bank, PayNow, PayNow QR | SGD |
| E-wallets | Skrill, Neteller | EUR |
| European methods | Giropay, Sofort | EUR |

Any single transaction must stay between €10 and €5,000, and the money appears on the balance within 1-2 minutes. The casino charges nothing for processing, though the payment provider or the blockchain network may add its own costs. Three things move the limits: where the player is, which currency is used and which method is chosen. Money sent through Neteller or Skrill does not trigger the welcome bonus. A player logs in to Longfu88, opens the cashier and presses Deposit, then picks a supported method with its currency or network, enters payment information and the amount, and confirms the transaction as the provider instructs.

### Crypto and Fiat Withdrawals: Timing and Fees
Longfu88 pays out to Mastercard, Visa, bank transfer, Online Banking, DBS Bank, MoMo, DANA, Touch'n Go, Litecoin, Ethereum, Bitcoin and USDT on three networks. A request must be between €20 and €5,000. The Lngfu88 withdrawal time is at most three business days for casino handling, and card, crypto and e-wallet payouts take 1-3 business days. A bank transfer adds a second stage, as the player's bank may need another 3-5 business days. The standard casino fee is zero, but providers and blockchains can still add costs. A 10% charge (minimum €2.25) may apply if the wagered amount is lower than the deposit, and a 15% charge may apply to certain transactions funded via card or bank transfer.

1. Log in and go to the cashier.
2. Select Withdrawal and pick a supported method.
3. Enter the amount and a blockchain address, bank account or wallet.
4. Complete any identity check that appears.
5. Review the details and confirm.
6. Money lands after casino handling ends and the banks or networks settle.

## Crypto Welcome Bonus and the Alternatives
Longfu88 keeps two first-deposit packages apart, and their figures are never added together. The crypto one, the Casino Crypto Welcome Bonus, pays 188% up to 2,888 USDT on a minimum deposit of 50 USDT. It stays valid for 10 days and carries a 40x requirement on deposit plus bonus. Eligible coins are USDC, BTC, LTC, USDT, BCH, XRP and ETH, and a bonus bet may not exceed 5 USDT per spin. Make the first qualifying crypto deposit to claim it.

The fiat package, the Casino Welcome Bonus, adds 18 free spins to a 188% match. This Longfu88 bonus tops out at €2,088 and needs a first qualifying deposit of €50, not the casino-wide €10 minimum. Newly registered players are eligible, with one welcome offer per account. For a €30 deposit, the Live Casino Welcome Bonus returns 125% up to €888 instead. The Casino Welcome Bonus and the Crypto Welcome Bonus replace each other as first-deposit offers. Activation happens inside My Bonuses, ahead of any wager, and no Longfu88 promo code is needed.

- Sign up and enter the requested personal details.
- Fund the first qualifying deposit.
- Activate the bonus in My Bonuses before betting.
- Meet the wagering on eligible games within the validity period.

### Wagering and Caps of the Fiat Welcome Bonus
The fiat welcome package carries a short list of terms.

| Condition | Value |
|---|---|
| Wagering | 25x applied to deposit plus bonus amount |
| Maximum bet | €22.5 per spin |
| Free spins wagering | 40x Free Spins winnings |
| Validity | 10 days from activation |
| Maximum cashout | 5x the initial bonus amount |

Money sent through Neteller or Skrill does not qualify, and a second bonus cannot run beside an active one. A player who requests a withdrawal before claiming the offer, or during its run, may lose eligibility. Cancelling removes the bonus funds and the winnings not yet converted, so it is worth finishing the wagering before the 10 days pass. Verification may be demanded before bonus winnings are released.

---

## SECTION
Write the blocks b07, b08 in ONE answer, in this order. They are one continuous section of the page: the sub-sections continue the parent, so the text must flow from block to block without repeating itself. Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts.

---

## BLOCK BRIEF
Block: b07, H2 "Crypto Reloads and Weekly Offers" (under H1 "Longfu88 Casino for Crypto Players in Singapore: Review")
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): b08 H3 "Cashback and Rebates"
Word Count: 128-162 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 162, but never beyond 178 words.
Format: paragraph + table. Visual Elements: Table — 4 of 5 tables on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu": 0 (do not use)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Weekly Reload [9]
- Weekend Reload [8]
- Crypto Reload [7]
- One-Day Reload Special [5]
- Seasonal Promotion [5]
- Free Spins [5]
Entity Connections to state explicitly [priority]:
- Weekly Reload → grants → 50 Free Spins [7]
- Promotions → do not stack with → another casino bonus that is already running [8]
Summary: Recurring reloads and special campaigns in a comparison table (reward, minimum deposit, wagering, validity), with the rules they share.
Copywriter Notes: Reload offers in one table. Lead-in sentence first; the table underneath it (Markdown) has one column per attribute, in this order: Offer, Reward, Min. deposit, Wagering, Validity. It covers seven offers as given. Row order: Casino Weekly Crypto Reload and Casino Weekend Crypto Reload first, then Casino Weekly Reload, Casino Weekend Reload, Casino Double Fortune (one-day reload special), Casino Trick or Treat Pumpkin Bonanza, Casino Dragon Quest (verification reward). Rules common to all offers, stated once below the table: the maximum bet is €5 per spin as long as bonus money is in play; every claim is switched on inside My Bonuses; within one promotional period only a single claim can be made; combining with a casino bonus that is already active is not possible. Use no tracked keyword in the body of this block.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_promotions.other_bonuses[2]: {"name": "Casino Weekly Reload", "type": "Weekly free spins", "reward": "50 Free Spins", "minimum_deposit": "€30", "wagering_requirement": "40x winnings from Free Spins", "validity": "7 days", "claiming_method": "A fulfilled set of eligibility and deposit conditions leads to the activation step in My Bonuses.", "eligibility": "The target group is registered players that comply with the qualification rules defined for the offer.", "important_terms": ["Up to €5 may be staked per spin, and no more, while wagering bonus funds.", "Two active casino bonuses cannot be combined at once.", "As a rule, each promotional period yields a single claim, exceptions aside."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[3]: {"name": "Casino Weekly Crypto Reload", "type": "Crypto weekly reload", "reward": "60% up to 1,000 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus", "validity": "7 days", "claiming_method": "A fulfilled set of eligibility and deposit conditions leads to the activation step in My Bonuses.", "eligibility": "The target group is registered players that comply with the qualification rules defined for the offer.", "important_terms": ["Two active casino bonuses cannot be combined at once.", "As a rule, each promotional period yields a single claim, exceptions aside.", "Up to €5 may be staked per spin, and no more, while wagering bonus funds."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[4]: {"name": "Casino Weekend Reload", "type": "Weekend deposit bonus", "reward": "Up to €3,360 + 50 Free Spins", "minimum_deposit": "€50", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "A fulfilled set of eligibility and deposit conditions leads to the activation step in My Bonuses.", "eligibility": "The target group is registered players that comply with the qualification rules defined for the offer.", "important_terms": ["Two active casino bonuses cannot be combined at once.", "As a rule, each promotional period yields a single claim, exceptions aside.", "Up to €5 may be staked per spin, and no more, while wagering bonus funds."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[5]: {"name": "Casino Weekend Crypto Reload", "type": "Weekend crypto bonus", "reward": "75% up to 750 USDT + 100 Free Spins", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "A fulfilled set of eligibility and deposit conditions leads to the activation step in My Bonuses.", "eligibility": "The target group is registered players that comply with the qualification rules defined for the offer.", "important_terms": ["Up to €5 may be staked per spin, and no more, while wagering bonus funds.", "As a rule, each promotional period yields a single claim, exceptions aside.", "Two active casino bonuses cannot be combined at once."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[6]: {"name": "Casino Double Fortune: One-Day Reload Special", "type": "One-day reload", "reward": "50% up to €500", "minimum_deposit": "€30", "wagering_requirement": "30x deposit plus bonus", "validity": "24 hours", "claiming_method": "A fulfilled set of eligibility and deposit conditions leads to the activation step in My Bonuses.", "eligibility": "The target group is registered players that comply with the qualification rules defined for the offer.", "important_terms": ["Up to €5 may be staked per spin, and no more, while wagering bonus funds.", "Two active casino bonuses cannot be combined at once.", "As a rule, each promotional period yields a single claim, exceptions aside."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[7]: {"name": "Casino Trick or Treat Pumpkin Bonanza", "type": "Seasonal casino promotion", "reward": "Up to 100 Free Spins", "minimum_deposit": "€20", "wagering_requirement": "40x Free Spins winnings", "validity": "7 days", "claiming_method": "A fulfilled set of eligibility and deposit conditions leads to the activation step in My Bonuses.", "eligibility": "The target group is registered players that comply with the qualification rules defined for the offer.", "important_terms": ["Up to €5 may be staked per spin, and no more, while wagering bonus funds.", "Two active casino bonuses cannot be combined at once.", "As a rule, each promotional period yields a single claim, exceptions aside."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[8]: {"name": "Get Verified and Get Extra forms the pitch of the casino's Dragon Quest", "type": "Verification reward", "reward": "€10 bonus credit", "minimum_deposit": "€20", "wagering_requirement": "30x promotional credit", "validity": "7 days", "claiming_method": "A fulfilled set of eligibility and deposit conditions leads to the activation step in My Bonuses.", "eligibility": "Account holders who answer a verification request and complete it during the campaign.", "important_terms": ["Two active casino bonuses cannot be combined at once.", "Up to €5 may be staked per spin, and no more, while wagering bonus funds.", "As a rule, each promotional period yields a single claim, exceptions aside."]}; keep exactly: 5, dragon quest, get verified and get extra, my bonuses

---

## BLOCK BRIEF
Block: b08, H3 "Cashback and Rebates" (under H2 "Crypto Reloads and Weekly Offers")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 83-106 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 106, but never beyond 116 words.
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
- Weekly Cashback [10]
- Live Casino Cashback [8]
- Unlimited Rebate [7]
- VIP Cashback Rates [6]
Entity Connections to state explicitly [priority]:
- Weekly Cashback → returns → 10% of net losses at most, counted across the week [9]
- Rebates → are credited → each day [7]
Summary: Weekly and live casino cashback including the VIP rates, plus the daily rebates per game category.
Copywriter Notes: Cashback and rebates, two layers. Casino Weekly Cashback: the Monday credit goes to My Bonuses; cashback wagering is 10x; opting in is valid for a cycle of four weeks; the week runs Monday (00:00 UTC) through Sunday (23:59 UTC); with a ceiling of €6,988, the refund tops out at 10% of the net loss the player ran up on casino play over those seven days. VIP tier decides the rate, and one sentence lists tier, percentage and cap: Rates by tier: Bronze, Silver, Gold, Platinum, Diamond = 2%, 4%, 6%, 8%, 10%. Live Casino Cashback: 25% up to €850. Daily rebates, packed into one sentence, with P2P at 0.8%, casino at 0.9% and both live casino and lottery at 1.0%, each carrying 1x wagering. What counts is wagering from the real-money balance; bonus funds never qualify. Percentages tied to VIP levels live in the VIP section, and these tier rates here (weekly cashback) must never be blended with them. Use no tracked keyword in the body of this block.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_promotions.other_bonuses[9]: {"name": "Casino Weekly Cashback", "type": "Casino cashback", "reward": "Up to 10% of weekly net casino losses, capped at €6,988", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "minimum_cashback": "€4.5", "opt_in": "An opt-in is required for the four-week cycle, with active accounts able to be renewed automatically.", "crediting": "Once the credit is placed in My Bonuses on Monday, activation is still necessary.", "wagering_requirement": "10x cashback before withdrawal", "cashback_by_vip": [{"level": "VIP Bronze", "percentage": 2, "maximum": "€1,888"}, {"level": "VIP Silver", "percentage": 4, "maximum": "€2,388"}, {"level": "VIP Gold", "percentage": 6, "maximum": "€2,988"}, {"level": "VIP Platinum", "percentage": 8, "maximum": "€3,988"}, {"level": "VIP Diamond", "percentage": 10, "maximum": "€6,988"}], "important_terms": ["A real-money casino bet or its winnings counts, but anything tied to bonus funds is excluded.", "Expiration awaits any weekly cashback that goes unactivated during its claim window."]}; keep exactly: my bonuses, monday
- brandinfo_promotions.other_bonuses[10]: {"name": "Live Casino Cashback", "type": "Live casino cashback", "reward": "25% up to €850", "minimum_cashback": "€4.5", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "crediting": "The Monday credit arrives in My Bonuses, yet it needs an opt-in step and an activation step.", "wagering_requirement": "10x credited cashback", "important_terms": ["The base comes from Live Casino games that are eligible, using stakes in real money with winnings removed.", "Funds sitting in bonus balances are omitted when cashback is computed."]}; keep exactly: my bonuses, monday, live casino
- brandinfo_promotions.other_bonuses[11]: {"name": "Unlimited Casino Rebate", "type": "Rebate", "rebate_percentage": 0.9, "calculation": "Real money wagers count once settled, provided they were on the relevant game category.", "crediting": "Daily, the rewards balance is where the rebate is credited.", "wagering_requirement": "1x credited rebate", "eligibility": "Registration plus qualifying settled wagers makes a player eligible."}
- brandinfo_promotions.other_bonuses[12]: {"name": "Unlimited Live Casino Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Real money wagers count once settled, provided they were on the relevant game category.", "crediting": "Daily, the rewards balance is where the rebate is credited.", "wagering_requirement": "1x credited rebate", "eligibility": "Registration plus qualifying settled wagers makes a player eligible."}
- brandinfo_promotions.other_bonuses[13]: {"name": "Unlimited P2P Rebate", "type": "Rebate", "rebate_percentage": 0.8, "calculation": "Real money wagers count once settled, provided they were on the relevant game category.", "crediting": "Daily, the rewards balance is where the rebate is credited.", "wagering_requirement": "1x credited rebate", "eligibility": "Registration plus qualifying settled wagers makes a player eligible."}
- brandinfo_promotions.other_bonuses[14]: {"name": "Unlimited Lottery Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Real money wagers count once settled, provided they were on the relevant game category.", "crediting": "Daily, the rewards balance is where the rebate is credited.", "wagering_requirement": "1x credited rebate", "eligibility": "Registration plus qualifying settled wagers makes a player eligible."}
