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

c0h1 | H2 | Popular Casino Games
c0h2 | H2 | New Slots to Play
c0h3 | H2 | Lizaro Casino: Key Information for UK Players
c0h4 | H2 | How to Register a New Account at Lizaro Casino?
c0h5 | H3 | Lizaro Casino License, Regulation and Legality in the UK
c0h6 | H2 | Lizaro Mobile Casino: Play on Your Smartphone or Tablet
c0h7 | H3 | Lizaro Casino App for Android and iOS
c0h8 | H2 | Why Players from the UK Choose Lizaro Casino?
c0h9 | H2 | Casino Games at Lizaro: Slots, Table Games and Live Casino
c0h10 | H3 | Slot Games
c0h11 | H3 | Live Dealer Casino
c0h12 | H3 | Classic Table Games
c0h13 | H3 | Progressive Jackpot Games
c0h14 | H3 | Instant Games
c0h15 | H3 | Video Poker
c0h16 | H3 | Virtual Sports
c0h17 | H2 | Top Game Providers Available at Lizaro
c0h18 | H2 | Lizaro Bonuses and Promotions for UK Players
c0h19 | H3 | Welcome Offer
c0h20 | H3 | Reload Promotions
c0h21 | H3 | Free Spins Offers
c0h22 | H3 | Cashback Promotions
c0h23 | H3 | Lizaro Loyalty and VIP Rewards
c0h24 | H2 | Deposits and Withdrawals Available at Lizaro for UK Players
c0h25 | H2 | Responsible Gambling and Player Protection at Lizaro Online Casino
c0h26 | H2 | Lizaro Casino Customer Support and Help Centre
c0h27 | H2 | Lizaro Casino Reviews from UK Players
c0h28 | H2 | Frequently Asked Questions
c1h1 | H2 | Overview of Lizaro Casino
c1h2 | H3 | Pros
c1h3 | H3 | Cons
c1h4 | H2 | Lizaro Casino Bonuses and Promotions
c1h5 | H3 | Welcome Bonus
c1h6 | H3 | Weekly Reload Bonuses
c1h7 | H3 | Free Spins
c1h8 | H3 | Live Cashback Bonus
c1h9 | H2 | VIP Program
c1h10 | H3 | VIP Cashback Bonus
c1h11 | H2 | Game Selection and Software
c1h12 | H3 | Slot Games
c1h13 | H3 | Table Games
c1h14 | H3 | Live Dealer Games
c1h15 | H3 | Instant Games
c1h16 | H2 | Payment Methods for Canadians
c1h17 | H3 | Deposits at Lizaro Casino
c1h18 | H3 | Withdrawals at Lizaro Casino
c1h19 | H2 | App and Mobile at Lizaro Casino
c1h20 | H2 | User Experience at Lizaro Casino
c1h21 | H2 | Security and Fair Play at Lizaro Casino
c1h22 | H2 | Customer Support
c1h23 | H2 | Our Verdict of Lizaro Casino
c1h24 | H2 | Lizaro Casino FAQs
c1h25 | H3 | What is the welcome bonus at Lizaro Casino?
c1h26 | H3 | Is Lizaro Casino available on mobile?
c1h27 | H3 | Is Lizaro Casino licensed?
c1h28 | H3 | What payment methods can Canadians use?
c1h29 | H3 | Does Lizaro Casino offer live dealer games?
c1h30 | H3 | Does Lizaro Casino have a VIP program?
c2h1 | H2 | What Is Our Expert Opinion on Lizaro?
c2h2 | H2 | Who Is Lizaro?
c2h3 | H3 | Key info about Lizaro
c2h4 | H2 | Is Lizaro safe and legit?
c2h5 | H2 | Lizaro Sportsbook Review
c2h6 | H3 | How does pre-match wagering work at Lizaro?
c2h7 | H2 | Top Sports
c2h8 | H3 | Which features are available at Lizaro?
c2h9 | H3 | Does Lizaro offer e-sports and virtual sports?
c2h10 | H2 | Lizaro Live Betting
c2h11 | H3 | How can I participate in live betting at Lizaro?
c2h12 | H3 | How does live payout compare to pre-match?
c2h13 | H3 | Are all sports covered in live betting?
c2h14 | H2 | Lizaro Sports Bonus
c2h15 | H3 | Lizaro Sports Promotions
c2h16 | H2 | Lizaro Casino Section
c2h17 | H3 | How many slot games are available at Lizaro?
c2h18 | H3 | What live casino options are offered?
c2h19 | H3 | Is the casino accessible on mobile devices?
c2h20 | H2 | What Are The Available Payment Methods At Lizaro?
c2h21 | H3 | Lizaro FIAT payments
c2h22 | H3 | Lizaro Crypto Payments
c2h23 | H2 | Additional Information on Lizaro
c2h24 | H3 | Lizaro Customer Support
