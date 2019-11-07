from string import digits
from validate import valid_string


def decode(string):
    string = valid_string(string)
    index = 0

    encoded_string = []
    for letter in string:
        if letter in digits:
            encoded_string.append(int(letter) * string[index + 1])

        elif string[index - 1] in digits:
            index += 1
            continue

        else:
            encoded_string.append(letter)
        index += 1
    return "".join(encoded_string)
