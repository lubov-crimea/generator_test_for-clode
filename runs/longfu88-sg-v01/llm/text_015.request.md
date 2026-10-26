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
Page intent: Longfu88 review for Singapore players who want the verdict and the numbers quickly. Cover in this order: one fact table, the Casino Welcome Bonus plus its conditions, promotions and rewards, VIP levels, games and studios, sports betting, sign-up and ID check, payments, phone play, then licence and data protection, safer-gambling guidance, support contacts, a brief FAQ and closing verdict. Voice: compact paragraphs of two to three sentences, roughly 14 words per sentence with a longer one now and then. Open every section on its most useful figure and close it on what that means for the player. Skip scene-setting and hook lines. Only two places carry a call to action: the welcome bonus section and the verdict. Each section is a flat H2 with no sub-sections. Brand facts come only from the AffBulk knowledge base longfu88-new; stay silent on whether Singapore law recognises the casino.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino in Singapore: Key Facts and Verdict (83-106 words): Opening paragraph: name the casino, sketch what it offers, give the year it started and address grown-ups in Singapore.
b02   H2 Key Facts in One Table (74-94 words): One-glance sheet of licence, operator, welcome bonus, minimum deposit, cashback, payments, currencies, languages and support.
b03   H2 Welcome Bonus and Its Terms (191-244 words): Casino Welcome Bonus numbers and four claiming steps, the competing offers, then a conditions table covering wagering, expiry and stake limits.
b04   H2 Weekly Promotions, Cashback and Rewards (160-203 words): Seven reload and seasonal offers in one table; weekly cashback tied to VIP tier and daily rebates; five reward features in short.
b05   H2 VIP Levels (77-97 words): How the VIP ladder works: points earned by real-money wagering, 25 levels inside five tiers, and what each climb unlocks.
b06   H2 Games and Studios (242-309 words): Nine game categories in one pass: three slot examples with RTP, live dealer with the exclusive baccarat, remaining categories, ten providers.
b07   H2 Sports Betting and Sports Offers (146-187 words): Sports and bet types on offer, live betting explained, then the sports bonus table and the odds rule common to them.
b08   H2 Sign-Up, Login and ID Check (173-219 words): Five numbered sign-up steps, then login with password recovery, followed by what triggers a document request, which documents count and how long review takes.
b09   H2 Deposits and Withdrawals (242-309 words): A deposit table of method types, limits and crediting speed plus the deposit route, then withdrawal methods, steps, payout times and fees.
b10   H2 Playing on Your Phone (90-113 words): Mobile access without an app: how the site behaves in Android, iOS and mobile browsers, the home-screen shortcut, and the account functions available.
b11   H2 Licence, Operator and Data Safety (165-212 words): Launch in 2026, which currencies and players are accepted, then licence, operator and the safeguards around data and accounts.
b12   H2 Responsible Gambling (90-113 words): Age rule, self-exclusion and closure through e-mail, self-assessment prompts and independent help organisations.
b13   H2 Support Channels (64-81 words): Ways to reach support, availability and supported languages.
b14   H2 Quick Answers (158-202 words): Quick answers on claiming the bonus, minimum deposit, withdrawal time and password recovery.
b15   H2 Final Verdict (83-106 words): Short closing verdict: the profile of player who fits, checks worth doing before depositing, and a safer-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino in Singapore: Key Facts and Verdict
Longfu88 opened its doors in 2026 with a lottery, a sportsbook, live-dealer tables and slots bundled up on one site. Jackpots, fishing, P2P, fast games, table games and crash and instant games fill out the lobby. Players from Singapore who are aged 18 and above can join.

Next come the key facts, licence line, games and studios, bonuses, mobile play, payments and responsible gambling. Every section opens on its most useful figure and ends on what it means in practice. Winnings are never promised, so a budget set in advance is the sensible starting point.

## Key Facts in One Table
| Parameter | Details |
|---|---|
| Licence | Costa Rica jurisdiction, Lumina as holder, registration 000-039123-R-319326-001 |
| Operator | Lumina, also the data controller |
| Welcome bonus | 188% match, 18 free spins, maximum amount €2,088 |
| Minimum deposit | €10 on any deposit |
| Cashback | Up to 10% of weekly net casino losses, capped at €6,988 |
| Payment methods | Mastercard, Bank Transfer, PayNow, Visa, Bitcoin, USDT (TRC20) |
| Currencies | THB, SGD, USD, EUR, MYR, USDT |
| Support languages | Thai, Malay, Indonesian, Vietnamese, English, Simplified Chinese |
| Support | 24/7 live chat and e-mail: support@longfu88.com |

## Welcome Bonus and Its Terms
The Longfu88 bonus is the Casino Welcome Bonus: €2,088 is the ceiling of a 188% match, and 18 Free Spins ride along. New registrants only qualify, one welcome offer per account. Its first qualifying deposit is €50, separate from the casino-wide €10 minimum deposit. Four steps claim it:

- Register and fill in the requested personal details.
- Make the first qualifying deposit.
- Open My Bonuses and switch the Casino Welcome Bonus on before placing any bet.
- Play eligible casino games until the wagering is finished.

No code is involved. After the deposit lands, the player activates the bonus in My Bonuses, so a Longfu88 promo code has no step on this route. Two alternatives exist: Live Casino Welcome Bonus pays 125% up to €888 for a €30 minimum deposit, while Casino Crypto Welcome Bonus pays 188% up to 2,888 USDT for a 50 USDT minimum deposit. A first deposit unlocks either the Casino Welcome Bonus or the Crypto variant, never both.

The payout conditions fit in a short table:

| Condition | Value |
|---|---|
| Wagering | 25x, counted on deposit plus bonus |
| Expiry | Lapses 10 days after activation |
| Free Spins winnings | 40x |
| Maximum bet | €22.5 per spin |
| Maximum cashout | 5x the initial bonus amount |

Deposits made with Skrill or Neteller are excluded, and the account holds one live promotional bonus at a time. Withdrawing before claiming or mid-bonus may cost eligibility, cancelling forfeits unconverted winnings, and an ID check may precede their release. Claim the Casino Welcome Bonus at Longfu88 once the €50 deposit is ready.

## Weekly Promotions, Cashback and Rewards
Seven offers share one table.

| Offer | Reward | Min. deposit | Wagering |
|---|---|---|---|
| Casino Trick or Treat Pumpkin Bonanza | Up to 100 Free Spins | €20 | 40x |
| Casino Dragon Quest | €10 credit | €20 | 30x |
| Casino Double Fortune | 50% match, max €500 | €30 | 30x |
| Casino Weekly Reload | 50 Free Spins | €30 | 40x |
| Casino Weekend Reload | Up to €3,360 + 50 Free Spins | €50 | 30x, 40x |
| Casino Weekly Crypto Reload | 60% up to 1,000 USDT | 20 USDT | 30x |
| Casino Weekend Crypto Reload | 75% up to 750 USDT + 100 Free Spins | 20 USDT | 30x, 40x |

My Bonuses activates each one: a single claim per period, no second live casino bonus, stakes capped at €5 a spin.

Casino Weekly Cashback returns up to 10% of weekly net casino losses, capped at €6,988, after a four-week opt-in. The credit lands in My Bonuses on Monday with 10x wagering. By VIP tier the rate is Bronze 2%, Silver 4%, Gold 6%, Platinum 8% and Diamond 10%. Live Casino Cashback adds 25% up to €850. Daily rebates carry 1x wagering: lottery 1.0%, live casino 1.0%, casino 0.9% and P2P 0.8%.

Challenges and Collections sit in the rewards area. Bonus Crab reveals a crab prize for 7 days, and the Wheel of Fortune runs on Coins or an eligible spin. The Coin Shop trades Coins for items and credit up to €4,500, with possible wagering rules.

## VIP Levels
Real-money wagering earns VIP points, and those points open a sequence of numbered levels: 25 of them, grouped under five tiers named Bronze, Silver, Gold, Platinum and Diamond. Level 1 asks for 1 point and carries a €9.8 reward, 1% cashback and a €9,800 withdrawal limit. At the top, level 25 requires 5,500 points and offers €980, 10% cashback and a €147,000 limit. Each step up improves personalised offers, withdrawal limits and cashback, while level 4 is where a personal VIP manager joins. Amounts differ by level and currency, and programme rules may change later.

## Games and Studios
Longfu88 Casino groups its games into nine categories: slots, live dealer games, jackpots, fishing, crash and instant games, P2P games, fast games, table games and lottery. The online casino spreads across jackpots, slots, fishing, lottery, P2P, fast games, crash games, table games and live dealer games, so a player can move from reels to cards to number draws without leaving the site.

Slots lead the list, and three titles show the range. Newcomers can read RTP as the long-term payback percentage of a slot over millions of spins, and volatility as how bumpy the payouts are. Wanted Dead or a Wild, from Hacksaw Gaming, has very high volatility, a 96.38% RTP and a top multiplier of 12,500x. Sweet Bonanza, from Pragmatic Play, pairs high volatility with a 96.48% RTP and a 21,175x ceiling. Gates of Olympus, also by Pragmatic Play, stands out for its RTP of 96.50% and a 5,000x top multiplier, again with high volatility.

Live dealer games sit in a category of their own, with Evolution and SA Gaming among the studios behind live tables. The live casino also showcases an exclusive, Longfu88 Baccarat, which follows standard baccarat gameplay.

Other categories differ mainly in how a player takes part. Table games are card and wheel formats played against the house. In P2P games the opponents are fellow players. Lottery rests on number draws, and fishing games ask the player to aim at moving targets. Fast games run short rounds, while crash and instant games end when a rising multiplier is cashed out in time or not.

Behind all of this stand ten providers: Yggdrasil, Skywind, SA Gaming, Red Tiger, Pragmatic Play, NetEnt, Hacksaw Gaming, Evolution, Big Time Gaming and Betsoft. Longfu 88 Casino gets slots as well as live and table titles from them, so no single studio defines the catalogue.

## Sports Betting and Sports Offers
Longfu sports is the sportsbook area of the platform. It groups racket sports (table tennis, badminton, tennis), ball sports (virtual football, volleyball, basketball, football), then cricket and esports. Bets come as live, single, handicap, outrights, Bet Builder, totals and accumulator. Live betting delivers in-play markets alongside live odds, and the events and markets on offer vary by jurisdiction.

Sport offers at Longfu88 stay apart from the casino bonuses. Three cards share a €50 minimum and 8x wagering:

| Offer | Reward | Min. deposit | Wagering |
|---|---|---|---|
| Sport Weekly Reload Bonus | 50% up to €2,500 | €50 | 8x |
| Sport First Deposit Bonus | 100% up to €1,888, valid 30 days | €50 | 8x |
| Sport Weekend Reload Bonus | 50% up to €3,750 | €50 | 8x |

Crypto versions start from 20 USDT and cap at 200, 500 and 1,000 USDT. Unlimited Sports Rebate pays 0.70% daily, and Sports Cashback gives back, weekly, 10% of eligible net sports losses, ceiling €2,500. Parlay Boost adds up to 100% on winnings on slips with at least three legs, while Bet Builder Risk Free gives 50% of the stake back, maximum €250. Only settled bets count: singles need odds of 2.00 or above, each accumulator leg 1.50, and voided or cashed-out bets are excluded.

## Sign-Up, Login and ID Check
Registration collects a legal name, e-mail, password, residential address and date of birth, and each player may hold one personal account only. Five numbered steps cover it:

1. Start at Longfu88 and click the Register button.
2. Key in a mailbox address, followed by a fresh password.
3. Confirm adulthood and agree to the Terms and Conditions plus Privacy Policy.
4. Complete the personal section, residential address included.
5. Hit Create Account, then follow the e-mail confirmation prompt if one appears.

Longfu88 login runs on e-mail and password: choose Login on the site, submit both, and clear any security check that appears before the account opens. Forgot Password on the login screen triggers a reset message, and its instructions let the player set a new password.

A verification request may arrive before a withdrawal goes through. Unusual or high-value transactions, an account review and changes to account or payment details can trigger one as well. Documents must be legible, current and consistent with the account profile:

- Identity: national ID card, driving licence or passport
- Address: utility bill or bank statement
- Proof of ownership of the payment method in use
- Source of funds, when requested

The submission window lasts up to 30 days, and a full set normally clears review inside 10 days. A withdrawal may be held until approval, and failed checks can lead to account restrictions or refused transactions.

## Deposits and Withdrawals
Deposit methods form six groups:

| Method type | Examples | Currencies |
|---|---|---|
| European banking | Sofort, Giropay | EUR |
| Electronic wallets | Neteller, Skrill | EUR |
| Crypto | Bitcoin, Litecoin, Ethereum, USDC, USDT on TRC20, ERC20 and BEP20 | USDT, USDC, ETH, BTC, LTC |
| Bank transfer | Bank Transfer | MYR, IDR, VND |
| Cards | Visa, Mastercard | IDR, SGD, VND, MYR |
| Singapore spotlight | OCBC Bank, DBS Bank, PayNow QR, PayNow | SGD |

Every method accepts at least €10 and at most €5,000 per transaction, and deposits credit in 1-2 minutes. The casino adds no processing fee, though providers and blockchain networks might. Exact limits depend on country, currency and method. The route runs through the cashier: choose Deposit, pick a method, enter the amount and follow the provider's confirmation. Neteller and Skrill deposits are shut out of the welcome bonus.

Withdrawals start at €20 and top out at €5,000. Destinations include Mastercard, Visa, MoMo, Touch'n Go, DANA, Online Banking, DBS Bank, Bank Transfer, Bitcoin, Ethereum, Litecoin and USDT over three networks. The process runs in six numbered steps:

1. Begin on Longfu88 by signing in, then enter the cashier.
2. Select Withdrawal and a supported route.
3. Key in the sum, plus the account, wallet or chain address to receive it.
4. Prove who owns the account and the payment method, where the casino asks.
5. Wait while the request is reviewed.
6. Receive the funds after the casino, bank or network settles the request.

Lngfu88 withdrawal time runs from 1 to 3 business days for cards, crypto and wallets, and requests are generally cleared within three working days. A bank transfer is handled by the casino in at most 3 business days, after which the bank adds 3 to 5 more. The casino charges no standard withdrawal fee, although provider and blockchain fees may be added. Turnover smaller than the sum deposited brings a 10% commission, minimum €2.25, and a prior 1x turnover on the deposit can be a condition. Certain transactions funded through a card or Bank Transfer can cost 15%. Pending ID checks can delay a payout.

## Playing on Your Phone
Mobile play runs through the browser: a responsive layout fits smartphones and tablets alike, which means no download, store page or APK is involved. Saving the site to the home screen puts the casino and the sportsbook one tap away, and that icon acts as the Longfu88 app while opening the same website, with account access, bonuses, deposits and withdrawals. On Android the steps are:

1. Open Longfu88 in Chrome.
2. Open the browser menu and pick Add to Home screen.
3. Confirm the shortcut.

On iOS, the route goes through Safari:

1. Open Longfu88 in Safari.
2. Tap Share, then choose Add to Home Screen.
3. Confirm Add.

## Licence, Operator and Data Safety
The online casino started operating in 2026 and takes account currencies SGD, THB, USD, EUR, MYR and USDT. A visitor about to register should check that the address belongs to the Longfu 88 Official Site, not to a copycat. Eligibility is straightforward: one personal account per player, age 18 and above, no third-party payment methods, and gambling that is lawful where the player lives.

The licence belongs to the operator Lumina, with Costa Rica as the jurisdiction and 000-039123-R-319326-001 as the registration number. For anyone weighing casino Longfu88, that licence line is the only regulatory statement made on this page. Lumina also acts as data controller, and its data protection officer can be reached at dpo@longfu88.com. Accounts, payments and personal information are guarded by technical and organisational measures. Data may go to regulators and law enforcement when required, payment service providers, technology providers and identity verification providers. Seven rights stay with the player: objection, withdrawal of consent, restriction, rectification, access, portability where applicable and erasure where legally permitted. Protecting login credentials falls to the account holder, and the operator may suspend activity for verification or suspected abuse.

## Responsible Gambling
Adults of 18 and over may play, and only in places where gambling is legal. Anyone wanting to step away can request self-exclusion by writing to customer support at support@longfu88.com. After processing, the restriction follows within 24 hours, and account access plus gambling can stay limited for the agreed period. Closure goes the same route: support receives the request, confirms the profile and the preferred exclusion terms, and access may be limited or cut off. Self-assessment questions help readers spot possible harm early. Gamblers Anonymous, GamCare and Gambling Therapy offer independent help, which this page cannot replace.

## Support Channels
Customer support has two channels. Live chat never closes, running 24/7, which suits a question that cannot wait until morning, such as a stalled deposit. For matters that need a written record, e-mail goes to support@longfu88.com. Help comes in six languages: Vietnamese, Thai, Simplified Chinese, Malay, Indonesian and English, so most Singapore players can write in the language they are most comfortable with. Both channels serve every account holder.

## Quick Answers
- **Once registration is complete, how does the Casino Welcome Bonus get claimed?** Depositing €50 as the first qualifying payment unlocks the offer, which is then activated in My Bonuses at Longfu88, before any bet is placed. No promo code is typed anywhere along this route.
- **Which deposit sum opens the platform, and which one the welcome bonus?** The platform-wide minimum is €10 per deposit. A €50 qualifying deposit is what the Casino Welcome Bonus needs, so a €10 payment alone will not trigger it.
- **How soon does a payout reach the player?** Money sent to a card, a crypto address or a wallet is released within 1-3 business days. Choosing bank transfer adds a casino stage capped at 3 business days, followed by a further 3-5 days at the receiving bank.
- **What should be done when the Longfu 88 password is forgotten?** Choosing Forgot Password on the login screen triggers an e-mailed reset link, and following that message sets a fresh password for the account.

---

## BLOCK BRIEF
Block: b15, H2 "Final Verdict" (under H1 "Longfu88 Casino in Singapore: Key Facts and Verdict")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 83-106 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 106, but never beyond 116 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 casino": exactly 1 time(s)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu": exactly 1 time(s)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Verdict [10]
- Welcome Bonus Terms [6]
- Responsible Gambling [6]
- Minimum Age [5]
Entity Connections to state explicitly [priority]:
- Player → ought to study → bonus rules and payment limits ahead of any deposit [7]
Summary: Short closing verdict: the profile of player who fits, checks worth doing before depositing, and a safer-gambling reminder.
Copywriter Notes: Verdict of three or four sentences. First sentence: the fit, a reader after one account that handles casino play, live dealers and sports bets, funded by local or crypto methods; if "Longfu88 casino" is used (as the name Longfu88 Casino), it belongs here. Second sentence: what to check before paying in, namely the €50 qualifying deposit, 25x wagering, verification and the turnover condition on withdrawals. Closing sentence or two: the 18+ line with reminders: gambling does not produce income, losses must not be chased, budgets and breaks are good practice. "Longfu" appears only as a short form of the casino name, if at all. Do not repeat figures, do not promise winnings, and keep hype out. Do not hint that any Singapore authority has licensed, legalised or approved the casino; a licence mention, if any, comes from the Brand Information alone. Closing call to action (version direction): put one plain invitation to claim the welcome bonus in this verdict; it is the page's second CTA. Use "Longfu88" exactly once, "Longfu88 casino" (written as the name Longfu88 Casino) exactly once and "Longfu" exactly once, and no other tracked keyword.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_general.minimum_age: 18
- brandinfo_responsible_gaming.responsible_gaming.policy: Participation requires an age of 18 or more, and gambling is allowed only in places where it is legal.; keep exactly: 18
