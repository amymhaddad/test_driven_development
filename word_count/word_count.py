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
    # space = re.search(r'\s+', words)
    # updated_phrase.append(re.sub("[\s*]", "", words).strip())
    
    updated_phrase = []
    
    for words in phrase.lower().split(" "):
        # import pdb; pdb.set_trace()

        #Not catching spaces, nor is words.isspace(), nor does '\s*'
        if words == " ":
            continue
        elif "\'" in words or words.isalpha():
            updated_phrase.append(words)
        else:
            updated_phrase.append(re.sub("[\W*\d*]", " ", words).strip())
        
    return " ".join(updated_phrase) 


phrase = "I    like spaces   !."
print(word_count(phrase))