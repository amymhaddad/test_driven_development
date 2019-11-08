



def validate_string(string):
    return "".join([letter for letter in string.lower() if letter.isalpha()])

def isogram(string):

    string = validate_string(string)

    unique_letters = set()
    for letter in string:
        unique_letters.add(letter)
    
    if len(unique_letters) == len(string):
        return True
    return False
