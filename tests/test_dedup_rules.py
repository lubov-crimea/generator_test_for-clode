import json

from textgen import paraphrase as P
from textgen.config import Settings
from textgen.checks import check_shingles
from textgen.inputs import Job
from textgen.lexical import brief_corpus, lexical_conflicts
from textgen.protected import Mask, protected_phrases
from textgen.shingles import tokens
from textgen.siblings import sibling_corpus, sibling_names

STEP = "Register an account and complete the required personal details."
KB = {"variables": {"promo": {
    "name": "Casino Weekly Reload",
    "reward": "50 Free Spins",
    "wagering": "40x winnings from Free Spins",
    "claiming": [STEP, "Make the first qualifying deposit of at least €30 within seven days."],
    "providers": ["Evolution", "NetEnt", "Pragmatic Play", "Yggdrasil"],
    "levels": [{"level": 1, "points": 10}, {"level": 2, "points": 30}, {"level": 3, "points": 90}],
}}}
GOOD = [f"Open an account first and fill in the personal details that the form asks for, wording {i} {w}" for i, w in enumerate("alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu".split())]


def mask():
    return Mask(protected_phrases(KB, "Longfu88"))


def test_sentences_of_a_knowledge_base_are_the_ones_to_paraphrase():
    sents = P.sentences_of(KB)
    assert set(sents.values()) == {STEP, "Make the first qualifying deposit of at least €30 within seven days."}


def test_paraphrase_must_keep_figures_and_not_invent_or_copy():
    s = "Make the first qualifying deposit of at least €30 within seven days."
    ok = "Within seven days the player funds the account with a first qualifying payment of €30 or more."
    assert P.validate_paraphrase(s, ok, mask()) == []
    assert any("figure lost" in e for e in P.validate_paraphrase(s, "Within seven days the player makes a first qualifying payment.", mask()))
    assert any("invented" in e for e in P.validate_paraphrase(s, "Within seven days make a first qualifying payment of at least €30 or 50 more.", mask()))
    assert any("shares" in e for e in P.validate_paraphrase(s, "Make the first qualifying deposit of at least €30 within eight days.", mask()))


def test_cards_use_the_slot_of_the_variant_and_keep_protected_values_exact():
    bank = {"slots": 3, "items": {P.text_key(STEP): {"text": STEP, "paraphrases": ["one wording of the registration step", "second wording", "third wording"]}}}
    c1 = P.Cards(KB, mask(), bank, slot=1, seed="run-a")
    c2 = P.Cards(KB, mask(), bank, slot=2, seed="run-a")
    v = KB["variables"]["promo"]
    assert "second wording" in c1.render_value("promo.claiming", v["claiming"])
    assert "third wording" in c2.render_value("promo.claiming", v["claiming"])
    assert STEP not in c1.render_value("promo.claiming", v["claiming"])
    assert "Casino Weekly Reload" in c1.render_value("promo.name", v["name"]) and "50 Free Spins" in c1.render_value("promo.reward", v["reward"])
    assert c1.missing  # the second sentence has no entry in the bank
    try:
        P.Cards(KB, mask(), bank, slot=0, seed="x", require=True).render_value("promo.claiming", v["claiming"])
        raise AssertionError("require_bank must stop")
    except RuntimeError:
        pass


def test_unordered_lists_get_the_order_of_the_run_ordered_ones_do_not():
    c = P.Cards(KB, mask(), {"items": {}}, slot=0, seed="s1")
    d = P.Cards(KB, mask(), {"items": {}}, slot=0, seed="s2")
    prov = KB["variables"]["promo"]["providers"] * 3
    a, b = json.loads(c.render_value("promo.providers", prov)), json.loads(d.render_value("promo.providers", prov))
    assert sorted(a) == sorted(b) == sorted(prov) and a != b
    assert json.loads(c.render_value("promo.providers", prov)) == a  # deterministic
    lv = KB["variables"]["promo"]["levels"]
    assert json.loads(c.render_value("promo.levels", lv)) == lv
    assert json.loads(c.render_value("promo.claiming_steps", ["a b", "c d", "e f"])) == ["a b", "c d", "e f"]


def _make_run(tmp, name, text, brand="Longfu88", geo="SG"):
    d = tmp / name
    d.mkdir()
    job = Job(geo=geo, keywords=[brand], competitors=[], knowledge_base="kb", brand=brand)
    (d / "00_input.json").write_text(json.dumps(job.to_dict()), encoding="utf-8")
    (d / "04_final.json").write_text(json.dumps({"blocks": [{"heading": "H", "text": text}]}), encoding="utf-8")
    return d


def test_siblings_share_brand_geo_and_knowledge_base(tmp_path):
    me = _make_run(tmp_path, "a-v01", "text of a")
    _make_run(tmp_path, "a-v02", "text of b")
    _make_run(tmp_path, "other", "text of c", geo="MY")
    assert sibling_names(me) == ["a-v02"]
    assert list(sibling_corpus(me)) == ["a-v02"]


def test_check_shingles_reports_a_run_shared_with_a_sibling(tmp_path):
    me = _make_run(tmp_path, "a-v01", "x")
    _make_run(tmp_path, "a-v02", "Players can claim the offer after they register an account and finish the form.")
    s = Settings.load()
    bad = check_shingles("b01", "Whoever wants it can claim the offer after they register an account and finish the form today.", me, s)
    assert bad and bad[0]["check"] == "shingle"
    assert check_shingles("b01", "The offer is available once the account exists and the form is done.", me, s) == []


def test_lexical_gate_finds_notes_shared_by_two_variant_briefs(tmp_path):
    for v, notes in (("v01", "Open with the welcome offer and say that the page is written for players from Singapore."),
                     ("v02", "Open with the welcome offer and say that the page is written for readers in Singapore."),
                     ("v03", "Start from the money side: the match percentage, the cap and the free spins come first.")):
        d = tmp_path / f"base-{v}"
        d.mkdir()
        brief = {"intent_summary": "A page about the offer.", "blocks": [{"id": "b01", "summary": "Summary " + v, "copywriter_notes": notes + ' Use "Longfu88" exactly twice.',
                                                                         "entity_connections": []}]}
        (d / "01_brief.json").write_text(json.dumps(brief), encoding="utf-8")
    dups, words = lexical_conflicts("base", tmp_path, 6)
    assert set(dups) == {"base-v01", "base-v02"} and set(words) == {"base-v01", "base-v02", "base-v03"}
    assert [t for _, t in brief_corpus(brief)][1].count("exactly twice") == 0  # the sentences written by code are not compared
