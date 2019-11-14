# 

from string import ascii_lowercase as letters


# def rotate(string, key):

#     if key == 0:
#         return string
#     new = []
#     for i, outer_letter in enumerate(letters):
#         for inner_letter in string: 
#             if inner_letter == outer_letter:
#                 new.append(letters[i+key%26])
#     new.reverse()
#     return "".join(new)


# print(rotate('abc', 2))

# assert rotate('cool', 26) == 'cool'


string = 'omg'

key = 5

# new = ''
# for i, outer_letter in enumerate(letters):
#     for ii, inner_letter in enumerate(string):
#         if inner_letter == outer_letter:
#             print(letters[i+key])

def rotate(string, key):
    if key == 0:
        return string

    else:
        new = ''
        for i, outer_letter in enumerate(string):
            # import pdb; pdb.set_trace()
            for ii, inner_letter in enumerate(letters):
                if inner_letter == outer_letter:
                    new += letters[ii+key]
        return new

print(rotate(string, key))