from anagram import anagram


def test_no_anagrams():
    assert (anagram("nature", ["book", "job", "swimming", "desk"])) == []


def test_one_anagram():
    assert (anagram("listen", ["enlists", "google", "inlets"])) == ["inlets"]


def test_multiple_anagrams():
    assert (anagram("listen", ["enlists", "google", "silent", "inlets"])) == [
        "silent",
        "inlets",
    ]


def test_given_word_with_capitalized_letter():
    assert (anagram("Cat", ["folder", "act", "paper", "garbage"])) == ["act"]


def test_anagram_choices_with_capitalized_letters():
    assert (anagram("brag", ["Big", "Small", "Grab", "House'"])) == ["Grab"]


def test_given_word_uppercase():
    assert (anagram("SAVE", ["vase", "desk", "folder", "pens"])) == ["vase"]


def test_uppercase_anagram_choices():
    assert (anagram("save", ["DESK", "WATER", "VASE", "BALL"])) == ["VASE"]
