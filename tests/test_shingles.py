from textgen.protected import Mask, is_protected_leaf, protected_phrases, unmask_text
from textgen.shingles import find_duplicates, taken_phrases, tokens


def test_tokens_ignore_markdown_and_punctuation():
    assert tokens("**Up to €2,088** + 18 Free-Spins!") == ["up", "to", "2,088", "18", "free", "spins"]


def test_shared_run_of_six_words_is_found_and_merged():
    a = {"A": [("b01", "Open the site and select Register today, then wait.")]}
    b = {"B": [("b01", "Players open the site and select Register before anything else.")]}
    d = find_duplicates({**a, **b}, n=6)
    assert set(d) == {"A", "B"}
    assert d["A"][0]["text"] == "open the site and select register"
    assert d["A"][0]["with"] == ["B"] and d["B"][0]["with"] == ["A"]


def test_five_shared_words_are_not_a_duplicate():
    corpus = {"A": [("b01", "open the site and select it")], "B": [("b01", "open the site and select that")]}
    assert find_duplicates(corpus, n=6) == {}


def test_longer_run_is_one_run_and_blocks_are_not_crossed():
    a = {"A": [("b01", "one two three four five six seven eight nine"), ("b02", "alpha beta gamma delta epsilon")]}
    b = {"B": [("b05", "one two three four five six seven eight nine"), ("b06", "zeta alpha beta gamma delta epsilon")]}
    d = find_duplicates({**a, **b}, n=6)
    assert [r["words"] for r in d["A"]] == [9]
    assert "alpha" not in d["A"][0]["text"]


def test_repeat_inside_one_text_is_ignored():
    corpus = {"A": [("b01", "one two three four five six. one two three four five six.")]}
    assert find_duplicates(corpus, n=6) == {}


KB = {"variables": {"promo": {
    "name": "Casino Double Fortune: One-Day Reload Special",
    "reward": "50% up to €500",
    "claiming": ["Register an account and complete the required personal details.", "Make the first qualifying deposit."],
    "languages": ["English", "Simplified Chinese"],
}}}


def test_protected_leaves_are_names_and_short_facts_not_sentences():
    assert is_protected_leaf("name", "Casino Double Fortune: One-Day Reload Special")
    assert is_protected_leaf("reward", "50% up to €500")
    assert not is_protected_leaf("claiming", "Register an account and complete the required personal details.")
    ph = protected_phrases(KB, brand="Longfu88")
    assert ("simplified", "chinese") in ph and ("longfu88",) in ph and ("50", "up", "to", "500") in ph
    assert not any(p[:2] == ("register", "an") for p in ph)


def test_mask_makes_a_protected_phrase_one_word_so_names_alone_are_no_duplicate():
    mask = Mask(protected_phrases(KB, brand="Longfu88"))
    name = "Casino Double Fortune One-Day Reload Special"
    a = {"A": [("b01", f"The {name} pays 50% up to €500 on a Friday.")]}
    b = {"B": [("b01", f"Players can use {name} with 50% up to €500 every week.")]}
    assert find_duplicates({**a, **b}, n=6) != {}  # unmasked: the name and the figure are a long shared run
    assert find_duplicates({**a, **b}, n=6, mask=mask) == {}  # masked: three words only
    c = {"C": [("b01", f"Here the {name} is the offer that rewards the first qualifying deposit of the week.")]}
    d = {"D": [("b01", f"Another page says the {name} is the offer that rewards the first qualifying deposit.")]}
    got = find_duplicates({**c, **d}, n=6, mask=mask)
    assert got and "casino double fortune one day reload special is the offer that" in got["C"][0]["text"]
    assert unmask_text(mask(tokens(name))) == "casino double fortune one day reload special"


def test_taken_phrases_lists_widespread_runs_first():
    texts = {f"S{i}": [("b01", "The casino is meant for players aged 18 or over, and this page is for readers. Unique %d words here now." % i)] for i in range(3)}
    got = taken_phrases(texts, n=6)
    assert got and got[0].startswith("the casino is meant for players")


def test_default_shingle_is_nine():
    from textgen.config import Settings
    from textgen.shingles import DEFAULT_N

    assert DEFAULT_N == 9 and Settings.load().shingle_n == 9

    base = 'alpha beta gamma delta epsilon zeta eta theta'
    a = {'a': [('b1', base + ' iota kappa')]}
    b = {'b': [('b1', base + ' lambda mu')]}
    assert find_duplicates({**a, **b}) == {}  # 8 shared words are not a duplicate at 9
    c = {'c': [('b1', base + ' iota')]}
    d = {'d': [('b1', base + ' iota')]}
    assert find_duplicates({**c, **d}) != {}

