"""Writes output/longfu88-bonus-sg-structure.md: rationale of the base ТЗ of the SG bonuses page, the 12 variants side by side, the structure
distance and the problems met. Run from the project root after `python -m textgen variants input/variants/longfu88-bonus-sg.json`:
    python tools/longfu88/make_bonus_sg_report.py"""
import json
import re
import statistics
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RUNS = Path("runs")
base = json.loads((RUNS / "longfu88-bonus-sg" / "01_brief.json").read_text(encoding="utf-8"))
clusters = {c["id"]: c for c in json.loads((RUNS / "longfu88-bonus-sg" / "01_heading_clusters.json").read_text(encoding="utf-8"))}

TOPIC = {"B01": "intro", "OV": "offer overview", "WB": "welcome bonus", "CL": "claim steps", "TM": "terms and wagering", "PC": "promo code", "MD": "minimum deposits",
         "RL": "reload bonuses", "FS": "free spins", "CR": "crypto offers", "LV": "live casino offers", "SE": "seasonal campaigns", "CB": "cashback", "RB": "rebates",
         "VP": "VIP program", "RW": "rewards area", "SP": "sports bonuses", "VF": "verification", "RG": "responsible use", "MB": "mobile access", "CK": "checklist",
         "FQ": "FAQ", "N1": "glossary (new)", "N2": "cashing out winnings (new)", "N3": "validity by offer (new)", "N4": "wagering compared (new)",
         "N5": "ledger of all offers (new)", "N6": "Bonus Crab detail (new)", "N7": "sports extras (new)"}
BASE_CODES = ["B01", "OV", "WB", "CL", "TM", "PC", "MD", "RL", "FS", "CR", "LV", "SE", "CB", "RB", "VP", "RW", "SP", "VF", "RG", "MB", "CK", "FQ"]

WHY = {
    "b01": "H1 + intro. Carries the tracked keyword 'Longfu88 promotions' (as tips.gg and tribuna put the brand + the topic into the H1). 'Longfu bonus' stands once in the body. The summary of the knowledge base (188% up to €2,088 + 18 Free Spins) is quoted once; the Singapore legal disclaimer sits here and in the sensitive blocks. Facts: welcome_bonus_summary, minimum_age.",
    "b02": "Cluster k01 (overview of bonus types; 3 of 4 competitors open with a table or list of the offers). Position 2 because the reader first wants the map. Heading carries 'Longfu88 bonus' (tips.gg uses it in 13 headings). A list of five families with names only, no amounts, so that the next blocks do not repeat numbers.",
    "b03": "Cluster k02 (welcome bonus, 3 competitors, avg position 0.21). First after the map. Heading has 'Longfu88 welcome bonus'. Facts only from the Casino Welcome Bonus plus the two alternatives; the €50 bonus deposit, never the general €10. Competitors' 100% up to $400 is forbidden.",
    "b04": "Cluster k03 (how to claim, 2 competitors, avg position 0.25, 219 words). Numbered list of the four steps of the knowledge base. The planted optional link to /login sits here (registration). Notes forbid copying steps that contain the brand name.",
    "b05": "Cluster k04 (wagering and terms, 3 competitors, the longest section of the pages: 197 words). Table term | value (25x, 40x, 10 days, €22.5, 5x) + the rules that can cost the bonus. Heading has the second 'Longfu88 bonus'. Competitors' '~20x' and '10-14 days' are not the casino's and are forbidden.",
    "b06": "Promo code is the topic of a tracked keyword and a question of tips.gg and tribuna; the knowledge base lists NO code, so the block answers exactly that and forbids inventing or implying a code (also affiliate codes). Heading has 'Longfu88 promo code'.",
    "b07": "Cluster k12 (payment methods and bonus compatibility, play.my). Only what concerns bonuses: the minimum deposit of each offer (table, nine rows) and the Neteller/Skrill exclusion. The general limits and the payment list belong to the payments page. The word 'Deposits' in the heading obliges a table (it has one).",
    "b08": "Cluster k05 (reload bonuses, 3 competitors). Table of four reloads; the Weekly Reload (50 Free Spins) is left to the free spins block so that no fact is repeated.",
    "b09": "Cluster k07 (free spins, play.my). Weekly Reload 50 Free Spins and the seasonal Pumpkin Bonanza with their 40x wagering on the winnings; no game names (none given).",
    "b10": "Crypto welcome and the two crypto reloads: the knowledge base has a full crypto offer set and the SG audience pays in USDT/crypto as well. Table + eligible coins.",
    "b11": "Live casino welcome bonus, live cashback and live rebate in one block: the live offers are a separate audience in the knowledge base.",
    "b12": "Seasonal Pumpkin Bonanza and the Dragon Quest verification reward: limited campaigns, the block warns that the list may change and forbids saying they run now.",
    "b13": "Cluster k06 (cashback, 2 competitors). The weekly cashback with the rates by VIP tier (table) and the live cashback. No VIP page exists on the SG sites, so the VIP levels may live here and in b15. Heading marks both parts.",
    "b14": "Unlimited rebates by category (table, four rows) - the knowledge base lists four, tribuna/tips.gg do not mention them: a differentiating section.",
    "b15": "Cluster k10 (VIP, play.my). The VIP program of the knowledge base: tiers, points, a five-row table of the 25 numbered levels. Notes forbid mapping tiers to levels (the base does not) and forbid quoting the level cashback % (could contradict the weekly cashback table).",
    "b16": "Cluster k09 (Bonus Crab etc., sg.com 8 headings). Rewards area as a five-item list.",
    "b17": "Cluster k11 (sports bonuses, play.my 189-word section; tips.gg mixes sports credits into the same offers). Table of four sports offers (8x wagering), the odds rule, Sports Cashback and Parlay Boost.",
    "b18": "Verification before bonus winnings (tips.gg: KYC before withdrawals, tribuna: confirmed account and verification). Documents list, 30-day window, 10-day review.",
    "b19": "Terms-and-responsible-usage heading of play.my (c3h12). Age, lawful play, self-assessment, support organisations; the legal disclaimer again.",
    "b20": "Cluster k13 (mobile bonus access, play.my). The base has no native app: the block forbids an app/APK claim; the planted optional link to /app sits here.",
    "b21": "Cluster k21 (verdict and strategy, tips.gg and play.my: 'Final verdict', 'Should you take advantage'). The notes forbid a verdict, a rating and advice, so the cluster is covered by a neutral checklist of seven checks.",
    "b22": "Cluster k20 (FAQ, 3 competitors, always the last section). Seven bold-question items; heading has 'Longfu88 offers'. No e-mail address is printed (it contains the brand).",
}

variants = {}
for i in range(1, 13):
    vid = f"v{i:02d}"
    brief = json.loads((RUNS / f"longfu88-bonus-sg-{vid}" / "01_brief.json").read_text(encoding="utf-8"))
    spec = json.loads((RUNS / f"longfu88-bonus-sg-{vid}" / "01_variant.json").read_text(encoding="utf-8"))
    variants[vid] = (brief, spec)

freq = Counter(code for _, spec in variants.values() for code in {b["topic"] for b in spec["blocks"]})


def heads(brief):
    return " > ".join(f'{"H" + str(b["level"])} {b["heading"]}' for b in brief["blocks"])


out = ["# Longfu88 SG: bonuses and promo code page, base ТЗ and 12 variants", "",
       "Generated by `tools/longfu88/make_bonus_sg_report.py` from `runs/longfu88-bonus-sg*`. Input `input/longfu88-bonus-sg.txt`, KB longfu88-new (id 576, unchanged since 2026-10-21), "
       "competitors read: tips.gg 2634 body words, tribuna.com 683, longfu88-sg.com/bonus 631, longfu88-play.my/bonuses 2544 (tips.gg and tribuna answer 403 to a script; their text was read in the browser and saved to `input/html/`).", "",
       "Size groups: small 631/683 (target 657, limit 788), medium 2544 (limit 3053), large 2634 (limit 2634, may be shorter). 12 texts: small 4, medium 6, large 2.", "",
       "## a) Base ТЗ (medium)", "",
       f'{len(base["blocks"])} blocks, {base["targets"]["target_body_words"]} words (limit {base["targets"]["max_body_words"]}), keywords {base["targets"]["keyword_targets"]}. '
       "The structure is the clusters of the competitors (mandatory: k01 overview, k02 welcome bonus, k03 claim steps, k04 wagering/terms, k05 reload, k06 cashback, k20 FAQ, k21 verdict) "
       "in the order of the reader's task: map -> main offer -> how to claim -> terms -> the code question -> the other offers -> loyalty and sports -> rules -> checklist -> FAQ. "
       "The base holds the WHOLE pool of topics; each variant takes a subset at its own depth.", "",
       "| # | Level | Heading | Words | Format | Clusters | Why this block, here |", "|---|---|---|---|---|---|---|"]
for b in base["blocks"]:
    cl = ", ".join(f"{c} {clusters[c]['canonical_title']}" for c in b["covers_clusters"]) or "-"
    out.append(f'| {b["id"]} | H{b["level"]} | {b["heading"]} | {b["words_min"]}-{b["words_max"]} | {"+".join(b["formats"])} | {cl} | {WHY[b["id"]]} |')

out += ["", "## b) The 12 variants", "",
        "| Variant | Group | Words (sum of mids) | Sum of maxima / limit | Blocks | Headings in page order | Topics most others lack |", "|---|---|---|---|---|---|---|"]
for vid, (brief, spec) in variants.items():
    codes = {b["topic"] for b in spec["blocks"]}
    rare = sorted((c for c in codes if freq[c] <= 3 and c not in ("B01",)), key=lambda c: freq[c])
    rare_txt = ", ".join(f"{TOPIC[c]} ({freq[c]}/12)" for c in rare) or "-"
    out.append(f'| {vid} {spec["name"]} | {brief["targets"]["tier"]} | {brief["targets"]["target_body_words"]} | {sum(b["words_max"] for b in brief["blocks"])} / {brief["targets"]["max_body_words"]} '
               f'| {len(brief["blocks"])} | {heads(brief)} | {rare_txt} |')

out += ["", "### Topics per variant (X = the variant has the topic; v01 merges the claim steps into its welcome bonus block, so only the welcome bonus is marked for it)", "",
        "| Topic | " + " | ".join(variants) + " | in how many |", "|---|" + "---|" * (len(variants) + 1)]
for code in BASE_CODES + ["N1", "N2", "N3", "N4", "N5", "N6", "N7"]:
    cells = ["X" if code in {b["topic"] for b in spec["blocks"]} else "" for _, spec in variants.values()]
    out.append(f"| {TOPIC[code]} | " + " | ".join(cells) + f" | {freq[code]} |")

dist = (Path("output") / "longfu88-bonus-sg-variants.md").read_text(encoding="utf-8").split("## Structure distance")[1].split("## Headings")[0]
rows = [(float(x), p) for p, x in re.findall(r"^\| (v\d+ / v\d+) \| ([\d.]+)", dist, re.M)]
vals = sorted(rows)
topics = {vid: {b["topic"] for b in spec["blocks"]} for vid, (_, spec) in variants.items()}
honest = sorted((len(topics[a] ^ topics[b]), a, b) for a, b in combinations(topics, 2))
out += ["", "## c) Structure distance", "",
        f"Official metric (`textgen/variants.py`, minimum {2.0:g}): {len(vals)} pairs, min {vals[0][0]} ({vals[0][1]}), median {statistics.median(v for v, _ in vals):.1f}, max {vals[-1][0]} ({vals[-1][1]}). "
        f"The five closest pairs: " + ", ".join(f"{p} {v}" for v, p in vals[:5]) + ".", "",
        "The official metric counts a new block as a topic of its own (by heading words), so a topic that two variants share under different headings is counted twice. "
        f"The honest check by topic codes (the same new topic counts once, depth ignored): min {honest[0][0]} ({honest[0][1]} / {honest[0][2]}), median {honest[len(honest) // 2][0]}, max {honest[-1][0]}; "
        "depth differences (facts, format, size, level of the shared topics) come on top. Full table: `output/longfu88-bonus-sg-variants.md`.", ""]

out += ["## d) Problems met and how they were resolved", "",
        "- **Generic clusters.** The rule-based `make_clusters.py` put almost every bonus heading into one cluster and made payments and VIP 'mandatory'. Replaced by `tools/longfu88/make_bonus_sg_clusters.py` (21 bonus-specific clusters, 8 mandatory).",
        "- **Competitors behind 403.** tips.gg (2.6k words) and tribuna (bonuses 683 words) block scripts. Their text was read in the browser and saved as `input/html/*.html`; with them the groups became small 631/683, medium 2544, large 2634 (without them the MY run had 1029).",
        "- **Medium = 2544 words and a thin knowledge base.** The base holds 22 topics at about 115 words each; every block is KB-backed (no padding). The medium variants end at 2352-2476 words (8-4% under the mean 2544): the topics a variant drops are replaced by deeper treatment of others, not by filler.",
        "- **Site pages.** `Site pages` of the input is not read by an existing run (`00_input.json`) and the own slug is not removed when `keywords[0]` is 'Longfu88': fixed in `00_input.json` by hand (login, app) and in the input file; `textgen variants` drops the links, so `tools/longfu88/attach_links_variants.py longfu88-bonus-sg` was run afterwards (v01-v03 and v10 have no natural place for a link).",
        "- **Validator findings fixed in the scripts:** overloaded blocks (large variants have 3 connections per block: words raised for md, vf, rg, ck, n7), keyword density in an intro (v10), a keyword set in the note but missing in the counts (v07, v08, v12), the VIP pointer in the cashback notes removed where the variant has no VIP section (v03, v05, v08, v10, v06), the intro notes list only the topics of the variant, a mandatory cluster not covered (v09, skipped with a reason), headings with 'deposit/withdraw' need a table (renamed), duplicate headings (3 renamed).",
        "- **Keyword forms.** Step 3 counts inflected forms: 'Longfu88 bonuses', 'Longfu bonuses', 'Longfu88 promo codes' would count as tracked keywords. Every intent_summary forbids them.",
        "- **Not verified:** no text has been generated; the ranges are checked by the validator only. The competitors' own figures (100% up to $400, ~20x, 10-14 days) are not used anywhere.", ""]

path = Path("output/longfu88-bonus-sg-structure.md")
path.write_text("\n".join(out), encoding="utf-8")
print(path, len("\n".join(out)), "chars")
