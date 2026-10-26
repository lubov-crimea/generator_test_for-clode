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
Country / GEO: Singapore
Language: English (en). Write ONLY in this language.
Page intent: Brand-review page about the Longfu88 online casino for players from Singapore, built as a balanced guide: the fact table, a pros and cons table straight after it, what the casino is, licence and privacy, registration and verification, the welcome bonus, reloads and cashback, VIP levels, games and providers, sports betting, deposits and withdrawals, mobile use, responsible gambling, support, a detailed FAQ of six answers and a closing note. Page voice: explanatory and neutral, every section opens with the question a reader would ask (never written as a question) and answers it in the first two sentences, sentences of about 16 words, paragraphs of two to three sentences; a figure is always followed by what it means in practice; one call to action at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Review for Singapore: Questions Answered (90-116 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Singapore.
b02   H2 Core Facts (95-121 words): A fact sheet of the casino: operator, licence, launch year, currencies, languages, payment methods, welcome bonus, minimum deposit, cashback, VIP tiers, Minimum age, support.
b03   H2 Pros and Cons Summary (50-64 words): A pros and cons table built only from facts stated elsewhere on the page.
b04   H2 What the Casino Is (80-100 words): What the casino is for a player from Singapore: launch year, account currencies, the official website and who may play.
b05   H2 Licence and Privacy (133-168 words): Who licenses and runs the casino (jurisdiction, operator, registration number) and how personal data and accounts are protected.
b06   H2 Registration and Login Steps (123-157 words): How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.
b07     H3 Verification Rules (90-116 words): When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.
b08   H2 Welcome Offer (128-162 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b09     H3 Wagering Terms (90-116 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b10   H2 VIP Programme (97-123 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b11   H2 Reload and Special Campaigns (110-139 words): The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
b12     H3 Cashback and Rebate Details (72-93 words): Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
b13   H2 Casino Games (80-100 words): The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.
b14     H3 Slot Examples (84-107 words): Three example slots with their provider, RTP, volatility and maximum multiplier.
b15     H3 Live Dealers (84-107 words): The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.
b16   H2 Game Studios (67-84 words): Which studios supply the games, named from the provider list.
b17   H2 Deposit Methods (122-154 words): Deposit methods grouped by type with the general limits and speed, the local options for Singapore and the six-step deposit route.
b18     H3 Withdrawal Rules (110-139 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b19   H2 Sportsbook (139-177 words): Sports and bet types, live betting and the sports bonuses with the shared odds rule.
b20   H2 Mobile Use (90-116 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b21   H2 Support Contacts (67-84 words): Support channels, availability and languages.
b22   H2 Safer Gambling (90-116 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b23   H2 Detailed FAQ (211-269 words): Short answers on minimum deposit, verification time, one account, the app question, withdrawal time, claiming the bonus.
b24   H2 Closing Thoughts (80-100 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Review for Singapore: Questions Answered
Longfu88 is an online casino that combines slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery and crash and instant games with a sportsbook, and it launched in 2026. This review is written for adult players from Singapore, who must be at least 18 years old to take part. Each section answers one practical question: the key facts, the licence, bonuses, games, payments, mobile play and responsible gambling. Conditions are placed next to the figures they belong to, so a reader can weigh the offer before deciding anything.

## Core Facts
| Parameter | Details |
|---|---|
| Operator | Lumina, also the data controller |
| Licence | Costa Rica jurisdiction, held by operator Lumina under registration number 000-039123-R-319326-001 |
| Launched | Launch year 2026 |
| Currencies | EUR, USD, MYR, THB, SGD, USDT |
| Support languages | English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese |
| Payment methods | Visa, Mastercard, Bank Transfer, Bitcoin, USDT (TRC20), PayNow |
| Welcome bonus | 188% bonus up to €2,088 + 18 Free Spins |
| Minimum deposit | €10 general minimum |
| Cashback | Up to 10% of weekly net casino losses |
| VIP tiers | Five tiers: Bronze, Silver, Gold, Platinum, Diamond |
| Minimum age | 18 years old |
| Support | E-mail support@longfu88.com and 24/7 live chat |

## Pros and Cons Summary
The advantages below are balanced against the conditions that come with them.

| Pros | Cons |
|---|---|
| General minimum deposit of €10 | Welcome bonus needs a €50 deposit and 25x wagering on deposit plus bonus |
| Wide choice of payment methods, including cryptocurrencies | Bank withdrawals can take several business days |
| Weekly cashback of up to 10% | A 10% or 15% commission may apply to withdrawals under the turnover rule |
| 24/7 live chat | Verification may delay the first payout |

## What the Casino Is
A player from Singapore meeting this brand for the first time needs a few basics. The online casino was launched in 2026, and accounts can be held in EUR, USD, MYR, THB, SGD or USDT, so a Singapore dollar balance is possible. Players should open the Longfu 88 Official Site address directly and avoid look-alike pages. Eligibility is straightforward: players must be at least 18 and legally permitted to gamble where they live. Longfu88 also expects accurate registration details, one personal account per player and no third-party payment methods.

## Licence and Privacy
The gambling licence is registered in Costa Rica and held by the operator Lumina under registration number 000-039123-R-319326-001. It is the only licence stated for casino Longfu88. Lumina also acts as the data controller, the party that decides how personal data is used, and its data protection officer can be reached at dpo@longfu88.com. Personal data may be shared with payment service providers, identity verification providers, technology providers and, when required, regulators and law enforcement. Players hold the rights of access, rectification, erasure where legally permitted, restriction, objection, portability where applicable and withdrawal of consent, which in practice lets a player ask what is held on the account and request corrections. The operator protects accounts, payments and personal data with technical and organisational safeguards, but the account holder remains responsible for safeguarding credentials. Activity may also be suspended for verification or suspected abuse.

## Registration and Login Steps
A player opens an account by email in five steps, and registration requires email, password, legal name, date of birth and residential address.

1. Open Longfu88 and select Register.
2. Enter email and create a password.
3. Confirm age and acceptance of Terms and Conditions and Privacy Policy.
4. Complete the additional personal details and residential address.
5. Select Create Account and complete any requested email confirmation.

A player searching for the Longfu caino login page needs the same short route: select Login on the website, enter the registered email and password, and complete any security check. The Longfu88 login uses email and password only. If the password is forgotten, choose Forgot Password on the login screen, request a reset link with the registered email and follow the emailed instructions to set a new one. Each player may hold only one personal account, so a second registration is not an option.

### Verification Rules
Verification may be required before a withdrawal, and it can also follow an account review, unusual or high-value transactions or changes to account or payment details. KYC verification confirms who owns the account, and these documents are accepted:

- Identity: passport, national identity card or driving licence
- Address: utility bill or bank statement
- Payment method: bank, card or digital wallet ownership evidence
- Source of funds, when requested: proof of income, bank statements or other supporting financial documents

Documents can be sent within up to 30 days of a request, and a complete set is normally reviewed within 10 days. Withdrawals may be held until the checks are done, and failed checks can lead to refused transactions or account restrictions.

## Welcome Offer
The main offer for a new player is the Casino Welcome Bonus, a first deposit casino bonus at Longfu88. On a first deposit, the Longfu88 bonus gives 188% up to €2,088 plus 18 Free Spins. It is meant for new registered players making their first qualifying deposit, with one welcome offer per account. This offer needs a minimum deposit of €50, which is separate from the general minimum of €10. Four steps lead to the bonus:

- Register an account and complete the required personal details.
- Make the first qualifying deposit.
- Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.
- Play eligible casino games and complete the wagering before expiry.

No promo code step is part of this claiming procedure: the route is the My Bonuses activation after the qualifying deposit. Two alternatives exist, the Live Casino Welcome Bonus (125% up to €888, minimum deposit €30) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, minimum deposit 50 USDT). Both the Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers. Register and claim the Casino Welcome Bonus with the first deposit.

### Wagering Terms
The terms behind the Casino Welcome Bonus decide how much of it can be withdrawn, so they belong before the first deposit rather than after it.

| Condition | Value |
|---|---|
| Wagering | 25x the deposit plus bonus amount |
| Free Spins wagering | 40x Free Spins winnings |
| Validity | 10 days from activation |
| Maximum bet | €22.5 per spin |
| Maximum cashout | 5x the initial bonus amount |

Wagering is counted on the combined deposit and bonus, not on the bonus alone. Neteller and Skrill deposits are excluded, and only one promotional bonus may be active at a time. A withdrawal request before claiming or while the bonus is active can void eligibility, cancelling forfeits bonus funds and unconverted winnings, and verification may be required before bonus winnings are paid.

## VIP Programme
The Longfu88 VIP Program rewards eligible real-money play: VIP points are earned through it and unlock numbered reward levels. There are 25 levels, grouped into the tiers Bronze, Silver, Gold, Platinum and Diamond. Higher levels raise the withdrawal limit and cashback, and from level 4 a personal VIP manager and personalised offers are added, so the programme mainly suits players who stay active over time. Reward and withdrawal limits may differ by VIP level and currency, and the rules can change.

| Level | Points | Reward | Cashback | Withdrawal limit |
|---|---|---|---|---|
| 1 | 1 | €9.8 | 1% | €9,800 |
| 5 | 70 | €24.5 | 2% | €34,300 |
| 10 | 700 | €147 | 4% | €63,700 |
| 15 | 2,100 | €392 | 6% | €88,200 |
| 20 | 3,600 | €637 | 8% | €117,600 |
| 25 | 5,500 | €980 | 10% | €147,000 |

---

## SECTION
Write the blocks b11, b12 in ONE answer, in this order. They are one continuous section of the page: the sub-sections continue the parent, so the text must flow from block to block without repeating itself. Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts.

---

## BLOCK BRIEF
Block: b11, H2 "Reload and Special Campaigns" (under H1 "Longfu88 Casino Review for Singapore: Questions Answered")
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): b12 H3 "Cashback and Rebate Details"
Word Count: 110-139 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 139, but never beyond 166 words.
Format: paragraph + list. Visual Elements: Bulleted/numbered list — 4 of 8 lists on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Longfu caino login": 0 (do not use)
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
- Weekly Reload → gives → 50 Free Spins [7]
- Promotions → cannot be combined with → another active casino bonus [8]
Summary: The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
Copywriter Notes: One lead-in sentence, then a bulleted list with one bullet per offer (the name in bold, then reward, minimum deposit, wagering and validity) for the seven offers as given: Casino Weekly Reload, Casino Weekly Crypto Reload, Casino Weekend Reload, Casino Weekend Crypto Reload, Casino Double Fortune (one-day reload special), Casino Trick or Treat Pumpkin Bonanza, Casino Dragon Quest (verification reward). After the table state the shared rules once: activation in My Bonuses, one claim per promotional period, no combination with another active casino bonus, maximum stake €5 per spin while wagering bonus funds. Use no tracked keyword in the body of this block.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_promotions.other_bonuses[2]: {"name": "Casino Weekly Reload", "type": "Weekly free spins", "reward": "50 Free Spins", "minimum_deposit": "€30", "wagering_requirement": "40x winnings from Free Spins", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}
- brandinfo_promotions.other_bonuses[3]: {"name": "Casino Weekly Crypto Reload", "type": "Crypto weekly reload", "reward": "60% up to 1,000 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}
- brandinfo_promotions.other_bonuses[4]: {"name": "Casino Weekend Reload", "type": "Weekend deposit bonus", "reward": "Up to €3,360 + 50 Free Spins", "minimum_deposit": "€50", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}
- brandinfo_promotions.other_bonuses[5]: {"name": "Casino Weekend Crypto Reload", "type": "Weekend crypto bonus", "reward": "75% up to 750 USDT + 100 Free Spins", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}
- brandinfo_promotions.other_bonuses[6]: {"name": "Casino Double Fortune: One-Day Reload Special", "type": "One-day reload", "reward": "50% up to €500", "minimum_deposit": "€30", "wagering_requirement": "30x deposit plus bonus", "validity": "24 hours", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}
- brandinfo_promotions.other_bonuses[7]: {"name": "Casino Trick or Treat Pumpkin Bonanza", "type": "Seasonal casino promotion", "reward": "Up to 100 Free Spins", "minimum_deposit": "€20", "wagering_requirement": "40x Free Spins winnings", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Registered players meeting the offer-specific qualification rules.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}
- brandinfo_promotions.other_bonuses[8]: {"name": "Casino Dragon Quest: Get Verified and Get Extra!", "type": "Verification reward", "reward": "€10 bonus credit", "minimum_deposit": "€20", "wagering_requirement": "30x promotional credit", "validity": "7 days", "claiming_method": "Activate the offer in My Bonuses after meeting its eligibility and deposit conditions.", "eligibility": "Players who complete requested account verification during the campaign.", "important_terms": ["One claim per promotional period unless otherwise stated.", "Cannot be combined with another active casino bonus.", "Maximum stake while wagering bonus funds: €5 per spin."]}

---

## BLOCK BRIEF
Block: b12, H3 "Cashback and Rebate Details" (under H2 "Reload and Special Campaigns")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 72-93 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 93, but never beyond 111 words.
Format: paragraph + table. Visual Elements: Table — 5 of 7 tables on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu caino login": 0 (do not use)
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
- Weekly Cashback → returns → up to 10% of weekly net casino losses [9]
- Rebates → are credited → daily [7]
Summary: Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
Copywriter Notes: Cover the Casino Weekly Cashback (up to 10% of weekly net casino losses, capped at €6,988; period Monday 00:00 UTC to Sunday 23:59 UTC; opt-in for a four-week cycle; credited to My Bonuses on Monday; 10x wagering of the cashback; the rate depends on the VIP tier: Bronze 2%, Silver 4%, Gold 6%, Platinum 8%, Diamond 10%, shown as a compact table of tier, percentage and maximum) and the Live Casino Cashback (25% up to €850). Mention the four daily rebates in one sentence (casino 0.9%, live casino 1.0%, P2P 0.8%, lottery 1.0%, each with 1x wagering). Only real-money bets count, bonus funds do not. The tier percentages here belong to the weekly cashback; do not mix them with the VIP level percentages of the VIP section. Use no tracked keyword in the body of this block.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_promotions.other_bonuses[9]: {"name": "Casino Weekly Cashback", "type": "Casino cashback", "reward": "Up to 10% of weekly net casino losses, capped at €6,988", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "minimum_cashback": "€4.5", "opt_in": "Opt in for a four-week cycle; active accounts can renew automatically.", "crediting": "Credited to My Bonuses on Monday; activation required.", "wagering_requirement": "10x cashback before withdrawal", "cashback_by_vip": [{"level": "VIP Bronze", "percentage": 2, "maximum": "€1,888"}, {"level": "VIP Silver", "percentage": 4, "maximum": "€2,388"}, {"level": "VIP Gold", "percentage": 6, "maximum": "€2,988"}, {"level": "VIP Platinum", "percentage": 8, "maximum": "€3,988"}, {"level": "VIP Diamond", "percentage": 10, "maximum": "€6,988"}], "important_terms": ["Only real-money casino bets and winnings count; bonus funds excluded.", "Weekly cashback expires if it is not activated within its claim window."]}
- brandinfo_promotions.other_bonuses[10]: {"name": "Live Casino Cashback", "type": "Live casino cashback", "reward": "25% up to €850", "minimum_cashback": "€4.5", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "crediting": "Credited to My Bonuses on Monday; opt-in and activation required.", "wagering_requirement": "10x credited cashback", "important_terms": ["Based on real-money stakes less winnings in eligible Live Casino games.", "Bonus balances are excluded from cashback calculations."]}
- brandinfo_promotions.other_bonuses[11]: {"name": "Unlimited Casino Rebate", "type": "Rebate", "rebate_percentage": 0.9, "calculation": "Qualifying settled real-money wagering on the relevant game category.", "crediting": "Rebate credited daily to the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Registered players with qualifying settled wagers."}
- brandinfo_promotions.other_bonuses[12]: {"name": "Unlimited Live Casino Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Qualifying settled real-money wagering on the relevant game category.", "crediting": "Rebate credited daily to the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Registered players with qualifying settled wagers."}
- brandinfo_promotions.other_bonuses[13]: {"name": "Unlimited P2P Rebate", "type": "Rebate", "rebate_percentage": 0.8, "calculation": "Qualifying settled real-money wagering on the relevant game category.", "crediting": "Rebate credited daily to the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Registered players with qualifying settled wagers."}
- brandinfo_promotions.other_bonuses[14]: {"name": "Unlimited Lottery Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Qualifying settled real-money wagering on the relevant game category.", "crediting": "Rebate credited daily to the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Registered players with qualifying settled wagers."}
