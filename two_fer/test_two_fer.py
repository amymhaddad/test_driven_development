from two_fer import two_fer


def test_function_name_alice():
    assert two_fer(name="Alice") == "One for Alice, two for me"


def test_function_name_jim():
    assert two_fer(name="Bob") == "One for Bob, two for me"


def test_function_no_name():
    assert two_fer() == "One for you, two for me"
