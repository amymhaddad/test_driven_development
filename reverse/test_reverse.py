from reverse import reverse


def test_string_lengths():
    assert len(reverse("cool")) == len("looc")


def test_empty_string():
    assert reverse("") == ""


def test_strings_contain_same_letters():
    assert set(reverse("flow")) == set("wolf")


def test_reverse_string():
    assert reverse("flow") == "wolf"


def test_string_with_capital_letter():
    assert reverse("Raw") == "war"


def test_palindromes():
    assert reverse("madam") == "madam"
