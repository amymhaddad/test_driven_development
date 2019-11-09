def validate_string(string):
    return "".join([letter for letter in string.lower() if letter.isalpha()])


# Option 1 - use set()
def isogram(string):

    string = validate_string(string)

    unique_letters = set()
    for letter in string:
        unique_letters.add(letter)

    if len(unique_letters) == len(string):
        return True
    return False


# Option 2 = use for loop
def isogram(string):
    string = validate_string(string)
    count = 0
    for i, outer_letter in enumerate(string):
        for inner_letter in string[i + 1 :]:
            if outer_letter == inner_letter:
                count += 1
    return bool(count < 1)
