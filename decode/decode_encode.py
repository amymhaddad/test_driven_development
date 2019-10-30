from string import digits



#tests passing automatically



def valid_string(string):
    new_string = ''
    for character in string.split(" "):
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

    update_string = []
    for letter in string:
        # import pdb; pdb.set_trace()
        if letter in digits:
            update_string.append(int(letter))
        else:
            update_string.append(letter)
   
    new = []
    for i, item in enumerate(update_string):
        if item == isinstance(item, int):
    
            new.append(item * update_string[i+1:i+2])
    
        # new.append(item)
        
    print(new)
    # return "".join(update_string)

    # return "".join([int(letter) * letter for letter in string if letter in digits])

print(decode("3W"))

# "WWWBWWWCBB"
    
    
# print(valid_string(""))

