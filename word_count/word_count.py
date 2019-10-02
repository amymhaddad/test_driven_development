from string import punctuation, digits

def word_count(phrase):

    phrase = validate_phrase(phrase)

    counter = 0
    word_count_dictionary = {}

    for word in phrase.split(" "):       

        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
        if word == '' and len(phrase) > 1:
            del word_count_dictionary[word]             
    return word_count_dictionary


def validate_phrase(phrase):
    """Remove punctuation and lowercase all words"""

    updated_phrase = ''
    for words in phrase.lower():
        if words in punctuation:
            updated_phrase += words.strip(punctuation)
        elif words in digits:
            continue
        else:
            updated_phrase += words

    return updated_phrase
   
print(word_count(phrase))

# print(validate_phrase(phrase))

