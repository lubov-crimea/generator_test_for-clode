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
