from scrabble import scrabble

def test_one_letter_word():
    assert scrabble('I') == 1

# def test_two_letter_word():
#     assert scrabble('of') == 5