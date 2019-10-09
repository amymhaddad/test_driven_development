from isbn import isbn


def test_empty_string_of_numbers():
    number = ""
    assert isbn(number) == False


def test_isbn_not_correct_length():
    number = "35982150"
    assert isbn(number) == False


def test_isbn_ends_with_X():
    number = "359821507X"
    assert isbn(number) == True


def test_isbn_without_hyphens():
    number = "3598215088"
    assert isbn(number) == True


def test_isbn_with_hypens():
    number = "3-598-21507-X"
    assert isbn(number) == True
