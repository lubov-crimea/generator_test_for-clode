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
c2h1 | H2 | Bonus offers and promotions
c2h2 | H3 | Welcome bonus
c2h3 | H3 | Other promotions
c2h4 | H2 | Rewards and loyalty programs at LongFu88
c2h5 | H2 | Licensing & security information
c2h6 | H2 | Usability and user experience
c2h7 | H3 | Navigation
c2h8 | H3 | Design
c2h9 | H2 | LongFu88 App
c2h10 | H2 | Payment methods
c2h11 | H3 | Deposit methods
c2h12 | H3 | Withdrawal methods
c2h13 | H3 | Deposit and withdrawal limits in Singapore
c2h14 | H3 | Deposit and withdrawal limits in Thailand
c2h15 | H2 | Customer service
c2h16 | H2 | Sports betting overview
c2h17 | H3 | Sports coverage (20+)
c2h18 | H3 | Sports odds
c2h19 | H3 | Live betting and streaming
c2h20 | H3 | Limits
c2h21 | H3 | Betting markets
c2h22 | H3 | Minimum / maximum deposits
c2h23 | H2 | Esports betting overview
c2h24 | H3 | Esports coverage
c2h25 | H3 | Esports odds
c2h26 | H3 | Esports live betting and streaming
c2h27 | H3 | Esports betting markets
c2h28 | H2 | Casino overview
c2h29 | H3 | Software providers
c2h30 | H3 | Selection of casino games
c2h31 | H3 | Live dealer games
c2h32 | H3 | Minimum / maximum deposits
c2h33 | H2 | Registration at LongFu88
c2h34 | H2 | Conclusion
c2h35 | H2 | User Reviews
c3h1 | H2 | Games and Providers – 7,500 Titles from 50+ Studios
c3h2 | H3 | Slots
c3h3 | H3 | Live Casino
c3h4 | H3 | Sports, E-sports and Lottery
c3h5 | H2 | Longfu88 Bonuses – Four Welcome Offers, One Account
c3h6 | H2 | VIP Programme – Bronze to Diamond
c3h7 | H2 | Payments – Local Methods for Malaysian Players
c3h8 | H2 | Is Longfu88 Safe? Security and Fair Play
c3h9 | H2 | Longfu88 Review – What Works and What to Know
c3h10 | H3 | Strengths
c3h11 | H3 | Worth knowing before you deposit
c3h12 | H2 | Mobile Access
c3h13 | H2 | Quick Links
c3h14 | H2 | Responsible Gambling
c3h15 | H2 | FAQ
c3h16 | H3 | Is longfu88 casino safe to play at?
c3h17 | H3 | What is the longfu88 welcome bonus?
c3h18 | H3 | How do I deposit at longfu88 Malaysia?
c3h19 | H3 | Does longfu88 have a mobile app?
c3h20 | H3 | What games does longfu88 casino have?
c4h1 | H2 | What You Find When You Open longfu88
c4h2 | H2 | Fan-Favourite Slots You Can Open Right Now
c4h3 | H3 | Classic Blackjack
c4h4 | H3 | French Roulette
c4h5 | H3 | Ocean Fortune
c4h6 | H3 | Halloween Fortune
c4h7 | H3 | Wild Walker
c4h8 | H3 | Fortune Mouse
c4h9 | H2 | Baccarat, Roulette and Dragon Tiger ‚Äî Streamed Live
c4h10 | H2 | Crash X, Aviator and Fast-Round Arcade Titles
c4h11 | H2 | How to Open Your Account and Reach the Games
c4h12 | H2 | Payments via Touch 'n Go, GrabPay, Boost dan FPX
c4h13 | H2 | Classic Table Games With Multiple Bet Ranges
c4h14 | H3 | Classic Blackjack
c4h15 | H3 | French Roulette
c4h16 | H3 | Ocean Fortune
c4h17 | H3 | Halloween Fortune
c4h18 | H3 | Wild Walker
c4h19 | H3 | Fortune Mouse
c4h20 | H2 | Thunder Fishing, Fish Rooms and Sportsbook Markets
c4h21 | H2 | Four Reasons Your Account Works Better Here
c4h22 | H3 | Local Payment Rails
c4h23 | H3 | Continuous Live Streams
c4h24 | H3 | Single Account Balance
c4h25 | H3 | Fast Account Verification
c4h26 | H2 | Playing longfu88 on Your Phone or Tablet
c4h27 | H2 | How We Protect Your Account and Ensure Fair Results
c4h28 | H3 | Encrypted Login
c4h29 | H3 | RNG Certification
c4h30 | H3 | Withdrawal Audit Trail
c4h31 | H3 | Two-Factor Option
c4h32 | H2 | Slot Themes, Live Rooms and Arcade Formats ‚Äî All in One Place
c4h33 | H2 | Check the Promo Board for What's Running This Week
c4h34 | H2 | Three Ways to Reach Our Support Team
c4h35 | H2 | Keeping Your longfu88 Account Safe
c4h36 | H2 | longfu88 in Malaysia ‚Äî Availability and Access
c4h37 | H2 | What We Hold Ourselves to on This Platform
c4h38 | H3 | Transparent Odds Display
c4h39 | H3 | Consistent Payout Processing
c4h40 | H3 | No Wallet Lock-In
c4h41 | H3 | 24-Hour Support Coverage
c4h42 | H2 | Deposit and Withdraw With Your Preferred Malaysian Wallet
c4h43 | H2 | Frequently Asked Questions About longfu88
c5h1 | H2 | Welcome Bonuses and Promotional Offers
c5h2 | H3 | Claim Your 188% Welcome Bonus Today
c5h3 | H2 | Game Selection and Software Providers
c5h4 | H2 | Sports Betting Through SABA Sports
c5h5 | H3 | Bet on Global Sports Events
c5h6 | H2 | Banking Methods and Transaction Processing
c5h7 | H2 | Mobile Gaming Experience
c5h8 | H2 | VIP Program and Loyalty Rewards
c5h9 | H3 | Explore 2,500+ Casino Games
c5h10 | H2 | Security Measures and Fair Gaming
c5h11 | H2 | Customer Support Channels
c5h12 | H2 | Key Platform Features
c5h13 | H2 | Tournament Competitions and Promotions
c5h14 | H2 | Responsible Gambling Tools
c5h15 | H2 | Game Provider Partnerships
c5h16 | H2 | Payment Security and Fraud Prevention
c5h17 | H3 | Experience Live Dealer Gaming
c5h18 | H2 | Join Longfu88 Today
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
c7h1 | H2 | Nombor ringkas di longfu88
c7h2 | H2 | Permainan utama dalam satu lobi
c7h3 | H3 | Andar Bahar
c7h4 | H3 | Secrets of Cleopatra
c7h5 | H3 | Lucky Twins
c7h6 | H3 | The Dog House Megaways
c7h7 | H3 | PUBG Mobile
c7h8 | H3 | Bombing Fishing
c7h9 | H2 | Studio dalam longfu88
c7h10 | H2 | Masuk ke ruang longfu88
c7h11 | H2 | Lima kawasan tahan lama
c7h12 | H3 | Pusat profil
c7h13 | H3 | Pilihan permainan
c7h14 | H3 | Rekod transaksi
c7h15 | H3 | Saluran sokongan
c7h16 | H3 | Terma laman
c7h17 | H2 | Rel pembayaran tempatan
c7h18 | H3 | Touch 'n Go
c7h19 | H3 | GrabPay
c7h20 | H3 | Boost
c7h21 | H3 | FPX
c7h22 | H2 | Tiga laluan sokongan
c7h23 | H3 | Live chat
c7h24 | H3 | Email
c7h25 | H3 | Bantuan mudah alih
c7h26 | H2 | Lobi lancar pada telefon
c7h27 | H2 | Cara kami bina keyakinan
c7h28 | H3 | Struktur boleh disemak
c7h29 | H3 | Akses polisi
c7h30 | H3 | Hubungan sokongan
c7h31 | H3 | Semakan transaksi
c7h32 | H2 | longfu88 berbanding carian berselerak
c7h33 | H2 | Akses Malaysia secara setempat
c7h34 | H2 | Cara bergerak dalam laman
c7h35 | H3 | Langkah pertama
c7h36 | H3 | Selepas akaun dibuka
c7h37 | H3 | Sebelum transaksi
c7h38 | H3 | Jika tersekat
c7h39 | H2 | FAQ
c7h40 | H2 | Empat perkara anda semak dahulu
c7h41 | H2 | Bacaan kadar dan kategori
c7h42 | H3 | Live Casino
c7h43 | H3 | Slots
c7h44 | H3 | Sportsbook
c7h45 | H3 | Crash Games
c7h46 | H3 | Bingo
c7h47 | H2 | Kawalan akaun dan akses
c7h48 | H2 | Enam tanda longfu88
c7h49 | H3 | Lobi gabungan
c7h50 | H3 | Tajuk dikenali
c7h51 | H3 | Studio jelas
c7h52 | H3 | Pilihan Malaysia
c7h53 | H3 | Kawalan akses
c7h54 | H3 | Bantuan tersusun
c8h1 | H2 | Perkara Pertama yang Perlu Anda Ketahui
c8h2 | H2 | Apa yang Menanti di Dalam Lobi longfu88
c8h3 | H3 | Fish Hunter
c8h4 | H3 | Lightning Roulette
c8h5 | H3 | Sugar Rush 1000
c8h6 | H3 | Badminton Betting
c8h7 | H3 | Caishen Wins
c8h8 | H3 | Aztec Gems
c8h9 | H2 | Studio Berkuasa Permainan longfu88
c8h10 | H2 | Meja, Permainan, dan Pasaran Tunggu Anda
c8h11 | H2 | Halaman Penting di longfu88
c8h12 | H3 | Panduan Pendaftaran Akaun
c8h13 | H3 | Cara Deposit dan Pengeluaran
c8h14 | H3 | Memahami RTP dan Varian Permainan
c8h15 | H3 | Kawalan Akaun dan Privasi Data
c8h16 | H3 | Hubungi Kami — Saluran dan Jam Operasi
c8h17 | H2 | Kaedah Pembayaran Tempatan kami
c8h18 | H3 | Touch 'n Go eWallet
c8h19 | H3 | GrabPay
c8h20 | H3 | Boost
c8h21 | H3 | FPX
c8h22 | H2 | longfu88 di Smartphone dan Tablet Anda
c8h23 | H2 | Hubungi Kami — Cara Terbaik untuk Anda
c8h24 | H3 | Chat Langsung
c8h25 | H3 | Dukungan Email
c8h26 | H3 | Bantuan Aplikasi Seluler
c8h27 | H2 | Tanda-tanda E-E-A-T longfu88
c8h28 | H3 | Struktur Akaun yang Dapat Diverifikasi
c8h29 | H3 | Saluran Sokongan yang Dapat Diakses
c8h30 | H3 | Kebijakan Privasi dan Keamanan
c8h31 | H3 | Keterlibatan Komunitas Jangka Panjang
c8h32 | H2 | longfu88 Versus Permainan Tersebar
c8h33 | H2 | longfu88 untuk Pemain Malaysia
c8h34 | H2 | Pertanyaan Lazim
c8h35 | H2 | Panduan Menavigasi longfu88
c8h36 | H3 | Langkah 1: Pendaftaran Akaun
c8h37 | H3 | Langkah 2: Memilih Kaedah Pembayaran
c8h38 | H3 | Langkah 3: Penjelajahan Lobi Pertama
c8h39 | H3 | Langkah 4: Mengelola Akaun Anda
c8h40 | H2 | Angka yang Menentukan longfu88
c8h41 | H2 | Cara Kami Melindungi Pengalaman Anda
c8h42 | H2 | RTP dan Transparansi Permainan longfu88
c8h43 | H3 | Slot
c8h44 | H3 | Kasino Langsung
c8h45 | H3 | Sportsbook
c8h46 | H3 | Permainan Arcade
c8h47 | H3 | Bingo
c8h48 | H2 | Enam Pilar Pengalaman longfu88
c8h49 | H3 | Lobi yang Tertata dengan Baik
c8h50 | H3 | Penyaring dan Pencarian Cepat
c8h51 | H3 | Mode Demo Gratis untuk Slot
c8h52 | H3 | Saldo dan Laporan Real-Time
c8h53 | H3 | Pengaturan Akaun yang Dapat Dipersonalisasi
c8h54 | H3 | Akses Responsif Lintas Perangkat
