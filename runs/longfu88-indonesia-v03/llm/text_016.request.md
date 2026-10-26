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
Country / GEO: Indonesia
Language: Indonesian (id). Write ONLY in this language.
Page intent: Brand-review page about the Longfu88 sportsbook and online casino for players from Indonesia, written for a bettor: the fact table, sports betting with markets, bet types and live betting, the sports bonuses, betting on mobile, registration and verification, payments, then the casino side with the welcome bonus, reloads and cashback, VIP levels, games and providers, licence and safety, responsible betting, support, pros and cons, an FAQ on sports and payouts and a verdict. Page voice: plain betting vocabulary, the reader is addressed as "you", sentences of about 17 words, every section starts with the market or the bet the reader makes and ends with the condition that decides the payout; paragraphs of two to four sentences; calls to action at the sports first deposit bonus and at the casino welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Indonesia.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Ulasan Sportsbook dan Kasino Longfu88 untuk Pemain Indonesia (102-128 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Indonesia.
b02   H2 Tabel Fakta Singkat (88-112 words): A fact sheet of the casino: operator, licence, Sports, Sports bonus, welcome bonus, cashback, minimum deposit, payment methods, currencies, languages, support.
b03   H2 Pasar Taruhan Olahraga (120-152 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b04     H3 Bonus untuk Taruhan Olahraga (94-120 words): The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
b05   H2 Taruhan dan Kasino di Ponsel (102-128 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b06   H2 Pendaftaran dan Login (181-231 words): Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes.
b07   H2 Pembayaran untuk Penaruh dan Pemain (261-334 words): Deposit methods by type with limits and speed in a table, the deposit route, then withdrawal methods, steps, timing and fees.
b08   H2 Penawaran Selamat Datang Kasino dan Syarat Taruhan (202-257 words): The Casino Welcome Bonus with its figures, claiming steps and alternatives, then the wagering, validity and bet limits in a table.
b09   H2 Level VIP (107-136 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b10   H2 Reload dan Cashback Kasino (181-231 words): The seven reload and seasonal offers in a table, then the weekly cashback with VIP rates, the live casino cashback and the rebates.
b11   H2 Lobi Kasino dan Slot (161-204 words): The nine game categories and three example slots with RTP, volatility and maximum multiplier.
b12   H2 Dealer Langsung, Permainan Lain, dan Studio (228-289 words): The live dealer section with the exclusive baccarat, the other game types and the ten providers.
b13   H2 Bertaruh dan Bermain dengan Lebih Aman (107-136 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b14   H2 Lisensi dan Keamanan (181-231 words): Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected.
b15   H2 Kelebihan dan Kekurangan bagi Penaruh (55-71 words): A pros and cons table built only from facts stated elsewhere on the page.
b16   H2 Opsi Kontak (74-94 words): Support channels, availability and languages.
b17   H2 Pertanyaan tentang Olahraga dan Akun (172-218 words): Short answers on the sports bonus, minimum deposit, withdrawal time, support languages, sports covered.
b18   H2 Kesimpulan untuk Penaruh (94-120 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Ulasan Sportsbook dan Kasino Longfu88 untuk Pemain Indonesia
Longfu88 adalah sportsbook sekaligus kasino online yang diluncurkan pada 2026. Taruhan olahraga menjadi pintu masuk pertama, sementara kasino online ini menggabungkan permainan kasino, dealer langsung, taruhan olahraga, dan lotere dalam satu akun. Lobinya terbagi ke sembilan kategori permainan: slot, dealer langsung, permainan meja, jackpot, fishing, permainan P2P, fast games, lotere, serta crash dan instant games. Ulasan ini ditulis untuk pemain dari Indonesia, dan pemain dewasa harus berusia minimal 18 tahun. Bagian berikutnya membahas fakta ringkas, lisensi, bonus, game, pembayaran, bermain lewat ponsel, dan bermain secara bertanggung jawab, sehingga pembaca bisa menimbang apakah penawarannya cocok dengan cara bertaruhnya sebelum setoran pertama. Urutannya mengikuti jalur penaruh: dari pasar olahraga ke akun, lalu ke sisi kasino.

## Tabel Fakta Singkat
=== b02 ===
| Parameter | Keterangan |
|---|---|
| Operator | Lumina |
| Lisensi | Kosta Rika, operator Lumina, nomor registrasi 000-039123-R-319326-001 |
| Olahraga | Sepak bola, bola basket, tenis, bulu tangkis, kriket, tenis meja, bola voli, esports, sepak bola virtual |
| Bonus olahraga | 100% hingga €1.888 |
| Bonus selamat datang | 188% hingga €2.088 + 18 Free Spins |
| Cashback | Hingga 10% dari kerugian bersih kasino mingguan |
| Setoran minimum | €10 |
| Metode pembayaran | QRIS, DANA, OVO Wallet, Mandiri, transfer bank, kartu Visa dan Mastercard, kripto Bitcoin |
| Mata uang | EUR, USD, MYR, THB, SGD, USDT |
| Bahasa dukungan | Inggris, Melayu, Mandarin Sederhana, Thai, Indonesia, Vietnam |
| Dukungan | support@longfu88.com, live chat 24/7 |

## Pasar Taruhan Olahraga
Sepak bola membuka daftar sembilan olahraga di sportsbook Longfu88. Daftar itu berlanjut ke bola basket, tenis, bulu tangkis, kriket, tenis meja, bola voli, esports, dan sepak bola virtual, sehingga penaruh yang tidak mengikuti sepak bola tetap menemukan pasar yang dikenal.

Ada tujuh jenis taruhan: single, accumulator, live, handicap, totals, outrights, dan Bet Builder. Single berisi satu pilihan dengan hitungan yang mudah, accumulator menggabungkan beberapa pilihan dalam satu taruhan, dan Bet Builder merangkai beberapa pasar dari satu pertandingan. Taruhan langsung memakai live odds dan pasar in-play, jadi odds bergerak mengikuti jalannya laga. Format ini cocok bagi penaruh yang lebih suka menonton jalannya pertandingan dulu, baru memilih pasar. Ketersediaan acara dan pilihan pasar dapat berbeda menurut yurisdiksi, sehingga pasar yang benar-benar tampil di akun menjadi patokan sebelum taruhan dipasang.

### Bonus untuk Taruhan Olahraga
Sport First Deposit Bonus memberi 100% hingga €1.888 pada setoran olahraga pertama, dan penawaran ini dipilih sebelum setoran atau lewat My Bonuses. Dua reload mingguan mengikuti polanya:

- **Sport First Deposit Bonus**: 100% hingga €1.888, setoran minimum €50, syarat putar 8x, berlaku 30 hari.
- **Sport Weekly Reload Bonus**: tambahan 50% hingga €2.500, setoran minimum €50, syarat putar 8x.
- **Sport Weekend Reload Bonus**: tambahan 50% hingga €3.750, setoran minimum €50, syarat putar 8x.

Pemain kripto memakai padanannya dalam USDT. Sports Cashback mengembalikan 10% hingga €2.500 dari kerugian bersih olahraga mingguan, Unlimited Sports Rebate memberi 0,70%, Parlay Boost menambah kemenangan hingga 100% untuk accumulator minimal tiga pilihan, dan Bet Builder Risk Free mengembalikan 50% taruhan hingga €250. Semua penawaran hanya menghitung taruhan settled: single butuh odds minimal 2,00, tiap pilihan accumulator minimal 1,50, dan taruhan void atau cash out tidak masuk hitungan.

## Taruhan dan Kasino di Ponsel
=== b05 ===
Taruhan olahraga dan putaran slot bisa dibuka dari layar ponsel, karena situs yang responsif berjalan di peramban smartphone maupun tablet, baik di Android, iOS, maupun web seluler. Dari sana tersedia kasino, sportsbook, akses akun, setoran, penarikan, dan bonus. Longfu88 app adalah versi situs ini yang disimpan sebagai pintasan di layar utama, sehingga kasino dan sportsbook terbuka dengan satu ketukan.

Di Android, pintasan dibuat dalam tiga langkah:

1. Buka Longfu88 di Chrome.
2. Buka menu peramban dan pilih Add to Home screen.
3. Konfirmasikan pintasan.

Di iOS, urutannya serupa lewat Safari:

1. Buka Longfu88 di Safari.
2. Ketuk Share dan pilih Add to Home Screen.
3. Konfirmasikan dengan Add.

## Pendaftaran dan Login
=== b06 ===
Akun harus ada sebelum taruhan pertama dipasang, dan pendaftaran lewat email meminta email, kata sandi, nama lengkap sesuai identitas, tanggal lahir, serta alamat tempat tinggal. Lima langkahnya berurutan:

1. Buka Longfu88 dan pilih Register.
2. Masukkan email dan buat kata sandi.
3. Konfirmasikan usia serta persetujuan atas Syarat dan Ketentuan dan Kebijakan Privasi.
4. Lengkapi data pribadi tambahan dan alamat tempat tinggal.
5. Pilih Create Account dan selesaikan konfirmasi email jika diminta.

Setiap pemain hanya boleh memegang satu akun pribadi. Proses Longfu88 login dimulai dengan memilih Login di situs, mengisi email dan kata sandi terdaftar, lalu menyelesaikan pemeriksaan keamanan bila muncul. Pemain yang mencari Longfu caino login cukup memilih Login di situs yang sama. Kata sandi yang terlupa dipulihkan lewat Forgot Password di layar login: tautan reset dikirim ke email terdaftar, dan kata sandi baru diatur mengikuti petunjuk di email tersebut.

Verifikasi identitas (KYC) dapat diminta sebelum penarikan, pada transaksi yang tidak biasa atau bernilai besar, dan ketika data akun atau pembayaran berubah. Dokumen yang umum diminta:

- Identitas: paspor, kartu identitas nasional, atau SIM.
- Bukti alamat: tagihan utilitas atau rekening koran.
- Bukti kepemilikan metode pembayaran.
- Sumber dana, jika diminta.

Dokumen dikirim dalam waktu hingga 30 hari sejak diminta, dan satu set dokumen yang lengkap ditinjau dalam waktu hingga 10 hari. Penarikan dapat ditahan sampai pemeriksaan selesai, sedangkan pemeriksaan yang gagal bisa berujung pada penolakan transaksi atau pembatasan akun.

## Pembayaran untuk Penaruh dan Pemain
=== b07 ===
Setoran menentukan seberapa cepat taruhan pertama bisa dipasang. Untuk pemain Indonesia, QRIS, DANA, OVO Wallet, Mandiri, BNI, dan BCA (IDR) menjadi pilihan utama dari enam kelompok metode.

| Jenis metode | Contoh | Mata uang |
|---|---|---|
| Bank dan dompet lokal | QRIS, DANA, OVO Wallet, Mandiri, BNI, BCA | IDR |
| Kartu | Visa, Mastercard | IDR, MYR, SGD, VND |
| Transfer bank | Bank Transfer | IDR, MYR, VND |
| Kripto | Bitcoin, Ethereum, Litecoin, USDT di jaringan TRC20, ERC20, dan BEP20, serta USDC | BTC, ETH, LTC, USDT, USDC |
| Dompet elektronik | Neteller, Skrill | EUR |
| Metode Eropa | Sofort, Giropay | EUR |

Batas umum berlaku untuk semua metode: setoran minimum €10 dan maksimum €5.000 per transaksi, dengan dana masuk dalam 1 sampai 2 menit. Kasino tidak memungut biaya pemrosesan, tetapi biaya penyedia pembayaran atau jaringan blockchain dapat berlaku. Batas bisa berbeda menurut negara, mata uang, dan metode, dan setoran Neteller serta Skrill tidak termasuk bonus selamat datang. Setoran dimulai dengan masuk ke akun Longfu88, membuka kasir, dan memilih Deposit. Setelah itu pemain memilih metode dengan mata uang atau jaringan yang didukung, mengisi jumlah dan data pembayaran, mengonfirmasi transaksi sesuai petunjuk penyedia, lalu menunggu dana masuk ke saldo permainan.

Penarikan tersedia lewat transfer bank, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT di tiga jaringan (TRC20, ERC20, BEP20), Touch'n Go, DANA, MoMo, DBS Bank, dan Online Banking, dengan minimum €20 dan maksimum €5.000. Enam langkahnya berurutan:

1. Masuk ke akun dan buka kasir.
2. Pilih Withdrawal, lalu tentukan tujuan atau metode pembayaran yang didukung.
3. Isi jumlah serta bank, dompet, atau alamat blockchain penerima.
4. Selesaikan verifikasi identitas dan metode pembayaran jika diminta.
5. Periksa permintaan dan konfirmasikan pengiriman.
6. Tunggu pemrosesan kasino dan penyelesaian bank atau jaringan sebelum dana diterima.

Soal Lngfu88 withdrawal time, penarikan lewat kartu, kripto, dan dompet digital memakan 1 sampai 3 hari kerja, sedangkan transfer bank membutuhkan hingga 3 hari kerja pemrosesan kasino ditambah 3 sampai 5 hari kerja pengiriman bank. Permintaan umumnya diproses dalam tiga hari kerja, dan pemeriksaan identitas dapat menunda pembayaran. Kasino tidak memungut biaya penarikan standar, tetapi biaya penyedia dan blockchain dapat berlaku. Komisi 10% (minimum €2,25) dapat dikenakan bila turnover lebih kecil daripada jumlah setoran, karena turnover setoran minimal 1x dapat diminta sebelum penarikan. Sebagian transaksi yang didanai kartu atau transfer bank dapat dikenai 15%.

## Penawaran Selamat Datang Kasino dan Syarat Taruhan
=== b08 ===
Sisi kasino dibuka dengan penawaran terpisah dari bonus olahraga. Longfu88 bonus bernama Casino Welcome Bonus memberi 188% hingga €2.088 plus 18 Free Spins, yaitu putaran slot dengan taruhan yang dibayar kasino. Penawaran ini untuk pemain baru yang mendaftar di Longfu88 dan melakukan setoran pertama yang memenuhi syarat, dengan satu penawaran selamat datang per akun. Setoran minimum khusus bonus ini €50. Jalur klaimnya adalah aktivasi di My Bonuses setelah setoran tersebut, dan Longfu88 promo code bukan bagian dari prosedur klaim yang tercantum.

- Daftarkan akun dan lengkapi data pribadi yang diminta.
- Lakukan setoran pertama yang memenuhi syarat.
- Aktifkan Casino Welcome Bonus di My Bonuses sebelum memasang taruhan apa pun.
- Mainkan game kasino yang memenuhi syarat dan selesaikan wagering sebelum bonus kedaluwarsa.

Daftar, setor, lalu aktifkan paketnya di My Bonuses sebelum bermain. Dua alternatif untuk setoran pertama adalah Live Casino Welcome Bonus (125% hingga €888, setoran minimum €30) dan Casino Crypto Welcome Bonus (188% hingga 2.888 USDT, setoran minimum 50 USDT), dan keduanya bersama Casino Welcome Bonus saling menggantikan.

Wagering sebesar 25 kali setoran plus jumlah bonus harus selesai selama masa berlaku, sedangkan kemenangan Free Spins punya syarat putar sendiri. Angka lengkapnya:

| Syarat | Nilai |
|---|---|
| Wagering | 25x setoran plus bonus |
| Wagering Free Spins | 40x kemenangan Free Spins |
| Masa berlaku | 10 hari sejak aktivasi |
| Taruhan maksimum | €22,5 per putaran |
| Cashout maksimum | 5x jumlah bonus awal |

Setoran Neteller dan Skrill dikecualikan, dan hanya satu bonus promosi yang boleh aktif pada satu waktu. Permintaan penarikan sebelum klaim atau saat bonus aktif dapat membatalkan kelayakan, sementara pembatalan menghanguskan dana bonus dan kemenangan promosi yang belum dikonversi. Verifikasi akun mungkin diminta sebelum kemenangan bonus dibayarkan.

## Level VIP
=== b09 ===
Poin VIP dikumpulkan dari permainan uang sungguhan yang memenuhi syarat, dan poin itu membuka level hadiah bernomor. Longfu88 VIP Program memiliki 25 level yang dikelompokkan ke lima tier: Bronze, Silver, Gold, Platinum, dan Diamond. Level 1 membutuhkan 1 poin dan memberi hadiah €9,8, cashback 1%, serta batas penarikan €9.800. Level 25 membutuhkan 5.500 poin, dengan hadiah €980, cashback 10%, dan batas penarikan €147.000. Level yang lebih tinggi menambah penawaran personal, cashback, batas penarikan yang lebih besar, dan manajer VIP pribadi mulai level 4, sehingga program ini lebih relevan bagi pemain yang bermain dalam volume tinggi dan konsisten. Hadiah dan batas penarikan dapat berbeda menurut level VIP dan mata uang, dan aturan program dapat berubah.

## Reload dan Cashback Kasino
=== b10 ===
Reload di Longfu88 dan promosi musiman datang terbagi ke tujuh penawaran.

| Penawaran | Hadiah | Setoran minimum | Wagering | Masa berlaku |
|---|---|---|---|---|
| Casino Weekly Reload | 50 Free Spins | €30 | 40x kemenangan Free Spins | 7 hari |
| Casino Weekly Crypto Reload | 60% hingga 1.000 USDT | 20 USDT | 30x setoran plus bonus | 7 hari |
| Casino Weekend Reload | Hingga €3.360 + 50 Free Spins | €50 | 30x setoran plus bonus, 40x kemenangan Free Spins | 7 hari |
| Casino Weekend Crypto Reload | 75% hingga 750 USDT + 100 Free Spins | 20 USDT | 30x setoran plus bonus, 40x kemenangan Free Spins | 7 hari |
| Casino Double Fortune (reload sehari) | 50% hingga €500 | €30 | 30x setoran plus bonus | 24 jam |
| Casino Trick or Treat Pumpkin Bonanza (promosi musiman) | Hingga 100 Free Spins | €20 | 40x kemenangan Free Spins | 7 hari |
| Casino Dragon Quest (hadiah verifikasi) | Kredit bonus €10 | €20 | 30x kredit promosi | 7 hari |

Semua penawaran diaktifkan di My Bonuses, hanya bisa diklaim sekali per periode promosi, dan tidak dapat digabung dengan bonus kasino aktif lain. Taruhan maksimum saat memutar dana bonus adalah €5 per putaran.

Casino Weekly Cashback mengembalikan hingga 10% dari kerugian bersih kasino mingguan, dengan batas €6.988. Periodenya Senin 00:00 UTC sampai Minggu 23:59 UTC, pemain ikut untuk siklus empat minggu, dan cashback masuk ke My Bonuses pada hari Senin dengan wagering 10x. Persentasenya mengikuti tier VIP: Bronze 2% (maksimum €1.888), Silver 4% (€2.388), Gold 6% (€2.988), Platinum 8% (€3.988), dan Diamond 10% (€6.988). Live Casino Cashback memberi 25% hingga €850. Rebate dikreditkan setiap hari: kasino 0,9%, live casino 1,0%, P2P 0,8%, dan lotere 1,0%, masing-masing dengan wagering 1x. Hanya taruhan uang sungguhan yang dihitung, sedangkan dana bonus tidak.

## Lobi Kasino dan Slot
=== b11 ===
Longfu 88 Casino menawarkan sembilan kategori permainan: slot, dealer langsung, permainan meja, jackpot, fishing, permainan P2P, fast games, lotere, serta crash dan instant games. Slot dibahas lebih dulu karena angka seperti RTP dan volatilitas paling mudah dibandingkan di sana, sedangkan live casino dan kategori lainnya menyusul di bagian berikutnya.

RTP adalah persentase taruhan yang secara teoretis kembali ke pemain dalam jangka panjang. Volatilitas menunjukkan seberapa sering dan seberapa besar pembayaran terjadi: makin tinggi, makin jarang pembayarannya, tetapi umumnya makin besar. Tiga contoh di Longfu88 memperlihatkan perbedaannya. Gates of Olympus dari Pragmatic Play memiliki RTP 96,50%, volatilitas tinggi, dan pengali maksimum 5.000x. Sweet Bonanza, juga dari Pragmatic Play, memiliki RTP 96,48%, volatilitas tinggi, dan pengali maksimum 21.175x. Wanted Dead or a Wild dari Hacksaw Gaming memiliki RTP 96,38%, volatilitas sangat tinggi, dan pengali maksimum 12.500x. Ketiganya hanya contoh, bukan daftar lengkap, dan pengali maksimum adalah batas teoretis, bukan hasil yang bisa diharapkan di setiap putaran. Bagi pemain yang baru mengenal slot, RTP dan volatilitas berguna sebagai pembanding sebelum menentukan besar taruhan, sebab volatilitas tinggi berarti saldo bergerak lebih tajam.

## Dealer Langsung, Permainan Lain, dan Studio
=== b12 ===
Dealer langsung adalah kategori lobi tempat ronde dipimpin dealer sungguhan lewat siaran video, dan di sinilah Longfu88 Baccarat berada, game eksklusif live atau meja dengan permainan baccarat. Sisi live ditenagai antara lain oleh studio Evolution dan SA Gaming, dua nama dari daftar penyedia kasino. Format ini cocok bagi pemain yang ingin merasakan ritme meja sungguhan, sebab ronde berjalan mengikuti dealer, bukan mengikuti kecepatan pemain.

Kategori lain punya cara main yang berbeda. Permainan meja adalah game kartu dan roda yang dimainkan melawan rumah. Fishing meminta pemain membidik target di layar, sedangkan permainan P2P mempertemukan pemain satu sama lain, bukan dengan rumah. Fast games berjalan dalam ronde pendek, lotere bertumpu pada undian angka, dan crash serta instant games memberi hasil cepat dalam satu ronde. Dengan begitu kasino online ini juga melayani pemain yang lebih suka ritme singkat daripada putaran slot. Bagi pemain di Longfu 88, ragam ini berarti pilihan tidak berhenti di slot dan sportsbook.

Pasokan game datang dari Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft, dan Hacksaw Gaming. Para penyedia ini memasok slot, game live, dan game meja ke kasino. Pragmatic Play memasok Gates of Olympus dan Sweet Bonanza, sedangkan Hacksaw Gaming memasok Wanted Dead or a Wild, tiga contoh slot yang sudah dibahas di atas. Nama studio membantu pemain menyaring lobi: pencari meja live bisa memulai dari Evolution atau SA Gaming, sementara pencari slot dapat memeriksa judul dari Pragmatic Play atau Hacksaw Gaming.

## Bertaruh dan Bermain dengan Lebih Aman
=== b13 ===
Bertaruh hanya untuk pemain berusia minimal 18 tahun dan hanya di tempat yang mengizinkannya secara hukum. Pemain yang merasa taruhannya mulai tidak terkendali dapat meminta pengecualian diri lewat email ke dukungan pelanggan di support@longfu88.com. Akses akun dan permainan dapat dibatasi selama periode yang disepakati, dan pembatasan berlaku dalam 24 jam setelah permintaan diproses. Penutupan akun juga diminta lewat dukungan pelanggan. Prosedurnya empat langkah: menghubungi dukungan, mengonfirmasi data akun dan ketentuan pengecualian yang diinginkan, membiarkan kasino membatasi atau menutup akses, lalu mencari bantuan independen bila perlu. Pertanyaan penilaian diri membantu mengenali kemungkinan kerugian akibat berjudi sejak awal. Halaman ini tidak menggantikan bantuan independen, yang tersedia dari:

- GamCare
- Gamblers Anonymous
- Gambling Therapy

## Lisensi dan Keamanan
=== b14 ===
Kasino online ini diluncurkan pada 2026 dan membuka akun dalam mata uang EUR, USD, MYR, THB, SGD, dan USDT. Pemain sebaiknya memakai alamat Longfu 88 Official Site dan menghindari halaman tiruan. Syarat bermainnya jelas: usia minimal 18 tahun, izin berjudi secara hukum di tempat tinggal, data pendaftaran yang akurat, satu akun pribadi, dan tanpa metode pembayaran milik pihak ketiga. Memastikan izin tersebut menjadi tanggung jawab pemain sendiri. Data yang akurat sejak awal juga memperkecil kemungkinan penarikan tertahan karena pemeriksaan, sehingga alamat dan data pendaftaran layak dicek sebelum setoran pertama.

Soal lisensi, casino Longfu88 mencantumkan yurisdiksi Kosta Rika, operator Lumina, dan nomor registrasi 000-039123-R-319326-001. Pernyataan itu satu-satunya informasi lisensi di halaman ini, dan lisensi tersebut dipegang oleh operator yang sama dengan pengendali data pribadi. Petugas perlindungan data dapat dihubungi lewat dpo@longfu88.com. Akun, pembayaran, dan data pribadi dilindungi dengan pengamanan teknis dan organisasi.

Data dapat dibagikan kepada penyedia layanan pembayaran, penyedia verifikasi identitas, penyedia teknologi, serta regulator dan penegak hukum bila diwajibkan. Pemain berhak atas akses, perbaikan, penghapusan jika diizinkan hukum, pembatasan, keberatan, portabilitas bila berlaku, dan penarikan persetujuan. Pemegang akun bertanggung jawab menjaga kredensial, sedangkan operator dapat menangguhkan aktivitas untuk verifikasi atau dugaan penyalahgunaan.

## Kelebihan dan Kekurangan bagi Penaruh
=== b15 ===
| Kelebihan | Kekurangan |
|---|---|
| Setoran minimum umum hanya €10 | Bonus selamat datang membutuhkan setoran €50 |
| Banyak metode pembayaran, termasuk kripto | Wagering 25x setoran plus bonus |
| Cashback mingguan hingga 10% | Komisi 10% atau 15% dapat dikenakan pada penarikan menurut aturan turnover |
| Program VIP dengan 25 level | Penarikan bank bisa memakan beberapa hari kerja |
| Live chat 24/7 | Verifikasi dapat menunda pembayaran pertama |

## Opsi Kontak
=== b16 ===
Pertanyaan soal taruhan yang belum jelas atau setoran yang belum masuk dapat langsung diajukan lewat live chat, yang tersedia 24/7. Jalur kedua adalah email ke support@longfu88.com, yang lebih cocok untuk urusan yang membutuhkan penjelasan tertulis, seperti pengecualian diri, penutupan akun, atau petunjuk verifikasi. Dukungan pelanggan melayani dalam bahasa Inggris, Melayu, Mandarin Sederhana, Thai, Indonesia, dan Vietnam, sehingga pemain dari Indonesia dapat menulis dalam bahasanya sendiri dan mendapat jawaban yang mudah diikuti. Menyiapkan email terdaftar dan rincian masalah sebelum menghubungi dukungan membuat permintaan lebih mudah dijelaskan.

---

## BLOCK BRIEF
Block: b17, H2 "Sports and Account Questions" (under H1 "Ulasan Sportsbook dan Kasino Longfu88 untuk Pemain Indonesia")
Page heading (output language): "Pertanyaan tentang Olahraga dan Akun"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 172-218 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 218, but never beyond 261 words.
Format: list. Visual Elements: Bulleted/numbered list — 7 of 7 lists on the page
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu caino login": 0 (do not use)
- "Longfu88 bonus": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 app": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu88 promo code": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu 88 casino": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "casino Longfu88": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Lngfu88 withdrawal time": 0 (do not use)
- "Longfu 88 Official Site": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Longfu": 0 (do not use)
- "Longfu sports": exactly 1 time(s)
Entities to cover [priority 1-10]:
- Frequently Asked Questions [8]
- The sports bonus [6]
- Minimum deposit [6]
- Withdrawal time [6]
- Support languages [6]
Entity Connections to state explicitly [priority]:
- Frequently Asked Questions → cover → the sports bonus, minimum deposit, withdrawal time, support languages, sports covered [6]
Summary: Short answers on the sports bonus, minimum deposit, withdrawal time, support languages, sports covered.
Copywriter Notes: A bulleted list of exactly 5 items, each a bold question followed by a short answer of 20-30 words, in this order: (1) what the first sports deposit bonus is (Sport First Deposit Bonus, 100% up to €1,888, minimum deposit €50, 8x wagering, 30 days); (2) what the minimum deposit is (€10 in general, €50 for the Casino Welcome Bonus); the answer contains the keyword "Longfu88" exactly once, written verbatim; (3) how long a withdrawal takes (card, crypto and wallet withdrawals 1 to 3 business days; bank transfer up to 3 business days of casino processing plus 3 to 5 business days of bank delivery; the wording must differ from the withdrawals section); (4) which languages support speaks (English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese); (5) which sports can be bet on (football, basketball, tennis, badminton, cricket, table tennis, volleyball, esports and virtual football); the question contains the keyword "Longfu sports" exactly once, written verbatim. The brand name "Longfu88" may stand in an answer, never in a question. These are the only questions on the page; the questions are the one place where question form is allowed. Use "Longfu88" exactly once and "Longfu sports" exactly once, and no other tracked keyword.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_general.minimum_deposit: €10
- brandinfo_sportsbook.sportsbook.sports_bonuses[0]: {"name": "Sport First Deposit Bonus", "reward": "100% up to €1,888", "minimum_deposit": "€50", "wagering_requirement": "8x deposit plus bonus", "validity": "30 days", "claiming_method": "Select the offer before the qualifying sports deposit or from My Bonuses.", "important_terms": ["Only settled qualifying sports bets contribute to wagering.", "Qualifying single bets must have odds of at least 2.00; each accumulator selection at least 1.50.", "Voided and cashed-out bets do not qualify.", "One claim per stated promotional period."]}
- brandinfo_welcome.welcome_bonus.minimum_deposit: €50
- brandinfo_withdrawal.withdrawal_methods[0].transaction_speed: Up to 3 business days for casino processing; bank delivery may require 3–5 additional business days
- brandinfo_withdrawal.withdrawal_methods[1].transaction_speed: 1–3 business days
- brandinfo_general.customer_support.languages: ["English", "Malay", "Simplified Chinese", "Thai", "Indonesian", "Vietnamese"]
- brandinfo_sportsbook.sportsbook.sports_available: ["Football", "Basketball", "Tennis", "Badminton", "Cricket", "Table tennis", "Volleyball", "Esports", "Virtual football"]
