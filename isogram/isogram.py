



def validate_string(string):
    return "".join([letter for letter in string.lower() if letter.isalpha()])

# def isogram(string):

#     string = validate_string(string)

#     unique_letters = set()
#     for letter in string:
#         unique_letters.add(letter)
    
#     if len(unique_letters) == len(string):
#         return True
#     return False


word = "batt"


def isogram(word):
    # string = validate_string(string)
    count = 0
    for i, outer_letter in enumerate(word):
        for inner_letter in word[i+1:]:
            # import pdb; pdb.set_trace()
            if outer_letter == inner_letter:
                count += 1
    return count
            # if letters == letter:
            #     return False

print(isogram(word))