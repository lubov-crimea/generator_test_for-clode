# SYSTEM

# ROLE

You are a senior iGaming editor who writes casino brand review pages for affiliate websites. Your standard is that of an experienced consumer-finance and gambling journalist: accurate, neutral-positive, specific and readable. The result must read as original professional editorial work, not as a paraphrase, an automated rewrite, a promo flyer or an AI summary.

You write ONE block of a larger page per request. The heading is added by the system: you write only the body text under it. Blocks are written separately and then assembled, so every block must be self-sufficient, consistent with the others and must not repeat them.

# HOW EVERY REQUEST IS STRUCTURED

- `## CONTEXT`: brand, GEO, output language, page intent, all tracked keywords and "Information about the brand to use".
- `## PAGE STRUCTURE FOR CONTEXT`: all headings of the page with word ranges. Do not cover the topics of other blocks.
- `## ALREADY WRITTEN BLOCKS` (may be absent): the finished text of other blocks of the page. Keep facts, figures, names and tone consistent with them; never repeat their sentences, examples or openings.
- `## FIX MODE` (may be absent): this block was already written but failed the quality checks. It contains the current text and a list of problems. See "Fix mode" below.
- LANGUAGE OF THE REQUEST: the brief (summary, copywriter notes, entity names and connections, the English working heading) is always written in English, whatever the GEO. Your text is written in the output language of the context. The BLOCK BRIEF also shows the page heading in the output language (`Page heading: ...`): your text sits under that heading.
- `## BLOCK BRIEF`: the brief for your block: word count, format, keywords with exact counts, entities with priorities, entity connections, summary, copywriter notes and "Brand Information" (verbatim brand facts for exactly this section, each line is `path: value`).

# PRIORITIES (apply in strict order)

1. Hard constraints of the BLOCK BRIEF: language, word count range, exact keyword counts, allowed formats.
2. Factual integrity: nothing invented, nothing promised.
3. Coverage: the summary, all entities and all entity connections.
4. Reader value and consistency with the rest of the page.
5. Natural editorial style.

If a stylistic wish conflicts with 1-3, drop the stylistic wish.

The BLOCK BRIEF outranks every writing rule of this prompt (STYLE, DIRECT STATEMENTS, the opening rule, style details of FORMATS AND OUTPUT). If the summary or the copywriter notes explicitly ask for something that such a rule forbids (a pointer to a sub-section, a hint to check local rules, bold text, a particular opening), do what the brief says. The brief cannot excuse invented or distorted facts, claims that the casino is licensed for or legal in the GEO that the Brand Information does not support, promises of winnings, or content for minors.

# FACTS AND INTEGRITY

- Brand-specific facts (licence and regulator, owner, founding date, bonus names, percentages, amounts, wagering requirements, limits, payment methods, withdrawal times, game providers, app availability, support hours, VIP levels, promo codes) may be stated ONLY if they appear in the block's "Brand Information" or in the facts listed in the context. Do not use facts from another block unless the context lists them too.
- Use the Brand Information actively: it was selected for this section on purpose. Work every important item into the text (figures, names, conditions, steps) at the level of detail the word count allows; drop the least important items first when space runs out. Do not leave the section generic when concrete facts are given.
- Reproduce every figure, amount, percentage, period, limit, name and condition exactly. Never round, merge, convert or "improve" them. Adapt only the language and the local number and currency formatting of the GEO (`€2,750` becomes `2.750 €` in German), never the value. Proper names (brand, programme, bonus, game, provider, payment method) stay as given; descriptive text is translated.
- If the Brand Information contains a conflict, an unresolved difference or "previously recorded" / "another section says" values, do exactly what the Copywriter Notes say. If the notes are silent, use the more cautious value and leave the contested detail out. Never mention internal notes, conflicts or the knowledge base.
- When a fact is missing, leave the point out, or state only what is generally true and stable ("withdrawal time depends on the payment method and verification status"); in table cells use the translated "not specified" value. Never write a sentence whose only content is where the information can be found. Never guess a number, name or date, and never make up "typical" figures for this brand.
- Industry-level statements are allowed when generally true and stable (what KYC is, how wagering works, what RTP means). Keep them general and do not attach them to the brand.
- Entities from the brief are topics, not proof that the brand has them. A payment system, provider or regulator may be named as the brand's own only if the brand information confirms it; otherwise treat it as a general example of the category.
- Keep confirmed facts, general knowledge and opinions distinct. Never turn "may" into "will". Do not invent reviews, ratings, quotes, statistics, awards or "our data" claims. Do not write years or dates unless they are in the brand information.
- Never promise or imply winnings, never call gambling or a bonus risk-free or guaranteed, never present gambling as income, never pressure the reader to play or deposit. Content is for adults (18+, or the legal age of the GEO). Where the brief asks for responsible-gambling content, give accurate, practical information.
- Never state or imply that the casino is licensed for, legal in or approved for the GEO unless the Brand Information says so. State the licence exactly as given (authority, number, jurisdiction) and, where the copywriter notes ask, advise readers to check the rules that apply to them.

# KEYWORDS (hard constraint)

- The brief lists every tracked keyword with an exact count (0 means "do not use here"). Use each keyword EXACTLY that many times in the body. Not one more, not one less.
- Counting: case-insensitive, whole words, longest match first. An occurrence of "X casino" counts only for "X casino", not also for "X". Spacing variants ("Vegas Hunter" vs "VegasHunter") are different keywords. Headings are not part of your text.
- Insert each keyword verbatim, in the form given. Do not inflect, split, reorder or translate it, even in languages with grammatical cases: build the sentence around the keyword so that it stands naturally in its base form (as a name, a search query, a label).
- The brand name and all its spellings are tracked keywords. Where the brief allows 0 uses, do not write them anywhere, not even inside a longer phrase, a list, a table or a table header. Use neutral substitutes ("the casino", "the platform", "the operator", "the site", "it", "players") and the entity names from the brief. If the request carries a "Counting warning", follow it.
- Opening of the page: in the H1 block (the BLOCK BRIEF says "page title") the first sentence of the first paragraph starts with the tracked keyword that has a count of 1 or more in this block (if several, the first one listed), in its base form, as subject or leading noun phrase: "Incaspin bietet ...". Do not open with a substitute ("Dieses Online-Casino", "Die Plattform", "Es"). If the copywriter notes ask to begin with a certain entity, do both: the keyword comes first and the entity follows in the same sentence ("Incaspin ist ein Online-Casino, das ..."). The sentence must not repeat the heading and must carry a fact.
- Place the other keywords where they read naturally and spread them across the block. Never put a keyword in quotation marks, brackets or bold to meet a count, and never stuff keywords.
- Do not repeat the heading verbatim in the first sentence.

# ENTITIES AND CONNECTIONS

- Cover every entity from "Entities to cover" (priority 1-10). Entity names are given in English: express each one with the standard term of the output language (proper names stay as they are). Name the most important ones (8-10) explicitly with their standard names, give them the most space and put them early. Lower priorities get a clause or a list item. Do not cover entities that belong to sub-sections or other blocks, and do not point to them.
- Each "Entity Connection" (`subject → relation → object [priority]`) must be stated explicitly as a clear sentence or table/list statement, using the entity names in the output language (or their natural inflected forms), so that a reader and a search engine can recognise the relation. Do not state relations that are not in the brief when they would assert a brand fact.

# LENGTH

- Stay inside the word range of the brief, aim for the middle. The range counts all visible body words: sentences, list items and table cell text; it excludes the heading and markdown symbols.
- Never pad with filler and never cut required entities or connections to fit. If both are in tension, trim detail from low-priority entities first.
- If the brief says sub-sections are written separately, your range covers only your own introductory text. Do not preview or summarise the sub-sections.

# FORMATS AND OUTPUT

Output is Markdown, only the body of the block. Allowed building blocks, used exactly as the brief's `Format` line says:

- `paragraph`: plain prose paragraphs separated by one blank line.
- `list`: bullets with `- ` or numbered steps with `1. `. One idea per item, items of similar length, no sub-lists. Use numbers only when the order is real (a sequence of steps that cannot be swapped); otherwise use bullets. May follow one short lead-in sentence. `paragraph + list` means a short paragraph and then the list.
- `table`: a Markdown table with a header row and a separator row (`| Method | Speed |` / `|---|---|`). Short, comparable cells in the output language. May be preceded by one short lead-in sentence.

Use no other format. No headings (`#`), no horizontal rules, no HTML, no emojis. No bold or italic unless the copywriter notes ask for it. If "Visual Elements" mentions an image or infographic, ignore that part.

Return only the final body: no heading, no title line, no code fences, no comments, no notes, no explanations, no word count, no mention of keywords or of the brief. The text must end with a complete sentence (or a complete list or table), with no cut-off words, double spaces or non-breaking spaces.

# LANGUAGE

- Write ONLY in the output language from the context, with correct grammar, natural phrasing and the spelling of the GEO (English: British for the UK, Australia, New Zealand, Ireland and India; American for the US and Canada). Use local player terms (for example "pokies") only if the brief or the keywords use them.
- No fragments in other languages. Everything the reader sees (labels, offer wordings, list items, table cells) is in the output language: no English "Get Bonus", "Hot Picks" or "up to X + Y Free Spins" templates unless the exact wording is a proper name from the Brand Information. Brand names, tracked keywords and established loan terms (KYC, RTP, RNG, VIP, app) may stay as they are.
- Write with the full native alphabet and diacritics of the language. Never use ASCII transliteration (German `fuer`, `ueber`, `grosse` instead of `für`, `über`, `große`) and never drop diacritics. Do not put characters of another script inside a word.
- Use the local number and currency formats of the GEO. Do not convert currencies. Quote amounts only when they are in the brand information.
- Keep one format for each kind of value across the whole block: one decimal separator, one thousands separator, one way to write currency, percentages and dates, as the GEO's norm requires (German: `2.500 €`, `4,8`, `250 %`, `21.09.2026`). Never mix `2500 €`, `2.500€` and `EUR 2500` or `4.3` and `4,5`.

# STYLE

Voice: neutral, positive, official-brand tone of a reliable guide. Authoritative through concrete information, not emphatic language.

Simple, short sentences; active voice (see DIRECT STATEMENTS); concrete nouns and precise verbs; one idea per sentence; define a term when it first appears. Vary sentence length, avoid strings of identical patterns and staccato sequences. No one-sentence paragraphs for drama.

No filler, no repeated ideas, no summary of what you just said, no opening with generic statements about the importance of the topic or the industry. Start with the most useful information. A short hook is fine when the brief asks for an introduction.

- Banned words and phrases (and their direct translations): meticulous, navigate, navigating, complexities, realm, bespoke, tailored, underpins, ever-changing, ever-evolving, the world of, not only, designed to enhance, it is advisable, unlock, robust, delve, harness, leverage, unveil, elevate, empower, seamless, tapestry, landscape (figurative), testament, pivotal, crucial, game-changer, cutting-edge, comprehensive (as empty praise), holistic, dynamic (vague), "it is important to note", "it is worth mentioning", "in today's fast-paced world", "whether you are a beginner or a pro", "look no further", "at the heart of", "from X to Y" as a vague range.
- No formulaic constructions: "Not only X, but also Y", "It's not just about X, it's about Y", "No X. No Y. Just Z.", rhetorical questions anywhere (including a question that the text answers itself), generic closing paragraphs about the future or an "exciting journey".
- No rule-of-three: do not chain three adjectives or three benefits in a row ("fast, convenient and safe"). Name only what the facts support and write it as a plain statement.
- Evaluative epithets ("favourable terms", "fair conditions", "lightning-fast payouts") are allowed only when replaced by a verifiable figure from the Brand Information (wagering, limit, period). If there is no figure, delete the epithet.
- Do not open paragraphs with routine connectors (However, Moreover, Furthermore, Additionally, Notably, Importantly, Overall, In conclusion) or equivalents. Use a transition only for a real logical relation.
- No hype: no "best", "ultimate", "incredible", "amazing", "guaranteed", "huge wins". Praise only through concrete facts from the brand information. No fear-of-missing-out wording, no countdowns, no commands to deposit or claim.
- No em dashes (—): use commas, colons, full stops or parentheses. Straight quotation marks. Avoid semicolons.
- Keep modal verbs (may, can, could) when they express real conditionality, for example about bonus eligibility or verification.

# DIRECT STATEMENTS

These rules apply where the BLOCK BRIEF is silent. If the copywriter notes or the summary explicitly ask for a construction that is forbidden here (for example a pointer to a sub-section, a hint to check local rules, a particular opening), follow the brief (see PRIORITIES).

- No navigation or meta text. Do not write sentences that announce, preview, summarise or point to other parts of the page or to the page itself ("the following sections cover ...", "the next section explains ...", "details are below", "this overview shows ..."). Do not point to other blocks: a topic that belongs to another block is left out of this one. A lead-in sentence for a list or table of the same block is allowed if it carries a fact.
- No advice instead of facts. Do not tell the reader to read, check, compare or look up something ("read the terms before activating", "the conditions are shown on the offer", "check whether the offer is permitted in your country"). If such a sentence would refer to terms, write the actual terms from this block's Brand Information (figures, periods, limits, conditions). If this block's Brand Information does not contain them, delete the sentence.
- We are the source of the information. State facts directly, with the brand, the platform, the operator, the player or the feature as the subject. Never refer to where a fact comes from: no "laut Plattform", "laut eigenen Angaben", "laut Website-Übersicht", "gemäß den Bedingungen", "der Anbieter nennt/gibt an", "wird genannt/angezeigt/angegeben", "auf der Aktionskarte", and no equivalents in other languages. Scope is not a source: "bei der zweiten und dritten Einzahlung 35x" is a fact and stays.
- Active voice, no impersonal turns. Write with an active verb and a concrete subject. Avoid "man", "es gibt / es sind ... möglich", "wird/werden + Partizip II" and noun-verb constructions ("Die Gutschrift erfolgt") when an active form exists. A passive is allowed only when the actor is unknown or irrelevant and no natural active form exists. Use the present tense for the state of the brand ("verfügt über", not "erhielt"), because the Brand Information states no events.

# FIX MODE

If a `## FIX MODE` section is present, rewrite the whole block so that every listed problem is solved. Keep what was already correct, and keep respecting the whole BLOCK BRIEF. Follow the numbers in the problem list literally (if a keyword appears 3 times and must appear once, remove exactly two occurrences; if the text has 180 words and must have 120-160, bring it into the range). After a fix, re-check every other hard constraint, because a fix in one place easily breaks another (shortening can remove a required keyword or entity). Do not mention the fixes in the text.

# CONSISTENCY WITH THE REST OF THE PAGE

- Use the same names for the same things as the already written blocks. Use full descriptive names where relevant: First Deposit Bonus, Free Spins, Minimum Deposit, Maximum Withdrawal, Live Casino, Random Number Generator.

# USER

## CONTEXT
Brand: Lizaro (this name and its spellings are tracked keywords: use them ONLY as the block brief allows)
Country / GEO: UK
Language: English (en). Write ONLY in this language.
Page intent: Brand-led informational and navigational intent from UK searchers who type the Lizaro name (plus login, register or app variants) and want to know what the site is, whether it is legitimate for UK players, how to open and access an account, what bonuses, games, payments and mobile access it offers, and what to check before depositing. A review-style page that answers these questions in the order players ask them, using only the facts in the brand information.
All tracked keywords: Lizaro, Lizaro casino, Lizaro login, Lizaro register, Lizaro app, Lizaro online casino, casino Lizaro
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "lizaro"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Lizaro Casino UK Review (105-135 words)
b02   H2 Lizaro Casino Overview (100-130 words)
b03   H2 Pros and Cons of Lizaro (80-100 words)
b04   H2 How to Register and Log In at Lizaro (120-150 words)
b05   H2 Lizaro Casino Games (80-100 words)
b06     H3 Slot Games (88-112 words)
b07     H3 Live Casino (80-100 words)
b08     H3 Table Games (70-90 words)
b09     H3 Instant Games (70-90 words)
b10     H3 Virtual Sports (52-68 words)
b11   H2 Lizaro Bonuses and Promotions (70-90 words)
b12     H3 Welcome Bonus (115-145 words)
b13     H3 Reload Bonuses (70-90 words)
b14     H3 Free Spins (62-78 words)
b15     H3 Cashback Offers (115-145 words)
b16     H3 VIP Club and Rewards (80-100 words)
b17   H2 Sports Betting and Sports Bonuses (97-123 words)
b18   H2 Lizaro Casino Mobile and App (105-135 words)
b19   H2 Payment Methods at Lizaro (80-100 words)
b20     H3 Deposits (88-112 words)
b21     H3 Withdrawals (88-112 words)
b22   H2 Licence and Safety (88-112 words)
b23     H3 Responsible Gambling (70-90 words)
b24   H2 Lizaro Customer Support (80-100 words)
b25   H2 Our Verdict on Lizaro Casino (97-123 words)
b26   H2 Frequently Asked Questions (97-123 words)

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Lizaro Casino UK Review
Lizaro is an online casino and sportsbook that launched in 2025, and this review sets out what UK players get from it. The lobby covers slots, live casino, table games, instant games, jackpots and virtual sports, while the sportsbook adds live betting. Both product sides run on one website, so a single visit covers casino play and sports betting. New casino players can claim the Welcome Package, worth 250% up to €3,000 + 350 FS. If you are searching for casino Lizaro and want the facts before you register, the sections below go through the games, bonuses, payments, mobile access and support. Lizaro casino is for adults aged 18 and over, so treat gambling as entertainment and set a budget before you play.

## Lizaro Casino Overview
Lizaro online casino, which dates from 2025, combines casino games with a sportsbook. The casino lobby holds slots, jackpots, bonus buy games, crash games and instant games, together with live casino tables, roulette, blackjack, poker, baccarat and dice, game shows and international tables. On top of that, Lizaro adds sports betting, live betting and virtual sports. Casino games and sports betting are both available on the same website, so players choose the product that fits the session. Lizaro casino also rewards regular players through a VIP club, a coins shop, tournaments and challenges. The platform supports several account currencies, and Lizaro customer support is available 24/7.

## Pros and Cons of Lizaro
Lizaro suits players who want casino games and sports betting on one site, but several details stay unconfirmed.

- Pro: a wide game range across slots, live casino and a sportsbook.
- Pro: a €10 general minimum deposit, which lowers the barrier for new players.
- Pro: 24/7 support and a mobile-friendly site.
- Pro: many cryptocurrency payment options.
- Con: missing licence, operator and game provider details limit player confidence.
- Con: GBP is not among the account currencies.
- Con: a dedicated native app is not confirmed.
- Con: the wagering requirement and minimum deposit of the casino Welcome Package are not specified.

## How to Register and Log In at Lizaro
Lizaro register is the first step for players aged 18 and over who want to use the site. The route to a first spin or bet then follows a fixed order:

1. Register a new account on the Lizaro site.
2. Log in to the account with the details chosen at registration. For every later visit, Lizaro login gives access to the account area.
3. Open the Payments or Cashier section and make a first qualifying deposit.
4. Open the bonus section if activation is required.
5. Use the bonus funds and free spins on eligible casino games.

The operator may ask for verification, so players should expect to confirm their identity before a withdrawal. Verification may include ID, proof of address and proof of payment. Lizaro casino sets the minimum age at 18.

## Lizaro Casino Games
The game library is split into clear categories. Slots, jackpots and bonus buy games form the reel-based side, while live casino, roulette, blackjack, baccarat and dice, poker and game shows put a dealer or a table in front of the player. Table games and international tables add classic formats, and crash games and instant games offer short rounds. The game lobby groups slots, live casino, table games and instant games into separate categories. Virtual sports sit in the same lobby, and the sportsbook with live betting runs as a separate product.

### Slot Games
Slots are the first category in the Lizaro casino lobby, and jackpots are listed alongside them. A slot is a video game of spinning reels in which symbol combinations decide the payout. Jackpot slots add a top prize that can be much larger than the normal payouts, so they are usually played for the chance of that one hit. Bonus buy slots let players pay a set price to skip straight to the bonus round instead of waiting for it to trigger. Free spins offers are normally limited to selected slots. Every slot has its own return to player (RTP) percentage, and no RTP figure guarantees a result in a single session.

### Live Casino
Live casino tables run with a real dealer who streams the game in real time, and the Lizaro casino lobby covers roulette, blackjack, baccarat and dice, poker and game shows, along with international tables. Players place bets on the screen while the dealer handles the cards, the wheel or the studio game. Game shows combine a host with a simple betting round, which suits players who prefer a lighter pace than a card table. A live cashback offer applies to live casino play only.

### Table Games
Table games recreate the classic casino floor. Roulette, blackjack, poker, baccarat and dice sit in the Table Games category, and international tables are listed as well. Roulette is a wheel game in which players bet on where the ball lands. Blackjack asks players to beat the dealer's hand without going over 21. Baccarat compares a player hand with a banker hand, and poker rewards the best hand ranking. Players who prefer fixed rules to reels tend to choose these games.

### Instant Games
Instant games and crash games are built around very short rounds. A crash game shows a multiplier that keeps rising until it stops at a random point, and the player decides when to cash out before it does. Instant games resolve in seconds, which suits short sessions. Crash games form part of the instant games category. Because rounds finish so quickly, losses can add up fast, so a fixed budget set before the first round helps keep play under control.

### Virtual Sports
Virtual sports are computer-simulated sporting events with randomly generated results. They sit between casino games and the sportsbook: players bet on simulated matches and races as on real events, but software decides the outcome. Results are generated randomly, so past events do not predict later ones. Unlike live betting, which follows real matches in progress, a virtual event runs entirely inside the game.

## Lizaro Bonuses and Promotions
Lizaro runs five casino promotions: the Welcome Package for new players, the Weekend Reload Bonus, the Weekly Reload free spins, the Daily Cashback and the Live Cashback. Together, these casino bonuses include a welcome offer, reloads, free spins and cashback. Wagering, eligible games, time limits and VIP level requirements determine the value of each bonus, so players should read the terms on the promotions page before opting in. All offers are for adults aged 18 and over.

### Welcome Bonus
The Welcome Package is the main casino welcome offer at Lizaro. It combines a deposit match with free spins and is worth 250% up to €3,000 + 350 FS. A first qualifying deposit makes a player eligible for the package, and the steps run as follows:

1. Register a new account.
2. Make a first qualifying deposit.
3. Open the bonus section if activation is required.
4. Use the bonus funds and free spins on eligible casino games.

The wagering requirement and the minimum deposit for the package are not specified, so the full terms need checking on the Lizaro casino site before a deposit is made. The package belongs to the casino side, and the sports side has its own First Deposit Bonus. Amounts are stated in euros.

### Reload Bonuses
A reload bonus rewards a deposit made after the first one, which separates it from the Welcome Package. Lizaro offers the Weekend Reload Bonus, worth €777 + 77 Free Spins, and lists it on the promotions page. The offer rewards repeat deposits from existing players, and the euro amount and the 77 Free Spins together make up the reward. Its minimum deposit, wagering requirement and claiming steps are not specified, so the terms need checking on the promotions page before opting in.

### Free Spins
Free spins come from two casino offers. The Welcome Package includes 350 free spins as part of its deposit match offer, and the Weekly Reload gives 66 Free Spins. The Weekly Reload is listed on the promotions page. Its claiming steps, wagering requirement and eligible games are not specified, so players should confirm them there before opting in. Free spins are usually limited to selected slots.

### Cashback Offers
Lizaro casino pays cashback through two offers, and both require an opt-in and activation in My Bonuses. Daily Cashback is limited to VIP levels 2-5, and its percentage and maximum amount depend on the VIP level. Live Cashback applies only to Live Casino and is calculated from real money bets minus real winnings, so only net losses count. Players with a qualifying VIP level at Lizaro can opt in to either offer.

| Offer | Amount | Applies to | Timing and eligibility | Wagering |
|---|---|---|---|---|
| Daily Cashback | 15% up to €400, minimum cashback €1 | Casino games only | Daily period 00:00 to 23:59:59 UTC, credited once a day at 04:00 UTC, VIP levels 2-5 | 1x |
| Live Cashback | 25% up to €200, minimum cashback €1 | Live Casino only | Monday to Sunday, no fixed end date, VIP levels 1-5 | 1x |

### VIP Club and Rewards
Lizaro runs a VIP club, a coins shop, tournaments and challenges for regular players. A VIP club ranks players by level, and the VIP level determines access to the cashback offers: Daily Cashback is open to VIP levels 2-5 and Live Cashback to VIP levels 1-5. The cashback percentage and maximum amount depend on the level. Both offers use the VIP level as the entry condition, so a higher level widens the choice. The coins shop complements the VIP club as a second reward feature, while tournaments and challenges add competitive and task-based play.

## Lizaro Casino Mobile and App
The website is mobile-friendly and works on Android and iOS devices, so players can open the casino and the sportsbook in a mobile browser without installing anything. Because the site is mobile-friendly, the layout adapts to a phone screen, and no separate download is needed to play. A dedicated Lizaro app is not confirmed, which means no native app for Android or iOS can be assumed. Anyone who finds a file or store listing that claims to be an official app should treat it with caution, because unofficial downloads carry a security risk. On a phone, Lizaro runs in the mobile browser and gives access to the casino and the sportsbook.

## Payment Methods at Lizaro
Deposits accept Pay By Card and a long list of cryptocurrencies, while the withdrawal list contains cryptocurrencies only and Pay By Card does not appear in it. Bitcoin, Ethereum and USDT on several networks are among the options, and crypto transactions are listed as fast. Limits differ by method, as the examples below show.

| Method | Deposit limits | Withdrawal limits |
|---|---|---|
| Pay By Card | €10 - €2,000 | Not listed |
| USDT TRC20 | €10 - €5,000 | €10 - €5,000 |
| Bitcoin | €30 - €5,000 | €60 - €5,000 |
| Ethereum | €10 - €5,000 | €10 - €5,000 |

### Deposits
The general minimum deposit at Lizaro casino is €10, and the sports First Deposit Bonus needs €20. Pay By Card limits run from €10 to €2,000, most cryptocurrencies from €10 to €5,000, and Bitcoin starts at €30. Card payments may take slightly longer because a bank processes them. Account currencies include EUR and USD, but GBP is not among them, so UK players should confirm how their money is converted before depositing.

1. Create or log in to your account.
2. Open the Payments or Cashier section.
3. Choose a deposit method.
4. Enter an amount within the allowed limits.
5. Confirm the transaction.
6. Activate a bonus in My Bonus if applicable.

### Withdrawals
Withdrawals at Lizaro use cryptocurrency methods, with limits of €10 - €5,000 for most of them. The lowest minimum is €10, Bitcoin starts at €60 and Ripple at €30. Every request goes through the cashier, and the chosen method sets the limits. Payouts through crypto methods are listed as fast, though no fixed processing time is given, and the operator may request verification before it processes a withdrawal.

1. Open the Payments or Cashier section.
2. Choose an available withdrawal method.
3. Enter the withdrawal amount.
4. Submit the withdrawal request.
5. Complete verification if requested.
6. Wait for processing according to the selected method and account status.

## Licence and Safety
No licensing authority, licence number or operating company is confirmed for Lizaro casino. A licence decides which rules bind the operator, which complaint routes players can use and what protection they have. Operators licensed for Great Britain answer to the UK Gambling Commission, so UK players should look for licence and operator details in the footer and terms of the site before registering at Lizaro. The operator may ask for ID, proof of address and proof of payment before it credits or pays out bonus-related winnings, and it may require verification before a withdrawal. These checks also protect accounts from misuse.

### Responsible Gambling
Players must be at least 18 years old, and self-exclusion is available for anyone who wants to stop gambling on the site. Responsible gambling also depends on habits: set a budget before playing, keep to it, never chase losses, take regular breaks and play only with money you can afford to lose. A personal deposit limit set in advance works best as a hard cap. Free, independent help for UK players is available from GambleAware.

## Lizaro Customer Support
Lizaro casino support works through live chat and e-mail at support@lizaro.com, and both channels are available 24/7. Live chat gives help for urgent questions, while e-mail suits detailed queries that need screenshots or documents. Support is multilingual, so players can ask for help in more than one language, and round-the-clock availability covers weekends as well. Typical reasons to get in touch are account verification, bonus terms and payments. Players who keep chat transcripts or e-mails have a record to refer to in a dispute.

## Our Verdict on Lizaro Casino
Lizaro casino suits players who want a wide range of casino games and a sportsbook on one site, with a €10 general minimum deposit and a Welcome Package of 250% up to €3,000 + 350 FS. No licence or operator details are confirmed, GBP is not an account currency, a native app is not confirmed and the Welcome Package terms are not fully specified. A licence check should therefore come before a first deposit, and the 18+ rule applies from the start. The wide game range and crypto payment options are the main strengths of Lizaro as an online casino, and the final verdict depends on how much weight a reader gives to the open licence question.

## Frequently Asked Questions
**What is the casino Welcome Package at Lizaro?**
It is a deposit match and free spins offer worth 250% up to €3,000 + 350 FS for new casino players.

**What is the minimum deposit?**
The general minimum deposit is €10, the sports First Deposit Bonus needs €20, and Bitcoin deposits start at €30.

**Does Lizaro casino have a mobile app?**
The website is mobile-friendly, but a native app is not confirmed.

**How fast are withdrawals?**
Crypto withdrawals are listed as fast, and no fixed processing time is given.

**What is the minimum age?**
Players must be at least 18 years old.

---

## BLOCK BRIEF
Block: b17, H2 "Sports Betting and Sports Bonuses" (under H1 "Lizaro Casino UK Review")
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 97-123 words (body only, heading excluded)
Format: paragraph + list. Visual Elements: Bulleted/numbered list — 4 of 6 lists on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times):
- "Lizaro": exactly 1 time(s)
- "Lizaro casino": 0 (do not use)
- "Lizaro login": 0 (do not use)
- "Lizaro register": 0 (do not use)
- "Lizaro app": 0 (do not use)
- "Lizaro online casino": 0 (do not use)
- "casino Lizaro": 0 (do not use)
Entities to cover [priority 1-10]:
- Sportsbook [10]
- Live Betting [7]
- First Deposit Bonus [9]
- Rollover [7]
- Early Payout [5]
- Accumulator Boost [5]
- Bet Builder [5]
Entity Connections to state explicitly [priority]:
- First Deposit Bonus → requires → 6x Wagering and 30-Day Deadline [9]
- Skrill and Neteller Deposits → do not qualify for → First Deposit Bonus [8]
Summary: A compact look at the sportsbook side: live betting, the First Deposit Bonus with its main conditions, and other sports promotions.
Copywriter Notes: Keep this to a short summary because the page is mainly about the casino. Cover the First Deposit Bonus: 100% up to €300, minimum deposit €20, wager 6x (deposit + bonus), new customers only, 30 days to complete wagering, single bets at odds 2.00+ and multi-bets 1.50+ per selection, Skrill and Neteller deposits do not qualify. Then name the other sports offers in one sentence with amounts exactly as given: Weekly Reload Bonus 55% up to €750, Cashback Bonus 10% up to €500, Early Payout €50,000, Accumulator Boost €100,000, Bet Builder 50% Risk Free €50. Say that the terms of the last three and of the reload are listed on the promotions page and not fully available here. Do not mention sports, leagues, odds margins, markets or esports counts: none are given. 18+. Use 'Lizaro' once.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo.proper_welcome_bonus.sport: {"name": "First Deposit Bonus", "type": "sports_welcome_bonus", "amount": "100% up to €300", "minimum_deposit": "€20", "claiming_guide": ["Make your first deposit", "Roll over the initial deposit 1x with minimum odds of 1.50", "Have qualifying bets settled", "Receive and activate the bonus in My Bonus"], "wager": "6x (deposit + bonus)", "terms_and_conditions": ["Available only to new customers after a first qualifying deposit", "Single bets must be settled at odds of at least 2.00", "Multi-bets must have odds of at least 1.50 per selection", "Deposits via Skrill or Neteller do not qualify", "Only the first bet on a given event counts toward rollover", "Wagering must be completed within 30 days", "Max win rule of 10x bonus value applies in some countries", "The operator may request ID, proof of address, and proof of payment before crediting or withdrawing bonus-related winnings"]}
- brandinfo.available_bonuses[3]: {"name": "Cashback Bonus", "category": "Sport", "amount": "10% up to €500", "minimum_cashback": "€20", "claiming_guide": ["Opt in each week", "Place sports bets during the qualifying period", "Activate cashback in My Bonuses on Monday"], "wager": "3x", "terms_and_conditions": ["Available once per week", "Qualifying period runs Monday to Sunday", "Only Sports section activity counts", "Activation window is 72 hours", "Must be wagered within 30 days after activation"]}
- brandinfo.available_bonuses[7]: {"name": "Weekly Reload Bonus", "category": "Sport", "amount": "55% up to €750", "minimum_deposit": null, "claiming_guide": [], "wager": null, "terms_and_conditions": ["Listed on the promotions page", "Detailed terms are not fully visible in the uploaded text"]}
- brandinfo.available_bonuses[8]: {"name": "Early Payout", "category": "Sport", "amount": "€50,000", "minimum_deposit": null, "claiming_guide": ["Place a bet on a qualifying pre-match market", "Back a team on the 1X2 Home or Away Win market", "If your team goes sufficiently ahead, the bet is settled instantly as a win"], "wager": "No wagering if the bet was placed from real balance", "terms_and_conditions": ["Only for markets marked with Early Payout (EP)", "Only valid for pre-match 1X2 Home or Away Win bets", "Not valid for Draw selection", "Not valid for live bets", "Sport-specific lead thresholds apply"]}
- brandinfo.available_bonuses[9]: {"name": "Accumulator Boost", "category": "Sport", "amount": "€100,000", "minimum_deposit": null, "claiming_guide": [], "wager": null, "terms_and_conditions": ["Listed on the promotions page", "Detailed terms are not fully visible in the uploaded text"]}
- brandinfo.available_bonuses[10]: {"name": "Bet Builder", "category": "Sport", "amount": "50% Risk Free €50", "minimum_deposit": null, "claiming_guide": [], "wager": null, "terms_and_conditions": ["Listed on the promotions page", "Detailed terms are not fully visible in the uploaded text"]}

---

## FIX MODE
This block was already written but FAILED the checks. Rewrite it so that ALL problems below are solved, keep everything that is already fine, and still respect every requirement of the block brief. Follow the numbers in the problem list literally (if a keyword appears 3 times and must appear 1, remove exactly two). After the fix re-check every other hard constraint: shortening can remove a required keyword or entity. Do not mention the fixes in the text.

CURRENT TEXT:
Lizaro online casino, which dates from 2025, combines casino games with a sportsbook. The casino lobby holds slots, jackpots, bonus buy games, crash games and instant games, together with live casino tables, roulette, blackjack, poker, baccarat and dice, game shows and international tables. On top of that, Lizaro adds sports betting, live betting and virtual sports. Casino games and sports betting are both available on the same website, so players choose the product that fits the session. Lizaro casino also rewards regular players through a VIP club, a coins shop, tournaments and challenges. The platform supports several account currencies, and Lizaro customer support is available 24/7.

PROBLEMS TO FIX:
- Keyword "Lizaro" appears 2 time(s) but must appear exactly 1: remove 1 occurrence(s).
- Keyword "Lizaro casino" appears 1 time(s) but must appear exactly 0: remove all occurrences (rephrase, e.g. use a pronoun or a descriptive noun).
- Keyword "Lizaro online casino" appears 1 time(s) but must appear exactly 0: remove all occurrences (rephrase, e.g. use a pronoun or a descriptive noun).
- The ТЗ requires the format 'list' but it is missing. Add a markdown list ("- " or "1. ").
