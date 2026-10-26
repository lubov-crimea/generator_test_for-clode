# SYSTEM

You are a senior SEO content strategist for iGaming affiliate sites. You build the technical brief (ТЗ) for ONE casino-brand review page that must outrank the given competitors for the given keywords in the given GEO.

You receive JSON with: geo, page language, brand and keywords, competitor H1s, keyword statistics of competitors, heading clusters (frequency, mandatory flag, typical section length, typical position), entity candidates mined from competitor texts, and numeric targets.

Work like this:

1. Decide the search intent behind the keywords (usually: brand query -> informational + navigational review page: what the casino is, register, login, bonuses, games, payments, app, safety). Put it in `intent_summary`.

2. Build the heading structure as a flat ordered list of blocks. Block 1 is the H1 (level 1) with a short intro. All other blocks are H2-H6.
   - EVERY cluster flagged `mandatory: true` must be covered by a heading (several near-duplicate clusters may share one heading; list their ids in `covers_clusters`).
   - Add a unique (non-mandatory) cluster only if it fits the intent and adds value. Skip off-topic ones.
   - Order blocks logically, using `avg_position` as a hint. Never skip heading levels (H2 -> H4). H3+ must sit under a fitting parent.
   - Headings are written in the page language. Put keywords into headings only where it reads naturally and where competitors do it.

3. For EVERY block provide all of the following (this is the format of the ТЗ):
   - `words_min` / `words_max`: allowed length of the BODY text (heading excluded). Use competitors' typical section lengths. The range width is about ±15% of the middle (max/min <= 1.4 is typical; never above 1.8). The sum of all middles must be close to `target_body_words`. A parent heading's own range covers only its own intro text; sub-sections have their own ranges.
   - `keywords`: how many times each keyword must appear in the BODY of this block (heading excluded). Include EVERY keyword, 0 when unused. For every keyword: sum over all blocks + occurrences inside headings must equal `keyword_targets[keyword]` exactly. Counting rules: case-insensitive, whole words, longest match first (an occurrence of "X casino" counts only for "X casino", not also for "X"). Spread them naturally: the brand early (intro) and in key sections, long-tail variants (login, app, register...) in the sections where they belong. Never more than 1 keyword mention per ~15 words in a block.
   - `entities`: 2-10 entities the block must cover, each with `priority` 1-10 (10 = the main entity of the block). Take them from `entity_candidates` and from the topic (payment systems, game providers, regulators, bonus types, technical terms, game types). Use generic names for the brand itself (e.g. "Online Casino"), never the brand name. Entities that are specific facts about the brand (a licence, a payment method, a provider) may be listed only if they appear in `facts_to_respect` or are clearly competitor-wide industry standards; otherwise list the category (e.g. "E-wallets") and let the notes say "name specifics only if given in the brand information".
   - `entity_connections`: 1-4 relations between entities the text must state explicitly, as subject -> relation (a verb phrase) -> object, with `priority` 1-10. Example: Licence -> regulates -> Online Casino [8].
   - `summary`: 1-3 sentences, what the block says, in the page language.
   - `copywriter_notes`: binding instructions in the page language: which entity to lead with, order of the argument, what to avoid, which facts must not be invented, tone. Concrete, not generic.
   - `formats`: list from ["paragraph", "list", "table"]. Steps/features -> list, comparisons/payment methods/specs -> table, explanations -> paragraph. A block may combine formats (e.g. ["paragraph","list"]).
   - `source`: "h1", "mandatory" or "unique".
   Write `summary`, `copywriter_notes` and entity/relation names in the PAGE LANGUAGE (like a real ТЗ for a writer in that language).

4. Check the whole brief for consistency before answering: logical order, no overlapping blocks, the intro does not duplicate later sections, entity connections do not contradict each other, keyword and word sums are correct.

Return the result through the tool.

# USER

{
 "geo": "PL",
 "page_language": "Polish",
 "keywords": [
  "Rockyspin",
  "Rocky Spin",
  "Rockyspin casino",
  "Rocky Spin casino",
  "Rockyspin login",
  "Rockyspin app",
  "Rockyspin register",
  "Rockyspin official",
  "Rockyspin online casino"
 ],
 "facts_to_respect": [],
 "competitor_h1": [
  "Rockyspin Casino: Automaty i kasyno na żywo",
  "Rocky Spin Casino — przewodnik gracza: logowanie, bonusy i wypłaty",
  "Rocky Spin Casino"
 ],
 "competitor_stats": [
  {
   "url": "https://rocky-spins.pl/",
   "body_words": 2989,
   "keywords_in_total": {
    "Rockyspin": 16,
    "Rocky Spin": 0,
    "Rockyspin casino": 7,
    "Rocky Spin casino": 0,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 1
   },
   "keywords_in_h1": {
    "Rockyspin": 0,
    "Rocky Spin": 0,
    "Rockyspin casino": 1,
    "Rocky Spin casino": 0,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 0
   },
   "keywords_in_h2": {
    "Rockyspin": 6,
    "Rocky Spin": 0,
    "Rockyspin casino": 3,
    "Rocky Spin casino": 0,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 0
   }
  },
  {
   "url": "https://rockyspins.com.pl/pl/",
   "body_words": 1357,
   "keywords_in_total": {
    "Rockyspin": 0,
    "Rocky Spin": 1,
    "Rockyspin casino": 0,
    "Rocky Spin casino": 15,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 0
   },
   "keywords_in_h1": {
    "Rockyspin": 0,
    "Rocky Spin": 0,
    "Rockyspin casino": 0,
    "Rocky Spin casino": 1,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 0
   },
   "keywords_in_h2": {
    "Rockyspin": 0,
    "Rocky Spin": 0,
    "Rockyspin casino": 0,
    "Rocky Spin casino": 8,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 0
   }
  },
  {
   "url": "https://rockyspin-pl.com/pl-pl/",
   "body_words": 1133,
   "keywords_in_total": {
    "Rockyspin": 13,
    "Rocky Spin": 2,
    "Rockyspin casino": 0,
    "Rocky Spin casino": 5,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 0
   },
   "keywords_in_h1": {
    "Rockyspin": 0,
    "Rocky Spin": 0,
    "Rockyspin casino": 0,
    "Rocky Spin casino": 1,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 0
   },
   "keywords_in_h2": {
    "Rockyspin": 4,
    "Rocky Spin": 1,
    "Rockyspin casino": 0,
    "Rocky Spin casino": 2,
    "Rockyspin login": 0,
    "Rockyspin app": 0,
    "Rockyspin register": 0,
    "Rockyspin official": 0,
    "Rockyspin online casino": 0
   }
  }
 ],
 "targets": {
  "target_body_words": 1357,
  "keyword_targets": {
   "Rockyspin": 13,
   "Rocky Spin": 1,
   "Rockyspin casino": 1,
   "Rocky Spin casino": 5,
   "Rockyspin login": 1,
   "Rockyspin app": 1,
   "Rockyspin register": 1,
   "Rockyspin official": 1,
   "Rockyspin online casino": 1
  }
 },
 "heading_clusters": [
  {
   "id": "k01",
   "canonical_title": "Rockyspin Casino w skrócie",
   "topic": "Casino overview / at a glance",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 108,
   "avg_position": 0.09,
   "examples": [
    "Rockyspin Casino",
    "Rocky Spin Casino w pigułce",
    "Informacje o Rocky Spin Casino",
    "Obraz kasyna RockySpin"
   ]
  },
  {
   "id": "k02",
   "canonical_title": "Bonusy i pakiet powitalny",
   "topic": "Welcome package and bonuses",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 93,
   "avg_position": 0.29,
   "examples": [
    "Pakiet Powitalny Rockyspin Casino",
    "Bonusy i promocje w Rockyspin",
    "Podział pakietu powitalnego",
    "Bonusy Rocky Spin Casino — sprawdzamy warunki"
   ]
  },
  {
   "id": "k17",
   "canonical_title": "Opinie graczy",
   "topic": "Player reviews",
   "frequency": 3,
   "mandatory": true,
   "levels": [
    2
   ],
   "avg_section_words": 125,
   "avg_position": 0.78,
   "examples": [
    "Opinie graczy",
    "Opinie graczy o Rocky Spin Casino",
    "Rocky Spin Casino opinie"
   ]
  },
  {
   "id": "k03",
   "canonical_title": "Kod promocyjny",
   "topic": "Promo code",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 74,
   "avg_position": 0.27,
   "examples": [
    "Rocky Spin Promo code",
    "Rocky Spin Casino promo code",
    "Szczegóły promocji:"
   ]
  },
  {
   "id": "k18",
   "canonical_title": "Logowanie do kasyna",
   "topic": "Login",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 64,
   "avg_position": 0.3,
   "examples": [
    "Logowanie do Rocky Spin Casino krok po kroku",
    "Problemy z logowaniem — co zrobić",
    "Casino login"
   ]
  },
  {
   "id": "k04",
   "canonical_title": "Cashback",
   "topic": "Cashback",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    3
   ],
   "avg_section_words": 98,
   "avg_position": 0.43,
   "examples": [
    "Cashback w Rocky Spin Casino",
    "Cashback"
   ]
  },
  {
   "id": "k12",
   "canonical_title": "Metody płatności i wpłaty",
   "topic": "Deposits and payment methods",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 148,
   "avg_position": 0.6,
   "examples": [
    "Metody płatności w Rockyspin",
    "Opcje depozytów i wypłat",
    "Wpłaty w Rocky Spin Casino: metody i księgowanie"
   ]
  },
  {
   "id": "k06",
   "canonical_title": "Zakłady sportowe",
   "topic": "Sports betting and sports welcome bonus",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 86,
   "avg_position": 0.68,
   "examples": [
    "Bonus powitalny na zakłady sportowe",
    "Zakłady sportowe w RockySpin"
   ]
  },
  {
   "id": "k07",
   "canonical_title": "Turnieje i stałe promocje",
   "topic": "Tournaments and ongoing promotions",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 109,
   "avg_position": 0.69,
   "examples": [
    "Stałe promocje i turnieje",
    "Turnieje i konkursy w Rockyspin",
    "Turnieje z nagrodami"
   ]
  },
  {
   "id": "k13",
   "canonical_title": "Wypłaty: limity i czas",
   "topic": "Withdrawals, limits and process",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 168,
   "avg_position": 0.7,
   "examples": [
    "Limity wypłat i proces wypłaty",
    "Wypłaty w Rocky Spin Casino: metody, czas, KYC"
   ]
  },
  {
   "id": "k16",
   "canonical_title": "Program VIP i lojalnościowy",
   "topic": "VIP and loyalty program",
   "frequency": 2,
   "mandatory": true,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 107,
   "avg_position": 0.82,
   "examples": [
    "Programy VIP i lojalnościowe Rockyspin",
    "Korzyści na poziomie Gold i Platinum",
    "Jak ranga wpływa na limity kasy",
    "Program Lojalnościowy w RockySpin"
   ]
  },
  {
   "id": "k08",
   "canonical_title": "Darmowe automaty demo",
   "topic": "Demo slots",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 0,
   "avg_position": 0.14,
   "examples": [
    "Darmowe automaty demo w Rockyspin"
   ]
  },
  {
   "id": "k09",
   "canonical_title": "Gry i automaty",
   "topic": "Games overview and slots",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 207,
   "avg_position": 0.21,
   "examples": [
    "Gry w Rockyspin Casino",
    "Automaty i gry specjalne"
   ]
  },
  {
   "id": "k10",
   "canonical_title": "Kasyno na żywo",
   "topic": "Live casino",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 207,
   "avg_position": 0.29,
   "examples": [
    "Kasyno na żywo w Rockyspin"
   ]
  },
  {
   "id": "k11",
   "canonical_title": "Największe wygrane",
   "topic": "Biggest recent wins",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 0,
   "avg_position": 0.33,
   "examples": [
    "Najnowsze duże wygrane w Rockyspin"
   ]
  },
  {
   "id": "k19",
   "canonical_title": "Rejestracja krok po kroku",
   "topic": "Registration",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 68,
   "avg_position": 0.33,
   "examples": [
    "Rejestracja w Rocky Spin Casino w 6 krokach"
   ]
  },
  {
   "id": "k05",
   "canonical_title": "Newbie Spins",
   "topic": "Newbie spins / lottery",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 47,
   "avg_position": 0.56,
   "examples": [
    "Newbie Spins",
    "Loteria Newbie Spins"
   ]
  },
  {
   "id": "k22",
   "canonical_title": "Sklep z nagrodami",
   "topic": "Coin shop / rewards store",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2,
    3
   ],
   "avg_section_words": 40,
   "avg_position": 0.61,
   "examples": [
    "Sklep w RockySpin – Wymień monety na nagrody",
    "Dostępne kategorie nagród:",
    "Jak zdobywać monety?"
   ]
  },
  {
   "id": "k14",
   "canonical_title": "Bezpieczeństwo płatności i danych",
   "topic": "Payment and data security",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 70,
   "avg_position": 0.67,
   "examples": [
    "Bezpieczeństwo płatności i danych"
   ]
  },
  {
   "id": "k15",
   "canonical_title": "Weryfikacja KYC",
   "topic": "KYC verification",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 62,
   "avg_position": 0.8,
   "examples": [
    "Weryfikacja KYC przed pierwszą wypłatą"
   ]
  },
  {
   "id": "k20",
   "canonical_title": "Plusy i minusy",
   "topic": "Pros and cons",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 83,
   "avg_position": 0.87,
   "examples": [
    "Plusy i minusy Rocky Spin Casino"
   ]
  },
  {
   "id": "k24",
   "canonical_title": "(widget)",
   "topic": "UI feedback widget (noise, not content)",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 12,
   "avg_position": 0.98,
   "examples": [
    "Widzisz coś, co powinniśmy poprawić?",
    "Dzięki — mamy to!"
   ]
  },
  {
   "id": "k21",
   "canonical_title": "Odpowiedzialna gra",
   "topic": "Responsible gambling",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    2
   ],
   "avg_section_words": 95,
   "avg_position": 1.0,
   "examples": [
    "Odpowiedzialna gra"
   ]
  },
  {
   "id": "k23",
   "canonical_title": "Dołącz i graj",
   "topic": "Closing call to action",
   "frequency": 1,
   "mandatory": false,
   "levels": [
    3
   ],
   "avg_section_words": 18,
   "avg_position": 1.0,
   "examples": [
    "Dołącz do RockySpin i graj po swojemu"
   ]
  }
 ],
 "entity_candidates": [
  {
   "entity": "Ciebie",
   "competitors": 3
  },
  {
   "entity": "EUR",
   "competitors": 3
  },
  {
   "entity": "Mastercard",
   "competitors": 3
  },
  {
   "entity": "VIP",
   "competitors": 2
  },
  {
   "entity": "Pragmatic Play",
   "competitors": 2
  },
  {
   "entity": "Apple Pay",
   "competitors": 2
  },
  {
   "entity": "Google Pay",
   "competitors": 2
  },
  {
   "entity": "Kasie",
   "competitors": 2
  },
  {
   "entity": "Google",
   "competitors": 2
  },
  {
   "entity": "Olympus",
   "competitors": 2
  },
  {
   "entity": "Rookie Rumble",
   "competitors": 2
  },
  {
   "entity": "Book",
   "competitors": 2
  },
  {
   "entity": "Gates",
   "competitors": 2
  },
  {
   "entity": "Androida",
   "competitors": 2
  },
  {
   "entity": "Do 25",
   "competitors": 2
  },
  {
   "entity": "USD",
   "competitors": 2
  },
  {
   "entity": "Loteria Newbie Spins",
   "competitors": 2
  },
  {
   "entity": "PLN",
   "competitors": 2
  },
  {
   "entity": "BGaming",
   "competitors": 1
  },
  {
   "entity": "KYC",
   "competitors": 1
  },
  {
   "entity": "Do 72",
   "competitors": 1
  },
  {
   "entity": "Win",
   "competitors": 1
  },
  {
   "entity": "Gold",
   "competitors": 1
  },
  {
   "entity": "Evolution",
   "competitors": 1
  },
  {
   "entity": "Pragmatic Play Live",
   "competitors": 1
  },
  {
   "entity": "Wins",
   "competitors": 1
  },
  {
   "entity": "Daily Bronze",
   "competitors": 1
  },
  {
   "entity": "Twoją",
   "competitors": 1
  },
  {
   "entity": "Bonus",
   "competitors": 1
  },
  {
   "entity": "Newbie Spins",
   "competitors": 1
  },
  {
   "entity": "Platinum",
   "competitors": 1
  },
  {
   "entity": "Rossobash SRL",
   "competitors": 1
  },
  {
   "entity": "Penguin King",
   "competitors": 1
  },
  {
   "entity": "RNG",
   "competitors": 1
  },
  {
   "entity": "Bonus Buy",
   "competitors": 1
  },
  {
   "entity": "Trending",
   "competitors": 1
  },
  {
   "entity": "Deutsches Roulette",
   "competitors": 1
  },
  {
   "entity": "Sunday Reload",
   "competitors": 1
  },
  {
   "entity": "RELDAY",
   "competitors": 1
  },
  {
   "entity": "Live Tournament",
   "competitors": 1
  },
  {
   "entity": "BTC",
   "competitors": 1
  },
  {
   "entity": "ETH",
   "competitors": 1
  },
  {
   "entity": "LTC",
   "competitors": 1
  },
  {
   "entity": "BCH",
   "competitors": 1
  },
  {
   "entity": "DOGE",
   "competitors": 1
  },
  {
   "entity": "TRX",
   "competitors": 1
  },
  {
   "entity": "Zarejestruj",
   "competitors": 1
  },
  {
   "entity": "Kasa",
   "competitors": 1
  },
  {
   "entity": "Royal Joker",
   "competitors": 1
  },
  {
   "entity": "Big Bass Bonanza",
   "competitors": 1
  },
  {
   "entity": "Starburst",
   "competitors": 1
  },
  {
   "entity": "Szop Rocky",
   "competitors": 1
  },
  {
   "entity": "Rocky750",
   "competitors": 1
  },
  {
   "entity": "Srebro",
   "competitors": 1
  },
  {
   "entity": "Złoto",
   "competitors": 1
  },
  {
   "entity": "Platyna",
   "competitors": 1
  },
  {
   "entity": "Programy VIP",
   "competitors": 1
  },
  {
   "entity": "Kostaryce",
   "competitors": 1
  },
  {
   "entity": "Kostaryki",
   "competitors": 1
  },
  {
   "entity": "USA",
   "competitors": 1
  }
 ]
}
