"""Splits every runs/<run>/05_affbulk_page.json into the data of pages_update (05_affbulk_update.json: seo, keywords, tableOfContent, content).
The website id of each page is checked against tools/longfu88/domains.json.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
for e in json.loads((ROOT / "tools/longfu88/domains.json").read_text(encoding="utf-8")):
    run = f"longfu88-{e['geo']}-{e['variant']}"
    page = json.loads((ROOT / "runs" / run / "05_affbulk_page.json").read_text(encoding="utf-8"))
    assert page["website"] == e["website_id"], (run, page["website"])
    upd = {k: page[k] for k in ("seo", "keywords", "tableOfContent", "content")}
    (ROOT / "runs" / run / "05_affbulk_update.json").write_text(json.dumps(upd, ensure_ascii=False), encoding="utf-8")
    print(run, e["domain"], "site", e["website_id"], "page", e["page_id"], "update-bytes", len(json.dumps(upd, ensure_ascii=False).encode("utf-8")))
