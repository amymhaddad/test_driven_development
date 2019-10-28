from decode_encode import encode, decode 


def test_encode_empty_string():
    return encode("") == ""

def test_encode_string_same_letter():
    return encode("WWW") == "3W"

def test_encode_string_multiple_different_letters():
    return encode("WWWBBB") == "3W3B"

def test_encode_string_multiple_same_letters_with_single_unique_letter():
    return encode("WWWB") == "3WB"

def test_endcode_string_multiple_same_letters_and_muliple_single_unique_letters():
    return encode("WWWBWWWCBB") == "3WB3WC2B"

def test_encode_long_diverse_string():
    return encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB") == "12WB12W3B24WB"

def test_decode_empty_string():
    return decode("") == ""

def test_decode_string_same_letter():
    return decode("3W") == "WWW"

def test_decode_string_multiple_different_letters():
    return decode("3W3B") == "WWWBBB"

def test_decode_string_multiple_same_letters_with_single_unique_letter():
    return decode("3WB") == "WWWB"

def test_decode_string_multiple_same_letters_and_multiple_single_unique_letters():
    return decode("3WB3WC2B") == "WWWBWWWCBB"


