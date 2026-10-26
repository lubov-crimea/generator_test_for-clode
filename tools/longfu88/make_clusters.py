"""Manual step 1.2 for the Longfu88 GEO runs: answers llm/heading_clusters.request.md with rule-based clusters.

    python tools/longfu88/make_clusters.py <run> [<run> ...]

Competitor headings are grouped by topic with multilingual keyword rules (English, Indonesian, Malay, Vietnamese, Thai). The topics are
the ones the base brief covers (tools/longfu88/make_base.py); a heading that matches no rule becomes a cluster of its own (it can never
be mandatory, because only clusters met on at least two pages are).
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[2]

# (topic, title, regex) - the first matching rule wins
RULES = [
    ("FAQ", "Frequently Asked Questions", r"\bfaq|frequently asked|pertanyaan|soalan|câu hỏi|cau hoi|คำถาม"),
    ("Pros and cons", "Pros and Cons", r"\bpros\b|\bcons\b|strength|kelebihan|kekurangan|ưu điểm|nhược điểm|ข้อดี|ข้อเสีย|what works"),
    ("Verdict and conclusion", "Verdict", r"verdict|conclusion|summary|should you|kesimpulan|ringkasan|kết luận|tổng kết|สรุป"),
    ("Responsible gambling", "Responsible Gambling", r"responsible|bertanggungjawab|bertanggung jawab|có trách nhiệm|รับผิดชอบ"),
    ("VIP programme and loyalty", "VIP Programme", r"\bvip\b|loyalty|reward|kesetiaan|thành viên|ระดับ|สมาชิก"),
    ("Cryptocurrency payments", "Crypto Payments", r"crypto|kripto|bitcoin|usdt|tiền điện tử|tiền ảo|คริปโต"),
    ("Withdrawals and payout speed", "Withdrawals", r"(?<!and )withdraw(?!.*deposit)|payout|penarikan|pengeluaran|rút tiền|ถอนเงิน|ถอน(?!.*ฝาก)"),
    ("Deposit methods and payments", "Payment Methods", r"deposit|payment|banking|cashier|pembayaran|setor|bayar|nạp|thanh toán|ฝาก|ชำระ|การเงิน|transaction"),
    ("Ongoing promotions and tournaments", "Ongoing Promotions", r"cashback|rebate|reload|tournament|turnamen|weekly|giải đấu|hoàn tiền|ทัวร์นาเมนต์|คืนยอด|missions|challenge"),
    ("Bonuses and welcome offers", "Bonuses and Welcome Offers", r"bonus|promo|offer|welcome|khuyến mãi|ưu đãi|โบนัส|โปรโมชั่น|selamat datang"),
    ("Registration and login", "Registration and Login", r"regist|sign[- ]?up|log[- ]?in|daftar|masuk|đăng ký|đăng nhập|สมัคร|เข้าสู่ระบบ|steps to"),
    ("Licence, security and fair play", "Safety and Fair Play", r"licen|secur|safe|fair|trust|kyc|verif|aman|keamanan|keselamatan|lesen|giấy phép|an toàn|bảo mật|xác minh|ใบอนุญาต|ปลอดภัย|ยืนยัน"),
    ("Mobile access and app", "Mobile Access", r"mobile|\bapp\b|aplikasi|ios|android|ứng dụng|แอป|มือถือ"),
    ("Customer support", "Customer Support", r"support|customer service|help|dukungan|sokongan|layanan pelanggan|hỗ trợ|chăm sóc|ลูกค้า|ติดต่อ|live chat"),
    ("Software providers", "Game Providers", r"provider|software|studio|penyedia|nhà cung cấp|ผู้ให้บริการ"),
    ("Lottery", "Lottery", r"lotter|togel|lotto|xổ số|หวย"),
    ("Fishing, P2P, fast and free games", "Instant and Specialty Games", r"fishing|p2p|crash|instant|fast game|free game|arcade|bắn cá|ยิงปลา|tembak ikan"),
    ("Slots", "Slots", r"slot|สล็อต|nổ hũ|jackpot"),
    ("Live casino", "Live Casino", r"live (dealer|casino|game)|casino langsung|trực tiếp|ไลฟ์|สด"),
    ("Table games and video poker", "Table Games", r"table|baccarat|roulette|blackjack|poker|sic bo|meja|bàn|บาคาร่า|รูเล็ต"),
    ("Sports betting and esports", "Sports Betting", r"sport|esport|e-sport|odds|betting|taruhan|cá cược|thể thao|กีฬา|เดิมพัน|sbobet|saba"),
    ("Games overview", "Games Overview", r"game|permainan|trò chơi|เกม|lobby|casino games"),
    ("Platform overview / about the casino", "About the Casino", r"about|overview|platform|introduction|tentang|giới thiệu|เกี่ยวกับ|tổng quan|ภาพรวม|usability|navigation|design"),
]


def classify(text: str):
    t = text.lower()
    for topic, title, rx in RULES:
        if re.search(rx, t):
            return topic, title
    return None


def main() -> None:
    for run in sys.argv[1:]:
        req = (ROOT / "runs" / run / "llm" / "heading_clusters.request.md").read_text(encoding="utf-8")
        rows = re.findall(r"^(c\d+h\d+) \| H\d \| (.*)$", req, re.MULTILINE)
        groups: dict[str, dict] = {}
        singles = []
        for hid, text in rows:
            hit = classify(text)
            if hit:
                g = groups.setdefault(hit[0], {"topic": hit[0], "canonical_title": hit[1], "member_ids": []})
                g["member_ids"].append(hid)
            else:
                singles.append({"topic": "Other: " + text[:60], "canonical_title": text[:60], "member_ids": [hid]})
        clusters = list(groups.values()) + singles
        used = [i for c in clusters for i in c["member_ids"]]
        assert sorted(used) == sorted(h for h, _ in rows), run
        (ROOT / "runs" / run / "llm" / "heading_clusters.json").write_text(json.dumps({"clusters": clusters}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(run, len(rows), "headings ->", len(groups), "topics +", len(singles), "single")


if __name__ == "__main__":
    main()
