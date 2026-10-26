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

c1h1 | H2 | BC Game офіційний сайт
c1h2 | H2 | Реєстрація на BC Game
c1h3 | H2 | Як скачати BC Game на мобільний
c1h4 | H2 | Найкращі ігри казино BCGame
c1h5 | H3 | Ігрові автомати
c1h6 | H3 | Лайв казино
c1h7 | H3 | Ставки на спорт
c1h8 | H3 | Лотерея
c1h9 | H2 | Платіжні системи
c1h10 | H3 | Виведення коштів
c1h11 | H2 | Заборонені країни
c1h12 | H2 | Бонуси та промо-акції
c1h13 | H2 | Сапорт
c1h14 | H2 | Вердикт
c1h15 | H2 | Поширені запитання
c1h16 | H3 | 💎 Казино БС Гейм легальне?
c1h17 | H3 | 📢 Кому належить BC Game?
c1h18 | H3 | 👨 З якого віку можна реєструватись у казино BCGame?
c1h19 | H3 | 📲 Де скачати BC Game для смартфона?
c1h20 | H2 | Схожі казино
c1h21 | H2 | BC Game відгуки
c2h1 | H2 | Эволюция игровых технологий на основе блокчейна
c2h2 | H2 | Навигация по глобальным нормативам
c2h3 | H2 | Играйте ответственно
c2h4 | H2 | Исследуйте экосистему
c2h5 | H3 | Будьте в курсе событий
c2h6 | H3 | Присоединяйтесь к сообществу
c2h7 | H3 | Станьте владельцем криптовалюты
