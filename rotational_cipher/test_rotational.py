from rotational import rotate

def test_rotate_by_0():
    assert rotate('a', 0) == 'a'

def test_rotate_by_5():
    assert rotate('omg', 5) == 'trl'

def test_rotate_by_26():
    assert rotate('Cool', 26) == 'Cool'

# def test_rotate_by_13():
#     assert rotate('The quick brown fox jumps over the lazy dog', 13) == 'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'
