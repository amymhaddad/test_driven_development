from armstrong import armstrong


def test_single_digit_number_is_armstrong():
    assert armstrong(9) == True


def test_double_digit_number_is_not_armstrong():
    assert armstrong(10) == False


def test_triple_digit_number_is_armstrong():
    assert armstrong(153) == True


def test_triple_digit_number_is_not_armstrong():
    assert armstrong(154) == False


def test_four_digit_number_is_armgstrong():
    assert armstrong(9474) == True
