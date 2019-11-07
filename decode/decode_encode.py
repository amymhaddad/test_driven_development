from string import digits
from decode_string import decode
from encode_string import encode


def main(string):

    for character in string:
        if character in digits:
            return decode(string)
        else:
            return encode(string)


if __name__ == "__main__":
    main(string)
