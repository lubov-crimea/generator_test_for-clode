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

c0h1 | H2 | Pakiet Powitalny Rockyspin Casino
c0h2 | H2 | Rockyspin Casino
c0h3 | H2 | Darmowe automaty demo w Rockyspin
c0h4 | H2 | Gry w Rockyspin Casino
c0h5 | H3 | Automaty i gry specjalne
c0h6 | H3 | Kasyno na żywo w Rockyspin
c0h7 | H2 | Najnowsze duże wygrane w Rockyspin
c0h8 | H2 | Bonusy i promocje w Rockyspin
c0h9 | H3 | Podział pakietu powitalnego
c0h10 | H3 | Stałe promocje i turnieje
c0h11 | H3 | Bonus powitalny na zakłady sportowe
c0h12 | H2 | Metody płatności w Rockyspin
c0h13 | H3 | Opcje depozytów i wypłat
c0h14 | H3 | Limity wypłat i proces wypłaty
c0h15 | H2 | Programy VIP i lojalnościowe Rockyspin
c0h16 | H3 | Korzyści na poziomie Gold i Platinum
c0h17 | H3 | Jak ranga wpływa na limity kasy
c0h18 | H2 | Turnieje i konkursy w Rockyspin
c0h19 | H2 | Opinie graczy
c0h20 | H2 | Widzisz coś, co powinniśmy poprawić?
c0h21 | H2 | Dzięki — mamy to!
c1h1 | H2 | Rocky Spin Casino w pigułce
c1h2 | H3 | Informacje o Rocky Spin Casino
c1h3 | H2 | Logowanie do Rocky Spin Casino krok po kroku
c1h4 | H3 | Problemy z logowaniem — co zrobić
c1h5 | H2 | Rejestracja w Rocky Spin Casino w 6 krokach
c1h6 | H2 | Bonusy Rocky Spin Casino — sprawdzamy warunki
c1h7 | H3 | Cashback w Rocky Spin Casino
c1h8 | H3 | Rocky Spin Promo code
c1h9 | H2 | Wpłaty w Rocky Spin Casino: metody i księgowanie
c1h10 | H3 | Bezpieczeństwo płatności i danych
c1h11 | H2 | Wypłaty w Rocky Spin Casino: metody, czas, KYC
c1h12 | H3 | Weryfikacja KYC przed pierwszą wypłatą
c1h13 | H2 | Plusy i minusy Rocky Spin Casino
c1h14 | H2 | Opinie graczy o Rocky Spin Casino
c1h15 | H2 | Odpowiedzialna gra
c2h1 | H2 | Obraz kasyna RockySpin
c2h2 | H2 | Rocky Spin Casino promo code
c2h3 | H3 | Szczegóły promocji:
c2h4 | H2 | Rocky Spin bonusy
c2h5 | H3 | Welcome Bonus
c2h6 | H3 | Newbie Spins
c2h7 | H3 | Cashback
c2h8 | H2 | Casino login
c2h9 | H2 | Rocky Spin Casino opinie
c2h10 | H2 | Sklep w RockySpin – Wymień monety na nagrody
c2h11 | H3 | Dostępne kategorie nagród:
c2h12 | H3 | Jak zdobywać monety?
c2h13 | H2 | Turnieje z nagrodami
c2h14 | H2 | Loteria Newbie Spins
c2h15 | H2 | Zakłady sportowe w RockySpin
c2h16 | H2 | Program Lojalnościowy w RockySpin
c2h17 | H3 | Jak zdobyć kolejne rangi w programie lojalnościowym RockySpin
c2h18 | H3 | Dołącz do RockySpin i graj po swojemu
