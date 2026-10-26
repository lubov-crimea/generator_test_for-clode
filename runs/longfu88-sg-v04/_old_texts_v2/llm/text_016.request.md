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
Page intent: Detailed brand-review page about the Longfu88 online casino for players from Singapore, written for a careful reader: who runs the casino and under which licence, the fact sheet, registration with account security and verification, the responsible-gambling tools, the welcome bonus with its terms, other promotions and VIP limits, payments with withdrawal timing, the game library, providers, the sportsbook, mobile access, support, a pros and cons table, an FAQ and a closing checklist. Page voice: precise and calm, sentences of about 20 words with a few short ones, paragraphs of three to four sentences; every advantage is followed by the condition or limit that goes with it, stated in the same detail as the advantage; a fact is followed by what it means in practice; one call to action only, at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Singapore.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Review: Licence, Limits and Player Protection (122-154 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Singapore.
b02   H2 Who Runs the Casino and Under Which Licence (204-260 words): Launch year, currencies and who may play, then the licence, the operator, the data controller and how data and accounts are protected.
b03   H2 Brand Fact Sheet (95-121 words): A fact sheet of the casino: licence, operator, launch year, Minimum age, languages, currencies, payment methods, welcome bonus, minimum deposit, cashback, Verification time, support.
b04   H2 Registration, Login and Account Security (123-157 words): How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.
b05     H3 Verification: Documents, Timing and Consequences (133-171 words): When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.
b06   H2 Responsible Gambling Tools (123-157 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b07   H2 Welcome Bonus and What It Requires (154-194 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b08     H3 Bonus Conditions in Detail (109-138 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b09   H2 Other Promotions and Their Rules (128-162 words): The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
b10     H3 Cashback and Rebate Conditions (83-106 words): Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
b11   H2 VIP Programme and Withdrawal Limits (115-146 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b12   H2 Payments and Deposit Limits (133-171 words): Deposit methods grouped by type with the general limits and speed, the local options for Singapore and the six-step deposit route.
b13     H3 Withdrawals, Fees and the Turnover Rule (128-162 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b14   H2 Game Library (83-106 words): The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.
b15     H3 Slots and Their RTP (102-130 words): Three example slots with their provider, RTP, volatility and maximum multiplier.
b16     H3 Live Casino (90-113 words): The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.
b17   H2 Game Providers (77-97 words): Which studios supply the games, named from the provider list.
b18   H2 Sports Betting Rules and Markets (109-138 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b19     H3 Sports Bonus Conditions (83-106 words): The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
b20   H2 Mobile Access (102-130 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b21   H2 Support and How to Reach It (77-97 words): Support channels, availability and languages.
b22   H2 Pros and Cons (53-67 words): A pros and cons table built only from facts stated elsewhere on the page.
b23   H2 Questions About Safety and Payouts (172-218 words): Short answers on verification time, one account, withdrawal fees, withdrawal time, who may play.
b24   H2 Checklist Before You Deposit (106-134 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Review: Licence, Limits and Player Protection
Longfu88 is an online casino launched in 2026 that covers nine game areas: slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games. A sportsbook sits beside them, so the online casino combines casino games, live dealer games, sports betting and lottery on one platform.

This review is written for players from Singapore, and for adults only: the minimum age is 18, and anyone younger may not register or play. The page follows the order in which a careful reader usually checks a casino. It begins with the operator and the licence, then covers the fact sheet, registration, bonuses and their terms, games, payments, mobile play and responsible gambling tools, so that the conditions behind every feature are clear before a deposit is made.

## Who Runs the Casino and Under Which Licence
=== b02 ===
The online casino was launched in 2026 and holds accounts in six currencies: EUR, USD, MYR, THB, SGD and USDT. SGD is on the list, so a player from Singapore can keep the balance in SGD. Registration is open to adults of 18 and older who are legally permitted to gamble in their place of residence. Each player may hold one personal account, must register with accurate information and may not use third-party payment methods. Because look-alike pages can imitate any casino, the safe habit is to open only the Longfu 88 Official Site address.

The licence of the casino Longfu88 sits in Costa Rica: the registration number is 000-039123-R-319326-001, and the licence is held by the operator, Lumina. A licence from one jurisdiction does not replace the rules of the country where a player lives, so local law still has to be checked before playing.

Lumina also acts as the data controller, and the data protection officer can be reached at dpo@longfu88.com. The operator protects accounts, payments and personal data with technical and organisational safeguards. Personal data may be shared with payment service providers, identity verification providers and technology providers, and with regulators and law enforcement when required. Players have rights of access, rectification, erasure where legally permitted, restriction, objection, portability where applicable and withdrawal of consent. The account holder stays responsible for safeguarding credentials, and the operator may suspend activity for verification or suspected abuse.

## Brand Fact Sheet
| Parameter | Details |
|---|---|
| Gambling licence | Jurisdiction Costa Rica, operator Lumina, registration number 000-039123-R-319326-001 |
| Operator | Lumina, also the data controller |
| Launched | 2026 |
| Minimum age | 18 years |
| Support languages | English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese |
| Currencies | EUR, USD, MYR, THB, SGD, USDT |
| Payment methods | Visa, Mastercard, Bank Transfer, Bitcoin, Ethereum, Litecoin, USDT (TRC20), PayNow |
| Welcome bonus | 188% up to €2,088 + 18 Free Spins |
| Minimum deposit | €10 for the casino in general |
| Cashback | Up to 10% of weekly net casino losses, capped at €6,988 |
| Verification time | Up to 10 days after a complete document set is received |
| Support | support@longfu88.com, 24/7 live chat or email |

## Registration, Login and Account Security
Registration is done by email and requires an email address, a password, a legal name, a date of birth and a residential address, collected over five steps.

1. Open Longfu88 and select Register.
2. Enter email and create a password.
3. Confirm age and acceptance of Terms and Conditions and Privacy Policy.
4. Complete the additional personal details and residential address.
5. Select Create Account and complete any requested email confirmation.

A player may hold only one personal account, and the age confirmation in step three covers 18+ and the legal gambling age of the relevant jurisdiction. The Longfu88 login runs on email and password: the player selects Login on the website, enters both and completes any security check. A forgotten password is handled through Forgot Password on the login screen. The reset link goes to the registered email, and the emailed instructions set a new password.

### Verification: Documents, Timing and Consequences
KYC verification may be required before a withdrawal, and also during an account review, on unusual or high-value transactions and after changes to account or payment details. The accepted documents fall into four groups:

- Identity: passport, national identity card or driving licence.
- Proof of address: utility bill or bank statement.
- Payment method: bank or card ownership evidence, or digital wallet ownership evidence.
- Source of funds, when requested: proof of income, bank statements or other supporting financial documents.

When Longfu88 asks for documents, they can be sent within up to 30 days, and a complete document set is reviewed within up to 10 days. Withdrawals may be held until the checks are done, and additional telephone or face verification can be requested. Failed checks can lead to refused transactions or account restrictions, so legible, current documents that match the account profile save the most time.

## Responsible Gambling Tools
Responsible gambling starts with the age rule: players must be at least 18 years old and gamble only where it is lawful. For a player who needs a break, self-exclusion is requested by email to customer support at support@longfu88.com. It is applied within 24 hours after the request is processed, and account access and gambling may be restricted for the agreed period, which is set with the player.

Account closure is requested through customer support in the same way. Both routes follow four short steps: contact support and ask for self-exclusion or closure, confirm the account details and the preferred terms, allow the casino to restrict or close access, and seek independent support where appropriate. Self-assessment questions help players identify possible gambling-related harm, which makes them a sensible habit before any deposit. Independent organisations give help that this page cannot replace:

- GamCare
- Gamblers Anonymous
- Gambling Therapy

## Welcome Bonus and What It Requires
The Casino Welcome Bonus is activated in My Bonuses after the qualifying deposit and before any wager. On the question of a Longfu88 promo code, the claiming route is that activation, and no promo code step is part of the listed claiming procedure.

The Longfu88 bonus is 188% up to €2,088 plus 18 Free Spins, that is spins on a slot with the stake paid by the casino. This deposit bonus is for new registered players on their first qualifying deposit, with one welcome offer per account. Its qualifying minimum deposit is €50, above the general minimum of the casino. Register at Longfu88 and claim the offer in four steps:

- Register an account and complete the required personal details.
- Make the first qualifying deposit.
- Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.
- Play eligible casino games and complete the wagering before expiry.

Two alternatives exist for a first deposit: the Live Casino Welcome Bonus (125% up to €888, minimum deposit €30) and the Casino Crypto Welcome Bonus (188% up to 2,888 USDT, minimum deposit 50 USDT). The Casino Welcome Bonus and the Crypto Welcome Bonus are alternative first-deposit offers.

### Bonus Conditions in Detail
The Casino Welcome Bonus comes with five conditions, and the wagering terms decide how much of the bonus can realistically be cashed out.

| Condition | Value |
|---|---|
| Wagering | 25x the deposit plus bonus amount |
| Free Spins wagering | 40x Free Spins winnings |
| Validity | 10 days from activation |
| Maximum bet | €22.5 per spin |
| Maximum cashout | 5x the initial bonus amount |

Deposits made with Neteller and Skrill are excluded from the promotion, and only one promotional bonus may be active at a time. A withdrawal request before claiming or while the bonus is active can void eligibility, and cancelling the promotion forfeits bonus funds and unconverted winnings. Account verification may also be required before promotional winnings are paid.

## Other Promotions and Their Rules
Seven further offers each have their own minimum deposit, wagering and validity:

- The **Casino Weekly Reload**: 50 Free Spins, €30 minimum, 40x winnings from Free Spins, 7 days.
- **Casino Weekly Crypto Reload**: 60% up to 1,000 USDT, 20 USDT minimum, 30x deposit plus bonus, 7 days.
- The **Casino Weekend Reload**: up to €3,360 + 50 Free Spins, €50 minimum, 30x deposit plus bonus and 40x Free Spins winnings, 7 days.
- **Casino Weekend Crypto Reload**: 75% up to 750 USDT + 100 Free Spins, 20 USDT minimum, 30x deposit plus bonus and 40x Free Spins winnings, 7 days.
- The **Casino Double Fortune**, the one-day reload special: 50% up to €500, €30 minimum, 30x deposit plus bonus, 24 hours.
- **Casino Trick or Treat Pumpkin Bonanza**, a seasonal promotion: up to 100 Free Spins, €20 minimum, 40x Free Spins winnings, 7 days.
- The **Casino Dragon Quest**, the verification reward: €10 bonus credit, €20 minimum, 30x promotional credit, 7 days.

Every offer is activated in My Bonuses and allows one claim per promotional period. None can be combined with another active casino bonus, and the maximum stake while wagering bonus funds is €5 per spin.

### Cashback and Rebate Conditions
The Casino Weekly Cashback returns up to 10% of weekly net casino losses, capped at €6,988, for the period from Monday 00:00 UTC to Sunday 23:59 UTC. It needs an opt-in for a four-week cycle, is credited to My Bonuses on Monday and carries 10x wagering of the cashback. The VIP cashback rates set the share and the cap:

| Tier | Rate | Maximum |
|---|---|---|
| VIP Bronze | 2% | €1,888 |
| VIP Silver | 4% | €2,388 |
| VIP Gold | 6% | €2,988 |
| VIP Platinum | 8% | €3,988 |
| VIP Diamond | 10% | €6,988 |

The Live Casino Cashback gives 25% up to €850. Four Unlimited Rebates are credited daily, each with 1x wagering: casino 0.9%, live casino 1.0%, P2P 0.8% and lottery 1.0%. Only real-money bets count, not bonus funds.

## VIP Programme and Withdrawal Limits
The VIP programme runs on points. VIP points come from eligible real-money play and unlock numbered reward levels, 25 in total, which are grouped into the tiers Bronze, Silver, Gold, Platinum and Diamond. Each level carries its own reward, cashback percentage and withdrawal limit, as the selected levels show:

| Level | Points | Reward | Cashback | Withdrawal limit |
|---|---|---|---|---|
| 1 | 1 | €9.8 | 1% | €9,800 |
| 5 | 70 | €24.5 | 2% | €34,300 |
| 10 | 700 | €147 | 4% | €63,700 |
| 15 | 2,100 | €392 | 6% | €88,200 |
| 20 | 3,600 | €637 | 8% | €117,600 |
| 25 | 5,500 | €980 | 10% | €147,000 |

Higher levels raise withdrawal limits and cashback, and they add personalised offers and, from level 4, a personal VIP manager. The cashback percentages in the table belong to the VIP levels and differ from the tier rates of the weekly cashback. Reward and withdrawal limits may differ by VIP level and currency, and the rules can change, so the current terms are worth checking before a player aims for a particular level.

## Payments and Deposit Limits
Deposit methods are grouped by type, with the Singapore options in the first row:

| Method type | Examples | Currencies |
|---|---|---|
| Local bank and wallet methods | PayNow, PayNow QR, DBS Bank, OCBC Bank | SGD |
| Cards | Visa, Mastercard | IDR, MYR, SGD, VND |
| Bank transfer | Bank Transfer, Online Banking | IDR, MYR, VND |
| Cryptocurrencies | Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), USDC | BTC, ETH, LTC, USDT, USDC |
| E-wallets and European methods | Neteller, Skrill, Sofort, Giropay | EUR |

Every method shares the same general limits: a minimum of €10, a maximum of €5,000 per transaction and crediting within 1-2 minutes. The casino charges no processing fee on deposits, but provider or blockchain network fees may apply, and limits can differ by country, currency and method. Neteller and Skrill deposits are excluded from the welcome bonus. The route has six steps: log in to the Longfu88 account and open the cashier, select Deposit, choose a method with its currency or network, enter the amount and payment details, confirm and authorise the payment, and wait for the funds to reach the playable balance.

### Withdrawals, Fees and the Turnover Rule
Withdrawals are paid by bank transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), Touch'n Go, DANA, MoMo, DBS Bank or Online Banking, with a €20 minimum and a €5,000 maximum, in six steps:

1. Log in to Longfu88 and open the cashier.
2. Select Withdrawal and choose a destination or payment method.
3. Enter the amount and the receiving bank, wallet, or blockchain address.
4. Complete identity and payment-method verification if prompted.
5. Review the request and confirm submission.
6. Wait for casino processing and any bank or network settlement.

The Lngfu88 withdrawal time depends on the method: cards, crypto and wallets take 1 to 3 business days, while a bank transfer needs up to 3 business days of casino processing plus 3 to 5 business days for bank delivery. Requests are generally processed within three working days, and identity checks may delay a payout. No standard casino withdrawal fee applies, but provider and blockchain fees may. A minimum 1x deposit turnover can apply before a withdrawal: where turnover is below the deposited amount, a 10% commission (minimum €2.25) may be charged, and 15% can apply to some card or bank transfer funded transactions.

## Game Library
The lobby of Longfu88 is split into nine game categories: slots, live dealer games, table games, jackpots, fishing, P2P games, fast games, lottery, and crash and instant games. This online casino offers all of them within one lobby, so a player can move from a slot to a live table or a lottery draw without leaving the site. These categories describe the structure of the lobby rather than the number of games in it. Two sub-sections look more closely at slots and at the live dealer section, while providers and the sportsbook have their own sections later on the page.

### Slots and Their RTP
Slots head the category list, and three examples show what the figures look like. Gates of Olympus from Pragmatic Play has an RTP of 96.50%, high volatility and a maximum multiplier of 5,000x. Sweet Bonanza, also from Pragmatic Play, has an RTP of 96.48%, high volatility and a maximum multiplier of 21,175x. Wanted Dead or a Wild is supplied by Hacksaw Gaming, with an RTP of 96.38%, very high volatility and a maximum multiplier of 12,500x. RTP is the share of stakes a slot returns to players over a very long run, while volatility describes how evenly those returns arrive: the higher the volatility, the longer the gaps between wins can be.

### Live Casino
Live dealer games form their own category in the lobby of Longfu 88 Casino, with tables hosted by dealers in real time. The category includes the exclusive Longfu88 Baccarat, an exclusive live or table game with baccarat gameplay, which gives a player who prefers baccarat a dedicated game to start from. Behind the category stand studios such as Evolution and SA Gaming, two providers from the casino's list that work in live dealer content, so the live section is powered by them among other studios. Which live games each studio supplies is not specified, and only baccarat is named here as a game of the casino's own.

## Game Providers
The studios behind Longfu 88 are named in the provider list: Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft and Hacksaw Gaming. Together, these game providers supply slots, live and table games to the casino. The slots section has already shown two of them at work, with Pragmatic Play behind Gates of Olympus and Sweet Bonanza and Hacksaw Gaming behind Wanted Dead or a Wild. A player who prefers a particular studio can look for its titles in the lobby before choosing a game.

## Sports Betting Rules and Markets
The sportsbook of Longfu88 covers nine sports and esports: football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football. Its Longfu sports section offers seven bet types: single, accumulator, live, handicap, totals, outrights and Bet Builder. A single is a bet on one selection, while an accumulator combines several selections into one bet, and a Bet Builder combines selections from the same event. Live betting brings live odds and in-play markets, so bets can be placed while an event is under way. Event availability and market selection can vary by jurisdiction, so the markets actually shown are the ones to check before planning a bet. The bonuses attached to the sportsbook follow in the next sub-section.

### Sports Bonus Conditions
The Sport First Deposit Bonus gives 100% up to €1,888 for a €50 deposit, with 8x wagering and 30 days of validity. Both reloads, the Sport Weekly Reload Bonus (50% up to €2,500) and the Sport Weekend Reload Bonus (50% up to €3,750), ask for the same €50 and 8x, with crypto versions. Sports Cashback returns 10% up to €2,500 of eligible weekly sports net losses, and the Unlimited Sports Rebate pays 0.70%. The 2 Goals Ahead early payout, Parlay Boost (up to 100% extra winnings, at least three legs) and Bet Builder Risk Free (50% stake back, up to €250) complete the list. Only settled qualifying bets count: singles need odds of at least 2.00, accumulator selections 1.50, and voided or cashed-out bets do not.

## Mobile Access
Mobile access rests on a responsive website that works on smartphone and tablet browsers, and the listed platforms are Android, iOS and mobile web. Adding the site to the home screen creates a shortcut with quick access to the casino and sportsbook. The Longfu88 app on a phone is therefore the home-screen version of the site. Casino, sportsbook, account access, deposits, withdrawals and bonuses are all available on mobile.

The Android route has three steps:

1. Open Longfu88 in Chrome.
2. Open browser menu and choose Add to Home screen.
3. Confirm the shortcut.

On iOS, the route runs through Safari:

1. Open Longfu88 in Safari.
2. Tap Share and choose Add to Home Screen.
3. Confirm Add.

## Support and How to Reach It
Customer support runs through two channels: a live chat that is available 24/7 and email support at support@longfu88.com. Live chat suits quick questions about a deposit or a bonus, while email fits requests that need a written record, such as self-exclusion or account closure. Support works in six languages: English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese, so a player can choose the language in which a question is easiest to put. Because live chat stays open around the clock, questions about verification or withdrawals can be raised as soon as they arise.

## Pros and Cons
Each advantage comes with a condition:

| Pros | Cons |
|---|---|
| Low minimum deposit of €10 | Welcome bonus needs a €50 deposit and 25x wagering on deposit plus bonus |
| Many payment methods, including cryptocurrencies | 10% or 15% commission can apply to withdrawals under the turnover rule |
| Weekly cashback of up to 10% | Bank withdrawals can take several business days |
| VIP programme with 25 levels, 24/7 live chat | Verification may delay the first payout |

---

## BLOCK BRIEF
Block: b23, H2 "Questions About Safety and Payouts" (under H1 "Longfu88 Casino Review: Licence, Limits and Player Protection")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 172-218 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 218, but never beyond 261 words.
Format: list. Visual Elements: Bulleted/numbered list — 8 of 8 lists on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": exactly 1 time(s)
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
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Frequently Asked Questions [8]
- Verification time [6]
- One account [6]
- Withdrawal fees [6]
- Withdrawal time [6]
Entity Connections to state explicitly [priority]:
- Frequently Asked Questions → cover → verification time, one account, withdrawal fees, withdrawal time, who may play [6]
Summary: Short answers on verification time, one account, withdrawal fees, withdrawal time, who may play.
Copywriter Notes: A bulleted list of exactly 5 items, each a bold question followed by a short answer of 20-30 words, in this order: (1) how long identity verification takes (up to 10 days after a complete document set; up to 30 days to send the documents when requested); the question contains the keyword "Longfu 88" exactly once, written verbatim; (2) whether a player may have more than one account (no: one personal account per player, and the account must be registered with accurate information); (3) whether withdrawals carry fees (no standard casino fee; provider and blockchain fees may apply; a 10% commission with a minimum of €2.25 can apply where turnover is below the deposit, and 15% on some card or bank funded transactions); the answer contains the keyword "Longfu88" exactly once, written verbatim; (4) how long a withdrawal takes (card, crypto and wallet withdrawals 1 to 3 business days; bank transfer up to 3 business days of casino processing plus 3 to 5 business days of bank delivery; the wording must differ from the withdrawals section); (5) who may play (at least 18 years old and legally permitted to gamble in the place of residence). The brand name "Longfu88" may stand in an answer, never in a question. These are the only questions on the page; the questions are the one place where question form is allowed. Use "Longfu88" exactly once and "Longfu 88" (written with a space) exactly once, and no other tracked keyword.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_account.verification.typical_review_time: Up to 10 days after a complete document set is received
- brandinfo_account.verification.document_submission_window: Up to 30 days when requested
- brandinfo_account.registration.eligibility: ["18+ and of legal gambling age in the relevant jurisdiction.", "Only one personal account per player."]
- brandinfo_privacy_policy.terms_conditions.conditional_fees: ["Where qualifying turnover is below the deposited amount, a 10% commission may apply with minimum €2.25.", "A 15% charge can apply to some card or bank transfer funded transactions under the casino rules."]
- brandinfo_withdrawal.withdrawal_methods[0].transaction_speed: Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days
- brandinfo_withdrawal.withdrawal_methods[1].transaction_speed: 1–3 business days
- brandinfo_general.minimum_age: 18
