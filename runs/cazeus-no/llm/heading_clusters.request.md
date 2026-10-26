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

c1h1 | H2 | About Cazeus casino Norway
c1h2 | H2 | Casino games
c1h3 | H3 | Slots
c1h4 | H3 | Table games
c1h5 | H3 | Live dealer games
c1h6 | H3 | Free games
c1h7 | H3 | Sportsbook
c1h8 | H2 | Bonuses and promotions
c1h9 | H2 | Deposits and withdrawals
c1h10 | H3 | Deposit methods
c1h11 | H3 | Withdrawal methods
c1h12 | H2 | Mobile and app experience
c1h13 | H2 | Licenses and security
c1h14 | H2 | Customer support
c1h15 | H2 | Responsible gambling tools
c1h16 | H2 | Our verdict on Cazeus casino for Norway players
c1h17 | H3 | Cazeus casino overview
c1h18 | H2 | User Reviews
c3h1 | H2 | Velkomstbonus: opptil 5000 kroner + 200 freespins!
c3h2 | H2 | Bonuskode
c3h3 | H2 | Freespins
c3h4 | H2 | Spesielle kampanjer og casino tilbud
c3h5 | H3 | Lojalitetsordning/VIP-program
c3h6 | H2 | Spillutvalg på Cazeus
c3h7 | H2 | Live casino
c3h8 | H2 | Sammenligning
c3h9 | H2 | Mobil casino og app
c3h10 | H2 | Innskudd og uttak på Cazeus Casino Norge
c3h11 | H2 | Kontakte kundesupport
c3h12 | H2 | Om Cazeus
c3h13 | H3 | Historien bak Cazeus
c3h14 | H2 | Ansvarlig spilling
c3h15 | H2 | Brukererfaring
c3h16 | H3 | Begrunnelse for scoren vi har gitt Cazeus
c3h17 | H3 | Totalvurdering – 84%
c3h18 | H2 | Skribentens kommentar
c3h19 | H2 | Ofte stilte spørsmål
c3h20 | H2 | Flere casinoomtaler
