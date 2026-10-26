PAGE TYPE: FOCUSED BRAND PAGE (the input `page.page_type` is "brand-subpage")

The page is not the general review of the brand: it is one page about a single topic (login, app, VIP programme, sports, bonuses and promo code, payments or similar) named by the H1. Everything above applies, plus:

- Topic discipline: report a block that retells other topics of the brand (games, the general review, company data, bonuses on a login page) instead of serving the topic of the page. A short pointer to a neighbouring topic of at most one clause is fine and is not a problem. The fix names the fragment to cut.
- Steps and procedures: a step, URL, button name, limit, time or screen of the brand is a brand fact and must be in the block's `brand_info`. A block without `brand_info` may only contain general industry knowledge; a brand procedure there is an invented fact. The order of steps equals the order in `brand_info`.
- Missing facts are never signalled to the reader ("check the website", "the details are not published"): report such wording as an issue and, when a fact the topic needs is simply absent from `brand_info`, add it to `missing_data` instead of asking the rewriter to invent it.
- There is no brand fact sheet on this page; do not ask for one.
