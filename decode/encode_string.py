from validate import valid_string


def encode(string):

    string = valid_string(string)

    duplicate_letter = ""
    letter_count = []

    for i, letter in enumerate(string):

        if duplicate_letter == "" or letter in duplicate_letter:
            duplicate_letter += letter

        else:
            letter_count += str(len(duplicate_letter)) + duplicate_letter[0]
            duplicate_letter = letter

    if len(duplicate_letter) > 1:
        letter_count += str(len(duplicate_letter)) + duplicate_letter[0]
    else:
        letter_count.append(duplicate_letter)

    return "".join(letter_count)
