from scrabble import scrabble


def test_no_word():
    assert scrabble("") == 0


def test_one_letter_word_uppercase():
    assert scrabble("I") == 1


def test_two_letter_word_lowercase():
    assert scrabble("of") == 5


def test_captialized_word():
    assert scrabble("Amy") == 8


def test_long_word():
    assert scrabble("cabbage") == 14
