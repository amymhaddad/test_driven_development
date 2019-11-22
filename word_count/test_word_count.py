from word_count import word_count


def test_no_words():
    assert word_count("") == 0


def test_count_single_word():
    assert word_count("word") == {"word": 1}


def test_two_words_separated_by_single_space():
    assert word_count("two words") == {"two": 1, "words": 1}


def test_repeated_words_separated_by_single_space():
    assert word_count("house house dog") == {"house": 2, "dog": 1}


def test_words_with_capital_letters():
    assert word_count("My name is Jill and my home is in Boston") == {
        "my": 2,
        "name": 1,
        "is": 2,
        "jill": 1,
        "and": 1,
        "home": 1,
        "in": 1,
        "boston": 1,
    }


def test_words_with_punctuation():
    assert word_count("My name is Jill, and my home is in Boston!") == {
        "my": 2,
        "name": 1,
        "is": 2,
        "jill": 1,
        "and": 1,
        "home": 1,
        "in": 1,
        "boston": 1,
    }


def test_words_with_apostrophes():
    assert word_count("I'm going to move to Florida.") == {
        "i'm": 2,
        "going": 1,
        "to": 2,
        "move": 1,
        "florida": 1,
    }


def test_hyphenated_words():
    assert word_count("That medicine is fast-acting.") == {
        "that": 1,
        "medicine": 1,
        "is": 1,
        "fast": 1,
        "acting": 1,
    }


def test_phase_with_numbers():
    assert word_count("I am 12 years old.") == {"i": 1, "am": 1, "years": 1, "old": 1}
