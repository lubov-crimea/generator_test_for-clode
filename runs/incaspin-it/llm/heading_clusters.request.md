# SYSTEM

You are an SEO analyst. You receive the H2-H6 headings of several competitor pages written in the same language, each as `id | level | text`.

Group headings that cover the same meaning / user intent into clusters (e.g. "How to register", "Sign up in 3 steps" and "Registration guide" belong together; "Welcome bonus" and "Bonuses and promotions" belong together only if they clearly cover the same topic).

Rules:
- Every id must go into exactly one cluster. Do not drop ids, do not invent ids.
- Group by meaning, not by wording. Different levels (H2 vs H3) can share a cluster.
- Do not over-merge: if two headings are about different things (e.g. "Payment methods" vs "Withdrawal speed"), keep them separate.
- `canonical_title`: the best neutral heading for the cluster, written in the same language as the competitor headings, 2-8 words, no brand name unless every member has it.
- `topic`: a short English label of the shared meaning.

# USER

Competitor headings (id | level | text). Group them by meaning.

c1h1 | H2 | Fino a 2.500 € + 250 giri gratis
c1h2 | H2 | Giochi popolari
c1h3 | H2 | Giochi top
c1h4 | H2 | Tutti i giochi
c1h5 | H2 | Promozioni IncaSpin pensate per te
c1h6 | H3 | Pacchetto di benvenuto fino a 2.500 € + 250 giri gratis
c1h7 | H3 | 250 giri gratis sulle slot di punta
c1h8 | H3 | Bonus di ricarica per i giocatori abituali
c1h9 | H3 | Cashback settimanale
c1h10 | H3 | Club VIP a livelli
c1h11 | H3 | Tornei e sfide live
c1h12 | H2 | Vincite recenti
c1h13 | H2 | IncaSpin Casino: la guida completa al tesoro d'oro inca del gioco online
c1h14 | H3 | Chi siamo: l'esperienza IncaSpin
c1h15 | H3 | La libreria di giochi: oltre 5.000 titoli da esplorare
c1h16 | H4 | Slot per ogni stile di gioco
c1h17 | H4 | Casinò live: il brivido del tavolo reale
c1h18 | H4 | Jackpot e giochi da tavolo
c1h19 | H3 | Il bonus di benvenuto: fino a 2.500 € + 250 giri gratis
c1h20 | H4 | Promozioni continue per i giocatori abituali
c1h21 | H4 | La nostra filosofia di gioco
c1h22 | H3 | Pagamenti: deposita e preleva come preferisci
c1h23 | H4 | Criptovalute: velocità e libertà
c1h24 | H4 | Prelievi rapidi
c1h25 | H3 | Il club VIP IncaSpin: ricompense che crescono con te
c1h26 | H3 | Gioco da mobile: il casinò sempre in tasca
c1h27 | H3 | Sicurezza e correttezza del gioco
c1h28 | H3 | Gioco responsabile: divertimento sotto controllo
c1h29 | H3 | Assistenza clienti: siamo sempre con te
c1h30 | H4 | Verifica del conto e KYC
c1h31 | H3 | Come registrarsi su IncaSpin in pochi passi
c1h32 | H3 | Per chi è pensato IncaSpin Casino
c1h33 | H2 | Domande frequenti su IncaSpin Casino
c2h1 | H2 | Informazioni su IncaSpin Casino
c2h2 | H3 | Operatore
c2h3 | H3 | Assistenza
c2h4 | H2 | I Giochi di IncaSpin Casino
c2h5 | H3 | - Slot su IncaSpin
c2h6 | H3 | - Live Casino su IncaSpin
c2h7 | H3 | - Giochi da Tavolo su IncaSpin
c2h8 | H3 | - Video Poker su IncaSpin
c2h9 | H3 | - Jackpot su IncaSpin
c2h10 | H2 | Sicurezza su IncaSpin Casino
c2h11 | H3 | Licenza e Conformità Normativa
c2h12 | H2 | Codici Promo di IncaSpin Casino
c2h13 | H3 | Come Vengono Attivate le Promozioni
c2h14 | H2 | Programma VIP di IncaSpin Casino
c2h15 | H3 | Vantaggi per Livello VIP
c2h16 | H2 | Il Bonus di IncaSpin Casino
c2h17 | H3 | Termini e Condizioni del Bonus
c2h18 | H3 | Promozioni Continuative
c2h19 | H2 | IncaSpin Casino su Mobile
c2h20 | H3 | Come Accedere da Mobile
c2h21 | H2 | Come Registrarsi su IncaSpin Casino
c2h22 | H3 | Passo 1 - Visita il Sito e Clicca su Registrati
c2h23 | H3 | Passo 2 - Inserisci i Tuoi Dati Personali
c2h24 | H3 | Passo 3 - Scegli Username e Password
c2h25 | H3 | Passo 4 - Accetta i Termini e Conferma via Email
c2h26 | H3 | Passo 5 - Primo Deposito e Bonus di Benvenuto
c2h27 | H2 | Depositi e Pagamenti su IncaSpin Casino
c2h28 | H3 | Depositi su IncaSpin
c2h29 | H3 | Prelievi su IncaSpin
c2h30 | H2 | Gioco Responsabile su IncaSpin Casino
c2h31 | H2 | IncaSpin: domande frequenti
