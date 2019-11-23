from string import digits 
import re


def word_count(phrase):
    """Count the words in a given phrase"""

    # phrase = validate_phrase(phrase)
    word_count_dictionary = {}



    if len(phrase) < 1:
        return 0

    for word in phrase.split(" "):
        
        # apostrophe = re.sub("\'", "", phrase)
        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
    return word_count_dictionary


def validate_phrase(phrase):
    """Remove punctuation and digits; lowercase all words"""

    # apostrophe = re.findall(r"\'", phrase)        
   
    updated_phrase = []
    for words in phrase.lower().split(" "):
        # import pdb; pdb.set_trace()
        if words.isalpha():
            updated_phrase.append(words)
        elif words.isdigit():
            continue
        elif "\'" in words:
            updated_phrase.append(words)
        else:

            only_words = re.sub("\W", " ", words)
            updated_phrase.append(only_words.strip())
        
        
    
    return " ".join(updated_phrase).strip()


phrase = "I'm jere.@! and fast-acting"
# # # 
print(validate_phrase(phrase))