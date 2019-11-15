
from string import ascii_lowercase as letters


def rotate(string, key):
    if key == 0:
        return string

    else:
        new = ''
        for outer_letter in string:
            for i, inner_letter in enumerate(letters):
                shift_value = (i + key) %26
                if inner_letter == outer_letter.lower():
                    if outer_letter.isupper():
                        new += letters[shift_value].capitalize()
                    else:
                        new += letters[shift_value]        
        return new

# print(rotate('The', 13))

