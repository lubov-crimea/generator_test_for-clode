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

c0h1 | H2 | Available Games at Longfu88
c0h2 | H3 | Casino Games
c0h3 | H3 | Longfu 88 Live Casino
c0h4 | H3 | Dive into Fishing
c0h5 | H3 | P2P – Play Against Other Players
c0h6 | H3 | Fast Games – Quick, Instant Wins
c0h7 | H3 | Sports Betting – Bet on Your Favorite Sports
c0h8 | H3 | Lottery
c0h9 | H2 | Bonuses – Boost Your Play with Generous Offers
c0h10 | H3 | Bonus Crab
c0h11 | H3 | Ongoing Promotions
c0h12 | H2 | Easy Registration and Seamless Login – Getting Started at Longfu88
c0h13 | H3 | Steps to Register:
c0h14 | H2 | Deposit Methods at Longfu 88
c0h15 | H2 | Customer Support
c0h16 | H2 | FAQs – Your Questions Answered
c0h17 | H3 | How do I register at Longfu88?
c0h18 | H3 | Can I use cryptocurrency to deposit?
c0h19 | H3 | How do I claim my bonus?
c0h20 | H3 | What games can I play at Longfu88?
c1h1 | H2 | About LongFu88
c1h2 | H2 | Casino games
c1h3 | H3 | Slots
c1h4 | H3 | Table games
c1h5 | H3 | Live Dealer Games
c1h6 | H3 | Free games
c1h7 | H3 | Sportsbook
c1h8 | H2 | Bonuses & promotions
c1h9 | H2 | Deposits & withdrawals
c1h10 | H3 | Deposit methods
c1h11 | H3 | Withdrawal methods
c1h12 | H2 | Mobile & app experience
c1h13 | H2 | Licensing & security
c1h14 | H2 | Customer support
c1h15 | H2 | Responsible gambling tools
c1h16 | H2 | Our verdict on LongFu88
c1h17 | H3 | LongFu88 overview
c1h18 | H2 | User Reviews
c3h1 | H2 | Welcome Bonuses and Promotional Offers
c3h2 | H3 | Claim Your 188% Welcome Bonus Today
c3h3 | H2 | Game Selection and Software Providers
c3h4 | H2 | Sports Betting Through SABA Sports
c3h5 | H3 | Bet on Global Sports Events
c3h6 | H2 | Banking Methods and Transaction Processing
c3h7 | H2 | Mobile Gaming Experience
c3h8 | H2 | VIP Program and Loyalty Rewards
c3h9 | H3 | Explore 2,500+ Casino Games
c3h10 | H2 | Security Measures and Fair Gaming
c3h11 | H2 | Customer Support Channels
c3h12 | H2 | Platform Overview
c3h13 | H2 | Tournament Competitions and Promotions
c3h14 | H2 | Responsible Gambling Tools
c3h15 | H2 | Game Provider Partnerships
c3h16 | H2 | Payment Security and Fraud Prevention
c3h17 | H3 | Experience Live Dealer Gaming
c3h18 | H2 | Should You Play at Longfu88?
c5h1 | H2 | Games and Providers – 7,500 Titles from 50+ Studios
c5h2 | H3 | Slots
c5h3 | H3 | Live Casino
c5h4 | H3 | Sports, E-sports and Lottery
c5h5 | H2 | Longfu88 Bonuses – Four Welcome Offers, One Account
c5h6 | H2 | VIP Programme – Bronze to Diamond
c5h7 | H2 | Payments – Local Methods for Malaysian Players
c5h8 | H2 | Is Longfu88 Safe? Security and Fair Play
c5h9 | H2 | Longfu88 Review – What Works and What to Know
c5h10 | H3 | Strengths
c5h11 | H3 | Worth knowing before you deposit
c5h12 | H2 | Mobile Access
c5h13 | H2 | Quick Links
c5h14 | H2 | Responsible Gambling
c5h15 | H2 | FAQ
c5h16 | H3 | Is longfu88 casino safe to play at?
c5h17 | H3 | What is the longfu88 welcome bonus?
c5h18 | H3 | How do I deposit at longfu88 Malaysia?
c5h19 | H3 | Does longfu88 have a mobile app?
c5h20 | H3 | What games does longfu88 casino have?
c6h1 | H2 | Sorotan Menyeluruh: Permainan, Bonus, Pembayaran & Kebolehpercayaan
c6h2 | H2 | Keselamatan: Main Dalam Persekitaran Terkawal
c6h3 | H2 | Bonus & Promosi di Longfu88 Casino
c6h4 | H3 | Analisis Bonus Selamat Datang
c6h5 | H3 | Ganjaran Berterusan Untuk Pemain Sedia Ada
c6h6 | H3 | Butiran Program VIP
c6h7 | H2 | Pilihan Permainan di Longfu Casino
c6h8 | H3 | Slot: Dunia Gulungan Untuk Semua Gaya
c6h9 | H3 | Kasino Langsung & Game Shows
c6h10 | H3 | Permainan Meja & Video Poker
c6h11 | H2 | Kaedah Pembayaran: Deposit & Pengeluaran
c6h12 | H2 | Sokongan Pemain & Permainan Bertanggungjawab
c6h13 | H2 | Kelebihan & Kekurangan Longfu Casino
c6h14 | H2 | Ringkasan: Mengapa Memilih Longfu 88 Casino?
c6h15 | H2 | Pengalaman Sebenar: Akses Pantas & Ujian Sistem Pembayaran
c6h16 | H3 | Akses Link Rasmi & Sistem Log Masuk Auto
c6h17 | H3 | Ujian Pembayaran: Berapa Cepat Boleh "Cuci"?
c6h18 | H3 | Kemudahan Navigasi Selepas Mendaftar
c6h19 | H3 | Variasi Mesin Slot & Rahsia Pusingan Pertaruhan (TO)
c6h20 | H3 | Sukan & Pertaruhan Bola Sepak (EPL)
c6h21 | H3 | Pengalaman Kasino Langsung (Live Casino) Tanpa Gangguan
c6h22 | H3 | Era Baharu Pembayaran Kripto
c6h23 | H3 | Keistimewaan Ahli VIP & Keutamaan Pengeluaran (Cuci)
c6h24 | H3 | Pengalaman Mudah Alih (Mobile UX) Tanpa Aplikasi Berat
c6h25 | H3 | Kesimpulan: Platform Stabil Dengan Proses Kewangan Pantas
c6h26 | H2 | Soalan Lazim (FAQ) - Longfu88
