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
Brand: Cazeus (this name and its spellings are tracked keywords: the block brief gives the exact count; where it says 0 the brand name is free to use)
Country / GEO: NO
Language: Norwegian (no). Write ONLY in this language.
Page intent: Brand-related (navigational and informational) review page about the Cazeus online casino for players from Norway: what the casino is, the welcome package and other promotions, games and providers, live casino, sports betting, registration and login, verification, deposits and withdrawals, VIP Club, mobile access, licence and data protection, support, responsible gambling, strengths and weaknesses. All brand-specific facts come from the AffBulk knowledge base Cazeus-upd.
All tracked keywords: Cazeus, Cazues casino
Information about the brand to use:
- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" (verbatim from the AffBulk knowledge base "Cazeus-upd"). Use only those facts for brand-specific claims.

---

## PAGE STRUCTURE FOR CONTEXT
b01 H1 Cazeus casino i Norge: anmeldelse av bonuser, spill og betaling (100-125 words): Short introduction: what the online casino offers to players from Norway (game categories, sportsbook, welcome package, 18+ age limit) and what the page covers.
b02   H2 Fakta om casinoet på et blikk (80-100 words): A compact fact sheet of the casino: operator, licence record, launch year, languages, currencies, payment methods, welcome bonus, cashback, minimum deposit and support contact.
b03   H2 Om Cazeus casino (158-202 words): Overview of the platform: launch year, the operator company and the currencies, including the Norwegian krone.
b04   H2 Velkomstpakke og bonuser hos Cazeus (220-280 words): The casino welcome package: amount and free spins, the qualifying deposit, the wagering requirements, validity, bet and cashout limits, game contribution and the fact that no promo code is needed.
b05     H3 Reload-bonuser og cashback (150-190 words): Recurring promotions after the welcome package: Weekly Reload, Weekend Reload Bonus, Daily Cashback and Live Cashback with rewards, minimum deposits and availability, plus their wagering rules.
b06     H3 Utfordringer, samlinger og belønningsbutikk (132-168 words): Game-like reward features: challenges, collections, the coins shop and the Wheel of Fortune, with the rules for earning coins and spins.
b07   H2 Spillutvalg (141-179 words): How the game lobby is organised: slots, table games, live casino, live game shows, jackpots, instant games, Megaways and bonus buy games.
b08     H3 Spillleverandører og populære spilleautomater (106-134 words): The studios behind the games and three example slots with provider, RTP, volatility and maximum multiplier.
b09     H3 Live casino (110-140 words): The live casino: live casino games and live game shows, the weekly Live Cashback and the low contribution of live games to bonus wagering.
b10   H2 Sportsbetting (188-238 words): The sportsbook: sports covered, minimum bet, live betting features and the sports welcome bonus with the wagering requirement valid for Norway.
b11   H2 Registrering og innlogging hos Cazeus (142-182 words): How to create an account and log in: the six registration steps, the personal data requested, the choice of the welcome package and password recovery.
b12     H3 Kontoverifisering (110-140 words): Verification: which documents may be requested, the 30-day submission deadline, the usual 10-day processing time and the effect of incomplete verification on payments.
b13   H2 Innskudd og uttak (78-98 words): Short introduction to payments: general deposit limits, dependence of the methods on country and currency, and the rule that the payment method must belong to the account holder.
b14     H3 Innskuddsmetoder (114-146 words): Deposit methods with minimum, maximum and speed, and how a deposit is made in the cashier.
b15     H3 Uttak av gevinster (165-210 words): How withdrawals work: minimum and maximum amount, processing time, the preference for the deposit method, the deposit rollover and the VIP limits.
b16   H2 VIP Club (142-182 words): The VIP Club with five levels: withdrawal limits and benefits by level, evaluation period, criteria and downgrade rule.
b17   H2 Mobil casino og app (99-126 words): Mobile play: there is no dedicated app, the casino is used through the mobile-optimised website in a browser, with the main functions available.
b18   H2 Lisens, sikkerhet og personvern (165-210 words): The licence record, the security and data-protection measures and the contact of the data protection officer.
b19   H2 Kundesupport (88-112 words): Support channels: live chat and e-mail, available around the clock.
b20   H2 Ansvarlig spilling (154-196 words): Responsible gambling at the casino: principles, temporary break and self-exclusion by e-mail, the absence of deposit, loss and session limits, and external support organisations.
b21   H2 Spillererfaring: fordeler og ulemper (110-140 words): A balanced summary of the strengths and weaknesses visible in the facts, as a pros and cons table, without quoting user reviews.
b22   H2 Totalvurdering av Cazeus casino (99-126 words): Closing assessment: who the casino suits, based on the minimum deposit and withdrawal, the sportsbook with live betting, and the points to check before playing.

---

## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)

# Cazeus casino i Norge: anmeldelse av bonuser, spill og betaling
Cazeus er et nettcasino for spillere fra Norge. Spilleautomater, bordspill og live casino står i spissen, og lobbyen har også live spillshow, jackpotspill og instant-spill. I tillegg finnes en sportsbook med live betting, slik at casino og sport kan brukes fra samme konto. Nye spillere møter en velkomstpakke på opptil 1 750 euro og 150 gratisspinn, og aldersgrensen på siden er 18 år.

Anmeldelsen går gjennom bonusene og vilkårene deres, spillutvalget, registreringen, betalingsmetodene, VIP Club, mobilbruken og sikkerheten. Målet er at leseren får et konkret bilde av tilbudet før det første innskuddet. Lisens og personvern omtales også, slik at vilkårene kan vurderes før kontoen opprettes.

## Fakta om casinoet på et blikk
| Parameter | Opplysninger |
|---|---|
| Operatørselskap | Liernin Enterprises Ltd |
| Lisensoppføring | PAGCOR, lisensnummer IGL-24-0021, historisk oppføring, gjeldende gyldighet er ikke bekreftet |
| Lanseringsår | Lansert i 2020 |
| Språk | Ikke spesifisert for nettsiden eller kundestøtten |
| Valutaer | Seks valutaer, blant dem NOK: EUR, USD, CAD, NOK, HUF og PLN |
| Betalingsmetoder | Kort, e-lommebøker og kryptovalutaer: Interac, Visa, Mastercard, Paysafecard, Neteller, Cash2Code, MiFinity, Bitcoin og flere |
| Velkomstbonus | Opptil 1 750 euro og 150 gratisspinn |
| Cashback | Daily Cashback på 3–15 % med tak på 400 euro for VIP-nivå 2 til 5 |
| Minimumsinnskudd | Fra 10 euro |
| Kundestøtte | E-post support@cazeus.com og live chat, tilgjengelig døgnet rundt (24/7) |

## Om Cazeus casino
Cazeus er et nettcasino som ble lansert i 2020 og drives av selskapet Liernin Enterprises Ltd. Operatøren står bak hele tilbudet på nettstedet, både casinoet og sportsboken, og selskapsnavnet sammen med lanseringsåret hører til de første opplysningene en spiller bør kjenne til før registrering. Navnet skrives av og til som Cazues casino i søk, og begge skrivemåtene gjelder det samme nettcasinoet. Selskapsnavnet viser hvem som er ansvarlig for nettstedet, men sier ingenting om lisensstatus eller om reglene selskapet følger, og dette får et eget avsnitt lenger ned på siden.

Cazeus godtar seks valutaer: EUR, USD, CAD, NOK, HUF og PLN. Det gjelder euro, amerikanske og kanadiske dollar, norske kroner, ungarske forint og polske zloty. For spillere fra Norge er det praktisk at NOK står på listen, fordi innskudd og spill da kan holdes i norske kroner. Valutaen bør likevel velges med tanke på hvilke kontoer og betalingsmetoder man selv bruker, og de enkelte metodene er omtalt i avsnittene om innskudd og uttak.

## Velkomstpakke og bonuser hos Cazeus
Velkomstpakken hos Cazeus gir opptil 1 750 euro i bonus og 150 gratisspinn. Pakken krever et kvalifiserende innskudd på minst 20 euro. Det er et høyere minimum enn det generelle minimumsinnskuddet på siden, som omtales i avsnittet om innskudd og uttak.

Bonusen må omsettes før den kan tas ut. Omsetningskravet, altså hvor mange ganger et beløp må satses på spill, er 35 ganger summen av innskudd og bonus. Kravet gjelder dermed både det innsatte beløpet og bonusen, ikke bonusen alene. Gratisspinn er spinn på en spilleautomat der casinoet betaler innsatsen, og gevinster fra dem har et eget krav på 40 ganger gevinsten, adskilt fra kravet til innskuddsbonusen. Hvert omsetningskrav må være oppfylt innen 10 dager fra aktiveringen, og så lenge bonusen er aktiv er høyeste innsats 5 euro per spill. Det høyeste beløpet som kan tas ut fra bonusen, tilsvarer 10 ganger det kreditterte bonusbeløpet.

Spilltypene bidrar ulikt til omsetningen. Spilleautomater teller 100 % og bidrar dermed fullt ut til kravet, mens live spill, videopoker og plinko teller 10 % og bordspill 0 %. For spilleren betyr det at pakken i praksis omsettes på spilleautomater, og at en kveld ved et bordspill ikke flytter omsetningen. Hos Cazeus kreves ingen bonuskode for å få velkomstpakken. Det lønner seg likevel å lese de fullstendige vilkårene før pakken aktiveres, siden omsetningskrav, frister og maksbeløp avgjør hvor mye av bonusen som kan bli til uttakbare penger.

### Reload-bonuser og cashback
Etter velkomstpakken finnes fire gjentakende tilbud: to for innskudd og to for cashback.

| Tilbud | Belønning | Minimumsinnskudd | Tilgjengelighet |
|---|---|---|---|
| Weekly Reload | 60 gratisspinn | 20 euro | Mandag til torsdag |
| Weekend Reload Bonus | 50 % opptil 800 euro og 80 gratisspinn | 20 euro, 50 euro for gratisspinnene | Fredag til søndag |
| Daily Cashback | 3–15 % opptil 400 euro | Ikke aktuelt | Daglig, fra VIP-nivå 2 |
| Live Cashback | 25 % opptil 200 euro | Ikke aktuelt | Ukentlig, alle VIP-nivåer |

Weekend Reload Bonus har et omsetningskrav på 35 ganger summen av innskudd og bonus, mens gevinstene fra gratisspinnene må omsettes 40 ganger. Bonusen må omsettes innen 10 dager, og gratisspinnene må brukes innen 7 dager. Gratisspinnene fra Weekly Reload har det samme kravet på 40 ganger og den samme fristen på 7 dager. Daily Cashback gjelder fra VIP-nivå 2 og regnes ut daglig, mens Live Cashback gir tilbake en andel av nettotapet i live casino hver uke. Cashback må aktiveres under My Bonuses og omsettes én gang. Mens en bonus omsettes, er høyeste innsats 5 euro, og bare én casinobonus kan være aktiv om gangen.

### Utfordringer, samlinger og belønningsbutikk
Belønningsbutikken heter Cazeus Shop, og valutaen i den er Cazeus Coins. Mynter tjenes på tre måter: 1 mynt for hver 10 euro som satses på kvalifiserte casinospill, mynter tilsvarende 5 % av hvert kvalifiserende innskudd og mynter for turneringsdeltakelse og plasseringer. I butikken byttes myntene mot bonuspenger, gratisspinn og gratisbets til sportsboken.

Wheel of Fortune er en egen belønningsmekanisme. Spilleren tjener 1 spinn for hver 100 euro som satses på kvalifiserte casinospill, og satsing med en aktiv bonus teller ikke med. Høyst 3 spinn kan tjenes per dag, og opptil 10 ubrukte spinn kan ligge klare om gangen, så spinnene tjenes jevnt og kan ikke samles opp i store mengder. Ved siden av dette finnes Challenges, der spilleren løser oppgaver og går gjennom mål for å tjene mynter og belønninger, og Collections, som består av 7 samlinger med 10 samlekort hver.

### Spillleverandører og populære spilleautomater
Spillene kommer fra flere studioer. Pragmatic Play, Play’n GO og BGaming hører til de mest kjente leverandørene, og lobbyen har i tillegg spill fra Amusnet, Spinomenal, Gamzix, Booongo, EGT, IGTech og Playson. Tre eksempler viser hvordan nøkkeltallene varierer fra spill til spill.

| Spill | Leverandør | RTP | Volatilitet | Maks. multiplikator |
|---|---|---|---|---|
| Coin Spark | CROCO Games | 92 % / 94 % / 95 % / 96 % | Middels | 2 000x |
| Piggy Party XL | CROCO Games | 96 % | Høy | 5 000x |
| 3 Hot Chilli Peppers | Iron Dog Studio (1X2 Network) | 95 % / 93 % / 91 % | Høy | 10 000x |

RTP viser hvor stor andel av innsatsene en spilleautomat teoretisk gir tilbake over lang tid, mens volatiliteten sier hvor store og hvor hyppige gevinstene er. Når et spill er oppgitt med flere RTP-verdier, finnes det i flere versjoner, så verdien er verdt å sjekke i spillinformasjonen.

### Live casino
Live casino hos Cazeus består av to deler: live casinospill og live spillshow. I begge styres spillet av en ekte dealer eller programleder via video, og spilleren deltar i sanntid over nettet. Spillshowene er en egen kategori ved siden av de vanlige live casinospillene. Live-delen passer for spillere som vil ha en annen opplevelse enn automatene, med fast spillrytme og en vert som leder runden.

Live Cashback gir 25 % tilbake, opptil 200 euro, og regnes ut fra innsatsene i live casino med ekte penger minus gevinstene med ekte penger. Tilbudet er et alternativ til bonusomsetning, for live spill teller bare 10 % mot omsetningskravene. Den som foretrekker live casino, har derfor mer å hente på cashbacken enn på å omsette en bonus.

## Sportsbetting
Sportsboken hos Cazeus dekker fotball, basketball, motorsport, tennis, baseball, bordtennis, ishockey og amerikansk fotball, i tillegg til e-sport, virtuell sport og andre internasjonale idretter. Minste innsats er 1 euro, så terskelen for å prøve et marked er lav, og spilleren trenger ikke satse store beløp for å se hvordan oddsene og betalingene fungerer.

Live betting er en egen del av tilbudet. Her kan spilleren satse underveis i kampen (in-play betting), bruke Cash Out for å avslutte et spill før hendelsen er over og sette sammen egne kombinasjoner med Bet Builder. Live-markedene suppleres av forhøyede odds på utvalgte arrangementer og tidlig utbetaling på kvalifiserende hendelser. Sportsboken tilbyr dermed live betting med Cash Out, som gir spilleren flere muligheter til å styre et spill etter at innsatsen er plassert.

Sportsbonusen er et eget tilbud ved siden av casinopakken. Nye kunder kan få 100 % opptil 100 euro på innskuddet. For spillere fra Norge er omsetningskravet (innskudd + bonus) x5, det vil si fem ganger summen av innskuddet og bonusen, og beløpet må satses før bonusen kan bli til uttakbare penger. Kravet er lavere enn omsetningskravet i casinoet, men det gjelder bare sportsbonusen og ikke velkomstpakken.

## Registrering og innlogging hos Cazeus
Kontoen opprettes via et skjema på nettstedet, og registreringen følger seks trinn:

1. Åpne nettstedet til Cazeus og velg Registrer.
2. Fyll ut registreringsskjemaet med riktige personopplysninger.
3. Velg kontotype og ønsket velkomstbonus, slik at riktig tilbud følger kontoen fra start.
4. Send inn skjemaet.
5. Gå til spillerprofilen og fullfør eventuelle trinn for kontooppsett.
6. Foreta et kvalifiserende innskudd dersom tilbudet som er valgt, forutsetter det.

Opplysningene bør være nøyaktige, fordi de sammenlignes med dokumentene i den senere verifiseringen, som omtales nedenfor. Skjemaet ber om fullt navn, fødselsdato, e-postadresse, telefonnummer, land, kjønn, brukernavn og postnummer, og om identifikasjonsnummer der det kreves. Velkomstpakken velges under registreringen eller før det kvalifiserende innskuddet. Innlogging skjer med valget Logg inn: spilleren åpner Cazeus, velger Logg inn og skriver inn de registrerte påloggingsopplysningene. Er passordet glemt, velger spilleren alternativet for glemt passord i innloggingsskjemaet og følger instruksjonene for tilbakestilling, slik at kontoen blir tilgjengelig igjen.

### Kontoverifisering
Verifisering, også kalt KYC (know your customer), er en kontroll av alder, identitet og betalingsmetoder som er vanlig hos regulerte casinoer. Casinoet kan be om pass, nasjonalt ID-kort eller førerkort, bevis på bostedsadresse og dokumentasjon på at betalingsmetoden tilhører spilleren. Kontoutskrifter, transaksjonshistorikk og, når det forlanges, bevis på hvor pengene kommer fra, kan også bli etterspurt.

Dokumentene må leveres innen 30 dager etter at forespørselen er sendt, og behandlingen er vanligvis ferdig innen 10 dager etter at all informasjon er mottatt. Mens verifiseringen ikke er fullført, kan innskudd og uttak bli blokkert. Det lønner seg derfor å ha dokumentene klare tidlig, slik at et senere uttak ikke blir forsinket av manglende bilder eller utskrifter.

## Innskudd og uttak
Kassen håndterer både innskudd og uttak. Et innskudd kan være fra 10 euro og opptil 10 000 euro, men hver betalingsmetode har egne grenser, som vises i tabellen nedenfor, og velkomstpakken krever et høyere minimum, slik bonusavsnittet viser. Hvilke metoder som er tilgjengelige, avhenger av land, kontovaluta og betalingsleverandør, og metoden må tilhøre kontoinnehaveren. Kravet betyr i praksis at kort og e-lommebøker må stå i spillerens eget navn, ikke i navnet til en venn eller et familiemedlem. De neste delene gjennomgår innskuddsmetodene og uttakene hver for seg.

### Innskuddsmetoder
Et innskudd gjøres i kassen: spilleren logger inn, åpner Kasse eller Betalinger, velger Innskudd og en metode, skriver inn beløp og betalingsopplysninger og bekrefter transaksjonen hos betalingsleverandøren. For kort og e-lommebøker tar casinoet ikke innskuddsgebyr, men gebyrer fra kortutstederen, leverandøren eller blokkjeden kan komme i tillegg.

| Metode | Minimum | Maksimum | Hastighet |
|---|---|---|---|
| Visa | 20 euro | 4 000 euro | Umiddelbart |
| Mastercard | 20 euro | 4 000 euro | Umiddelbart |
| Paysafecard | 15 euro | 1 400 euro | Umiddelbart |
| Neteller | 20 euro | 7 800 euro | Umiddelbart |
| MiFinity | 15 euro | 3 750 euro | Umiddelbart |
| Bitcoin | 45 euro | 10 000 euro | Etter nettverksbekreftelse |
| Ethereum | 20 euro | 8 000 euro | Etter nettverksbekreftelse |
| Tether USDT (ERC20) | 20 euro | 8 000 euro | Etter nettverksbekreftelse |

Beløpsgrensene varierer altså mellom metodene. Blant kryptovalutaene kan Dogecoin, Litecoin, Tron, USD Coin, BNB, Solana og Cardano også brukes, og Cash2Code finnes ved siden av Paysafecard som forhåndsbetalt kupong, avhengig av land.

### Uttak av gevinster
Et uttak starter med en forespørsel i kassen. Forespørselen går til casinoets økonomiavdeling, som behandler den innen 3 virkedager når kravene og kontrollene er oppfylt. Utbetalingen hos betalingsleverandøren eller i blokkjeden kan ta ekstra tid. Cazeus godtar uttak fra 10 euro, og det høyeste beløpet er 10 000 euro per transaksjon, med forbehold om grenser for metoden og kontoen.

Den høye grensen er bare et tak per transaksjon. I tillegg gjelder daglige og månedlige uttaksgrenser for VIP-nivåene, og de er lavere på de laveste nivåene, som beskrevet i avsnittet om VIP Club. Ingen bør derfor regne med å kunne ta ut 10 000 euro på én gang.

Der det er mulig, utbetales uttaket med samme metode som innskuddet. Før uttak gjelder dessuten et innskuddsomløp på 1 gang, det vil si at innskutte penger må være satset minst én gang. Casinoet kan også be om verifisering før utbetalingen, som beskrevet i avsnittet om kontoverifisering, og et uttak kan bli forsinket hvis dokumentene mangler. Det kan derfor være lurt å sende inn dokumentene før det første uttaket.

## VIP Club
VIP Club har fem nivåer, og nivået vurderes over 90 kalenderdager ut fra innskuddsaktivitet, uttaksaktivitet og mottatte bonuser. Nivået bestemmer hvor mye som kan tas ut per dag og per måned, og høyere nivåer gir også høyere Daily Cashback.

| Nivå | Daglig uttaksgrense | Månedlig uttaksgrense | Viktigste fordeler |
|---|---|---|---|
| Nivå 1 | 500 euro | 7 000 euro | Kampanjer, livechat 24/7, Live Cashback |
| Nivå 2 | 500 euro | 10 000 euro | Daily Cashback på 3 % opptil 100 euro og Live Cashback |
| Nivå 3 | 800 euro | 12 000 euro | Høyere uttaksgrenser, Daily Cashback 5 % opptil 200 euro |
| Nivå 4 | 1 000 euro | 15 000 euro | Personlig VIP-manager, personlige tilbud, Daily Cashback 10 % opptil 300 euro |
| Nivå 5 | 1 500 euro | 20 000 euro | Høyeste uttaksgrenser, personlig VIP-manager, personlige tilbud, Daily Cashback 15 % opptil 400 euro |

En spiller som ikke har satset aktivt på en måned, nedgraderes automatisk til nivå 1. Uttaksgrensene i tabellen gjelder i tillegg til grensen per transaksjon, så nivået har direkte betydning for hvor raskt større gevinster kan tas ut.

## Mobil casino og app
Det finnes ingen egen app for mobil. I stedet er nettstedet tilpasset mobile nettlesere, slik at spilleren åpner cazeus.com i en støttet nettleser og kan spille uten å installere noe. Mobilnettstedet erstatter dermed en egen app, og det gir tilgang til hovedfunksjonene i casinoet.

Casinospill og live casino finnes på mobilen, og det samme gjelder sportsboken med live betting, registrering og innlogging, kampanjer og VIP-funksjoner. Innskudd og uttak kan gjøres med de støttede betalingsmetodene, og kundestøtten nås via live chat og e-post. Siden alt kjøres i nettleseren, må telefonen eller nettbrettet ha en stabil internettforbindelse mens spilleren er innlogget.

## Lisens, sikkerhet og personvern
Casinoet er oppført med en lisens fra PAGCOR, den filippinske spillreguleringsmyndigheten. Lisensnummeret er IGL-24-0021, og operatøren er Liernin Enterprises Ltd. En lisens betyr at operatøren skal følge reglene til myndigheten som har utstedt den, men hvor strenge reglene er, varierer mellom land. Oppføringen er historisk, og gyldigheten i dag er ikke bekreftet, så spillere bør sjekke statusen hos reguleringsmyndigheten før de setter inn penger. Lisensen er ikke en norsk lisens, og den gir i seg selv ikke grunnlag for å si at tilbudet er godkjent eller lovlig i Norge.

Sikkerheten bygger på administrative, tekniske og fysiske tiltak som skal beskytte opplysningene mot uautorisert tilgang, tap, tyveri og misbruk. Tiltakene vurderes og forbedres fortløpende. Ingen overføring eller lagring på internett kan likevel garanteres helt sikker, og spilleren bør derfor bruke et eget passord og logge ut etter spilløkter på delte enheter.

Spørsmål og forespørsler om personopplysninger sendes til personvernombudet på dpo@cazeus.com. Personvernombudet behandler henvendelser om hvordan casinoet bruker og beskytter dataene som samles inn om spillerne.

## Kundesupport
Kundesupporten kan nås på to måter: via live chat og via e-post på support@cazeus.com. Begge kanalene er åpne 24/7, så en spiller kan få hjelp også på kvelden og i helgene. Support er nyttig når kontoen ikke lar seg åpne, når verifiseringen trenger oppfølging eller når en spiller vil ha en pause fra spilling. Live chat egner seg best til raske spørsmål underveis, mens e-post passer for saker som krever dokumenter eller en skriftlig forklaring. Det lønner seg å oppgi brukernavnet og en kort beskrivelse av problemet i den første meldingen, slik at saken kan behandles uten unødvendig frem og tilbake.

## Ansvarlig spilling
Spilling bør ses på som underholdning og ikke som en inntektskilde, og man bør bare spille med penger man har råd til å tape. Det hjelper å holde oversikt over tiden og pengene som brukes, og å la være å jage tap.

Casinoet tilbyr en midlertidig pause og selvutestengelse. Begge ordnes ved å kontakte kundestøtten på support@cazeus.com, og ved selvutestengelse blir kontoen stengt så snart det er praktisk mulig. Spilleren har selv ansvaret for ikke å opprette nye kontoer. Innskuddsgrenser, tapsgrenser og tidsgrenser for spilløkter tilbys ikke, så kontrollen ligger i større grad hos spilleren selv, og det er særlig viktig å sette egne rammer for tid og penger før spillingen starter.

Hjelp utenfor casinoet finnes hos GamCare, Gamblers Anonymous og Gambling Therapy, som gir råd, støtte og samtaler til personer som er rammet av spillrelaterte problemer. Den som merker at spillingen går utover økonomi, arbeid eller relasjoner, bør ta kontakt tidlig. Spilling er forbeholdt voksne over 18 år.

## Spillererfaring: fordeler og ulemper
Spillererfaringen preges av både sterke sider og begrensninger, og tabellen oppsummerer de viktigste punktene som følger av opplysningene på siden.

| Fordeler | Ulemper |
|---|---|
| Velkomstpakke på opptil 1 750 euro og 150 gratisspinn | Ingen egen app, bare mobilnettsted |
| VIP Club med 5 nivåer | Ingen innskudds-, tap- eller tidsgrenser |
| Kundestøtte døgnet rundt | Omsetningskrav på bonusene |
| Casino og sportsbook i én konto | Lisensoppføring med ubekreftet gyldighet |

Velkomstpakken er en styrke for den som vil bruke bonuser, og VIP Club gir lojale spillere noe å strekke seg etter. Fraværet av innskuddsgrenser er derimot en svakhet i verktøyene for ansvarlig spilling, og den ubekreftede lisensstatusen og mobilnettstedet uten app er punkter som bør vurderes før et innskudd.

## Totalvurdering av Cazeus casino
Cazeus passer for spillere fra Norge som vil ha casino og sportsbook med live betting på samme konto, og terskelen er lav: både minste innskudd og minste uttak er 10 euro. Kombinasjonen av spilleautomater, live casino og sport samler flere interesser i én lobby og én saldo. Velkomstpakken gir et bredt utgangspunkt, men omsetningskravene gjør at vilkårene bør leses nøye før bonusen aktiveres.

Før det første innskuddet bør spilleren også ta med at det ikke finnes noen egen app, at lisensoppføringen har ubekreftet gyldighet og at casinoet ikke har en norsk lisens. Spilling er forbeholdt voksne og bør holdes innenfor et budsjett som man har råd til å tape.

---

## BLOCK BRIEF
Block: b07, H2 "Casino Games" (under H1 "Cazeus casino i Norge: anmeldelse av bonuser, spill og betaling")
Page heading (output language): "Spillutvalg"
Write ONLY the body text under this heading. Do not output the heading itself.
Sub-sections written separately (do NOT cover their topics here): b08 H3 "Spillleverandører og populære spilleautomater"; b09 H3 "Live casino"
Word Count: 141-179 words (body only, heading excluded). If the facts, the entities and a natural style need more room, go over 179, but never beyond 214 words.
Format: paragraph. Visual Elements: None specified
Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; a grammatical form of the keyword (case ending, plural) counts as the keyword):
- "Cazeus": exactly 1 time(s)
- "Cazues casino": 0 (do not use)
Entities to cover [priority 1-10]:
- Game Categories [10]
- Slots [8]
- Table Games [6]
- Jackpots [5]
Entity Connections to state explicitly [priority]:
- Game Categories → include → Slots, Table Games, Jackpots and Instant Games [6]
Summary: How the game lobby is organised: slots, table games, live casino, live game shows, jackpots, instant games, Megaways and bonus buy games.
Copywriter Notes: Describe how the lobby is organised (structure first): Slots, Table Games, Live Casino Games, Live Game Shows, Jackpots, Instant Games, Megaways and Bonus Buy Games, with a short explanation of Megaways and Bonus Buy in a clause each (general explanation, not brand claims). Mention that the sportsbook has its own section and that live casino and providers are described in the sub-sections below. Do not state any game count or provider here. Use 'Cazeus' exactly once. Link to the neighbouring topic with one fact-based sentence (for example that slots contribute 100 % to bonus wagering, as given in the bonus section) only if it fits naturally.
Brand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):
- brandinfo_games.game_types: ["Slots", "Table Games", "Live Casino Games", "Live Game Shows", "Jackpots", "Instant Games", "Megaways", "Bonus Buy Games", "Sportsbook"]

---

## FIX MODE
This block was already written but FAILED the checks. Rewrite it so that ALL problems below are solved, keep everything that is already fine, and still respect every requirement of the block brief. Follow the numbers in the problem list literally (if a keyword appears 3 times and must appear 1, remove exactly two). After the fix re-check every other hard constraint: shortening can remove a required keyword or entity. Do not mention the fixes in the text.

CURRENT TEXT:
Spillobbyen hos Cazeus er delt inn i kategorier, slik at spilleren kan gå rett til den typen spill som passer. Spilleautomatene er den mest sentrale kategorien. Blant dem finnes Megaways-spill, der antall gevinstmuligheter endres fra runde til runde, og spill med bonuskjøp, der spilleren mot en høyere innsats kan kjøpe seg direkte inn i bonusrunden. Bordspill, som kort- og rulettspill, har sin egen kategori, og det samme gjelder jackpotspill, der en stor gevinstpott er hovedpoenget, og instant-spill, der resultatet kommer umiddelbart etter innsatsen. Utvalget omfatter altså seks hovedkategorier i tillegg til Megaways og bonuskjøp.

Live casino og live spillshow ligger i en egen del, som omtales lenger ned, og sportsboken har et eget avsnitt. Valget av kategori har også en praktisk side, for hvor mye hver kategori bidrar til omsetningen av velkomstpakken, framgår av bonusavsnittet. Spilleren som vil bruke en bonus, bør derfor se på det før valget av spill.

PROBLEMS TO FIX:
- Replace the sentence 'Spilleautomatene er den mest sentrale kategorien.' with a neutral statement, for example that slots are the first game type of the lobby list, and keep the rest of the paragraph (Megaways, bonus buy, table games, jackpots, instant games). Keep 'Cazeus' exactly once and the word count in the 141-179 range.
