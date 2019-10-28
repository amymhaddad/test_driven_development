from string import digits


def encode_decode(string):
    if string == "":
        return ""
    
    if encode(string):
        return encode(string)
    return decode(string)



def encode(string):

    duplicate_letter = ''
    letter_count = []

    for i, letter in enumerate(string):        
        
        if duplicate_letter == '' or letter in duplicate_letter:
            duplicate_letter += letter
            
        else:
            letter_count += str(len(duplicate_letter)) + duplicate_letter[0]
            duplicate_letter = letter
            
    letter_count.append(letter)   
            
    return "".join(letter_count)
  

def decode(string):
    return "".join([int(letter) * letter   for letter in string if letter in digits])

