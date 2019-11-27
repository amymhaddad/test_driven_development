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

    remove_spaces_hyphens = re.sub(r'(\s{2,}|\-{1,})', " ", phrase.lower())   
    
    update = [re.sub(r'[\d*\W*]', "", word) for word in remove_spaces_hyphens.split(" ")]
    # for word in remove_spaces_hyphens.split(" "):
    #     update.append(re.sub(r'[\d*\W*]', "", word))

    try:
        update.remove("")
        return " ".join(update)
    except ValueError:
        return " ".join(update)
    


# phrase = "like.! I    like.! spaces and fast-acting 12!"
# print(word_count(phrase))

# i like spaces