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
Page intent: Brand-review page about the Longfu88 online casino for players from Singapore, built as a balanced guide: the fact table, a pros and cons table straight after it, what the casino is, licence and privacy, registration and verification, the welcome bonus, reloads and cashback, VIP levels, games and providers, sports betting, deposits and withdrawals, mobile use, responsible gambling, support, a detailed FAQ of six answers and a closing note. Page voice: explanatory and neutral, every section opens with the question a reader would ask (never written as a question) and answers it in the first two sentences, sentences of about 16 words, paragraphs of two to three sentences; a figure is always followed by what it means in practice; one call to action at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Review for Singapore: What to Know First (96-122 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Singapore.
b02   H2 Casino Facts (95-121 words): A fact sheet of the casino: operator, launch year, licence, languages, currencies, payment methods, welcome bonus, cashback, minimum deposit, Minimum age, VIP tiers, support.
b03   H2 Pros and Cons Table (53-67 words): A pros and cons table built only from facts stated elsewhere on the page.
b04   H2 About the Casino (83-106 words): What the casino is for a player from Singapore: launch year, account currencies, the official website and who may play.
b05   H2 Licence and Data Protection (141-178 words): Who licenses and runs the casino (jurisdiction, operator, registration number) and how personal data and accounts are protected.
b06   H2 Registration and Login (123-157 words): How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.
b07     H3 Identity Verification (96-122 words): When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.
b08   H2 Welcome Bonus (133-171 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b09     H3 Wagering and Limits (96-122 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b10   H2 Reloads and Special Offers (115-146 words): The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
b11     H3 Cashback and Rebates (77-97 words): Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
b12   H2 VIP Levels (102-130 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b13   H2 Games (83-106 words): The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.
b14     H3 Slots (90-113 words): Three example slots with their provider, RTP, volatility and maximum multiplier.
b15     H3 Live Casino (90-113 words): The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.
b16   H2 Game Providers (70-90 words): Which studios supply the games, named from the provider list.
b17   H2 Sports Betting (146-187 words): Sports and bet types, live betting and the sports bonuses with the shared odds rule.
b18   H2 Mobile Play (96-122 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b19   H2 Deposits (128-162 words): Deposit methods grouped by type with the general limits and speed, the local options for Singapore and the six-step deposit route.
b20     H3 Withdrawals (115-146 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b21   H2 Support (70-90 words): Support channels, availability and languages.
b22   H2 Responsible Gambling (96-122 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b23   H2 Frequently Asked Questions (211-269 words): Short answers on claiming the bonus, minimum deposit, verification time, one account, the app question, withdrawal time.
b24   H2 Conclusion (83-106 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Review for Singapore: What to Know First
Longfu88 is an online casino launched in 2026 that combines casino games, live dealer games, sports betting and lottery on one site. The lobby covers slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery and crash and instant games, and a sportsbook sits beside them. Play is meant for adults, so every player must be at least 18 years old.

This page is written for players from Singapore. It starts with the key facts and then covers the licence, registration, bonuses, games, payments, mobile play and responsible gambling. Advantages and the conditions that come with them are set side by side, so the picture stays balanced.

## Casino Facts
| Parameter | Details |
|---|---|
| Operator | Lumina, also the data controller |
| Launched | 2026 |
| Licence | Costa Rica licence held by operator Lumina, registration number 000-039123-R-319326-001 |
| Support languages | English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese |
| Currencies | EUR, USD, MYR, THB, SGD, USDT |
| Payment methods | Visa, Mastercard, Bank Transfer, Bitcoin, USDT (TRC20), PayNow |
| Welcome bonus | 188% up to €2,088 + 18 Free Spins on the first qualifying deposit |
| Cashback | Up to 10% of weekly net casino losses, capped at €6,988 |
| Minimum deposit | €10 (general minimum) |
| Minimum age | 18 years |
| VIP tiers | Five tiers: Bronze, Silver, Gold, Platinum, Diamond |
| Support | support@longfu88.com and 24/7 live chat |

## Pros and Cons Table
Each advantage below is balanced against a condition that comes with it.

| Pros | Cons |
|---|---|
| Low general minimum deposit of €10 | Welcome Bonus needs a €50 deposit and 25x wagering |
| Many payment methods, including cryptocurrencies | A 10% or 15% commission can apply to withdrawals |
| Weekly cashback of up to 10% | Bank withdrawals can take several business days |
| VIP programme with 25 levels and 24/7 live chat | Verification may delay the first payout |

## About the Casino
Longfu88 is an online casino launched in 2026 that opens accounts in six currencies: EUR, USD, MYR, THB, SGD and USDT. Singapore dollars are on the list, so a player from Singapore can keep the balance in SGD. Players should use the Longfu 88 Official Site address and avoid look-alike pages, because a copied site is not the casino itself.

Eligibility is straightforward. Players must be 18 or older and legally permitted to gamble where they live. Each player may hold one personal account, registered with accurate information, and pays only with methods in their own name.

## Licence and Data Protection
The gambling licence of the casino Longfu88 is issued in Costa Rica and held by the operator Lumina, under registration number 000-039123-R-319326-001. That is the only licence the casino names, and nothing here says anything about its status in Singapore. Lumina also acts as the data controller, and the data protection officer can be reached at dpo@longfu88.com.

Personal data may be shared with payment service providers, identity verification providers, technology providers and, when required, regulators and law enforcement. Players keep several rights over that data: access, rectification, erasure where legally permitted, restriction, objection, portability where applicable and withdrawal of consent. A player who wants to use one of them can start with a request to the officer at the address above.

The operator protects accounts, payments and personal information with technical and organisational safeguards. Responsibility is shared, though: the account holder must safeguard credentials, so passwords should stay private, and activity may be suspended for verification or suspected abuse.

## Registration and Login
A player opens an account by email in five steps, and registration requires an email, a password, a legal name, a date of birth and a residential address.

1. Open Longfu88 and select Register.
2. Enter email and create a password.
3. Confirm age and acceptance of Terms and Conditions and Privacy Policy.
4. Complete the additional personal details and residential address.
5. Select Create Account and complete any requested email confirmation.

Each player may hold only one personal account, and the age confirmation means 18+ and the legal gambling age of the relevant jurisdiction. Returning players use the Longfu88 login: select Login on the website, enter the registered email and password, and complete any security check. If the password is lost, choose Forgot Password on the login screen, request a reset link using the registered email and follow the emailed instructions to set a new one.

### Identity Verification
Verification may be required before a withdrawal, and also after an account review, on unusual or high-value transactions and when account or payment details change. Documents are due within up to 30 days when requested, and a complete set is reviewed within 10 days of receipt. Withdrawals may be held until the checks are done, and failed checks can lead to refused transactions or account restrictions. The documents fall into four groups:

- Identity: passport, national identity card or driving licence
- Address: utility bill or bank statement
- Payment method: bank or card ownership evidence, or digital wallet ownership evidence
- Source of funds, when requested: proof of income, bank statements or other supporting financial documents

## Welcome Bonus
The Casino Welcome Bonus, the Longfu88 bonus for new players, gives 188% up to €2,088 plus 18 Free Spins, that is spins on a slot with the stake paid by the casino. It is a deposit bonus for new registered players on their first qualifying deposit, with one welcome offer per account. The qualifying minimum deposit of this offer is €50, which is higher than the general minimum of €10 and applies only here. Claiming takes four steps:

- Register an account and complete the required personal details.
- Make the first qualifying deposit.
- Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.
- Play eligible casino games and complete the wagering before expiry.

The claiming route is the My Bonuses activation after the qualifying deposit, and no promo code step is part of the listed procedure. Two other first-deposit offers exist: the Live Casino Welcome Bonus (125% up to €888, minimum deposit €30) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, minimum deposit 50 USDT). The Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers, so a player picks one of them. Register at Longfu88 and claim the Casino Welcome Bonus with the first qualifying deposit.

### Wagering and Limits
The terms of the Casino Welcome Bonus fit into five conditions, and the bonus expires 10 days after activation.

| Condition | Value |
|---|---|
| Wagering | 25x the deposit plus bonus amount |
| Free Spins wagering | 40x Free Spins winnings |
| Validity | 10 days from activation |
| Maximum bet | €22.5 per spin |
| Maximum cashout | 5x the initial bonus amount |

Deposits made with Neteller and Skrill are excluded, and only one promotional bonus can be active at a time. A withdrawal request before claiming or while the bonus is active can void eligibility, and cancelling forfeits bonus funds and unconverted winnings. Verification may be required before bonus winnings are paid.

## Reloads and Special Offers
Reloads return a share of a later deposit. Each offer lists reward, minimum deposit and wagering, and validity is 7 days unless noted.

- **Casino Weekly Reload**: 50 Free Spins, €30, 40x winnings from Free Spins.
- **Casino Weekly Crypto Reload**: 60% up to 1,000 USDT, 20 USDT, 30x deposit plus bonus.
- **Casino Weekend Reload**: up to €3,360 + 50 Free Spins, €50, 30x deposit plus bonus, 40x Free Spins winnings.
- **Casino Weekend Crypto Reload**: 75% up to 750 USDT + 100 Free Spins, 20 USDT, 30x deposit plus bonus, 40x Free Spins winnings.
- **Casino Double Fortune**, a one-day reload special: 50% up to €500, €30, 30x deposit plus bonus, 24 hours.
- **Casino Trick or Treat Pumpkin Bonanza**, a seasonal promotion: up to 100 Free Spins, €20, 40x Free Spins winnings.
- **Casino Dragon Quest**: €10 bonus credit, €20, 30x promotional credit.

Every promotion is activated in My Bonuses, allows one claim per period and cannot be combined with another active casino bonus. The maximum stake is €5 per spin while bonus funds are wagered.

### Cashback and Rebates
The Casino Weekly Cashback returns up to 10% of weekly net casino losses, capped at €6,988, for the period from Monday 00:00 UTC to Sunday 23:59 UTC. It needs an opt-in for a four-week cycle, is credited to My Bonuses on Monday and carries 10x wagering. The rate follows the VIP tier:

| Tier | Cashback | Maximum |
|---|---|---|
| Bronze | 2% | €1,888 |
| Silver | 4% | €2,388 |
| Gold | 6% | €2,988 |
| Platinum | 8% | €3,988 |
| Diamond | 10% | €6,988 |

The Live Casino Cashback gives 25% up to €850. Four unlimited rebates are credited daily with 1x wagering: casino 0.9%, live casino 1.0%, P2P 0.8% and lottery 1.0%. Only real-money bets count, not bonus funds.

## VIP Levels
The Longfu88 VIP Program turns eligible real-money play into VIP points, and those points unlock numbered reward levels. There are 25 levels, grouped into the tiers Bronze, Silver, Gold, Platinum and Diamond. Higher levels raise withdrawal limits and cashback, and from level 4 a personal VIP manager joins the personalised offers. The table shows six of the levels:

| Level | Points | Reward | Cashback | Withdrawal limit |
|---|---|---|---|---|
| 1 | 1 | €9.8 | 1% | €9,800 |
| 5 | 70 | €24.5 | 2% | €34,300 |
| 10 | 700 | €147 | 4% | €63,700 |
| 15 | 2,100 | €392 | 6% | €88,200 |
| 20 | 3,600 | €637 | 8% | €117,600 |
| 25 | 5,500 | €980 | 10% | €147,000 |

Reward and withdrawal limits may differ by VIP level and currency, and level-based benefits and the programme rules can change.

## Games
Longfu88 Casino groups its lobby into nine categories: slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games. The range goes beyond classic reels, since jackpots, fishing and crash games sit next to the table games. Fast games and crash games suit short rounds, whereas live dealer games and table games follow the pace of a table. Slots come first below, followed by the live dealer section, and the remaining categories complete what a player at Longfu88 can open from one account.

### Slots
Three example slots show how the key figures differ between titles. Gates of Olympus, from Pragmatic Play, has an RTP of 96.50% and a maximum multiplier of 5,000x, with high volatility. Sweet Bonanza, also from Pragmatic Play, has an RTP of 96.48%, high volatility and a maximum multiplier of 21,175x. Hacksaw Gaming supplies Wanted Dead or a Wild, which has an RTP of 96.38%, very high volatility and a maximum multiplier of 12,500x. RTP is the share of stakes a slot returns to players over a very long run, while volatility describes how large and how frequent the wins tend to be: the higher it is, the more the balance can swing.

### Live Casino
The Live Casino is the part of the lobby built around live dealer games, and it includes the exclusive Longfu88 Baccarat, a game with baccarat gameplay. At Longfu 88 Casino the title is classed as an exclusive live or table game, so a player who likes baccarat has a house game to try beside the studio titles. Evolution and SA Gaming are among the studios that power the Live Casino, which means the section does not depend on a single supplier. Players who prefer a human dealer to a random number generator will find the section built for them. The full provider list follows in its own section.

## Game Providers
Game providers supply the slots, live and table games to Longfu 88, and the list covers Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft and Hacksaw Gaming. Pragmatic Play and Hacksaw Gaming appear in the slot examples above, while Evolution and SA Gaming are named among the live studios. With several studios in one lobby, a player gets a choice of styles inside each category.

## Sports Betting
The sportsbook of Longfu88 covers football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football in the Longfu sports section. Seven bet types are offered: single, accumulator, live, handicap, totals, outrights and Bet Builder. Live betting adds live odds and in-play markets, while event availability and market selection can vary by jurisdiction.

Sports bonuses run apart from the casino offers. The Sport First Deposit Bonus is valid for 30 days.

| Offer | Reward | Min. deposit | Wagering |
|---|---|---|---|
| Sport First Deposit Bonus | 100% up to €1,888 | €50 | 8x |
| Sport Weekly Reload Bonus | 50% up to €2,500 | €50 | 8x |
| Sport Weekend Reload Bonus | 50% up to €3,750 | €50 | 8x |

The Sport Crypto Welcome Bonus, Sport Crypto Weekly Reload and Sport Crypto Weekend Reload are the crypto equivalents. Sports Cashback returns 10% up to €2,500 of eligible sports net losses weekly, and the Unlimited Sports Rebate pays 0.70%. 2 Goals Ahead settles eligible football bets early when the selected team leads by two goals, Parlay Boost adds up to 100% extra winnings on accumulators with at least three legs, and Bet Builder Risk Free returns 50% of the stake up to €250.

Only settled qualifying sports bets count. Single bets need odds of at least 2.00 and each accumulator selection at least 1.50, while voided and cashed-out bets do not qualify.

## Mobile Play
Mobile access runs through a responsive website that works on smartphone and tablet browsers, so the supported platforms are Android, iOS and mobile web. The site can also be added to the home screen as a shortcut, and that shortcut gives quick access to the casino and the sportsbook. Through either route a player reaches account access, deposits, withdrawals and bonuses as well. The routes differ slightly by system.

On Android the shortcut is added in three steps:

1. Open Longfu88 in Chrome.
2. Open browser menu and choose Add to Home screen.
3. Confirm the shortcut.

On iOS the same result takes three steps in Safari:

1. Open Longfu88 in Safari.
2. Tap Share and choose Add to Home Screen.
3. Confirm Add.

---

## SECTION
Write the blocks b19, b20 in ONE answer, in this order. They are one continuous section of the page: the sub-sections continue the parent, so the text must flow from block to block without repeating itself. Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts.

---

## BLOCK BRIEF
Block: b19, H2 "Deposits" (under H1 "Longfu88 Casino Review for Singapore: What to Know First")
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): b20 H3 "Withdrawals"
Word Count: 128-162 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 162, but never beyond 194 words.
Format: paragraph + table. Visual Elements: Table — 7 of 7 tables on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
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
- Payment Methods [10]
- Bank Transfer [7]
- Cryptocurrency [7]
- E-wallets [6]
- Deposit Limits [7]
- Processing Speed [6]
Entity Connections to state explicitly [priority]:
- Deposits → are credited → within 1-2 minutes [8]
- Casino → charges → no processing fee on deposits, while provider or network fees may apply [7]
Summary: Deposit methods grouped by type with the general limits and speed, the local options for Singapore and the six-step deposit route.
Copywriter Notes: One lead-in sentence, then a Markdown table Method type | Examples | Currencies with the groups: local bank and wallet methods, cards (Visa, Mastercard), bank transfer, cryptocurrencies (Bitcoin, Ethereum, Litecoin, USDT in TRC20, ERC20 and BEP20, USDC and others from the list), e-wallets (Neteller, Skrill) and the European methods (Sofort, Giropay). For Singapore highlight PayNow, PayNow QR, DBS Bank and OCBC Bank (SGD) as given. General limits for every method: minimum €10, maximum €5,000 per transaction, speed 1-2 minutes, no casino processing fee, provider or blockchain network fees may apply. Do NOT quote the per-currency limit lines of single methods (they mix euro signs with local-currency amounts) and say that the limits can differ by country, currency and method. Neteller and Skrill deposits are excluded from the welcome bonus. After the table, the six deposit steps in one flowing sentence or two. Keep tracked keywords out of the table. Use "Longfu88" exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_deposit.deposit_methods: [{"method": "BCA", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €5,000 per transaction"]}, {"method": "BNI", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €20, maximum €40,000 per transaction"]}, {"method": "Bank Transfer", "currencies": ["IDR", "MYR", "VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €25, maximum €82,000 per transaction", "MYR: minimum €50, maximum €50,000 per transaction", "VND: minimum €100, maximum €500,000 per transaction"]}, {"method": "Bitcoin", "currencies": ["BTC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €590, maximum €98,490 per transaction", "MYR: minimum €145, maximum €23,840 per transaction", "SGD: minimum €45, maximum €7,560 per transaction", "THB: minimum €1,100, maximum €182,910 per transaction", "VND: minimum €929, maximum €154,949 per transaction"]}, {"method": "Bitcoin Cash", "currencies": ["BCH"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "Cardano", "currencies": ["ADA"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "DANA", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €5,000 per transaction"]}, {"method": "DBS Bank", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €50, maximum €5,000 per transaction"]}, {"method": "DuitNow", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €50,000 per transaction"]}, {"method": "Ethereum", "currencies": ["ETH"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "Giropay", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "GrabPay", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €5,000 per transaction"]}, {"method": "Litecoin", "currencies": ["LTC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "Mandiri", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €20, maximum €40,000 per transaction"]}, {"method": "Mastercard", "currencies": ["IDR", "MYR", "SGD", "VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €200, maximum €30,000 per transaction", "MYR: minimum €50, maximum €9,000 per transaction", "SGD: minimum €18, maximum €3,000 per transaction", "VND: minimum €320, maximum €50,000 per transaction"]}, {"method": "MoMo", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €30,000 per transaction"]}, {"method": "Neteller", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "OCBC Bank", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €50, maximum €5,000 per transaction"]}, {"method": "OVO Wallet", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €2,000 per transaction"]}, {"method": "Online Banking", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €10,000 per transaction"]}, {"method": "PayNow", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €10, maximum €5,000 per transaction"]}, {"method": "PayNow QR", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €10, maximum €5,000 per transaction"]}, {"method": "PromptPay QR", "currencies": ["THB"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["THB: minimum €300, maximum €200,000 per transaction"]}, {"method": "QRIS", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €50,000 per transaction"]}, {"method": "Ripple", "currencies": ["XRP"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "Skrill", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Sofort", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Touch'n Go", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €5,000 per transaction"]}, {"method": "USDC", "currencies": ["USDC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "USDT (BEP20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"], "network": "BEP20"}, {"method": "USDT (ERC20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"], "network": "ERC20"}, {"method": "USDT (TRC20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "VND: minimum €309, maximum €154,949 per transaction"], "network": "TRC20"}, {"method": "VietQR", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €300,000 per transaction"]}, {"method": "ViettelPay", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €20,000 per transaction"]}, {"method": "Visa", "currencies": ["IDR", "MYR", "SGD", "VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €200, maximum €30,000 per transaction", "MYR: minimum €50, maximum €9,000 per transaction", "SGD: minimum €18, maximum €3,000 per transaction", "VND: minimum €320, maximum €50,000 per transaction"]}, {"method": "Zalo", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €100,000 per transaction"]}]
- brandinfo_deposit.deposit_guide: ["Log in to the Longfu88 account.", "Open the cashier and select Deposit.", "Choose an available payment method and its supported currency or blockchain network.", "Enter the amount and payment information.", "Confirm and authorize the transaction using the provider instructions.", "Wait for the funds to be credited to the playable balance."]
- brandinfo_general.minimum_deposit: €10
- brandinfo_general.currencies: ["EUR", "USD", "MYR", "THB", "SGD", "USDT"]
Counting warning: the facts above contain tracked keywords "Longfu88" (x1). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').

---

## BLOCK BRIEF
Block: b20, H3 "Withdrawals" (under H2 "Deposits")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 115-146 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 146, but never beyond 175 words.
Format: paragraph + list. Visual Elements: Bulleted/numbered list — 6 of 8 lists on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
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
- Withdrawal Time [10]
- Withdrawal Methods [8]
- Minimum Withdrawal [7]
- Withdrawal Fees [7]
- Deposit Turnover [6]
Entity Connections to state explicitly [priority]:
- Withdrawal → is processed within → up to 3 business days [9]
- Bank Transfer → may need → 3-5 more business days for delivery [7]
Summary: How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
Copywriter Notes: Give the methods as listed (bank transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT in three networks, Touch'n Go, DANA, MoMo, DBS Bank, Online Banking), the minimum €20 and maximum €5,000, the six steps as a NUMBERED list, and the processing time: card, crypto and wallet withdrawals take 1 to 3 business days; bank transfer takes up to 3 business days for casino processing plus 3 to 5 business days for bank delivery; requests are generally processed within three working days. Where "Lngfu88 withdrawal time" is used, write it verbatim with this spelling in the sentence that gives the processing time. Fees: no standard casino withdrawal fee, provider and blockchain fees may apply; a 10% commission (minimum €2.25) can apply where turnover is below the deposited amount (a minimum 1x deposit turnover can apply before a withdrawal) and 15% on some card or bank transfer funded transactions. Do NOT quote the per-market minimum lines of single methods (they mix euro signs with local-currency amounts). Identity checks can delay a payout (see the verification section). Use "Longfu88" exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_withdrawal.withdrawal_methods: [{"method": "Bank Transfer", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["IDR", "MYR", "VND"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "Visa", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["IDR", "MYR", "SGD", "VND"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "Mastercard", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["IDR", "MYR", "SGD", "VND"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "Bitcoin", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["BTC"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Ethereum", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["ETH"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Litecoin", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["LTC"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "USDT (TRC20)", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "USDT (ERC20)", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "USDT (BEP20)", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Touch'n Go", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["MYR"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "DANA", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["IDR"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "MoMo", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "1–3 business days", "currencies": ["VND"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "DBS Bank", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["SGD"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "Online Banking", "minimum": "€20", "maximum": "€5,000", "fee": "No standard casino withdrawal fee; provider and blockchain fees may apply. A 10% fee (minimum €2.25) can apply to inadequate rollover, and certain card or bank-funded transactions may incur 15%.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["MYR"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Vietnam: minimum €10,000 (VND market)"]}]
- brandinfo_withdrawal.withdrawal_guide: ["Log in to Longfu88 and open the cashier.", "Select Withdrawal and choose a supported destination or payment method.", "Enter the amount and the receiving bank, wallet, or blockchain address.", "Complete identity and payment-method verification if prompted.", "Review the request and confirm submission.", "Wait for casino processing and any bank or network settlement before receiving funds."]
- brandinfo_privacy_policy.terms_conditions.withdrawal_terms: ["A minimum 1x deposit turnover can apply before a withdrawal.", "Withdrawal requests are generally processed within three working days.", "Bank transfers may need another 3–5 business days for settlement.", "The operator may request KYC documents before processing payments."]
- brandinfo_privacy_policy.terms_conditions.conditional_fees: ["Where qualifying turnover is below the deposited amount, a 10% commission may apply with minimum €2.25.", "A 15% charge can apply to some card or bank transfer funded transactions under the casino rules."]
- brandinfo_general.payment_methods.withdrawal: ["Bank Transfer", "Visa", "Mastercard", "Bitcoin", "Ethereum", "Litecoin", "USDT (TRC20)", "USDT (ERC20)", "USDT (BEP20)", "Touch'n Go", "DANA", "MoMo", "DBS Bank", "Online Banking"]
Counting warning: the facts above contain tracked keywords "Longfu88" (x1). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').
