from string import digits
import re


def word_count(phrase):
    """Count the words in a given phrase"""

    phrase = validate_phrase(phrase)
    word_count_dictionary = {}



    if len(phrase) < 1:
        return 0

    for word in phrase.split(" "):
        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
        if word == "":
            del word_count_dictionary[word]
    return word_count_dictionary


def validate_phrase(phrase):
    """Remove punctuation and digits; lowercase all words"""

    only_words = re.sub('\W', " ", phrase)

    updated_phrase = []
    for words in only_words.lower().split(" "):
        if words.isalpha():
            updated_phrase.append(words)
        elif words.isdigit():
            continue
    
    return " ".join(updated_phrase).strip()


# phrase = "That medicine is fast-acting."
# # # # 
# print(word_count(phrase))