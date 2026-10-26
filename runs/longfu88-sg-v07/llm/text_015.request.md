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
Page intent: If a reader skims only one line, it should say that this is a Singapore-facing walkthrough of the Longfu88 online casino organised around the money trail: the fact table first, then deposits, withdrawals and fees, verification and payout checks, sign-up, the welcome bonus with its wagering, cashback and rebates, reloads, VIP levels with their withdrawal limits, games and studios, sports betting, mobile access, then licence and data safety, then responsible gambling, then support, a money FAQ and a closing verdict on the payment terms. When wording is in doubt, favour practical, number-led prose: sentences near 15 words, paragraphs of two or three sentences, and a final beat in every section that tells what the rule costs or how long it takes. Quote each amount together with its currency or condition. Allow a single call to action, and let it live in the welcome bonus section alone. Every brand fact comes out of AffBulk's longfu88-new knowledge base and nowhere else and stay silent on what Singapore law makes of the casino.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Payments, Bonuses and Payouts Reviewed (96-122 words): Compact opener: what kind of casino this is, which gaming areas it covers, when it launched, and that its audience is adult players in Singapore.
b02   H2 Payment and Brand Facts (88-112 words): At-a-glance fact table: the operator and its licence, what can be paid with and in which currencies, the smallest deposit, withdrawal limits, payout speed, the bonus and cashback headline and the available languages plus support.
b03   H2 Deposit Methods and Limits (141-178 words): Deposit methods sorted by kind, what every method has in common on limits and speed, the options tailored to Singapore, and the way the six steps run.
b04     H3 Withdrawals and Payout Times (128-162 words): Everything about getting money out: eligible methods, the six steps, how long it takes, request limits and the fees that can apply under certain conditions.
b05   H2 Verification and Payout Checks (109-138 words): Why verification is requested, which documents are accepted, how many days there are to send them, how long the check takes and what happens when it fails.
b06   H2 Registration and Login (123-157 words): How to register by e-mail in five numbered steps, what the sign-up form requests, the single-account rule, plus login and password recovery.
b07   H2 Welcome Bonus and Wagering (197-252 words): Opens with the welcome offer (its figures, how to claim it, rival offers) and closes with a terms table: wagering, duration, stake caps.
b08   H2 Cashback and Rebates (90-113 words): Cashback in its weekly and live-casino forms, with the rates tied to VIP level, along with per-category daily rebates.
b09   H2 Reloads and Seasonal Offers (122-154 words): Reload deals and seasonal campaigns measured on validity, wagering, minimum deposit and reward, finishing with the rules that bind every one of them.
b10   H2 VIP Levels and Withdrawal Limits (115-146 words): Real-money points feed a ladder of 25 reward levels split across five tiers, plus what moving up brings.
b11   H2 Games You Can Play (255-325 words): Overview of the nine categories, three example slots and their RTP numbers, the live area where the house-exclusive baccarat title sits, and the other game types.
b12   H2 Providers (70-90 words): The providers whose titles fill the lobby, named from the provider list.
b13   H2 Sports Betting and Its Bonuses (154-194 words): Sports covered and the kinds of bet available, in-play betting, and then the sports bonuses with the odds rule common to all.
b14   H2 Mobile Payments and Play (96-122 words): Playing on handheld devices: Android, iOS and mobile web all run through the browser; covers the responsive layout, a shortcut on the home screen and which account tools are available.
b15   H2 Licence and Data Protection (173-219 words): Starts with basic facts (launch year, currencies, eligibility), then licence, operator and how data and accounts are protected.
b16   H2 Responsible Gambling (96-122 words): Minimum age, then self-exclusion and account closure requested by e-mail, self-checks for harm, and independent organisations to turn to.
b17   H2 Support (70-90 words): Contact routes for support, when they are open and the languages offered.
b18   H2 Money Questions (172-218 words): Quick answers about the smallest deposit, usable crypto, account currencies, how long payouts take and whether withdrawals cost anything.
b19   H2 What the Payment Terms Mean (96-122 words): Closing verdict: which readers the offer fits, what to examine before a deposit and a reminder to play responsibly.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Payments, Bonuses and Payouts Reviewed
Longfu88 puts a sportsbook next to jackpots, slots, a lottery, fishing, P2P and table games, live dealer rooms, fast games and crash or instant titles, and the site has been running since 2026. That makes it a broad online casino, with nine game categories under one account and a betting section alongside them.

Readers in Singapore who are 18 or older are the audience here, since 18 is the age at which a player may join. The page opens with a table of payment and brand facts, then follows the money from deposits to withdrawals, before moving on to bonuses, games, mobile play, the licence, responsible gambling and support. Winning is never certain, so each section sticks to rules and numbers.

## Payment and Brand Facts
=== b02 ===
| Aspect | Details |
|---|---|
| Operator | Lumina |
| Licence | Lumina, Costa Rica, 000-039123-R-319326-001 |
| Payment methods | Mastercard, Bitcoin, PayNow, Bank Transfer, Visa, USDT (TRC20), Skrill, Neteller, DuitNow, Online Banking, GrabPay, Litecoin, Ethereum, Cardano |
| Currencies | USDT, THB, USD, SGD, MYR, EUR |
| Minimum deposit | €10, casino-wide |
| Withdrawal limits | €20 minimum, €5,000 maximum |
| Payout speed | 1–3 business days |
| Welcome bonus | 18 free spins plus a 188% bonus of up to €2,088 |
| Cashback | 10% returned on net casino losses each week, ceiling €6,988 |
| Languages | Indonesian, Thai, Simplified Chinese, Malay, English, Vietnamese |
| Support | support@longfu88.com, 24/7 live chat |

## Deposit Methods and Limits
Deposit options group into a few method types, with the Singapore routes listed first.

| Method type | Examples | Currencies |
|---|---|---|
| Singapore routes | PayNow, PayNow QR, OCBC Bank, DBS Bank | SGD |
| Cards | Mastercard, Visa | SGD, MYR, IDR, VND |
| Bank transfer | Bank Transfer | MYR, VND, IDR |
| E-wallets | Neteller, Skrill | EUR |
| European routes | Giropay, Sofort | EUR |
| Cryptocurrencies | Bitcoin, Ethereum, Litecoin, USDC, USDT (BEP20, ERC20, TRC20), Ripple, Cardano, Bitcoin Cash | BTC, ETH, LTC, USDC, USDT, XRP, ADA, BCH |
| Regional banks and wallets | DuitNow, GrabPay, DANA, QRIS, MoMo, PromptPay QR | MYR, IDR, VND, THB |

Every method shares one frame: a €10 minimum, a €5,000 maximum per transaction, and funds on the balance in roughly 1-2 minutes. Country, currency and method can each change the limits. The casino bills no handling charge on a deposit, whereas payment providers or blockchain networks may tack on their own. Neteller and Skrill deposits are left out of the welcome bonus. Six steps cover the process: sign in to Longfu88, open the cashier, press Deposit, pick a method and currency or network, enter the amount and payment information, then confirm with the provider.

### Withdrawals and Payout Times
Longfu88 pays out through bank-style options (Online Banking, DBS Bank, Bank Transfer), wallets (MoMo, DANA, Touch'n Go), cards (Mastercard, Visa) and crypto (USDT on three networks, Litecoin, Ethereum, Bitcoin). Each request must be at least €20 and no more than €5,000.

A withdrawal is capped at three business days on the casino's side, and typical requests finish within that span. Cards, crypto and wallets complete in 1-3 business days, while a bank transfer can be followed by 3 to 5 extra business days before the bank releases the money. Identity checks may delay a payout (see the verification section). The casino charges no regular withdrawal fee, though providers and networks may. If turnover falls below the deposited amount, a 10% commission (minimum €2.25) may apply under the 1x deposit turnover rule, and some card- or bank-funded transactions may attract 15%.

1. Sign in and open the cashier.
2. Tap Withdrawal.
3. Choose a payout method.
4. Enter the amount and receiving details.
5. Review and submit the request.
6. Wait while the casino and bank or network process it.

## Verification and Payout Checks
=== b05 ===
Longfu88 may require KYC verification before money leaves the account. A withdrawal request, unusual or high-value transactions and changes to payment details are the usual prompts. Four kinds of evidence are accepted:

- Identity: a passport, with a national identity card or driving licence as alternatives.
- Residence: a recent utility bill, or alternatively a statement from a bank.
- Funding tool: papers showing the player owns whichever bank card or digital wallet funds the account.
- Funds origin, on request: income proof, bank statements or other supporting financial papers.

The player gets 30 days to send the files, which need to be current and legible. Once the set is complete, a verdict follows after an assessment lasting up to 10 days. Until then withdrawals wait. If the check fails, transactions can be refused and the account restricted.

## Registration and Login
=== b06 ===
Longfu88 offers one sign-up route, by e-mail. The form collects a legal name, a date of birth and a residential address, along with the login details of the new account. A player is limited to a single account, and entry starts at age 18.

1. Select Register once the site is open.
2. Provide an e-mail and a freshly created password.
3. Tick the age confirmation, then accept the Privacy Policy and the Terms and Conditions.
4. Complete the extra personal fields, residential address included.
5. Hit Create Account, then finish whatever e-mail confirmation follows.

Returning players open the site, press Login and fill in the pair picked while joining, meaning the password and the e-mail address. After any security check clears, the Longfu88 login lands in the account. Anyone who forgot the password picks Forgot Password on the login screen, which mails a reset link, and the guidance inside that mail creates a new one.

## Welcome Bonus and Wagering
=== b07 ===
Longfu88 leads with the Casino Welcome Bonus, a first deposit casino bonus for newcomers. Eighteen free spins arrive alongside a 188% match of up to €2,088, which is all the Longfu88 bonus amounts to. A €50 first deposit is what qualifies, not the €10 minimum that applies elsewhere in the casino, and no account may collect the offer twice. Rival first-deposit choices are the Live Casino Welcome Bonus, 125% up to €888 from €30, and the Casino Crypto Welcome Bonus, 188% up to 2,888 USDT from 50 USDT.

A Longfu88 promo code is not a step in the procedure, since the claim goes through My Bonuses after the deposit:

- Open an account and give the personal data requested.
- Fund it with a qualifying first deposit.
- Activate the offer in My Bonuses prior to any wager.
- Clear the wagering requirement with eligible casino games before the offer ends.

The wagering requirement multiplies the deposit and bonus together by 25. Every other condition is collected in the table below.

| Condition | Value |
|---|---|
| Maximum bet | €22.5 per spin |
| Bonus validity | 10 days from activation |
| Wagering on free spins winnings | 40x |
| Maximum cashout | 5x the initial bonus amount |
| Wagering on deposit plus bonus | 25x |

Neteller and Skrill top-ups do not count toward the offer, and promotions are taken singly, so a second one waits until the active one ends. Eligibility is at risk when a cash-out is requested ahead of the claim or in mid-bonus. Cancelling forfeits bonus funds and unconverted winnings, and an account check may precede payment of bonus winnings. Claim the welcome bonus once the first qualifying deposit is in.

## Cashback and Rebates
=== b08 ===
Casino Weekly Cashback repays a slice of the net casino losses from the week, at most 10%, with €6,988 as the ceiling. Losses are measured between Monday 00:00 UTC and Sunday 23:59 UTC, and only real-money play counts, never bonus funds. After opting in, a player gets a four-week cycle. On Monday the credit lands in My Bonuses, with 10x wagering on it. Rates follow the VIP tier: Platinum pays 8% (maximum €3,988), Diamond 10% (€6,988), Gold 6% (€2,988), and the lower tiers Silver 4% (€2,388) and Bronze 2% (€1,888). Live Casino Cashback pays 25% up to €850. Daily rebates are 0.9% on casino, 1.0% on lottery, 1.0% on live casino and 0.8% on P2P play, each with 1x wagering.

## Reloads and Seasonal Offers
=== b09 ===
Seven offers run for 7 days, bar the one-day special. Dragon Quest, labelled Get Verified and Get Extra, gives a €10 bonus credit after verification (€20 minimum, 30x). Casino Trick or Treat Pumpkin Bonanza offers up to 100 Free Spins from €20, with 40x on winnings. The one-day reload special, Casino Double Fortune, runs 24 hours at 50% up to €500 from €30, with 30x. Casino Weekend Reload pays up to €3,360 + 50 Free Spins from €50, and Casino Weekend Crypto Reload 75% up to 750 USDT + 100 Free Spins from 20 USDT, both at 30x on deposit plus bonus and 40x on spin winnings. On the weekly side, Casino Weekly Reload pays out 50 Free Spins from €30 at 40x on winnings, and Casino Weekly Crypto Reload gives 60% up to 1,000 USDT from 20 USDT at 30x. Activation happens in My Bonuses. A promotional period allows a single claim, no offer stacks alongside an active casino bonus, and bonus stakes top out at €5 per spin.

## VIP Levels and Withdrawal Limits
=== b10 ===
In the Longfu88 VIP Program, VIP points come from eligible wagering with real money, and they lead to 25 numbered reward levels. The levels sit in five tiers, from Bronze at the bottom to Diamond at the top, with Silver, Gold and Platinum between. Six steps of the ladder appear below.

| VIP level | Points | Cashback | Reward | Withdrawal limit |
|---|---|---|---|---|
| 1 | 1 | 1% | €9.8 | €9,800 |
| 5 | 70 | 2% | €24.5 | €34,300 |
| 10 | 700 | 4% | €147 | €63,700 |
| 15 | 2,100 | 6% | €392 | €88,200 |
| 20 | 3,600 | 8% | €637 | €117,600 |
| 25 | 5,500 | 10% | €980 | €147,000 |

Each higher level enlarges the cashback as well as the withdrawal ceiling. From level 4 a personal VIP manager joins in, together with personalised offers. Rewards and withdrawal limits shift with the currency and the VIP level, and the rules of the programme are open to change.

## Games You Can Play
=== b11 ===
Longfu88 Casino groups its lobby into lottery, P2P games, jackpots, slots, crash and instant games, fishing, table games, fast games and live dealer games, nine categories in all. Betting on sport is available too and gets a separate section later. This part looks at slots, the live area and everything else in the lobby, with no totals of games or providers quoted.

Two numbers matter when a slot is judged. Return to player, or RTP, is the percentage of wagered money the game is designed to return to players as spins accumulate over time, while volatility tells how bumpy the ride is. High volatility means fewer but larger payouts, and a quiet stretch can precede them. Gates of Olympus returns an RTP of 96.50% with a 5,000x ceiling at high volatility. Pragmatic Play also made Sweet Bonanza: a 21,175x ceiling, 96.48% RTP and high volatility. Hacksaw Gaming developed Wanted Dead or a Wild, the riskiest of the trio: RTP 96.38%, very high volatility, 12,500x. They illustrate the slot range rather than ranking as favourites or exclusive picks.

Live dealer games occupy a lobby area of their own, where Evolution and SA Gaming are listed among the providers. Longfu88 Baccarat, a baccarat-style game exclusive to the house, is part of that area.

The other categories differ in what the player actually does. A lottery round ends with a draw after numbers are chosen. In crash and instant games, rounds are short and the player picks the moment to cash out. Fast games move through quick rounds with simple rules, fishing titles are shooting-style games with moving targets, in P2P games the opponents are other players, and table games bring in card and wheel classics. At Longfu 88 Casino these types therefore differ by opponent and round length.

## Providers
=== b12 ===
Ten game providers stock the Longfu 88 lobby with slots, live games and table games: Skywind, Yggdrasil, Hacksaw Gaming, Betsoft, Big Time Gaming, Red Tiger, NetEnt, Pragmatic Play, SA Gaming and Evolution. With that many makers behind the catalogue, the lobby does not rest on a single house style, and a reader can check the names before registering. Evolution and SA Gaming are the two linked to the live area, while the studios in between supply the other titles.

## Sports Betting and Its Bonuses
=== b13 ===
The sportsbook at Longfu88 spans nine sports and esports titles: basketball, football, tennis, badminton, cricket, volleyball, esports, table tennis and virtual football. Bets come as singles, accumulators, Bet Builder picks, handicaps, totals, outrights and live wagers. Live betting means in-play markets with odds refreshed as the action unfolds, and jurisdiction may change which events and markets are offered. In the Longfu sports area sit three deposit deals.

| Offer | Reward | Minimum deposit | Wagering requirement |
|---|---|---|---|
| Sport First Deposit Bonus | 100% up to €1,888 | €50 | 8x deposit and bonus |
| Sport Weekly Reload Bonus | 50% up to €2,500 | €50 | 8x the deposit plus bonus |
| Sport Weekend Reload Bonus | 50% up to €3,750 | €50 | 8x |

The first offer awards a bonus equal to 100% of the deposit, capped at €1,888, valid for 30 days. Parlay Boost lifts winnings by up to 100% on bets of 3 or more legs, Bet Builder Risk Free refunds 50% of the stake (maximum €250), and 2 Goals Ahead pays out early once the selected team leads by two goals. The Unlimited Sports Rebate pays 0.70%, and Sports Cashback returns 10% up to €2,500 of weekly eligible net sports losses. Voided or cashed-out bets do not qualify. Minimum odds are 2.00 on a single and 1.50 on each accumulator leg.

## Mobile Payments and Play
=== b14 ===
One responsive website fits both phone and tablet browsers, so Android, iOS and mobile web players land on the same casino and sportsbook inside the browser. Cashier tools, bonuses and the account sit in that same layout. Whenever the Longfu88 app comes up, the phrase refers to the website itself, pinned to the phone's starting page by an icon: that shortcut puts the casino and sportsbook one tap away.

For iOS, the list below sets up that shortcut:

1. In Safari, go to Longfu88.
2. Press the Share button.
3. Pick Add to Home Screen.
4. Confirm with Add.

For Android, the order differs slightly:

1. In Chrome, go to Longfu88.
2. Tap the browser menu.
3. Select Add to Home screen.
4. Accept the shortcut prompt.

## Licence and Data Protection
=== b15 ===
Launched in 2026, this online casino lets players keep a balance in USDT, THB, USD, SGD, MYR or EUR. Only adults aged 18 or more who are permitted under law to gamble where they reside may join. Each person is expected to use a single personal account, register with accurate details and avoid payment methods owned by others. Anyone trying to reach the Longfu 88 Official Site is better served by typing the address carefully than by clicking an imitation page.

For the casino Longfu88, the licence entry lists Lumina as the operating company, with registration number 000-039123-R-319326-001 and Costa Rica as the jurisdiction. The licence belongs to that operating company, which also takes the role of data controller. Its operator safeguards personal data, payments and accounts with technical and organisational safeguards. Regulators and law enforcement receive data when required, and so may technology, identity verification and payment service providers. Rights include access, rectification, restriction, objection, portability, withdrawing consent and erasure where legally permitted, with dpo@longfu88.com as the data contact. Guarding credentials falls to whoever owns the account, and activity may be suspended should the operator need verification or suspect abuse.

---

## BLOCK BRIEF
Block: b16, H2 "Responsible Gambling" (under H1 "Longfu88 Casino Payments, Bonuses and Payouts Reviewed")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 96-122 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 122, but never beyond 134 words.
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
- Responsible Gambling [10]
- Self-Exclusion [8]
- Account Closure [6]
- Self-Assessment [5]
- GamCare [5]
- Gambling Therapy [5]
Entity Connections to state explicitly [priority]:
- Self-Exclusion → starts → when the player writes to customer support by e-mail [8]
- Players → are pointed toward → Gambling Therapy, Gamblers Anonymous and GamCare [7]
Summary: Minimum age, then self-exclusion and account closure requested by e-mail, self-checks for harm, and independent organisations to turn to.
Copywriter Notes: Say that players must be at least 18 and may gamble only where the law allows. Self-exclusion: it is requested by writing to customer support by e-mail, blocks play and account access until the agreed period ends, and takes effect within 24 hours once the request is processed. Cover closing the account via customer support as well, summing up its four steps. Mention self-assessment questions for spotting problem play, and name Gambling Therapy, Gamblers Anonymous and GamCare in a single sentence. Should a reader wonder if this page is enough, state that it cannot replace independent help. Printing the Brand Information mailbox (the self-exclusion sentence works) gives this block its one "Longfu88". Use no tracked keyword in the body of this block.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_responsible_gaming.responsible_gaming: {"policy": "A player must hold the age of at least 18 years and respect local law on where gambling is permitted.", "self_exclusion": {"request_method": "Email support@longfu88.com", "processing_time": "Within 24 hours after the self-exclusion request is processed", "effect": "Limits on account access and gambling may be in force across the agreed period."}, "account_closure": "A request for account closure is made to customer support.", "self_assessment": "Possible harm from gambling can be identified by players answering self-assessment questions.", "support_organizations": ["Gamblers Anonymous", "Gambling Therapy", "GamCare"], "contact": "support@longfu88.com", "procedure": ["Support is the contact point for requesting self-exclusion or closing an account.", "The player states the terms of exclusion preferred and verifies the account details.", "Acceptance that the casino may restrict or close access is needed.", "Appropriate cases call for independent support to be sought."]}; keep exactly: 18, account access, customer support
