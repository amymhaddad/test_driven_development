

def encode(string):

    duplicate_letter = ''
    letter_count = []
    count = 0

    for i, letter in enumerate(string):        
        # import pdb; pdb.set_trace()
        
        if not duplicate_letter:
            duplicate_letter += letter
            count += 1

        elif letter in duplicate_letter:
            duplicate_letter += letter
            count += 1
            
        else:     
            letter_count.append(str(count))
            letter_count.append(duplicate_letter[0])
            letter_count.append(letter)
        
        letter = duplicate_letter 
            
    return "".join(letter_count)
       

    # return "3W"

print(encode('WWWBWWW'))

