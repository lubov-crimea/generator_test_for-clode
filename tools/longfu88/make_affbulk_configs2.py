"""Writes runs/<run>/05_affbulk_config.json for the local-language Longfu88 pages (4 sites x 5 GEO pages).

    python tools/longfu88/make_affbulk_configs2.py            # all 20 runs
    python tools/longfu88/make_affbulk_configs2.py longfu88-vietnam-v02 ...

Rules of this import (user, 2026-10-23): 12 random slots + 12 random crash games + all live games on every page; canonical of every page
points to itself; the five pages of a domain carry the same hreflang set; bonus pictures are the usual ones, pictures only (no caption
text); reviews are invented (editorial content). Facts (bonus figures) come from the knowledge base longfu88-new only.
"""
import datetime
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "longfu88"))
import make_affbulk_configs as en  # noqa: E402  (English pools of the Singapore pages)

TODAY = datetime.date(2026, 10, 23)

# site -> domain, website id, page ids of the existing pages (None = to be created)
SITES = {
    "v01": ("longfu-88.casino", 38, {"index": 49, "th": 122, "my": 123, "sg": 124, "vn": 125}),
    "v02": ("longfu88.vip", 106, {"index": 126, "vn": 127, "sg": 128, "my": 129, "th": 130}),
    "v03": ("longfu88.mobi", 108, {"index": 136, "vn": 137, "sg": 138, "my": 139, "th": 140}),
    "v04": ("longfu-888.com", 107, {"index": 131, "th": None, "my": None, "sg": None, "vn": None}),
}
# GEO run -> slug, locale, hreflang, customPageLang (as on the existing pages of these sites)
GEO = {
    "indonesia": ("index", "id", "id-ID", "id-ID"),
    "malaysia": ("my", "ms", "ms-MY", "ms"),
    "vietnam": ("vn", "vi", "vi-VN", "vi"),
    "thailand": ("th", "th", "th-TH", "th"),
    "singapore": ("sg", "en", "en-SG", "en"),
}
HREFLANG_ORDER = ["indonesia", "thailand", "malaysia", "singapore", "vietnam"]  # id-ID, th-TH, ms-MY, en-SG, vi-VN (as on the sites)

# media library: folder 45 (slots), 46 (crash), 47 (live); names as in the files
SLOTS = [("Legacy of Dead", 71), ("Big Bass Bonanza", 72), ("StarBurst", 73), ("Zeus vs Hades", 80), ("Razor Shark", 83),
         ("Gates Of Olympus 1000", 84), ("Book of Ra", 85), ("Sugar Rush", 87), ("Buffalo King Megaways", 91), ("The Dog House", 92),
         ("Dead or Alive", 93), ("888 gold", 94), ("Eye of Horus", 96), ("Sun of Egypt", 98), ("Mega Moolah", 99), ("Sweet Bonanza", 100),
         ("Maya Gold", 103), ("Wolf Gold", 106), ("3 Hot Chilli Peppers", 107), ("Book of Dead", 109), ("Joker Stoker", 227),
         ("Le Fisherman", 228), ("Wild Clusters", 229), ("Thunder Coins", 230), ("Le Bandit", 231)]
CRASH = [("JetX", 70), ("Plinko", 74), ("SpaceMan", 75), ("Reactoonz", 76), ("Aviatrix", 77), ("Aviamasters", 78), ("Ballonix", 81),
         ("Piggy Tap", 82), ("Balloon", 86), ("Big Bass Crash", 88), ("Aviator", 89), ("Penalty Shoot Out", 90), ("Chicken Road", 97),
         ("Squid Game", 101), ("Lucky Jet", 104), ("F777 Fighters", 108), ("Tower Rush", 232)]
LIVE = [("Lightning Roulette", 79), ("Ice Fishing", 102), ("Money Time", 233), ("Monopoly Live", 234), ("Sweet Bonanza Candyland", 235),
        ("Crazy Time", 2208), ("Race Track", 2625), ("Infinite Blackjack", 2626), ("Marble Race", 2627), ("American Roulette", 2628),
        ("Lightning Dragon Tiger", 2629), ("Crazy Balls", 2630)]
BONUS_IMAGES = [4654, 4657, 4656, 4655, 4652, 4653]  # the usual bonus pictures of the brand (folder Bonuses), pictures only

L = {
    "indonesia": {
        "hero_btn": ["Daftar", "Daftar Sekarang", "Gabung Sekarang"],
        "hero": ["Bonus Selamat Datang Kasino: 188% hingga €2.088 + 18 Putaran Gratis",
                 "Penawaran awal: 188% hingga €2.088 + 18 Putaran Gratis untuk deposit pertama",
                 "Mulai dengan 188% hingga €2.088 + 18 Putaran Gratis",
                 "Bonus deposit pertama: 188% hingga €2.088 + 18 Putaran Gratis"],
        "preview_title": ["Bonus Longfu88", "Promo Longfu88", "Penawaran Longfu88", "Penawaran Terkini Longfu88"],
        "preview_btn": ["Dapatkan Bonus", "Klaim Bonus", "Lihat Penawaran", "Klaim Sekarang"],
        "cta": ["Klaim Bonus", "Main Sekarang", "Daftar", "Dapatkan Bonus", "Gabung Sekarang", "Mulai Bermain", "Buka Akun", "Lihat Penawaran",
                "Coba Live Casino", "Cek Bonus"],
        "reviews_title": ["Ulasan Pemain", "Kata Para Pemain", "Ulasan dari Pemain"],
        "promo_title": "Bonus Selamat Datang Kasino", "promo_desc": "188% hingga €2.088 + 18 Putaran Gratis",
        "promo_btn": ["Klaim Bonus", "Dapatkan Bonus", "Klaim Penawaran"],
        "disclaimer": ["18+. Syarat dan ketentuan berlaku. Bermainlah dengan bijak.", "Khusus 18+. Syarat bonus berlaku. Mohon bermain dengan bijak.",
                       "18+. Berlaku syarat dan ketentuan. Bermain secara bertanggung jawab.", "Pemain harus berusia 18+. Syarat penawaran berlaku. Bermain dengan bijak."],
        "kw": "kasino, kasino online, kasino kripto, bermain, judi, slot, live casino, taruhan olahraga, daftar, login, KYC, aplikasi, pembayaran, bonus, bonus selamat datang, Indonesia, ID",
    },
    "malaysia": {
        "hero_btn": ["Daftar", "Daftar Sekarang", "Sertai Sekarang"],
        "hero": ["Bonus Alu-aluan Kasino: 188% sehingga €2,088 + 18 Putaran Percuma",
                 "Tawaran permulaan: 188% sehingga €2,088 + 18 Putaran Percuma untuk deposit pertama",
                 "Mulakan dengan 188% sehingga €2,088 + 18 Putaran Percuma",
                 "Bonus deposit pertama: 188% sehingga €2,088 + 18 Putaran Percuma"],
        "preview_title": ["Bonus Longfu88", "Promosi Longfu88", "Tawaran Longfu88", "Tawaran Terkini Longfu88"],
        "preview_btn": ["Dapatkan Bonus", "Tuntut Bonus", "Lihat Tawaran", "Tuntut Sekarang"],
        "cta": ["Tuntut Bonus", "Main Sekarang", "Daftar", "Dapatkan Bonus", "Sertai Sekarang", "Mula Bermain", "Buka Akaun", "Lihat Tawaran",
                "Cuba Kasino Langsung", "Semak Bonus"],
        "reviews_title": ["Ulasan Pemain", "Kata Para Pemain", "Ulasan daripada Pemain"],
        "promo_title": "Bonus Alu-aluan Kasino", "promo_desc": "188% sehingga €2,088 + 18 Putaran Percuma",
        "promo_btn": ["Tuntut Bonus", "Dapatkan Bonus", "Tuntut Tawaran"],
        "disclaimer": ["18+. Terma dan syarat terpakai. Bermain secara bertanggungjawab.", "Hanya 18+. Syarat bonus terpakai. Sila bermain dengan bertanggungjawab.",
                       "18+. Terma dan syarat tertakluk. Main dengan bertanggungjawab.", "Pemain mesti berumur 18+. Syarat tawaran terpakai. Bermain dengan bertanggungjawab."],
        "kw": "kasino, kasino dalam talian, kasino kripto, main, perjudian, slot, kasino langsung, pertaruhan sukan, daftar, log masuk, KYC, aplikasi, pembayaran, bonus, bonus alu-aluan, Malaysia, MY",
    },
    "vietnam": {
        "hero_btn": ["Đăng ký", "Đăng ký ngay", "Tham gia ngay"],
        "hero": ["Thưởng chào mừng casino: 188% đến €2.088 + 18 vòng quay miễn phí",
                 "Ưu đãi khởi đầu: 188% đến €2.088 + 18 vòng quay miễn phí cho lần nạp đầu",
                 "Bắt đầu với 188% đến €2.088 + 18 vòng quay miễn phí",
                 "Thưởng nạp đầu: 188% đến €2.088 + 18 vòng quay miễn phí"],
        "preview_title": ["Thưởng Longfu88", "Khuyến mãi Longfu88", "Ưu đãi Longfu88", "Ưu đãi mới của Longfu88"],
        "preview_btn": ["Nhận thưởng", "Xem ưu đãi", "Nhận ngay", "Lấy ưu đãi"],
        "cta": ["Nhận thưởng", "Chơi ngay", "Đăng ký", "Nhận ưu đãi", "Tham gia ngay", "Bắt đầu chơi", "Mở tài khoản", "Xem ưu đãi", "Thử live casino", "Xem thưởng"],
        "reviews_title": ["Đánh giá của người chơi", "Người chơi nói gì", "Nhận xét từ người chơi"],
        "promo_title": "Thưởng chào mừng casino", "promo_desc": "188% đến €2.088 + 18 vòng quay miễn phí",
        "promo_btn": ["Nhận thưởng", "Nhận ưu đãi", "Nhận ngay"],
        "disclaimer": ["18+. Áp dụng điều khoản và điều kiện. Hãy chơi có trách nhiệm.", "Chỉ dành cho người từ 18 tuổi. Áp dụng điều kiện thưởng. Hãy chơi có trách nhiệm.",
                       "18+. Điều khoản và điều kiện được áp dụng. Chơi có trách nhiệm.", "Người chơi phải từ 18 tuổi. Áp dụng điều kiện ưu đãi. Hãy chơi có trách nhiệm."],
        "kw": "casino, casino online, casino tiền mã hóa, chơi, cá cược, slot, live casino, cược thể thao, đăng ký, đăng nhập, KYC, ứng dụng, thanh toán, thưởng, thưởng chào mừng, Việt Nam, VN",
    },
    "thailand": {
        "hero_btn": ["สมัครสมาชิก", "สมัครเลย", "เข้าร่วมเลย"],
        "hero": ["โบนัสต้อนรับคาสิโน: 188% สูงสุด €2,088 + ฟรีสปิน 18 ครั้ง",
                 "ข้อเสนอเริ่มต้น: 188% สูงสุด €2,088 + ฟรีสปิน 18 ครั้ง สำหรับการฝากครั้งแรก",
                 "เริ่มต้นด้วย 188% สูงสุด €2,088 + ฟรีสปิน 18 ครั้ง",
                 "โบนัสฝากครั้งแรก: 188% สูงสุด €2,088 + ฟรีสปิน 18 ครั้ง"],
        "preview_title": ["โบนัส Longfu88", "โปรโมชัน Longfu88", "ข้อเสนอ Longfu88", "ข้อเสนอล่าสุดของ Longfu88"],
        "preview_btn": ["รับโบนัส", "ดูข้อเสนอ", "รับเลย", "ดูโบนัส"],
        "cta": ["รับโบนัส", "เล่นเลย", "สมัครสมาชิก", "ดูโบนัส", "เข้าร่วมเลย", "เริ่มเล่น", "เปิดบัญชี", "ดูข้อเสนอ", "ลองคาสิโนสด", "เช็กโบนัส"],
        "reviews_title": ["รีวิวจากผู้เล่น", "ผู้เล่นว่าอย่างไร", "ความเห็นจากผู้เล่น"],
        "promo_title": "โบนัสต้อนรับคาสิโน", "promo_desc": "188% สูงสุด €2,088 + ฟรีสปิน 18 ครั้ง",
        "promo_btn": ["รับโบนัส", "รับข้อเสนอ", "รับเลย"],
        "disclaimer": ["18+ ใช้เงื่อนไขและข้อกำหนด เล่นอย่างรับผิดชอบ", "สำหรับผู้มีอายุ 18 ปีขึ้นไป ใช้เงื่อนไขโบนัส กรุณาเล่นอย่างรับผิดชอบ",
                       "18+ เป็นไปตามข้อกำหนดและเงื่อนไข เล่นอย่างมีความรับผิดชอบ", "ผู้เล่นต้องมีอายุ 18 ปีขึ้นไป ใช้เงื่อนไขของข้อเสนอ เล่นอย่างรับผิดชอบ"],
        "kw": "คาสิโน, คาสิโนออนไลน์, คาสิโนคริปโต, เล่น, สล็อต, คาสิโนสด, แทงกีฬา, สมัครสมาชิก, เข้าสู่ระบบ, KYC, แอป, การชำระเงิน, โบนัส, โบนัสต้อนรับ, ไทย, TH",
    },
}

SEO = {  # (title <= 60, description 120-160) per run
    "longfu88-indonesia-v01": ("Longfu88 Casino Indonesia: Bonus 188% hingga €2.088", "Ulasan Longfu88 untuk pemain Indonesia: fakta utama, bonus 188% dengan 18 putaran gratis, permainan, taruhan olahraga, pembayaran, dan dukungan."),
    "longfu88-indonesia-v02": ("Longfu88 Casino: Keamanan, Syarat, dan Kontrol", "Ulasan Longfu88 untuk pemain Indonesia yang berhati-hati: operator dan lisensi, keamanan akun, verifikasi, alat judi bertanggung jawab, dan syarat bonus."),
    "longfu88-indonesia-v03": ("Ulasan Sportsbook dan Kasino Longfu88 Indonesia", "Longfu88 untuk penaruh di Indonesia: pasar taruhan olahraga, taruhan langsung, bonus olahraga, ditambah bonus selamat datang kasino dan metode pembayaran."),
    "longfu88-indonesia-v04": ("Longfu88 di Ponsel: Panduan Cepat untuk Indonesia", "Longfu88 di ponsel untuk pemain Indonesia: cara membuka situs, daftar dan masuk, bonus pertama, deposit, penarikan, permainan, dan taruhan olahraga."),
    "longfu88-malaysia-v01": ("Longfu88 Casino Malaysia: Bonus 188% hingga €2,088", "Ulasan ringkas Longfu88 untuk pemain di Malaysia: fakta utama, bonus alu-aluan 188% dengan 18 putaran percuma, permainan, buku sukan dan pembayaran."),
    "longfu88-malaysia-v02": ("Longfu88 Langkah Demi Langkah untuk Malaysia", "Panduan Longfu88 untuk pemain Malaysia: semakan pengendali, pendaftaran, deposit, tawaran alu-aluan, pilihan permainan, VIP, pengeluaran dan kawalan diri."),
    "longfu88-malaysia-v03": ("Longfu88 Casino Malaysia: Permainan dan Tawaran", "Teroka lobi Longfu88 di Malaysia: slot, kasino langsung, permainan pantas, penyedia permainan, serta tawaran alu-aluan, VIP, deposit dan pengeluaran."),
    "longfu88-malaysia-v04": ("Longfu88 Malaysia: Pembayaran dan Pengeluaran", "Aliran wang di Longfu88 untuk pemain Malaysia: kaedah deposit dan had, semakan ID sebelum pengeluaran, tawaran alu-aluan, cashback dan program VIP."),
    "longfu88-vietnam-v01": ("Đánh giá Longfu88: trò chơi và ưu đãi cho Việt Nam", "Đánh giá Longfu88 cho người chơi Việt Nam: sảnh trò chơi, nhà cung cấp, thưởng chào mừng 188% kèm 18 vòng quay miễn phí, cược thể thao và thanh toán."),
    "longfu88-vietnam-v02": ("Longfu88 Casino: Hướng dẫn đầy đủ cho Việt Nam", "Hướng dẫn đầy đủ về Longfu88 tại Việt Nam: hồ sơ nhà cái, giấy phép, đăng ký, thưởng chào mừng, chương trình VIP, trò chơi, cược thể thao và thanh toán."),
    "longfu88-vietnam-v03": ("Longfu88 Casino Việt Nam: Đánh giá nhanh", "Đánh giá nhanh Longfu88 cho người chơi Việt Nam: thông tin chính, ưu đãi nạp đầu 188% kèm 18 vòng quay, VIP, trò chơi, cược thể thao và thanh toán."),
    "longfu88-vietnam-v04": ("Longfu88: nhà cái thể thao và casino cho Việt Nam", "Longfu88 cho người cược tại Việt Nam: thị trường cược thể thao, cược trực tiếp, thưởng thể thao, cùng thưởng chào mừng casino và các phương thức thanh toán."),
    "longfu88-thailand-v01": ("คู่มือ Longfu88 casino ทีละขั้นตอนสำหรับคนไทย", "คู่มือ Longfu88 สำหรับผู้เล่นชาวไทย ตรวจสอบผู้ดำเนินการ สมัครสมาชิก ฝากเงิน รับโบนัสต้อนรับ 188% เลือกเกม ถอนเงิน และการเล่นอย่างรับผิดชอบ"),
    "longfu88-thailand-v02": ("รีวิว Longfu88 casino เกมและโปรโมชั่นสำหรับคนไทย", "รีวิว Longfu88 สำหรับผู้เล่นชาวไทย ล็อบบี้เกม ค่ายเกม โบนัสต้อนรับ 188% พร้อมฟรีสปิน 18 ครั้ง แทงกีฬา ระดับ VIP การฝากและถอนเงิน"),
    "longfu88-thailand-v03": ("Longfu88 บนมือถือ คู่มือเริ่มเล่นสำหรับคนไทย", "Longfu88 บนมือถือสำหรับผู้เล่นชาวไทย วิธีตั้งไอคอนที่หน้าจอหลัก สมัคร เข้าสู่ระบบ รับโบนัสแรก ฝากเงิน ถอนเงิน เกมและเดิมพันกีฬา"),
    "longfu88-thailand-v04": ("คู่มือฉบับสมบูรณ์ Longfu88 casino สำหรับคนไทย", "คู่มืออ้างอิง Longfu88 สำหรับผู้เล่นชาวไทย ใบอนุญาต การสมัคร ตารางโบนัส ระดับ VIP คลังเกม แทงกีฬา การชำระเงิน และฝ่ายสนับสนุนลูกค้า"),
    "longfu88-singapore-v01": ("Longfu88 Casino Singapore: Bonuses, Games, Payments", "Longfu88 reviewed for players in Singapore: quick facts, the 188% welcome bonus with 18 free spins, VIP ladder, reloads, sports betting and payment options."),
    "longfu88-singapore-v02": ("Longfu88 Singapore: Payments and Payout Review", "How money moves at Longfu88 for Singapore players: deposit methods and limits, ID checks before cash-outs, welcome offer wagering, cashback and VIP."),
    "longfu88-singapore-v03": ("Longfu88 Casino Review for Singapore: Q&A", "Balanced Longfu88 overview for Singapore: pros and cons, licence and privacy, registration steps, welcome offer, VIP, games, studios, deposits and mobile use."),
    "longfu88-singapore-v04": ("Longfu88 Singapore: Safety, Terms and Controls", "Longfu88 reviewed for careful players in Singapore: operator, licence and data handling, safe login, self-exclusion tools, welcome offer terms and VIP limits."),
}

NAMES = {
    "indonesia": {"f": ["Rina Wulandari", "Dewi Lestari", "Putri Anggraini", "Siti Rahmawati", "Ayu Kartika", "Nadia Safitri", "Intan Permata", "Maya Sari", "Lestari", "Wulan"],
                  "m": ["Budi Santoso", "Agus Pratama", "Rizky Maulana", "Dimas Saputra", "Fajar Nugroho", "Eko Prasetyo", "Reza Firmansyah", "Andi Wijaya", "Bayu", "Hendra"]},
    "malaysia": {"f": ["Aina Sofea", "Siti Hajar", "Farah Nadia", "Nur Syafiqah", "Liyana", "Mei Chen", "Kavitha", "Aisyah Zahra", "Suhana", "Hui Ying"],
                 "m": ["Hafizuddin", "Amirul", "Izzat", "Zafri", "Haikal", "Kumar", "Wei Liang", "Syazwan", "Faiz Hakimi", "Daniel Tan"]},
    "vietnam": {"f": ["Nguyễn Thị Lan", "Võ Ngọc Mai", "Đặng Thanh Hà", "Hoàng Gia Hân", "Huỳnh Thu Trang", "Ngô Khánh Linh", "Trần Mai Anh", "Lê Phương Thảo", "Phạm Bích Ngọc", "Bùi Minh Châu"],
                "m": ["Trần Minh Tuấn", "Lê Hoàng Anh", "Phạm Quốc Bảo", "Bùi Văn Khoa", "Phan Đức Long", "Đỗ Hải Nam", "Nguyễn Gia Huy", "Vũ Anh Dũng", "Lý Thanh Sơn", "Hồ Trung Kiên"]},
    "thailand": {"f": ["ปิยะพร", "พิมพ์ชนก", "อรทัย", "กมลชนก", "สุภาพร", "นภัสวรรณ", "ปวีณา", "ศิริพร", "ชลธิชา", "วรัญญา"],
                 "m": ["สมชาย", "ณัฐวุฒิ", "ธีรภัทร", "วรเมธ", "ชยพล", "อนุชา", "ภานุพงศ์", "กิตติพงษ์", "ธนากร", "ปรเมศวร์"]},
    "singapore": en.NAMES["sg"],
}
AVATARS = en.AVATARS

# topic sentences (first person or neutral, no figures, no promises) and closing sentences per language
TOPICS = ["reg", "games", "mobile", "support", "pay", "promo", "sports"]
T = {
    "indonesia": {
        "reg": ["Pendaftaran berjalan cepat, formulirnya jelas, dan saya tidak perlu menebak data apa yang harus diisi.",
                "Saya mendaftar lewat ponsel dan email konfirmasinya langsung masuk, jadi akun bisa dipakai tanpa menunggu lama.",
                "Alur membuat akun sederhana: email dan kata sandi dulu, lalu data pribadi di layar berikutnya.",
                "Konfirmasi usia dan syarat ketentuan ada di halaman daftar, jadi semuanya terlihat sejak awal.",
                "Membuat akun terasa mudah bahkan untuk pemula, dan login berikutnya berjalan tanpa kendala."],
        "games": ["Lobinya mudah dijelajahi dan saya cepat menemukan slot yang dicari lewat kategori yang rapi.",
                  "Pilihannya beragam, dari slot, meja live, sampai game instan, jadi jarang kehabisan hal baru untuk dicoba.",
                  "Bagian live casino dan crash punya menu sendiri, tidak tercampur dalam satu daftar panjang.",
                  "Pencarian berdasarkan jenis game berfungsi baik, dan studio yang terkenal mudah dikenali di lobi.",
                  "Saya lebih sering main slot, dan lobi menyusunnya dengan rapi sehingga game favorit mudah dibuka lagi."],
        "mobile": ["Saya memakai situsnya di ponsel setiap hari, dan setelah ditambahkan ke layar utama rasanya seperti aplikasi biasa.",
                   "Versi mobilnya responsif, dan kasir maupun lobi game tampil baik di layar kecil.",
                   "Bermain lewat browser ponsel terasa lancar dan saya tidak perlu mengunduh apa pun.",
                   "Tombol dan menu cukup besar untuk layar ponsel, dan area akun mudah ditemukan.",
                   "Situs berjalan baik di ponsel maupun laptop, jadi saya bisa berganti perangkat tanpa kehilangan tempat."],
        "support": ["Live chat menjawab pertanyaan saya soal verifikasi dengan sopan, dan jawabannya sesuai dengan halaman bantuan.",
                    "Tim dukungan sabar menjawab pertanyaan lanjutan dan menjelaskan langkahnya dengan jelas.",
                    "Menenangkan bahwa live chat tersedia sepanjang waktu, dan saya mendapat balasan yang membantu saat butuh.",
                    "Saya menulis ke dukungan lewat email dan menerima jawaban yang jelas serta sopan.",
                    "Agen di chat memandu saya mengunggah dokumen tanpa membuatnya terasa rumit."],
        "pay": ["Kasir menampilkan banyak metode pembayaran, dan saya bisa memilih yang biasa saya pakai tanpa repot.",
                "Deposit lewat metode lokal yang biasa saya gunakan berjalan sederhana, dan setiap langkah di kasir ditampilkan jelas.",
                "Saya suka ada pilihan transfer bank, kartu, dan kripto, karena saya berganti-ganti sesuai kebutuhan.",
                "Halaman pembayarannya tidak menyembunyikan apa pun, dan saya bisa melihat metode yang tersedia sebelum memilih.",
                "Proses penarikan mengikuti langkah yang sama jelasnya dengan deposit, dan kasir menjelaskan tiap layar."],
        "promo": ["Halaman promosi mudah ditemukan, dan setiap penawaran menunjukkan syarat sebelum saya mengaktifkannya.",
                  "Saya suka membuka bagian hadiah setelah login karena semua penawaran terkumpul di satu tempat.",
                  "Syarat bonus ditulis dengan jelas, jadi saya tahu apa yang diharapkan sebelum ikut.",
                  "Program VIP dijelaskan dengan baik, dan mudah melihat cara kerja levelnya.",
                  "Cashback dan reload ditampilkan berdampingan, sehingga mudah dibandingkan."],
        "sports": ["Sportsbook-nya memuat olahraga yang saya ikuti, dan berpindah antara pasar pra-pertandingan dan live terasa mudah.",
                   "Saya suka bertaruh sepak bola di sini, dan jenis taruhan tersusun jelas di kupon.",
                   "Taruhan langsung berjalan lancar di ponsel, dan pasar diperbarui tanpa jeda yang terasa.",
                   "Satu akun untuk sportsbook dan kasino menghemat saya dari mengurus dua login.",
                   "Berpindah dari kasino ke sportsbook cukup satu ketukan, cocok dengan cara saya bermain."],
        "close": ["Secara keseluruhan situsnya rapi dan mudah dipakai.", "Tidak terlalu ramai, dan fungsinya sesuai yang saya butuhkan.",
                  "Untuk sekarang saya akan tetap memakainya.", "Pilihan yang pas bagi yang suka tampilan bersih.",
                  "Tidak mewah, tapi bekerja seperti yang dijelaskan.", "Layak dicoba bagi yang penasaran.",
                  "Pengalamannya terasa tertata dengan baik.", "Setelah beberapa saat, mudah sekali menemukan semua yang dibutuhkan."],
    },
    "malaysia": {
        "reg": ["Pendaftaran cepat, borangnya jelas, dan saya tidak perlu meneka maklumat apa yang diperlukan.",
                "Saya mendaftar melalui telefon dan e-mel pengesahan tiba serta-merta, jadi akaun boleh digunakan tanpa menunggu lama.",
                "Cara membuka akaun mudah: e-mel dan kata laluan dahulu, kemudian butiran peribadi pada skrin seterusnya.",
                "Pengesahan umur dan terma ada di halaman pendaftaran, jadi semuanya jelas dari awal.",
                "Membuat akaun terasa mudah walaupun untuk orang baharu, dan log masuk selepas itu berjalan lancar."],
        "games": ["Lobinya mudah dijelajah dan saya cepat menjumpai slot yang dicari melalui kategori yang kemas.",
                  "Pilihannya pelbagai, daripada slot, meja langsung hingga permainan pantas, jadi jarang kehabisan sesuatu yang baharu.",
                  "Bahagian kasino langsung dan crash mempunyai menu sendiri, tidak bercampur dalam satu senarai panjang.",
                  "Carian mengikut jenis permainan berfungsi baik, dan studio terkenal mudah dikenali dalam lobi.",
                  "Saya lebih kerap bermain slot, dan lobi menyusunnya dengan kemas supaya permainan kegemaran mudah dibuka semula."],
        "mobile": ["Saya menggunakan laman ini di telefon setiap hari, dan selepas ditambah ke skrin utama ia terasa seperti aplikasi biasa.",
                   "Versi mudah alihnya responsif, dan kaunter bayaran serta lobi permainan dipaparkan dengan baik pada skrin kecil.",
                   "Bermain melalui pelayar telefon terasa lancar dan saya tidak perlu memuat turun apa-apa.",
                   "Butang dan menu cukup besar untuk telefon, dan ruang akaun mudah dijumpai.",
                   "Laman ini berjalan baik pada telefon dan komputer riba, jadi saya boleh bertukar peranti tanpa kehilangan tempat."],
        "support": ["Sembang langsung menjawab soalan saya tentang pengesahan dengan sopan, dan jawapannya sama seperti halaman bantuan.",
                    "Pasukan sokongan bersabar menjawab soalan susulan dan menerangkan langkah dengan jelas.",
                    "Menenangkan apabila sembang langsung tersedia sepanjang masa, dan saya mendapat balasan yang berguna ketika perlu.",
                    "Saya menulis kepada sokongan melalui e-mel dan menerima jawapan yang jelas serta sopan.",
                    "Ejen dalam sembang membimbing saya memuat naik dokumen tanpa menjadikannya rumit."],
        "pay": ["Kaunter bayaran menyenaraikan banyak kaedah, dan saya boleh memilih yang biasa digunakan tanpa bersusah payah.",
                "Deposit melalui kaedah tempatan yang biasa saya guna berjalan mudah, dan setiap langkah dipaparkan dengan jelas.",
                "Saya suka ada pilihan perbankan, kad dan kripto, kerana saya bertukar mengikut keperluan.",
                "Halaman pembayaran tidak menyembunyikan apa-apa, dan saya dapat melihat kaedah yang tersedia sebelum memilih.",
                "Proses pengeluaran mengikut langkah yang sama jelasnya seperti deposit, dan setiap skrin diterangkan."],
        "promo": ["Halaman promosi mudah dijumpai, dan setiap tawaran menunjukkan syarat sebelum saya mengaktifkannya.",
                  "Saya suka membuka bahagian ganjaran selepas log masuk kerana semua tawaran dikumpulkan di satu tempat.",
                  "Syarat bonus ditulis dengan jelas, jadi saya tahu apa yang dijangka sebelum menyertai.",
                  "Program VIP diterangkan dengan baik, dan mudah melihat cara tahapnya berfungsi.",
                  "Cashback dan tawaran muat semula disenaraikan bersama, jadi mudah dibandingkan."],
        "sports": ["Buku sukan ada sukan yang saya ikuti, dan bertukar antara pasaran pra-perlawanan dan langsung terasa mudah.",
                   "Saya suka bertaruh bola sepak di sini, dan jenis pertaruhan tersusun jelas pada slip.",
                   "Pertaruhan langsung berjalan lancar di telefon, dan pasaran dikemas kini tanpa kelewatan yang ketara.",
                   "Satu akaun untuk buku sukan dan kasino menjimatkan saya daripada menguruskan dua log masuk.",
                   "Bertukar daripada kasino ke buku sukan hanya perlu satu ketikan, sesuai dengan cara saya bermain."],
        "close": ["Secara keseluruhan laman ini kemas dan mudah digunakan.", "Tidak terlalu sesak, dan berfungsi seperti yang saya perlukan.",
                  "Buat masa ini saya akan terus menggunakannya.", "Pilihan sesuai untuk yang suka reka letak bersih.",
                  "Tidak mewah, tetapi berfungsi seperti yang diterangkan.", "Berbaloi dicuba oleh yang ingin tahu.",
                  "Pengalamannya terasa tersusun dengan baik.", "Selepas seketika, senang untuk mencari semua yang diperlukan."],
    },
    "vietnam": {
        "reg": ["Đăng ký diễn ra nhanh, biểu mẫu rõ ràng và tôi không phải đoán cần điền thông tin gì.",
                "Tôi đăng ký bằng điện thoại và email xác nhận đến ngay, nên tài khoản dùng được mà không phải chờ lâu.",
                "Quy trình tạo tài khoản đơn giản: email và mật khẩu trước, rồi đến thông tin cá nhân ở màn hình tiếp theo.",
                "Phần xác nhận độ tuổi và điều khoản nằm ngay trên trang đăng ký, nên mọi thứ đều rõ từ đầu.",
                "Tạo tài khoản khá dễ, ngay cả với người mới, và những lần đăng nhập sau đó không gặp trục trặc."],
        "games": ["Sảnh game dễ duyệt và tôi nhanh chóng tìm được slot mình cần nhờ các danh mục gọn gàng.",
                  "Lựa chọn khá đa dạng, từ slot, bàn live đến game nhanh, nên hiếm khi hết thứ mới để thử.",
                  "Phần live casino và crash có menu riêng, không bị lẫn trong một danh sách dài.",
                  "Tìm theo loại game hoạt động tốt, và các studio quen thuộc dễ nhận ra trong sảnh.",
                  "Tôi chủ yếu chơi slot, và sảnh sắp xếp gọn nên tôi dễ mở lại những game yêu thích."],
        "mobile": ["Tôi dùng trang trên điện thoại mỗi ngày, và sau khi thêm vào màn hình chính nó giống như một ứng dụng thông thường.",
                   "Phiên bản di động phản hồi tốt, cả quầy thanh toán lẫn sảnh game đều hiển thị ổn trên màn hình nhỏ.",
                   "Chơi bằng trình duyệt điện thoại khá mượt và tôi không cần tải thêm gì.",
                   "Nút và menu đủ lớn cho điện thoại, và khu vực tài khoản dễ tìm.",
                   "Trang chạy tốt trên cả điện thoại lẫn laptop, nên tôi đổi thiết bị mà không mất vị trí đang dùng."],
        "support": ["Live chat trả lời câu hỏi về xác minh một cách lịch sự, và câu trả lời khớp với trang trợ giúp.",
                    "Đội hỗ trợ kiên nhẫn với câu hỏi tiếp theo và giải thích các bước rõ ràng.",
                    "Thật yên tâm khi live chat luôn có mặt, và tôi nhận được phản hồi hữu ích khi cần.",
                    "Tôi viết email cho bộ phận hỗ trợ và nhận được câu trả lời rõ ràng, lịch sự.",
                    "Nhân viên trong chat hướng dẫn tôi tải tài liệu lên mà không làm mọi thứ phức tạp."],
        "pay": ["Quầy thanh toán liệt kê nhiều phương thức, và tôi chọn được cách mình hay dùng mà không mất công tìm.",
                "Nạp tiền bằng phương thức nội địa quen thuộc diễn ra đơn giản, và từng bước ở quầy thanh toán đều rõ.",
                "Tôi thích có lựa chọn ngân hàng, thẻ và tiền mã hóa, vì tôi đổi qua lại tùy lúc.",
                "Trang thanh toán không giấu điều gì, và tôi thấy được các phương thức hiện có trước khi chọn.",
                "Việc rút tiền theo các bước rõ ràng như khi nạp, và mỗi màn hình đều có giải thích."],
        "promo": ["Trang khuyến mãi dễ tìm, và mỗi ưu đãi ghi rõ điều kiện trước khi tôi kích hoạt.",
                  "Tôi hay vào mục phần thưởng sau khi đăng nhập vì mọi ưu đãi được gom ở một chỗ.",
                  "Điều kiện thưởng được viết rõ ràng, nên tôi biết trước mình cần làm gì khi tham gia.",
                  "Chương trình VIP được giải thích tốt, và dễ thấy các cấp độ vận hành ra sao.",
                  "Hoàn tiền và thưởng nạp lại được xếp cạnh nhau nên dễ so sánh."],
        "sports": ["Mục cược thể thao có các môn tôi theo dõi, và chuyển giữa kèo trước trận với kèo trực tiếp rất dễ.",
                   "Tôi thích cược bóng đá ở đây, và các loại cược được trình bày rõ trên phiếu cược.",
                   "Cược trực tiếp chạy mượt trên điện thoại, và tỷ lệ cập nhật không có độ trễ mà tôi nhận thấy.",
                   "Một tài khoản cho cả cược thể thao và casino giúp tôi khỏi phải quản lý hai lần đăng nhập.",
                   "Chuyển từ casino sang cược thể thao chỉ cần một lần chạm, hợp với cách tôi chơi."],
        "close": ["Nhìn chung đây là trang gọn gàng và dễ dùng.", "Không rườm rà và đúng với những gì tôi cần.",
                  "Hiện tại tôi sẽ tiếp tục dùng.", "Lựa chọn hợp cho ai thích giao diện sạch.",
                  "Không hào nhoáng, nhưng hoạt động đúng như mô tả.", "Đáng để xem qua với ai đang tò mò.",
                  "Trải nghiệm tổng thể được sắp xếp khá tốt.", "Sau một lúc là dễ tìm thấy mọi thứ cần dùng."],
    },
    "thailand": {
        "reg": ["การสมัครสมาชิกทำได้รวดเร็ว แบบฟอร์มชัดเจน และไม่ต้องเดาว่าต้องกรอกข้อมูลอะไร",
                "สมัครผ่านโทรศัพท์ได้เลย อีเมลยืนยันมาถึงทันที จึงเริ่มใช้งานบัญชีได้โดยไม่ต้องรอนาน",
                "ขั้นตอนสร้างบัญชีไม่ซับซ้อน เริ่มจากอีเมลและรหัสผ่าน แล้วจึงกรอกข้อมูลส่วนตัวในหน้าถัดไป",
                "การยืนยันอายุและข้อกำหนดอยู่ในหน้าสมัครเลย จึงเห็นทุกอย่างตั้งแต่ต้น",
                "การสร้างบัญชีง่ายแม้สำหรับมือใหม่ และการเข้าสู่ระบบครั้งต่อมาก็ไม่มีปัญหา"],
        "games": ["ล็อบบี้เกมเรียกดูง่าย หาสล็อตที่ต้องการได้เร็วจากหมวดหมู่ที่จัดไว้เป็นระเบียบ",
                  "มีเกมให้เลือกหลากหลาย ทั้งสล็อต โต๊ะสด และเกมด่วน จึงมีของใหม่ให้ลองอยู่เสมอ",
                  "ส่วนคาสิโนสดและเกมแครชมีเมนูแยกของตัวเอง ไม่ปะปนอยู่ในรายการยาวรายการเดียว",
                  "ค้นหาตามประเภทเกมได้ดี และเห็นค่ายเกมที่คุ้นเคยได้ง่ายในล็อบบี้",
                  "เล่นสล็อตเป็นหลัก ล็อบบี้จัดหมวดไว้เรียบร้อย เปิดเกมโปรดกลับมาเล่นได้สะดวก"],
        "mobile": ["ใช้งานเว็บบนมือถือทุกวัน และหลังเพิ่มไว้ที่หน้าจอหลักก็ให้ความรู้สึกเหมือนแอปทั่วไป",
                   "เวอร์ชันมือถือปรับตามหน้าจอได้ดี ทั้งส่วนการเงินและล็อบบี้เกมแสดงผลได้ดีบนจอเล็ก",
                   "เล่นผ่านเบราว์เซอร์บนมือถือได้ลื่นไหล ไม่ต้องดาวน์โหลดอะไรเพิ่ม",
                   "ปุ่มและเมนูมีขนาดพอเหมาะกับมือถือ และหาส่วนบัญชีได้ง่าย",
                   "เว็บทำงานได้ดีทั้งบนมือถือและแล็ปท็อป สลับอุปกรณ์ได้โดยไม่เสียตำแหน่งที่ใช้อยู่"],
        "support": ["แชทสดตอบคำถามเรื่องการยืนยันตัวตนอย่างสุภาพ และคำตอบตรงกับหน้าช่วยเหลือ",
                    "ทีมสนับสนุนใจเย็นกับคำถามต่อเนื่องและอธิบายขั้นตอนได้ชัดเจน",
                    "อุ่นใจที่มีแชทสดตลอดเวลา และได้รับคำตอบที่เป็นประโยชน์เมื่อต้องการ",
                    "เขียนอีเมลถึงฝ่ายสนับสนุนแล้วได้รับคำตอบที่ชัดเจนและสุภาพ",
                    "เจ้าหน้าที่ในแชทแนะนำการอัปโหลดเอกสารโดยไม่ทำให้รู้สึกยุ่งยาก"],
        "pay": ["หน้าการเงินแสดงช่องทางชำระเงินไว้หลากหลาย เลือกแบบที่ใช้ประจำได้โดยไม่ต้องค้นหา",
                "ฝากเงินด้วยช่องทางในประเทศที่คุ้นเคยทำได้ง่าย และแต่ละขั้นตอนแสดงไว้ชัดเจน",
                "ชอบที่มีทั้งธนาคาร บัตร และคริปโตให้เลือก เพราะเปลี่ยนใช้ตามสะดวกในแต่ละช่วง",
                "หน้าชำระเงินไม่ซ่อนอะไร เห็นช่องทางที่มีให้ใช้ก่อนเลือก",
                "การถอนเงินมีขั้นตอนชัดเจนเหมือนตอนฝาก และทุกหน้าจอมีคำอธิบายประกอบ"],
        "promo": ["หน้าโปรโมชันหาง่าย และแต่ละข้อเสนอระบุเงื่อนไขไว้ก่อนกดรับ",
                  "ชอบเปิดดูส่วนรางวัลหลังเข้าสู่ระบบ เพราะข้อเสนอทั้งหมดรวมอยู่ในที่เดียว",
                  "เงื่อนไขโบนัสเขียนไว้ชัดเจน จึงรู้ล่วงหน้าว่าต้องทำอะไรบ้างก่อนเข้าร่วม",
                  "โปรแกรม VIP อธิบายได้ดี และเห็นได้ง่ายว่าแต่ละระดับทำงานอย่างไร",
                  "แคชแบ็กและโบนัสเติมเงินแสดงอยู่ด้วยกัน จึงเปรียบเทียบได้ง่าย"],
        "sports": ["ส่วนแทงกีฬามีกีฬาที่ติดตามอยู่ และสลับระหว่างราคาก่อนแข่งกับราคาสดได้สะดวก",
                   "ชอบแทงฟุตบอลที่นี่ ประเภทการแทงจัดวางชัดเจนในสลิป",
                   "การแทงสดทำงานลื่นบนมือถือ และราคาอัปเดตโดยไม่มีหน่วงที่สังเกตได้",
                   "บัญชีเดียวใช้ได้ทั้งแทงกีฬาและคาสิโน ไม่ต้องจัดการสองล็อกอิน",
                   "สลับจากคาสิโนไปแทงกีฬาได้ในแตะเดียว เข้ากับรูปแบบการเล่นของตัวเอง"],
        "close": ["โดยรวมเป็นเว็บที่เรียบร้อยและใช้งานง่าย", "ไม่รก และทำงานตรงตามที่ต้องการ",
                  "ตอนนี้ตั้งใจจะใช้ต่อไป", "เป็นตัวเลือกที่ดีสำหรับคนชอบหน้าตาสะอาด",
                  "ไม่หวือหวา แต่ทำงานตรงตามที่อธิบาย", "น่าลองดูสำหรับคนที่สนใจ",
                  "ประสบการณ์โดยรวมจัดระเบียบได้ดี", "ใช้ไปสักพักก็หาทุกอย่างที่ต้องการได้ง่าย"],
    },
    "singapore": {**{k: en.A[k] for k in TOPICS}, "close": en.B},
}


def hreflang_html(domain: str) -> str:
    out = []
    for g in HREFLANG_ORDER:
        slug, _, code, _ = GEO[g]
        out.append(f'<link rel="alternate" hreflang="{code}" href="https://{domain}/{"" if slug == "index" else slug}" />')
    return "\r\n".join(out)


def pick(rnd, pool, n):
    pool = [x for x in pool]
    rnd.shuffle(pool)
    return pool[:n]


def reviews_for(geo: str, seed: str, used: dict) -> list[dict]:
    rnd = random.Random(seed)
    n = rnd.choice([5, 6])
    topics = rnd.sample(TOPICS, n)
    names = {g: rnd.sample(NAMES[geo][g], len(NAMES[geo][g])) for g in "fm"}
    avs = {g: rnd.sample(AVATARS[g], len(AVATARS[g])) for g in "fm"}
    items = []
    for i, t in enumerate(topics):
        g = "f" if i % 2 == 0 else "m"
        if rnd.random() < 0.3:
            g = "m" if g == "f" else "f"
        pool = T[geo][t]
        free = [k for k in range(len(pool)) if used.get((geo, t, k), 0) < 1] or list(range(len(pool)))
        k = rnd.choice(free)
        used[(geo, t, k)] = used.get((geo, t, k), 0) + 1
        sep = "" if geo == "thailand" else " "
        text = pool[k] + (" " if geo == "thailand" else sep) + rnd.choice(T[geo]["close"])
        date = TODAY - datetime.timedelta(days=rnd.randint(0, 9))
        items.append({"username": names[g].pop(), "review": text, "date": date.isoformat(), "avatar": avs[g].pop(), "rating": rnd.choice([5, 5, 4])})
    items.sort(key=lambda r: r["date"], reverse=True)
    return items


def config(run: str, geo: str, vid: str, used: dict) -> dict:
    domain, site, pages = SITES[vid]
    slug, locale, code, lang = GEO[geo]
    rnd = random.Random("cfg2-" + run)
    n = int(vid[1:])
    cfg = L.get(geo)
    if geo == "singapore":
        cfg = {"hero_btn": ["Register", "Sign Up", "Join Now"], "hero": en.HERO_LABEL, "preview_title": en.PREVIEW_TITLE, "preview_btn": en.BUTTONS,
               "cta": en.CTA_POOL, "reviews_title": ["Real Player Reviews", "What Players Say", "Player Reviews"],
               "promo_title": "Casino Welcome Bonus", "promo_desc": "188% up to €2,088 + 18 Free Spins", "promo_btn": ["Claim Bonus", "Get Bonus", "Claim Offer"],
               "disclaimer": en.DISCLAIMER, "kw": en.KEYWORDS_ADD["sg"]}
    title, desc = SEO[run]
    imgs = BONUS_IMAGES[n % 6:] + BONUS_IMAGES[: n % 6]
    swipers = {"slots": sorted(pick(rnd, SLOTS, 12), key=lambda x: x[0].lower()), "crash": sorted(pick(rnd, CRASH, 12), key=lambda x: x[0].lower()),
               "live": sorted(LIVE, key=lambda x: x[0].lower())}
    return {
        "website_id": site, "domain": domain, "page_id": pages[slug], "slug": slug, "locale": locale,
        "seo": {"title": title, "description": desc, "customCanonical": f'https://{domain}/{"" if slug == "index" else slug}', "customPageLang": lang},
        "customHeadHTML": hreflang_html(domain),
        "keywords": {"main": "Longfu88", "additional": cfg["kw"]},
        "hero": {"label": cfg["hero"][n % len(cfg["hero"])], "mainLabel": "", "background": 140, "button": rnd.choice(cfg["hero_btn"])},
        "swipers": swipers,
        "preview": {"title": cfg["preview_title"][n % len(cfg["preview_title"])],
                    "items": [{"image": i, "button": cfg["preview_btn"][(n + k) % len(cfg["preview_btn"])]} for k, i in enumerate(imgs)]},
        "reviews": {"title": rnd.choice(cfg["reviews_title"]), "items": reviews_for(geo, "rev2-" + run, used)},
        "promo": {"title": cfg["promo_title"], "description": cfg["promo_desc"], "disclaimer": cfg["disclaimer"][n % len(cfg["disclaimer"])],
                  "button": rnd.choice(cfg["promo_btn"])},
        "cta_texts": rnd.sample(cfg["cta"], 5),
    }


def main() -> None:
    want = set(sys.argv[1:])
    used: dict = {}
    for geo in GEO:
        for vid in SITES:
            run = f"longfu88-{geo}-{vid}"
            cfg = config(run, geo, vid, used)
            if want and run not in want:
                continue
            bad = []
            if len(cfg["seo"]["title"]) > 60:
                bad.append(f'title {len(cfg["seo"]["title"])}')
            if not 120 <= len(cfg["seo"]["description"]) <= 160:
                bad.append(f'description {len(cfg["seo"]["description"])}')
            (ROOT / "runs" / run / "05_affbulk_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
            print(run, cfg["seo"]["customCanonical"], cfg["page_id"], "OK" if not bad else "CHECK " + ", ".join(bad))


if __name__ == "__main__":
    main()
