

def encode(string):

    duplicate_letter = ''
    letter_count = ''
    count = 0

    for i, letter in enumerate(string):
        # import pdb; pdb.set_trace()
        
        if not duplicate_letter:

            duplicate_letter += letter
            count += 1

        elif letter in duplicate_letter:
            duplicate_letter += letter
            count += 1
        
        # elif letter not in duplicate_letter:
        #     letter_count += 
        return duplicate_letter
       

    # return "3W"

print(encode('WWW'))

