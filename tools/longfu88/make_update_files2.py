"""Second batch (local-language pages): from runs/<run>/05_affbulk_config.json + 05_affbulk_page.json writes
   05_affbulk_update.json  (data of pages_update: seo, keywords, tableOfContent, content, customHeadHTML) for pages that exist,
   05_affbulk_create.json  (data of pages_create: the whole page) for pages that do not exist yet (page_id is null).
Both are compact JSON.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
for geo in ("indonesia", "malaysia", "vietnam", "thailand", "singapore"):
    for v in ("v01", "v02", "v03", "v04"):
        run = f"longfu88-{geo}-{v}"
        cfg = json.loads((ROOT / "runs" / run / "05_affbulk_config.json").read_text(encoding="utf-8"))
        page = json.loads((ROOT / "runs" / run / "05_affbulk_page.json").read_text(encoding="utf-8"))
        assert page["website"] == cfg["website_id"] and page["slug"] == cfg["slug"], run
        for f in ("05_affbulk_update.json", "05_affbulk_create.json"):
            (ROOT / "runs" / run / f).unlink(missing_ok=True)
        if cfg["page_id"]:
            data = {k: page[k] for k in ("seo", "keywords", "tableOfContent", "content", "customHeadHTML")}
            name = "05_affbulk_update.json"
        else:
            data = page
            name = "05_affbulk_create.json"
        (ROOT / "runs" / run / name).write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(run, cfg["domain"], "site", cfg["website_id"], "page", cfg["page_id"], name, len(json.dumps(data, ensure_ascii=False).encode("utf-8")))
