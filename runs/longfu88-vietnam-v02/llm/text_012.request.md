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
Country / GEO: Vietnam
Language: Vietnamese (vi). Write ONLY in this language.
Page intent: Long reference page about the Longfu88 online casino for players from Vietnam: what the casino offers, the fact table, licence and data protection, registration and verification, the welcome bonus with a terms table, reloads, cashback, rewards, the VIP programme, the game library by category, providers, the sportsbook with a bonus table, deposit methods, withdrawals, mobile access, responsible gambling, support, pros and cons, a six-answer FAQ and a verdict. Page voice: formal and exhaustive, sentences of about 21 words, paragraphs of three to four sentences, tables wherever two or more attributes belong to an item, comparative statements that put offers side by side, every table introduced by one sentence and followed by one sentence on what it means; one call to action at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Vietnam.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 casino: hướng dẫn đầy đủ dành cho người chơi Việt Nam (112-144 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Vietnam.
b02   H2 Hồ sơ nhà cái (91-117 words): What the casino is for a player from Vietnam: launch year, account currencies, the official website and who may play.
b03   H2 Bảng thông tin sòng bạc (109-139 words): A fact sheet of the casino: licence, operator, launch year, currencies, languages, payment methods, welcome bonus, cashback, minimum deposit, Minimum age, Sports, Game providers, VIP tiers, support.
b04   H2 Giấy phép, đơn vị vận hành và quyền riêng tư (158-202 words): Who licenses and runs the casino (jurisdiction, operator, registration number) and how personal data and accounts are protected.
b05   H2 Quy trình đăng ký và đăng nhập (123-157 words): How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.
b06     H3 Kiểm tra giấy tờ KYC (112-144 words): When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.
b07   H2 Chi tiết thưởng chào mừng (151-191 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b08     H3 Điều kiện thưởng chào mừng trong một bảng (112-144 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b09   H2 Chương trình VIP: cấp bậc và hạn mức (119-151 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b10   H2 Thưởng nạp lại, ưu đãi đặc biệt và khuyến mãi theo mùa (132-167 words): The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
b11     H3 Tỷ lệ hoàn tiền và hoàn trả (86-109 words): Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
b12     H3 Các tính năng trong khu vực phần thưởng (80-100 words): The gamification features of the rewards area: Bonus Crab, Wheel of Fortune, Challenges, Collections and the Coin Shop.
b13   H2 Tổng quan thư viện trò chơi (91-117 words): The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.
b14     H3 Tựa slot và con số đáng chú ý (104-133 words): Three example slots with their provider, RTP, volatility and maximum multiplier.
b15     H3 Khu vực sòng bạc trực tiếp (99-125 words): The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.
b16     H3 Các danh mục khác (86-109 words): The remaining game categories in one block: table games, fishing, P2P, fast games, lottery and crash and instant games.
b17   H2 Nhà cung cấp trò chơi trong sảnh (55-69 words): Which studios supply the games, named from the provider list.
b18   H2 Bảng phương thức và hạn mức nạp tiền (141-179 words): Deposit methods grouped by type with the general limits and speed, the local options for Vietnam and the six-step deposit route.
b19     H3 Rút tiền: các bước, thời gian và phí (132-167 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b20   H2 Tổng quan cá cược thể thao (112-144 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b21     H3 Thưởng và tăng tỷ lệ cược thể thao (86-109 words): The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
b22   H2 Chơi trên thiết bị di động (106-134 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b23   H2 Công cụ cờ bạc có trách nhiệm (112-144 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b24   H2 So sánh ưu điểm và hạn chế (55-69 words): A pros and cons table built only from facts stated elsewhere on the page.
b25   H2 Kênh hỗ trợ khách hàng (80-100 words): Support channels, availability and languages.
b26   H2 Giải đáp các câu hỏi thường gặp (229-293 words): Short answers on wagering, withdrawal time, weekly cashback, VIP levels, password recovery, claiming the bonus.
b27   H2 Đánh giá cuối cùng (104-133 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 casino: hướng dẫn đầy đủ dành cho người chơi Việt Nam
Longfu88 là sòng bạc trực tuyến ra mắt vào năm 2026, kết hợp trò chơi casino, trò chơi live dealer, cá cược thể thao và xổ số trong cùng một nền tảng. Sảnh game được chia thành các danh mục slot, live dealer, trò chơi bàn, jackpot, bắn cá, P2P, trò chơi nhanh, xổ số cùng crash và instant, còn mục thể thao vận hành như một sportsbook riêng. Bài viết được viết cho người chơi từ Việt Nam, và người chơi trưởng thành phải đủ ít nhất 18 tuổi mới được tham gia.

Các phần tiếp theo lần lượt đi qua bảng thông tin, giấy phép, đăng ký, thưởng, thư viện trò chơi, thanh toán, chơi trên di động và cờ bạc có trách nhiệm, để người đọc có đủ dữ kiện cụ thể trước khi tự cân nhắc quyết định.

## Hồ sơ nhà cái
Longfu88 là sòng bạc trực tuyến được ra mắt vào năm 2026, và tài khoản tại đây có thể dùng sáu loại tiền tệ gồm EUR, USD, MYR, THB, SGD và USDT. Người chơi nên truy cập đúng địa chỉ của Longfu 88 Official Site thay vì các trang giả mạo có tên gần giống, vì thông tin đăng nhập và giao dịch chỉ nên nhập trên trang chính thức. Điều kiện tham gia gồm bốn điểm: người chơi phải đủ 18 tuổi, phải được phép đánh bạc hợp pháp tại nơi mình cư trú, chỉ dùng một tài khoản cá nhân với thông tin đăng ký chính xác và không sử dụng phương thức thanh toán của người khác.

## Bảng thông tin sòng bạc
| Thông số | Chi tiết |
|---|---|
| Giấy phép | Costa Rica, Lumina, số đăng ký 000-039123-R-319326-001 |
| Đơn vị vận hành | Lumina |
| Năm ra mắt | 2026 |
| Tiền tệ | EUR, USD, MYR, THB, SGD, USDT |
| Ngôn ngữ hỗ trợ | Tiếng Anh, Tiếng Mã Lai, Tiếng Trung giản thể, Tiếng Thái, Tiếng Indonesia, Tiếng Việt |
| Phương thức thanh toán | Thẻ Visa, Mastercard, chuyển khoản ngân hàng, Bitcoin, USDT, ví MoMo |
| Thưởng chào mừng | 188% tối đa €2.088 + 18 vòng quay miễn phí |
| Hoàn tiền | Tối đa 10% thua lỗ ròng casino hằng tuần |
| Nạp tối thiểu | €10 |
| Độ tuổi tối thiểu | 18 |
| Thể thao | Bóng đá, bóng rổ, quần vợt, cầu lông, cricket, bóng bàn, bóng chuyền, thể thao điện tử |
| Nhà cung cấp trò chơi | Evolution, Pragmatic Play, NetEnt, Red Tiger cùng các nhà cung cấp khác |
| Hạng VIP | Bronze, Silver, Gold, Platinum, Diamond |
| Hỗ trợ | support@longfu88.com, chat trực tuyến 24/7 |

## Giấy phép, đơn vị vận hành và quyền riêng tư
Giấy phép mà casino Longfu88 nêu thuộc phạm vi pháp lý Costa Rica, do đơn vị vận hành Lumina nắm giữ với số đăng ký 000-039123-R-319326-001, và đó là toàn bộ thông tin cấp phép của nền tảng. Lumina cũng là bên kiểm soát dữ liệu, tức là đơn vị quyết định dữ liệu cá nhân được xử lý ra sao, đồng thời bảo vệ tài khoản, giao dịch thanh toán và thông tin cá nhân bằng các biện pháp kỹ thuật và tổ chức.

Dữ liệu có thể được chia sẻ với nhà cung cấp dịch vụ thanh toán, xác minh danh tính và công nghệ, cũng như với cơ quan quản lý và cơ quan thực thi pháp luật khi có yêu cầu. Người chơi có quyền truy cập, chỉnh sửa, xóa dữ liệu khi pháp luật cho phép, hạn chế xử lý, phản đối, chuyển dữ liệu khi áp dụng và rút lại sự đồng ý. Các yêu cầu này được gửi tới cán bộ bảo vệ dữ liệu của Longfu88 qua email trong chính sách quyền riêng tư.

Chủ tài khoản tự chịu trách nhiệm giữ an toàn cho thông tin đăng nhập, còn đơn vị vận hành có thể tạm ngừng hoạt động để xác minh hoặc khi nghi ngờ lạm dụng.

## Quy trình đăng ký và đăng nhập
Đăng ký tại Longfu88 bằng email gồm năm bước và yêu cầu email, mật khẩu, họ tên pháp lý, ngày sinh cùng địa chỉ cư trú.

1. Mở trang web và chọn Đăng ký.
2. Nhập email và tạo mật khẩu.
3. Xác nhận độ tuổi, đồng ý với Điều khoản và Điều kiện cùng Chính sách quyền riêng tư.
4. Điền thêm thông tin cá nhân và địa chỉ cư trú.
5. Chọn Tạo tài khoản và hoàn tất xác nhận email nếu hệ thống yêu cầu.

Mỗi người chơi chỉ được giữ một tài khoản cá nhân. Ở bước Longfu88 login, người chơi chọn Đăng nhập, nhập email và mật khẩu đã đăng ký, rồi hoàn tất kiểm tra bảo mật nếu có. Người tìm trang Longfu caino login cũng đi theo trình tự này. Khi quên mật khẩu, người chơi chọn Quên mật khẩu ở màn hình đăng nhập, nhận liên kết đặt lại qua email và làm theo hướng dẫn để tạo mật khẩu mới.

### Kiểm tra giấy tờ KYC
Xác minh KYC có thể được yêu cầu trước khi rút tiền, khi có giao dịch bất thường hoặc giá trị lớn, và khi thông tin tài khoản hay thanh toán thay đổi. Người chơi có tối đa 30 ngày để gửi giấy tờ sau khi được yêu cầu, gồm các loại sau:

- Giấy tờ tùy thân: hộ chiếu, thẻ căn cước quốc gia hoặc giấy phép lái xe.
- Chứng minh địa chỉ: hóa đơn tiện ích hoặc sao kê ngân hàng.
- Bằng chứng quyền sở hữu thẻ, tài khoản ngân hàng hoặc ví điện tử dùng để thanh toán.
- Chứng minh nguồn tiền khi được yêu cầu, chẳng hạn bằng chứng thu nhập.

Bộ hồ sơ đầy đủ thường được xem xét trong vòng 10 ngày kể từ khi nhận. Trong thời gian chờ, yêu cầu rút tiền có thể bị giữ lại, còn nếu kiểm tra không đạt, giao dịch có thể bị từ chối và tài khoản có thể bị hạn chế.

## Chi tiết thưởng chào mừng
Longfu88 bonus mang tên Casino Welcome Bonus là ưu đãi nạp tiền đầu tiên, cấp 188% tối đa €2.088 cùng 18 vòng quay miễn phí. Ưu đãi dành cho người chơi mới đã đăng ký, áp dụng cho khoản nạp đầu tiên đủ điều kiện, và mỗi tài khoản chỉ nhận một ưu đãi chào mừng. Mức nạp tối thiểu của riêng ưu đãi này là €50, cao hơn mức nạp tối thiểu chung €10 của sòng bạc. Người chơi tại Longfu88 nhận thưởng theo bốn bước:

- Đăng ký tài khoản và điền thông tin cá nhân.
- Thực hiện khoản nạp đầu tiên đủ điều kiện.
- Kích hoạt Casino Welcome Bonus trong My Bonuses trước khi đặt cược.
- Chơi trò chơi casino hợp lệ và hoàn thành vòng cược trước khi hết hạn.

Con đường nhận thưởng là kích hoạt trong My Bonuses sau khoản nạp đủ điều kiện, vì quy trình trên không có bước nhập Longfu88 promo code nào. Hai ưu đãi nạp đầu khác là Live Casino Welcome Bonus (125% tối đa €888, nạp tối thiểu €30) và Casino Crypto Welcome Bonus (188% tối đa 2.888 USDT, nạp tối thiểu 50 USDT), cả hai thay thế Casino Welcome Bonus ở khoản nạp đầu. Hãy đăng ký và nhận Casino Welcome Bonus ở khoản nạp đầu tiên.

### Điều kiện thưởng chào mừng trong một bảng
Năm thông số dưới đây quyết định cách tiền thưởng của Casino Welcome Bonus được quy đổi thành tiền có thể rút.

| Điều kiện | Giá trị |
|---|---|
| Vòng cược thưởng | 25x tổng khoản nạp và tiền thưởng |
| Vòng cược vòng quay miễn phí | 40x tiền thắng từ vòng quay miễn phí |
| Thời hạn | 10 ngày kể từ khi kích hoạt |
| Cược tối đa | €22,5 mỗi vòng quay |
| Rút tối đa | 5x số tiền thưởng ban đầu |

Khoản nạp bằng Neteller và Skrill bị loại khỏi ưu đãi, và mỗi lúc chỉ một khuyến mãi được hoạt động. Yêu cầu rút tiền trước khi nhận thưởng hoặc khi thưởng còn hiệu lực có thể làm mất tư cách nhận ưu đãi, còn hủy khuyến mãi đồng nghĩa với mất tiền thưởng và tiền thắng chưa quy đổi. Tài khoản cũng có thể cần xác minh trước khi trả tiền thắng từ thưởng.

## Chương trình VIP: cấp bậc và hạn mức
Longfu88 VIP Program tích điểm VIP từ hoạt động chơi bằng tiền thật đủ điều kiện, và các điểm này mở khóa 25 cấp thưởng được đánh số, gộp thành năm hạng Bronze, Silver, Gold, Platinum và Diamond. Bảng dưới đây nêu sáu mốc tiêu biểu là cấp 1, 5, 10, 15, 20 và 25.

| Cấp | Điểm | Phần thưởng | Hoàn tiền | Hạn mức rút |
|---|---|---|---|---|
| 1 | 1 | €9,8 | 1% | €9.800 |
| 5 | 70 | €24,5 | 2% | €34.300 |
| 10 | 700 | €147 | 4% | €63.700 |
| 15 | 2.100 | €392 | 6% | €88.200 |
| 20 | 3.600 | €637 | 8% | €117.600 |
| 25 | 5.500 | €980 | 10% | €147.000 |

Cấp càng cao, hạn mức rút và tỷ lệ hoàn tiền càng tăng, với cấp 25 cho hạn mức rút €147.000 so với €9.800 ở cấp 1. Từ cấp 4, người chơi còn có quản lý VIP cá nhân cùng các ưu đãi cá nhân hóa. Phần thưởng và hạn mức rút có thể khác nhau theo cấp VIP và loại tiền tệ, và quy tắc chương trình có thể thay đổi.

## Thưởng nạp lại, ưu đãi đặc biệt và khuyến mãi theo mùa
Longfu88 có bảy ưu đãi định kỳ và theo dịp, trong đó Casino Weekly Reload tặng 50 vòng quay miễn phí.

| Ưu đãi | Thưởng | Nạp tối thiểu | Vòng cược | Hiệu lực |
|---|---|---|---|---|
| Casino Weekly Reload | 50 vòng quay miễn phí | €30 | 40x thắng vòng quay | 7 ngày |
| Casino Weekly Crypto Reload | 60% tối đa 1.000 USDT | 20 USDT | 30x nạp + thưởng | 7 ngày |
| Casino Weekend Reload | €3.360 + 50 vòng quay | €50 | 30x nạp + thưởng, 40x thắng vòng quay | 7 ngày |
| Casino Weekend Crypto Reload | 75% tối đa 750 USDT + 100 vòng quay | 20 USDT | 30x nạp + thưởng, 40x thắng vòng quay | 7 ngày |
| Casino Double Fortune (một ngày) | 50% tối đa €500 | €30 | 30x nạp + thưởng | 24 giờ |
| Khuyến mãi theo mùa Casino Trick or Treat Pumpkin Bonanza | 100 vòng quay | €20 | 40x thắng vòng quay | 7 ngày |
| Casino Dragon Quest (xác minh) | €10 tín dụng thưởng | €20 | 30x tín dụng | 7 ngày |

Mọi ưu đãi kích hoạt trong My Bonuses, mỗi kỳ chỉ nhận một lần và không kết hợp với thưởng casino khác đang hoạt động. Cược tối đa khi cược tiền thưởng là €5 mỗi vòng quay.

### Tỷ lệ hoàn tiền và hoàn trả
Casino Weekly Cashback hoàn tối đa 10% thua lỗ ròng casino hằng tuần, giới hạn €6.988, tính từ 00:00 UTC thứ Hai đến 23:59 UTC Chủ nhật. Người chơi đăng ký theo chu kỳ bốn tuần, tiền hoàn vào My Bonuses thứ Hai, cược 10x trước khi rút, và tỷ lệ phụ thuộc hạng VIP.

| Hạng VIP | Tỷ lệ | Mức tối đa |
|---|---|---|
| Bronze | 2% | €1.888 |
| Silver | 4% | €2.388 |
| Gold | 6% | €2.988 |
| Platinum | 8% | €3.988 |
| Diamond | 10% | €6.988 |

Live Casino Cashback hoàn 25% tối đa €850. Unlimited Rebate được cộng hằng ngày theo danh mục: casino 0,9%, casino trực tiếp 1,0%, P2P 0,8% và xổ số 1,0%, mỗi khoản cược 1x. Chỉ cược tiền thật được tính.

### Các tính năng trong khu vực phần thưởng
Khu vực Rewards có năm tính năng, và phần thưởng có thể mang vòng cược riêng. Bonus Crab cho nhận lượt chọn để mở phần thưởng cua, hiệu lực 7 ngày, cược 30x với tiền thưởng và 40x với tiền thắng từ vòng quay miễn phí. Wheel of Fortune dùng một lượt quay hợp lệ hoặc Coins, hiệu lực 7 ngày, cược 30x. Challenges mở khóa Coins, vòng quay miễn phí và tín dụng thưởng, còn Collections cho đổi các bộ sưu tập hoàn chỉnh. Tại Coin Shop, Coins đổi lấy phần thưởng và tín dụng thưởng tới €4.500, giá tùy từng món.

## Tổng quan thư viện trò chơi
Longfu 88 Casino cung cấp chín danh mục trong sảnh game: slot, trò chơi live dealer, trò chơi bàn, jackpot, bắn cá, trò chơi P2P, trò chơi nhanh, xổ số cùng crash và instant. Slot và live dealer đại diện cho hai cách chơi khác nhau, một bên quay theo từng vòng, một bên ngồi cùng người chia bài. Jackpot, crash và trò chơi nhanh dành cho người thích nhịp chơi gọn. Tại Longfu88, các danh mục nằm chung một sảnh, và ba phần tiếp theo lần lượt trình bày slot, khu vực casino trực tiếp cùng các danh mục còn lại.

### Tựa slot và con số đáng chú ý
Ba tựa slot dưới đây minh họa các chỉ số cần xem trước khi quay. RTP là tỷ lệ hoàn trả lý thuyết của máy trong thời gian dài, còn độ biến động cho biết tiền thắng đến thưa hay đều. Gates of Olympus của Pragmatic Play có RTP 96,50%, độ biến động cao và hệ số nhân tối đa 5.000x. Sweet Bonanza cũng của Pragmatic Play có RTP 96,48%, độ biến động cao và hệ số nhân tối đa 21.175x. Wanted Dead or a Wild do Hacksaw Gaming cung cấp, với RTP 96,38%, độ biến động rất cao và hệ số nhân tối đa 12.500x, nên đây là tựa có mức dao động lớn nhất trong ba tựa.

### Khu vực sòng bạc trực tiếp
Live dealer games là một danh mục riêng của sảnh, nơi người chơi tham gia bàn chơi có người chia bài được truyền trực tiếp. Điểm riêng của khu vực này là Longfu88 Baccarat, một trò chơi live hoặc trò chơi bàn độc quyền với lối chơi baccarat. Mảng live casino được vận hành bởi nhiều studio, trong đó có Evolution và SA Gaming trong danh sách nhà cung cấp của sảnh. Danh sách đầy đủ các studio nằm ở phần nhà cung cấp phía dưới. Người chơi quan tâm tới hình thức chơi với người chia bài có thể bắt đầu từ danh mục này.

### Các danh mục khác
Bên cạnh slot, live dealer và jackpot, sòng bạc trực tuyến còn cung cấp sáu danh mục khác, mỗi danh mục là một kiểu chơi riêng.

- **Trò chơi bàn**: các trò bài và bàn cổ điển, người chơi đặt cược theo luật của từng trò.
- **Bắn cá**: người chơi nhắm bắn cá trên màn hình để nhận phần thưởng.
- **Trò chơi P2P**: người chơi đối đầu với những người chơi khác thay vì với nhà cái.
- **Trò chơi nhanh**: các trò có vòng chơi ngắn và nhịp độ nhanh.
- **Xổ số**: người chơi chọn số rồi chờ kết quả quay thưởng.
- **Crash và instant**: các trò có kết quả nhanh, người chơi tự quyết định mức cược.

## Nhà cung cấp trò chơi trong sảnh
=== b17 ===
Các studio dưới đây cung cấp slot, trò chơi live và trò chơi bàn cho sảnh của Longfu 88, và mỗi tên được ghi đúng như trong danh sách nhà cung cấp, để người chơi dễ đối chiếu với các tựa slot đã nêu ở phần trước:

- Evolution
- Red Tiger
- NetEnt
- Big Time Gaming
- Pragmatic Play
- Yggdrasil
- SA Gaming
- Skywind
- Betsoft
- Hacksaw Gaming

## Bảng phương thức và hạn mức nạp tiền
Longfu88 chia phương thức nạp tiền thành sáu nhóm, trong đó MoMo, Zalo, ViettelPay và VietQR dùng VND.

| Loại phương thức | Ví dụ | Tiền tệ |
|---|---|---|
| Ví và mã QR cho Việt Nam | MoMo, Zalo, ViettelPay, VietQR | VND |
| Ngân hàng và ví khu vực | QRIS, DANA, DuitNow, PayNow | IDR, MYR, SGD |
| Thẻ | Visa, Mastercard | IDR, MYR, SGD, VND |
| Chuyển khoản ngân hàng | Bank Transfer | IDR, MYR, VND |
| Tiền mã hóa | Bitcoin, Ethereum, Litecoin, USDC, USDT trên ba mạng TRC20, ERC20, BEP20 | BTC, ETH, LTC, USDT, USDC |
| Ví quốc tế và châu Âu | Neteller, Skrill, Sofort, Giropay | EUR |

Mọi phương thức có mức nạp tối thiểu €10, tối đa €5.000 mỗi giao dịch và được cộng trong 1-2 phút, còn sòng bạc không thu phí xử lý, dù nhà cung cấp hoặc mạng blockchain có thể tính phí. Hạn mức có thể khác nhau theo quốc gia, tiền tệ và phương thức. Khoản nạp bằng Neteller và Skrill không được tính cho thưởng chào mừng. Quy trình gồm sáu bước: đăng nhập, mở quầy thu ngân và chọn Nạp tiền, chọn phương thức, nhập số tiền và thông tin, xác nhận theo hướng dẫn của nhà cung cấp, rồi chờ tiền vào số dư chơi.

### Rút tiền: các bước, thời gian và phí
Longfu88 cho rút tiền qua chuyển khoản ngân hàng, thẻ Visa và Mastercard, MoMo, DANA, Touch'n Go, tiền mã hóa (Bitcoin, Ethereum, Litecoin, USDT trên ba mạng) cùng DBS Bank và Online Banking, với mức tối thiểu €20 và tối đa €5.000.

1. Đăng nhập và mở quầy thu ngân.
2. Chọn Rút tiền và phương thức nhận tiền.
3. Nhập số tiền và thông tin nhận tiền.
4. Hoàn tất xác minh nếu được yêu cầu.
5. Xác nhận yêu cầu.
6. Chờ xử lý và tất toán trước khi nhận tiền.

Lngfu88 withdrawal time thường là tối đa 3 ngày làm việc: thẻ, tiền mã hóa và ví cần 1 đến 3 ngày, còn chuyển khoản ngân hàng cần thêm 3 đến 5 ngày để tất toán. Sòng bạc không thu phí rút tiền tiêu chuẩn, nhưng phí của nhà cung cấp và blockchain có thể phát sinh. Hoa hồng 10% (tối thiểu €2,25) có thể áp dụng khi doanh số cược thấp hơn khoản đã nạp, còn một số giao dịch nạp bằng thẻ hoặc chuyển khoản có thể chịu 15%.

---

## SECTION
Write the blocks b20, b21 in ONE answer, in this order. They are one continuous section of the page: the sub-sections continue the parent, so the text must flow from block to block without repeating itself. Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts.

---

## BLOCK BRIEF
Block: b20, H2 "Sports Betting Overview" (under H1 "Longfu88 casino: hướng dẫn đầy đủ dành cho người chơi Việt Nam")
Page heading (output language): "Tổng quan cá cược thể thao"
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): b21 H3 "Thưởng và tăng tỷ lệ cược thể thao"
Word Count: 112-144 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 144, but never beyond 172 words.
Format: paragraph. Visual Elements: None specified
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
- "Longfu sports": exactly 1 time(s)
Entities to cover [priority 1-10]:
- Sportsbook [10]
- Football [7]
- Esports [6]
- Live Betting [7]
- Bet Builder [5]
- Accumulator [5]
Entity Connections to state explicitly [priority]:
- Sportsbook → covers → football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football [8]
- Live Betting → offers → live odds and in-play markets [7]
Summary: The sportsbook: the sports and esports covered, the bet types and live betting.
Copywriter Notes: Give the nine sports and esports as listed (football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports, virtual football), the seven bet types (single, accumulator, live, handicap, totals, outrights, Bet Builder) and live betting with live odds and in-play markets. Where "Longfu sports" is used, write it as a natural phrase for the sports section (for example the Longfu sports section). Event availability and market selection can vary by jurisdiction. Name no sports league or event and no sportsbook platform. Use "Longfu88" exactly once and "Longfu sports" exactly once, and no other tracked keyword.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_sportsbook.sportsbook.sports_available: ["Football", "Basketball", "Tennis", "Badminton", "Cricket", "Table tennis", "Volleyball", "Esports", "Virtual football"]
- brandinfo_sportsbook.sportsbook.bet_types: ["Single", "Accumulator", "Live", "Handicap", "Totals", "Outrights", "Bet Builder"]
- brandinfo_sportsbook.sportsbook.live_betting: {"available": true, "features": ["Live odds", "In-play markets"]}
- brandinfo_sportsbook.sportsbook.important_terms: ["Event availability and market selection can vary by jurisdiction."]

---

## BLOCK BRIEF
Block: b21, H3 "Sports Bonuses and Boosts" (under H2 "Tổng quan cá cược thể thao")
Page heading (output language): "Thưởng và tăng tỷ lệ cược thể thao"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 86-109 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 109, but never beyond 130 words.
Format: paragraph + table. Visual Elements: Table — 7 of 8 tables on the page
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
- Sport First Deposit Bonus [10]
- Sports Cashback [7]
- Parlay Boost [6]
- Bet Builder Risk Free [5]
- Minimum Odds [6]
Entity Connections to state explicitly [priority]:
- Sport First Deposit Bonus → gives → 100% up to €1,888 [8]
- Qualifying Bets → need → minimum odds of 2.00 for singles [7]
Summary: The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
Copywriter Notes: Give a compact table Offer | Reward | Min. deposit | Wagering for the Sport First Deposit Bonus (100% up to €1,888, €50, 8x, 30 days), the Sport Weekly Reload Bonus (50% up to €2,500, €50, 8x) and the Sport Weekend Reload Bonus (50% up to €3,750, €50, 8x); then name the crypto equivalents, Sports Cashback (10% up to €2,500 of eligible sports net losses, weekly), Unlimited Sports Rebate (0.70%), 2 Goals Ahead early payout, Parlay Boost (up to 100% extra winnings, at least three legs) and Bet Builder Risk Free (50% stake return up to €250) in prose. Rules that apply: only settled qualifying sports bets count, single bets need odds of at least 2.00 and each accumulator selection at least 1.50, voided and cashed-out bets do not qualify. Do not mix these with the casino bonuses. Use no tracked keyword in the body of this block.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_sportsbook.sportsbook.sports_bonuses: [{"name": "Sport First Deposit Bonus", "reward": "100% up to €1,888", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Welcome Bonus", "reward": "100% up to 200 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Weekly Reload Bonus", "reward": "50% up to €2,500", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Weekend Reload Bonus", "reward": "50% up to €3,750", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Weekly Reload", "reward": "50% up to 500 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Sport Crypto Weekend Reload", "reward": "50% up to 1,000 USDT", "minimum_deposit": "20 USDT", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}, {"name": "Unlimited Sports Rebate", "reward": "0.70% of qualifying settled sports wagers", "wagering_requirement": "1x credited rebate", "crediting": "Daily"}, {"name": "Sports Cashback", "reward": "10% up to €2,500 of eligible sports net losses", "calculation_period": "Weekly", "wagering_requirement": "1x cashback", "eligibility": "Registered players with eligible real-money losing bets"}, {"name": "2 Goals Ahead - Early Payout", "reward": "Early settlement of eligible football bets when the selected team leads by two goals", "important_terms": ["Only participating pre-match match-winner markets qualify.", "Settlement is subject to published event eligibility."]}, {"name": "Parlay Boost", "reward": "Up to 100% extra winnings on qualifying accumulators", "minimum_legs": 3, "wagering_requirement": "No additional bonus wagering on settled enhanced winnings", "important_terms": ["Boost depends on the number of qualifying selections."]}, {"name": "Bet Builder Risk Free", "reward": "50% risk-free stake return up to €250", "eligibility": "Qualifying pre-match Bet Builder selections", "wagering_requirement": "1x credited free-bet stake", "validity": "7 days"}]
