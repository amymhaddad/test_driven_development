from string import digits

def valid_string(string):
    new_string = ''
    for character in string:
        if character.isalpha():
            new_string += character.upper()
        else:
            new_string += character
    return new_string


def encode(string):
  
    string = valid_string(string)

    duplicate_letter = ''
    letter_count = []

    for i, letter in enumerate(string):  
        
        if duplicate_letter == '' or letter in duplicate_letter:
            duplicate_letter += letter
        
        else:
            letter_count += str(len(duplicate_letter)) + duplicate_letter[0]
            duplicate_letter = letter
            
    if len(duplicate_letter) > 1:
        letter_count += str(len(duplicate_letter)) + duplicate_letter[0]   
    else:
        letter_count.append(duplicate_letter)
    
    return "".join(letter_count) 


def decode(string):
    string = valid_string(string)
    index = 0

    encoded_string = []
    for letter in string:
        if letter in digits:
            encoded_string.append(int(letter) * string[index +1])

        elif string[index -1] in digits:  
            index += 1
            continue

        else:
            encoded_string.append(letter)
        index += 1
    return "".join(encoded_string)
