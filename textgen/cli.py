"""Usage:
    python -m textgen run input/vegashunter.txt          # whole pipeline
    python -m textgen step1 vegashunter-australia        # single step on an existing run
    python -m textgen headings|step2|step3|step4 <run>
    python -m textgen loop <run>                          # step 3 + fix loop through step 2
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import headings as H
from . import store
from .config import RUNS_DIR, Settings
from .inputs import Job, load_job, make_slug
from .llm import AnthropicLLM, ManualLLM
from .pipeline import check_and_fix_loop, run_all
from .step1 import run_step1
from .step2 import run_step2
from .step3 import run_step3
from .step4 import run_step4
from .store import Run


def main(argv: list[str] | None = None) -> None:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    try:
        _main(argv)
    except (RuntimeError, FileNotFoundError, ValueError) as e:
        sys.exit(f"Error: {e}")


def _main(argv: list[str] | None) -> None:
    ap = argparse.ArgumentParser(prog="textgen")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("run", help="run the whole pipeline from an input file")
    p.add_argument("input")
    p.add_argument("--force", action="store_true", help="redo step 1 even if 01_brief.json exists")
    p.add_argument("--words", type=int, help="override target body length (default: median of competitors)")
    p.add_argument("--html-dir", type=Path, help="folder with saved competitor pages <domain>.html")
    p.add_argument("--force-final", action="store_true", help="save the txt even if checks did not pass")

    p = sub.add_parser("tiers", help="size groups of the competitors of a run and how many texts go to each group")
    p.add_argument("run")
    p.add_argument("--texts", type=int, help="number of texts to make: shows the split between the groups")

    for name in ("step1", "headings", "step2", "step3", "step4", "loop"):
        q = sub.add_parser(name)
        q.add_argument("run", help="run name (folder in runs/) or path")
        if name == "step1":
            q.add_argument("--words", type=int)
            q.add_argument("--html-dir", type=Path)
            q.add_argument("--force", action="store_true")
        if name == "step4":
            q.add_argument("--force-final", action="store_true")

    for name in ("variants", "compare"):
        q = sub.add_parser(name, help="build several different ТЗ from a blueprint (input/variants/*.json)" if name == "variants"
                           else "compare the ТЗ variants of a blueprint")
        q.add_argument("blueprint", type=Path)
        q.add_argument("--allow-similar", action="store_true",
                       help="do not fail when two variants cover the same set of topics (the default is to fail: the structures must differ)")
        if name == "variants":
            q.add_argument("--only", help="comma-separated variant ids, e.g. v01,v03")
            q.add_argument("--force", action="store_true", help="rebuild the ТЗ even if text generation has started")

    p = sub.add_parser("shingles", help="technical duplicates: runs of 9+ words shared by two texts (04_final.json of the given runs)")
    p.add_argument("runs", nargs="+", help="run names or glob patterns, e.g. 'longfu88-login-sg-v*'; every run is compared with every other one")
    p.add_argument("--n", type=int, default=9, help="shingle length in words (default 9)")
    p.add_argument("--json", type=Path, help="write the full report (every run of shared words) to this file")
    p.add_argument("--show", type=int, default=0, help="print the first N shared runs of every text")
    p.add_argument("--no-protected", action="store_true", help="count names, amounts and other protected facts of the knowledge base as ordinary words")

    p = sub.add_parser("lexical", help="the briefs of the variants of a base run must not share runs of 9+ words in their notes (they would be echoed by the writers)")
    p.add_argument("base", help="base run name; its variants are <base>-v01, <base>-v02 ...")
    p.add_argument("--n", type=int, default=9)

    p = sub.add_parser("bank", help="paraphrase bank of the knowledge base of a run: list | check | merge | status")
    p.add_argument("action", choices=["list", "check", "merge", "status"])
    p.add_argument("run", help="a run that uses the knowledge base")
    p.add_argument("--chunk", type=int, default=25, help="sentences per request file (list)")
    p.add_argument("--file", help="an answer file to validate (check)")

    for q in sub.choices.values():
        q.add_argument("--llm", choices=["api", "manual"], default="api",
                       help="manual = no API: requests go to <run>/llm/*.request.md, answers are read from <run>/llm/*.json")

    args = ap.parse_args(argv)
    settings = Settings.load()

    if args.cmd == "run":
        job = load_job(args.input)
        slug = make_slug(job)
        existing = RUNS_DIR / slug / store.INPUT
        if existing.exists() and not args.force:
            old = json.loads(existing.read_text(encoding="utf-8"))
            new = job.to_dict()
            key = ("keywords", "competitors", "geo", "page_type", "casinos")
            if tuple(old.get(k, [] if k == "casinos" else "brand-review" if k == "page_type" else None) for k in key) != tuple(new[k] for k in key):
                sys.exit(f"Run '{slug}' already exists with different input. Use --force to redo it from step 1.")
            new["language"] = old.get("language") or new["language"]
            job = Job(**new)
        run = Run.create(slug, job)
        print(f"run: {run.path}")
        ok = run_all(run, _make_llm(args, run), settings, args.html_dir, args.words, args.force, args.force_final)
        sys.exit(0 if ok else 2)

    if args.cmd in ("variants", "compare"):
        _variants(args, settings)
        return

    if args.cmd == "shingles":
        _shingles(args)
        return
    if args.cmd == "lexical":
        _lexical(args)
        return
    if args.cmd == "bank":
        _bank(args, settings)
        return

    if args.cmd == "tiers":
        from . import tiers as T

        from .analysis import usable_pages

        run = Run.open(args.run)
        if run.has(store.TIERS):
            tiers = run.load_json(store.TIERS)
        else:  # a run made before the size groups: computed from its saved competitor pages
            pages = usable_pages(run.load_json(store.COMPETITORS_RAW))
            tiers = T.build_tiers([p["body_words"] for p in pages if p.get("ok")], settings)
        print(T.describe(tiers))
        if args.texts:
            split = T.allocate(args.texts, tiers, settings)
            print(f"\n{args.texts} texts: " + ", ".join(f"{name} {n}" for name, n in split.items()))
        return

    run = _open_or_create(args.run)
    if args.cmd == "step4":
        run_step4(run, force=args.force_final)
        return
    llm = _make_llm(args, run)
    if args.cmd == "step1":
        run_step1(run, llm, settings, args.html_dir, args.words, args.force)
    elif args.cmd == "headings":
        brief = run.load_json(store.BRIEF)
        heads = H.localize(run, brief, llm, settings, only=None)
        for b in brief["blocks"]:
            print(f"  {b['id']} {b['heading']}  ->  {heads[b['id']]}")
    elif args.cmd == "step2":
        run_step2(run, llm, settings)
    elif args.cmd == "step3":
        passed, _ = run_step3(run, llm, settings, iteration=_next_iter(run))
        sys.exit(0 if passed else 2)
    elif args.cmd == "loop":
        sys.exit(0 if check_and_fix_loop(run, llm, settings) else 2)


def _variants(args, settings: Settings) -> None:
    from . import variants as V

    blueprint = json.loads(args.blueprint.read_text(encoding="utf-8"))
    V.configure(blueprint)
    base = Run.open(blueprint["base_run"])
    if base.job().page_type == "top-list":
        raise RuntimeError(f"Variants are built from a brand-review or brand-subpage ТЗ; the run {base.path.name} is a top-list.")
    only = set(args.only.split(",")) if getattr(args, "only", None) else None
    specs = [v for v in blueprint["variants"] if not only or v["id"] in only]
    briefs: dict[str, dict] = {}
    failed = False
    for spec in specs:
        slug = f'{base.path.name}-{spec["id"]}'
        if args.cmd == "variants":
            try:
                result = V.write_variant(base, spec, settings, force=args.force)
            except (RuntimeError, ValueError) as e:
                print(f"{slug}: FAILED\n  {e}")
                failed = True
                continue
            print(f"{slug}: {len(result['blocks'])} blocks, body {result['targets'].get('base_body_words')} -> {result['targets']['target_body_words']} words, "
                  f"keywords {result['targets']['keyword_targets']}")
        briefs[spec["id"]] = Run.open(slug).load_json(store.BRIEF) if (RUNS_DIR / slug / store.BRIEF).exists() else None
    briefs = {k: v for k, v in briefs.items() if v and "blocks" in v and "variant" in v}
    if len(briefs) > 1:
        from .config import OUTPUT_DIR

        base_brief = base.load_json(store.BRIEF)
        report = V.compare(briefs, base_brief)
        OUTPUT_DIR.mkdir(exist_ok=True)
        out = OUTPUT_DIR / f"{base.path.name}-variants.md"
        out.write_text(report, encoding="utf-8")
        print(report.split("## Headings")[0])
        print(f"full report: {out}")
        conflicts = V.structure_conflicts(briefs, base_brief)
        if conflicts and not getattr(args, "allow_similar", False):
            print("STRUCTURE TOO SIMILAR (see 'Structure distance' in the report; give the variants other topics or other depth of the shared topics, "
                  "or pass --allow-similar):")
            print("\n".join(f"  {c}" for c in conflicts))
            failed = True
    sys.exit(1 if failed else 0)


def _bank(args, settings: Settings) -> None:
    from .bankcmd import run_bank

    run_bank(args.action, Run.open(args.run), settings, args.chunk, args.file)


def _lexical(args) -> None:
    """Exit code 1 when the briefs of two variants share a run of `--n` words."""
    from . import lexical as L

    dups, words = L.lexical_conflicts(args.base, RUNS_DIR, args.n)
    if not words:
        raise RuntimeError(f"no variants of {args.base} (runs {args.base}-vNN with a 01_brief.json)")
    print(f"lexical check of the briefs ({args.n} words): {len(words)} variants")
    for name in sorted(words):
        runs = dups.get(name, [])
        w = sum(r["words"] for r in runs)
        print(f"  {name:28} {words[name]:5} words  {len(runs):3} shared runs  {w:4} words inside ({100 * w / max(words[name], 1):.0f}%)")
        for r in runs[:2]:
            print(f"      [{r['block']}] {r['words']}w with {','.join(x.rsplit('-', 1)[-1] for x in r['with'][:3])}: {r['text'][:100]}")
    total = sum(len(v) for v in dups.values())
    print("OK: the briefs of the variants share nothing" if not total else f"TOO SIMILAR: {total} shared runs in {len(dups)} briefs: the writers will echo them (rewrite the notes, see tools/longfu88/notes_diversify.py)")
    sys.exit(1 if total else 0)


def _shingles(args) -> None:
    """Exit code 1 when two texts share a run of `--n` or more words."""
    import fnmatch

    from . import shingles as S

    names = sorted({d.name for d in RUNS_DIR.iterdir() if d.is_dir() and any(fnmatch.fnmatch(d.name, pat) for pat in args.runs)})
    corpus: dict[str, list[tuple[str, str]]] = {}
    for name in names:
        final = RUNS_DIR / name / store.FINAL_JSON
        if final.exists():
            blocks = json.loads(final.read_text(encoding="utf-8"))["blocks"]
            corpus[name] = [(f"b{i + 1:02d} {b['heading']}", b["heading"] + "\n\n" + b["text"]) for i, b in enumerate(blocks)]
    if len(corpus) < 2:
        raise RuntimeError(f"need at least two finished texts (04_final.json), found {len(corpus)} for {args.runs}")
    from .protected import mask_for_runs

    mask = None if args.no_protected else mask_for_runs(corpus)
    dups = S.find_duplicates(corpus, args.n, mask)
    print(f"shingle {args.n}: {len(corpus)} texts compared" + ("" if mask is None else f" (protected facts of the knowledge base: {mask.size} phrases count as one word)"))
    for name, total, runs, words in S.summary(corpus, dups):
        print(f"  {name:28} {total:5} words  {runs:3} shared runs  {words:4} words inside ({100 * words / max(total, 1):.0f}%)")
        for r in dups.get(name, [])[:args.show]:
            print(f"      [{r['block'][:34]}] {r['words']}w with {','.join(x.rsplit('-', 1)[-1] if x.rsplit('-', 1)[-1].startswith('v') else x for x in r['with'][:4])}: {r['text'][:110]}")
    if args.json:
        args.json.write_text(json.dumps(dups, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"full report: {args.json}")
    total_runs = sum(len(v) for v in dups.values())
    print("OK: no technical duplicates" if not total_runs else f"FOUND {total_runs} shared runs in {len(dups)} texts")
    sys.exit(1 if total_runs else 0)


def _open_or_create(arg: str) -> Run:
    """A run name/path, or (convenience) an input file - then the run is created from it."""
    p = Path(arg)
    if p.is_file():
        job = load_job(p)
        slug = make_slug(job)
        existing = RUNS_DIR / slug / store.INPUT
        if existing.exists():  # never overwrite the input of another run that happens to get the same name
            old = json.loads(existing.read_text(encoding="utf-8"))
            new = job.to_dict()
            key = ("keywords", "competitors", "geo", "page_type", "casinos")
            if tuple(old.get(k, [] if k == "casinos" else "brand-review" if k == "page_type" else None) for k in key) != tuple(new[k] for k in key):
                raise RuntimeError(f"Run '{slug}' already exists with a different input; add `Slug - <name>` to the input file to name the new run.")
            return Run.open(slug)
        return Run.create(slug, job)
    return Run.open(arg)


def _make_llm(args, run: Run):
    return ManualLLM(run.path / "llm") if args.llm == "manual" else AnthropicLLM()


def _next_iter(run: Run) -> int:
    return len(list(run.path.glob("03_check_iter_*.json")))


if __name__ == "__main__":
    main()


