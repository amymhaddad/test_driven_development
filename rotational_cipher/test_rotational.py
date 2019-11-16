from rotational import rotate

def test_rotate_letter_by_0():
    assert rotate('a', 0) == 'a'

def test_rotate_letters_by_5():
    assert rotate('omg', 5) == 'trl'

def test_rotate_word_with_captial_letter_by_26():
    assert rotate('Cool', 26) == 'Cool'

def test_rotate_sentence_by_13_version1():
    assert rotate('The quick brown fox jumps over the lazy dog.', 13) == 'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'

def test_rotate_sentence_by_13_version2():
    assert rotate('Gur dhvpx oebja sbk whzcf bire gur ynml qbt.', 13) == 'The quick brown fox jumps over the lazy dog.'
