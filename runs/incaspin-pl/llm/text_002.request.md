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
Brand: Incaspin (this name and its spellings are tracked keywords: the block brief gives the exact count; where it says 0 the brand name is free to use)
Country / GEO: PL
Language: Polish (pl). Write ONLY in this language.
Page intent: Brand-related (navigational and informational) review page about the Incaspin online casino for players from Poland: what the casino is, key facts, licence and safety, registration and login, verification, welcome bonus and its terms, other promotions, loyalty programme, games and providers, payments, withdrawals and limits, mobile PWA, sports betting, responsible gambling, support and FAQ. All brand facts come from the AffBulk knowledge base incaspin-new; nothing is claimed about the legal status of the casino in Poland.
All tracked keywords: Incaspin, Inca Spin, Incaspin casino
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "incaspin-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Incaspin Casino: recenzja kasyna dla polskich graczy (84-106 words): Short introduction: what the online casino is, which four areas it covers and who the page is written for (adult players from Poland), plus a signpost to the topics of the page.
b02   H2 Kasyno w skrócie (58-74 words): A compact fact sheet of the casino: operator, licence, launch year, support languages, currencies, payment methods, welcome bonus, cashback, minimum deposit and support e-mail.
b03   H2 Licencja i bezpieczeństwo w Incaspin Casino (132-168 words): Who licenses and runs the casino (authority, number, jurisdiction, operator company, payment agent) and how accounts and verification documents are protected technically.
b04   H2 Rejestracja i logowanie w Incaspin (136-174 words): How to open an account by email in five steps, the one-account-per-person rule, and how login, password recovery and two-factor authentication work.
b05     H3 Weryfikacja konta (KYC) (101-129 words): When identity verification is required, which documents are accepted, how long the review takes and what happens with false documents.
b06   H2 Bonus powitalny w Incaspin Casino (132-168 words): The Casino Welcome Package: total amount, free spins, the three deposit stages, minimum deposit and how the bonus is claimed.
b07     H3 Zasady obrotu i warunki bonusu (115-145 words): Terms of the welcome package in a table: wagering, maximum bet, validity, free spin delivery, game contribution, free spin winnings cap and eligible slots.
b08   H2 Promocje i cashback w Incaspin (123-157 words): Promotions beyond the welcome package: Highroller Bonus, Sunday Reload and Weekly Cashback, compared in a table with a short commentary.
b09   H2 Program lojalnościowy Incaspin (141-179 words): The Boomerang loyalty programme: points, six ranks in a table, rewards, and the gamification features (Wheel of Fortune, Missions, Reward Chests, Points Store).
b10   H2 Gry w Incaspin Casino (110-140 words): Overview of the game library: the categories offered and the size of the lobby; details follow in the sub-sections.
b11     H3 Sloty i jackpoty (92-118 words): Slot examples and jackpot titles available in the lobby.
b12     H3 Kasyno na żywo (92-118 words): The live casino section with its roulette, baccarat and game show titles.
b13     H3 Gry stołowe, crash i błyskawiczne (101-129 words): Instant and crash titles and the casino's own original games.
b14   H2 Dostawcy gier w Incaspin (88-112 words): Which studios supply the games: a few key providers named in a sentence and a bulleted list of further studios.
b15   H2 Metody płatności i wpłaty (120-152 words): Deposit methods with minimum, maximum and speed in a table, and the short route of a deposit through the cashier.
b16     H3 Wypłaty i czas realizacji (142-182 words): How withdrawals work: methods, six-step route, processing time, minimum amount, wagering of deposits and verification.
b17     H3 Limity i waluty (101-129 words): Which currencies the account can use and examples of withdrawal limits and bank charges.
b18   H2 Gra mobilna: aplikacja PWA Incaspin (124-156 words): Mobile play as a Progressive Web App: what it is, how to install it on iPhone and Android, and which sections it contains.
b19   H2 Zakłady sportowe i e-sport w Incaspin (142-182 words): The sportsbook: sports and esports covered, bet types, and the separate Sportsbook Welcome Package.
b20   H2 Odpowiedzialna gra (142-182 words): Tools for responsible play: age limit, deposit limits, other limits, self-exclusion, help organisations and basic rules.
b21   H2 Obsługa klienta (92-118 words): Support channels, availability and languages.
b22   H2 Najczęstsze pytania o Incaspin Casino (145-185 words): Five short answers: promo code for the welcome bonus, minimum deposit, withdrawal time, password recovery, mobile access.
b23   H2 Podsumowanie (81-104 words): Closing assessment: what kind of player the offer fits, what to check before depositing, and a responsible-gambling reminder.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Incaspin Casino: recenzja kasyna dla polskich graczy
Incaspin to kasyno online, które łączy cztery obszary: klasyczne kasyno, kasyno na żywo, bukmachera sportowego i zakłady na e-sport. Gry kasynowe stanowią rdzeń oferty, a dział sportowy uzupełnia ją dla osób, które wolą obstawiać wyniki, niż kręcić bębnami. Strona powstała z myślą o polskich graczach, ale zasady dotyczące gier online różnią się między państwami, dlatego każdy użytkownik powinien sprawdzić, czy ta oferta jest dla niego dostępna. Korzystać z serwisu mogą wyłącznie osoby, które ukończyły 18 lat. Kolejne sekcje opisują rejestrację, bonusy, gry, płatności, grę na telefonie i bezpieczeństwo, dzięki czemu ocena Incaspin opiera się na konkretnych informacjach.

## Kasyno w skrócie
| Parametr | Dane |
|---|---|
| Operator | Legasta Technologies SRL |
| Licencja | wydawca Tobique Gaming Commission, numer 0000158, jurysdykcja Tobique |
| Rok startu | 2025 |
| Języki obsługi | angielski i inne języki |
| Waluty | EUR, BRL, CAD, AUD oraz kryptowaluty BTC i ETH |
| Metody płatności | Visa, Mastercard, Apple Pay, Google Pay, Skrill, Neteller, kryptowaluty, przelew bankowy |
| Bonus powitalny | do 2750 € i 275 darmowych spinów |
| Cashback | do 25% tygodniowej straty netto |
| Minimalny depozyt | 20 € (pierwsza wpłata pakietu powitalnego) |
| Wsparcie | support@incaspin.com |

## Rejestracja i logowanie w Incaspin
Konto w Incaspin Casino zakłada się wyłącznie przy użyciu adresu e-mail, a cały proces mieści się w pięciu krokach:

1. Otworzyć stronę serwisu i wybrać opcję rejestracji.
2. Wpisać adres e-mail.
3. Utworzyć hasło.
4. Potwierdzić, że ma się ukończone 18 lat.
5. Wysłać formularz rejestracyjny.

Obowiązuje przy tym jedna zasada: każda osoba może mieć tylko jedno konto, a limit dotyczy także gospodarstwa domowego, adresu IP i komputera. Duplikaty mogą zostać zawieszone lub zamknięte, a zakłady, bonusy i wygrane z takich kont mogą zostać unieważnione. Dodatkowe konto nie daje więc żadnej przewagi, a naraża saldo na utratę.

Logowanie w Incaspin przebiega równie prosto: wystarczy wybrać opcję logowania i podać e-mail oraz hasło użyte przy rejestracji. Gracz, który zapomniał hasła, korzysta z opcji przypomnienia hasła na ekranie logowania i postępuje według instrukcji wysłanej e-mailem. Dodatkową warstwę ochrony daje uwierzytelnianie dwuskładnikowe, czyli drugi etap potwierdzenia obok hasła, które można włączyć w ustawieniach konta. W Incaspin warto włączyć je od razu po rejestracji.

### Weryfikacja konta (KYC)
Weryfikacja tożsamości (KYC, czyli sprawdzenie, kim jest gracz) może być wymagana przed pierwszą wypłatą oraz podczas kontroli wpłat, a do czasu pełnej weryfikacji konta kasyno nie realizuje żadnych wypłat. Wymagane dokumenty gracz przesyła w ramach weryfikacji, a w Incaspin należą do nich:

- dokument tożsamości: paszport, dowód osobisty lub prawo jazdy
- aktualny rachunek za media albo wyciąg bankowy
- potwierdzenie metody płatności, z której korzysta gracz
- selfie z dokumentem tożsamości lub kontrola tożsamości na żywo

Większość dokumentów jest sprawdzana w czasie od kilku godzin do jednego dnia. Dokumenty muszą być autentyczne, ponieważ fałszywe lub podrobione materiały mogą skutkować zajęciem wpłaconych środków i wygranych.

## Bonus powitalny w Incaspin Casino
Casino Welcome Package to pakiet powitalny Incaspin Casino, który łączy bonusy od wpłat o łącznej wartości do 2750 € z 275 darmowymi spinami, czyli spinami na slocie, w których stawkę pokrywa kasyno. Incaspin rozkłada go na pierwsze trzy wpłaty, ale nie po równo: najwięcej darmowych spinów przypada na start, a druga wpłata daje wyłącznie bonus pieniężny.

- pierwsza wpłata: do 1000 € i 200 darmowych spinów
- druga wpłata: 100% do 1000 €
- trzecia wpłata: 75% do 750 € i 75 darmowych spinów

Po zsumowaniu trzy bonusy dają 2750 €, więc pakiet opłaca się przede wszystkim graczom, którzy planują kilka wpłat. Kto wpłaci tylko raz, skorzysta najwyżej z pierwszego etapu. Wejście do oferty Incaspin jest niskoprogowe: pierwsza wpłata wymaga 20 €, a oferta przewiduje progi wpłat 20 €, 50 € i 300 €. Bonusy z pakietu trafiają na konto automatycznie, kod promocyjny nie jest potrzebny, a wpisanie go przy bonusie z pakietu powitalnego pozbawia gracza prawa do tego bonusu. Zasady obrotu i limity opisuje kolejna część. Gracz, który chce sprawdzić Incaspin, może więc po prostu się zarejestrować i dokonać pierwszej wpłaty.

### Zasady obrotu i warunki bonusu
Warunki pakietu powitalnego najłatwiej ocenić w zestawieniu, które obejmuje obrót, maksymalną stawkę, ważność oraz zasady darmowych spinów w Incaspin.

| Warunek | Wartość |
|---|---|
| Obrót | 35x bonus przy bonusach za drugą i trzecią wpłatę, domyślnie 40x, o ile oferta nie określa inaczej |
| Maksymalna stawka podczas obrotu | 5 € na slotach i 10 € w grach na żywo |
| Ważność bonusów pakietu | 7 dni |
| Darmowe spiny | 50 darmowych spinów dziennie przez pięć dni po pierwszej wpłacie, aktywacja możliwa przez 3 dni, spiny i wygrane ważne 7 dni |
| Udział gier w obrocie | sloty 100%, gry karciane, ruletka, poker i video poker 5%, gry z krupierem na żywo 0% |
| Maksymalna wygrana z darmowych spinów | 50 €, o ile oferta nie określa inaczej |
| Sloty z darmowymi spinami | Darmowe spiny obejmują sloty Gates of Olympus, Aztec Magic, Aztec Magic Deluxe, Johnny Cash, Platinum Lightning oraz Platinum Lightning Deluxe |

W praktyce bonus rozlicza się więc na slotach, bo gry na żywo nie wliczają się do obrotu. Przed aktywacją pakietu Incaspin warto porównać te warunki z własnym stylem gry.

## Promocje i cashback w Incaspin
Poza pakietem powitalnym Incaspin Casino oferuje trzy kolejne promocje. W Incaspin pierwszą z nich jest Weekly Cashback, czyli tygodniowy zwrot do 25% strat netto, przy czym jego wysokość zależy od aktywności gracza i jego statusu w programie lojalnościowym. Dwie pozostałe oferty to doładowania wpłaty, które zestawia poniższa tabela.

| Promocja | Bonus | Min. wpłata | Obrót |
|---|---|---|---|
| Highroller Bonus | 50% do 500 € | 300 € | 40x bonus |
| Sunday Reload | 25% do 100 € | 15 € | 40x |
| Weekly Cashback | do 25% tygodniowych strat netto | - | - |

Highroller Bonus jest przeznaczony dla graczy, którzy wykorzystali wszystkie bonusy z kasynowego pakietu powitalnego, i można z niego korzystać co 30 dni. Sunday Reload obowiązuje w niedziele, więc w Incaspin jest to oferta dla graczy, którzy wpłacają właśnie w tym dniu. Przy wyborze promocji w Incaspin warto zacząć od progu minimalnej wpłaty, bo od niego zależy dostęp do oferty.

## Program lojalnościowy Incaspin
Program lojalnościowy Boomerang nagradza grę o prawdziwe pieniądze na slotach punktami Boomerang Points (BP). Liczą się dwa osobne wskaźniki: suma wszystkich zdobytych punktów decyduje o randze, a punkty do wydania gracz przeznacza na otwieranie skrzyń z nagrodami, co nie obniża rangi. Im wyższa ranga, tym więcej BP gracz otrzymuje za każde 10 € stawki na slotach:

| Ranga | Wymagane BP | BP za 10 € stawki na slotach |
|---|---|---|
| Scout | 0 | 100 |
| Shaman | 25 000 | 150 |
| Chief | 150 000 | 200 |
| Emperor | 1 500 000 | 300 |
| Legend | 10 000 000 | 400 |
| Inca | 60 000 000 | 500 |

Punkty to jednak nie wszystko. W Incaspin działają też elementy grywalizacji: Wheel of Fortune z losowanymi nagrodami, Points Store, w którym zdobyte BP można wymienić na nagrody, oraz misje dzienne, tygodniowe i bezterminowe, a za te ostatnie można zdobyć do 100 000 BP. Skrzynie z nagrodami zawierają premie gotówkowe, darmowe spiny i punkty BP. Co ważne dla wypłat, ranga lojalnościowa może zwiększać limity wypłat, więc program Incaspin ma znaczenie także poza samym zbieraniem punktów.

## Gry w Incaspin Casino
Podstawę oferty Incaspin Casino stanowi biblioteka, która liczy ponad 5000 tytułów. Najważniejsze są sloty i kasyno na żywo, ale lobby sięga dalej: obejmuje ruletkę, blackjacka, bakarata i poker, a także gry stołowe, gry natychmiastowe i gry typu crash, w których liczy się szybkość rundy. Osobne kategorie zajmują sloty z funkcją Bonus Buy, jackpoty, gry własne kasyna, tytuły z grupy Books oraz sloty z kategorii Drops & Wins. Taki podział pozwala wybrać grę według stylu, od spokojnej rozgrywki po szybkie rundy. Incaspin porządkuje całość w kategorie, więc szczegóły dotyczące slotów, kasyna na żywo oraz gier stołowych, crash i błyskawicznych opisują kolejne podrozdziały. Wybór jest szeroki także dlatego, że kategorie różnią się tempem: w jednych liczy się szybkość rundy, w innych dłuższa sesja przy stole lub automacie, więc w Incaspin wybór nie ogranicza się do jednego stylu gry.

### Sloty i jackpoty
W kategorii slotów znajdują się między innymi Gates of Olympus, Big Bass Splash, Book of Khonsu, Burning Chilli X oraz Mad Jesters: Hold & Win. Ten ostatni należy do slotów z mechaniką Hold & Win, w której wybrane symbole zostają na planszy, a gracz otrzymuje dodatkowe obroty z zablokowanymi symbolami. Osobną grupę tworzą jackpoty, takie jak Break The Piggy Bank, Crown of Fire Jackpot Play i Shining Hot 40 Jackpot Play. Jackpot to nagroda, której wartość wykracza poza zwykłą wygraną ze slotu, dlatego przed rozpoczęciem gry warto przeczytać opis konkretnego tytułu. Incaspin łączy więc klasyczne i nowsze automaty w jednym katalogu.

### Kasyno na żywo
Kasyno na żywo to gry prowadzone w czasie rzeczywistym przez krupiera. W lobby Incaspin znajdują się warianty ruletki: Lightning Roulette, Red Door Roulette i Gates of Olympus Roulette. Do gier karcianych i kościanych należą Speed Baccarat, Sic Bo oraz Dragon Tiger, a miłośników formuły teleturnieju przyciągają Crazy Time, Sweet Bonanza CandyLand i Ice Fishing. W tej samej sekcji działa także Disco Balls. Taki podział pokazuje, że oferta na żywo obejmuje zarówno klasyczne stoły, jak i gry w stylu show. Warto pamiętać, że gry z krupierem na żywo wliczają się do obrotu bonusowego w 0%, więc nie pomagają w rozliczeniu bonusu.

### Gry stołowe, crash i błyskawiczne
Gry stołowe w lobby obejmują ruletkę, blackjacka, bakarata i poker. Obok nich działa oferta błyskawiczna i typu crash, czyli gier o krótkich rundach, w których wynik zależy od rosnącego mnożnika. Do tej grupy należą Chicken Road, Chicken Road 2, Plinko, Plinko 2, Golden Plinko, Tower Rush oraz Aviamasters. Kasyno prezentuje też własne gry: Dragon Pots, MegaBlock, Chicken Coin, Joker's Clash i Plinko1000, a obok nich wspomniane już Chicken Road i Chicken Road 2. W Incaspin gry własne uzupełniają tytuły zewnętrznych dostawców. Gry stołowe sprawdzają się u osób, które wolą podejmować decyzje we własnym tempie, a tytuły błyskawiczne u tych, którzy chcą krótkich rund. Szybkie rundy wymagają jednak uwagi przy ustalaniu budżetu.

## Dostawcy gier w Incaspin
Katalog Incaspin Casino buduje wielu dostawców, a wśród nich wyróżniają się Pragmatic Play, znany ze slotów, oraz Evolution, kojarzony z grami na żywo. Studia te odpowiadają za sloty, gry stołowe i transmisje z krupierem, więc to od nich zależy, jak wygląda codzienny wybór w lobby. Poniżej zebrano wybranych twórców, których tytuły trafiają do oferty:

- Pragmatic Play
- Evolution
- Playtech
- NetEnt
- Microgaming
- Hacksaw Gaming
- Nolimit City
- Push Gaming

To tylko część listy, ponieważ lobby obejmuje znacznie więcej studiów. Dzięki temu oferta Incaspin nie opiera się na jednym źródle, a gracze w Incaspin mają szeroki wybór.

## Metody płatności i wpłaty
Wpłaty w Incaspin Casino obsługują cztery grupy metod: karty płatnicze, portfele elektroniczne, przelew bankowy i kryptowaluty. Kasyno nie pobiera opłat za wpłaty, ale zewnętrzni dostawcy płatności mogą naliczać własne koszty. Limity zależą od metody, a pierwsza wpłata na pakiet powitalny wymaga 20 €:

| Metoda | Min. | Maks. | Czas |
|---|---|---|---|
| Visa, Mastercard, Revolut, Skrill | 15 € | 4000 € | natychmiast |
| Paysafecard | 15 € | 1000 € | natychmiast |
| Neteller, Jeton | 10 € | 5000 € | natychmiast |
| Apple Pay, Google Pay | 10 € | 5000 € | natychmiast |
| Przelew bankowy | 10 € | 5000 € | tego samego dnia do 3 dni roboczych |
| Bitcoin, Ethereum, Litecoin | 15 € w ekwiwalencie | 5000 € w ekwiwalencie | natychmiast, potwierdzenie transakcji może się różnić |
| Dogecoin | 10 € w ekwiwalencie | 5000 € w ekwiwalencie | natychmiast, potwierdzenie transakcji może się różnić |

Sama wpłata przebiega w kilku krokach: po zalogowaniu gracz otwiera kasę, wybiera metodę, wpisuje kwotę mieszczącą się w limitach i potwierdza transakcję u dostawcy płatności. Po zaksięgowaniu wystarczy sprawdzić saldo konta, a wpłata w Incaspin w większości metod trafia na konto od razu.

### Wypłaty i czas realizacji
Kasyno realizuje wypłaty przez Visa OCT, Mastercard Payment Transfer, Skrill, Neteller, Jeton, przelew bankowy oraz kryptowaluty: Bitcoin, Ethereum, Litecoin i Dogecoin. Zlecenie wypłaty składa się w sześciu krokach:

1. Zalogować się i otworzyć kasę lub sekcję wypłat.
2. Wybrać dostępną metodę wypłaty, najlepiej tę, której użyto do wpłaty.
3. Wpisać kwotę wypłaty i sprawdzić swój limit.
4. Przejść wymaganą weryfikację tożsamości lub metody płatności.
5. Potwierdzić zlecenie wypłaty.
6. Odczekać do 72 godzin na wewnętrzne przetwarzanie, a potem na rozliczenie przez dostawcę płatności.

Na czas wypłaty składa się więc kontrola po stronie kasyna oraz czas dostawcy: w przypadku przelewu bankowego dochodzi od 1 do 5 dni roboczych, a przy kryptowalutach potwierdzenie w sieci blockchain. Minimalna kwota wypłaty wynosi od 50 do 120 €, w zależności od kraju lub metody płatności. Wpłacone środki trzeba obrócić co najmniej trzykrotnie, a do pełnej weryfikacji konta żadna wypłata nie jest realizowana. Maksymalne limity mogą zależeć od rangi lojalnościowej i są widoczne w kasie. Kasyno nie pobiera opłat, ale zewnętrzne koszty banku lub dostawcy mogą wystąpić, dlatego w Incaspin warto zaplanować wypłatę z wyprzedzeniem.

### Limity i waluty
Konto w Incaspin obsługuje sześć walut: cztery tradycyjne, czyli EUR, BRL, CAD i AUD, oraz dwie kryptowaluty, BTC i ETH. Taki podział ma znaczenie w praktyce, ponieważ kurs kryptowalut zmienia się w czasie, a waluty tradycyjne mają stabilniejszą wartość. Limity wypłat zależą natomiast od metody. W przypadku portfeli Skrill i Neteller maksymalna kwota pojedynczej wypłaty wynosi 5000 €. Przelew bankowy nie wiąże się z opłatą po stronie kasyna, ale banki pośredniczące mogą naliczyć do 16 € kosztów. W praktyce przed zleceniem wypłaty warto sprawdzić w kasie zarówno limit, jak i koszty wybranej metody, ponieważ obie wartości różnią się między sposobami płatności, a ich porównanie pozwala uniknąć niespodzianek.

## Gra mobilna: aplikacja PWA Incaspin
Na telefonie Incaspin Casino działa jako Progressive Web App (PWA), czyli strona internetowa zapisana na ekranie głównym urządzenia i uruchamiana jak zwykła aplikacja. Instalacja odbywa się bezpośrednio w przeglądarce, bez sklepu z aplikacjami, i jest dostępna zarówno na iOS, jak i na Androidzie. Po instalacji gracz ma dostęp do sekcji Kasyno, Kasyno na żywo, Sport, E-sport, Bonusy, Promocje, Wheel of Fortune, Lojalność oraz Misje. Ikona na ekranie głównym otwiera serwis od razu, bez wpisywania adresu w przeglądarce.

Na iPhonie i iPadzie instalacja wymaga czterech kroków:

1. Otworzyć Incaspin w przeglądarce Safari.
2. Stuknąć przycisk Udostępnij.
3. Wybrać opcję Dodaj do ekranu początkowego.
4. Wpisać nazwę i stuknąć Dodaj.

Na Androidzie także wystarczą cztery kroki:

1. Otworzyć Incaspin w przeglądarce mobilnej.
2. Wybrać opcję Zainstaluj aplikację lub Dodaj do ekranu głównego.
3. Potwierdzić instalację.
4. Uruchomić grę z ikony na ekranie głównym.

## Zakłady sportowe i e-sport w Incaspin
Dział sportowy obejmuje zakłady na piłkę nożną, tenisa, koszykówkę, hokej na lodzie, krykieta i siatkówkę, a także na e-sport, w którym dostępne są między innymi Counter-Strike, eFootball, eBasketball i eTennis. Wśród dyscyplin są także baseball, snooker, piłka ręczna, tenis stołowy, szachy, Formuła 1, wyścigi konne, boks, MMA i dart, więc wybór nie ogranicza się do najpopularniejszych sportów. Rynki obejmują wynik 1x2, podwójną szansę, sumy, handicap, akumulatory i zakłady na żywo, więc gracz dobiera typ zakładu do wydarzenia. Osobną ofertą jest Sportsbook Welcome Package, niezależny od pakietu kasynowego i rozłożony na trzy pierwsze wpłaty sportowe:

- pierwsza wpłata sportowa: 100% do 100 €
- druga wpłata sportowa: 75% do 150 €
- trzecia wpłata sportowa: 50% do 200 €

Łącznie pakiet sięga do 450 €, minimalna wpłata wynosi 20 €, a obrót to 5x bonus sportowy. Dla Incaspin oznacza to, że gracz kasynowy i gracz sportowy mają osobne bonusy powitalne, każdy z własnymi warunkami.

## Odpowiedzialna gra
Odpowiedzialna gra zaczyna się od limitu wieku: korzystać z serwisu mogą wyłącznie osoby, które ukończyły 18 lat. Narzędzia do kontroli budżetu znajdują się w koncie, w sekcji Moje konto, a w niej w zakładce Odpowiedzialna gra. Limity wpłat obowiązują w okresach dziennym (kroczące 24 godziny), tygodniowym (kroczące 168 godzin) i miesięcznym (kroczące 720 godzin). Obniżenie limitu działa od razu, natomiast podwyższenie lub usunięcie wchodzi w życie po 24 godzinach, więc limit można szybko zaostrzyć, ale nie można go spontanicznie poluzować. Dostępne są także limity zakładów, limity strat i limity czasu sesji. Samowykluczenie blokuje dostęp do konta na wybrany okres od 3 miesięcy do 5 lat albo bezterminowo, a gdy gracz nie wskaże czasu, obowiązuje 6 miesięcy. W tym okresie nie można wpłacać ani wypłacać środków. Incaspin udostępnia te narzędzia w koncie gracza, a pomoc i podstawowe zasady to:

- czat na żywo i e-mail kasyna, a także Gambling Therapy, Gamblers Anonymous i test samooceny BeGambleAware
- hazard nie jest źródłem dochodu
- nie warto odrabiać strat ani grać pod wpływem alkoholu lub narkotyków
- warto ustalić budżet i robić przerwy

## Obsługa klienta
Obsługa klienta jest dostępna całą dobę, przez siedem dni w tygodniu. Czat na żywo odpowiada bez przerwy (24/7), a osoby, które wolą pisać, mogą skontaktować się przez e-mail pod adresem support@incaspin.com. Uzupełnieniem jest sekcja FAQ z odpowiedziami na najczęstsze pytania, do której warto zajrzeć przed pierwszym kontaktem, bo wiele spraw da się wyjaśnić od razu. Zespół wsparcia pracuje po angielsku i w innych językach. Przy zgłoszeniu pomaga przygotowanie danych konta, a w sprawach płatności także szczegółów transakcji, ponieważ ułatwia to sprawdzenie sprawy. Odpowiedź przychodzi bez względu na porę dnia, więc problem z kontem lub wpłatą nie musi czekać do rana.

## Najczęstsze pytania o Incaspin Casino
- **Czy do bonusu powitalnego potrzebny jest kod promocyjny?** Nie, kasyno przyznaje bonusy z pakietu powitalnego automatycznie. Wpisanie kodu przy bonusie z tego pakietu pozbawia gracza prawa do tego bonusu, więc kodu lepiej nie podawać.
- **Jaka jest minimalna wpłata na pakiet powitalny?** Pierwsza wpłata wymaga 20 €, a oferta przewiduje progi wpłat 20 €, 50 € i 300 €.
- **Jak długo trwa wypłata?** Do 72 godzin trwa kontrola po stronie kasyna, po niej następuje rozliczenie przez operatora płatności, który ma własny czas realizacji. Całość zależy więc od wybranej metody.
- **Jak zalogować się na konto Inca Spin?** Wystarczy wpisać e-mail i hasło z rejestracji. Gdy hasło jest nieznane, na ekranie logowania działa opcja przypomnienia hasła, a instrukcję resetu kasyno wysyła e-mailem.
- **Czy Incaspin Casino ma aplikację mobilną?** Incaspin działa jako Progressive Web App instalowana bezpośrednio z przeglądarki, bez sklepu z aplikacjami. Ikona trafia na ekran główny telefonu, a po instalacji serwis otwiera się jednym stuknięciem.

## Podsumowanie
Incaspin łączy kasyno, kasyno na żywo i zakłady sportowe w jednym miejscu, a dodatkowo oferuje grę przez PWA oraz obsługę klienta dostępną całą dobę. Taki zestaw odpowiada graczom, którzy cenią szeroką ofertę i prostą rejestrację. Przed wpłatą warto przeczytać warunki bonusów oraz sprawdzić limity wybranej metody płatności, bo to one decydują o realnej wartości oferty w Incaspin. Korzystać z serwisu mogą tylko osoby od 18. roku życia. Hazard nie jest źródłem dochodu, dlatego warto ustalić budżet, nie odrabiać strat i robić przerwy.

---

## BLOCK BRIEF
Block: b03, H2 "Licence and Safety at Incaspin Casino" (under H1 "Incaspin Casino: recenzja kasyna dla polskich graczy")
Page heading (output language): "Licencja i bezpieczeństwo w Incaspin Casino"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 132-168 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 168, but never beyond 201 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Incaspin": exactly 2 time(s)
- "Inca Spin": 0 here, but the brand name may appear when the text reads naturally: at most 2 time(s) in this block (one per 50 words)
- "Incaspin casino": exactly 1 time(s)
Entities to cover [priority 1-10]:
- Gambling Licence [10]
- Operator [8]
- Payment Agent [6]
- Data Security [6]
- Player Responsibility [4]
Entity Connections to state explicitly [priority]:
- Gambling Licence → is issued by → the licensing authority [8]
- Operator → runs → the Online Casino [8]
- Encryption and Firewall → protect → account and payment data [6]
Summary: Who licenses and runs the casino (authority, number, jurisdiction, operator company, payment agent) and how accounts and verification documents are protected technically.
Copywriter Notes: Lead with the Gambling Licence: state it exactly as given (authority Tobique Gaming Commission, licence number 0000158, jurisdiction Tobique). Then the Operator (Legasta Technologies SRL, Costa Rica) and the Payment Agent (OptaStream Innovations Limited). Then security measures: HTTPS/TLS 1.3, SSL certificates, WAF and DDoS protection, identity checks and responsible-gaming controls, and that verification documents are encrypted and processed securely. NEVER say or imply that the casino is licensed for, legal in or approved in Poland; add one calm practical sentence that rules for online gambling differ between countries and that players should check whether the offer is allowed for them. Do not mention a company registration number, an address or any licence other than the one given. Use "Incaspin" exactly twice and "Incaspin casino" (written as the name Incaspin Casino) exactly once.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_general.licences: [{"authority": "Tobique Gaming Commission", "licence_number": "0000158", "jurisdiction": "Tobique"}]
- brandinfo_general.operator.company_name: Legasta Technologies SRL
- brandinfo_general.operator.jurisdiction: Costa Rica
- brandinfo_general.payment_agent.company_name: OptaStream Innovations Limited
- brandinfo_general.business_overview.security: HTTPS/TLS 1.3, SSL certificates, WAF and DDoS protection; identity checks and responsible-gaming controls
- brandinfo_privacy_policy.privacy_policy.data_security.verification_documents: The site states that verification documents are encrypted and processed securely

---

## FIX MODE
This block was already written but FAILED the checks. Rewrite it so that ALL problems below are solved, keep everything that is already fine, and still respect every requirement of the block brief. Follow the numbers in the problem list literally (if a keyword appears 3 times and must appear 1, remove exactly two). After the fix re-check every other hard constraint: shortening can remove a required keyword or entity. Do not mention the fixes in the text.

CURRENT TEXT:
Licencja hazardowa Incaspin Casino została wydana przez Tobique Gaming Commission pod numerem 0000158, a jurysdykcją jest Tobique. Kasyno Incaspin prowadzi spółka Legasta Technologies SRL z Kostaryki, natomiast obsługą płatności zajmuje się osobny podmiot, OptaStream Innovations Limited z Cypru. Podział ról wygląda więc tak: jedna firma odpowiada za serwis, druga za przepływ środków. Reguły dotyczące gier online różnią się między państwami, dlatego polski gracz powinien samodzielnie sprawdzić, czy korzystanie z takiej oferty jest dla niego dozwolone.

Po stronie technicznej platforma stosuje protokoły HTTPS i TLS 1.3 oraz certyfikaty SSL, które chronią dane konta tam, gdzie padają wrażliwe informacje: przy rejestracji, płatnościach i przesyłaniu dokumentów. Zaporę aplikacyjną (WAF) i ochronę przed atakami DDoS uzupełniają kontrole tożsamości oraz narzędzia odpowiedzialnej gry. Dokumenty weryfikacyjne są szyfrowane i przetwarzane w bezpieczny sposób. Dla Incaspin oznacza to ochronę opartą na kilku warstwach, a nie na jednym zabezpieczeniu.

PROBLEMS TO FIX:
- Rewrite this sentence in b03 with different wording and a different angle (for example: before opening an account a Polish player should check for themselves how the rules of their own country treat an offer run by a foreign operator). Keep it neutral, do not say or imply that the casino is licensed, legal or approved in Poland, and keep all other facts unchanged. The tracked keywords must stay as they are in the block: "Incaspin" twice and "Incaspin Casino" once (none of them is in the sentence being changed).
