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
Country / GEO: Thailand
Language: Thai (th). Write ONLY in this language.
Page intent: Long reference page about the Longfu88 online casino for players from Thailand: what the casino offers, the fact table, licence and data protection, registration and verification, the welcome bonus with a terms table, reloads, cashback, rewards, the VIP programme, the game library by category, providers, the sportsbook with a bonus table, deposit methods, withdrawals, mobile access, responsible gambling, support, pros and cons, a six-answer FAQ and a verdict. Page voice: formal and exhaustive, sentences of about 21 words, paragraphs of three to four sentences, tables wherever two or more attributes belong to an item, comparative statements that put offers side by side, every table introduced by one sentence and followed by one sentence on what it means; one call to action at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Thailand.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 คู่มือฉบับสมบูรณ์เกี่ยวกับ Longfu88 casino สำหรับผู้เล่นชาวไทย (112-144 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Thailand.
b02   H2 ข้อมูลโดยสรุปของคาสิโน (91-117 words): What the casino is for a player from Thailand: launch year, account currencies, the official website and who may play.
b03   H2 ตารางข้อมูลคาสิโน (109-139 words): A fact sheet of the casino: licence, operator, launch year, currencies, languages, payment methods, welcome bonus, cashback, minimum deposit, Minimum age, Sports, Game providers, VIP tiers, support.
b04   H2 ใบอนุญาต ผู้ให้บริการ และความเป็นส่วนตัว (158-202 words): Who licenses and runs the casino (jurisdiction, operator, registration number) and how personal data and accounts are protected.
b05   H2 ขั้นตอนการสมัครสมาชิกและการเข้าสู่ระบบ (123-157 words): How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.
b06     H3 การตรวจสอบเอกสาร KYC (112-144 words): When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.
b07   H2 รายละเอียดโบนัสต้อนรับ (151-191 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b08     H3 เงื่อนไขโบนัสต้อนรับในรูปแบบตาราง (112-144 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b09   H2 โปรแกรม VIP ระดับขั้นและวงเงิน (119-151 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b10   H2 โบนัสเติมเงิน โปรพิเศษ และแคมเปญตามเทศกาล (132-167 words): The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
b11     H3 อัตราแคชแบ็กและเรียเบต (86-109 words): Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
b12     H3 ฟีเจอร์ของรางวัล (80-100 words): The gamification features of the rewards area: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop.
b13   H2 ภาพรวมคลังเกม (91-117 words): The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.
b14     H3 เกมสล็อตและจำนวนเกม (104-133 words): Three example slots with their provider, RTP, volatility and maximum multiplier.
b15     H3 ส่วนของไลฟ์คาสิโน (99-125 words): The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.
b16     H3 หมวดหมู่เกมอื่น ๆ (86-109 words): The remaining game categories in one block: table games, fishing, P2P, fast games, lottery and crash and instant games.
b17   H2 ผู้พัฒนาเกมในล็อบบี้ (55-69 words): Which studios supply the games, named from the provider list.
b18   H2 ช่องทางฝากเงินและตารางวงเงิน (141-179 words): Deposit methods grouped by type with the general limits and speed, the local options for Thailand and the six-step deposit route.
b19     H3 การถอนเงิน ขั้นตอน ระยะเวลา และค่าธรรมเนียม (132-167 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b20   H2 ภาพรวมการเดิมพันกีฬา (112-144 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b21     H3 โบนัสและบูสต์สำหรับกีฬา (86-109 words): The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
b22   H2 การเล่นผ่านมือถือ (106-134 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b23   H2 ช่องทางการติดต่อฝ่ายสนับสนุน (80-100 words): Support channels, availability and languages.
b24   H2 เครื่องมือเล่นอย่างมีความรับผิดชอบ (112-144 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b25   H2 ข้อดีและข้อจำกัดเปรียบเทียบ (55-69 words): A pros and cons table built only from facts stated elsewhere on the page.
b26   H2 คำตอบสำหรับคำถามที่พบบ่อย (229-293 words): Short answers on wagering, withdrawal time, weekly cashback, VIP levels, password recovery, claiming the bonus.
b27   H2 บทสรุปส่งท้าย (104-133 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# คู่มือฉบับสมบูรณ์เกี่ยวกับ Longfu88 casino สำหรับผู้เล่นชาวไทย
Longfu88 เป็นคาสิโนออนไลน์ที่เปิดให้บริการในปี 2026 โดยรวมเกมสล็อต ไลฟ์ดีลเลอร์ เกมโต๊ะ แจ็กพอต เกมยิงปลา เกม P2P เกมเร็ว ลอตเตอรี่ และเกม Crash & instant ไว้ในเว็บไซต์เดียว ควบคู่กับสปอร์ตบุ๊กสำหรับเดิมพันกีฬา คาสิโนออนไลน์แห่งนี้จึงรวมเกมคาสิโน ไลฟ์ดีลเลอร์ การเดิมพันกีฬา และลอตเตอรี่ไว้ภายใต้บัญชีผู้ใช้เดียว

บทความนี้เขียนขึ้นสำหรับผู้เล่นชาวไทยที่ต้องการภาพรวมก่อนตัดสินใจสมัครสมาชิก ผู้เล่นต้องมีอายุอย่างน้อย 18 ปีจึงจะใช้บริการได้ เนื้อหาไล่เรียงตั้งแต่ข้อมูลพื้นฐาน ใบอนุญาต โบนัส คลังเกม ช่องทางฝากถอนเงิน การเล่นผ่านมือถือ ไปจนถึงแนวทางเล่นอย่างมีความรับผิดชอบ การเล่นพนันมีความเสี่ยง และผลลัพธ์ของแต่ละรอบไม่สามารถคาดการณ์ได้

## ข้อมูลโดยสรุปของคาสิโน
=== b02 ===
Longfu88 เปิดให้บริการในปี 2026 และรองรับบัญชีผู้เล่นในหลายสกุลเงิน ได้แก่ EUR, USD, MYR, THB, SGD และ USDT ผู้เล่นจากประเทศไทยจึงพบสกุลเงินบาท (THB) อยู่ในรายการเดียวกับสกุลเงินอื่น ในการเข้าใช้งาน ควรพิมพ์ที่อยู่ของ Longfu 88 Official Site ด้วยตนเองหรือบันทึกไว้ในรายการโปรด และไม่ควรเข้าผ่านหน้าเว็บที่ใช้ชื่อคล้ายกัน

ผู้ที่ประสงค์จะเล่นต้องมีอายุ 18 ปีขึ้นไป และต้องได้รับอนุญาตให้เล่นการพนันตามกฎหมายในที่อยู่อาศัยของตน ผู้เล่นต้องลงทะเบียนด้วยข้อมูลที่ถูกต้อง ถือบัญชีส่วนบุคคลเพียงบัญชีเดียว และไม่ใช้วิธีชำระเงินของบุคคลที่สาม

## ตารางข้อมูลคาสิโน
=== b03 ===
| รายการ | ข้อมูล |
|---|---|
| ใบอนุญาต | คอสตาริกา, Lumina, เลขทะเบียน 000-039123-R-319326-001 |
| ผู้ให้บริการ | Lumina |
| ปีที่เปิดให้บริการ | 2026 |
| สกุลเงิน | EUR, USD, MYR, THB, SGD, USDT |
| ภาษา | อังกฤษ, มาเลย์, จีนตัวย่อ, ไทย, อินโดนีเซีย, เวียดนาม |
| วิธีชำระเงิน | บัตร Visa, Mastercard, โอนผ่านธนาคาร, Bitcoin, USDT, PromptPay QR |
| โบนัสต้อนรับ | 188% สูงสุด €2,088 + ฟรีสปิน 18 ครั้ง |
| แคชแบ็ก | สูงสุด 10% ของยอดเสียสุทธิรายสัปดาห์ |
| ฝากขั้นต่ำ | €10 |
| อายุขั้นต่ำ | 18 ปี |
| กีฬา | ฟุตบอล, บาสเกตบอล, เทนนิส, แบดมินตัน, คริกเก็ต, อีสปอร์ต |
| ผู้พัฒนาเกม | สตูดิโออย่าง Evolution, Pragmatic Play และ Hacksaw Gaming |
| ระดับ VIP | Bronze, Silver, Gold, Platinum, Diamond |
| ฝ่ายสนับสนุน | support@longfu88.com, แชทสด 24/7 |

## ใบอนุญาต ผู้ให้บริการ และความเป็นส่วนตัว
=== b04 ===
ใบอนุญาตของ casino Longfu88 ออกให้ในเขตอำนาจของคอสตาริกา โดยมี Lumina เป็นผู้ถือใบอนุญาตและผู้ให้บริการ เลขทะเบียนคือ 000-039123-R-319326-001 ข้อมูลนี้เป็นข้อมูลด้านใบอนุญาตเพียงรายการเดียวของเว็บไซต์ ผู้เล่นจึงควรตรวจสอบกฎหมายในพื้นที่ของตนเองก่อนตัดสินใจเล่น

Lumina ทำหน้าที่เป็นผู้ควบคุมข้อมูลส่วนบุคคลด้วย และผู้เล่นติดต่อเจ้าหน้าที่คุ้มครองข้อมูลได้ที่อีเมล dpo@longfu88.com ผู้ให้บริการใช้มาตรการทางเทคนิคและมาตรการด้านการจัดการเพื่อปกป้องบัญชี การชำระเงิน และข้อมูลส่วนบุคคล ข้อมูลอาจถูกส่งต่อให้ผู้ให้บริการชำระเงิน ผู้ให้บริการยืนยันตัวตน ผู้ให้บริการด้านเทคโนโลยี รวมถึงหน่วยงานกำกับดูแลและเจ้าหน้าที่บังคับใช้กฎหมายเมื่อมีข้อกำหนดให้ต้องเปิดเผย

ผู้เล่นมีสิทธิขอเข้าถึงข้อมูล แก้ไขข้อมูลให้ถูกต้อง ขอให้ลบข้อมูลเมื่อกฎหมายอนุญาต จำกัดการประมวลผล คัดค้านการประมวลผล โอนย้ายข้อมูลตามที่เกี่ยวข้อง และถอนความยินยอม ส่วนความปลอดภัยของบัญชี ผู้ถือบัญชีมีหน้าที่เก็บรักษาข้อมูลเข้าสู่ระบบด้วยตนเอง และผู้ให้บริการอาจระงับการใช้งานชั่วคราวเพื่อตรวจสอบหรือเมื่อสงสัยว่ามีการใช้งานผิดปกติ

## ขั้นตอนการสมัครสมาชิกและการเข้าสู่ระบบ
การสมัครสมาชิกทำผ่านอีเมล และผู้เล่นต้องเตรียมอีเมล รหัสผ่าน ชื่อตามกฎหมาย วันเกิด และที่อยู่ตามภูมิลำเนาให้พร้อมก่อนเริ่ม โดยผู้เล่นหนึ่งคนถือบัญชีส่วนบุคคลได้เพียงบัญชีเดียว ขั้นตอนมีห้าข้อตามลำดับดังนี้

1. เปิด Longfu88 แล้วเลือกสมัครสมาชิก
2. กรอกอีเมลและสร้างรหัสผ่าน
3. ยืนยันอายุ และยอมรับข้อกำหนดและเงื่อนไขพร้อมนโยบายความเป็นส่วนตัว
4. กรอกข้อมูลส่วนบุคคลเพิ่มเติมและที่อยู่ตามภูมิลำเนา
5. เลือกสร้างบัญชี และยืนยันอีเมลหากระบบร้องขอ

หลังสมัครแล้ว ขั้นตอน Longfu88 login ใช้อีเมลและรหัสผ่านที่ลงทะเบียนไว้ โดยเลือกเข้าสู่ระบบบนเว็บไซต์ แล้วผ่านการตรวจสอบความปลอดภัยหากระบบกำหนด ผู้เล่นที่ค้นหาหน้าเข้าสู่ระบบด้วยคำว่า Longfu caino login ควรตรวจให้แน่ใจว่าเข้าสู่เว็บไซต์ทางการ หากลืมรหัสผ่าน ให้เลือก Forgot Password ที่หน้าเข้าสู่ระบบ ขอลิงก์รีเซ็ตผ่านอีเมล แล้วตั้งรหัสผ่านใหม่ตามคำแนะนำ

### การตรวจสอบเอกสาร KYC
ระบบอาจขอให้ยืนยันตัวตนเมื่อมีการตรวจสอบบัญชี ก่อนการถอนเงิน เมื่อมีธุรกรรมผิดปกติหรือมีมูลค่าสูง และเมื่อมีการเปลี่ยนแปลงข้อมูลบัญชีหรือข้อมูลการชำระเงิน เอกสารที่ใช้มีดังนี้

- เอกสารยืนยันตัวตน: หนังสือเดินทาง บัตรประจำตัวประชาชน หรือใบขับขี่
- หลักฐานที่อยู่: ใบแจ้งค่าสาธารณูปโภคหรือใบแจ้งยอดธนาคาร
- หลักฐานความเป็นเจ้าของวิธีชำระเงิน ทั้งบัญชีธนาคาร บัตร และกระเป๋าเงินดิจิทัล
- เอกสารแสดงแหล่งที่มาของเงินทุน เช่น หลักฐานรายได้ เมื่อมีการร้องขอ

ผู้เล่นมีเวลาส่งเอกสารได้สูงสุด 30 วันนับจากที่ถูกร้องขอ และเมื่อได้รับเอกสารครบชุดแล้ว การตรวจสอบใช้เวลาไม่เกิน 10 วัน ในระหว่างนี้คำขอถอนเงินอาจถูกพักไว้จนกว่าการตรวจสอบจะเสร็จสิ้น หากการตรวจสอบไม่ผ่าน ธุรกรรมอาจถูกปฏิเสธ บัญชีอาจถูกจำกัดการใช้งาน และการถอนเงินอาจถูกระงับไว้

## รายละเอียดโบนัสต้อนรับ
Casino Welcome Bonus เป็นโบนัสเงินฝากครั้งแรกของฝั่งคาสิโน สำหรับผู้เล่นใหม่ที่ลงทะเบียนกับ Longfu88 และฝากเงินครั้งแรกตามเงื่อนไข โดยหนึ่งบัญชีรับข้อเสนอต้อนรับได้เพียงหนึ่งครั้ง Longfu88 bonus นี้ให้โบนัส 188% สูงสุด €2,088 พร้อมฟรีสปิน 18 ครั้ง ซึ่งเป็นการหมุนสล็อตโดยคาสิโนจ่ายค่าเดิมพันให้ ยอดฝากขั้นต่ำของโบนัสนี้คือ €50 ลงทะเบียนและรับ Casino Welcome Bonus ด้วยการฝากเงินครั้งแรก

นอกจากนี้ยังมีข้อเสนอฝากครั้งแรกอีกสองรายการ ได้แก่ Live Casino Welcome Bonus 125% สูงสุด €888 ฝากขั้นต่ำ €30 และ Casino Crypto Welcome Bonus 188% สูงสุด 2,888 USDT ฝากขั้นต่ำ 50 USDT โดย Casino Welcome Bonus กับ Crypto Welcome Bonus เป็นข้อเสนอทางเลือกสำหรับการฝากครั้งแรก เส้นทางการรับโบนัสคือการเปิดใช้งานใน My Bonuses หลังฝากเงินครั้งแรก และในขั้นตอนที่ระบุไว้ไม่มีขั้นตอนกรอก Longfu88 promo code ขั้นตอนมีสี่ข้อดังนี้

- ลงทะเบียนและกรอกข้อมูลส่วนบุคคลที่จำเป็นให้ครบ
- ฝากเงินครั้งแรกตามเงื่อนไข
- เปิดใช้งาน Casino Welcome Bonus ในหน้า My Bonuses ก่อนวางเดิมพันใด ๆ
- เล่นเกมคาสิโนที่ร่วมรายการและทำยอดหมุนเวียนให้ครบก่อนโบนัสหมดอายุ

### เงื่อนไขโบนัสต้อนรับในรูปแบบตาราง
เงื่อนไขของ Casino Welcome Bonus กำหนดยอดหมุนเวียน เพดานเดิมพัน และอายุโบนัสไว้ชัดเจน ดังตารางต่อไปนี้

| เงื่อนไข | รายละเอียด |
|---|---|
| ยอดหมุนเวียนโบนัส | 25 เท่าของเงินฝากรวมโบนัส |
| ยอดหมุนเวียนฟรีสปิน | 40 เท่าของเงินที่ชนะจากฟรีสปิน |
| อายุโบนัส | 10 วันนับจากเปิดใช้งาน |
| เดิมพันสูงสุด | €22.5 ต่อสปิน |
| ถอนสูงสุดจากโบนัส | 5 เท่าของเงินโบนัสเริ่มต้น |

เงินฝากผ่าน Neteller และ Skrill ไม่ร่วมรายการนี้ และเปิดใช้งานโบนัสโปรโมชั่นได้ครั้งละหนึ่งรายการ การขอถอนเงินก่อนรับโบนัสหรือขณะโบนัสยังใช้งานอยู่อาจทำให้สิทธิ์โปรโมชั่นเป็นโมฆะ ส่วนการยกเลิกโปรโมชั่นจะทำให้เงินโบนัสและเงินที่ชนะซึ่งยังไม่ได้แปลงสภาพถูกริบ และอาจต้องยืนยันบัญชีก่อนจ่ายเงินที่ชนะจากโปรโมชั่น

## โปรแกรม VIP ระดับขั้นและวงเงิน
=== b09 ===
Longfu88 VIP Program ให้ผู้เล่นสะสมแต้ม VIP จากการเล่นด้วยเงินจริงที่เข้าเกณฑ์ และแต้มเหล่านี้ปลดล็อกระดับรางวัลที่มีหมายเลขกำกับรวม 25 ระดับ ซึ่งจัดอยู่ในห้าชั้น ได้แก่ Bronze, Silver, Gold, Platinum และ Diamond ตารางด้านล่างแสดงระดับ 1, 5, 10, 15, 20 และ 25 เพื่อให้เห็นว่าแต่ละขั้นต่างกันอย่างไร

| ระดับ | แต้มที่ต้องใช้ | รางวัล | แคชแบ็ก | วงเงินถอน |
|---|---|---|---|---|
| 1 | 1 | €9.8 | 1% | €9,800 |
| 5 | 70 | €24.5 | 2% | €34,300 |
| 10 | 700 | €147 | 4% | €63,700 |
| 15 | 2,100 | €392 | 6% | €88,200 |
| 20 | 3,600 | €637 | 8% | €117,600 |
| 25 | 5,500 | €980 | 10% | €147,000 |

ยิ่งระดับสูงขึ้น แคชแบ็กและวงเงินถอนก็เพิ่มตาม โดยระดับที่สูงขึ้นยังมีข้อเสนอเฉพาะบุคคล และผู้จัดการ VIP ส่วนตัวตั้งแต่ระดับ 4 เป็นต้นไป รางวัลและวงเงินถอนอาจต่างกันตามระดับ VIP และสกุลเงิน และเงื่อนไขอาจเปลี่ยนแปลงตามกฎของโปรแกรม

---

## SECTION
Write the blocks b10, b11, b12 in ONE answer, in this order. They are one continuous section of the page: the sub-sections continue the parent, so the text must flow from block to block without repeating itself. Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts.

---

## BLOCK BRIEF
Block: b10, H2 "Reloads, Specials and Seasonal Campaigns" (under H1 "คู่มือฉบับสมบูรณ์เกี่ยวกับ Longfu88 casino สำหรับผู้เล่นชาวไทย")
Page heading (output language): "โบนัสเติมเงิน โปรพิเศษ และแคมเปญตามเทศกาล"
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): b11 H3 "อัตราแคชแบ็กและเรียเบต"; b12 H3 "ฟีเจอร์ของรางวัล"
Word Count: 132-167 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 167, but never beyond 200 words.
Format: paragraph + table. Visual Elements: Table — 4 of 8 tables on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
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
Copywriter Notes: One lead-in sentence, then a Markdown table Offer | Reward | Min. deposit | Wagering | Validity for the seven offers as given: Casino Weekly Reload, Casino Weekly Crypto Reload, Casino Weekend Reload, Casino Weekend Crypto Reload, Casino Double Fortune (one-day reload special), Casino Trick or Treat Pumpkin Bonanza, Casino Dragon Quest (verification reward). After the table state the shared rules once: activation in My Bonuses, one claim per promotional period, no combination with another active casino bonus, maximum stake €5 per spin while wagering bonus funds. Use "Longfu88" exactly once, and no other tracked keyword. Keep the tracked keywords out of list items and table cells unless a Brand Information value printed there contains them.
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
Block: b11, H3 "Cashback and Rebate Rates" (under H2 "โบนัสเติมเงิน โปรพิเศษ และแคมเปญตามเทศกาล")
Page heading (output language): "อัตราแคชแบ็กและเรียเบต"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 86-109 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 109, but never beyond 130 words.
Format: paragraph + table. Visual Elements: Table — 5 of 8 tables on the page
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

---

## BLOCK BRIEF
Block: b12, H3 "Rewards Features" (under H2 "โบนัสเติมเงิน โปรพิเศษ และแคมเปญตามเทศกาล")
Page heading (output language): "ฟีเจอร์ของรางวัล"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 80-100 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 100, but never beyond 120 words.
Format: paragraph. Visual Elements: None specified
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
- Bonus Crab [8]
- Wheel of Fortune [7]
- Challenges [6]
- Collections [5]
- Coin Shop [6]
Entity Connections to state explicitly [priority]:
- Coins → are exchanged in → the Coin Shop for rewards [7]
- Challenges → unlock → coins, free spins and bonus credits [6]
Summary: The gamification features of the rewards area: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop.
Copywriter Notes: Describe the five features in short sentences as given: Bonus Crab (claim picks to open a crab reward, valid 7 days, 30x on bonus credit and 40x on free spin winnings), Wheel of Fortune (spend an eligible spin or Coins, 7 days, 30x), Challenges and Collections (found under Rewards), Coin Shop (exchange Coins for rewards and bonus credits up to €4,500, prices vary by item, separate wagering may apply). Say that rewards can carry their own wagering requirements. Use no tracked keyword in the body of this block.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_promotions.gamification_features: [{"name": "Bonus Crab", "mechanics": "Claim qualifying picks to open a crab reward and reveal a casino prize.", "access": "Rewards area; qualifying activity may grant free picks.", "rewards": ["Bonus credits", "Free Spins", "Coins"], "validity": "7 days after reward assignment", "wagering_requirement": "30x awarded bonus credit; 40x winnings from Free Spins"}, {"name": "Wheel of Fortune", "mechanics": "Spend an eligible spin or Coins to rotate a prize wheel.", "access": "Rewards area", "rewards": ["Bonus credits", "Free Spins", "Coins"], "validity": "7 days", "wagering_requirement": "30x bonus awards"}, {"name": "Challenges", "mechanics": "Complete qualifying gambling tasks to unlock listed rewards.", "access": "Rewards > Challenges", "rewards": ["Coins", "Free Spins", "Bonus credits"], "validity": "As shown for each challenge"}, {"name": "Collections", "mechanics": "Collect campaign items by completing qualifying activity; redeem completed sets.", "access": "Rewards > Collections", "rewards": ["Coins", "Bonus rewards"], "validity": "Campaign-specific"}, {"name": "Coin Shop", "mechanics": "Exchange earned Coins for rewards in the Shop.", "access": "Rewards > Shop", "rewards": ["Reward items and bonus credits up to €4,500"], "important_terms": ["Coin prices and prize availability vary by item.", "Rewards may carry separate wagering requirements."]}]
