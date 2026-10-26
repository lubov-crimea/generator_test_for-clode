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
Country / GEO: IT
Language: Italian (it). Write ONLY in this language.
Page intent: Brand-related (navigational and informational) page about the Incaspin online casino for players from Italy: overview, registration and login, welcome bonus with conditions and promo-code rule, further promotions, games and providers, sports betting, payments and withdrawals, verification, mobile web app, VIP and loyalty programme, safety and licence, responsible gambling, support and FAQ. All brand-specific facts come from the AffBulk knowledge base incaspin-new.
All tracked keywords: Incaspin, Inca Spin, Incaspin casino
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "incaspin-new"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Incaspin Casino: bonus, registrazione, giochi e prelievi (75-95 words): Short introduction: what the online casino is, which areas it covers (casino, live casino, sports betting, esports) and what the page explains (bonus, registration, games, payments, app, safety).
b02   H2 Incaspin Casino in breve (154-196 words): Overview of the platform: launch year, operator, licence details, game categories, currencies and support availability.
b03   H2 Il casinò in sintesi (66-84 words): A compact fact sheet of the casino: operator, licence, launch year, support languages, currencies, payment methods, welcome bonus, cashback, minimum deposit and support e-mail.
b04   H2 Come registrarsi su Incaspin Casino (141-179 words): How to register: one introductory sentence, a numbered list of the five sign-up steps and the account restrictions (one account per person, 18+).
b05     H3 Accesso e sicurezza dell'account (88-112 words): How to log in, how to reset a forgotten password, how to switch on two-factor authentication and what the account area contains.
b06   H2 Il bonus di benvenuto di Incaspin Casino (211-269 words): The welcome package: up to 2.750 EUR and 275 free spins over three deposits, with a list of the three steps and the slots for the free spins.
b07     H3 Condizioni del bonus in sintesi (106-134 words): A table of the key conditions of the welcome package: minimum deposit, wagering, validity, maximum bet, game contribution and further rules.
b08     H3 Codice promo e attivazione (82-105 words): No promo code is needed for the welcome package: bonuses are credited automatically and entering a code disqualifies the player from that bonus.
b09   H2 Altre promozioni e cashback su Incaspin (141-179 words): The ongoing promotions after the welcome package: Highroller Bonus, Sunday Reload and Weekly Cashback with a comparison table.
b10   H2 I giochi di Incaspin Casino (132-168 words): Overview of the game library: size, game types and signposts to the subsections for slots, live casino, table games and jackpots, and providers.
b11     H3 Slot (105-132 words): Slots at the casino with concrete titles from the game list.
b12     H3 Casinò live (105-132 words): Live casino games with concrete titles from the game list.
b13     H3 Giochi da tavolo, jackpot e crash game (121-154 words): Table games, jackpots, crash and instant games and the in-house originals.
b14     H3 Fornitori di giochi (82-105 words): The studios behind the games: a selection of well-known providers from the provider list.
b15   H2 Scommesse sportive ed eSport su Incaspin (165-210 words): The sportsbook: sports and esports covered, bet types, leagues and the sportsbook welcome package.
b16   H2 Depositi e metodi di pagamento (194-246 words): Deposit methods in a table with minimum, maximum and speed, plus the deposit steps and fee remarks.
b17   H2 Prelievi su Incaspin (209-266 words): How withdrawals work: numbered steps, processing time, minimum and maximum amounts and the conditions before a payout.
b18     H3 Verifica del conto (KYC) (106-134 words): Why and how the account is verified: required documents, review time and the consequence of false documents.
b19   H2 Gioco da mobile: Incaspin su Android e iOS (132-168 words): Mobile play through the progressive web app: no store download, installation steps for iOS and Android and the available sections.
b20   H2 Programma VIP e fedeltà su Incaspin (209-266 words): The Boomerang loyalty programme: points, the six ranks in a table, missions, wheel of fortune and reward chests.
b21   H2 Sicurezza e licenza di Incaspin Casino (165-210 words): Safety facts: licence and operator, payment agent, encryption and attack protection, document handling and the 18+ rule.
b22   H2 Gioco responsabile (192-245 words): Responsible-gambling tools: deposit limits, other limits, self-exclusion, support organisations, protection of minors and practical warnings.
b23   H2 Assistenza clienti (88-112 words): Support channels: 24/7 live chat, e-mail with the address, FAQ and the languages of the support.
b24   H2 Domande frequenti su Incaspin Casino (220-280 words): A FAQ list with six questions: promo code, age, withdrawals, mobile access, multiple accounts and currencies, each answered in one or two sentences.
b25   H2 Conclusione (66-84 words): A short wrap-up of the strengths named on the page and a reminder to play responsibly.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Incaspin Casino: bonus, registrazione, giochi e prelievi
Incaspin è un casinò online che riunisce slot, casinò live, scommesse sportive ed eSport in un solo account, riservato ai maggiorenni (18+). Il pacchetto di benvenuto arriva fino a 2.750 € più 275 giri gratis. La pagina è pensata per i giocatori italiani e segue il percorso di un nuovo iscritto: registrazione, bonus e giochi, poi depositi e prelievi, app mobile, sicurezza e gioco responsabile. Ogni sezione riporta cifre e condizioni, così da valutare l'offerta prima di iscriversi.

## Incaspin Casino in breve
Incaspin Casino è una piattaforma di gioco online attiva dal 2025. Il nome si incontra spesso scritto in due parole, Inca Spin, ma la grafia del marchio è Incaspin. Sullo stesso sito convivono quattro aree: casinò online, casinò live, sportsbook ed eSport, con più di 5.000 giochi tra cui scegliere, dalle slot ai tavoli con croupier dal vivo.

Dietro la piattaforma c'è l'operatore Legasta Technologies SRL, registrato in Costa Rica, che gestisce il casinò e risponde del servizio offerto ai giocatori. La licenza di Incaspin è rilasciata dalla Tobique Gaming Commission, con numero 0000158 e giurisdizione Tobique. Operatore e licenza compaiono anche nella tabella che segue, insieme agli altri dati essenziali della piattaforma, da controllare con attenzione prima di aprire un conto.

Il conto può essere tenuto in EUR, BRL, CAD, AUD, BTC ed ETH, quindi sia in valute tradizionali sia in criptovalute. Per i dubbi sul conto Incaspin mette a disposizione un'assistenza clienti attiva 24/7.

## Il casinò in sintesi
| Parametro | Dettaglio |
|---|---|
| Operatore | Legasta Technologies SRL |
| Licenza | Tobique Gaming Commission, n. 0000158 |
| Anno di lancio | 2025 |
| Lingue dell'assistenza | Inglese e altre lingue |
| Valute | euro (EUR), BRL, CAD, AUD, BTC, ETH |
| Metodi di pagamento | Visa, Mastercard, Apple Pay, Google Pay, Skrill, Neteller, criptovalute, bonifico bancario |
| Bonus di benvenuto | Fino a 2.750 € + 275 giri gratis |
| Cashback | Fino al 25% delle perdite nette settimanali |
| Deposito minimo | 20 € |
| Assistenza via e-mail | support@incaspin.com |

## Come registrarsi su Incaspin Casino
La registrazione su Incaspin richiede soltanto un indirizzo e-mail. Il giocatore apre il conto con l'e-mail e una password e dichiara di avere almeno 18 anni, in cinque passaggi che seguono quest'ordine:

1. Aprire incaspin.com e selezionare l'opzione di registrazione.
2. Inserire un indirizzo e-mail.
3. Creare una password.
4. Confermare di avere almeno 18 anni.
5. Inviare il modulo di registrazione.

Conviene usare un indirizzo e-mail a cui si ha accesso stabile, perché la procedura di recupero della password passa da lì. Ogni persona può avere un solo conto, e il vincolo vale anche per nucleo familiare, indirizzo IP e computer: due iscrizioni dalla stessa casa o dallo stesso dispositivo non sono ammesse. Se Incaspin individua un account doppio, può sospenderlo o chiuderlo e annullare le puntate, i bonus e le vincite collegati. Il limite di età è 18 anni, perciò la conferma al quarto passaggio è una condizione per aprire il conto e non una semplice formalità.

### Accesso e sicurezza dell'account
Per entrare nel conto Incaspin servono l'e-mail e la password scelte in fase di iscrizione. Chi dimentica la password usa il link Password dimenticata nella schermata di accesso e segue le istruzioni di reimpostazione ricevute per e-mail. Per proteggere meglio il conto, nelle impostazioni dell'account si può attivare l'autenticazione a due fattori, che affianca alla password un secondo controllo. Una volta dentro, l'area personale raccoglie i dati del profilo e le preferenze di valuta, i metodi di pagamento, la cronologia di gioco e di scommessa, lo stato dei bonus e i limiti di gioco responsabile.

## Il bonus di benvenuto di Incaspin Casino
Incaspin Casino accoglie i nuovi iscritti con il Casino Welcome Package, un pacchetto di benvenuto che arriva fino a 2.750 € più 275 giri gratis, cioè giri su una slot con la puntata a carico del casinò. Il bonus non si riceve in un'unica soluzione: è distribuito sui primi tre depositi, e ciascuno ha la propria percentuale e il proprio tetto. I tre tetti sommati danno appunto 2.750 €, mentre i giri gratis si concentrano nel primo e nel terzo deposito.

- Primo deposito: fino a 1.000 € più 200 giri gratis, la quota più consistente dei giri.
- Secondo deposito: 100% fino a 1.000 €, un bonus in denaro pari alla somma versata entro il tetto.
- Terzo deposito: 75% fino a 750 € più 75 giri gratis, che chiudono il pacchetto.

Incaspin riserva i giri gratis a slot selezionate, tra cui Gates of Olympus, Aztec Magic e Johnny Cash, quindi il pacchetto è pensato soprattutto per chi preferisce le slot ai tavoli. Il primo deposito è il punto di forza per questo tipo di giocatore: da solo porta 200 dei 275 giri. Il secondo deposito, che non porta giri gratis, offre invece un bonus che raddoppia la somma versata, nei limiti del tetto. Prima di depositare conviene comunque leggere le condizioni del bonus di Incaspin: la tabella che segue riassume puntata, validità e contributo dei vari giochi al requisito.

### Condizioni del bonus in sintesi
Le condizioni del pacchetto di benvenuto di Incaspin sono raccolte in questa tabella.

| Condizione | Dettaglio |
|---|---|
| Deposito minimo | 20 € sul primo deposito, con scaglioni da 20 €, 50 € e 300 € |
| Requisito di puntata | 35x il bonus sul secondo e sul terzo deposito, 40x come regola generale salvo diversa indicazione |
| Validità | 7 giorni per i bonus del pacchetto |
| Puntata massima | 5 € sulle slot e 10 € sui giochi live durante la puntata del bonus |
| Bonus attivi | Un solo bonus alla volta, che si può mettere in pausa, ma il timer di scadenza continua |
| Prelievo delle vincite | Solo dopo aver soddisfatto i requisiti di puntata |
| Contributo dei giochi | Slot 100%, giochi di carte, roulette, poker e video poker 5%, giochi live 0% |
| Bonus sticky | Si gioca prima il saldo in denaro reale |
| Vincite massime dai giri gratis | 50 € per i giri gratis di iscrizione, salvo diversa indicazione dell'offerta |

### Codice promo e attivazione
Il pacchetto di benvenuto non richiede alcun codice promo. I bonus del pacchetto vengono accreditati automaticamente, quindi al giocatore basta effettuare i depositi previsti, senza passaggi aggiuntivi. C'è però un dettaglio da ricordare: inserire un codice promo per un bonus del pacchetto rende il giocatore non idoneo a quel bonus. Per questo, sul conto Incaspin, il pacchetto va richiesto così com'è, senza codici aggiuntivi. Prima del primo deposito conviene leggere con attenzione le condizioni dell'offerta, riassunte nella tabella qui sopra, a partire da puntata e validità.

## Altre promozioni e cashback su Incaspin
Dopo il pacchetto di benvenuto, Incaspin propone promozioni ricorrenti per chi continua a giocare: una ricarica riservata ai depositi più alti, una ricarica domenicale e un cashback settimanale. Le tre offerte si distinguono per importo, deposito minimo e requisito di puntata, e la tabella le mette a confronto.

| Promozione | Bonus | Deposito minimo | Requisito di puntata |
|---|---|---|---|
| Highroller Bonus | 50% fino a 500 € | 300 € | 40x il bonus |
| Sunday Reload | 25% fino a 100 € | 15 € | 40x |
| Cashback settimanale | Fino al 25% delle perdite nette settimanali | n/d | n/d |

L'Highroller Bonus è la ricarica più alta: premia i giocatori che hanno già usato tutti i bonus del pacchetto di benvenuto e si può richiedere ogni 30 giorni, con un deposito minimo di 300 €. Sunday Reload è invece una ricarica settimanale del 25% fino a 100 €, disponibile la domenica e con una soglia d'ingresso più bassa, 15 €. Il cashback settimanale di Incaspin restituisce una quota delle perdite nette della settimana, fino al 25%, e l'importo effettivo dipende dall'attività e dallo status di fedeltà del giocatore. Il requisito di puntata di 40x riguarda le due ricariche, quindi conviene verificarlo prima di attivarle. Missioni, ruota e forzieri dei premi sono trattati nella sezione sul programma fedeltà.

## I giochi di Incaspin Casino
Incaspin mette a disposizione una libreria di più di 5.000 giochi, organizzata per categorie in modo che il giocatore parta dal genere che preferisce. L'offerta comprende slot, casinò live, roulette, blackjack, baccarat e poker, ma anche giochi istantanei, crash game, bonus buy e jackpot, oltre ai giochi originali, ai titoli in stile Book e alle slot Drops & Wins. Le categorie si rivolgono a gusti diversi: le slot a chi cerca partite rapide, il casinò live a chi vuole un croupier in carne e ossa, i giochi da tavolo a chi preferisce regole classiche. Le sezioni che seguono descrivono le slot, il casinò live, i giochi da tavolo con jackpot e crash game e i fornitori che sviluppano i titoli. I giochi di Incaspin si possono quindi esplorare una categoria alla volta, senza scorrere l'intero catalogo.

### Slot
Le slot sono il primo genere dell'elenco e raccolgono titoli con meccaniche diverse. Alla formula hold and win appartengono Mad Jesters: Hold & Win, Coin Strike Hold and Win e Double Dragon Gold: Hold & Win, in cui di norma i simboli speciali restano fissi sui rulli durante i respin. Le slot in stile Book, con il simbolo che si espande durante il bonus, includono Book of Khonsu e Book of Hidden Tombs. Tra i nomi più noti figurano anche Gates of Olympus, Big Bass Splash e Burning Chilli X, utili come punto di partenza per chi non conosce ancora il catalogo di Incaspin. Per ogni titolo conviene leggere in gioco le regole specifiche, perché funzioni e dinamiche cambiano da una slot all'altra.

### Casinò live
Il casinò live riunisce giochi condotti da un croupier o da un presentatore in diretta. Alla roulette appartengono Lightning Roulette, Red Door Roulette e Gates of Olympus Roulette, mentre Speed Baccarat e Dragon Tiger rappresentano i tavoli di carte e Sic Bo il gioco di dadi. Crazy Time, Sweet Bonanza CandyLand, Ice Fishing e Disco Balls sono invece game show, il cui format somiglia più a uno spettacolo televisivo che a un tavolo classico. Nel casinò live di Incaspin i titoli si dividono quindi in quattro famiglie: roulette, tavoli di carte, dadi e game show. Chi ama il ritmo di una partita guidata da un presentatore trova nei game show l'alternativa ai tavoli tradizionali.

### Giochi da tavolo, jackpot e crash game
I giochi da tavolo coprono roulette, blackjack, baccarat e poker, i classici per chi preferisce regole stabili e decisioni ponderate ai ritmi serrati dei rulli. Le regole sono note da tempo, quindi questi giochi si prestano anche a chi si avvicina ai tavoli per la prima volta. Su Incaspin completano slot e tavoli anche i jackpot, con titoli come Break The Piggy Bank, Halloween Jackpot, Crown of Fire Jackpot Play e Shining Hot 40 Jackpot Play, che offrono un'alternativa alle slot tradizionali.

Per le partite brevi ci sono i giochi istantanei e crash: Chicken Road, Plinko, Tower Rush e Aviamasters, partite che in genere durano pochi istanti e si ripetono rapidamente. A questo gruppo appartengono anche i giochi originali della casa, tra cui Chicken Road 2, Dragon Pots e MegaBlock, che Incaspin affianca ai titoli dei fornitori esterni.

### Fornitori di giochi
I giochi della libreria sono sviluppati da un lungo elenco di studi, decine di fornitori in tutto, che producono sia le slot sia i giochi live. Pragmatic Play, Evolution, NetEnt, Yggdrasil, Red Tiger, Big Time Gaming, Microgaming, Hacksaw Gaming, Nolimit City e Push Gaming sono tra i nomi più conosciuti del settore e compaiono tra i partner di Incaspin. Accanto a loro lavorano studi più piccoli, che portano temi e meccaniche diversi. Per il giocatore la presenza di molti fornitori significa un catalogo meno ripetitivo, con stili grafici e funzioni che cambiano da un titolo all'altro.

## Scommesse sportive ed eSport su Incaspin
Incaspin affianca al casinò uno sportsbook con una sezione dedicata agli eSport. Tra gli sport si trovano calcio, tennis, pallacanestro e hockey su ghiaccio, mentre per gli eSport sono previsti Counter-Strike, eFootball ed eBasketball. I campionati in vetrina comprendono UEFA Champions League, Premier League inglese, Serie A italiana, Bundesliga tedesca e LaLiga spagnola. Le scommesse vanno dall'esito 1x2 alla doppia chance, dai totali over/under all'handicap, fino alle combinazioni e alle puntate live, quindi lo sportsbook copre sia le giocate semplici sia quelle più articolate.

Il pacchetto di benvenuto dello sportsbook è separato da quello del casinò e arriva fino a 450 € sui primi tre depositi sportivi: il primo vale il 100% fino a 100 €, il secondo il 75% fino a 150 € e il terzo il 50% fino a 200 €. Il deposito minimo è di 20 €, il requisito di puntata è 5x e il bonus ha una validità di 14 giorni. Per soddisfare il requisito servono scommesse multiple (accumulator) di almeno 3 eventi, con quota minima di 1,40 per ogni selezione, quindi il pacchetto si adatta soprattutto a chi gioca combinazioni. Prima di scegliere il bonus sportivo conviene verificare queste soglie, perché le giocate singole non rientrano tra le scommesse valide.

## Depositi e metodi di pagamento
Incaspin accetta depositi con carte (Visa e Mastercard), portafogli elettronici come Skrill e Neteller, Revolut, Apple Pay e Google Pay, bonifico bancario e criptovalute. I limiti cambiano da un metodo all'altro: la tabella raggruppa i metodi che hanno gli stessi importi minimi e massimi, espressi in euro o nel loro equivalente in criptovalute.

| Metodo | Minimo | Massimo | Velocità |
|---|---|---|---|
| Visa, Mastercard, Revolut, Skrill | 15 € | 4.000 € | Istantanea |
| Paysafecard | 15 € | 1.000 € | Istantanea |
| Neteller, Jeton, Apple Pay, Google Pay (portafogli e pagamenti mobili) | 10 € | 5.000 € | Istantanea |
| Bonifico bancario | 10 € | 5.000 € | Dallo stesso giorno a 1-3 giorni lavorativi |
| Bitcoin, Ethereum, Litecoin | 15 € equivalenti | 5.000 € equivalenti | Istantanea, ma la conferma può variare |
| Dogecoin | 10 € equivalenti | 5.000 € equivalenti | Istantanea, ma la conferma può variare |

La maggior parte dei metodi accredita il deposito all'istante. Fanno eccezione il bonifico bancario, che può richiedere fino a 3 giorni lavorativi, e le criptovalute, per cui la conferma della transazione può variare. Il casinò non applica commissioni, ma il fornitore del pagamento può addebitare costi esterni. Su Incaspin si apre la sezione Deposito o la cassa, si sceglie il metodo, si inserisce l'importo entro i limiti del metodo e si conferma l'operazione seguendo le istruzioni del fornitore. Il bonus di benvenuto richiede un deposito di almeno 20 €, quindi conviene guardare anche questa soglia, oltre al minimo del metodo scelto, prima di versare la somma.

## Prelievi su Incaspin
I prelievi su Incaspin seguono una procedura in sei passaggi, che parte dalla cassa del conto e termina con l'elaborazione interna e il tempo del fornitore del pagamento:

1. Accedere al conto e aprire la cassa o la sezione Prelievi.
2. Scegliere un metodo di prelievo disponibile, preferibilmente quello usato per il deposito, se applicabile.
3. Inserire l'importo del prelievo e controllare il proprio limite personale.
4. Completare l'eventuale verifica di identità o del metodo di pagamento.
5. Confermare la richiesta di prelievo.
6. Attendere fino a 72 ore per l'elaborazione interna, seguite dal periodo di accredito del fornitore del pagamento.

L'importo minimo di prelievo va da 50 a 120 € a seconda del paese o del metodo di pagamento. Il massimo arriva a 15.000 € per Visa, Mastercard, bonifico bancario e per Bitcoin, Ethereum e Litecoin (in equivalente), e a 5.000 € per Skrill, Neteller e Jeton. I limiti massimi possono dipendere anche dal livello di fedeltà e sono visibili nella cassa. Il casinò non trattiene commissioni sui prelievi, mentre i fornitori possono applicare costi propri e, per il bonifico, la banca intermediaria può addebitare fino a 16 €. Per le vincite superiori a 10.000 € è previsto il pagamento in rate mensili fino a 10.000 €.

Due condizioni vanno rispettate prima di ogni richiesta: i depositi devono essere puntati almeno tre volte e nessun prelievo viene elaborato finché il conto non è completamente verificato. Per questo conviene completare la verifica in anticipo, come descritto nella sezione seguente.

### Verifica del conto (KYC)
Su Incaspin la verifica dell'identità può essere richiesta prima del primo prelievo e durante i controlli sui depositi, e finché il conto non è completamente verificato non viene elaborato alcun prelievo. I documenti richiesti sono questi:

- Passaporto, carta d'identità nazionale o patente di guida.
- Una bolletta recente o un estratto conto bancario.
- La prova del metodo di pagamento usato.
- Un selfie con il documento d'identità oppure un controllo d'identità dal vivo.

La maggior parte delle verifiche richiede da poche ore a un giorno, quindi caricare i documenti in anticipo evita ritardi al primo prelievo. I documenti devono essere autentici: una documentazione falsa o fraudolenta può portare al sequestro dei fondi depositati e delle vincite.

## Gioco da mobile: Incaspin su Android e iOS
Incaspin Casino non richiede alcun download da uno store: il gioco da mobile passa da una Progressive Web App (PWA), che si installa direttamente dal browser dello smartphone o del tablet. La PWA è disponibile per iOS e per Android e, una volta aggiunta alla schermata Home, si apre con la propria icona come un'app tradizionale. I passaggi cambiano di poco tra i due sistemi.

Su iPhone e iPad:

1. Aprire Incaspin in Safari su iPhone o iPad.
2. Toccare Condividi.
3. Selezionare Aggiungi alla schermata Home.
4. Scegliere un nome e toccare Aggiungi.

Su Android:

1. Aprire Incaspin nel browser del telefono.
2. Selezionare Installa app oppure Aggiungi alla schermata Home.
3. Confermare l'installazione.
4. Avviare l'app dall'icona sulla schermata Home.

Una volta installata, la PWA dà accesso alle sezioni principali: casinò, casinò live, sport, eSport, bonus, promozioni, ruota della fortuna, fedeltà e missioni.

## Programma VIP e fedeltà su Incaspin
Il programma fedeltà di Incaspin si chiama Boomerang e ruota attorno ai Boomerang Points (BP). I punti si guadagnano giocando con denaro reale alle slot: i BP accumulati nel tempo determinano il livello del giocatore, mentre i BP spendibili si possono scambiare con i forzieri premio e nello store dei punti. I livelli sono sei, e a ogni salita aumentano i BP ottenuti per ogni 10 € puntati sulle slot.

| Livello | BP richiesti | BP per 10 € puntati sulle slot |
|---|---|---|
| Scout | 0 | 100 |
| Shaman | 25.000 | 150 |
| Chief | 150.000 | 200 |
| Emperor | 1.500.000 | 300 |
| Legend | 10.000.000 | 400 |
| Inca | 60.000.000 | 500 |

Il percorso è graduale: si parte dal livello Scout senza requisiti e si arriva al livello Inca con 60.000.000 BP. A rendere più rapida la raccolta dei punti contribuiscono le missioni giornaliere, settimanali e a vita, che assegnano BP e altre ricompense: le missioni giornaliere si azzerano ogni giorno, mentre quelle a vita possono arrivare a 100.000 BP. La Ruota della Fortuna mette in palio premi, e i forzieri, che si aprono spendendo BP, nascondono ricompense casuali come bonus in denaro, giri gratis e altri punti. Tra i forzieri speciali ci sono Inca Chest, con un prezzo di 1.000 BP, e Paititi Treasure, con un prezzo di 1.000.000 BP. Un livello più alto può inoltre aumentare i limiti di prelievo.

## Gioco responsabile
Il gioco su Incaspin è riservato ai maggiorenni (18+) e va tenuto sotto controllo: la piattaforma mette a disposizione strumenti che il giocatore può impostare dal proprio conto. I limiti di deposito servono a controllare la spesa, e gli altri strumenti completano questa tutela:

- Limiti di deposito giornalieri, settimanali e mensili (finestre mobili di 24, 168 e 720 ore), da impostare in Il mio account > Gioco responsabile. Ridurre un limite ha effetto immediato, mentre aumentarlo o rimuoverlo richiede 24 ore.
- Altri limiti: di puntata, di perdita e di tempo di sessione.
- Autoesclusione da 3 mesi a 5 anni oppure a tempo indeterminato, che blocca l'accesso al conto. Se non si sceglie un periodo, la durata è di 6 mesi.

Un tetto settimanale o mensile più basso può prevalere sui limiti più alti di periodo più breve, perché i depositi della finestra mobile contano ai fini del limite. Chi ha bisogno di aiuto può rivolgersi all'assistenza tramite chat live o e-mail, oppure a organizzazioni esterne come Gambling Therapy, Gamblers Anonymous e l'autovalutazione di BeGambleAware. Per proteggere i minori, i dati di accesso e le carte di pagamento non vanno condivisi con loro, e si può ricorrere a software di controllo parentale o di filtro. Valgono poi alcune regole di buon senso: il gioco non è una fonte di reddito, non si inseguono le perdite, non si gioca sotto l'effetto di alcol o altre sostanze e conviene fissare un budget e fare pause regolari.

## Assistenza clienti
Il servizio clienti è attivo 24/7 tramite chat live ed e-mail, e il sito comprende anche una sezione FAQ per le domande più frequenti, da consultare prima di scrivere per le richieste più semplici. L'indirizzo e-mail dell'assistenza è support@incaspin.com. Il supporto risponde in inglese e in altre lingue, quindi per essere certi di farsi capire conviene scrivere in inglese. Gli argomenti per cui contattare il servizio clienti sono tipicamente la verifica del conto, i pagamenti e i bonus: avere a portata di mano i dati dell'operazione in questione rende la richiesta più chiara.

## Domande frequenti su Incaspin Casino
- **Serve un codice promo per il bonus di benvenuto di Incaspin?** No. Il pacchetto di benvenuto si attiva da solo con i depositi previsti, mentre un codice digitato per quei bonus fa perdere il diritto a riceverli.
- **Qual è l'età minima per giocare?** L'età minima è di 18 anni. La conferma di avere almeno 18 anni fa parte della registrazione ed è una condizione per aprire il conto.
- **Quanto tempo richiede un prelievo su Incaspin e qual è l'importo minimo?** Dopo la richiesta passano fino a 72 ore di lavorazione interna, più i tempi del metodo di pagamento. La soglia minima oscilla tra 50 e 120 €, in base al paese o al metodo, e il prelievo presuppone che i depositi siano stati giocati almeno tre volte.
- **Esiste un'app per il mobile?** Sì, come Progressive Web App da installare dal browser, senza passare da uno store di app.
- **Si possono avere più account su Incaspin?** No. Ogni persona può aprire un solo conto, e lo stesso limite riguarda famiglia, indirizzo IP e dispositivo: in caso di duplicati il conto può essere sospeso o chiuso e le vincite annullate.
- **In quali valute si può giocare?** Sono previsti sei codici di valuta: EUR, BRL, CAD e AUD tra le valute tradizionali, BTC ed ETH tra le criptovalute.
- **Come si recupera una password dimenticata?** Dalla schermata di accesso si seleziona Password dimenticata, poi si segue la procedura di reimpostazione che arriva via e-mail.

## Conclusione
Incaspin Casino riunisce per i maggiorenni un bonus di benvenuto con un massimo di 2.750 € e 275 giri gratis, una libreria di giochi molto ampia, l'accesso da mobile senza download da uno store e un'assistenza attiva 24/7. Prima di registrarsi conviene leggere le condizioni dei bonus e fissare i propri limiti: il gioco è riservato a chi ha almeno 18 anni e deve restare un intrattenimento sotto controllo. Chi decide di iscriversi a Incaspin trova nelle sezioni precedenti i dati essenziali per scegliere con consapevolezza.

---

## BLOCK BRIEF
Block: b21, H2 "Safety and Licence at Incaspin Casino" (under H1 "Incaspin Casino: bonus, registrazione, giochi e prelievi")
Page heading (output language): "Sicurezza e licenza di Incaspin Casino"
Write ONLY the body text under this heading. Do not output the heading itself.
Word Count: 165-210 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 210, but never beyond 252 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Incaspin": exactly 1 time(s)
- "Inca Spin": 0 here, but the brand name may appear when the text reads naturally: at most 3 time(s) in this block (one per 50 words)
- "Incaspin casino": exactly 1 time(s)
Entities to cover [priority 1-10]:
- Gambling Licence [10]
- Operator [8]
- Encryption (TLS) [7]
- Payment Agent [6]
- KYC and AML Checks [6]
Entity Connections to state explicitly [priority]:
- Gambling Licence → is held by → the Operator [8]
- Encryption (TLS) → protects → Player Data [7]
Summary: Safety facts: licence and operator, payment agent, encryption and attack protection, document handling and the 18+ rule.
Copywriter Notes: Lead with the Gambling Licence: Tobique Gaming Commission, licence number 0000158, jurisdiction Tobique, and the operator Legasta Technologies SRL (Costa Rica); payment-related operations are handled by OptaStream Innovations Limited (Cyprus). Then security: HTTPS/TLS 1.3, SSL certificates, web application firewall and DDoS protection; verification documents are encrypted; identity and payment checks are carried out for compliance (KYC, AML); players must be at least 18. Never call the licence European, Italian or ADM and do not suggest approval in Italy; one neutral sentence that players should check the rules of their own country is allowed. Use "Incaspin" once and "Incaspin casino" once.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_general.licences: [{"authority": "Tobique Gaming Commission", "licence_number": "0000158", "jurisdiction": "Tobique"}]
- brandinfo_general.operator: {"company_name": "Legasta Technologies SRL", "company_number": "3-102-921383", "jurisdiction": "Costa Rica", "registered_address": "Province 01 San Jose, Canton 01 San Jose, Cathedral District, Tenth Avenue, Thirty-Three and Thirty-Five Streets, Office 3335"}
- brandinfo_general.payment_agent: {"company_name": "OptaStream Innovations Limited", "registration_number": "HE 472273", "jurisdiction": "Cyprus", "registered_address": "Souliou, 18, 2018, Strovolos, Nicosia, Cyprus"}
- brandinfo_general.business_overview.security: HTTPS/TLS 1.3, SSL certificates, WAF and DDoS protection; identity checks and responsible-gaming controls
- brandinfo_privacy_policy.privacy_policy.data_security: {"encryption": "TLS 1.3 / HTTPS / SSL protection stated in the supplied site overview", "infrastructure": ["Web Application Firewall", "DDoS protection"], "verification_documents": "The site states that verification documents are encrypted and processed securely"}
- brandinfo_privacy_policy.privacy_policy.third_party_sharing: {"payment_agent": "OptaStream Innovations Limited handles payment-related operations as named in earlier accepted brand data", "regulatory_compliance": "The site describes identity and payment verification carried out for compliance"}
- brandinfo_privacy_policy.privacy_policy.minors_privacy.age_restrictions: Players must be at least 18 years old

---

## FIX MODE
This block was already written but FAILED the checks. Rewrite it so that ALL problems below are solved, keep everything that is already fine, and still respect every requirement of the block brief. Follow the numbers in the problem list literally (if a keyword appears 3 times and must appear 1, remove exactly two). After the fix re-check every other hard constraint: shortening can remove a required keyword or entity. Do not mention the fixes in the text.

CURRENT TEXT:
La licenza è il primo elemento da controllare in un casinò online, e quella di Incaspin Casino è rilasciata dalla Tobique Gaming Commission con il numero 0000158 e giurisdizione Tobique. A detenerla è l'operatore Legasta Technologies SRL, registrato in Costa Rica: la licenza indica l'autorità che autorizza l'attività, l'operatore la società che ne risponde. Le operazioni di pagamento sono gestite da OptaStream Innovations Limited, con sede a Cipro.

Sul fronte tecnico Incaspin usa HTTPS con TLS 1.3 e certificati SSL, protetti da un web application firewall e da una protezione DDoS, che servono a difendere i dati del giocatore da accessi non autorizzati e da attacchi al sito. I documenti inviati per la verifica sono cifrati ed elaborati in modo sicuro, mentre i controlli di identità e di pagamento rispondono a esigenze di conformità: sono i controlli KYC e antiriciclaggio (AML). Il gioco è riservato a chi ha almeno 18 anni. Queste informazioni permettono di capire chi gestisce il servizio e con quali protezioni tecniche vengono trattati i dati. Spetta al giocatore, infine, controllare le regole del proprio paese prima di aprire un conto.

PROBLEMS TO FIX:
- Rewrite the opening of b21 with a different construction than in b02: for example lead with the licence number ("la licenza numero 0000158 della Tobique Gaming Commission, con giurisdizione Tobique") and then say that it is held by the operator Legasta Technologies SRL (Costa Rica) without repeating the wording of b02. Delete the sentence "Queste informazioni permettono di capire chi gestisce il servizio e con quali protezioni tecniche vengono trattati i dati." Keep every fact (authority, licence number 0000158, jurisdiction Tobique, operator and country, payment agent OptaStream Innovations Limited in Cyprus, TLS 1.3, SSL, firewall, DDoS, encrypted documents, KYC and AML, 18+, check the rules of one's own country). Keep "Incaspin Casino" exactly once and "Incaspin" exactly once in the block, and keep the length at no fewer than 165 words by adding concrete detail from the facts, not filler.
