def valid_string(string):
    new_string = ""
    for character in string:
        if character.isalpha():
            new_string += character.upper()
        else:
            new_string += character
    return new_string
