from decode_encode import encode 

def test_encode_string_same_letter_all_caps():
    return encode('WWW') == "3W"

def test_encode_string_multiple_letters_all_caps():
    return encode('WWWBBB') == "3W3B"

def test_encode_string_multiple_letters_with_single_letter_all_caps():
    return encode('WWWB') == "3WB"