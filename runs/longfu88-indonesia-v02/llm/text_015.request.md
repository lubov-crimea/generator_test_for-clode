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
Page intent: Detailed brand-review page about the Longfu88 online casino for players from Indonesia, written for a careful reader: who runs the casino and under which licence, the fact sheet, registration with account security and verification, the responsible-gambling tools, the welcome bonus with its terms, other promotions and VIP limits, payments with withdrawal timing, the game library, providers, the sportsbook, mobile access, support, a pros and cons table, an FAQ and a closing checklist. Page voice: precise and calm, sentences of about 20 words with a few short ones, paragraphs of three to four sentences; every advantage is followed by the condition or limit that goes with it, stated in the same detail as the advantage; a fact is followed by what it means in practice; one call to action only, at the welcome bonus. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Indonesia.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 casino Indonesia: ulasan keamanan, syarat, dan kontrol (126-161 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Indonesia.
b02   H2 Operator, lisensi, dan pengelolaan data (212-270 words): Launch year, currencies and who may play, then the licence, the operator, the data controller and how data and accounts are protected.
b03   H2 Data resmi brand (95-121 words): A fact sheet of the casino: licence, operator, Minimum age, launch year, currencies, languages, payment methods, minimum deposit, welcome bonus, cashback, Verification time, support.
b04   H2 Pendaftaran dan login yang aman (123-157 words): How to open an account by e-mail in five numbered steps, the required details, the one-account rule, login and password recovery.
b05     H3 Cara kerja verifikasi dan dokumen yang dibutuhkan (139-177 words): When the casino asks for verification, which documents are accepted, the deadline to send them, the review time and what happens if checks fail.
b06   H2 Judi bertanggung jawab: self-exclusion dan bantuan (123-157 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b07   H2 Penawaran selamat datang dan syaratnya (160-203 words): The Casino Welcome Bonus: percentage, maximum amount, free spins, qualifying deposit, who can claim it and the four claiming steps, plus the two alternative first-deposit offers.
b08     H3 Wagering, batas, dan pengecualian (112-144 words): The terms of the Casino Welcome Bonus in a table, with the exclusions and what they mean in practice.
b09   H2 Level VIP dan batas yang lebih tinggi (120-152 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b10   H2 Reload dan promosi musiman beserta aturannya (133-168 words): The recurring reload offers and special campaigns in a comparison table (reward, minimum deposit, wagering, validity) with the shared rules.
b11     H3 Syarat cashback (87-110 words): Weekly and live casino cashback with the VIP rates, and the daily rebates by game category.
b12   H2 Metode deposit dan batasnya (139-177 words): Deposit methods grouped by type with the general limits and speed, the local options for Indonesia and the six-step deposit route.
b13     H3 Penarikan dana: waktu, biaya, dan turnover (133-168 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b14   H2 Permainan yang tersedia (87-110 words): The size of the lobby in categories: slots, live dealer, table games, jackpots, fishing, P2P, fast games, lottery and crash and instant games.
b15     H3 Slot: RTP dan volatilitas (106-135 words): Three example slots with their provider, RTP, volatility and maximum multiplier.
b16     H3 Permainan live dealer (93-119 words): The live dealer section: what it offers, the exclusive baccarat game and the live studios among the providers.
b17   H2 Penyedia permainan (80-100 words): Which studios supply the games, named from the provider list.
b18   H2 Bermain lewat ponsel (106-134 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b19   H2 Pasar taruhan olahraga dan aturannya (112-144 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b20     H3 Promosi olahraga (87-110 words): The sportsbook offers: first deposit bonus, weekly and weekend reloads, cashback, early payout, parlay boost and risk-free bet builder, with the shared odds rule.
b21   H2 Kelebihan dan batasan (55-69 words): A pros and cons table built only from facts stated elsewhere on the page.
b22   H2 Saluran dukungan dan bahasa (80-100 words): Support channels, availability and languages.
b23   H2 Pertanyaan seputar verifikasi dan pembayaran (172-218 words): Short answers on one account, withdrawal fees, withdrawal time, who may play, verification time.
b24   H2 Sebelum melakukan deposit (106-134 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 casino Indonesia: ulasan keamanan, syarat, dan kontrol
Longfu88 adalah kasino online yang menggabungkan permainan kasino, live dealer, taruhan olahraga, dan lotere dalam satu akun. Lobinya terbagi menjadi sembilan kategori permainan: slot, live dealer, permainan meja, jackpot, fishing, permainan P2P, fast games, lotere, serta crash dan instant games. Di samping lobi tersebut tersedia sportsbook untuk taruhan olahraga. Kasino ini diluncurkan pada 2026, sehingga riwayat operasinya masih singkat.

Halaman ini ditulis untuk pemain dari Indonesia yang ingin menilai kasino secara teliti sebelum mendaftar. Pemain dewasa harus berusia minimal 18 tahun, dan batas itu berlaku untuk seluruh layanan. Ulasan berikut membahas data resmi dan lisensi, bonus beserta syaratnya, permainan, pembayaran, akses lewat ponsel, serta alat judi bertanggung jawab. Setiap kelebihan dijelaskan bersama syarat yang menyertainya, sehingga pembaca dapat menimbang tawaran dengan tenang. Tidak ada hasil permainan yang dapat dipastikan, dan perjudian bukan sumber penghasilan.

## Operator, lisensi, dan pengelolaan data
Longfu88 diluncurkan pada 2026 dan menerima akun dalam enam mata uang: EUR, USD, MYR, THB, SGD, dan USDT. Daftar ini penting dicermati sejak awal, karena mata uang akun sebaiknya sesuai dengan metode pembayaran yang akan dipakai. Pemain sebaiknya hanya membuka alamat Longfu 88 Official Site dan menjauhi halaman tiruan, sebab data akun serta pembayaran baru terlindungi bila diakses lewat situs yang benar. Syarat bermain cukup tegas. Pemain harus berusia minimal 18 tahun, secara hukum diperbolehkan berjudi di tempat tinggalnya, mendaftar dengan data yang akurat, memakai satu akun pribadi, dan tidak memakai metode pembayaran milik pihak ketiga. Aturan terakhir berarti rekening atau dompet digital yang dipakai harus atas nama pemilik akun.

Soal lisensi, casino Longfu88 mencantumkan yurisdiksi Costa Rica. Lisensi itu dipegang oleh operator Lumina dengan nomor registrasi 000-039123-R-319326-001, dan hanya itu yang tercatat tentang lisensi. Pemain dari Indonesia tetap perlu memeriksa sendiri aturan perjudian di wilayah tempat tinggalnya.

Lumina juga bertindak sebagai pengendali data, jadi pemegang lisensi dan pihak yang mengelola data pemain adalah entitas yang sama. Operator melindungi akun, pembayaran, dan informasi pribadi dengan pengamanan teknis dan organisasi. Data dapat dibagikan kepada penyedia layanan pembayaran, penyedia verifikasi identitas, penyedia teknologi, serta regulator dan penegak hukum bila diwajibkan. Pemain memiliki hak akses, koreksi, penghapusan sejauh diizinkan hukum, pembatasan, keberatan, portabilitas bila berlaku, dan penarikan persetujuan. Pemegang akun bertanggung jawab menjaga kredensialnya, sedangkan operator dapat menangguhkan aktivitas untuk keperluan verifikasi atau bila ada dugaan penyalahgunaan.

## Data resmi brand
| Parameter | Keterangan |
|---|---|
| Lisensi kasino | Yurisdiksi di Costa Rica, dipegang operator Lumina dengan nomor registrasi 000-039123-R-319326-001 |
| Operator kasino | Lumina |
| Usia minimum pemain | 18 tahun |
| Tahun peluncuran | 2026 |
| Mata uang akun | EUR, USD, MYR, THB, SGD, USDT |
| Bahasa layanan dukungan | Inggris, Melayu, Mandarin Sederhana, Thai, Indonesia, Vietnam |
| Metode pembayaran deposit | QRIS, DANA, OVO Wallet, Visa, Mastercard, Bank Transfer, Bitcoin, USDT |
| Deposit minimum umum | €10 |
| Bonus selamat datang kasino | 188% hingga €2.088 + 18 Free Spins |
| Cashback kasino | Hingga 10% dari kerugian bersih kasino per minggu |
| Waktu peninjauan verifikasi | Hingga 10 hari setelah dokumen lengkap diterima |
| Kontak dukungan | Alamat e-mail support@longfu88.com serta live chat yang aktif 24/7 |

## Pendaftaran dan login yang aman
Pendaftaran di Longfu88 memakai e-mail dan memerlukan alamat e-mail, kata sandi, nama legal, tanggal lahir, serta alamat tempat tinggal. Lima langkahnya berurutan:

1. Buka situs dan pilih Register.
2. Masukkan e-mail dan buat kata sandi.
3. Konfirmasi usia serta persetujuan terhadap Syarat dan Ketentuan dan Kebijakan Privasi.
4. Lengkapi data pribadi tambahan dan alamat tempat tinggal.
5. Pilih Create Account, lalu selesaikan konfirmasi e-mail bila diminta.

Setiap pemain hanya boleh memegang satu akun pribadi, jadi data yang dimasukkan harus akurat sejak awal. Proses Longfu88 login sendiri singkat: pemain memilih Login di situs, mengisi e-mail dan kata sandi terdaftar, lalu menyelesaikan pemeriksaan keamanan bila muncul. Pemain yang mencari halaman Longfu caino login sebaiknya memastikan alamat situsnya benar sebelum mengisi data apa pun. Bila kata sandi terlupa, pilih Forgot Password di layar login, minta tautan reset lewat e-mail terdaftar, lalu ikuti petunjuk di e-mail untuk menetapkan kata sandi baru.

### Cara kerja verifikasi dan dokumen yang dibutuhkan
Verifikasi KYC, yaitu pemeriksaan identitas pemain oleh operator, dapat diminta saat peninjauan akun, sebelum penarikan, pada transaksi tidak biasa atau bernilai tinggi, dan ketika data akun atau pembayaran berubah. Longfu88 memberi waktu hingga 30 hari untuk mengirim dokumen setelah diminta. Dokumen harus terbaca, masih berlaku, dan sesuai dengan profil akun, dan verifikasi tambahan lewat telepon atau wajah dapat diminta. Penarikan dapat ditahan sampai pemeriksaan selesai, sedangkan set dokumen yang lengkap ditinjau dalam waktu hingga 10 hari. Karena itu, pemain yang berencana menarik dana sebaiknya menyiapkan dokumen lebih awal dan mengirimkannya sekaligus, bukan satu per satu. Bila pemeriksaan gagal, transaksi dapat ditolak, akun dibatasi, atau penarikan ditahan sampai kepatuhan terpenuhi. Dokumen yang diterima:

- Dokumen identitas: paspor, kartu identitas nasional, atau SIM
- Bukti alamat: tagihan utilitas atau rekening koran bank
- Bukti kepemilikan metode pembayaran: kartu, rekening bank, atau dompet digital
- Bukti sumber dana bila diminta: bukti penghasilan, rekening koran, atau dokumen keuangan pendukung lain

## Judi bertanggung jawab: self-exclusion dan bantuan
Pemain harus berusia minimal 18 tahun dan berjudi hanya di tempat yang mengizinkannya. Pemain yang merasa kendalinya melemah dapat meminta self-exclusion lewat e-mail ke dukungan pelanggan di support@longfu88.com. Permintaan itu membatasi akses akun dan aktivitas berjudi selama jangka waktu yang disepakati, dan pembatasan diterapkan dalam 24 jam setelah permintaan diproses. Penutupan akun juga diajukan lewat dukungan pelanggan. Prosedurnya terdiri dari empat langkah: menghubungi dukungan, mengonfirmasi data akun beserta ketentuan pengecualian yang diinginkan, memberi kasino waktu untuk membatasi atau menutup akses, lalu mencari bantuan independen bila perlu. Pertanyaan penilaian diri (self-assessment) membantu pemain mengenali kemungkinan kerugian akibat berjudi, sehingga lebih baik dijawab sebelum masalahnya membesar. Contoh tandanya adalah bermain lebih lama atau bertaruh lebih besar daripada rencana semula. Halaman ini tidak dapat menggantikan bantuan independen, yang tersedia dari organisasi berikut:

- GamCare
- Gamblers Anonymous
- Gambling Therapy

## Penawaran selamat datang dan syaratnya
Casino Welcome Bonus diaktifkan lewat My Bonuses setelah deposit pertama yang memenuhi syarat dan sebelum taruhan apa pun dipasang. Prosedur klaim yang tercantum tidak memuat langkah Longfu88 promo code, sehingga pemain tidak perlu mencari kode untuk mengklaimnya. Paket Longfu88 bonus ini memberi 188% hingga €2.088 ditambah 18 Free Spins, yaitu putaran gratis pada slot dengan taruhan yang ditanggung kasino. Penawaran ditujukan bagi pemain baru yang sudah terdaftar di Longfu88 dan berlaku untuk deposit pertama yang memenuhi syarat, dengan satu penawaran selamat datang per akun. Deposit minimum khusus bonus ini adalah €50, sehingga setoran yang lebih kecil tidak memenuhi syarat. Dua penawaran lain menjadi alternatif deposit pertama: Live Casino Welcome Bonus (125% hingga €888, deposit minimum €30) dan Casino Crypto Welcome Bonus (188% hingga 2.888 USDT, deposit minimum 50 USDT). Casino Welcome Bonus dan Crypto Welcome Bonus adalah penawaran alternatif untuk deposit pertama, jadi pemain memilih salah satunya. Klaim Casino Welcome Bonus lewat deposit pertama setelah syaratnya dibaca. Alurnya terdiri dari empat langkah:

- Daftarkan akun dan lengkapi data pribadi yang diminta.
- Lakukan deposit pertama yang memenuhi syarat.
- Aktifkan Casino Welcome Bonus di My Bonuses sebelum memasang taruhan.
- Mainkan game kasino yang memenuhi syarat dan selesaikan wagering sebelum bonus kedaluwarsa.

### Wagering, batas, dan pengecualian
Syarat berikut menentukan kapan bonus dan kemenangannya dapat ditarik, sehingga perlu dibaca sebelum deposit pertama.

| Syarat | Nilai |
|---|---|
| Wagering | 25x deposit plus bonus |
| Wagering Free Spins | 40x kemenangan Free Spins |
| Masa berlaku | 10 hari sejak aktivasi |
| Taruhan maksimum | €22,5 per putaran |
| Cashout maksimum | 5x jumlah bonus awal |

Kemenangan dari Free Spins memiliki syarat wagering tersendiri, sehingga dihitung terpisah dari wagering deposit dan bonus, dan seluruhnya harus selesai dalam masa berlaku 10 hari. Deposit lewat Neteller dan Skrill dikecualikan dari promosi ini. Hanya satu bonus promosi yang boleh aktif dalam satu waktu, dan permintaan penarikan sebelum klaim atau saat bonus aktif dapat membatalkan kelayakan promosi. Membatalkan promosi berarti dana bonus dan kemenangan promosi yang belum dikonversi hangus. Verifikasi akun juga dapat diminta sebelum kemenangan promosi dibayarkan, jadi dokumen sebaiknya sudah siap.

## Level VIP dan batas yang lebih tinggi
Longfu88 VIP Program memberi poin VIP dari permainan uang sungguhan yang memenuhi syarat, dan poin itu membuka level hadiah bernomor. Ada 25 level yang dikelompokkan ke dalam lima tier: Bronze, Silver, Gold, Platinum, dan Diamond. Tabel berikut menampilkan enam level sebagai gambaran jalur dari bawah ke atas.

| Level | Poin | Hadiah | Cashback | Batas penarikan |
|---|---|---|---|---|
| 1 | 1 | €9,8 | 1% | €9.800 |
| 5 | 70 | €24,5 | 2% | €34.300 |
| 10 | 700 | €147 | 4% | €63.700 |
| 15 | 2.100 | €392 | 6% | €88.200 |
| 20 | 3.600 | €637 | 8% | €117.600 |
| 25 | 5.500 | €980 | 10% | €147.000 |

Semakin tinggi level, semakin banyak yang ditambahkan: penawaran personal, cashback, batas penarikan yang lebih besar, dan manajer VIP pribadi mulai dari level 4. Jumlah poin naik tajam di level atas, sehingga level 25 menuntut jauh lebih banyak permainan daripada level 5. Hadiah dan batas penarikan dapat berbeda menurut level VIP dan mata uang, dan aturan program dapat berubah, jadi ketentuan terbaru layak diperiksa sebelum mengejar level tertentu.

## Reload dan promosi musiman beserta aturannya
Promosi berulang mengikuti pola mingguan dan akhir pekan, dengan versi kripto dan kampanye khusus. Tujuh penawarannya:

- **Casino Weekly Reload**: memberi 50 Free Spins, minimum deposit €30, wagering 40x kemenangan Free Spins, 7 hari.
- **Casino Weekly Crypto Reload**: penawaran 60% hingga 1.000 USDT dengan setoran minimum 20 USDT, wagering 30x dari deposit dan bonus, berlaku 7 hari.
- **Casino Weekend Reload**: hingga €3.360 + 50 Free Spins, minimum deposit €50, wagering 30x deposit dan bonus serta 40x kemenangan Free Spins, 7 hari.
- **Casino Weekend Crypto Reload**: bonus 75% hingga 750 USDT + 100 Free Spins, minimum deposit 20 USDT, wagering sama seperti Weekend Reload, 7 hari.
- **Casino Double Fortune: One-Day Reload Special**: bonus 50% hingga €500, minimum deposit €30, wagering 30x deposit dan bonus, 24 jam.
- **Casino Trick or Treat Pumpkin Bonanza**: promosi musiman hingga 100 Free Spins, minimum deposit €20, wagering 40x kemenangan Free Spins, 7 hari.
- **Casino Dragon Quest: Get Verified and Get Extra!**: kredit bonus €10 untuk verifikasi akun, minimum deposit €20, wagering 30x kredit promosi, 7 hari.

Aturan bersama: aktivasi di My Bonuses, satu klaim per periode promosi kecuali ditentukan lain, tidak dapat digabung dengan bonus kasino lain yang sedang aktif, dan taruhan maksimum €5 per putaran selama wagering dana bonus.

### Syarat cashback
Casino Weekly Cashback mengembalikan hingga 10% dari kerugian bersih kasino mingguan, dengan batas €6.988. Periode hitungnya Senin 00:00 UTC sampai Minggu 23:59 UTC. Pemain ikut lewat opt-in untuk siklus empat minggu, dan hasilnya masuk ke My Bonuses pada hari Senin dengan wagering 10x. Persentasenya bergantung pada tier VIP, sedangkan Live Casino Cashback memberi 25% hingga €850. Unlimited Rebate dikreditkan setiap hari dengan wagering 1x: kasino 0,9%, live casino 1,0%, P2P 0,8%, dan lotere 1,0%. Hanya taruhan uang sungguhan yang dihitung, bukan dana bonus.

| Tier VIP | Persentase | Maksimum |
|---|---|---|
| Bronze | 2% | €1.888 |
| Silver | 4% | €2.388 |
| Gold | 6% | €2.988 |
| Platinum | 8% | €3.988 |
| Diamond | 10% | €6.988 |

## Metode deposit dan batasnya
Bagi pemain dari Indonesia, QRIS, DANA, OVO Wallet, Mandiri, BNI, dan BCA dalam IDR menjadi pilihan lokal, di samping kartu, transfer bank, kripto, e-wallet, dan metode Eropa.

| Jenis metode | Contoh | Mata uang |
|---|---|---|
| Bank dan dompet lokal | QRIS, DANA, OVO Wallet, Mandiri, BNI, BCA | IDR |
| Kartu | Visa, Mastercard | IDR, MYR, SGD, VND |
| Transfer bank | Bank Transfer | IDR, MYR, VND |
| Kripto | Bitcoin, Ethereum, Litecoin, USDT di jaringan TRC20, ERC20, dan BEP20, USDC, serta aset kripto lain | BTC, ETH, LTC, USDT, USDC, BCH, XRP, ADA |
| E-wallet | Neteller, Skrill | EUR |
| Metode Eropa | Sofort, Giropay | EUR |

Batas umum untuk setiap metode adalah minimum €10 dan maksimum €5.000 per transaksi, dengan kredit masuk dalam 1-2 menit. Kasino tidak memungut biaya pemrosesan, tetapi penyedia pembayaran atau jaringan blockchain dapat mengenakan biaya, dan batas dapat berbeda menurut negara, mata uang, dan metode. Deposit lewat Neteller dan Skrill dikecualikan dari bonus selamat datang. Alurnya enam langkah: masuk ke akun Longfu88, buka kasir dan pilih Deposit, pilih metode beserta mata uang atau jaringan blockchain yang didukung, isi jumlah dan data pembayaran, konfirmasi serta otorisasi transaksi sesuai petunjuk penyedia, lalu tunggu dana masuk ke saldo yang dapat dimainkan.

### Penarikan dana: waktu, biaya, dan turnover
Penarikan di Longfu88 tersedia lewat Bank Transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT di tiga jaringan (TRC20, ERC20, BEP20), Touch'n Go, DANA, MoMo, DBS Bank, dan Online Banking, dengan minimum €20 dan maksimum €5.000. Untuk Lngfu88 withdrawal time, penarikan kartu, kripto, dan dompet digital memerlukan 1 sampai 3 hari kerja. Transfer bank memerlukan hingga 3 hari kerja untuk pemrosesan kasino, ditambah 3 sampai 5 hari kerja untuk pengiriman bank, dan permintaan umumnya diproses dalam tiga hari kerja.

Kasino tidak memungut biaya penarikan standar, tetapi biaya penyedia dan blockchain dapat berlaku. Komisi 10% (minimum €2,25) dapat dikenakan bila turnover di bawah jumlah deposit, karena turnover minimum 1x deposit dapat berlaku sebelum penarikan. Sebagian transaksi yang didanai kartu atau transfer bank dapat dikenai 15%. Pemeriksaan identitas dapat menunda pembayaran. Langkah penarikan:

1. Masuk ke akun dan buka kasir.
2. Pilih Withdrawal dan metode atau tujuan yang didukung.
3. Isi jumlah serta rekening bank, dompet, atau alamat blockchain penerima.
4. Selesaikan verifikasi identitas dan metode pembayaran bila diminta.
5. Periksa permintaan dan konfirmasikan pengiriman.
6. Tunggu pemrosesan kasino serta penyelesaian bank atau jaringan sebelum dana diterima.

## Permainan yang tersedia
Lobi Longfu88 disusun menurut sembilan kategori: slot, live dealer, permainan meja, jackpot, fishing, permainan P2P, fast games, lotere, serta crash dan instant games. Pembagian ini memudahkan pemain memilih format sesuai selera, mulai dari slot dan jackpot sampai ronde singkat di fast games serta crash dan instant games. Lotere dan permainan P2P menawarkan cara bermain yang berbeda dari mesin slot. Slot dan live dealer mendapat sub-bagian tersendiri dalam ulasan ini, sedangkan kategori lainnya cukup dikenali dari namanya sebelum pemain membuka lobi. Pemain yang baru mengenal lobi sebaiknya memulai dari satu atau dua kategori saja, supaya syarat bonus dan batas taruhan pribadi lebih mudah dipantau.

### Slot: RTP dan volatilitas
Slot memberi contoh paling jelas tentang cara membaca angka sebuah permainan. Gates of Olympus dari Pragmatic Play memiliki RTP 96,50%, volatilitas tinggi, dan pengali maksimum 5.000x. Sweet Bonanza, juga dari Pragmatic Play, memiliki RTP 96,48%, volatilitas tinggi, dan pengali maksimum 21.175x. Wanted Dead or a Wild dari Hacksaw Gaming mencatat RTP 96,38%, volatilitas sangat tinggi, dan pengali maksimum 12.500x. RTP adalah persentase taruhan yang secara teori dikembalikan slot dalam jangka panjang, sedangkan volatilitas menggambarkan seberapa sering dan seberapa besar kemenangan datang: volatilitas tinggi berarti kemenangan lebih jarang, tetapi dapat lebih besar. Pemain yang menginginkan hasil lebih merata biasanya mencari volatilitas yang lebih rendah, sedangkan ketiga judul ini sama-sama berada di sisi tinggi. Ketiganya hanyalah contoh, dan pengali maksimum bukan jaminan hasil.

### Permainan live dealer
Permainan live dealer adalah kategori lobi tempat dealer sungguhan memimpin ronde lewat siaran langsung dari studio. Di Longfu 88 Casino, kategori ini mencakup game eksklusif Longfu88 Baccarat, permainan live atau meja dengan gameplay baccarat. Evolution dan SA Gaming, dua studio live dalam daftar penyedia, termasuk di antara pemasok kategori ini, tetapi game live yang dipasok masing-masing tidak dirinci. Baccarat adalah permainan kartu yang membandingkan tangan pemain dengan tangan banker, dan versi live memperlihatkan pembagian kartunya secara langsung. Bagi pemain yang lebih menyukai interaksi dengan dealer daripada putaran otomatis, kategori ini menjadi alternatif di luar slot, tetapi syarat promosi tetap perlu dibaca sebelum bermain. Penyedia lainnya dibahas pada bagian berikut.

## Penyedia permainan
Permainan di Longfu 88 dipasok oleh studio-studio berikut: Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft, dan Hacksaw Gaming. Para penyedia ini memasok slot, game live, dan permainan meja ke kasino. Pragmatic Play dan Hacksaw Gaming sudah muncul lewat contoh slot di atas, sedangkan Evolution dan SA Gaming dikenal lewat sisi live. Setiap studio memiliki katalog sendiri, jadi pemain dapat membandingkan beberapa nama sebelum memilih game. Daftar nama ini berguna bagi pemain yang ingin mencari game dari studio yang sudah dikenalnya.

## Bermain lewat ponsel
Kasino berjalan sebagai situs responsif di peramban ponsel dan tablet, dengan platform Android, iOS, dan web seluler. Situs dapat ditambahkan ke layar utama sebagai pintasan, sehingga Longfu88 app dalam pengertian ini adalah versi layar utama dari situs yang sama. Lewat pintasan itu pemain langsung mengakses kasino, sportsbook, akun, deposit, penarikan, dan bonus tanpa mengetik alamat setiap kali. Di Android, pintasan dibuat lewat Chrome dengan tiga langkah:

1. Buka Longfu88 di Chrome.
2. Buka menu peramban dan pilih Add to Home screen.
3. Konfirmasi pintasan.

Di iOS, pintasan dibuat lewat Safari, juga dalam tiga langkah:

1. Buka Longfu88 di Safari.
2. Ketuk Share dan pilih Add to Home Screen.
3. Konfirmasi dengan Add.

## Pasar taruhan olahraga dan aturannya
Di bagian Longfu sports, sportsbook mencakup sepak bola, bola basket, tenis, bulu tangkis, kriket, tenis meja, bola voli, esports, dan sepak bola virtual. Esports berdiri sejajar dengan cabang tradisional, sehingga pemain yang mengikuti turnamen gim dapat bertaruh dari akun yang sama dengan permainan kasino. Ada tujuh jenis taruhan: tunggal, akumulator, live, handicap, totals, outrights, dan Bet Builder. Taruhan tunggal hanya memuat satu seleksi, sedangkan akumulator menggabungkan beberapa seleksi dalam satu taruhan. Pemain yang ingin menyusun taruhan sendiri dapat memakai Bet Builder, yang menggabungkan beberapa pasar dari satu pertandingan. Live betting memakai live odds dan pasar in-play yang berubah selama pertandingan berjalan. Ketersediaan acara dan pilihan pasar dapat berbeda menurut yurisdiksi, jadi daftar di Longfu88 tidak selalu sama di setiap wilayah.

### Promosi olahraga
Sport First Deposit Bonus memberi 100% hingga €1.888 dengan deposit minimum €50, wagering 8x, dan masa berlaku 30 hari. Sport Weekly Reload Bonus memberi 50% hingga €2.500 dan Sport Weekend Reload Bonus 50% hingga €3.750, keduanya dengan minimum €50 dan wagering 8x. Versi kripto tersedia sebagai padanannya. Sports Cashback mengembalikan 10% hingga €2.500 dari kerugian bersih taruhan olahraga yang memenuhi syarat setiap minggu, dan Unlimited Sports Rebate memberi 0,70%. Ada pula 2 Goals Ahead (pembayaran lebih awal), Parlay Boost hingga 100% tambahan kemenangan pada akumulator dengan minimal tiga seleksi, dan Bet Builder Risk Free dengan pengembalian taruhan 50% hingga €250. Hanya taruhan yang sudah selesai dan memenuhi syarat dihitung. Taruhan tunggal memerlukan odds minimal 2,00, setiap seleksi akumulator minimal 1,50, dan taruhan batal atau cash out tidak dihitung.

## Kelebihan dan batasan
| Kelebihan | Batasan |
|---|---|
| Deposit minimum umum hanya €10 | Bonus selamat datang memerlukan deposit €50 dan wagering 25x deposit dan bonus |
| Pilihan metode pembayaran luas, termasuk kripto | Komisi 10% atau 15% dapat dikenakan pada penarikan menurut aturan turnover |
| Cashback mingguan hingga 10% | Penarikan lewat bank dapat memakan beberapa hari kerja |
| Program VIP dengan 25 level dan live chat 24/7 | Verifikasi dapat menunda pembayaran pertama |

---

## BLOCK BRIEF
Block: b22, H2 "Support Channels and Languages" (under H1 "Longfu88 casino Indonesia: ulasan keamanan, syarat, dan kontrol")
Page heading (output language): "Saluran dukungan dan bahasa"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 80-100 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 100, but never beyond 120 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
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
- Customer Support [10]
- Live Chat [8]
- Email Support [7]
- Support Languages [6]
Entity Connections to state explicitly [priority]:
- Live Chat → is available → 24/7 [8]
- Customer Support → speaks → English, Malay, Simplified Chinese, Thai, Indonesian and Vietnamese [6]
Summary: Support channels, availability and languages.
Copywriter Notes: Give the two channels (24/7 live chat and e-mail), the e-mail address exactly as given (it contains the tracked keyword "Longfu88") and the six support languages (English, Malay, Simplified Chinese, Thai, Indonesian, Vietnamese). Do not mention a phone line, a ticket system, an average response time or a social account: none is given. Use "Longfu88" exactly once, and no other tracked keyword. The e-mail address contains the tracked keyword "Longfu88"; it is part of the exact count of this block.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_general.customer_support: {"channels": ["24/7 live chat", "Email"], "email": "support@longfu88.com", "languages": ["English", "Malay", "Simplified Chinese", "Thai", "Indonesian", "Vietnamese"]}
Counting warning: the facts above contain tracked keywords "Longfu88" (x1). Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example 'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the permitted uses of this block ({'Longfu88': 1}); otherwise paraphrase ('the website', 'your account', 'the casino's own games').
