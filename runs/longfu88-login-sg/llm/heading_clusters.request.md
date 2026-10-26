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

c0h1 | H2 | How to Register and Log In to Your Longfu88 Account
c0h2 | H3 | Step-by-Step Registration Process
c0h3 | H2 | Troubleshooting Login Issues – Get Back to Gaming Fast
c0h4 | H3 | 1. Double-Check Your Login Information
c0h5 | H3 | 2. Clear Your Browser Cache and Cookies
c0h6 | H3 | 3. Try a Different Device or Browser
c0h7 | H3 | 4. Contact Customer Support
c0h8 | H2 | Longfu88 Casino Bonuses – Start Your Journey with Exciting Offers
c0h9 | H3 | Welcome Bonus Overview
c0h10 | H2 | Customer Support – We’re Here to Help!
c0h11 | H2 | FAQ – Frequently Asked Questions
c0h12 | H3 | How do I log in to my Longfu88 account?
c0h13 | H3 | What should I do if I forgot my password?
c0h14 | H3 | How do I verify my account?
c0h15 | H3 | Can I log in from multiple devices?
c1h1 | H2 | How to Register at Longfu88
c1h2 | H3 | Create Your Account ‚Äî Claim 188% Welcome Bonus
c1h3 | H2 | Longfu88 Login Process ‚Äî Quick Access to Your Account
c1h4 | H3 | Account Recovery and Password Reset
c1h5 | H2 | Account Security Features at Longfu88
c1h6 | H2 | Account Verification Requirements
c1h7 | H3 | Verify Your Account ‚Äî Unlock Full Access
c1h8 | H2 | Managing Your Longfu88 Account Settings
c1h9 | H3 | Deposit and Withdrawal Limits
c1h10 | H3 | Communication Preferences
c1h11 | H2 | Multi-Currency and Multi-Account Policies
c1h12 | H2 | Account Closure and Self-Exclusion
c1h13 | H3 | Your Account Opens Thousands of Games
c1h14 | H2 | Mobile Account Access
c1h15 | H2 | VIP Account Benefits and Tier Progression
