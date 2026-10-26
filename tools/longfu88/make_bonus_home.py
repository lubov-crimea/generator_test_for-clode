"""Home pages of the Longfu88 MY sites with ONE internal link to /bonuses. Run from the project root:
    python tools/longfu88/make_bonus_home.py
For each variant: runs/longfu88-my-vNN/05_affbulk_update_app.json (home content with the /login and /app links) -> an existing phrase of the
first welcome/bonus section is wrapped in <a href="/bonuses">, no word is added or removed -> 05_affbulk_update_bonus.json. The previous
payload stays as it is. Nothing is written to AffBulk here."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HREF = "/bonuses"
ANCHORS = {
    "v01": "Longfu88 bonus", "v02": "Casino Welcome Bonus", "v03": "Longfu88 bonus", "v04": "Longfu88 bonus",
    "v05": "first deposit casino bonus", "v06": "Casino Welcome Bonus", "v07": "first-deposit offer", "v08": "Casino Welcome Bonus",
}


def inside_link(p: str, phrase: str) -> bool:
    for m in re.finditer(r"<a\b.*?</a>", p, re.S):
        if phrase in m.group(0):
            return True
    return False


def wrap(content: list[dict], phrase: str) -> tuple[list[dict], str]:
    out = json.loads(json.dumps(content))
    for b in out:
        if b["__component"] != "blocks.article":
            continue
        head = re.search(r"<h[23]>(.*?)</h[23]>", b["article"])
        if not head or not re.search(r"welcome|bonus|offer", head.group(1), re.I):
            continue
        for p in re.findall(r"<p>.*?</p>", b["article"], re.S):
            if phrase in p and not inside_link(p, phrase):
                b["article"] = b["article"].replace(p, p.replace(phrase, f'<a href="{HREF}">{phrase}</a>', 1), 1)
                return out, head.group(1)
    raise ValueError(f"phrase not found: {phrase!r}")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    for vid, phrase in ANCHORS.items():
        home = ROOT / "runs" / f"longfu88-my-{vid}"
        content = json.loads((home / "05_affbulk_update_app.json").read_text(encoding="utf-8"))["content"]
        assert HREF not in json.dumps(content), vid
        new, where = wrap(content, phrase)
        (home / "05_affbulk_update_bonus.json").write_text(json.dumps({"content": new}, ensure_ascii=False), encoding="utf-8")
        print(f"{vid}: anchor {phrase!r} in the section {where!r}")


if __name__ == "__main__":
    main()
