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

c1h1 | H2 | Introduction
c1h2 | H2 | Vegas Hunter Casino Bonuses & Promotions
c1h3 | H2 | Casino Game Categories at Vegas Hunter
c1h4 | H3 | Games we cover
c1h5 | H3 | Slots
c1h6 | H3 | Card Games
c1h7 | H3 | Roulette
c1h8 | H3 | Crash Games
c1h9 | H3 | Game Shows
c1h10 | H3 | Casual Games
c1h11 | H3 | Fishing Games
c1h12 | H3 | Craps
c1h13 | H3 | Lottery Games
c1h14 | H3 | Mines Games
c1h15 | H3 | Video Poker
c1h16 | H3 | Virtual Sports
c1h17 | H2 | Mobile Casino App for Android & iOS
c1h18 | H2 | Top Providers
c1h19 | H2 | Payment Methods at Vegas Hunter Australia
c1h20 | H3 | Traditional Payment Methods
c1h21 | H3 | Cryptocurrency Payments
c1h22 | H3 | Additional Information
c1h23 | H2 | Why Australian Players Choose Vegas Hunter
c1h24 | H2 | How to Start Playing (Step-by-Step Guide)
c1h25 | H2 | Responsible Gambling
c1h26 | H2 | Support
c1h27 | H2 | Conclusion
c1h28 | H2 | FAQ
c2h1 | H2 | Everything About the CrashPirate Casino Site
c2h2 | H3 | Licensing, Safety and Is CrashPirate Legit?
c2h3 | H3 | Customer Support and Complaints
c2h4 | H2 | Registering an Account at CrashPirate
c2h5 | H2 | Payment Methods, Deposits and Withdrawals
c2h6 | H3 | Withdrawal Times, Limits and Processing
c2h7 | H3 | KYC Verification: Which Documents and How Long
c2h8 | H2 | Online Slots and Casino Games
c2h9 | H3 | Game Providers
c2h10 | H3 | Jackpot, Instant Win and Table Games
c2h11 | H3 | Crash Games and How They Work
c2h12 | H2 | Live Dealer Games
c2h13 | H2 | CrashPirate App and Mobile Play
c2h14 | H2 | Welcome Bonus and Ongoing Promotions
c2h15 | H2 | Tournaments and Prize Drops
c2h16 | H2 | VIP Club and Loyalty Rewards
c2h17 | H2 | Pros and Cons of CrashPirate Casino
c2h18 | H2 | Responsible Gambling and Player Protection
c2h19 | H3 | Is CrashPirate Casino Legit and Safe to Use?
c2h20 | H3 | Can UK Players Ppen an Account at CrashPirate?
c2h21 | H3 | How Long Do CrashPirate Withdrawals Take?
c2h22 | H3 | What Is the CrashPirate Welcome Bonus?
c2h23 | H3 | Does CrashPirate Have a Mobile App?
c2h24 | H3 | How Do Crash Games Work?
c2h25 | H3 | How Do I Contact CrashPirate Customer Support?
