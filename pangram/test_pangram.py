from pangram import pangram


def test_empty_sentence():
    assert pangram("") == False


def test_sentence_without_spaces():
    assert pangram("thequickbrownfoxjumpsoverthelazydog") == True


def test_sentence_with_spaces():
    assert pangram("the quick brown fox jumps over the lazy dog") == True


def test_sentence_with_capital_letter():
    assert (
        pangram("We promptly judged antique ivory buckles for the next prize") == True
    )


def test_sentence_multiple_capital_letters():
    assert pangram("The Five Boxing Wizards Jump Quickly") == True


def test_sentence_with_punctuation():
    assert pangram("the quick brown fox jumps over the lazy dog.") == True


def test_sentence_with_capital_letter_and_punctuation():
    assert pangram("Pack my box with five dozen liquor jugs.") == True


def test_sentence_multiple_capital_letters_and_punctuation_marks():
    assert pangram("J.Q. Schwartz flung V.D. Pike my box!") == True


def test_sentence_with_capital_letter_is_not_pangram():
    assert pangram("The girls and boys went to school today") == False


def test_sentence_with_captital_letter_and_punctuation_is_not_pangram():
    assert pangram("Pack my box with a dozen liquor jugs.") == False
