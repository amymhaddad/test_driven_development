from string import digits, punctuation
import re


def word_count(phrase):
    """Count the words in a given phrase"""

    phrase = validate_phrase(phrase)
    word_count_dictionary = {}

    if len(phrase) < 1:
        return 0

    for word in phrase.split(" "):
        if "\'" in word:
            word_count_dictionary[word] = 2
        else:
            word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
    return word_count_dictionary


def validate_phrase(phrase):
    """Remove punctuation and digits; lowercase all words"""
    
    
   
    updated_phrase = []
    
    for words in phrase.lower().split(" "):
        space = re.match(r'\s+', words)
        
        if space:
            # updated_phrase.append(re.sub("[\s+]", "", words))
            continue
        elif "\'" in words:
            updated_phrase.append(words)
        elif words in digits or words in punctuation:
            updated_phrase.append(re.sub("[\W\d]", " ", words))  
        else:
            updated_phrase.append(words)
    return " ".join(updated_phrase) 


phrase = " like spaces 12     !"
# # # # 
print(validate_phrase(phrase))