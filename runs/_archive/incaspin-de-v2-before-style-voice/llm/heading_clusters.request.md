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

c1h1 | H2 | Top Slots
c1h2 | H2 | Crash & Instant
c1h3 | H2 | Live
c1h4 | H2 | Incaspin Casino Informationen
c1h5 | H2 | Incaspin Casino Registrierung
c1h6 | H2 | Alle Bonusangebote im Überblick
c1h7 | H2 | Incaspin Casino Bonuses
c1h8 | H3 | Willkommenspaket
c1h9 | H3 | First Deposit Bonus
c1h10 | H3 | Second Deposit Bonus
c1h11 | H3 | Third Deposit Bonus
c1h12 | H3 | Highroller Bonus
c1h13 | H3 | Willkommensbonus – Erste Einzahlungen & Umsatzbedingungen
c1h14 | H3 | Cashback-Aktion – Wöchentliche Rückzahlungen auf Nettoverluste
c1h15 | H2 | Promo-Code im Incaspin Casino: So nutzen Sie exklusive Angebote
c1h16 | H2 | Spiele im Incaspin Casino
c1h17 | H3 | Slots
c1h18 | H3 | Live Games
c1h19 | H3 | Table Games
c1h20 | H2 | Zahlungen
c1h21 | H2 | Incaspin Casino App
c1h22 | H2 | FAQ
c1h23 | H3 | Kann ich im Incaspin Casino kostenlos spielen?
c1h24 | H3 | Wie zahle ich im Incaspin Casino Gewinne aus?
c1h25 | H3 | Wie aktiviere ich den Willkommensbonus im Incaspin Casino?
c1h26 | H3 | Kann ich das Incaspin Casino auf dem Handy nutzen?
c2h1 | H2 | Hoe je account aanmaken bij IncaSpin
c2h2 | H2 | Veiligheid en Licentie
c2h3 | H2 | Betalingsmethoden bij IncaSpin
c2h4 | H3 | Stortingsmethoden
c2h5 | H3 | Opnamemethoden en Verwerkingstijden
c2h6 | H2 | Ons Spellenassortiment
c2h7 | H3 | Gokkasten en Progressieve Jackpots
c2h8 | H3 | Live Casino
c2h9 | H3 | Tafelspellen en Instantspellen
c2h10 | H2 | Onze Softwareleveranciers
c2h11 | H2 | Onze Welkomstbonus en Promoties
c2h12 | H2 | Onze Trouwheidsprogramma en VIP-voordelen
c2h13 | H2 | Mobiel Spelen bij IncaSpin
c2h14 | H2 | Klantenservice bij Inca Spin
c2h15 | H2 | Waarom Kiezen voor IncaSpin?
c2h16 | H2 | Conclusie
c2h17 | H2 | Veelgestelde Vragen
c2h18 | H3 | Is IncaSpin een betrouwbaar casino?
c2h19 | H3 | Wat is de minimale storting bij Inca Spin?
c2h20 | H3 | Hoe lang duurt een uitbetaling bij IncaSpin?
c2h21 | H3 | Kan ik IncaSpin op mijn mobiel spelen?
c2h22 | H3 | Welke spellen zijn beschikbaar bij Inca Spin?
c2h23 | H3 | Hoe neem ik contact op met de klantenservice van IncaSpin?
c3h1 | H2 | Bis zu 2.500 € + 250 Freispiele
c3h2 | H2 | Beliebte Spiele
c3h3 | H2 | Top-Spiele
c3h4 | H2 | Alle Spiele
c3h5 | H2 | Das macht IncaSpin Casino besonders
c3h6 | H3 | Über 5.000 Spiele
c3h7 | H3 | Willkommenspaket bis 2.500 € + 250 FS
c3h8 | H3 | Schnelle Auszahlungen
c3h9 | H3 | VIP-Treueprogramm
c3h10 | H3 | Mobil ohne Download
c3h11 | H3 | Support rund um die Uhr
c3h12 | H2 | Letzte Gewinne
c3h13 | H2 | IncaSpin Casino – dein Abenteuer rund um den Inka-Goldschatz
c3h14 | H3 | Die Spielebibliothek von IncaSpin
c3h15 | H4 | Slots in allen Variationen
c3h16 | H4 | Live-Casino mit echten Dealern
c3h17 | H4 | Jackpots und Tischspiele
c3h18 | H3 | Willkommensbonus und Aktionen
c3h19 | H3 | Zahlungen und schnelle Auszahlungen
c3h20 | H4 | Sichere Verifizierung
c3h21 | H3 | Der VIP-Club und unser Treueprogramm
c3h22 | H3 | Mobil spielen – überall und jederzeit
c3h23 | H3 | Sicherheit und Fairness
c3h24 | H3 | Verantwortungsvolles Spielen
c3h25 | H3 | Support rund um die Uhr
c3h26 | H3 | In wenigen Schritten registriert
c3h27 | H3 | Für wen ist IncaSpin Casino gedacht?
c3h28 | H3 | Bereit für dein Abenteuer?
c3h29 | H2 | Häufige Fragen zu IncaSpin Casino
