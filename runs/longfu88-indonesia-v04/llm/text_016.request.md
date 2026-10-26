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
Page intent: Compact brand-review page about the Longfu88 online casino for players from Indonesia, built for a reader on a phone: the fact table, opening the casino on mobile, sign-up and login, the first bonus, adding funds, taking money out, what to play, sports bets, promotions and rewards, VIP levels, licence and data rules, responsible play, support, a short FAQ and a summary. Page voice: how-to and imperative, sentences of about 12 words, paragraphs of one to two sentences, many short flat H2 sections, each opens with the action the reader takes and ends with the one thing to check; lists and short tables where they save words; calls to action at the first bonus only. All brand facts come from the AffBulk knowledge base longfu88-new; nothing is claimed about the legal status of the casino in Indonesia.
All tracked keywords: Longfu88, Longfu 88, Longfu88 casino, Longfu88 login, Longfu caino login, Longfu88 bonus, Longfu88 app, Longfu88 promo code, Longfu 88 casino, casino Longfu88, Lngfu88 withdrawal time, Longfu 88 Official Site, Longfu, Longfu sports
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "longfu88-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Longfu88 Casino di Ponsel: Ulasan untuk Pemain Indonesia (88-112 words): Short introduction: what the online casino is, which game areas it covers, when it launched and that this page is written for adult players from Indonesia.
b02   H2 Fakta Singkat dalam Tabel (74-94 words): A fact sheet of the casino: licence, minimum deposit, welcome bonus, payment methods, Mobile access, currencies, languages, cashback, support.
b03   H2 Cara Membuka Situs di Ponsel (106-134 words): Mobile play on Android, iOS and mobile web: the responsive site, the home-screen shortcut and the account functions available.
b04   H2 Daftar Akun dan Masuk (175-225 words): Registration in five numbered steps, login and password recovery, then when documents are requested, which ones and how long the review takes.
b05   H2 Bonus Pertama dan Syaratnya (188-241 words): The Casino Welcome Bonus with its figures, claiming steps and alternatives, then the wagering, validity and bet limits in a table.
b06   H2 Pembayaran: Cara Isi Saldo (135-173 words): Deposit methods grouped by type with the general limits and speed, the local options for Indonesia and the six-step deposit route.
b07   H2 Cara Menarik Dana (122-154 words): How withdrawals work: the methods, the six-step route, the processing time, the limits and the conditional fees.
b08   H2 Permainan yang Bisa Dimainkan (257-326 words): The nine game categories, three example slots with RTP, the live section with the exclusive baccarat, the other categories and the ten providers.
b09   H2 Taruhan Olahraga (102-130 words): The sportsbook: the sports and esports covered, the bet types and live betting.
b10   H2 Promo Rutin dan Hadiah (168-215 words): The seven reload and seasonal offers in a table, the weekly cashback with VIP rates and the rebates, and the five reward features in short.
b11   H2 Level Klub VIP (88-112 words): How the VIP programme works: points from real-money play, the five tiers, the 25 reward levels and what changes on the way up.
b12   H2 Lisensi dan Aturan Data (168-215 words): Launch year, currencies and who may play, then the licence, the operator and how data and accounts are protected.
b13   H2 Bermain dengan Bertanggung Jawab (94-120 words): Age limit, self-exclusion and account closure by e-mail request, self-assessment and the help organisations.
b14   H2 Dukungan Pelanggan (68-86 words): Support channels, availability and languages.
b15   H2 FAQ Seputar Ponsel (158-202 words): Short answers on withdrawal time, claiming the bonus, password recovery, the app question.
b16   H2 Kesimpulan (81-104 words): A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Longfu88 Casino di Ponsel: Ulasan untuk Pemain Indonesia
Longfu88 adalah kasino online yang meluncur pada 2026 dan menggabungkan slot, permainan dealer langsung, permainan meja, jackpot, tembak ikan, permainan P2P, permainan cepat, lotere, serta permainan crash dan instan dengan sportsbook dalam satu akun. Setiap kategori permainan punya bagian sendiri di lobi, sehingga pemain bisa langsung menuju jenis permainan yang diminati.

Halaman ini ditulis untuk pemain dari Indonesia dan dibaca paling nyaman lewat ponsel. Urutannya mengikuti langkah pemain: fakta singkat, lisensi, bonus, permainan, pembayaran, cara bermain di ponsel, dan permainan yang bertanggung jawab. Pemain wajib berusia minimal 18 tahun.

## Fakta Singkat dalam Tabel
=== b02 ===
| Parameter | Keterangan |
|---|---|
| Lisensi | Yurisdiksi Kosta Rika, operator Lumina, nomor registrasi 000-039123-R-319326-001 |
| Setoran minimum | €10 |
| Bonus selamat datang | 188% hingga €2.088 + 18 putaran gratis |
| Metode pembayaran | QRIS, DANA, OVO Wallet, Visa, Mastercard, Bank Transfer, Bitcoin, USDT |
| Akses seluler | Android, iOS, web seluler |
| Mata uang | EUR, USD, MYR, THB, SGD, USDT |
| Bahasa dukungan | Inggris, Melayu, Mandarin Sederhana, Thai, Indonesia, Vietnam |
| Cashback | Hingga 10% dari kerugian bersih kasino mingguan |
| Dukungan | Surel support@longfu88.com dan obrolan langsung 24/7 setiap hari |

## Cara Membuka Situs di Ponsel
=== b03 ===
Buka situs lewat peramban ponsel, tanpa perlu mengunduh apa pun. Situs responsifnya berjalan di peramban ponsel pintar dan tablet, sehingga Android, iOS, dan web seluler memakai alamat yang sama. Pintasan di layar utama berfungsi sebagai Longfu88 app, yaitu versi layar utama dari situs yang sama, dengan akses cepat ke kasino dan sportsbook. Dari sana tersedia juga akses akun, setoran, penarikan, dan bonus. Pakai Chrome di Android dan Safari di iOS, lalu ikuti tiga langkah berikut.

| Langkah | Android (Chrome) | iOS (Safari) |
|---|---|---|
| 1 | Buka Longfu88 di Chrome. | Buka Longfu88 di Safari. |
| 2 | Buka menu peramban dan pilih Tambahkan ke layar utama. | Ketuk Bagikan dan pilih Tambah ke Layar Utama. |
| 3 | Konfirmasi pintasan. | Konfirmasi dengan Tambah. |

## Daftar Akun dan Masuk
=== b04 ===
Daftar lewat email dalam lima langkah, dengan data berikut: email, kata sandi, nama lengkap sesuai identitas, tanggal lahir, dan alamat tempat tinggal.

1. Buka Longfu88 dan pilih Daftar.
2. Masukkan email dan buat kata sandi.
3. Konfirmasi usia serta persetujuan atas Syarat dan Ketentuan dan Kebijakan Privasi.
4. Lengkapi data pribadi tambahan dan alamat tempat tinggal.
5. Pilih Buat Akun dan selesaikan konfirmasi email bila diminta.

Setiap pemain hanya boleh memiliki satu akun pribadi. Untuk masuk, pilih Masuk di situs, isi email dan kata sandi terdaftar, lalu selesaikan pemeriksaan keamanan bila muncul. Pemain yang mencari halaman Longfu caino login cukup memakai alur yang sama. Bila kata sandi terlupa, pilih Lupa Kata Sandi di layar masuk, minta tautan reset ke email terdaftar, lalu ikuti petunjuk di email tersebut.

Verifikasi KYC bisa diminta sebelum penarikan, pada transaksi tidak biasa atau bernilai tinggi, dan saat data akun atau pembayaran berubah. Siapkan dokumen berikut:

- Identitas: paspor, kartu identitas nasional, atau surat izin mengemudi.
- Alamat: tagihan utilitas atau rekening koran.
- Bukti kepemilikan metode pembayaran: kartu, rekening bank, atau dompet digital.
- Sumber dana bila diminta: bukti penghasilan atau rekening koran.

Kirim dokumen dalam 30 hari sejak diminta. Set dokumen yang lengkap biasanya ditinjau dalam waktu hingga 10 hari. Selama pemeriksaan berjalan, penarikan dapat ditahan, dan pemeriksaan yang gagal bisa berujung pada penolakan transaksi atau pembatasan akun. Periksa satu hal sebelum mengunggah: dokumen harus terbaca jelas, masih berlaku, dan sesuai profil akun.

## Bonus Pertama dan Syaratnya
=== b05 ===
Longfu88 bonus pertama bernama Casino Welcome Bonus: 188% hingga €2.088 plus 18 putaran gratis. Bonus setoran ini untuk pemain baru yang sudah terdaftar, berlaku pada setoran pertama yang memenuhi syarat, dan hanya satu penawaran selamat datang per akun. Setoran minimum bonus ini €50, bukan setoran minimum umum kasino.

- Daftar akun dan lengkapi data pribadi yang diminta.
- Lakukan setoran pertama yang memenuhi syarat.
- Aktifkan Casino Welcome Bonus di My Bonuses sebelum memasang taruhan apa pun.
- Mainkan permainan kasino yang memenuhi syarat dan selesaikan taruhan wajib sebelum bonus kedaluwarsa.

Daftar langkah di atas tidak memuat kode promo. Jalur klaimnya adalah aktivasi di My Bonuses setelah setoran yang memenuhi syarat. Dua alternatif setoran pertama juga tersedia: Live Casino Welcome Bonus (125% hingga €888, setoran minimum €30) dan Casino Crypto Welcome Bonus (188% hingga 2.888 USDT, setoran minimum 50 USDT). Casino Welcome Bonus dan Crypto Welcome Bonus saling menggantikan, jadi hanya satu yang bisa dipilih. Daftar di Longfu88 dan klaim bonus pertama setelah setoran.

Taruhan wajib bonus ini adalah 25 kali setoran plus jumlah bonus, dan bonus kedaluwarsa 10 hari setelah aktivasi.

| Syarat | Nilai |
|---|---|
| Taruhan wajib | 25x setoran plus bonus |
| Taruhan wajib putaran gratis | 40x kemenangan putaran gratis |
| Masa berlaku | 10 hari sejak aktivasi |
| Taruhan maksimum | €22,5 per putaran |
| Penarikan maksimum | 5x jumlah bonus awal |

Setoran lewat Neteller dan Skrill tidak termasuk dalam promosi ini, dan hanya satu bonus promosi yang boleh aktif pada satu waktu. Permintaan penarikan sebelum klaim atau saat bonus aktif dapat membatalkan kelayakan, sedangkan pembatalan menghanguskan dana bonus dan kemenangan promosi yang belum dikonversi. Verifikasi akun mungkin diperlukan sebelum kemenangan promosi dibayarkan.

## Pembayaran: Cara Isi Saldo
=== b06 ===
Pilih metode setoran dari enam kelompok berikut, yang semuanya memakai batas umum yang sama.

| Jenis metode | Contoh | Mata uang |
|---|---|---|
| Bank dan dompet lokal | QRIS, DANA, OVO Wallet, Mandiri, BNI, BCA | IDR |
| Kartu | Visa, Mastercard | IDR, MYR, SGD, VND |
| Transfer bank | Bank Transfer | IDR, MYR, VND |
| Kripto | Bitcoin, Ethereum, Litecoin, USDC, dan USDT di jaringan TRC20, ERC20, serta BEP20 | BTC, ETH, LTC, USDT, USDC |
| Dompet elektronik | Neteller, Skrill | EUR |
| Metode Eropa | Sofort, Giropay | EUR |

Setoran minimum €10 dan maksimum €5.000 per transaksi, dengan dana masuk dalam 1-2 menit. Kasino tidak memungut biaya pemrosesan, tetapi biaya penyedia pembayaran atau jaringan blockchain mungkin berlaku. Batas dapat berbeda menurut negara, mata uang, dan metode. Setoran Neteller dan Skrill tidak berlaku untuk bonus selamat datang.

Alurnya enam langkah: masuk ke akun Longfu88, buka kasir dan pilih Setoran, lalu pilih metode beserta mata uang atau jaringan blockchain yang didukung. Isi jumlah dan data pembayaran, konfirmasi transaksi sesuai petunjuk penyedia, dan tunggu dana masuk ke saldo yang bisa dimainkan.

## Cara Menarik Dana
=== b07 ===
Penarikan dana tersedia lewat Bank Transfer, Visa, Mastercard, Bitcoin, Ethereum, Litecoin, USDT di tiga jaringan (TRC20, ERC20, BEP20), Touch'n Go, DANA, MoMo, DBS Bank, dan Online Banking. Batasnya minimum €20 dan maksimum €5.000, dengan enam langkah berikut.

1. Masuk ke Longfu88 dan buka kasir.
2. Pilih Penarikan dan metode pembayaran yang didukung.
3. Isi jumlah serta rekening bank, dompet, atau alamat blockchain penerima.
4. Selesaikan verifikasi identitas dan metode pembayaran bila diminta.
5. Periksa permintaan dan konfirmasi pengiriman.
6. Tunggu pemrosesan kasino dan penyelesaian bank atau jaringan.

Soal Lngfu88 withdrawal time, penarikan lewat kartu, kripto, dan dompet digital memakan 1 sampai 3 hari kerja. Transfer bank butuh hingga 3 hari kerja pemrosesan kasino, ditambah 3 sampai 5 hari kerja pengiriman oleh bank. Secara umum, permintaan diproses dalam tiga hari kerja. Kasino tidak memungut biaya penarikan standar, tetapi biaya penyedia dan blockchain mungkin berlaku. Komisi 10% (minimum €2,25) dapat dikenakan bila perputaran taruhan di bawah jumlah setoran, sebab perputaran setoran minimal 1x dapat berlaku sebelum penarikan. Pada sebagian transaksi yang didanai kartu atau transfer bank, biayanya 15%. Pemeriksaan identitas dapat menunda pembayaran.

## Permainan yang Bisa Dimainkan
=== b08 ===
Buka lobi Longfu88 Casino dan pilih satu dari sembilan kategori permainan: slot, permainan dealer langsung, permainan meja, jackpot, tembak ikan, permainan P2P, permainan cepat, lotere, serta permainan crash dan instan. Pembagian ini membuat pemain bisa langsung menuju jenis permainan yang diinginkan, tanpa menggulir daftar panjang.

Slot adalah kategori pertama yang perlu dilihat. Gates of Olympus dari Pragmatic Play memiliki RTP 96,50%, volatilitas tinggi, dan pengali maksimum 5.000x. Sweet Bonanza dari Pragmatic Play mencatat RTP 96,48%, volatilitas tinggi, dan pengali maksimum 21.175x. Wanted Dead or a Wild dari Hacksaw Gaming memiliki RTP 96,38%, volatilitas sangat tinggi, dan pengali maksimum 12.500x. RTP adalah persentase taruhan yang secara teoretis kembali ke pemain dalam jangka panjang, sedangkan volatilitas menunjukkan seberapa besar dan seberapa jarang kemenangan datang. Karena itu, RTP yang tinggi tidak menjamin hasil dalam satu sesi.

Dealer langsung berdiri sebagai kategori tersendiri di lobi. Di sana tersedia Longfu88 Baccarat, permainan live atau meja eksklusif dengan gameplay baccarat. Evolution dan SA Gaming, dua nama dari daftar penyedia, dikenal sebagai studio dealer langsung.

Kategori lainnya dapat dibedakan dari apa yang dilakukan pemain. Permainan meja menghadirkan permainan kartu dan roda dengan aturan baku. Jackpot berfokus pada hadiah utama berukuran besar. Pada tembak ikan, pemain membidik ikan di layar untuk mengumpulkan poin. Permainan P2P mempertemukan pemain dengan sesama pemain, bukan dengan kasino. Permainan cepat dan permainan crash serta instan memberi hasil dalam hitungan detik, sedangkan lotere bertumpu pada pemilihan angka dan hasil pengundian.

Di Longfu 88, daftar penyedia mencakup Evolution, Red Tiger, NetEnt, Big Time Gaming, Pragmatic Play, Yggdrasil, SA Gaming, Skywind, Betsoft, dan Hacksaw Gaming. Para penyedia ini memasok slot, permainan live, dan permainan meja ke Longfu 88 Casino. Cek satu hal sebelum bermain: pilih permainan sesuai anggaran, bukan sesuai pengali tertinggi.

## Taruhan Olahraga
=== b09 ===
Buka bagian Longfu sports untuk memasang taruhan olahraga. Longfu88 menyediakan sportsbook dengan sembilan pilihan: sepak bola, basket, tenis, bulu tangkis, kriket, tenis meja, bola voli, esports, dan sepak bola virtual. Jenis taruhannya ada tujuh: taruhan tunggal, akumulator, taruhan langsung, handicap, total, outright, dan Bet Builder. Taruhan tunggal memuat satu pilihan, sedangkan akumulator menggabungkan beberapa pilihan dalam satu taruhan, sehingga semuanya harus tepat. Handicap memberi selisih awal pada salah satu pihak, dan outright dipasang pada hasil akhir sebuah kompetisi. Bet Builder menyusun beberapa pasar dari satu pertandingan. Taruhan langsung menyediakan odds langsung dan pasar in-play selama pertandingan berjalan. Ketersediaan acara dan pilihan pasar dapat berbeda menurut yurisdiksi, jadi cek daftar pertandingan sebelum memasang taruhan.

## Promo Rutin dan Hadiah
=== b10 ===
Cek promo berikut di Longfu88.

| Penawaran | Hadiah | Setoran minimum | Taruhan wajib | Berlaku |
|---|---|---|---|---|
| Casino Weekly Reload | 50 putaran gratis | €30 | 40x kemenangan putaran gratis | 7 hari |
| Casino Weekly Crypto Reload | 60% hingga 1.000 USDT | 20 USDT | 30x setoran plus bonus | 7 hari |
| Casino Weekend Reload | Hingga €3.360 + 50 putaran gratis | €50 | 30x setoran plus bonus, 40x kemenangan putaran gratis | 7 hari |
| Casino Weekend Crypto Reload | 75% hingga 750 USDT + 100 putaran gratis | 20 USDT | 30x setoran plus bonus, 40x kemenangan putaran gratis | 7 hari |
| Casino Double Fortune | 50% hingga €500 | €30 | 30x setoran plus bonus | 24 jam |
| Casino Trick or Treat Pumpkin Bonanza (musiman) | Hingga 100 putaran gratis | €20 | 40x kemenangan putaran gratis | 7 hari |
| Casino Dragon Quest | Kredit bonus €10 | €20 | 30x kredit promosi | 7 hari |

Semua promo diaktifkan di My Bonuses, satu klaim per periode, tanpa gabungan dengan bonus aktif lain, taruhan maksimum €5 per putaran.

Casino Weekly Cashback mengembalikan hingga 10% kerugian bersih kasino mingguan, maksimum €6.988, Senin 00:00 sampai Minggu 23:59 UTC. Ikut untuk siklus empat minggu, masuk ke My Bonuses setiap Senin, taruhan wajib 10x. Tarif VIP 2% sampai 10%. Live Casino Cashback memberi 25% hingga €850. Rebat harian dari taruhan uang asli, wajib 1x: kasino 0,9%, live casino 1,0%, P2P 0,8%, lotere 1,0%.

Di menu Rewards, Bonus Crab membuka hadiah (7 hari, taruhan wajib 30x dan 40x). Wheel of Fortune memakai satu putaran atau Coins (7 hari, 30x). Challenges dan Collections ada di sana. Coin Shop menukar Coins dengan hadiah dan kredit bonus hingga €4.500. Hadiah bisa bersyarat taruhan sendiri.

## Level Klub VIP
=== b11 ===
Poin VIP didapat dari permainan uang asli yang memenuhi syarat, dan poin itu membuka level hadiah bernomor. Ada 25 level yang dikelompokkan ke lima tingkat: Bronze, Silver, Gold, Platinum, dan Diamond. Level 1 butuh 1 poin, dengan hadiah level €9,8, cashback 1%, dan batas penarikan €9.800. Level 25 butuh 5.500 poin, dengan hadiah level €980, cashback 10%, dan batas penarikan €147.000. Semakin tinggi level, semakin besar cashback dan batas penarikan, ditambah penawaran personal serta manajer VIP pribadi mulai level 4. Besaran hadiah dan batas penarikan dapat berbeda menurut level dan mata uang, dan aturannya dapat berubah, jadi cek ketentuan terbaru sebelum mengejar level berikutnya.

## Lisensi dan Aturan Data
=== b12 ===
Kasino ini diluncurkan pada 2026 dan menerima akun dalam mata uang EUR, USD, MYR, THB, SGD, dan USDT, jadi pilih mata uang akun sebelum setoran pertama. Gunakan alamat Longfu 88 Official Site dan hindari halaman tiruan. Pemain harus berusia minimal 18 tahun, diizinkan secara hukum untuk berjudi di tempat tinggalnya, memakai satu akun pribadi, dan tidak memakai metode pembayaran milik pihak ketiga. Periksa aturan perjudian di tempat tinggal sebelum mendaftar.

Lisensi casino Longfu88 tercatat di yurisdiksi Kosta Rika atas nama operator Lumina, dengan nomor registrasi 000-039123-R-319326-001. Operator yang sama bertindak sebagai pengendali data, dan petugas perlindungan data dapat dihubungi di dpo@longfu88.com. Operator melindungi akun, pembayaran, dan data pribadi dengan pengamanan teknis dan organisasi. Data dapat dibagikan kepada penyedia layanan pembayaran, penyedia verifikasi identitas, penyedia teknologi, serta regulator dan penegak hukum bila diwajibkan. Artinya, regulator dan penegak hukum hanya menerima data jika hal itu memang diwajibkan.

Pemain berhak atas akses, perbaikan, penghapusan bila diizinkan hukum, pembatasan, keberatan, portabilitas bila berlaku, dan penarikan persetujuan. Pemegang akun bertanggung jawab menjaga kredensialnya, sedangkan operator dapat menangguhkan aktivitas untuk verifikasi atau dugaan penyalahgunaan. Jaga kata sandi tetap pribadi dan jangan bagikan ke siapa pun.

## Bermain dengan Bertanggung Jawab
=== b13 ===
Pemain harus berusia minimal 18 tahun dan hanya berjudi di tempat yang mengizinkannya. Untuk pengecualian diri, kirim permintaan lewat e-mail ke dukungan pelanggan. Akses akun dan permainan dapat dibatasi selama periode yang disepakati, dan prosesnya selesai dalam 24 jam setelah permintaan diproses. Penutupan akun juga diajukan lewat dukungan pelanggan dalam empat langkah: hubungi dukungan, konfirmasi data akun serta ketentuan pengecualian yang diinginkan, biarkan kasino membatasi atau menutup akses, lalu cari bantuan independen bila perlu. Pertanyaan penilaian diri membantu pemain mengenali kemungkinan dampak buruk judi. Bantuan independen tersedia dari GamCare, Gamblers Anonymous, dan Gambling Therapy, karena halaman ini tidak dapat menggantikannya.

## Dukungan Pelanggan
=== b14 ===
Hubungi dukungan pelanggan lewat dua kanal: obrolan langsung yang aktif 24/7 atau e-mail ke support@longfu88.com. Obrolan langsung cocok untuk pertanyaan yang butuh jawaban cepat, sedangkan e-mail lebih praktis untuk pesan yang panjang. Dukungan tersedia dalam enam bahasa: Inggris, Melayu, Mandarin Sederhana, Thai, Indonesia, dan Vietnam, sehingga pemain dari Indonesia dapat menulis dalam bahasa sendiri. Tulis inti masalah di pesan pertama agar penanganannya lebih mudah, dan simpan balasan dukungan untuk rujukan berikutnya.

## FAQ Seputar Ponsel
=== b15 ===
- **Berapa lama waktu yang dibutuhkan untuk menarik dana dari akun setelah permintaan dikirim?** Di Longfu88, kartu, kripto, dan dompet digital butuh 1 sampai 3 hari kerja. Transfer bank butuh hingga 3 hari kerja di kasino, lalu 3 sampai 5 hari kerja di bank.
- **Apakah klaim Casino Welcome Bonus memerlukan langkah tambahan berupa Longfu88 promo code?** Tidak ada langkah kode promo. Aktifkan Casino Welcome Bonus di My Bonuses setelah setoran pertama €50 yang memenuhi syarat, sebelum memasang taruhan apa pun, lalu selesaikan taruhan wajibnya.
- **Apa yang harus dilakukan jika lupa kata sandi saat Longfu88 login?** Pilih Lupa Kata Sandi di layar masuk, minta tautan reset ke e-mail terdaftar, lalu ikuti petunjuk di e-mail itu untuk membuat kata sandi baru. Setelah itu masuk lagi memakai kata sandi baru.
- **Apakah ada aplikasi yang bisa diunduh ke ponsel Android atau iOS?** Tidak ada unduhan aplikasi yang dijelaskan. Kasino berjalan sebagai situs responsif di peramban, yang bisa ditambahkan ke layar utama pada Android dan iOS sebagai pintasan.

---

## BLOCK BRIEF
Block: b16, H2 "Wrap-Up" (under H1 "Longfu88 Casino di Ponsel: Ulasan untuk Pemain Indonesia")
Page heading (output language): "Kesimpulan"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 81-104 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 104, but never beyond 124 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Longfu88": exactly 1 time(s)
- "Longfu 88": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu88 casino": exactly 1 time(s)
- "Longfu88 login": 0 here, but the brand name may appear when the text reads naturally: at most 1 time(s) in this block (one per 50 words)
- "Longfu caino login": 0 (do not use)
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
- Player → should check → the bonus terms and payment limits before depositing [7]
Summary: A short verdict: whom the offer fits, what to check before depositing and the responsible-gambling reminder.
Copywriter Notes: Close with three or four sentences: which kind of player the facts fit (someone who wants casino, live and sports betting in one account with local and crypto payments), what to check before depositing (the €50 qualifying deposit, 25x wagering, the withdrawal turnover rule and verification), then the 18+ limit with the reminders that gambling is not a source of income, that losses should not be chased and that a budget and breaks help. Where "Longfu88 casino" is used (the name Longfu88 Casino), it sits in the first sentence. Where "Longfu" is used, write it as the short name of the casino. Repeat no figures, make no promises of winnings, no hype. NEVER say or imply that the casino is licensed, legal or approved in Indonesia; the licence named in the Brand Information is the only licence statement. Use "Longfu88" exactly once, "Longfu88 casino" (written as the name Longfu88 Casino) exactly once and "Longfu" exactly once, and no other tracked keyword.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_general.minimum_age: 18
- brandinfo_responsible_gaming.responsible_gaming.policy: Players must be at least 18 years old and gamble only where lawful.
