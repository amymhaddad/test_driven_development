from decode_encode import encode 

def test_encode_string_same_letter_all_caps():
    return encode('WWW') == "3W"