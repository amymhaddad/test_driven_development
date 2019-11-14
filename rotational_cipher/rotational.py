
from string import ascii_lowercase as letters

def rotate(string, key):
    if key == 0:
        return string

    else:
        new = ''
        for outer_letter in string:
            for i, inner_letter in enumerate(letters):
                if inner_letter == outer_letter.lower():
                    if outer_letter.isupper():
                        new += letters[i+key%26].capitalize()
                    else:
                        new += letters[i+key%26]
        return new

# print(rotate(string, key)