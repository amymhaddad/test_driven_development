from string import digits 
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
        if "\'" in words:
            updated_phrase.append(words)
        # elif words.isdigit():
        #     continue
        else:
            # spaces = re.sub("[\s]", "", words)
            
            updated_phrase.append(re.sub("[\W\d]", " ", words).strip())
    return " ".join(updated_phrase) 


phrase = "I    like spaces 12  !"
# # # # 
print(word_count(phrase))

#why doesn't the re.sub("[\W\d\s]", " ", words).strip()) catch the spaces? Even if I create a separate variable to catch the spaces, it's not catchign but it works in pythex.