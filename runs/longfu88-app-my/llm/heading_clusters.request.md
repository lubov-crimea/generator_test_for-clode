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

c0h1 | H2 | Lobi bergerak untuk telefon anda
c0h2 | H2 | 6 fungsi yang terasa laju
c0h3 | H2 | Pasang dalam 3 langkah mudah
c0h4 | H2 | Keperluan telefon sebelum pasang
c0h5 | H2 | 6 skrin utama dalam aplikasi
c0h6 | H2 | Bantuan khusus untuk aplikasi
c0h7 | H3 | Sembang aplikasi
c0h8 | H3 | E-mel sokongan
c0h9 | H3 | Pusat pemasangan
c0h10 | H2 | Cara kami lindungi aplikasi
c0h11 | H3 | Pautan dalam akaun
c0h12 | H3 | Semakan kod
c0h13 | H3 | Sesi peranti
c0h14 | H3 | Pemulihan akaun
c0h15 | H3 | Kebenaran minimum
c0h16 | H3 | Kemas kini terkawal
c0h17 | H2 | Aplikasi berbanding pelayar mudah alih
c0h18 | H3 | Kelajuan masuk
c0h19 | H3 | Kegemaran lobi
c0h20 | H3 | Notifikasi akaun
c0h21 | H3 | Paparan meja langsung
c0h22 | H3 | Slip taruhan
c0h23 | H3 | Kawalan storan
c0h24 | H2 | Soalan lazim tentang aplikasi
c1h1 | H2 | Apa yang aplikasi mudah alih longfu88 tawarkan
c1h2 | H2 | Ciri-ciri yang dipandu oleh keselamatan dan kecepatan
c1h3 | H3 | Login Biometrik
c1h4 | H3 | Notifikasi Betul pada Masa
c1h5 | H3 | Mod Gelap
c1h6 | H3 | Pratonton Lobby Luar Talian
c1h7 | H3 | Deposit Cepat Dalam Aplikasi
c1h8 | H3 | Penarikan Terus ke e-Dompet
c1h9 | H2 | Muat turun dan pasang dalam 3 langkah
c1h10 | H2 | Keserasian aplikasi untuk Android dan iOS
c1h11 | H3 | Android
c1h12 | H3 | iOS
c1h13 | H3 | Sambungan Internet
c1h14 | H3 | Wilayah Disokong
c1h15 | H2 | Apa yang anda lihat apabila membuka aplikasi longfu88
c1h16 | H2 | Bantuan untuk pengguna aplikasi mudah alih
c1h17 | H3 | Sembang Sokongan Dalam Aplikasi
c1h18 | H3 | E-mel Sokongan
c1h19 | H3 | Panduan Pemasangan & FAQ
c1h20 | H2 | Kepercayaan dan keselamatan dalam aplikasi longfu88
c1h21 | H3 | Penandatanganan Kod Swasta
c1h22 | H3 | Tiada Kedai Pihak Ketiga
c1h23 | H3 | Enkripsi Data Pengguna
c1h24 | H3 | Pengesahan Dua Lapisan
c1h25 | H3 | Pemulihan Akaun Jika Terlupa Kata Laluan
c1h26 | H3 | Perlindungan Permintaan Penarikan
c1h27 | H2 | Mengapa aplikasi mudah alih longfu88 mengatasi versi penyemak imbas
c1h28 | H2 | Soalan tentang aplikasi mudah alih longfu88
c2h1 | H2 | Add LongFu88 to Your Home Screen — One-Time Setup
c2h2 | H3 | Android — Chrome (Recommended)
c2h3 | H3 | iPhone / iPad — Safari
c2h4 | H2 | What Works on Mobile — Everything
c2h5 | H3 | Slots
c2h6 | H3 | Live Casino
c2h7 | H3 | Sports Betting
c2h8 | H3 | Deposits & Withdrawals
c2h9 | H3 | Account Management
c2h10 | H2 | Login on Mobile — Options
c2h11 | H2 | Mobile Performance — Minimum Requirements
c2h12 | H3 | Android
c2h13 | H3 | iPhone / iPad
c2h14 | H2 | Mobile Notifications — Stay Updated on Bonuses
c2h15 | H2 | Troubleshooting — Common Mobile Issues
c2h16 | H3 | Site not loading on mobile
c2h17 | H3 | Game not launching
c2h18 | H3 | Login loop — keeps returning to login screen
c2h19 | H3 | Live stream buffering on 4G
c2h20 | H3 | Home screen shortcut not showing casino — shows browser address bar
c2h21 | H2 | Mobile Security
c2h22 | H2 | FAQ – LongFu88 Mobile
c2h23 | H3 | Why doesn’t LongFu88 have a dedicated app?
c2h24 | H3 | Can I deposit and withdraw on mobile?
c2h25 | H3 | Does mobile use more data than desktop?
c2h26 | H3 | Can I use Face ID or fingerprint to log in?
c2h27 | H3 | Is the mobile experience the same as desktop?
c2h28 | H3 | Where do I find the Long Fu88 mobile version?
c4h1 | H2 | What the longfu88 App Adds to Your Experience
c4h2 | H2 | App Capabilities Worth Knowing About
c4h3 | H2 | Install the App in 3 Steps
c4h4 | H2 | Phones and Versions the App Runs On
c4h5 | H2 | What You See Inside the longfu88 App
c4h6 | H2 | Get Help for Any App Issue Fast
c4h7 | H2 | How We Keep Your App Account Safe
c4h8 | H3 | Code-Signed APK
c4h9 | H3 | Single Official Source
c4h10 | H3 | Encrypted Data in Transit
c4h11 | H3 | Account Recovery Process
c4h12 | H3 | Session Timeout Control
c4h13 | H3 | No Third-Party SDK Tracking
c4h14 | H2 | App Experience Compared to Mobile Browser
c4h15 | H3 | Login Speed
c4h16 | H3 | Push Notifications
c4h17 | H3 | Offline Lobby Preview
c4h18 | H3 | Live Stream Stability
c4h19 | H3 | Quick Deposit Access
c4h20 | H3 | Storage vs No-Install
c4h21 | H2 | Questions About the longfu88 App Answered
c4h22 | H2 | Related Pages
