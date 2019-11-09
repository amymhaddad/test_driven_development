from isogram import isogram


def test_short_word_is_isogram():
    assert isogram("cat") == True


def test_long_word_is_isogram():
    assert isogram("lumberjacks") == True


def test_long_word_is_not_isogram():
    assert isogram("isograms") == False


def test_phrase_with_spaces_is_isogram():
    assert isogram("if only") == True


def test_phrase_with_hyphens():
    assert isogram("six-year-old") == True


def test_phrase_with_mixed_case():
    assert isogram("Emily Jung") == True
