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

c0h1 | H2 | Jak sprawdzić licencję i wiarygodność serwisu Incaspin Casino
c0h2 | H3 | Przejrzyste warunki licencji w serwisie Incaspin Casino dla graczy
c0h3 | H3 | Sygnały zaufania i ostrzeżenia przy ocenie marki Incaspin Legit
c0h4 | H2 | Oferta gier i dostawców w kasynie Incaspin Kasyno
c0h5 | H3 | Sloty, stoły i live dealer w Kasyno Incaspin
c0h6 | H3 | Dostawcy oprogramowania widoczni w sekcjach Kasyno Incaspin dla graczy
c0h7 | H2 | Bonusy, promocje i warunki obrotu w Incaspin Pl
c0h8 | H3 | Powitalna oferta opisana w każdej rzetelnej Incaspin Recenzja
c0h9 | H3 | Reguły obrotu bonusu oraz limity w serwisie Incaspin Pl
c0h10 | H2 | Płatności, wypłaty i waluty w nowoczesnym kasynie Incaspin
c0h11 | H3 | Metody wpłat i wypłat opisane w Incaspin Review
c0h12 | H3 | Limity transakcji oraz waluta eur w Incaspin Opinie
c0h13 | H2 | Mobilna obsługa, bezpieczeństwo i wsparcie w Kasyno Incaspin Opinie
c0h14 | H3 | Aplikacja, przeglądarka i szybkość ładowania w Kasyno Incaspin Opinie
c0h15 | H3 | Kanały kontaktu i reakcja działu wsparcia w Incaspin Casino Opinie
c0h16 | H2 | Końcowa ocena, doświadczenia graczy i rekomendacja Incaspin Casino Review
c0h17 | H3 | Podsumowanie opinii użytkowników o marce Incaspin Casino Review
c0h18 | H3 | Kiedy warto wybrać serwis z perspektywy Incaspin dla gracza
c0h19 | H2 | Najczęściej zadawane pytania
c1h1 | H2 | Legalność, licencja i polski dostęp w serwisie Incaspin
c1h2 | H3 | Jak potwierdzić licencję i status legalny Incaspin Legit
c1h3 | H3 | Najważniejsze informacje o polskiej wersji Incaspin Pl dla graczy
c1h4 | H2 | Oferta gier, dostawcy i sekcje kasynowe w Incaspin Casino
c1h5 | H3 | Jakie automaty oferuje nowoczesne kasyno Incaspin Casino dla graczy
c1h6 | H3 | Którzy dostawcy gier budują ofertę Incaspin Kasyno najmocniej
c1h7 | H2 | Bonusy, promocje i warunki gry opisane w Incaspin Review
c1h8 | H3 | Jak działają promocje opisane w Incaspin Review obecnie
c1h9 | H3 | Na co zwracać uwagę przy Incaspin Casino Review
c1h10 | H2 | Wpłaty, wypłaty i waluty w praktyce Kasyno Incaspin
c1h11 | H3 | Jak wyglądają wpłaty i wypłaty w Kasyno Incaspin
c1h12 | H3 | Jakie limity i waluty opisują Kasyno Incaspin Opinie
c1h13 | H2 | Mobilna wygoda, interfejs i opinie graczy o Incaspin
c1h14 | H3 | Co pokazują użytkownicy w sekcji mobilnej Incaspin Opinie
c1h15 | H3 | Jak ocenić wygodę korzystania z Incaspin Casino Opinie
c1h16 | H2 | Końcowa ocena, reputacja i wnioski z Incaspin Recenzja
c1h17 | H3 | Jak podsumować zalety serwisu Incaspin przed decyzją końcową
c1h18 | H3 | Które elementy tworzą końcową ocenę portalu Incaspin Recenzja
c1h19 | H2 | Najczęściej zadawane pytania
c2h1 | H2 | How to Join Us
c2h2 | H2 | Licence, Safety, and Responsible Gaming
c2h3 | H2 | Banking at Inca Spin
c2h4 | H3 | Deposit Methods
c2h5 | H3 | Withdrawal Methods and Timelines
c2h6 | H3 | Supported Currencies
c2h7 | H2 | Withdrawal Limits
c2h8 | H2 | Our Game Library
c2h9 | H3 | Slots and Instant Games
c2h10 | H3 | Live Casino
c2h11 | H3 | Table Games and More
c2h12 | H2 | Our Software Providers
c2h13 | H2 | Our Welcome Package and Bonuses
c2h14 | H2 | Loyalty Programme and Gamification
c2h15 | H2 | IncaSpin on Mobile
c2h16 | H2 | Our Customer Support Team
c2h17 | H2 | Why Choose IncaSpin Casino
c2h18 | H2 | Frequently Asked Questions
c2h19 | H3 | Is IncaSpin Casino a licensed and legitimate platform?
c2h20 | H3 | What is the welcome bonus at Inca Spin?
c2h21 | H3 | How do I log in to my Inca Spin account?
c2h22 | H3 | Does IncaSpin Casino have a mobile app?
c2h23 | H3 | What is the minimum deposit at Inca Spin?
c2h24 | H3 | How quickly are withdrawals processed at IncaSpin?
c2h25 | H3 | What game providers power the IncaSpin Casino library?
c2h26 | H3 | Is there a no deposit bonus available at Inca Spin?
