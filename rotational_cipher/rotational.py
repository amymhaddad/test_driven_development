
from string import ascii_lowercase as letters

def rotate(string, key):
    if key == 0:
        return string

    else:
        new = ''
        for outer_letter in string:
            for i, inner_letter in enumerate(letters):
                if inner_letter == outer_letter.lower():
                    # import pdb; pdb.set_trace()
                    if outer_letter.isupper():
                        new += letters[i+key%26].capitalize() 
                    else:
                        new += letters[i+key%26]
        return new

# print(rotate('The quick brown fox jumps over the lazy dog', 13))

#  'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'

#Create new function for phrases; use .split(" ") and a double for loop 