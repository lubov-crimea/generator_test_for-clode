"""Home pages of the SG sites: widget texts and internal links into runs/longfu88-sg-vNN/05_affbulk_config.json, then the page is rebuilt.

    python tools/longfu88/home_finalize.py [widgets] [links] [build]

widgets  runs/_sg_publish/home_widget_texts.json -> config hero label, promo disclaimer, review texts (other fields stay)
links    config `internal_links`: one anchor of at most 3 words for /bonuses, /login and /app, taken from the running text of the built page
build    python -m affbulk.build_page for every run
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8")

from affbulk.build_page import build_page  # noqa: E402
from affbulk.links import wrap_phrase  # noqa: E402

RUNS = [f"longfu88-sg-v{i:02d}" for i in range(1, 13)]
CANDIDATES = {
    "/bonuses": ["Longfu88 bonus", "welcome bonus", "welcome offer", "Casino Welcome Bonus", "bonuses", "bonus"],
    "/login": ["Longfu88 login", "log in", "login", "sign up", "registration", "sign-up"],
    "/app": ["Longfu88 app", "home screen shortcut", "home-screen shortcut", "mobile access", "mobile play", "on your phone", "phone"],
}


def cfg_path(run: str) -> Path:
    return Path("runs") / run / "05_affbulk_config.json"


def widgets() -> None:
    texts = json.loads(Path("runs/_sg_publish/home_widget_texts.json").read_text(encoding="utf-8"))
    for i, run in enumerate(RUNS, 1):
        t = texts[f"v{i:02d}"]
        c = json.loads(cfg_path(run).read_text(encoding="utf-8"))
        items = c["reviews"]["items"]
        assert len(items) == len(t["reviews"]), run
        c["hero"]["label"] = t["hero_label"]
        c["promo"]["disclaimer"] = t["disclaimer"]
        for it, txt in zip(items, t["reviews"]):
            it["review"] = txt
        cfg_path(run).write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
        print(run, "widgets written")


def links() -> None:
    for run in RUNS:
        c = json.loads(cfg_path(run).read_text(encoding="utf-8"))
        c.pop("internal_links", None)
        cfg_path(run).write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
        final = json.loads((Path("runs") / run / "04_final.json").read_text(encoding="utf-8"))
        content = build_page(final, c)["content"]
        chosen = []
        for href, cands in CANDIDATES.items():
            for ph in cands:
                try:
                    wrap_phrase(content, ph, href)
                except ValueError:
                    continue
                chosen.append({"anchor": ph, "href": href})
                break
            else:
                print(run, "NO ANCHOR for", href)
        c["internal_links"] = chosen
        cfg_path(run).write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
        print(run, [(x["anchor"], x["href"]) for x in chosen])


def build() -> None:
    for run in RUNS:
        subprocess.run([sys.executable, "-m", "affbulk.build_page", run], check=True, stdout=subprocess.DEVNULL)
        print(run, "built")


if __name__ == "__main__":
    steps = sys.argv[1:] or ["widgets", "links", "build"]
    for s in steps:
        {"widgets": widgets, "links": links, "build": build}[s]()
