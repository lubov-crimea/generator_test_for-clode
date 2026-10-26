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

c0h1 | H2 | Log Masuk Ahli yang Selamat
c0h2 | H3 | Terlupa Kata Laluan?
c0h3 | H2 | Pengalaman Longfu Menanti
c0h4 | H2 | Belum Ada Akaun?
c0h5 | H2 | Soalan Log Masuk Lazim
c1h1 | H2 | How to Register and Log In to Your Longfu88 Account
c1h2 | H3 | Step-by-Step Registration Process
c1h3 | H2 | Troubleshooting Login Issues – Get Back to Gaming Fast
c1h4 | H3 | 1. Double-Check Your Login Information
c1h5 | H3 | 2. Clear Your Browser Cache and Cookies
c1h6 | H3 | 3. Try a Different Device or Browser
c1h7 | H3 | 4. Contact Customer Support
c1h8 | H2 | Longfu88 Casino Bonuses – Start Your Journey with Exciting Offers
c1h9 | H3 | Welcome Bonus Overview
c1h10 | H2 | Customer Support – We’re Here to Help!
c1h11 | H2 | FAQ – Frequently Asked Questions
c1h12 | H3 | How do I log in to my Longfu88 account?
c1h13 | H3 | What should I do if I forgot my password?
c1h14 | H3 | How do I verify my account?
c1h15 | H3 | Can I log in from multiple devices?
c2h1 | H2 | How to Register at Longfu88
c2h2 | H3 | Create Your Account ‚Äî Claim 188% Welcome Bonus
c2h3 | H2 | Longfu88 Login Process ‚Äî Quick Access to Your Account
c2h4 | H3 | Account Recovery and Password Reset
c2h5 | H2 | Account Security Features at Longfu88
c2h6 | H2 | Account Verification Requirements
c2h7 | H3 | Verify Your Account ‚Äî Unlock Full Access
c2h8 | H2 | Managing Your Longfu88 Account Settings
c2h9 | H3 | Deposit and Withdrawal Limits
c2h10 | H3 | Communication Preferences
c2h11 | H2 | Multi-Currency and Multi-Account Policies
c2h12 | H2 | Account Closure and Self-Exclusion
c2h13 | H3 | Your Account Opens Thousands of Games
c2h14 | H2 | Mobile Account Access
c2h15 | H2 | VIP Account Benefits and Tier Progression
c3h1 | H2 | Apa yang Anda Perlukan untuk Bermula
c3h2 | H2 | Cara Membayar untuk Pendaftaran dan Deposit Pertama Anda
c3h3 | H2 | Sokongan untuk Pertanyaan Akaun Anda
c3h4 | H3 | Sembang Langsung
c3h5 | H3 | E-mel Sokongan
c3h6 | H3 | Pusat Bantuan
c3h7 | H2 | Bagaimana Kami Melindungi Maklumat Pendaftaran Anda
c3h8 | H3 | Enkripsi SSL 256-bit
c3h9 | H3 | Pengesahan Identiti Dua Lapisan
c3h10 | H3 | Privasi Data
c3h11 | H3 | Pengesahan Pembayaran
c3h12 | H3 | Perlindungan Akaun
c3h13 | H3 | Pemantauan Aktiviti
c3h14 | H2 | Pertanyaan Pengguna Baru tentang Pendaftaran
c4h1 | H2 | Sediakan Akaun Anda dalam Tiga Langkah
c4h2 | H2 | Deposit dengan Pilihan Pembayaran Anda
c4h3 | H3 | Touch 'n Go
c4h4 | H3 | GrabPay
c4h5 | H3 | Boost
c4h6 | H3 | FPX
c4h7 | H2 | Sokongan Ketika Anda Memerlukannya
c4h8 | H3 | Lupa Kata Sandi
c4h9 | H3 | Pengesahan Akaun
c4h10 | H3 | Hubungi Pasukan Kami
c4h11 | H2 | Privasi dan Perlindungan Akaun
c4h12 | H3 | Enkripsi SSL 256-bit
c4h13 | H3 | Pengesahan Identiti
c4h14 | H3 | Perlindungan Data
c4h15 | H3 | Pengesahan Dua Faktor
c4h16 | H3 | Pantau Aktiviti Login
c4h17 | H3 | Perlindungan Pengeluaran
c4h18 | H2 | Soalan Lazim tentang Login dan Akaun
