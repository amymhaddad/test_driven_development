

def encode(string):

    duplicate_letter = ''
    letter_count = []

    for i, letter in enumerate(string):        
        
        if duplicate_letter == '' or letter in duplicate_letter:
            duplicate_letter += letter
            
        else:
            letter_count.append(str(len(duplicate_letter)))
            letter_count.append(duplicate_letter[0])
            duplicate_letter = letter
            
    letter_count.append(letter)   
            
    return "".join(letter_count)
  
# print(encode('WWB'))

from string import digits

def decode(string):
    decoded_string = []
    
    for letter in string:
        if letter in digits:
            number = int(letter)

    decoded_string.append(number * letter)

    return "".join(decoded_string)


print(decode("3W3B"))

#  return decode("3W") == "WWW"

