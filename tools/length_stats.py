"""Length statistics of the competitors for every finished run (base runs, not the -vNN variants that copy them):
the body of the whole page and the size of every heading cluster per competitor, as median / 3rd quartile / mean and the same values
x1.2 and x1.3 (candidate limits). Writes output/length_stats.md and output/length_stats.csv. Run from the project root:
    python tools/length_stats.py

A cluster size is what one competitor writes about the topic: the sum of the section words of its headings in the cluster. The
statistics are taken over the competitors that have the cluster. Clusters come from runs/<run>/llm/heading_clusters.json (member ids
c<competitor>h<heading>), or, when that file is missing, from the examples saved in 01_heading_clusters.json (up to 8 per cluster:
marked `~`)."""
import csv
import json
import math
import re
import statistics
from pathlib import Path

RUNS = Path("runs")
OUT = Path("output")
MULTS = (1.0, 1.2, 1.3)
MANDATORY_RATIO = 0.5


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def stats(values: list[int]) -> dict[str, float]:
    q3 = statistics.quantiles(values, n=4, method="inclusive")[2] if len(values) > 1 else values[0]
    return {"median": statistics.median(values), "q3": q3, "mean": statistics.mean(values)}


def row_numbers(values: list[int]) -> list[int]:
    s = stats(values)
    return [round(s[k] * m) for m in MULTS for k in ("median", "q3", "mean")]


def clusters_of(run: Path, pages: list[dict]) -> list[dict]:
    """[{title, ids:[(competitor, heading index)], approx}] like the pipeline: the model's clusters + one cluster per forgotten heading."""
    ok = [i for i, p in enumerate(pages) if p.get("ok")]
    flat = {f"c{i}h{j}": (i, j) for i in ok for j, h in enumerate(pages[i]["headings"]) if h["level"] != 1}
    out: list[dict] = []
    answer = run / "llm" / "heading_clusters.json"
    if answer.exists():
        seen: set[str] = set()
        for c in load(answer)["clusters"]:
            ids = [m for m in c["member_ids"] if m in flat and m not in seen]
            if ids:
                seen.update(ids)
                out.append({"title": c["canonical_title"], "ids": [flat[m] for m in ids], "approx": False})
        for hid, (i, j) in flat.items():
            if hid not in seen:
                out.append({"title": pages[i]["headings"][j]["text"], "ids": [(i, j)], "approx": False})
        return out
    by_text = {(i, pages[i]["headings"][j]["level"], pages[i]["headings"][j]["text"]): (i, j) for (i, j) in flat.values()}
    for c in load(run / "01_heading_clusters.json"):
        ids = [by_text[(e["competitor"], e["level"], e["text"])] for e in c["examples"] if (e["competitor"], e["level"], e["text"]) in by_text]
        if ids:
            out.append({"title": c["canonical_title"], "ids": ids, "approx": c["frequency"] > len({i for i, _ in ids}) or len(c["examples"]) >= 8})
    return out


def analyse(run: Path) -> dict:
    pages = load(run / "01_competitors_raw.json")
    for p in pages:  # a page that loaded but has no text (script-rendered, blocked) says nothing about the length
        if p.get("ok") and not p.get("body_words"):
            p["ok"], p["empty"] = False, True
    ok = [i for i, p in enumerate(pages) if p.get("ok")]
    need = max(2 if len(ok) >= 2 else 1, math.ceil(MANDATORY_RATIO * len(ok)))
    pipeline = load(run / "01_keyword_stats.json")["aggregate"]["median_body_words"] if (run / "01_keyword_stats.json").exists() else None
    rows = []
    intro = [sum(h["words"] for h in pages[i]["headings"] if h["level"] == 1) for i in ok]
    intro = [w for w in intro if w > 0]
    if intro:
        rows.append({"title": "(H1 intro)", "values": intro, "mandatory": False, "approx": False})
    for c in clusters_of(run, pages):
        per: dict[int, int] = {}
        for i, j in c["ids"]:
            per[i] = per.get(i, 0) + pages[i]["headings"][j]["words"]
        values = [w for w in per.values() if w > 0]
        if values:
            rows.append({"title": c["title"], "values": sorted(values), "mandatory": len(per) >= need, "approx": c["approx"]})
    rows.sort(key=lambda r: (-r["mandatory"], -len(r["values"]), r["title"]))
    body = [pages[i]["body_words"] for i in ok]
    job = load(run / "00_input.json")
    brief = load(run / "01_brief.json")["targets"] if (run / "01_brief.json").exists() else {}
    variants = [load(v / "01_brief.json")["targets"]["target_body_words"] for v in sorted(RUNS.glob(f"{run.name}-v[0-9][0-9]")) if (v / "01_brief.json").exists()]
    return {"run": run.name, "geo": job["geo"], "page_type": job.get("page_type", "brand-review"), "competitors": len(ok), "of": len(pages),
            "empty": sum(1 for p in pages if p.get("empty")), "pipeline": pipeline,
            "body": sorted(body), "rows": rows, "need": need, "tz": brief.get("target_body_words"), "tz_limit": brief.get("max_body_words"),
            "variants": (min(variants), max(variants), len(variants)) if variants else None}


HEAD = ["median", "Q3", "mean", "median x1.2", "Q3 x1.2", "mean x1.2", "median x1.3", "Q3 x1.3", "mean x1.3"]


def main() -> None:
    runs = sorted(p for p in RUNS.iterdir() if p.is_dir() and not p.name.startswith("_") and not re.search(r"-v\d\d$", p.name)
                  and (p / "01_competitors_raw.json").exists())
    data = [analyse(r) for r in runs]
    OUT.mkdir(exist_ok=True)
    md = ["# Competitor length statistics", "",
          "Body words (headings excluded). Q3 = 3rd quartile (inclusive), the x1.2 / x1.3 columns multiply each statistic. "
          "A cluster size is what one competitor writes on the topic (the sum of its section words in the cluster); `~` = from the saved examples only.", "",
          "Pages that loaded but have no text (body 0) are left out; `pipeline median` is the median the ТЗ used (it still counted those pages).", "",
          "## Whole page", "", "| run | page type | competitors | body words per competitor | " + " | ".join(HEAD) + " | pipeline median | ТЗ now (base / variants) |",
          "|---|---|---|---|" + "---|" * (len(HEAD) + 2)]
    csv_rows = [["run", "cluster", "mandatory", "competitors", "values"] + HEAD]
    for d in data:
        nums = row_numbers(d["body"])
        tz = f'{d["tz"]}' + (f' (limit {d["tz_limit"]})' if d["tz_limit"] else "") + (f' / {d["variants"][0]}-{d["variants"][1]} ({d["variants"][2]})' if d["variants"] else "")
        md.append(f'| {d["run"]} | {d["page_type"]} | {d["competitors"]}/{d["of"]}{f" (+{d["empty"]} empty)" if d["empty"] else ""} | {", ".join(map(str, d["body"]))} | '
                  + " | ".join(map(str, nums)) + f' | {d["pipeline"]} | {tz} |')
        csv_rows.append([d["run"], "(whole page)", "", d["competitors"], " ".join(map(str, d["body"]))] + nums)
    md += ["", "## Clusters per run (mandatory = in at least half of the loaded competitors; singletons of one competitor are listed last)", ""]
    for d in data:
        md += [f'### {d["run"]} ({d["geo"]}, {d["competitors"]} competitors, mandatory from {d["need"]})', "",
               "| cluster | mandatory | n | sizes | " + " | ".join(HEAD) + " |", "|---|---|---|---|" + "---|" * len(HEAD)]
        for r in d["rows"]:
            nums = row_numbers(r["values"])
            title = r["title"].replace("|", "/")
            md.append(f'| {title}{" ~" if r["approx"] else ""} | {"yes" if r["mandatory"] else ""} | {len(r["values"])} | {", ".join(map(str, r["values"]))} | ' + " | ".join(map(str, nums)) + " |")
            csv_rows.append([d["run"], r["title"], "yes" if r["mandatory"] else "", len(r["values"]), " ".join(map(str, r["values"]))] + nums)
        md.append("")
    (OUT / "length_stats.md").write_text("\n".join(md), encoding="utf-8")
    with open(OUT / "length_stats.csv", "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f, delimiter=";").writerows(csv_rows)
    print(f"{len(data)} runs -> {OUT / 'length_stats.md'}, {OUT / 'length_stats.csv'}")


if __name__ == "__main__":
    main()
