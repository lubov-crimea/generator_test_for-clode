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
Page intent: Compact brand-review page about the Longfu88 online casino for players from Thailand, built for a reader on a phone: the fact table, opening the casino on mobile, sign-up and login, the first bonus, adding funds, taking money out, what to play, sports bets, promotions and rewards, VIP levels, licence and data rules, responsible play, support, a short FAQ and a summary. Page voice: how-to and imperative, sentences of about 12 words, paragraphs of one to two sentences, many short flat H2 sections, each opens with the action the reader takes and ends with the one thing to check; lists and short tables where they save words; calls to action at the first bonus only. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Thailand.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 รีวิว Longfu88 casino บนมือถือสำหรับผู้เล่นชาวไทย (88-112 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Thailand.
b02   H2 ข้อมูลสำคัญในตารางเดียว (74-94 words): A fact sheet of the casino: licence, minimum deposit, welcome bonus, payment methods, Mobile access, currencies, languages, cashback, support.
b03   H2 ตั้งค่าเล่นบนมือถือในไม่กี่นาที (106-134 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b04   H2 สมัครสมาชิกและเข้าสู่ระบบ (175-225 words): Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes.
b05   H2 โบนัสแรกและเงื่อนไข (188-241 words): The Casino Welcome Bonus with its figures, claiming steps and alternatives, then the wagering, validity and bet limits in a table.
b06   H2 การฝากเงิน (135-173 words): Deposit methods grouped by type with the general limits and speed, the local options for Thailand and the six-step deposit route.
b07   H2 การถอนเงิน (122-154 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b08   H2 เกมที่น่าเล่น (257-326 words): The nine game categories, three example slots with RTP, the live section with the exclusive baccarat, the other categories and the ten providers.
b09   H2 เดิมพันกีฬา (102-130 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b10   H2 โปรโมชันและรางวัลต่อเนื่อง (168-215 words): The seven reload and seasonal offers in a table, the weekly cashback with VIP rates and the rebates, and the five reward features in short.
b11   H2 ระดับสมาชิก VIP (88-112 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b12   H2 ใบอนุญาตและกฎข้อมูลส่วนบุคคล (168-215 words): Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected.
b13   H2 การเล่นอย่างรับผิดชอบ (94-120 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b14   H2 ฝ่ายสนับสนุนลูกค้า (68-86 words): Support channels, availability and languages.
b15   H2 คำถามที่พบบ่อยบนมือถือ (158-202 words): Short answers on withdrawal time, claiming the bonus, password recovery, the app question.
b16   H2 สรุปก่อนตัดสินใจ (81-104 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# รีวิว Longfu88 casino บนมือถือสำหรับผู้เล่นชาวไทย
Longfu88 เป็นคาสิโนออนไลน์ที่เปิดตัวในปี 2026 โดยรวมเกมคาสิโน ไลฟ์ดีลเลอร์ การเดิมพันกีฬา และหวยไว้ในบัญชีเดียว หมวดเกมประกอบด้วยสล็อต ไลฟ์ดีลเลอร์ เกมโต๊ะ แจ็กพอต เกมยิงปลา เกม P2P เกมเร็ว หวย และเกมแครชกับเกมทันใจ พร้อมสปอร์ตบุ๊กสำหรับเดิมพันกีฬา

หน้านี้เขียนสำหรับผู้เล่นชาวไทย ผู้เล่นต้องมีอายุอย่างน้อย 18 ปี เนื้อหาเรียงตามลำดับการใช้งานจริง ได้แก่ ข้อมูลสำคัญ ใบอนุญาต โบนัส เกม การฝากถอน การเล่นบนมือถือ และการเล่นอย่างรับผิดชอบ

## ข้อมูลสำคัญในตารางเดียว
=== b02 ===
| รายการ | ข้อมูล |
|---|---|
| ใบอนุญาต | คอสตาริกา ผู้ดำเนินการ Lumina 000-039123-R-319326-001 |
| ฝากขั้นต่ำ | €10 |
| โบนัสต้อนรับ | 188% สูงสุด €2,088 + ฟรีสปิน 18 ครั้ง |
| ช่องทางชำระเงิน | บัตร Visa และ Mastercard, โอนผ่านธนาคาร, Bitcoin, USDT, PromptPay QR |
| มือถือ | Android, iOS, เว็บมือถือ |
| สกุลเงิน | EUR, USD, MYR, THB, SGD, USDT |
| ภาษาที่รองรับ | อังกฤษ, มลายู, จีน, ไทย, อินโดนีเซีย, เวียดนาม |
| แคชแบ็ก | สูงสุด 10% ของยอดขาดทุนสุทธิรายสัปดาห์ |
| ฝ่ายสนับสนุน | support@longfu88.com, ไลฟ์แชต 24 ชั่วโมง |

## ตั้งค่าเล่นบนมือถือในไม่กี่นาที
=== b03 ===
เปิดเว็บไซต์ผ่านเบราว์เซอร์บนสมาร์ตโฟนหรือแท็บเล็ต เพราะคาสิโนเป็นเว็บไซต์แบบปรับตามหน้าจอ รองรับ Android, iOS และเว็บมือถือ จากนั้นเพิ่มทางลัดไว้บนหน้าจอหลัก ทางลัดนี้คือ Longfu88 app ในรูปแบบเว็บไซต์ ช่วยให้เข้าคาสิโนและสปอร์ตบุ๊กได้ทันที

ผ่านทางลัดเดียวกันใช้ได้ทั้งการเข้าบัญชี การฝาก การถอน และโบนัส ทำตามขั้นตอนในตารางตามอุปกรณ์ที่ใช้

| ขั้นตอน | Android (Chrome) | iOS (Safari) |
|---|---|---|
| 1 | เปิด Longfu88 ใน Chrome | เปิด Longfu88 ใน Safari |
| 2 | เปิดเมนูเบราว์เซอร์ แล้วเลือก Add to Home screen | แตะ Share แล้วเลือก Add to Home Screen |
| 3 | ยืนยันทางลัด | ยืนยันด้วย Add |

## สมัครสมาชิกและเข้าสู่ระบบ
=== b04 ===
สมัครด้วยอีเมลตามห้าขั้นตอน โดยเตรียมอีเมล รหัสผ่าน ชื่อตามกฎหมาย วันเกิด และที่อยู่ที่พักอาศัยไว้ก่อน

1. เปิด Longfu88 แล้วเลือกปุ่ม Register
2. กรอกอีเมลและตั้งรหัสผ่าน
3. ยืนยันอายุและยอมรับข้อกำหนด เงื่อนไข และนโยบายความเป็นส่วนตัว
4. กรอกข้อมูลส่วนตัวและที่อยู่ที่พักอาศัยเพิ่มเติม
5. เลือกปุ่ม Create Account แล้วยืนยันอีเมลหากระบบร้องขอ

หนึ่งคนมีบัญชีส่วนตัวได้เพียงบัญชีเดียว

ผู้เล่นที่ค้นหา Longfu caino login เพื่อหาหน้าเข้าสู่ระบบ ให้เลือก Login บนเว็บไซต์ ใส่อีเมลและรหัสผ่านที่ลงทะเบียนไว้ แล้วผ่านการตรวจสอบความปลอดภัยหากระบบขอ ลืมรหัสผ่านให้เลือก Forgot Password ขอลิงก์รีเซ็ตทางอีเมล แล้วตั้งรหัสผ่านใหม่ตามคำแนะนำ

คาสิโนอาจขอยืนยันตัวตนก่อนถอนเงิน เมื่อมีธุรกรรมผิดปกติหรือมูลค่าสูง หรือเมื่อมีการเปลี่ยนข้อมูลบัญชีหรือการชำระเงิน เอกสารที่ใช้มีดังนี้

- ยืนยันตัวตน: หนังสือเดินทาง บัตรประจำตัวประชาชน หรือใบขับขี่
- ยืนยันที่อยู่: ใบแจ้งค่าสาธารณูปโภคหรือใบแจ้งยอดบัญชีธนาคาร
- หลักฐานความเป็นเจ้าของช่องทางชำระเงิน
- เอกสารแหล่งที่มาของเงินเมื่อมีการร้องขอ

ส่งเอกสารภายใน 30 วันหลังได้รับคำขอ การตรวจสอบใช้เวลาสูงสุด 10 วันหลังได้รับเอกสารครบชุด ระหว่างนี้การถอนเงินอาจถูกพักไว้ หากตรวจสอบไม่ผ่าน ธุรกรรมอาจถูกปฏิเสธหรือบัญชีอาจถูกจำกัด

## โบนัสแรกและเงื่อนไข
=== b05 ===
Casino Welcome Bonus เป็นโบนัสฝากเงินครั้งแรกสำหรับผู้เล่นใหม่ บัญชีหนึ่งรับได้ครั้งเดียว Longfu88 bonus ชุดนี้ให้ 188% สูงสุด €2,088 พร้อมฟรีสปิน 18 ครั้ง ยอดฝากครั้งแรกของโบนัสนี้ขั้นต่ำ €50 ไม่ใช่ €10 ซึ่งเป็นยอดฝากขั้นต่ำทั่วไป สมัครกับ Longfu88 แล้วรับโบนัสตามสี่ขั้นตอนนี้

1. ลงทะเบียนบัญชีและกรอกข้อมูลส่วนตัวให้ครบ
2. ฝากเงินครั้งแรกที่เข้าเงื่อนไข
3. เปิดใช้งาน Casino Welcome Bonus ที่ My Bonuses ก่อนวางเดิมพันใด ๆ
4. เล่นเกมคาสิโนที่ร่วมรายการและทำยอดหมุนเวียนให้ครบก่อนโบนัสหมดอายุ

การรับโบนัสทำผ่าน My Bonuses หลังฝากเงินที่เข้าเงื่อนไข ขั้นตอนนี้ไม่มีการใส่โค้ดโปรโมชัน ทางเลือกอีกสองรายการคือ Live Casino Welcome Bonus 125% สูงสุด €888 ฝากขั้นต่ำ €30 และ Casino Crypto Welcome Bonus 188% สูงสุด 2,888 USDT ฝากขั้นต่ำ 50 USDT โดย Casino Welcome Bonus กับ Crypto Welcome Bonus เลือกได้อย่างใดอย่างหนึ่ง

เงื่อนไขของโบนัสแรกสรุปไว้ในตารางนี้

| เงื่อนไข | ค่า |
|---|---|
| ยอดหมุนเวียนโบนัส | 25x ของยอดฝากรวมโบนัส |
| ยอดหมุนเวียนฟรีสปิน | 40x ของเงินรางวัลจากฟรีสปิน |
| อายุโบนัส | 10 วันนับจากเปิดใช้งาน |
| เดิมพันสูงสุด | €22.5 ต่อสปิน |
| ถอนสูงสุดจากโบนัส | 5x ของยอดโบนัสเริ่มต้น |

ฝากด้วย Neteller และ Skrill ไม่ร่วมรายการ และเปิดโบนัสได้ครั้งละหนึ่งรายการ ขอถอนก่อนรับโบนัสหรือระหว่างใช้โบนัสอาจทำให้สิทธิ์เป็นโมฆะ การยกเลิกทำให้เงินโบนัสและเงินรางวัลที่ยังไม่แปลงถูกริบ อาจต้องยืนยันบัญชีก่อนจ่ายเงินรางวัล ฝากครั้งแรกให้ถึง €50 แล้วรับ Casino Welcome Bonus ได้ทันที

## การฝากเงิน
=== b06 ===
เลือกช่องทางฝากตามประเภทในตาราง ทุกช่องทางฝากขั้นต่ำ €10 สูงสุด €5,000 ต่อรายการ และเงินเข้าภายใน 1-2 นาที

| ประเภท | ตัวอย่าง | สกุลเงิน |
|---|---|---|
| ธนาคารและวอลเล็ตท้องถิ่น | QR ของไทยอย่าง PromptPay QR และวอลเล็ต DANA | THB, IDR |
| บัตร | บัตร Visa และ Mastercard | IDR, MYR, SGD, VND |
| โอนผ่านธนาคาร | การโอนแบบ Bank Transfer | IDR, MYR, VND |
| คริปโต | เหรียญ Bitcoin, Ethereum, Litecoin, USDC และ USDT ผ่านเครือข่าย TRC20, ERC20, BEP20 | BTC, ETH, LTC, USDC, USDT |
| อีวอลเล็ต | บริการ Neteller และ Skrill | EUR |
| วิธีแบบยุโรป | บริการ Sofort และ Giropay | EUR |

ผู้เล่นในไทยใช้ PromptPay QR (THB) ได้ คาสิโนไม่คิดค่าธรรมเนียมประมวลผลการฝาก แต่ผู้ให้บริการชำระเงินหรือเครือข่ายบล็อกเชนอาจคิดค่าธรรมเนียม วงเงินต่างกันได้ตามประเทศ สกุลเงิน และช่องทาง ส่วน Neteller และ Skrill ไม่ร่วมโบนัสต้อนรับ

ขั้นตอนฝากมีหกขั้น เข้าสู่บัญชี Longfu88 เปิดแคชเชียร์แล้วเลือกฝากเงิน เลือกช่องทางพร้อมสกุลเงินหรือเครือข่าย กรอกจำนวนเงินและข้อมูลชำระเงิน ยืนยันตามคำแนะนำ แล้วรอเงินเข้ายอดเล่น

## การถอนเงิน
=== b07 ===
ถอนเงินผ่านช่องทางที่รองรับ ได้แก่ Bank Transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT (TRC20, ERC20, BEP20), Touch'n Go, DANA, MoMo, DBS Bank และ Online Banking ถอนขั้นต่ำ €20 สูงสุด €5,000

1. เข้าสู่ระบบ Longfu88 และเปิดแคชเชียร์
2. เลือกถอนเงิน แล้วเลือกช่องทางที่รองรับ
3. กรอกจำนวนเงินและบัญชีธนาคาร วอลเล็ต หรือที่อยู่บล็อกเชนปลายทาง
4. ยืนยันตัวตนและช่องทางชำระเงินหากระบบขอ
5. ตรวจรายการแล้วกดยืนยันคำขอ
6. รอคาสิโนประมวลผลและรอธนาคารหรือเครือข่ายโอนเงินให้เสร็จ

Lngfu88 withdrawal time ของบัตร คริปโต และวอลเล็ตคือ 1-3 วันทำการ ส่วนการโอนผ่านธนาคารใช้เวลาประมวลผลสูงสุด 3 วันทำการ และธนาคารอาจส่งเงินเพิ่มอีก 3-5 วันทำการ คำขอโดยทั่วไปประมวลผลภายในสามวันทำการ การตรวจสอบตัวตนอาจทำให้ล่าช้า

คาสิโนไม่คิดค่าธรรมเนียมถอนมาตรฐาน แต่ผู้ให้บริการและเครือข่ายอาจคิดเพิ่ม หากยอดหมุนเวียนต่ำกว่ายอดฝาก อาจมีค่าธรรมเนียม 10% (ขั้นต่ำ €2.25) และบางธุรกรรมที่ฝากด้วยบัตรหรือโอนผ่านธนาคารอาจถูกคิด 15% ตรวจยอดหมุนเวียนขั้นต่ำ 1x ของยอดฝากก่อนกดถอน

## เกมที่น่าเล่น
=== b08 ===
เปิดล็อบบี้ของ Longfu88 Casino แล้วเลือกจากเก้าหมวดเกม ได้แก่ สล็อต ไลฟ์ดีลเลอร์ เกมโต๊ะ แจ็กพอต เกมยิงปลา เกม P2P เกมเร็ว หวย และเกมแครชกับเกมทันใจ ตรวจดูตัวอย่างสล็อตก่อน เพราะแต่ละเกมมีค่า RTP และตัวคูณสูงสุดต่างกัน

Gates of Olympus จาก Pragmatic Play มี RTP 96.50% ความผันผวนสูง และตัวคูณสูงสุด 5,000x ส่วน Sweet Bonanza จาก Pragmatic Play มี RTP 96.48% ความผันผวนสูง และตัวคูณสูงสุด 21,175x

Wanted Dead or a Wild จาก Hacksaw Gaming มี RTP 96.38% ความผันผวนสูงมาก และตัวคูณสูงสุด 12,500x RTP คือสัดส่วนเงินเดิมพันที่เกมคืนให้ผู้เล่นในระยะยาว ส่วนความผันผวนบอกว่าเงินรางวัลมาถี่หรือห่างเพียงใด

หมวดไลฟ์ดีลเลอร์เป็นอีกส่วนหนึ่งของล็อบบี้ และมี Longfu88 Baccarat เกมเอ็กซ์คลูซีฟที่เล่นแบบบาคาร่า รายชื่อผู้พัฒนาเกมมี Evolution และ SA Gaming ซึ่งเป็นสตูดิโอเกมไลฟ์ ผู้ที่อยากเล่นกับดีลเลอร์จริงควรเริ่มจากหมวดนี้

หมวดอื่นแยกกันตามวิธีเล่น เกมโต๊ะคือเกมไพ่และเกมโต๊ะแบบดั้งเดิม เกมยิงปลาให้ผู้เล่นเล็งยิงปลาบนหน้าจอ และเกม P2P เป็นการเล่นกับผู้เล่นคนอื่น เกมเร็วจบรอบในเวลาสั้น หวยคือการเลือกเลขแล้วรอผลออก ส่วนเกมแครชและเกมทันใจตัดสินผลทันทีในแต่ละรอบ ผู้เล่นที่เปิดเมนูของ Longfu 88 จะเห็นแจ็กพอตแยกเป็นอีกหมวดหนึ่ง

เกมของ Longfu 88 Casino มาจากผู้พัฒนาหลายราย ได้แก่Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft และ Hacksaw Gaming ผู้พัฒนาเหล่านี้จัดหาสล็อต เกมไลฟ์ และเกมโต๊ะให้กับคาสิโน

## เดิมพันกีฬา
=== b09 ===
เปิดส่วน Longfu sports เมื่ออยากเดิมพันกีฬา สปอร์ตบุ๊กครอบคลุมฟุตบอล บาสเกตบอล เทนนิส แบดมินตัน คริกเก็ต เทเบิลเทนนิส วอลเลย์บอล อีสปอร์ต และฟุตบอลเสมือน ผู้เล่นที่ติดตามฟุตบอลหรืออีสปอร์ตจึงหาตลาดที่ตามอยู่ได้ง่าย

Longfu88 มีรูปแบบเดิมพันเจ็ดแบบ ได้แก่ เดี่ยว แอคคิวมูเลเตอร์ ไลฟ์ แฮนดิแคป ยอดรวม เดิมพันระยะยาว และ Bet Builder แอคคิวมูเลเตอร์รวมหลายรายการไว้ในใบเดียว ส่วน Bet Builder ให้ประกอบตลาดของแมตช์เดียวกันเอง การเดิมพันสดมีอัตราต่อรองสดและตลาดระหว่างแข่งขัน เหมาะกับผู้ที่ตามดูเกมไปพร้อมกัน รายการแข่งและตลาดเดิมพันอาจต่างกันตามเขตอำนาจ ตรวจรายการก่อนวางเดิมพัน

## โปรโมชันและรางวัลต่อเนื่อง
=== b10 ===
ข้อเสนอฝากซ้ำของ Longfu88 อยู่ในตารางนี้ โดย 30x คิดจากยอดฝากรวมโบนัส

| ข้อเสนอ | รางวัล | ฝากขั้นต่ำ | หมุนเวียน |
|---|---|---|---|
| Casino Weekly Reload | ฟรีสปิน 50 | €30 | ฟรีสปิน 40x |
| Casino Weekly Crypto Reload | 60% ถึง 1,000 USDT | 20 USDT | 30x |
| Casino Weekend Reload | ถึง €3,360 + ฟรีสปิน 50 | €50 | 30x + ฟรีสปิน 40x |
| Casino Weekend Crypto Reload | 75% ถึง 750 USDT + ฟรีสปิน 100 | 20 USDT | 30x + ฟรีสปิน 40x |
| Casino Double Fortune | 50% ถึง €500 | €30 | 30x |
| ข้อเสนอเทศกาลชื่อ Casino Trick or Treat Pumpkin Bonanza | ฟรีสปินถึง 100 | €20 | ฟรีสปิน 40x |
| Casino Dragon Quest | เครดิตโบนัส €10 | €20 | 30x |

อายุ 7 วัน ยกเว้น Casino Double Fortune 24 ชั่วโมง เปิดใช้ใน My Bonuses ใช้ร่วมโบนัสอื่นไม่ได้ เดิมพันสูงสุด €5 ต่อสปิน

Casino Weekly Cashback คืนสูงสุด 10% ของยอดขาดทุนสุทธิรายสัปดาห์ในคาสิโน ไม่เกิน €6,988 เข้า My Bonuses วันจันทร์ หมุนเวียน 10x อัตรา VIP คือ Bronze 2% (€1,888), Silver 4% (€2,388), Gold 6% (€2,988), Platinum 8% (€3,988), Diamond 10% (€6,988)

Live Casino Cashback คืน 25% ถึง €850 เรเบตรายวันคือคาสิโน 0.9% ไลฟ์คาสิโน 1.0% P2P 0.8% หวย 1.0% หมุนเวียน 1x

Bonus Crab 7 วัน 30x และฟรีสปิน 40x Wheel of Fortune 7 วัน 30x Challenges Collections และ Coin Shop แลก Coins ได้ถึง €4,500 อาจมียอดหมุนเวียนแยก

## ระดับสมาชิก VIP
=== b11 ===
สะสมคะแนน VIP จากการเล่นด้วยเงินจริงที่เข้าเงื่อนไข คะแนนจะปลดล็อกระดับรางวัลที่มีหมายเลข 25 ระดับ แบ่งเป็นห้ากลุ่ม ได้แก่ Bronze, Silver, Gold, Platinum และ Diamond ระดับ 1 ใช้ 1 คะแนน ให้รางวัล €9.8 แคชแบ็ก 1% และวงเงินถอน €9,800 ส่วนระดับ 25 ใช้ 5,500 คะแนน ให้รางวัล €980 แคชแบ็ก 10% และวงเงินถอน €147,000

ระดับที่สูงขึ้นเพิ่มข้อเสนอเฉพาะบุคคล แคชแบ็ก วงเงินถอนที่สูงขึ้น และผู้จัดการ VIP ส่วนตัวตั้งแต่ระดับ 4 รางวัลและวงเงินอาจต่างกันตามระดับและสกุลเงิน และกฎอาจเปลี่ยน

## ใบอนุญาตและกฎข้อมูลส่วนบุคคล
=== b12 ===
คาสิโนเปิดตัวในปี 2026 และรองรับบัญชีสกุล EUR, USD, MYR, THB, SGD และ USDT เข้าเว็บไซต์ผ่านที่อยู่ของ Longfu 88 Official Site เท่านั้น และอย่าใช้หน้าเลียนแบบ ผู้เล่นต้องอายุ 18 ปีขึ้นไปและเล่นได้ตามกฎหมายของสถานที่พำนัก ถือบัญชีส่วนตัวได้เพียงหนึ่งบัญชี และห้ามใช้ช่องทางชำระเงินของบุคคลที่สาม

ใบอนุญาตของ casino Longfu88 อยู่ภายใต้เขตอำนาจคอสตาริกา ผู้ดำเนินการคือ Lumina เลขทะเบียน 000-039123-R-319326-001 Lumina ยังเป็นผู้ควบคุมข้อมูล และผู้ดูแลการคุ้มครองข้อมูลติดต่อได้ที่ dpo@longfu88.com

ข้อมูลอาจส่งต่อให้ผู้ให้บริการชำระเงิน ผู้ให้บริการยืนยันตัวตน ผู้ให้บริการเทคโนโลยี และหน่วยงานกำกับหรือเจ้าหน้าที่บังคับใช้กฎหมายเมื่อจำเป็น ผู้เล่นมีสิทธิ์เข้าถึง แก้ไข ลบเมื่อกฎหมายอนุญาต จำกัด คัดค้าน โอนย้ายข้อมูล และถอนความยินยอม

ผู้ดำเนินการใช้มาตรการทางเทคนิคและการจัดการเพื่อปกป้องบัญชี การชำระเงิน และข้อมูลส่วนบุคคล ส่วนเจ้าของบัญชีต้องดูแลข้อมูลเข้าสู่ระบบด้วยตนเอง

## การเล่นอย่างรับผิดชอบ
=== b13 ===
ผู้เล่นต้องอายุอย่างน้อย 18 ปีและเล่นเฉพาะในที่ที่กฎหมายอนุญาต หากควบคุมการเล่นไม่ได้ ให้ขอห้ามตัวเองเข้าเล่นทางอีเมลถึงฝ่ายสนับสนุนที่ support@longfu88.com การเข้าบัญชีและการเล่นอาจถูกจำกัดตามระยะเวลาที่ตกลง โดยดำเนินการภายใน 24 ชั่วโมงหลังคำขอได้รับการประมวลผล ปิดบัญชีขอผ่านฝ่ายสนับสนุนลูกค้าได้เช่นกัน ขั้นตอนมีสี่ขั้น ติดต่อฝ่ายสนับสนุน ยืนยันข้อมูลบัญชีและเงื่อนไขที่ต้องการ ให้คาสิโนจำกัดหรือปิดการเข้าถึง แล้วขอความช่วยเหลือจากหน่วยงานอิสระเมื่อเหมาะสม

แบบประเมินตนเองช่วยให้สังเกตสัญญาณของผลเสียจากการพนัน ผู้ที่ต้องการคำปรึกษาติดต่อ GamCare, Gamblers Anonymous และ Gambling Therapy ได้ หน้านี้ไม่อาจแทนความช่วยเหลือจากผู้เชี่ยวชาญอิสระ

## ฝ่ายสนับสนุนลูกค้า
=== b14 ===
ติดต่อฝ่ายสนับสนุนลูกค้าผ่านไลฟ์แชตที่เปิดตลอด 24 ชั่วโมง หรือส่งอีเมลถึง support@longfu88.com ไลฟ์แชตเหมาะกับคำถามที่ต้องการคำตอบทันที ส่วนอีเมลเหมาะกับเรื่องที่ต้องอธิบายรายละเอียด ฝ่ายสนับสนุนรองรับหกภาษา ได้แก่ อังกฤษ มลายู จีนตัวย่อ ไทย อินโดนีเซีย และเวียดนาม ผู้เล่นชาวไทยจึงเลือกสื่อสารเป็นภาษาไทยได้ เตรียมข้อมูลบัญชีให้พร้อมก่อนเริ่มแชต

---

## BLOCK BRIEF
Block: b15, H2 "Mobile FAQ" (under H1 "รีวิว Longfu88 casino บนมือถือสำหรับผู้เล่นชาวไทย")
Page heading (output language): "คำถามที่พบบ่อยบนมือถือ"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 158-202 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 202, but never beyond 242 words.
Format: list. Visual Elements: Bulleted/numbered list — 4 of 4 lists on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 login": exactly 1 time(s)
- "Longfu caino login": 0 (do not use)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 promo code": exactly 1 time(s)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu": 0 (do not use)
- "Longfu sports": 0 (do not use)
Entities to cover [priority 1-10]:
- Frequently Asked Questions [8]
- Withdrawal time [6]
- Claiming the bonus [6]
- Password recovery [6]
- The app question [6]
Entity Connections to state explicitly [priority]:
- Frequently Asked Questions → cover → withdrawal time, claiming the bonus, password recovery, the app question [6]
Summary: Short answers on withdrawal time, claiming the bonus, password recovery, the app question.
Copywriter Notes: A bulleted list of exactly 4 items, each a bold question followed by a short answer of 20-30 words, in this order: (1) how long a withdrawal takes (card, crypto and wallet withdrawals 1 to 3 business days; bank transfer up to 3 business days of casino processing plus 3 to 5 business days of bank delivery; the wording must differ from the withdrawals section); the answer contains the keyword "Longfu88" exactly once, written verbatim; (2) how to claim the Casino Welcome Bonus (activate it in My Bonuses after the first qualifying deposit of €50; the claiming procedure has no promo code step); the question contains the keyword "Longfu88 promo code" exactly once, written verbatim; (3) how to recover a forgotten password (Forgot Password on the login screen, reset link by e-mail); the question contains the keyword "Longfu88 login" exactly once, written verbatim; (4) whether there is an app (no download is described: the casino is a responsive website that can be added to the home screen on Android and iOS). The brand name "Longfu88" may stand in an answer, never in a question. These are the only questions on the page; the questions are the one place where question form is allowed. Use "Longfu88" exactly once, "Longfu88 login" exactly once and "Longfu88 promo code" exactly once, and no other tracked keyword.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_account.login.password_recovery: ["Choose Forgot Password on the login screen.", "Request a reset link using the registered email.", "Follow the emailed instructions to set a new password."]
- brandinfo_welcome.welcome_bonus.claiming_procedure: ["Register an account and complete the required personal details.", "Make the first qualifying deposit.", "Activate the Casino Welcome Bonus in My Bonuses before placing any wagers.", "Play eligible casino games and complete the wagering before expiry."]
- brandinfo_withdrawal.withdrawal_methods[0].transaction_speed: Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days
- brandinfo_withdrawal.withdrawal_methods[1].transaction_speed: 1–3 business days
- brandinfo_welcome.welcome_bonus.minimum_deposit: €50
- brandinfo_app.app_information.platforms: ["Android", "iOS", "Mobile web"]
- brandinfo_app.app_information.mobile_access: Responsive Longfu88 website usable on smartphone and tablet browsers.
Counting warning: the facts above contain tracked keywords "Longfu88" (x1). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 1, 'Longfu88 login': 1, 'Longfu88 promo code': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').
