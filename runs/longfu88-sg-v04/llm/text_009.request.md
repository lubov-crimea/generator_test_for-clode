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
Page intent: Who is this page for, and what do they need to settle before opening an account? A careful adult in Singapore weighing up the Longfu88 online casino, so the page walks through the operator and its licence, a quick fact sheet, sign-up with account safety and identity checks, the responsible-gambling tools, then the welcome bonus plus the conditions tied to it, then the other offers and VIP limits, deposits and payout timing, the games, studios and sportsbook, mobile play, and last support, a table weighing pros against cons, an FAQ and a final checklist. Voice: calm and exact, mostly sentences near twenty words with the odd short one, no paragraph is shorter than three sentences or longer than four. After each advantage comes its condition or limit, given as much room as the advantage itself, and each fact is followed by what it changes for the player. The page carries just one call to action, set beside the welcome bonus. For brand facts the only source is AffBulk, namely the longfu88-new knowledge base; the page keeps silent on how Singapore law regards the casino.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (as a fact card from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino Review: Licence, Limits and Player Protection (122-154 words): What is Longfu88 and who is reading about it? A brief orientation: the game areas on offer, the year it started and the adult Singapore audience.
b02   H2 Who Runs the Casino and Under Which Licence (204-260 words): Who stands behind the casino? Begins with the launch year, the supported account currencies and the admission rules; then come the licence, the operator, the data controller and the protection given to accounts and data.
b03   H2 Brand Fact Sheet (95-121 words): An at-a-glance fact sheet covering the licence and operator, launch year, Minimum age, languages offered, accepted currencies, payment methods, minimum deposit, welcome bonus, cashback, Verification time and support.
b04   H2 Registration, Login and Account Security (123-157 words): How does a newcomer sign up? Five numbered steps for registering by e-mail, which details the form collects, the one-account rule, and then signing in and recovering a password.
b05     H3 Verification: Documents, Timing and Consequences (133-171 words): When is a player asked to prove their identity? What sets a check off, which papers are accepted, the period for submitting them, how long the review runs and the outcome of a failed check.
b06   H2 Responsible Gambling Tools (123-157 words): How can players keep control? The age minimum, self-exclusion, account closure when the player e-mails a request, self-test questions and where outside support is found.
b07   H2 Welcome Bonus and What It Requires (154-194 words): What does the Casino Welcome Bonus give and how is it claimed? Its percentage, maximum amount, free spins, required qualifying deposit, the eligible players, a four-step claim route, and finally the pair of alternative first-deposit offers.
b08     H3 Bonus Conditions in Detail (109-138 words): Which terms apply to the Casino Welcome Bonus? Conditions in table form, plus the exclusions and how a real player is affected by them.
b09   H2 Other Promotions and Their Rules (128-162 words): Which reload offers and campaigns come back regularly? For each: what it pays, the deposit needed, the wagering and how long it lasts; and finally the conditions all of them share.
b10     H3 Cashback and Rebate Conditions (83-106 words): How much comes back to the player? Three layers: the Casino Weekly Cashback with its VIP-tier rates, the Live Casino Cashback, and a separate daily rebate for each game category.
b11   H2 VIP Programme and Withdrawal Limits (115-146 words): What does the VIP programme offer? How VIP points are earned through real-money play, and how they feed five tiers made of 25 reward levels with perks that expand toward the top.
b12   H2 Payments and Deposit Limits (133-171 words): How do deposits work? Which methods exist per type, which limits and speed apply to all of them, which options suit Singapore, and what the six deposit steps are.
b13     H3 Withdrawals, Fees and the Turnover Rule (128-162 words): How does a payout work? Supported payout methods, the six steps to follow, the time a payout needs, minimum and maximum amounts, and fees that vary with circumstances.
b14   H2 Game Library (83-106 words): How big is the lobby? Nine categories in all: P2P, slots, lottery, jackpots, crash and instant games, live dealer, fishing, table games and fast games.
b15     H3 Slots and Their RTP (102-130 words): Which slots illustrate the lobby? Three sample slots, each described by studio, volatility, RTP and highest multiplier.
b16     H3 Live Casino (90-113 words): What does the live section offer? The live section's position within the lobby, the casino's own baccarat game and the live studios named among the providers.
b17   H2 Game Providers (77-97 words): Who supplies the games? The studios, quoted straight from the provider list.
b18   H2 Sports Betting Rules and Markets (109-138 words): What can be bet on? Which sports and esports are covered, how a bet can be placed and what live betting adds.
b19     H3 Sports Bonus Conditions (83-106 words): Which offers does the sportsbook have? Weekend and weekly reload offers, the first deposit bonus, a cashback, an early payout, Parlay Boost and Bet Builder Risk Free, followed by the odds condition they have in common.
b20   H2 Mobile Access (102-130 words): How does mobile play work across Android, iOS and mobile web? A responsive layout, an icon placed on the home screen, and the usual account actions close at hand.
b21   H2 Support and How to Reach It (77-97 words): How can players get help? Channels, hours and languages.
b22   H2 Pros and Cons (53-67 words): What speaks for and against the casino? A table that sets pros against cons and draws exclusively on facts stated in earlier sections.
b23   H2 Questions About Safety and Payouts (172-218 words): Which questions come up most? Short answers on verification time, one account, withdrawal fees, withdrawal time and who may play.
b24   H2 Checklist Before You Deposit (106-134 words): What is the verdict? Who the offer is meant for, what deserves a second look prior to depositing, and a final responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino Review: Licence, Limits and Player Protection
Longfu88 is an online casino launched in 2026 that unites slot-style games, live dealer tables, sports wagering and lottery in a single place. The review addresses grown-up readers in Singapore who want the main points settled before opening an account, since membership starts at 18.

Nine game categories make up the lobby. Slots, live dealer rooms and table games form the familiar core, while jackpots, fishing titles and P2P games sit on a second shelf. Fast games, lottery draws and crash and instant titles cover shorter rounds. A sportsbook runs alongside the casino for readers who prefer betting on matches to spinning reels.

Next come the licence and the fact sheet, followed by bonuses, the game lobby, payments, play on a phone and safer gambling. Gambling carries real risk and costs real money, so nothing here suggests that a player will win.

## Who Runs the Casino and Under Which Licence
Starting from 2026, Longfu88 has run as an online casino whose account currencies are USDT, EUR, SGD, THB, USD and MYR. Anyone heading for the Longfu 88 Official Site should type the address by hand and ignore look-alike pages. Admission rules are short: the player is 18 or older, registers with accurate details, keeps a single personal account and pays only with methods in their own name. Local law matters too, since play is allowed only where gambling is lawful for the resident, so a check of local rules comes before any deposit.

The licence answers the next question. Costa Rica is the jurisdiction, the registration number is 000-039123-R-319326-001, and the licence has been awarded to the operator Lumina. Behind casino Longfu88 therefore stands a named company, which also acts as the data controller for personal information. Questions about data go to the data protection officer, whose e-mail address appears in the privacy policy.

Recipients of personal data can include technology providers, identity verification providers and payment service providers, and also regulators or law enforcement whenever such bodies make a demand. A player may ask for access, rectification, restriction or objection, and also has portability where applicable, the withdrawal of consent, and deletion in cases the law allows. Technical and organisational measures let the operator guard player accounts, payments and personal information. Keeping login credentials safe is the duty of the account holder, while the operator reserves the right to put activity on hold if abuse is suspected.

## Brand Fact Sheet
| Topic | Information |
|---|---|
| Licence | Issued in Costa Rica to Lumina, number 000-039123-R-319326-001 |
| Operator | Lumina, which handles personal data as controller |
| Launched | Year 2026 |
| Minimum age | 18 years or older |
| Support languages | English, Simplified Chinese, Malay, Thai, Vietnamese, Indonesian |
| Currencies | SGD, USD, EUR, USDT, THB, MYR |
| Payment methods | Visa, Mastercard, PayNow, Bank Transfer, Bitcoin, USDT (TRC20), Skrill |
| Welcome bonus | 18 free spins with a 188% match capped at €2,088 |
| Minimum deposit | Lowest accepted amount across the casino: €10 |
| Cashback | Weekly refund, 10% at most, based on net casino losses |
| Verification time | Up to 10 days after the document set is complete |
| Support | support@longfu88.com and 24/7 live chat |

## Registration, Login and Account Security
Signing up at Longfu88 runs on e-mail and takes five steps, and the form gathers an e-mail plus password, the full legal name, the date of birth and the place of residence.

1. Open the website and select Register.
2. Type in an e-mail address and create a password.
3. Confirm the age, the Terms and Conditions and the Privacy Policy.
4. Fill in the remaining personal details, including the residential address.
5. Press Create Account, then answer the confirmation request in the inbox if one arrives.

A second profile is ruled out, because the casino allows one personal account per player. Coming back through the Longfu88 login means picking Login on the site, typing the e-mail and password that were registered, and passing whichever security check is shown. Lost passwords are handled with the Forgot Password option on that screen: the system mails a link for choosing a new password, and following it completes the recovery.

### Verification: Documents, Timing and Consequences
KYC verification, the identity check that casinos run on their players, may be required before any cash-out. Longfu88 can raise it when a withdrawal is coming, when an account review takes place, when transactions look unusual or large, and when account or payment details change. The accepted papers fall into four groups:

- Identity: a passport, a national identity card or a driving licence.
- Proof of residence: a bank statement or a utility bill.
- Payment channel: evidence that the card, bank account or e-wallet in question belongs to the player.
- Origin of funds: proof of income, bank statements or other financial documents if the casino asks.

Players have up to 30 days to hand in readable, current documents that match the account profile. Once the set is complete, the review runs for up to 10 days, and a telephone or face check may be added as an extra step. Funds may stay on hold meanwhile. A failed check may lead to refused transactions, a restricted account, or payouts withheld until compliance is settled.

## Responsible Gambling Tools
Control tools begin with a floor of 18 years and a limit on where play takes place: gambling is allowed only in places where the law permits it. A player who wants a break can ask for self-exclusion, which gets underway once the request is e-mailed to customer support. Once it is processed, within 24 hours, the agreed period may bring limits on gambling as well as on account access. Account closure runs through the same channel and follows four short steps: contact support, confirm the account details and the terms of exclusion preferred, give the casino permission to restrict or close access, and receive a pointer to independent help where it is suitable.

Self-assessment questions help a player notice whether gambling has started to cause harm. Players may get in touch with outside organisations when the answers worry them:

- GamCare
- Gamblers Anonymous
- Gambling Therapy

None of these tools replaces advice from independent professionals, and a player in doubt should seek that help before making another deposit.

## Welcome Bonus and What It Requires
Claiming needs no code. Longfu88 asks the player to switch the offer on inside My Bonuses once the qualifying deposit has landed, and the published procedure holds no Longfu88 promo code step at all. The Longfu88 bonus named Casino Welcome Bonus is a first deposit offer: its match rate is 188%, the ceiling sits at €2,088, and 18 free spins join the package. It requires a qualifying deposit of €50, whereas deposits in general start at €10, so the two figures should not be confused. Only newly registered players qualify, and each account receives a single welcome offer.

The route to the offer has four stages:

- Register and fill in the personal details the site requires.
- Deposit the first qualifying amount.
- Activate the Casino Welcome Bonus under My Bonuses, ahead of any wager.
- Meet the wagering by playing eligible casino games while the offer is valid.

Two further first-deposit offers stand as alternatives. The Live Casino Welcome Bonus pays 125% up to €888 against a €30 deposit, while the Casino Crypto Welcome Bonus pays 188% up to 2,888 USDT against 50 USDT. A newcomer who is ready can claim the Casino Welcome Bonus right after registering.

### Bonus Conditions in Detail
Five terms decide whether the Casino Welcome Bonus can turn into withdrawable money, and each one deserves a look before the deposit is made.

| Condition | Value |
|---|---|
| Wagering requirement | 25x the deposit plus bonus amount |
| Maximum bet | €22.5 on each spin |
| Validity | 10 days from activation |
| Maximum cashout | 5x the initial bonus amount |
| Free Spins winnings | 40x wagering |

A deposit made through Neteller or Skrill is ineligible, and just a single promotion can run at once. Requesting a withdrawal before the claim or during bonus play may cancel eligibility, which means losing the bonus money together with unconverted winnings. The account may also be asked for verification prior to payout of bonus winnings.

## Other Promotions and Their Rules
Seven offers recur, each by reward, deposit, wagering and validity.

- **Casino Weekend Crypto Reload**: 75% up to 750 USDT + 100 Free Spins, 20 USDT, 30x deposit plus bonus and 40x Free Spins winnings, for 7 days.
- **Casino Weekend Reload**: up to €3,360 + 50 Free Spins, €50, 30x deposit plus bonus and 40x Free Spins winnings, for 7 days.
- **Casino Weekly Crypto Reload**: 60% up to 1,000 USDT, 20 USDT, 30x deposit plus bonus, for 7 days.
- **Casino Weekly Reload**: 50 Free Spins, €30, 40x winnings from Free Spins, for 7 days.
- **Casino Trick or Treat Pumpkin Bonanza**: up to 100 Free Spins, €20, 40x Free Spins winnings, for 7 days.
- **Dragon Quest, Get Verified and Get Extra**: €10 bonus credit, €20, 30x promotional credit, for 7 days.
- **Casino Double Fortune: One-Day Reload Special**: 50% up to €500, €30, 30x deposit plus bonus, for 24 hours.

Each is switched on under My Bonuses and claimed once per promotional period. None runs beside another active casino bonus, and a spin may stake at most €5 while bonus money is wagered.

### Cashback and Rebate Conditions
Casino Weekly Cashback returns up to 10% of weekly net casino losses, capped at €6,988. Monday 00:00 UTC opens the tally and Sunday 23:59 UTC closes it. That credit reaches My Bonuses on Monday and carries 10x wagering, while every four-week cycle needs its own opt-in. Rates depend on level:

| Level | Rate | Cap |
|---|---|---|
| VIP Bronze | 2% | €1,888 |
| VIP Silver | 4% | €2,388 |
| VIP Gold | 6% | €2,988 |
| VIP Platinum | 8% | €3,988 |
| VIP Diamond | 10% | €6,988 |

Live Casino Cashback pays 25% up to €850. Four daily rebates run at 0.9% for casino, 1.0% for live casino, 0.8% for P2P and 1.0% for lottery, each with 1x wagering and real-money bets only.

## VIP Programme and Withdrawal Limits
Within the Longfu88 VIP Program, wagering real money on eligible games collects VIP points. Collected points lead to reward levels that carry numbers. The ladder holds 25 levels grouped in five tiers: Diamond at the peak, with Platinum, Gold, Silver and Bronze beneath it. Six steps show how rewards and limits scale:

| Level | Points needed | Reward | Cashback | Withdrawal limit |
|---|---|---|---|---|
| Level 1 | 1 point | €9.8 | 1% | €9,800 |
| Level 5 | 70 points | €24.5 | 2% | €34,300 |
| Level 10 | 700 points | €147 | 4% | €63,700 |
| Level 15 | 2,100 points | €392 | 6% | €88,200 |
| Level 20 | 3,600 points | €637 | 8% | €117,600 |
| Level 25 | 5,500 points | €980 | 10% | €147,000 |

Higher levels enlarge both the cashback share and the withdrawal ceiling. Personalised offers come with them, and level 4 onward adds a personal VIP manager. Rewards and limits may differ by currency as well as level, while programme rules can alter benefits or promotion eligibility.

---

## SECTION
Write the blocks b12, b13 in ONE answer, in this order. They are one continuous section of the page: the sub-sections continue the parent, so the text must flow from block to block without repeating itself. Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts.

---

## BLOCK BRIEF
Block: b12, H2 "Payments and Deposit Limits" (under H1 "Longfu88 Casino Review: Licence, Limits and Player Protection")
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): b13 H3 "Withdrawals, Fees and the Turnover Rule"
Word Count: 133-171 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 171, but never beyond 188 words.
Format: paragraph + table. Visual Elements: Table — 5 of 6 tables on the page
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
- Deposits → arrive → within 1-2 minutes [8]
- Casino → charges → nothing for processing deposits, while providers and networks may bill their own fees [7]
Summary: How do deposits work? Which methods exist per type, which limits and speed apply to all of them, which options suit Singapore, and what the six deposit steps are.
Copywriter Notes: How does money reach the account, and what are the ceilings? After a single introductory sentence, insert a Markdown table with Method type, Examples and Currencies as its columns. Rows: cards (Mastercard, Visa); then local bank and wallet methods; bank transfer; cryptocurrencies (USDC alongside the remaining listed coins, Bitcoin, Ethereum, Litecoin and USDT via three networks: TRC20, ERC20, BEP20); e-wallets (Neteller and Skrill) and European methods (Sofort and Giropay). Singapore readers get OCBC Bank, DBS Bank, PayNow QR and PayNow highlighted, with SGD as currency, as supplied. Limits that hold for all methods: from €10 up to €5,000 per transaction, with funds credited in 1-2 minutes. The casino adds no processing fee itself, though a payment provider or a blockchain network might charge one. Leave out the per-currency limit lines that single methods carry, since euro signs and local-currency figures are mixed in them; tell the reader instead that the method, the currency and the country can each alter the limits. A deposit made with Neteller or Skrill cannot be used to claim the welcome bonus. Beneath the table, squeeze the deposit route (six steps) into a line or two. Nothing tracked belongs inside the table. Use "Longfu88" exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_deposit.deposit_methods: [{"method": "VietQR", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €300,000 per transaction"]}, {"method": "Online Banking", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €10,000 per transaction"]}, {"method": "Ethereum", "currencies": ["ETH"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["THB: minimum €370, maximum €182,910 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "PayNow QR", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €10, maximum €5,000 per transaction"]}, {"method": "Skrill", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Neteller", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "BNI", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €20, maximum €40,000 per transaction"]}, {"method": "Litecoin", "currencies": ["LTC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "MYR: minimum €50, maximum €23,840 per transaction"]}, {"method": "DANA", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €5,000 per transaction"]}, {"method": "Sofort", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "GrabPay", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €5,000 per transaction"]}, {"method": "Zalo", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €100,000 per transaction"]}, {"method": "Ripple", "currencies": ["XRP"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["THB: minimum €370, maximum €182,910 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction"]}, {"method": "Bank Transfer", "currencies": ["MYR", "VND", "IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €50, maximum €50,000 per transaction", "IDR: minimum €25, maximum €82,000 per transaction", "VND: minimum €100, maximum €500,000 per transaction"]}, {"method": "PayNow", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €10, maximum €5,000 per transaction"]}, {"method": "PromptPay QR", "currencies": ["THB"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["THB: minimum €300, maximum €200,000 per transaction"]}, {"method": "Touch'n Go", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €5,000 per transaction"]}, {"method": "Bitcoin", "currencies": ["BTC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["THB: minimum €1,100, maximum €182,910 per transaction", "MYR: minimum €145, maximum €23,840 per transaction", "VND: minimum €929, maximum €154,949 per transaction", "SGD: minimum €45, maximum €7,560 per transaction", "IDR: minimum €590, maximum €98,490 per transaction"]}, {"method": "BCA", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €5,000 per transaction"]}, {"method": "MoMo", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €30,000 per transaction"]}, {"method": "ViettelPay", "currencies": ["VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €50, maximum €20,000 per transaction"]}, {"method": "OVO Wallet", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €2,000 per transaction"]}, {"method": "DuitNow", "currencies": ["MYR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €30, maximum €50,000 per transaction"]}, {"method": "Mastercard", "currencies": ["SGD", "VND", "MYR", "IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €18, maximum €3,000 per transaction", "MYR: minimum €50, maximum €9,000 per transaction", "VND: minimum €320, maximum €50,000 per transaction", "IDR: minimum €200, maximum €30,000 per transaction"]}, {"method": "Visa", "currencies": ["SGD", "IDR", "MYR", "VND"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €50, maximum €9,000 per transaction", "VND: minimum €320, maximum €50,000 per transaction", "SGD: minimum €18, maximum €3,000 per transaction", "IDR: minimum €200, maximum €30,000 per transaction"]}, {"method": "QRIS", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €10, maximum €50,000 per transaction"]}, {"method": "USDC", "currencies": ["USDC"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €50, maximum €23,840 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "VND: minimum €309, maximum €154,949 per transaction"]}, {"method": "USDT (TRC20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction"], "network": "TRC20"}, {"method": "Bitcoin Cash", "currencies": ["BCH"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["THB: minimum €370, maximum €182,910 per transaction", "MYR: minimum €50, maximum €23,840 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "SGD: minimum €15, maximum €7,560 per transaction"]}, {"method": "Cardano", "currencies": ["ADA"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €196, maximum €98,490 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "MYR: minimum €50, maximum €23,840 per transaction"]}, {"method": "OCBC Bank", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €50, maximum €5,000 per transaction"]}, {"method": "Giropay", "currencies": ["EUR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["EUR: minimum €10, maximum €5,000 per transaction"]}, {"method": "DBS Bank", "currencies": ["SGD"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["SGD: minimum €50, maximum €5,000 per transaction"]}, {"method": "Mandiri", "currencies": ["IDR"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["IDR: minimum €20, maximum €40,000 per transaction"]}, {"method": "USDT (ERC20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["VND: minimum €309, maximum €154,949 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "SGD: minimum €15, maximum €7,560 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "MYR: minimum €50, maximum €23,840 per transaction"], "network": "ERC20"}, {"method": "USDT (BEP20)", "currencies": ["USDT"], "minimum": "€10", "maximum": "€5,000", "fee": "No casino processing fee; payment provider or blockchain network fees may apply", "transaction_speed": "1–2 minutes", "important_terms": ["MYR: minimum €50, maximum €23,840 per transaction", "THB: minimum €370, maximum €182,910 per transaction", "IDR: minimum €196, maximum €98,490 per transaction", "VND: minimum €309, maximum €154,949 per transaction", "SGD: minimum €15, maximum €7,560 per transaction"], "network": "BEP20"}]
- brandinfo_deposit.deposit_guide: ["A cashier visit and a selection of Deposit follow.", "Authorization and confirmation of the transaction proceed according to provider instructions.", "Players fill in the payment information along with the amount.", "Players begin by logging in to their Longfu88 account.", "Next comes a wait for the playable balance to receive the credited funds.", "Which payment method to use is chosen from those available, with a compatible currency or blockchain network."]; keep exactly: longfu88, payment information
- brandinfo_general.minimum_deposit: €10
- brandinfo_general.currencies: ["USDT", "EUR", "SGD", "THB", "USD", "MYR"]
Counting warning: the facts above contain tracked keywords "Longfu88" (x1). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').

---

## BLOCK BRIEF
Block: b13, H3 "Withdrawals, Fees and the Turnover Rule" (under H2 "Payments and Deposit Limits")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 128-162 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 162, but never beyond 178 words.
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
- "Lngfu88 withdrawal time": exactly 1 time(s)
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
- Withdrawal → is completed after → 3 business days at the longest [9]
- Bank Transfer → can extend this by → another 3-5 business days until the funds arrive [7]
Summary: How does a payout work? Supported payout methods, the six steps to follow, the time a payout needs, minimum and maximum amounts, and fees that vary with circumstances.
Copywriter Notes: What happens between pressing withdraw and seeing the money? Name the supported methods (DBS Bank, Online Banking, DANA, MoMo, Touch'n Go, bank transfer, Mastercard, Visa, USDT over three networks, Bitcoin, Ethereum and Litecoin), then the boundaries (at least €20, at most €5,000), followed by the six steps in the form of a NUMBERED list, and the timing. Card, crypto-address and wallet withdrawals reach the player in 1 to 3 business days. Bank transfers are slower: the casino holds the request for up to 3 business days, after which the bank needs 3 to 5 more before the account is credited; the general processing target is three working days. Wherever "Lngfu88 withdrawal time" shows up, write it verbatim with exactly this spelling, in the sentence naming the processing time. Fees of their own may come from payment providers and blockchain networks, yet the casino applies no standard withdrawal fee. A commission of 10% (minimum €2.25) is possible if the player has wagered less than the sum deposited; the reason is that betting the deposit through at least once (1x) can be a prerequisite for cashing out. A rate of 15% can hit specific transactions that came in via card or bank transfer. Skip the per-market minimum lines of individual methods, since they mix € symbols with amounts in local currency. Close by sending readers to the verification section, with a note that identity checks may hold a payout up. Use "Longfu88" exactly once and "Lngfu88 withdrawal time" (verbatim, with this spelling) exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
Brand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your own words, never copy a sentence of this card, and write list items in your own order and phrasing:
- brandinfo_withdrawal.withdrawal_methods: [{"method": "DBS Bank", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["SGD"], "important_terms": ["Thailand: minimum €1,945 (THB market)", "Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Vietnam: minimum €10,000 (VND market)", "Singapore: minimum €80 (SGD market)"]}, {"method": "Visa", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["MYR", "IDR", "VND", "SGD"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Vietnam: minimum €10,000 (VND market)", "Thailand: minimum €1,945 (THB market)", "Singapore: minimum €80 (SGD market)", "Malaysia: minimum €50 (MYR market)"]}, {"method": "Bitcoin", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["BTC"], "important_terms": ["Thailand: minimum €375 (THB market)", "Singapore: minimum €15 (SGD market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Online Banking", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["MYR"], "important_terms": ["Thailand: minimum €1,945 (THB market)", "Malaysia: minimum €50 (MYR market)", "Vietnam: minimum €10,000 (VND market)", "Singapore: minimum €80 (SGD market)", "Indonesia: minimum €25,000 (IDR market)"]}, {"method": "USDT (BEP20)", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "Bank Transfer", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days", "currencies": ["MYR", "VND", "IDR"], "important_terms": ["Thailand: minimum €1,945 (THB market)", "Singapore: minimum €80 (SGD market)", "Indonesia: minimum €25,000 (IDR market)", "Malaysia: minimum €50 (MYR market)", "Vietnam: minimum €10,000 (VND market)"]}, {"method": "USDT (TRC20)", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Thailand: minimum €375 (THB market)", "Singapore: minimum €15 (SGD market)", "Vietnam: minimum €308,000 (VND market)"]}, {"method": "USDT (ERC20)", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["USDT"], "important_terms": ["Singapore: minimum €15 (SGD market)", "Vietnam: minimum €308,000 (VND market)", "Thailand: minimum €375 (THB market)"]}, {"method": "Litecoin", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["LTC"], "important_terms": ["Vietnam: minimum €308,000 (VND market)", "Singapore: minimum €15 (SGD market)", "Thailand: minimum €375 (THB market)"]}, {"method": "Ethereum", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["ETH"], "important_terms": ["Thailand: minimum €375 (THB market)", "Vietnam: minimum €308,000 (VND market)", "Singapore: minimum €15 (SGD market)"]}, {"method": "MoMo", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["VND"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "DANA", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["IDR"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "Touch'n Go", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["MYR"], "important_terms": ["Indonesia: minimum €10,000 (IDR market)", "Malaysia: minimum €100 (MYR market)"]}, {"method": "Mastercard", "minimum": "€20", "maximum": "€5,000", "fee": "Withdrawing carries no standard casino fee. Providers and blockchains may add costs of their own. Inadequate rollover may lead to a 10% fee of at least €2.25, while 15% may be incurred in the case of certain transactions funded by card or by bank.", "transaction_speed": "1–3 business days", "currencies": ["IDR", "SGD", "VND", "MYR"], "important_terms": ["Indonesia: minimum €25,000 (IDR market)", "Vietnam: minimum €10,000 (VND market)", "Singapore: minimum €80 (SGD market)", "Thailand: minimum €1,945 (THB market)", "Malaysia: minimum €50 (MYR market)"]}]; keep exactly: 10, 2.25, 15
- brandinfo_withdrawal.withdrawal_guide: ["Should verification be requested, identity and payment method get verified.", "Players access Longfu88 through login and enter the cashier.", "Go for Withdrawal and settle on a supported destination or, alternatively, a payment method.", "Players go over the request and approve its submission.", "Players wait through the casino's handling and through settlement at the bank or network, if there is any, prior to getting the funds.", "The destination of the funds is given as a bank, wallet or blockchain address, alongside the amount."]; keep exactly: longfu88
- brandinfo_privacy_policy.terms_conditions.withdrawal_terms: ["Bank transfers may be subject to a further period of 3–5 business days before settlement.", "A withdrawal may be preceded by a requirement to turn over the deposit at a minimum of 1x.", "Requests for KYC documents may come from the operator prior to handling payments.", "As a rule, requests to withdraw are handled in three working days or less."]; keep exactly: 1x, 3, 5, kyc documents
- brandinfo_privacy_policy.terms_conditions.conditional_fees: ["If the deposited amount exceeds qualifying turnover, the commission may be 10%, and not less than €2.25.", "A charge of 15% is possible for particular transactions paid for with a card or via bank transfer, as the casino rules provide."]; keep exactly: 10, 2.25, 15, bank transfer
- brandinfo_general.payment_methods.withdrawal: ["MoMo", "USDT (ERC20)", "USDT (TRC20)", "Mastercard", "Bitcoin", "Bank Transfer", "Touch'n Go", "Litecoin", "Visa", "USDT (BEP20)", "DANA", "Ethereum", "Online Banking", "DBS Bank"]
Counting warning: the facts above contain tracked keywords "Longfu88" (x1). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 1, 'Lngfu88 withdrawal time': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').
