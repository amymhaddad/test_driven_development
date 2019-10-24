

def encode(string):

    duplicate_letter = ''
    letter_count = []
    # count = 0

    for i, letter in enumerate(string):        
        
        if duplicate_letter == '' or letter in duplicate_letter:
            # import pdb; pdb.set_trace()
            duplicate_letter += letter
            
            
        elif letter not in duplicate_letter:
            letter_count.append(len(duplicate_letter))
            letter_count.append(duplicate_letter[0])
            duplicate_letter = letter
            
    letter_count.append(letter)   
            
                
               
        

    return letter_count
       


print(encode('WWB'))

