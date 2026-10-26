"""Plants the internal links of the site (`Site pages` of the input, textgen/sitemap.py) in the ТЗ variants of a base run.

`python -m textgen variants` composes the blocks of a variant from the blueprint and does not carry the `internal_links` of the base
ТЗ (step 1.7 plants them only in the base run). This helper does for every variant what step 1.7 does for the base: it attaches each
page of `site_pages` to the first block (not the H1) whose heading or summary names the topic (optional links of a subpage), saves
`site_pages` and `internal_links` into 01_brief.json and renders 01_brief.md again (with the "Home link" and "Internal links" lines).
Idempotent. Run after `textgen variants`:

    python tools/longfu88/attach_links_variants.py longfu88-login-sg
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from textgen import brief as B  # noqa: E402
from textgen import store  # noqa: E402
from textgen.sitemap import attach_internal_links, site_pages_for  # noqa: E402
from textgen.store import Run  # noqa: E402


def main(base: str) -> None:
    runs = sorted(p for p in (ROOT / "runs").glob(f"{base}-v[0-9][0-9]") if p.is_dir())
    if not runs:
        sys.exit(f"no variants of {base}")
    for path in runs:
        run = Run(path)
        result = run.load_json(store.BRIEF)
        pages = site_pages_for(run.job())
        for b in result["blocks"]:
            b.pop("internal_links", None)
        placed = attach_internal_links(result, pages, required=False) if pages else {}
        if pages:
            result["site_pages"] = pages
        run.save_json(store.BRIEF, result)
        kb = run.knowledge_base()
        render = {"intent_summary": result["intent_summary"], "blocks": result["blocks"], "skipped_clusters": result.get("skipped_clusters", []),
                  "brand": result.get("brand"), "page_type": result.get("page_type"), "site_pages": result.get("site_pages", [])}
        run.save_text(store.BRIEF_MD, B.render_markdown(
            render, {"geo": result["geo"], "language": result["language"], "knowledge_base": kb["title"] if kb else None, "page_type": result.get("page_type")},
            result["targets"]))
        print(f"{path.name}: " + (", ".join(f"/{s} -> {bid}" for s, bid in placed.items()) or "no link planted"))


if __name__ == "__main__":
    main(sys.argv[1])
