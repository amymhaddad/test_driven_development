from string import digits



#some of my tests will pass but they shouldn't


#fix encode() so it if gets ONLY the same values, it returns the proper count --> WWW == 3W

def encode(string):
  
    # string = valid_string(string)

    duplicate_letter = ''
    letter_count = []

    for i, letter in enumerate(string):  
        
        if duplicate_letter == '' or letter in duplicate_letter:
            duplicate_letter += letter
        
        if letter not in duplicate_letter:
            # import pdb; pdb.set_trace()
            letter_count += str(len(duplicate_letter)) + duplicate_letter[0]
            duplicate_letter = letter
            
    if len(duplicate_letter) > 1:
        letter_count += str(len(duplicate_letter)) + duplicate_letter[0]   
    else:
        letter_count.append(duplicate_letter)
    # import pdb; pdb.set_trace()
            
    return "".join(letter_count) 

print(encode("WWWB"))


def decode(string):
    return "".join([int(letter) * letter for letter in string if letter in digits])


# def valid_string(string):
#     new_string = ''
#     for character in string.split(" "):
#         if character.isalpha():
#             new_string += character.upper()
#         else:
#             new_string += character
#     return new_string
    
    
# print(valid_string(""))

