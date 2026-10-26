"""Report on the ТЗ of the Longfu88 SG app page: base block list, table of the 12 variants, structure distances.

    python tools/longfu88/app_sg_report.py            -> output/longfu88-app-sg-structure.md (+ a short summary on stdout)

Two distances are printed. "gate" is the one of textgen/variants.py (a new block is the topic "new: <words of its heading>", so the same
extra topic under two headings counts as two topics). "honest" counts an extra topic by its id (games, sports, pay, ...) whatever the
heading is, so it is the real difference in topics plus depth (facts, format, size, level)."""
import json
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from textgen import variants as V  # noqa: E402
from textgen.store import Run  # noqa: E402

BASE = "longfu88-app-sg"
NID = json.loads(Path("output/longfu88-app-sg-topics.json").read_text(encoding="utf-8"))
TOPIC_NAME = {"b02": "features", "b03": "download lead", "b04": "Android", "b05": "iOS", "b06": "devices", "b07": "shortcut/tab", "b08": "account",
              "b09": "security", "b10": "fixes", "b11": "support", "b12": "FAQ", "games": "games", "sports": "sports", "pay": "payments table",
              "wd": "withdrawals", "welcome": "welcome offer", "kyc": "verification", "rg": "responsible gaming", "reg": "registration",
              "vip": "VIP program", "promo": "cashback/reload", "data": "technical data", "elig": "eligibility", "cur": "currencies/languages"}
RATIONALE = {
    "b01": "H1 with the keyword \"Longfu88 app\"; names the page as the mobile route (responsive site + home-screen shortcut) and signposts the topics; competitors open with the same promise (.bid, .best, .vin, tribuna). Facts: platforms, mobile access, minimum age.",
    "b02": "Cluster k01 (Mobile Access, 5 of 5 competitors: \"what the app offers\", \"6 functions\", \"what works on mobile\"). Position 2 like .best/.vin. Only the six features of brandinfo_app; games, sports, payments and bonuses are left to the site's other pages (k08 and k09 are skipped with a reason).",
    "b03": "Cluster k01, install lead (.best \"install in 3 steps\", tribuna \"how to download\", official.games \"add to home screen\"). It answers the \"download / apk\" intent honestly: the KB has no file, so the block says a shortcut is added and carries the keywords Longfu88 download (heading) and Longfu88 apk (body).",
    "b04": "H3 under the install lead (competitors give Android and iOS separate sub-sections). Chrome > menu > Add to Home screen > confirm; exactly the KB steps; carries \"Longfu88 Android\". Nothing about APK, unknown sources or OS versions (tribuna invents them).",
    "b05": "H3, the iOS twin: Safari > Share > Add to Home Screen > Add; carries \"Longfu88 iOS\". Different lead-in from b04.",
    "b06": "Cluster k01 \"phones and versions\" (.bid, .best, .vin, official.games). Only the three platforms of the KB; no OS versions, memory or speed, which the competitors invent.",
    "b07": "Cluster k01 \"app vs mobile browser\" (.bid, .vin, tribuna): reframed as shortcut vs browser tab, because the KB has one website. Compares only what is true: same site, same account, one-time setup.",
    "b08": "Cluster k03 (Registration and Login, official.games \"Login on mobile\", .best \"account recovery\"). Login by e-mail and password as on a computer, Forgot Password as a pointer; gets the internal link to /login. No 2FA, biometrics, session timeout (competitors invent them).",
    "b09": "Cluster k07 (Safety; .best/.vin/.bid/official.games \"mobile security\"). Only two KB facts: the holder keeps the credentials, the operator applies safeguards and may suspend activity; notes forbid code signing, encryption and 2FA claimed by competitors.",
    "b10": "Our own block (competitors have troubleshooting: official.games, tribuna). Four plain fixes: shortcut missing, page not loading, login failing, still stuck; no error codes.",
    "b11": "Support is a non-mandatory cluster (k02) but every app page has it (.bid, .best, .vin). Live chat 24/7 and e-mail from the KB; the e-mail contains the keyword Longfu88, so the block holds exactly one brand mention (INTRINSIC rule).",
    "b12": "Cluster k06 FAQ (all five competitors close with questions). Five questions on a store app, phones, shortcut, login and help; answers repeat facts only.",
}
PROBLEMS = [
    "Stale run input: `00_input.json` had been written before the input file got its `Site pages` line (the CLI reuses an existing run input). I removed `00_input.json` and re-ran step 1, so the run now carries `site_pages`.",
    "`Site pages - bonuses, login, app` would plant a link from the app page to itself (the keyword \"Longfu88\" gives no own slug); the app input now says `Site pages - bonuses, login`. The same trap exists for the other two page types of the batch if they list their own page.",
    "`python -m textgen variants` does not plant internal links (only step 1 does); `tools/longfu88/attach_links_variants.py` does it for the variants afterwards (idempotent).",
    "Headings that contain withdraw / payment / deposit words need a table in the same block (validate_visuals): v09's H1 and v12's withdrawal block were renamed (\"Cash-Out\") instead of adding a table to a list of steps.",
    "Competitor clusters are rule-based (make_clusters.py); three competitor pages are in Malay, so only k01, k03, k06, k07, k08, k09 are mandatory. Games (k08) and payments (k09) belong to other pages of the site: the base skips them with a reason (2 of 6), variants that add games or payments cover them instead.",
    "The KB has no native app: all competitor claims about APK files, OS versions, biometrics, push notifications, code signing, encryption, 2FA, offline mode are excluded by NO_APP_CLAIMS / NO_SECURITY_CLAIMS in every block.",
    "The gate of textgen/variants.py counts an extra topic under two different headings as two topics, which inflates the distance; the report therefore also prints the honest distance (extra topics by id).",
]


def profile_honest(brief, base):
    p = V.topic_profile(brief, base)
    out = {}
    for k, v in p.items():
        if k.startswith("new:"):
            # find the heading of this block
            for b in brief["blocks"]:
                if (b.get("variant_origin") or ["new"]) == ["new"] and f'new:{" ".join(sorted(V._words(b["heading"])))}' == k:
                    out["x:" + NID[b["heading"].lower()]] = v
                    break
        else:
            out[k] = v
    return out


def main() -> None:
    base_run = Run.open(BASE)
    base = base_run.load_json("01_brief.json")
    runs = sorted(p.name for p in Path("runs").glob(f"{BASE}-v[0-9][0-9]"))
    briefs = {n[-3:]: Run.open(n).load_json("01_brief.json") for n in runs}
    prof = {k: V.topic_profile(b, base) for k, b in briefs.items()}
    hon = {k: profile_honest(b, base) for k, b in briefs.items()}
    names = list(briefs)

    def tname(key):
        key = key.replace("x:", "")
        return TOPIC_NAME.get(key, key)

    L = ["# Longfu88 app page, SG: brief structure", "", "Base run `longfu88-app-sg` (medium group: 975 / 983 words -> target 979, limit 1175), 12 variants "
         "`longfu88-app-sg-v01..v12` (small 3, medium 4, large 5). Source of the numbers: `runs/longfu88-app-sg-vNN/01_brief.json`.", "",
         "## a) Base ТЗ: blocks and why", "", "| # | Level | Heading | Words | Keywords (body) | Why this heading, here, with these facts |", "|---|---|---|---|---|---|"]
    for b in base["blocks"]:
        kws = ", ".join(f"{k} x{v}" for k, v in b["keywords"].items() if v) or "-"
        hk = ", ".join(f"{k} x{v}" for k, v in b["heading_keywords"].items() if v)
        L.append(f'| {b["id"]} | H{b["level"]} | {b["heading"]} | {b["words_min"]}-{b["words_max"]} | {kws}{" ; heading: " + hk if hk else ""} | {RATIONALE[b["id"]]} |')
    L += ["", f'Base total {base["targets"]["target_body_words"]} words; keyword targets: ' + ", ".join(f"{k} x{v}" for k, v in base["targets"]["keyword_targets"].items()) + ".",
          "Skipped mandatory clusters: " + "; ".join(f'{s["id"]} ({s["reason"]})' for s in base.get("skipped_clusters", [])) + ".", "",
          "## b) The 12 variants", "", "| Variant | Group | Words (mid sum / limit) | Blocks | Headings in order (H1 / H2 / H3) | What makes the structure different |", "|---|---|---|---|---|---|"]
    allt = {k: set(hon[k]) for k in names}
    for k in names:
        b = briefs[k]
        heads = "<br>".join(f'{"H"+str(x["level"])} {x["heading"]}' for x in b["blocks"])
        extras = sorted(t for t in allt[k] if t.startswith("x:"))
        lacks = sorted(t for t in TOPIC_NAME if t.startswith("b") and t not in ("b01",) and t not in allt[k])
        merged = [x for x in b["blocks"] if len(x.get("variant_origin", [])) > 1]
        diff = "extra: " + (", ".join(tname(t) for t in extras) or "none") + "; without: " + (", ".join(tname(t) for t in lacks) or "none")
        if merged:
            diff += "; merged: " + "; ".join("+".join(tname(o) for o in m["variant_origin"]) for m in merged)
        tbl = [tname(x) for x in prof[k] if False]
        fm = [(NID.get(x["heading"].lower(), None) and tname(NID[x["heading"].lower()])) or tname(x["variant_origin"][0]) for x in b["blocks"] if "table" in x["formats"]]
        if fm:
            diff += "; tables: " + ", ".join(fm)
        L.append(f'| {k} | {b["targets"]["tier"]} | {b["targets"]["target_body_words"]} / {b["targets"]["max_body_words"]} (max sum {sum(x["words_max"] for x in b["blocks"])}) | {len(b["blocks"])} | {heads} | {diff} |')
    # distances
    def dist(pr):
        out = {}
        for a, c in combinations(names, 2):
            out[(a, c)] = V.structure_distance(pr[a], pr[c])
        return out

    dg, dh = dist(prof), dist(hon)
    L += ["", "## c) Structure distance (gate: every pair >= 2.0)", "", "| pair | gate | honest | topics only one covers (honest) | depth (honest) | most different shared topics (honest) |", "|---|---|---|---|---|---|"]
    for key in dg:
        g, h = dg[key], dh[key]
        L.append(f"| {key[0]} / {key[1]} | {g[0]:.1f} | {h[0]:.1f} | {h[1]} | {h[2]:.1f} | {'; '.join(h[3][:2]) or '-'} |")
    gv, hv = sorted(v[0] for v in dg.values()), sorted(v[0] for v in dh.values())
    mid = lambda xs: xs[len(xs) // 2]  # noqa: E731
    lo_g = min(dg, key=lambda k: dg[k][0])
    lo_h = min(dh, key=lambda k: dh[k][0])
    L += ["", f"- gate: min {gv[0]:.1f} ({lo_g[0]} / {lo_g[1]}), median {mid(gv):.1f}, max {gv[-1]:.1f}; pairs below 2.0: {sum(x < 2 for x in gv)}",
          f"- honest: min {hv[0]:.1f} ({lo_h[0]} / {lo_h[1]}), median {mid(hv):.1f}, max {hv[-1]:.1f}; pairs below 2.0: {sum(x < 2 for x in hv)}",
          "", "## d) Problems met and how they were resolved", ""] + [f"- {p}" for p in PROBLEMS]
    Path("output/longfu88-app-sg-structure.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"gate min {gv[0]:.1f} ({lo_g}) median {mid(gv):.1f}; honest min {hv[0]:.1f} ({lo_h}) median {mid(hv):.1f}; below 2.0: gate {sum(x < 2 for x in gv)}, honest {sum(x < 2 for x in hv)}")
    for k in names:
        b = briefs[k]
        print(k, b["targets"]["tier"], b["targets"]["target_body_words"], "/", b["targets"]["max_body_words"], "max-sum", sum(x["words_max"] for x in b["blocks"]), "blocks", len(b["blocks"]))


if __name__ == "__main__":
    main()
