"""Brief variants (textgen/variants.py): composition from a base ТЗ and the keyword sentence of the notes."""
import pytest

from textgen.variants import (clean_notes, depth_difference, keyword_sentence, structure_conflicts, structure_distance, topic_profile,
                              topic_set)

BONUS_ALL = ["w.amount", "w.terms", "w.claiming"]


def _blk(heading, origin, refs=(), fmt=("paragraph",), mid=80, level=2):
    return {"heading": heading, "variant_origin": origin, "kb_refs": list(refs), "formats": list(fmt), "level": level,
            "words_min": round(mid * 0.88), "words_max": round(mid * 1.12)}


def _brief(*blocks):
    return {"blocks": list(blocks)}


def _base():
    return {"blocks": [{"id": "b01", "kb_refs": []}, {"id": "b02", "kb_refs": BONUS_ALL}, {"id": "b12", "kb_refs": []}]}


def test_topic_set_ignores_order_headings_and_merging():
    a = _brief(_blk("Intro", ["b01"]), _blk("Install", ["b03", "b04"]), _blk("FAQ", ["b12"]))
    b = _brief(_blk("Questions", ["b12"]), _blk("Start here", ["b01"]), _blk("Steps", ["b04"]), _blk("Setup", ["b03"]))
    assert topic_set(a) == topic_set(b) == {"b01", "b03", "b04", "b12"}


def test_same_topics_in_another_order_with_other_headings_are_too_close():
    a = _brief(_blk("Intro", ["b01"]), _blk("Bonus", ["b02"], BONUS_ALL), _blk("FAQ", ["b12"]))
    b = _brief(_blk("Questions", ["b12"]), _blk("Welcome offer", ["b02"], BONUS_ALL), _blk("Start", ["b01"]))
    out = structure_conflicts({"v01": a, "v02": b}, _base(), min_distance=2)
    assert len(out) == 1 and out[0].startswith("v01 / v02: structure distance 0.0 < 2")


def test_a_topic_that_only_one_variant_covers_counts_one_and_new_blocks_count_by_heading():
    a = _brief(_blk("Intro", ["b01"]), _blk("FAQ", ["b12"]))
    b = _brief(_blk("Intro", ["b01"]), _blk("FAQ", ["b12"]), _blk("Sports on a phone", ["new"]))
    c = _brief(_blk("Intro", ["b01"]), _blk("FAQ", ["b12"]), _blk("Phone sports", ["new"]))
    assert structure_distance(topic_profile(a), topic_profile(b))[:2] == (1.0, 1)
    assert structure_distance(topic_profile(b), topic_profile(c))[1] == 2  # a differently named new block is another topic


def test_depth_of_the_same_topic_counts_amount_only_versus_full_conditions():
    amount = _brief(_blk("Welcome bonus", ["b02"], ["w.amount"], mid=40))
    full = _brief(_blk("Welcome bonus", ["b02"], BONUS_ALL, ("paragraph", "list"), mid=110))
    total, only, depth, top = structure_distance(topic_profile(amount, _base()), topic_profile(full, _base()))
    assert only == 0 and total > 0.7 and top and top[0].startswith("b02: facts")
    # the other facts, the format and the size each add to the difference; nothing differs -> 0
    same = depth_difference(topic_profile(full, _base())["b02"], topic_profile(full, _base())["b02"])
    assert same[0] == 0


def test_a_merged_block_is_compared_per_topic_with_its_own_facts_only():
    merged = _brief(_blk("Bonus and FAQ", ["b02", "b12"], BONUS_ALL, mid=100))
    separate = _brief(_blk("Bonus", ["b02"], BONUS_ALL, mid=50), _blk("FAQ", ["b12"], mid=50))
    prof_m, prof_s = topic_profile(merged, _base()), topic_profile(separate, _base())
    assert prof_m["b02"]["facts"] == prof_s["b02"]["facts"] == set(BONUS_ALL)
    assert prof_m["b02"]["words"] == 50


def test_keyword_sentence_counts_and_other_keywords():
    kw = {"Incaspin": 2, "Inca Spin": 0, "Incaspin casino": 1}
    s = keyword_sentence(kw, ["paragraph"], [], False, "")
    assert s == 'Use "Incaspin" exactly twice and "Incaspin casino" (written as the name Incaspin Casino) exactly once, and no other tracked keyword.'
    all_three = keyword_sentence({"Incaspin": 1, "Inca Spin": 1, "Incaspin casino": 1}, ["paragraph"], [], False, "")
    assert all_three.endswith("exactly once.") and "no other" not in all_three
    s = keyword_sentence({"Incaspin": 3, "Inca Spin": 0, "Incaspin casino": 0}, ["paragraph", "table"], [], False, "")
    assert s.startswith('Use "Incaspin" exactly three times, and no other tracked keyword.')
    assert "table cells" in s


def test_keyword_sentence_without_keywords_and_lists_ok():
    assert keyword_sentence({"Incaspin": 0}, ["list"], [], False, "") == "Use no tracked keyword in the body of this block."
    s = keyword_sentence({"Incaspin": 1}, ["list"], ["Note."], True, "Tail.")
    assert "table cells" not in s and s.endswith("Note. Tail.")


def test_clean_notes_drops_old_keyword_sentences_but_keeps_rulings():
    b = {"id": "b11", "copywriter_notes": 'Name a selection of slots. Explain a mechanic. Use "Incaspin" exactly once; do not write the brand name in the titles of games.'}
    assert clean_notes(b) == "Name a selection of slots. Explain a mechanic. Do not write the brand name in the titles of games."


def test_clean_notes_intrinsic_sentences_are_rewritten():
    b = {"id": "b21", "copywriter_notes": 'State the channels. Print the e-mail address exactly as given (support@incaspin.com): it contains the tracked keyword and is the one occurrence of "Incaspin" of this block. No other tracked keyword.'}
    out = clean_notes(b)
    assert "one occurrence" not in out and "support@incaspin.com" in out


def test_clean_notes_fails_loudly_when_the_base_notes_changed():
    with pytest.raises(ValueError):
        clean_notes({"id": "b02", "copywriter_notes": "The base notes were rewritten."})
