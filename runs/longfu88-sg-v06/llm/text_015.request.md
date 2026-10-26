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
Page intent: Editorial brief for a brand review centred on Longfu88, a sportsbook paired with an online casino, and aimed at adult bettors in Singapore. Planned coverage runs in this order: fact table; sports betting with markets, bet types and live betting; sports bonuses; mobile betting; registration and verification; payments; the casino side with welcome bonus, reloads and cashback; VIP levels; games and providers; licence and safety; responsible betting; support; pros and cons; an FAQ on sports and payouts; a verdict. Register is plain betting vocabulary, with the reader addressed as "you" and sentences averaging about 17 words. Each section opens with the market or bet the reader places and ends on the condition that settles the payout; keep paragraphs short, two to four sentences each. Calls to action sit at the sports first deposit bonus and at the casino welcome bonus. The only source of brand facts is knowledge base longfu88-new in AffBulk, and the page must stay silent on how Singapore law treats the casino.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Sports and Casino Review for Singapore Players (96-122 words): Opening overview: a definition of the online casino, the kinds of play it offers, the year it went live, and the adult Singapore readers this page is written for.
b02   H2 Sports and Casino Facts (88-112 words): Support, minimum deposit and Sports bonus feature in a compact casino fact sheet, next to licence, operator, currencies, languages, payment methods, cashback and welcome bonus, plus Sports.
b03   H2 Sports Betting at the Casino (115-146 words): Sportsbook coverage: the sports and esports available, the range of wagers, and betting while an event is under way.
b04     H3 Sports Bonuses and Boosts (90-113 words): Run-through of the sportsbook offers: the first deposit bonus, weekend and weekly reloads, early payout, parlay boost, cashback and a risk-free bet builder, along with the shared odds requirement.
b05   H2 Betting on Mobile (96-122 words): Using the casino on a phone or tablet, whether on Android, iOS or mobile web: the layout that adapts to screen size, adding a shortcut to the device's home screen, and which account tools can be used from it.
b06   H2 Registration, Login and Verification (173-219 words): The five numbered registration steps, then logging in with password recovery, then document requests: their timing, the documents needed and the length of the review.
b07   H2 Deposits and Withdrawals (249-316 words): Ways to deposit sorted by category, with limits and speed in a table and a short route description, followed by the withdrawal side: which methods, the steps, the time needed and any fees.
b08   H2 Casino Welcome Bonus and Its Terms (191-244 words): Casino Welcome Bonus: figures, claiming route and alternatives, with a final table covering wagering, validity period and bet caps.
b09   H2 Reloads and Cashback (173-219 words): The block opens with a table covering seven reload and seasonal offers, then moves to the weekly cashback with its VIP rates, the live casino cashback and the rebates.
b10   H2 VIP Programme (102-130 words): The VIP programme explained: points earned by staking real money, 25 reward levels arranged in five tiers, and the perks that open up along the way.
b11   H2 Casino Games and Slots (154-194 words): Three sample slots with RTP, volatility and maximum multiplier, preceded by the nine game categories.
b12   H2 Live Casino, Other Games and Providers (218-276 words): A live dealer lobby featuring the exclusive baccarat table, then the other game types and a list of ten providers.
b13   H2 Licence and Security (173-219 words): Begins with when the casino launched, which currencies it supports and who may play, and continues with the licence, the operating company and what protects player data and accounts.
b14   H2 Responsible Betting and Gambling (102-130 words): Responsibility topics: the age limit, e-mail requests for self-exclusion and account closure, self-assessment, and organisations offering help.
b15   H2 Support (70-90 words): Ways to reach support, hours of availability and the languages offered.
b16   H2 Pros and Cons (53-67 words): Table of pros and cons drawing solely on facts already given on the page.
b17   H2 Questions About Sports and Payouts (172-218 words): Short answers on which sports are covered, the sports bonus, minimum deposit, how long withdrawals take, and the support languages.
b18   H2 Verdict for Sports Fans (90-113 words): Short closing verdict: who the casino suits, what to confirm prior to a first deposit, and a closing nudge towards responsible gambling.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Sports and Casino Review for Singapore Players
Longfu88 pairs a sportsbook with a casino, and further play areas sit beside the betting: jackpots, fishing, P2P games, lottery, table games, slots, live dealer games, fast games and a crash and instant category. Since going live in 2026, the platform has kept all of this in one lobby. The online casino combines lottery, sports betting and slot-style and live dealer casino games, which gives bettors a wide choice. Readers of this review are adults living in Singapore, and only people aged 18 or older may join. Later sections cover the brand facts, bonuses, money in and out, mobile play, the licence and responsible gambling, so the fit can be judged before registering.

## Sports and Casino Facts
| Item | Detail |
|---|---|
| Licence | Costa Rica, Lumina, 000-039123-R-319326-001 |
| Operator | Lumina |
| Welcome bonus | 18 free spins, 188% match, maximum €2,088 |
| Cashback | Weekly net casino losses, 10% back, capped at €6,988 |
| Currencies | USDT, USD, MYR, SGD, EUR, THB |
| Support languages | Indonesian, Thai, Malay, English, Simplified Chinese, Vietnamese |
| Payment methods | Visa, PayNow, USDT, Bitcoin, Bank Transfer, Mastercard |
| Sports | Football, Basketball, Tennis, Badminton, Cricket, Volleyball, Table tennis, Esports, Virtual football |
| Sports bonus | 100% up to €1,888, first deposit |
| Minimum deposit | €10 per deposit, any method |
| Support | 24/7 live chat and an email address, support@longfu88.com |

## Sports Betting at the Casino
The sportsbook takes in nine disciplines, led by ball and racket sports: football, basketball, tennis, badminton, table tennis, volleyball and cricket. Virtual football and esports complete the list for bettors who follow gaming events. Longfu88 offers seven bet types: single, accumulator, handicap, totals, outrights, Bet Builder and live. A single wager covers one selection, while an accumulator joins several, so the slip stands or falls on every leg. Live betting supplies in-play markets priced with live odds, which shift as the event unfolds. Football fans can combine these tools in a Bet Builder or follow a match as it develops. Available events and markets may differ with the player's jurisdiction, so the list is worth checking before a wager is placed.

### Sports Bonuses and Boosts
Qualifying bets are subject to an odds floor of 2.00 on single bets, and accumulator legs need 1.50, while voided or cashed-out bets earn nothing. Crypto deposits get USDT versions. Bet Builder Risk Free returns 50% of the stake up to €250, Parlay Boost adds up to 100% to three-leg accumulator winnings, and Sports Cashback pays back 10% of weekly net sports losses, up to €2,500. Unlimited Sports Rebate pays 0.70%, and 2 Goals Ahead settles football bets early.

- **Sport First Deposit Bonus**: provides a match of 100% up to €1,888, €50 minimum, 8x wagering, 30 days
- **Sport Weekly Reload Bonus**: 50% up to €2,500, €50 minimum, 8x wagering
- **Sport Weekend Reload Bonus**: 50% up to €3,750, €50 minimum, 8x wagering

## Betting on Mobile
Mobile play works on Android, iOS and mobile web, because the site is responsive and loads in phone and tablet browsers. The Longfu88 app is simply the site version pinned to the home screen, with no app-store listing or APK file behind it. That shortcut launches the casino and sportsbook with one tap, and bonuses, deposits, withdrawals and account access stay within reach.

On Android, Chrome needs four steps:

1. Open Longfu88 in Chrome.
2. Tap the browser menu button.
3. Choose Add to Home screen.
4. Confirm the shortcut.

On iOS, Safari takes three steps:

1. Open Longfu88 in Safari.
2. Tap Share and select Add to Home Screen.
3. Confirm with Add.

## Registration, Login and Verification
Sign-up collects the legal name, email, password, birth date and home address, with a ceiling of one personal account per player. Five steps lead through it:

1. Go to Longfu88 and press Register.
2. Fill in the email and choose a password.
3. Confirm age and accept the Terms and Conditions with the Privacy Policy.
4. Enter further personal data and the residential address.
5. Select Create Account, then complete the email confirmation when requested.

Applicants need to be 18 or over and satisfy the gambling age of their jurisdiction. The Longfu88 login runs through the website's Login option, with the registered email and password and a possible security check. A forgotten password is handled on that same screen: the registered email is submitted, and an emailed reset link opens the way to a new one.

Verification can be demanded before any withdrawal, after the player edits profile or payment data, or around unusual and high-value transactions. Documents:

- A passport, national identity card or driving licence for identity
- A utility bill or bank statement for the address
- Evidence of who owns the payment method
- Source of funds, such as proof of income, if asked

Submission is open for up to 30 days, and a complete set is reviewed within 10 days. Payouts may wait until the checks end, while a failed check puts transactions or the account at risk of refusal or restriction.

## Deposits and Withdrawals
Every deposit method shares one floor of €10 and one ceiling of €5,000 per transaction, and the funds reach the balance within 1-2 minutes.

| Method type | Examples | Currencies |
|---|---|---|
| Cards | Visa, Mastercard | SGD, MYR, IDR, VND |
| E-wallets | Skrill, Neteller | EUR |
| Bank transfer | Bank Transfer | MYR, IDR, VND |
| Singapore options | DBS Bank, OCBC Bank, PayNow QR, PayNow | SGD |
| European methods | Sofort, Giropay | EUR |
| Cryptocurrencies | Bitcoin, Ethereum, Litecoin, USDT (ERC20, BEP20, TRC20), USDC | BTC, ETH, LTC, USDT, USDC |

The casino bills no fee of its own on deposits, but a payment provider or a blockchain network may add one, and country, currency and method all shape the limits. A deposit through Neteller or Skrill is left out of the welcome offer. At the cashier the player picks a method and currency, enters the amount and payment information, then authorises the payment as the provider instructs.

Longfu88 pays out through Visa, Mastercard, bank transfer, Online Banking, DBS Bank, Touch'n Go, DANA, MoMo and crypto: USDT over three networks, Litecoin, Bitcoin and Ethereum. Each request must fall between €20 and €5,000.

1. Enter the cashier from the signed-in account.
2. Choose Withdrawal, then a payout method.
3. Type the amount and the recipient's wallet address or bank details.
4. Check the request before confirming it.
5. Pass identity and payment method verification if prompted.
6. Allow the casino to process it, after which a bank or network settles the payout.

The Lngfu88 withdrawal time for wallet, crypto and card requests is 1 to 3 business days. A bank transfer takes up to 3 business days at the casino, and the receiving bank then needs 3-5 more. Three working days is the usual limit for handling a request.

The casino sets no regular payout charge, but providers or networks may bill separately. A 10% commission (minimum €2.25) can apply when turnover stays below the deposit, so at least 1x turnover of the deposit may come first. Some card or bank transfer funded transactions can carry 15%. KYC documents may also hold a payout back.

## Casino Welcome Bonus and Its Terms
The Casino Welcome Bonus targets newly registered players and sits apart from the sports offers. A first deposit of at least €50 unlocks it, unlike the casino-wide minimum of €10. Each account may claim a single welcome offer. The Longfu88 bonus is a 188% deposit match limited to €2,088, and 18 free spins are bundled with it.

Claiming follows four stages:

- Create the account.
- Fund it with the first deposit that meets the €50 threshold.
- Turn the bonus on under My Bonuses before placing a bet.
- Clear the wagering on eligible games before expiry.

No Longfu88 promo code enters the picture, since the bonus goes live in My Bonuses after the deposit is credited and none of the stages asks for a code. Two alternatives exist at Longfu88. The Casino Crypto Welcome Bonus gives 188% up to 2,888 USDT on 50 USDT, while the Live Casino Welcome Bonus gives 125% up to €888 on €30. The crypto version and the Casino Welcome Bonus exclude each other, as both rest on the first deposit.

These conditions govern how the bonus is cleared:

| Condition | Value |
|---|---|
| Validity | 10 days counted from activation |
| Wagering | Deposit plus bonus, multiplied by 25x |
| Maximum bet | Up to €22.5 for a spin |
| Maximum cashout | Capped at 5x the initial bonus amount |
| Wagering on Free Spins | 40x the Free Spins winnings |

Deposits via Neteller or Skrill do not take part. Two promotions cannot run together, and a cash-out request filed ahead of claiming, or mid-promotion, can cost the player eligibility. If the offer is cancelled, its funds go too, along with unconverted winnings.

## Reloads and Cashback
Seven offers follow common rules: one claim per period, activation in My Bonuses, no overlap with a live casino bonus, and bets of €5 or less per spin.

| Offer | Reward | Validity | Minimum deposit | Wagering |
|---|---|---|---|---|
| Casino Weekly Crypto Reload | 60% up to 1,000 USDT | 7 days | 20 USDT | 30x deposit plus bonus |
| Casino Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | 7 days | €20 | 40x Free Spins winnings |
| Casino Dragon Quest | €10 credit | 7 days | €20 | 30x promotional credit |
| Casino Weekend Reload | Up to €3,360 + 50 Free Spins | 7 days | €50 | 30x deposit plus bonus, 40x Free Spins winnings |
| Casino Double Fortune | 50% up to €500 | 24 hours | €30 | 30x deposit plus bonus |
| Casino Weekly Reload | 50 Free Spins | 7 days | €30 | 40x Free Spins winnings |
| Casino Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 7 days | 20 USDT | 30x deposit plus bonus, 40x Free Spins winnings |

Casino Weekly Cashback returns up to 10% of net casino losses weekly. Each window shuts Sunday 23:59 UTC after opening Monday 00:00. Opt-in covers four weeks, My Bonuses gets the payout every Monday, with 10x wagering. Rates follow VIP level:

| Level | Share |
|---|---|
| Bronze | 2%, cap €1,888 |
| Silver | 4%, cap €2,388 |
| Gold | 6%, cap €2,988 |
| Platinum | 8%, cap €3,988 |
| Diamond | 10%, cap €6,988 |

At Longfu88, Live Casino Cashback pays 25% up to €850. Daily rebates (1x wagering) give casino 0.9%, lottery 1.0%, live casino 1.0% and P2P 0.8%.

## VIP Programme
Play with real money feeds the Longfu88 VIP Program. Eligible stakes earn VIP points, and each threshold of points unlocks a reward level in numbered order, 25 in total. Five tiers hold these levels, with Bronze lowest, then Silver, Gold and Platinum, and Diamond highest.

The two ends show the scale. Entry level 1 asks for a single point and pays €9.8, plus 1% cashback, and the withdrawal ceiling stands at €9,800. Top level 25 asks for 5,500 points, and its numbers are €980, 10% and €147,000.

Climbing brings more than money. A personal VIP manager joins in at level 4, alongside personalised offers, cashback and raised withdrawal limits. Currency matters as much as level for these figures, and the rules may change.

## Casino Games and Slots
Longfu 88 Casino arranges its lobby into nine categories: slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery and a crash and instant section. Live dealer games and the remaining categories get their own section further down, so this one stays with the reels. At Longfu88 the slot shelf can be sampled through three titles with their figures.

Pragmatic Play supplies Sweet Bonanza, which shows an RTP of 96.48%, high volatility and a maximum multiplier of 21,175x. Hacksaw Gaming created Wanted Dead or a Wild: its RTP is 96.38%, its volatility very high, and its multiplier tops out at 12,500x. Gates of Olympus, again from Pragmatic Play, is credited with an RTP of 96.50% together with a 5,000x multiplier ceiling and high volatility.

For readers new to the terms, RTP shows what portion of the money staked flows back to players across thousands of spins. Volatility tells how those payouts are spread: higher values point to rarer but bigger hits. These three titles are samples and not a ranking of the lobby.

## Live Casino, Other Games and Providers
The live casino is the part of the lobby where dealers run each round on camera. Its studios include Evolution and SA Gaming, and the live floor also features Longfu88 Baccarat, an exclusive table that follows standard baccarat play. Apart from that table, the lobby names no further live game or show. Readers who prefer a dealer to an animated reel will look here first, and the studios behind it are the same ones listed among the providers below.

Past the live floor, the online casino extends to several other types of play. Crash and instant titles hinge on a single decision: leave the round before the multiplier stops climbing. A fishing game hands the player a cannon to point at moving targets. Table games keep to the card and wheel formats in which the player takes on the house. Lottery means choosing numbers ahead of a draw. P2P games pit players against each other and not against the casino, while fast games compress a round into a few seconds.

Behind all of this stands a roster of ten providers: Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft and Hacksaw Gaming. They supply the content for the casino's slots, live tables and table games, and the Longfu 88 lobby is built from their catalogues.

## Licence and Security
The online casino opened its doors in 2026 and runs accounts in USDT, USD, MYR, SGD, EUR and THB. Eligible players are 18 or older, permitted to gamble under the laws of their own country, limited to one personal account and barred from third-party payment methods. Anyone looking for the site should treat the Longfu 88 Official Site as the real address and skip copycat pages.

On licensing, casino Longfu88 gives the following: jurisdiction Costa Rica, registration number 000-039123-R-319326-001, company Lumina. That company is the operator named on the licence and also acts as the controller of personal data. Technical and organisational safeguards protect the data, payments and accounts of Longfu88 players. Information may reach payment service providers, identity verification providers and technology providers, and, if a legal duty applies, to regulators and law enforcement bodies.

Players keep a set of data rights: access, rectification, erasure where legally permitted, restriction, objection, portability where applicable and withdrawal of consent. Credentials stay the account holder's responsibility. The operator may pause account activity while verification takes place or abuse is suspected.

## Responsible Betting and Gambling
The casino admits adults of 18 and above, in places where local law permits gambling at all. Self-exclusion begins with an e-mail to support@longfu88.com. Once the request is processed, it takes effect within 24 hours, and account access and gambling stay restricted for the agreed period. Closing an account also goes through customer support. The procedure has four steps: send the request, confirm the preferred terms and the account details, leave the casino free to restrict or end access, and turn to independent support where suitable.

A short set of self-assessment questions helps a player notice potential gambling-related harm. Players can contact these organisations:

- GamCare
- Gamblers Anonymous
- Gambling Therapy

The information on this page is no substitute for professional support from such organisations.

## Support
Help reaches the player through two channels. Live chat stays open round the clock every day (24/7), so an urgent question about a deposit or a bet does not wait for office hours. A longer request is better suited to e-mail, sent to support@longfu88.com, where the details can be written out in full. Customer support works in Thai, Vietnamese, English, Simplified Chinese, Indonesian and Malay, which means a player can pick the language he or she is most comfortable with.

---

## BLOCK BRIEF
Block: b16, H2 "Pros and Cons" (under H1 "Longfu88 Sports and Casino Review for Singapore Players")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 53-67 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 67, but never beyond 73 words.
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
- Advantages → are offset by → the conditions attached to them [7]
Summary: Table of pros and cons drawing solely on facts already given on the page.
Copywriter Notes: Format: two columns only, Pros | Cons, in a Markdown table. Four or five rows are expected. Pros are facts taken from the page (24/7 live chat, a 25-level VIP programme, a weekly cashback that reaches 10%, a wide choice of payment methods that includes cryptocurrencies, and a small minimum deposit of €10 that applies in general); the cons reflect them as conditions (a first payout that verification may delay; withdrawals by bank that can take several working days; a 10% or 15% commission on withdrawals made under the turnover rule; and a welcome bonus that depends on a €50 deposit and on 25x wagering of deposit plus bonus together). The introduction is limited to one line, no new facts are introduced, and the table contains no tracked keyword. Use no tracked keyword in the body of this block.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_general.minimum_deposit: €10
- brandinfo_welcome.welcome_bonus.wagering_requirement: 25x the deposit plus bonus amount
- brandinfo_privacy_policy.terms_conditions.conditional_fees: ["A minimum of €2.25 applies to the 10% commission that may be charged when qualifying turnover does not reach the deposited amount.", "Transactions that a card or bank transfer funds may be subject to a 15% charge in certain cases, in line with the casino rules."]; keep exactly: 10, 2.25, 15, bank transfer
- brandinfo_games.providers: ["Yggdrasil", "SA Gaming", "NetEnt", "Skywind", "Red Tiger", "Pragmatic Play", "Betsoft", "Big Time Gaming", "Hacksaw Gaming", "Evolution"]
- brandinfo_promotions.other_bonuses[9].reward: Up to 10% of weekly net casino losses, capped at €6,988
