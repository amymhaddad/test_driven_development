from raindrops import raindrops


def test_number_with_factor_3():
    assert raindrops(3) == "Pling"


def test_number_with_factor_5():
    assert raindrops(5) == "Plang"


def test_number_with_factor_7():
    assert raindrops(7) == "Plong"


def test_number_is_0():
    assert raindrops(0) == ""


def test_number_multiple_of_28():
    assert raindrops(28) == "Plong"


def test_number_multiple_of_12():
    assert raindrops(12) == "Pling"


def test_number_multiple_of_10():
    assert raindrops(10) == "Plang"


def test_number_with_no_matching_factors():
    assert raindrops(34) == "34"


def test_number_with_factors_3_and_5():
    assert raindrops(15) == "PlingPlang"


def test_number_with_factors_3_and_7():
    assert raindrops(21) == "PlingPlong"


def test_number_with_factors_5_and_7():
    assert raindrops(35) == "PlangPlong"


def test_number_with_factors_3_5_7():
    assert raindrops(105) == "PlingPlangPlong"
