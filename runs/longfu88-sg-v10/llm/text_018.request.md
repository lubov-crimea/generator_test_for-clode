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
Page intent: Treat this as a reference page for Singapore readers who want the casino's claims weighed, not recited. The scope runs from the Longfu88 offer and the fact table through licence and data protection, account opening and identity checks, the welcome bonus and a table of its conditions, reloads, cashback, rewards and the VIP programme, then game categories and providers, the sportsbook with its bonus table, deposits, withdrawals, mobile access, responsible gambling, support, pros and cons, six FAQ answers and a closing verdict. Keep the register formal and thorough, never breezy: sentences near 21 words, paragraphs built from three to four sentences, a table wherever an item carries two or more attributes, and offers set side by side rather than praised in isolation. Each table gets one sentence before it and one after it saying what the reader should take from it. Permit exactly one call to action and put it beside the welcome bonus. longfu88-new, the AffBulk knowledge base, supplies every brand fact on the page, and whether Singapore law treats the casino as lawful is left unaddressed.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Complete Guide for Singapore Players (109-138 words): Opening lines that characterise the casino through the game areas it offers, state the year it launched and signal that the readers addressed are grown-ups living in Singapore.
b02   H2 What the Casino Offers (90-113 words): A snapshot of the casino for a Singapore player: the year it launched, the account currencies, the official site and who is allowed to play.
b03   H2 Casino Information (109-139 words): A quick-reference sheet: operator and launch year, then the licence, languages and currencies, payment methods, the minimum deposit, the welcome bonus and cashback, Minimum age, then Sports and Game providers, the VIP tiers and finally support.
b04   H2 Licensing, Operator and Data Protection (154-194 words): The licensing jurisdiction, the operating company with its registration number, then the protections applied to account and personal data.
b05   H2 Registration and Login Guide (123-157 words): Signing up with an e-mail address: five numbered steps, the data the form collects, the rule of one account per player, then logging in and recovering a password.
b06     H3 Verification (KYC) (109-138 words): When ID checks are triggered, the documents the casino takes, the cut-off for uploading, the time the review needs and the consequences of a failed check.
b07   H2 Casino Welcome Bonus (146-187 words): What the Casino Welcome Bonus gives (percentage, cap, free spins), the deposit that unlocks it, the players who may claim it, four claiming steps and two rival first-deposit offers.
b08     H3 Terms of the Welcome Bonus (109-138 words): A table of conditions for the Casino Welcome Bonus, and below it the exclusions with a note on how they affect an actual player.
b09   H2 Reload Bonuses and Seasonal Promotions (128-162 words): A comparison table of the recurring reloads and seasonal campaigns that sets out, per row, what each pays, the deposit needed, the playthrough and the time limit, followed by the rules common to all of them.
b10     H3 Cashback and Rebate Programme (83-106 words): Weekly and live casino cashback, with rates set by VIP tier, followed by the day-by-day rebates for each game category.
b11     H3 Rewards Hub (77-97 words): Five light-hearted extras in the rewards area: Bonus Crab, plus the Coin Shop, Collections, Challenges and a Wheel of Fortune.
b12   H2 VIP Programme: Levels, Points and Limits (115-146 words): How points from real-money play carry a player through 25 reward levels and five tiers, and what actually improves along the way.
b13   H2 Game Library by Category (90-113 words): The breadth of the lobby, given as nine categories: lottery and fast games, P2P and fishing, jackpots, table games, live dealer, slots, plus crash and instant titles.
b14     H3 Slot Games (102-130 words): Three example slots, each profiled with its studio, RTP, volatility rating and highest multiplier.
b15     H3 Live Casino Games (96-122 words): Live dealer play: its general character, the house baccarat game and the studios from the provider list that operate live tables.
b16     H3 Other Game Types (83-106 words): A single wrap-up of the remaining game types: table games and fishing, P2P, fast games and lottery, with crash and instant titles.
b17   H2 Software Providers (53-67 words): The game studios behind the lobby, taken from the provider list.
b18   H2 Payment Methods and Deposit Limits (141-178 words): Deposit methods sorted by category, the limits and processing speed they have in common, local options for Singapore and a six-step walk through making a deposit.
b19     H3 Withdrawal Methods and Times (128-162 words): Cashing out step by step: the methods on offer, the six-step route, how fast requests are handled, the limits, and the charges that apply only in certain conditions.
b20   H2 Sportsbook (109-138 words): Coverage of the sportsbook: which sports and esports it lists, the kinds of bet and in-play wagering.
b21     H3 Sports Bonus Table (83-106 words): Sportsbook offers set side by side: weekly and weekend reloads, the first deposit bonus, and the extras (Bet Builder Risk Free, Parlay Boost, early payout and cashback), all governed by one odds rule.
b22   H2 Mobile Access and Installation (106-134 words): Casino access from a mobile device: Android, iOS and the mobile browser, the way the site adapts, the saved home-screen shortcut and the account tools that keep working.
b23   H2 Customer Support Channels (77-97 words): Contacting customer support: the available channels, the hours it is staffed, and the languages used.
b24   H2 Responsible Gambling Policy (109-138 words): Age limit first; after it self-exclusion and account closure, both arranged through an e-mail to support, then self-assessment and sources of outside help.
b25   H2 Pros and Cons Overview (53-67 words): Pros and cons in a two-column table, compiled strictly from facts the page has stated elsewhere.
b26   H2 Frequently Asked Questions (229-293 words): Brief replies about password recovery, VIP levels, weekly cashback, how long a withdrawal takes, wagering and claiming the bonus.
b27   H2 Verdict (102-130 words): A closing verdict covering who the offer suits, what merits a check before depositing, and a brief nod to responsible gambling.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Complete Guide for Singapore Players
Longfu88 is an online casino that went live in 2026 and gathers a sportsbook, slots, live dealer and table games, jackpots, fishing, P2P and fast games, lottery, and crash and instant titles on a single site. Such a mix matters because a player can move between a spin session, a live table and a match bet without opening a second account.

The guide is written for adult readers in Singapore, and the age requirement is 18 or above. Further down, it covers play from a handset, the cashier options, the size of the game choice, current promotions, the licence behind the operation, a quick fact sheet and the tools for safer gambling. Each part is kept factual, so the reader can weigh the casino without hype.

## What the Casino Offers
=== b02 ===
Longfu88 opened its doors to players in 2026, and accounts can be held in six currencies: USD, EUR, USDT, THB, MYR and SGD. Singapore dollars are therefore available for local readers who prefer not to convert funds at every deposit.

The safest way in is the address named Longfu 88 Official Site, and readers are better off avoiding look-alike pages that copy its design. Eligibility is spelled out in a few short rules. A player must be 18 or older, must live where gambling is lawful, may keep one personal account only, and has to register with accurate details. Funding the balance from payment methods that belong to another person is not allowed.

## Casino Information
=== b03 ===
| Area | Facts |
|---|---|
| Operator | Lumina |
| Launched | 2026 |
| Licence | Number 000-039123-R-319326-001, issued to Lumina, Costa Rica |
| Support languages | English, Thai, Indonesian, Vietnamese, Simplified Chinese, Malay |
| Currencies | USD, EUR, USDT, THB, MYR, SGD |
| Payment methods | PayNow, Visa, USDT, Mastercard, Bitcoin, Bank Transfer |
| Welcome bonus | Up to €2,088 (188%) with 18 free spins |
| Cashback | Up to 10% of weekly net casino losses, capped at €6,988 |
| Minimum deposit | €10 |
| Minimum age | 18 |
| Game providers | Betsoft, NetEnt, Red Tiger, Big Time Gaming, SA Gaming, Yggdrasil, Evolution, Hacksaw Gaming, Pragmatic Play, Skywind |
| Sports | Cricket, Esports, Volleyball, Table tennis, Virtual football, Badminton, Basketball, Football, Tennis |
| VIP tiers | Bronze, Silver, Gold, Platinum, Diamond |
| Support | support@longfu88.com and 24/7 live chat |

## Licensing, Operator and Data Protection
=== b04 ===
The licence comes first. Registration number 000-039123-R-319326-001 was issued in Costa Rica to the operator Lumina, and that is the only licensing claim made for casino Longfu88 on this page. Nothing here suggests that any Singapore body has authorised, approved or supervised the operation. The same company acts as data controller, and questions about personal data go to a data protection officer at dpo@longfu88.com.

Safeguards cover three areas: account access, payment flows and personal details, all of which the operator protects through technical and organisational measures. Information may be passed to regulators and law enforcement when they require it, and also to payment service providers, identity verification providers and technology providers.

Players hold a set of rights over their data: access, rectification, restriction, objection, withdrawal of consent, portability where applicable and erasure where the law permits it. Security is shared in practice. The registered holder of an account carries responsibility for guarding passwords and other sign-in details, since the operator may suspend an account because of verification needs or suspected abuse.

## Registration and Login Guide
Opening an account at Longfu88 follows five steps and relies on e-mail registration.

1. Choose the Register option on the site.
2. Enter an e-mail address and set a password.
3. Confirm the age and agree to both the Terms and Conditions and the Privacy Policy.
4. Add the residential address and the remaining personal details.
5. Select Create Account, then finish any e-mail confirmation that is requested.

The form asks for the legal name, date of birth, residential address, e-mail and password, and each player may hold just one personal account. Each later Longfu88 login starts with the Login button: the player types in the registered e-mail and password and passes any security check that appears. A player who forgets the password selects Forgot Password on the sign-in page, which sends a reset link to the registered e-mail, and a new password is then set by following the message.

### Verification (KYC)
Identity checks are tied to particular moments. Verification can be requested before a withdrawal is released, when a transaction looks unusual or large, and after changes to account or payment details.

The casino accepts these documents:

- Photo ID: a driving licence, national identity card or passport.
- Address evidence: a utility bill or a bank statement.
- Ownership evidence for the payment method in use.
- Evidence of the source of funds, when asked for.

The upload window lasts 30 days from the request, and the casino decides within up to 10 days once everything has arrived. A failed check has consequences: transactions may be refused, the account restricted, and withdrawals held back until the player meets the compliance requirements.

## Casino Welcome Bonus
Newcomers at Longfu88 are offered the Casino Welcome Bonus, a first deposit casino offer. The Longfu88 bonus returns up to €2,088 at 188%, with 18 Free Spins added to the package. It suits freshly registered players whose first deposit qualifies, and a second welcome offer cannot be stacked on the same account. Two amounts must be kept apart: this offer opens with a €50 deposit as the minimum, whereas €10 is the minimum deposit for the casino in general.

No code is involved. A Longfu88 promo code is neither needed nor requested, because the route runs through activation in My Bonuses once the deposit has been made. Four items make up the path:

- Complete the registration and the personal details.
- Fund the account with a first deposit that qualifies.
- Switch the offer on under My Bonuses, ahead of the first bet.
- Play eligible casino games to finish the playthrough before expiry.

Two rival first-deposit offers sit beside it: the Casino Crypto Welcome Bonus pays 188% up to 2,888 USDT from 50 USDT, and the Live Casino Welcome Bonus pays 125% up to €888 from €30. Register and claim the Casino Welcome Bonus to start with the main package.

### Terms of the Welcome Bonus
The table below lists the conditions attached to the Casino Welcome Bonus, so that the headline figures can be read together with their limits.

| Condition | Value |
|---|---|
| Maximum bet | €22.5 per spin |
| Validity | 10 days from activation |
| Maximum cashout | 5x the initial bonus amount |
| Wagering | 25x the deposit plus bonus amount |
| Free spins wagering | 40x Free Spins winnings |

Some exclusions trip up careless players. Neteller and Skrill deposits are not eligible, and bonuses run one after another, never in parallel. A cash-out request lodged ahead of claiming, or while the bonus is live, may cost the player the offer. Cancelling hands back the bonus money and every unconverted win, while payout of bonus winnings can wait for verification. A player should therefore finish the playthrough inside the ten days.

## Reload Bonuses and Seasonal Promotions
Longfu88 runs seven recurring or seasonal offers, compared below.

| Promotion | Reward | Minimum deposit | Playthrough | Validity |
|---|---|---|---|---|
| Casino Weekly Reload | 50 Free Spins | €30 | 40x Free Spins winnings | 7 days |
| Casino Weekly Crypto Reload | 60% up to 1,000 USDT | 20 USDT | 30x deposit plus bonus | 7 days |
| Casino Weekend Reload | Up to €3,360 + 50 Free Spins | €50 | 30x deposit plus bonus, 40x spin winnings | 7 days |
| Casino Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 20 USDT | 30x deposit plus bonus, 40x spin winnings | 7 days |
| Casino Dragon Quest | €10 bonus credit | €20 | 30x promotional credit | 7 days |
| Casino Double Fortune: One-Day Reload Special | 50% up to €500 | €30 | 30x deposit plus bonus | 24 hours |
| Casino Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | €20 | 40x Free Spins winnings | 7 days |

All seven need activation in My Bonuses, allow one claim per promotional period, exclude any other live casino bonus and limit spin stakes to €5 while bonus money is in play.

### Cashback and Rebate Programme
Casino Weekly Cashback refunds up to 10% of weekly net casino losses, capped at €6,988, over a week that runs Monday 00:00 UTC through Sunday 23:59 UTC, counting real-money play only. A player opts in for each four-week cycle, receives the credit in My Bonuses on Monday and wagers it 10x. The VIP tier sets the rate:

| Tier | Cap | Rate |
|---|---|---|
| Diamond | €6,988 | 10% |
| Platinum | €3,988 | 8% |
| Gold | €2,988 | 6% |
| Silver | €2,388 | 4% |
| Bronze | €1,888 | 2% |

Live Casino Cashback adds 25% up to €850. Daily rebates post per category: P2P 0.8%, lottery and live casino 1.0% each, casino 0.9%, each wagered 1x.

### Rewards Hub
Bonus Crab turns qualifying picks into a crab reward of bonus credits, Coins or Free Spins, valid for 7 days, with credit wagered 30x and spin winnings 40x. A turn of the Wheel of Fortune costs an eligible spin or Coins and carries 30x on bonus awards. Challenges, listed under Rewards, hand out Coins, bonus credits and Free Spins once their tasks are done. Collections share that area and pay Coins or bonus rewards for a completed set. The Coin Shop swaps Coins for reward items or bonus credit worth up to €4,500, with prices and extra wagering varying by item.

## VIP Programme: Levels, Points and Limits
=== b12 ===
Points from qualifying real-money play feed the Longfu88 VIP Program, and those points open a ladder of 25 numbered reward levels. The ladder is grouped into five tiers: Diamond is the highest and Bronze the lowest, with Silver, Gold and Platinum in between. Six sample levels below show the points each one needs, its reward, its cashback percentage and its withdrawal limit.

| Level | Points needed | Reward | Cashback rate | Withdrawal limit |
|---|---|---|---|---|
| 1 | 1 | €9.8 | 1% | €9,800 |
| 5 | 70 | €24.5 | 2% | €34,300 |
| 10 | 700 | €147 | 4% | €63,700 |
| 15 | 2,100 | €392 | 6% | €88,200 |
| 20 | 3,600 | €637 | 8% | €117,600 |
| 25 | 5,500 | €980 | 10% | €147,000 |

Every step up raises the cashback rate and the withdrawal limit, and personalised offers arrive along the way. A personal VIP manager becomes available from level 4. Rewards and limits are not uniform: amounts differ from level to level and from currency to currency, and the scheme's rules are open to change.

## Game Library by Category
Longfu 88 Casino fills its lobby with nine categories: slots, live dealer games, jackpots, table games, lottery, fast games, P2P games, fishing, plus crash and instant titles. A player at Longfu88 can therefore move from a reel session to a card table without leaving the site, and every category has its own place in the lobby. Slots and jackpots form the reel side, live dealer and table games cover the card side, and crash titles, lottery, fast games, P2P and fishing fill the remaining space. The three sections that follow look at slots, live casino play and the other game types in turn.

### Slot Games
Wanted Dead or a Wild, built by Hacksaw Gaming, sits at the aggressive end of this sample, rated very high for volatility, with 96.38% RTP and a 12,500x ceiling. Sweet Bonanza from Pragmatic Play is rated high for volatility, carries 96.48% RTP and reaches up to 21,175x. Gates of Olympus, also from Pragmatic Play, is rated at 96.50% RTP with high volatility and a 5,000x multiplier ceiling. RTP means the percentage of all stakes that a slot is built to pay back across a very large number of spins, so it describes the long run, not a single sitting. Volatility shows how evenly wins arrive: at higher settings, payouts come further apart and may be larger.

### Live Casino Games
Live dealer games are one category of the lobby, and their tables are run in real time by a human dealer rather than by software alone. The casino also offers a house-made title, Longfu88 Baccarat, which can be played live or as a table game and follows the rules of baccarat. Among the studios on the provider list, Evolution and SA Gaming operate live tables. Because the category sits beside slots and table games, a player can switch formats on the same account without registering again, and a person who likes a dealer at the table has a clear place to start.

### Other Game Types
Outside the reels and the live studio, the lobby adds game types that each work in a different way:

- **Crash and instant games:** the player places a stake on a rising multiplier or sees the outcome at once.
- **Lottery and fast games:** short draws and quick rounds that settle in moments.
- **P2P games:** players compete against each other, not against the house.
- **Fishing games:** arcade-style rounds where the player aims at targets on screen.
- **Table games:** classic card and table formats played against the casino.

## Software Providers
=== b17 ===
Slots, live tables and table games at Longfu 88 are powered by outside game studios, and the provider list spans reel-based titles as well as dealer-led formats. The studios are set out below in no particular order, so the sequence implies no ranking.

- Pragmatic Play
- NetEnt
- Evolution
- Betsoft
- Red Tiger
- Hacksaw Gaming
- Skywind
- Yggdrasil
- Big Time Gaming
- SA Gaming

## Payment Methods and Deposit Limits
Deposits are accepted through six method types, and the currencies attached to each are listed beside the examples.

| Method type | Examples | Currencies |
|---|---|---|
| Singapore banking | PayNow, PayNow QR, DBS Bank, OCBC Bank | SGD |
| Bank transfer | Bank Transfer | MYR, IDR, VND |
| Card payments | Mastercard, Visa | VND, SGD, MYR, IDR |
| European banking | Sofort, Giropay | EUR |
| Digital wallets | Neteller, Skrill | EUR |
| Crypto coins | USDC, USDT (TRC20, ERC20, BEP20), Litecoin, Ethereum, Bitcoin | USDC, USDT, LTC, ETH, BTC |

The Singapore row matters most to local readers, as DBS Bank, OCBC Bank, PayNow and PayNow QR all work in SGD. Each deposit starts at €10 and is capped at €5,000 per transaction, with the funds on the balance within 1-2 minutes. No handling charge comes from the casino, whereas providers or networks may add their own. Limits vary by residence, currency and method, and Neteller or Skrill deposits cannot trigger the welcome bonus. The route itself is short: log in to the Longfu88 account, open the cashier, choose Deposit and a method, enter the payment information and amount, then confirm.

### Withdrawal Methods and Times
Cash-outs run through Online Banking, DBS Bank, MoMo, DANA, Touch'n Go, USDT (TRC20, ERC20, BEP20), Litecoin, Ethereum, Bitcoin, Mastercard, Visa and Bank Transfer, from €20 to €5,000. Processing under the Lngfu88 withdrawal time takes three working days at most, and cards, crypto and wallets are typically settled in 1 to 3 business days, while a bank transfer can take 3 to 5 more days on the bank's side. No standard fee is levied by the casino, but a 10% commission (minimum €2.25) applies when wagering is lower than the deposit, 15% may apply to a share of the transactions financed by card or bank, and a 1x deposit turnover may be required. Six steps lead to a payout:

1. Sign in at Longfu88 and open the cashier.
2. Choose a supported method under Withdrawal.
3. Enter the amount and name the recipient.
4. Review and confirm the request.
5. Complete any identity or payment-method check that appears.
6. Await casino processing, then bank or network settlement.

ID verification can delay a payout, as the verification part above explains.

## Sportsbook
The Longfu sports lineup at Longfu88 spans nine disciplines: esports, tennis, cricket, basketball, volleyball, football, badminton, table tennis and virtual football. Seven bet types are available: handicap, Bet Builder, totals, live, outrights, accumulator and single. A single is a wager on one selection, whereas an accumulator ties several selections together on one slip, so every leg has to succeed. Live betting rests on in-play markets together with live odds, so a wager may be placed once a match has started. Availability is not identical everywhere: the player's jurisdiction may decide which events and which markets show up. The next part sets out the offers attached to the sportsbook and the rule that governs them.

### Sports Bonus Table
Core sports offers are listed below.

| Offer | Reward | Minimum deposit | Wagering |
|---|---|---|---|
| Sport First Deposit Bonus | 100% up to €1,888 | €50 | 8x deposit plus bonus |
| Sport Weekly Reload Bonus | 50% up to €2,500 | €50 | 8x deposit plus bonus |
| Sport Weekend Reload Bonus | 50% up to €3,750 | €50 | 8x deposit plus bonus |

Bet Builder Risk Free refunds up to €250 (50% of the stake), Parlay Boost lifts the payout of any three-leg slip or longer by up to 100%, early payout comes with 2 Goals Ahead, and every week Sports Cashback gives back 10% of net losses, capped at €2,500. Voided and cashed-out bets never count, while singles need odds of 2.00 and accumulator legs 1.50.

## Mobile Access and Installation
Mobile access runs through a responsive website that adjusts to small phone screens and larger tablet ones, so Android, iOS and the mobile browser all reach the same casino and sportsbook. Saved to the home screen as an icon, the site gives fast entry to casino play and sportsbook bets, and the phrase Longfu88 app describes exactly this installed shortcut. On a phone, casino games and the sportsbook work alongside bonuses, deposits, withdrawals and account access.

Android setup takes four steps in Chrome:

1. Open Longfu88 in Chrome.
2. Open the browser menu.
3. Pick Add to Home screen.
4. Confirm the shortcut.

On iPhone and iPad, Safari does the job:

1. Open Longfu88 in Safari.
2. Tap Share.
3. Select Add to Home Screen.
4. Confirm with Add.

## Customer Support Channels
Players who need help can reach the support team through two channels. Live chat is attended 24/7, so questions about a deposit, a bonus or an account can be raised at any hour. The second channel is e-mail, sent to support@longfu88.com, which suits longer questions that call for a written record. Assistance is given in six languages: English, Thai, Indonesian, Vietnamese, Simplified Chinese and Malay. No other contact route is listed for the casino, so these two are the ones to use.

## Responsible Gambling Policy
Gambling is open to adults aged 18 or over, and and play is acceptable solely in places where gambling is lawful. Self-exclusion starts when the player writes to customer support at support@longfu88.com. The request is handled within 24 hours of being processed, and for the agreed period both gambling and account access remain restricted. Closing the account also runs through customer support and takes four short steps: the request is made, the details held on the account are verified along with the preferred terms of exclusion, the casino's right to restrict or close access is accepted, and independent support is sought where the situation calls for it. Self-assessment questions let players spot signs that gambling is turning harmful. This page cannot replace independent help, and these organisations provide it:

- GamCare
- Gamblers Anonymous
- Gambling Therapy

## Pros and Cons Overview
Each advantage below comes with the condition attached to it.

| Pros | Cons |
|---|---|
| Minimum deposit of just €10 | Welcome bonus requires €50 down and a 25x rollover of deposit plus bonus |
| Weekly cashback reaching 10% | Cash-outs under the turnover rule can carry a 10% or 15% commission |
| Many payment methods, cryptocurrencies included | Bank withdrawals may take several business days |
| 24/7 live chat | First payout can be slowed by verification |

## Frequently Asked Questions
- **How does a registered player claim the Casino Welcome Bonus?** Activation takes place in My Bonuses after the qualifying €50 first deposit and ahead of any wager. Longfu88 requires no promo code, and none of the claiming steps mentions one.
- **Which wagering rules apply to the welcome bonus once it is active?** Deposit plus bonus must be wagered 25x, while Free Spins winnings carry 40x. The bonus stays valid for 10 days from activation, and the maximum bet is €22.5 per spin.
- **How long does it take for a withdrawal request to be completed?** Payouts to cards, crypto addresses and wallets take between 1 and 3 business days. A bank transfer first spends at most 3 business days with the casino, after which the receiving bank needs 3 to 5.
- **How is Casino Weekly Cashback calculated and credited to a player?** Net casino losses in a given week come back at up to 10% for opted-in players, limited to €6,988. The money is placed in My Bonuses every Monday and must be activated there.
- **How does a player climb the VIP ladder over time?** Points from eligible real-money play open 25 numbered VIP levels. Moving up the ladder raises the reward, the cashback rate and the withdrawal limit tied to the account.
- **How can the Longfu 88 password be reset when it has slipped a player's mind?** A reset link goes to the registered e-mail once Forgot Password is chosen on the sign-in page, and following its instructions sets a fresh password.

---

## BLOCK BRIEF
Block: b27, H2 "Verdict" (under H1 "Longfu88 Casino Complete Guide for Singapore Players")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 102-130 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 130, but never beyond 143 words.
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
- Player → should review → bonus conditions as well as limits on payments, prior to a deposit [7]
Summary: A closing verdict covering who the offer suits, what merits a check before depositing, and a brief nod to responsible gambling.
Copywriter Notes: Use three or four sentences to wrap up. Start with the profile of the person these facts serve: someone after slots, live tables and a sportsbook on one account, funded locally or in crypto. Second, what to verify before paying in: how the turnover rule applies to withdrawals, the €50 qualifying deposit with its 25x wagering, and ID verification. Finally, state the 18+ limit, then remind readers that gambling is no way to make a living, that a set budget and frequent pauses are the practical safeguards, and that losses must not be chased. Put "Longfu88 casino", i.e. the brand written Longfu88 Casino, into the opening sentence. Wherever "Longfu" appears, it is simply the casino's short name. Don't repeat figures, don't promise winnings, don't hype. Avoid any implication that Singapore authorises or vets this casino; licensing may be mentioned solely in the form the Brand Information records. Use "Longfu88" exactly once, "Longfu88 casino" (written as the name Longfu88 Casino) exactly once and "Longfu" exactly once, and no other tracked keyword.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_general.minimum_age: 18
- brandinfo_responsible_gaming.responsible_gaming.policy: Only adults who are 18 or over, and who play where it is lawful to do so, may gamble.; keep exactly: 18
