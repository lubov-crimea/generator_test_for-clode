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
Page intent: Page type: review of Longfu88 for adults in Singapore, framed as a first-timer's walkthrough. Stages in order: basic facts, licence check, account creation and verification, first deposit, welcome bonus with wagering terms, game choice, providers, promotions and the VIP programme once the welcome offer is used, mobile access, withdrawals, sports betting, responsible gambling, support, short Q&A, summary. Voice: stage by stage. Every section starts with what the player does and closes by pointing at the next stage. Sentences: roughly 16 words. Paragraphs: two or three sentences. Description order: how the feature is built first, then who it suits. Lists: numbered whenever step order matters. Calls to action: attach each one to a concrete step such as register, deposit or claim. Facts about the brand: the AffBulk knowledge base longfu88-new, nothing else. Legal standing: say nothing about how Singapore regards the casino.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino from Sign-Up to Withdrawal: a Singapore Guide (96-122 words): Opening overview: first the casino's character, then its game areas, its start year, and finally the note that the page addresses adults in Singapore.
b02   H2 Basics Before You Register (88-112 words): Fact table at a glance: operator and launch year first, then licence, languages and currencies, then money items (welcome bonus, cashback, minimum deposit and payment methods), then Minimum age and support.
b03   H2 Checking the Licence and Operator First (178-228 words): First stop before you register: when it launched, which currencies accounts use, who may play; after that the licence itself, the operator behind it, and safeguards for data and accounts.
b04   H2 Creating the Account: Registration and Login (123-157 words): Registration by e-mail as five numbered steps, then the data needed, the single-account rule, signing in and resetting a forgotten password.
b05     H3 Passing Identity Verification (96-122 words): Verification triggers, accepted document types, how long players have to submit them, how long the review lasts and what failed checks lead to.
b06   H2 Funding the Account: Deposit Methods (122-154 words): Deposit options grouped by type, the shared limits and crediting speed, the Singapore-specific choices and the six deposit steps.
b07   H2 Claiming the Welcome Bonus (133-171 words): Casino Welcome Bonus in detail: its percentage and cap, free spins, qualifying deposit and eligibility, the four steps to claim it, and two other first-deposit offers.
b08     H3 Meeting the Wagering Terms (102-130 words): Welcome Bonus conditions in table form, then the exclusions together with their practical consequences.
b09   H2 Choosing What to Play (83-106 words): Lobby breadth by category: jackpots, fishing and P2P, slots, live dealer and table games, plus lottery, then fast games, then crash and instant games.
b10     H3 Starting with Slots (90-113 words): Three example slots; for each: the studio, RTP, volatility and the top multiplier.
b11     H3 Moving to the Live Tables (90-113 words): Live dealer area: how far it reaches, the house baccarat title, and those studios in the provider list that show up for live play.
b12     H3 Trying Other Game Types (77-97 words): The remaining game categories collected here: fast games and lottery, fishing, P2P, crash and instant games and table games.
b13   H2 The Studios Supplying the Games (77-97 words): Game studios, taken as listed among the providers.
b14   H2 Promotions After the First Deposit (122-154 words): Reload offers and special campaigns compared in one table: what each one pays, minimum deposit, wagering requirement and validity period, plus the rules all of them share.
b15     H3 Cashback and Rebates (77-97 words): Weekly cashback and live casino cashback, the VIP-tier rates, and the daily rebates broken down per game category.
b16     H3 Earning Rewards and Coins (70-90 words): Game-style extras found under Rewards: the Coin Shop, Challenges, Bonus Crab, Collections and Wheel of Fortune.
b17   H2 Climbing the VIP Levels (102-130 words): Inside the VIP programme: real-money play earns points, the ladder has five tiers with 25 reward levels across them, and every step up unlocks perks.
b18   H2 Playing on the Go (96-122 words): Mobile access through Android, iOS and the mobile web: the responsive site, the shortcut kept on the home screen and the account functions that can be used.
b19   H2 Withdrawing Your Winnings (115-146 words): Payout mechanics: supported methods, the six-step procedure, timing, limits, and fees that are charged only in certain cases.
b20   H2 Betting on Sports as Well (102-130 words): Sportsbook snapshot: the sports and esports covered, plus bet types and live in-play betting.
b21     H3 Sports Bonuses (77-97 words): Sports promotions: weekend and weekly reloads, the first-deposit bonus, the Bet Builder with risk-free cover, parlay boost, early payout and cashback, along with the odds requirement common to them.
b22   H2 Keeping Play Under Control (96-122 words): Age limit, self-exclusion, closing an account on an e-mailed request, a set of self-assessment questions and places to get help.
b23   H2 Getting Help (70-90 words): Contact routes for support, its opening hours and the languages it answers in.
b24   H2 Common Questions Along the Way (158-202 words): Brief answers covering eligibility, minimum deposit, bonus claiming, how long verification takes and password recovery.
b25   H2 Summary for New Players (90-113 words): Closing verdict: the type of player it suits, items to check ahead of a deposit and a responsible-gambling note.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino from Sign-Up to Withdrawal: a Singapore Guide
Longfu88 is a 2026 arrival among online casinos, where most entertainment sits behind a single account. The lobby holds slots, live dealer games and table games, followed by jackpots, fishing, P2P and fast games, while crash and instant games and a lottery round out the range. A sportsbook sits next to the casino side, so betting on events belongs to the same offer. Singapore adults are the readers this guide has in mind, and players must be at least 18.

The sections ahead are arranged in a deliberate order: responsible gambling and mobile play first, then payments, the games and the bonuses, and finally the licence together with the key facts.

## Basics Before You Register
| Fact | Detail |
|---|---|
| Operator | Lumina, the company that acts as data controller |
| Launched | Opened in 2026 |
| Licence | Registration number 000-039123-R-319326-001, operator Lumina, jurisdiction Costa Rica |
| Support languages | Simplified Chinese, Thai, Malay, English, Indonesian, Vietnamese |
| Currencies | USDT, SGD, USD, THB, EUR, MYR |
| Payment methods | PayNow, USDT, Bitcoin, Bank Transfer, Visa, Mastercard and more |
| Minimum deposit | €10 across the casino |
| Welcome bonus | 188% deposit match, ceiling €2,088, with 18 free spins |
| Cashback | 10% back on weekly net casino losses |
| Minimum age | 18 years |
| Support | Live chat around the clock, plus mail to support@longfu88.com |

## Checking the Licence and Operator First
A newcomer should first confirm what the site is and who stands behind it. Longfu88 entered the market with a 2026 launch, and balances are kept in one of six currencies: USDT, SGD, USD, THB, EUR or MYR. Picking the page called Longfu 88 Official Site rather than a lookalike is a sensible habit before any details are typed in.

Eligibility rests on four conditions. Anyone younger than 18 is excluded, and gambling has to be lawful where the person lives, so the local rules matter first. Payments must come from methods the player owns, and each person may keep one personal account with accurate registration details.

Next comes the licence. The casino Longfu88 is listed under registration number 000-039123-R-319326-001 in the jurisdiction of Costa Rica, and the holder is the operator Lumina. That company also serves as data controller. Personal information may be passed to identity verification providers, payment service providers and technology providers, and to regulators or law enforcement when the law requires it. Technical and organisational safeguards protect accounts, payments and personal data. Players keep rights of access, rectification, restriction, objection, withdrawal of consent, erasure where legally permitted and portability where applicable. Whoever holds an account must keep its credentials safe. With these basics settled, the next stage is opening the account.

## Creating the Account: Registration and Login
Registration is done by e-mail and asks for a legal name, e-mail address, password, date of birth and residential address, collected over five steps.

1. Start on the website and press Register.
2. Give a mailbox address and select a password.
3. Accept the Terms and Conditions along with the Privacy Policy, and confirm being 18 or older.
4. Enter the home address and the remaining personal fields.
5. Press Create Account and, if a confirmation message reaches the inbox, follow it.

Each player is entitled to just one personal account. Returning to Longfu88 later means tapping Login, typing the e-mail used at sign-up together with the password, and passing whichever security check appears. Should the password be lost, the Forgot Password option sends the registered address a reset link, and a fresh password is set through it. Once the account exists, the identity check comes next.

### Passing Identity Verification
Verification may be requested before withdrawal, and it can also follow unusual or high-value transactions or a change to account or payment details. Documents may be submitted within 30 days of a request. The accepted set looks like this:

- Identity: passport, national identity card or driving licence
- Address: utility bill or bank statement
- Payment method: bank or card ownership evidence, or digital wallet ownership evidence
- Source of funds, when asked: bank statements, proof of income or similar financial records

Once a complete set is received, the review takes up to 10 days. Until it ends, a payout may be held back. A failed check may end in refused transactions or restrictions on the account, so current, readable files that match the profile save time. The deposit stage follows.

## Funding the Account: Deposit Methods
Longfu88 sorts its deposit options by type, and the table below shows which currencies each group handles.

| Method type | Examples | Currencies |
|---|---|---|
| Local banks and wallets | OCBC Bank, DBS Bank, PayNow, PayNow QR | SGD |
| Cards | Mastercard, Visa | SGD, IDR, MYR, VND |
| Bank transfer | Bank Transfer | IDR, MYR, VND |
| European methods | Giropay, Sofort | EUR |
| E-wallets | Skrill, Neteller | EUR |
| Cryptocurrencies | USDC, Litecoin, Ethereum, Bitcoin, USDT (BEP20, ERC20, TRC20) | USDC, LTC, ETH, BTC, USDT |

Funds arrive within 1-2 minutes on every route, and one transaction runs from €10 to €5,000, though limits shift with country, currency and payment method. The casino charges nothing for handling deposits, but the provider or the blockchain network can levy a charge. Neteller and Skrill are excluded from the welcome bonus. The sequence is: log in, open the cashier and choose Deposit, pick a method with its network or currency, enter payment information and the amount, confirm with the provider, then wait for the balance to update.

## Claiming the Welcome Bonus
At Longfu88, the Casino Welcome Bonus waits for every newly registered player. The Longfu88 bonus pairs a match of 188% with a ceiling of €2,088 and 18 free spins, which are spins on a slot whose stake the casino covers. Qualification starts with a first deposit of €50, a threshold that belongs to this bonus only, since the casino-wide minimum is €10. A second welcome offer on one account is not possible.

Claiming takes four steps:

- Sign up and finish the personal details section of the form.
- Deposit at least €50 as the qualifying first payment.
- Open My Bonuses and activate the Casino Welcome Bonus before any wager.
- Use eligible casino games to complete the wagering ahead of expiry.

No Longfu88 promo code figures in the process: activation happens under My Bonuses once the deposit has gone through, and the published procedure contains no step involving a promo code. The first deposit can trigger the Casino Welcome Bonus or else the Crypto Welcome Bonus (188%, cap of 2,888 USDT, from 50 USDT), while the Live Casino Welcome Bonus needs €30 for 125% up to €888.

### Meeting the Wagering Terms
Each condition of the Casino Welcome Bonus is worth reading before the first deposit is made:

- **Maximum bet:** €22.5 per spin
- **Wagering:** 25x, covering the deposit and the bonus sum together
- **Validity:** 10 days after activation
- **Free spins wagering:** 40x on whatever those spins win
- **Maximum cashout:** 5x the initial bonus amount

Players funding the account through Neteller or Skrill cannot take part, and a second promotion cannot run next to this one. Asking for a payout ahead of claiming, or mid-bonus, can cost the player eligibility. Cancelling the promotion means losing the bonus money and any unconverted winnings, and verification may hold bonus winnings back before payment.

## Choosing What to Play
Picking a first game begins with the lobby of Longfu88 Casino, which holds nine categories: slots, jackpots, live dealer games, table games, fishing, P2P games, crash and instant games, fast games and lottery. Each one is a separate corner of the same lobby, so a session can move from a spin on the reels to a hand at the table without leaving the site. On Longfu88, slots come first below, with three example titles, then the live tables, and finally the remaining categories grouped together.

### Starting with Slots
Slots are the natural first stop, and three titles show how the numbers differ. Gates of Olympus from Pragmatic Play carries high volatility, 96.50% RTP and a 5,000x top multiplier. Sweet Bonanza, also from Pragmatic Play, shares the high volatility and sits at 96.48% RTP, but its top multiplier reaches 21,175x. Wanted Dead or a Wild, developed by Hacksaw Gaming, tops out at 12,500x, with 96.38% RTP and a very high volatility rating. For a player, RTP signals how much of the money staked comes back across many spins, and volatility signals how bumpy that return is. These three are examples, not a ranking.

### Moving to the Live Tables
Live dealer games form one category in the lobby of Longfu 88 Casino, and it suits players who prefer a real dealer and a table to reels. The house title is Longfu88 Baccarat, an exclusive live or table game built on baccarat gameplay. Evolution and SA Gaming both appear among the studios in the provider list, and both are known as live dealer studios, so the live area draws on names like these. Which live games each of them supplies is not specified, and other live titles and shows stay unnamed here. Once the tables are covered, the remaining categories are next.

### Trying Other Game Types
Beyond slots and live tables, six further categories round out the lobby:

- **Lottery:** the player picks numbers and waits for a draw.
- **P2P games:** the opponent is another participant at the table, not the house.
- **Table games:** digital versions of card and wheel classics, with the player deciding each bet.
- **Crash and instant games:** a round ends at an unpredictable moment, and the player chooses when to cash out.
- **Fishing:** an arcade-style game where the player aims at moving targets on screen.
- **Fast games:** short rounds that resolve within moments.

The studios behind the lobby come next.

## The Studios Supplying the Games
Behind the lobby of Longfu 88 stand ten studios, and between them they supply the slots, the live games and the table games that fill it. Big Time Gaming, NetEnt, Evolution, Hacksaw Gaming and Betsoft head the provider list, followed by Pragmatic Play, Red Tiger, Yggdrasil, SA Gaming and Skywind. Players who already have a favourite developer can use this list to check whether it appears before choosing a game. The next stage looks at what the account can earn after the first deposit.

---

## SECTION
Write the blocks b14, b15, b16 in ONE answer, in this order. They are one continuous section of the page: the sub-sections continue the parent, so the text must flow from block to block without repeating itself. Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts.

---

## BLOCK BRIEF
Block: b14, H2 "Promotions After the First Deposit" (under H1 "Longfu88 Casino from Sign-Up to Withdrawal: a Singapore Guide")
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): b15 H3 "Cashback and Rebates"; b16 H3 "Earning Rewards and Coins"
Word Count: 122-154 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 154, but never beyond 169 words.
Format: paragraph + table. Visual Elements: Table — 3 of 5 tables on the page
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
- Weekly Reload [9]
- Weekend Reload [8]
- Crypto Reload [7]
- One-Day Reload Special [5]
- Seasonal Promotion [5]
- Free Spins [5]
Entity Connections to state explicitly [priority]:
- Weekly Reload → awards → 50 Free Spins [7]
- Promotions → may not run alongside → another casino bonus currently running [8]
Summary: Reload offers and special campaigns compared in one table: what each one pays, minimum deposit, wagering requirement and validity period, plus the rules all of them share.
Copywriter Notes: Opening: one lead-in sentence. Table: Markdown, five columns in this order: Offer, Reward, Min. deposit, Wagering, Validity. Rows: the seven offers as given, namely Casino Weekly Reload, Casino Weekly Crypto Reload, Casino Weekend Reload, Casino Weekend Crypto Reload, Casino Double Fortune (one-day reload special), Casino Trick or Treat Pumpkin Bonanza and Casino Dragon Quest (verification reward). Shared rules: mention them once, after the table. Rules: an offer is switched on inside My Bonuses, a promotional period permits one claim only, an active casino bonus rules out a second one, and during the wagering of bonus funds no stake may exceed €5 per spin. Use "Longfu88" exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_promotions.other_bonuses[2]: {"name": "Casino Weekly Reload", "type": "Weekly free spins", "reward": "50 Free Spins", "minimum_deposit": "€30", "wagering_requirement": "40x winnings from Free Spins", "validity": "7 days", "claiming_method": "In My Bonuses, activation of the offer follows after its deposit and eligibility conditions have been satisfied.", "eligibility": "Registered players qualify provided they fulfil the rules for qualification that are specific to the offer.", "important_terms": ["A promotional period permits one claim, except where stated differently.", "Another active casino bonus rules out combining it with this one.", "No stake above €5 per spin is allowed when wagering bonus funds."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[3]: {"name": "Casino Weekly Crypto Reload", "type": "Crypto weekly reload", "reward": "60% up to 1,000 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus", "validity": "7 days", "claiming_method": "In My Bonuses, activation of the offer follows after its deposit and eligibility conditions have been satisfied.", "eligibility": "Registered players qualify provided they fulfil the rules for qualification that are specific to the offer.", "important_terms": ["No stake above €5 per spin is allowed when wagering bonus funds.", "Another active casino bonus rules out combining it with this one.", "A promotional period permits one claim, except where stated differently."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[4]: {"name": "Casino Weekend Reload", "type": "Weekend deposit bonus", "reward": "Up to €3,360 + 50 Free Spins", "minimum_deposit": "€50", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "In My Bonuses, activation of the offer follows after its deposit and eligibility conditions have been satisfied.", "eligibility": "Registered players qualify provided they fulfil the rules for qualification that are specific to the offer.", "important_terms": ["Another active casino bonus rules out combining it with this one.", "No stake above €5 per spin is allowed when wagering bonus funds.", "A promotional period permits one claim, except where stated differently."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[5]: {"name": "Casino Weekend Crypto Reload", "type": "Weekend crypto bonus", "reward": "75% up to 750 USDT + 100 Free Spins", "minimum_deposit": "20 USDT", "wagering_requirement": "30x deposit plus bonus; 40x Free Spins winnings", "validity": "7 days", "claiming_method": "In My Bonuses, activation of the offer follows after its deposit and eligibility conditions have been satisfied.", "eligibility": "Registered players qualify provided they fulfil the rules for qualification that are specific to the offer.", "important_terms": ["No stake above €5 per spin is allowed when wagering bonus funds.", "A promotional period permits one claim, except where stated differently.", "Another active casino bonus rules out combining it with this one."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[6]: {"name": "Casino Double Fortune: One-Day Reload Special", "type": "One-day reload", "reward": "50% up to €500", "minimum_deposit": "€30", "wagering_requirement": "30x deposit plus bonus", "validity": "24 hours", "claiming_method": "In My Bonuses, activation of the offer follows after its deposit and eligibility conditions have been satisfied.", "eligibility": "Registered players qualify provided they fulfil the rules for qualification that are specific to the offer.", "important_terms": ["A promotional period permits one claim, except where stated differently.", "No stake above €5 per spin is allowed when wagering bonus funds.", "Another active casino bonus rules out combining it with this one."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[7]: {"name": "Casino Trick or Treat Pumpkin Bonanza", "type": "Seasonal casino promotion", "reward": "Up to 100 Free Spins", "minimum_deposit": "€20", "wagering_requirement": "40x Free Spins winnings", "validity": "7 days", "claiming_method": "In My Bonuses, activation of the offer follows after its deposit and eligibility conditions have been satisfied.", "eligibility": "Registered players qualify provided they fulfil the rules for qualification that are specific to the offer.", "important_terms": ["Another active casino bonus rules out combining it with this one.", "A promotional period permits one claim, except where stated differently.", "No stake above €5 per spin is allowed when wagering bonus funds."]}; keep exactly: 5, my bonuses
- brandinfo_promotions.other_bonuses[8]: {"name": "Get Verified and Get Extra is the casino's Dragon Quest promotion", "type": "Verification reward", "reward": "€10 bonus credit", "minimum_deposit": "€20", "wagering_requirement": "30x promotional credit", "validity": "7 days", "claiming_method": "In My Bonuses, activation of the offer follows after its deposit and eligibility conditions have been satisfied.", "eligibility": "Eligible are players completing requested account verification within the campaign.", "important_terms": ["A promotional period permits one claim, except where stated differently.", "Another active casino bonus rules out combining it with this one.", "No stake above €5 per spin is allowed when wagering bonus funds."]}; keep exactly: 5, dragon quest, get verified and get extra, my bonuses

---

## BLOCK BRIEF
Block: b15, H3 "Cashback and Rebates" (under H2 "Promotions After the First Deposit")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 77-97 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 97, but never beyond 106 words.
Format: paragraph + table. Visual Elements: Table — 4 of 5 tables on the page
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
- Weekly Cashback → hands back → up to 10% of the week's net casino losses [9]
- Rebates → reach players → every single day [7]
Summary: Weekly cashback and live casino cashback, the VIP-tier rates, and the daily rebates broken down per game category.
Copywriter Notes: Item one: Casino Weekly Cashback. Terms: weekly net casino losses as the base, rate up to 10%, cap €6,988. Period: from Monday 00:00 UTC through Sunday 23:59 UTC. Enrolment: opt-in covers one four-week cycle. Payout: the Monday credit lands in My Bonuses, with 10x wagering of the cashback. Rate by VIP tier: from Bronze at 2% through Silver 4%, Gold 6% and Platinum 8% up to Diamond at 10%. Lay the tiers out as a short table with the columns tier, percentage and maximum. Item two: Live Casino Cashback, 25% up to €850. Item three: one sentence covering four daily rebates, namely P2P 0.8%, casino 0.9%, lottery 1.0% and live casino 1.0%, each carrying 1x wagering. Counting rule: real-money bets only, bonus funds do not count. Keep apart: tier percentages in this block are weekly-cashback rates and differ from the rates that belong to VIP levels in the VIP section, so never swap them. Use no tracked keyword in the body of this block.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_promotions.other_bonuses[9]: {"name": "Casino Weekly Cashback", "type": "Casino cashback", "reward": "Up to 10% of weekly net casino losses, capped at €6,988", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "minimum_cashback": "€4.5", "opt_in": "Automatic renewal is possible for active accounts, following an opt-in for one four-week cycle.", "crediting": "Activation is a prerequisite for the credit placed in My Bonuses on Monday.", "wagering_requirement": "10x cashback before withdrawal", "cashback_by_vip": [{"level": "VIP Bronze", "percentage": 2, "maximum": "€1,888"}, {"level": "VIP Silver", "percentage": 4, "maximum": "€2,388"}, {"level": "VIP Gold", "percentage": 6, "maximum": "€2,988"}, {"level": "VIP Platinum", "percentage": 8, "maximum": "€3,988"}, {"level": "VIP Diamond", "percentage": 10, "maximum": "€6,988"}], "important_terms": ["Counting is limited to real-money casino wagers and wins, with bonus funds excluded.", "Within the claim window, the weekly cashback has to be activated, otherwise it expires."]}; keep exactly: my bonuses, monday
- brandinfo_promotions.other_bonuses[10]: {"name": "Live Casino Cashback", "type": "Live casino cashback", "reward": "25% up to €850", "minimum_cashback": "€4.5", "calculation_period": "Monday 00:00 UTC through Sunday 23:59 UTC", "crediting": "Every Monday the amount is added to My Bonuses, with opt-in and activation required.", "wagering_requirement": "10x credited cashback", "important_terms": ["Winnings get deducted from stakes paid in real money within eligible Live Casino games to form the base.", "When cashback is calculated, bonus balances are not taken into account."]}; keep exactly: my bonuses, monday, live casino
- brandinfo_promotions.other_bonuses[11]: {"name": "Unlimited Casino Rebate", "type": "Rebate", "rebate_percentage": 0.9, "calculation": "Qualification comes from settled wagering in real money within the relevant game category.", "crediting": "Daily crediting puts the rebate into the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Qualifying settled wagers are needed from a registered player."}
- brandinfo_promotions.other_bonuses[12]: {"name": "Unlimited Live Casino Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Qualification comes from settled wagering in real money within the relevant game category.", "crediting": "Daily crediting puts the rebate into the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Qualifying settled wagers are needed from a registered player."}
- brandinfo_promotions.other_bonuses[13]: {"name": "Unlimited P2P Rebate", "type": "Rebate", "rebate_percentage": 0.8, "calculation": "Qualification comes from settled wagering in real money within the relevant game category.", "crediting": "Daily crediting puts the rebate into the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Qualifying settled wagers are needed from a registered player."}
- brandinfo_promotions.other_bonuses[14]: {"name": "Unlimited Lottery Rebate", "type": "Rebate", "rebate_percentage": 1.0, "calculation": "Qualification comes from settled wagering in real money within the relevant game category.", "crediting": "Daily crediting puts the rebate into the rewards balance.", "wagering_requirement": "1x credited rebate", "eligibility": "Qualifying settled wagers are needed from a registered player."}

---

## BLOCK BRIEF
Block: b16, H3 "Earning Rewards and Coins" (under H2 "Promotions After the First Deposit")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 70-90 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 90, but never beyond 99 words.
Format: list. Visual Elements: Bulleted/numbered list — 6 of 11 lists on the page
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
- Coins → get traded at → the Coin Shop in return for rewards [7]
- Challenges → pay out → bonus credits, free spins and coins [6]
Summary: Game-style extras found under Rewards: the Coin Shop, Challenges, Bonus Crab, Collections and Wheel of Fortune.
Copywriter Notes: List: five features, a bullet apiece, with the name bolded and a single short sentence after it. Bonus Crab: valid for 7 days; claiming it lets the player pick a crab that opens a reward; bonus credit carries 30x wagering and free spin winnings 40x. Wheel of Fortune: either an eligible spin or spent Coins triggers it; 7 days, 30x. Challenges and Collections: each is found under Rewards. Coin Shop: bonus credits up to €4,500 and rewards can be bought with Coins, item prices differ, and separate wagering may apply. Reminder: rewards can come with their own wagering requirements. Use no tracked keyword in the body of this block.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_promotions.gamification_features: [{"name": "Bonus Crab", "mechanics": "Claiming qualifying picks makes it possible to unseal a crab reward and uncover a casino prize.", "access": "In the rewards area, qualifying activity can result in free picks.", "rewards": ["Free Spins", "Bonus credits", "Coins"], "validity": "7 days after reward assignment", "wagering_requirement": "30x awarded bonus credit; 40x winnings from Free Spins"}, {"name": "Challenges", "mechanics": "Rewards that appear in the list unlock when qualifying gambling tasks are finished.", "access": "Rewards > Challenges", "rewards": ["Free Spins", "Bonus credits", "Coins"], "validity": "As shown for each challenge"}, {"name": "Collections", "mechanics": "Qualifying activity yields campaign items to collect, and each completed set can be redeemed.", "access": "Rewards > Collections", "rewards": ["Coins", "Bonus rewards"], "validity": "Campaign-specific"}, {"name": "Wheel of Fortune", "mechanics": "An eligible spin or Coins can be spent to turn a prize wheel.", "access": "Rewards area", "rewards": ["Bonus credits", "Free Spins", "Coins"], "validity": "7 days", "wagering_requirement": "30x bonus awards"}, {"name": "Coin Shop", "mechanics": "In the Shop, rewards are obtained by exchanging earned Coins.", "access": "Rewards > Shop", "rewards": ["Reward items and bonus credits up to €4,500"], "important_terms": ["Depending on the item, the coin price and prize availability change.", "Some rewards may have their own, separate wagering requirements."]}]; keep exactly: rewards area, coins
