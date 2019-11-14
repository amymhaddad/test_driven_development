from rotational import rotate

def test_rotate_by_0():
    assert rotate('a', 0) == 'a'

def test_rotate_by_5():
    assert rotate('omg', 5) == 'trl'

def test_rotate_by_26():
    assert rotate('cool', 26) == 'cool'
