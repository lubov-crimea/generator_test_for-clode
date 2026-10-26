"""Manual step 1.2 for the Longfu88 SG bonuses page: answers runs/longfu88-bonus-sg/llm/heading_clusters.json with bonus-specific clusters
(the generic rules of make_clusters.py put every bonus heading into one cluster). Run from the project root:
    python tools/longfu88/make_bonus_sg_clusters.py
Competitor index: c0 tips.gg, c1 tribuna.com, c2 longfu88-sg.com/bonus, c3 longfu88-play.my/bonuses."""
import json
from pathlib import Path

CL = [
    ("Overview of the bonus types and the casino", "Bonus Overview", ["c0h3", "c1h1", "c1h2", "c1h3", "c1h4", "c1h5", "c1h6", "c3h1", "c3h2", "c3h13"]),
    ("Welcome bonus: size, eligibility, key details", "Welcome Bonus", ["c0h4", "c0h5", "c2h4", "c3h3"]),
    ("How to claim the bonus step by step", "How to Claim the Welcome Bonus", ["c0h2", "c0h11", "c3h4"]),
    ("Wagering requirements and bonus terms", "Wagering and Bonus Terms", ["c0h8", "c1h7", "c1h8", "c3h5", "c3h12"]),
    ("Reload bonuses and recurring weekly or weekend offers", "Reload Bonuses", ["c0h7", "c2h5", "c2h6", "c2h7", "c3h8"]),
    ("Cashback offers", "Cashback Offers", ["c2h8", "c3h11"]),
    ("Free spins offers", "Free Spins", ["c3h9"]),
    ("Promo codes and bonus codes", "Promo Codes", ["c0h1", "c0h6", "c0h16", "c0h22"]),
    ("Rewards area: Bonus Crab", "Bonus Crab", ["c2h1", "c2h2", "c2h3", "c2h10", "c2h11", "c2h12", "c2h13", "c2h14"]),
    ("VIP program and loyalty rewards", "VIP Program and Loyalty", ["c3h6", "c3h7"]),
    ("Sports betting bonuses", "Sports Betting Bonuses", ["c3h10"]),
    ("Payment methods and bonus compatibility", "Payment Methods and Bonuses", ["c3h14"]),
    ("Bonuses on mobile", "Mobile Bonus Access", ["c3h15"]),
    ("Comparison with other casinos and advantages", "Bonus Comparison", ["c0h12", "c0h13"]),
    ("Bonus offers by country and legality", "Bonus Availability by Country", ["c0h9", "c0h23"]),
    ("Referral bonus", "Referral Bonus", ["c0h10"]),
    ("Withdrawal of bonus winnings", "Withdrawing Bonus Winnings", ["c0h18"]),
    ("Expiry of bonuses and eligibility of players", "Bonus Expiry and Eligibility", ["c0h17", "c0h20"]),
    ("Customer reviews", "Customer Reviews", ["c0h21"]),
    ("Frequently asked questions about bonuses", "Bonus FAQ", ["c0h15", "c0h19", "c0h24", "c2h9", "c3h17"]),
    ("Verdict and strategy on whether to take the bonuses", "Getting the Most from Bonuses", ["c0h14", "c3h16", "c3h18"]),
]
out = {"clusters": [{"topic": t, "canonical_title": c, "member_ids": m} for t, c, m in CL]}
ids = [i for _, _, m in CL for i in m]
assert len(ids) == len(set(ids)), "duplicate ids"
Path("runs/longfu88-bonus-sg/llm/heading_clusters.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(CL), "clusters,", len(ids), "headings")
