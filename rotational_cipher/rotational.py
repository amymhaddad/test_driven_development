

from string import ascii_lowercase as letters

string = 'm'
rotate = 13


for i, letter in enumerate(letters):
    if letter == string:
        #add an index of 13 to string
        print(letters[i%26])