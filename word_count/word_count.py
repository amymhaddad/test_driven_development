from string import punctuation as punctuation_marks

phrase = 'My name is Jill and my home is in Boston!'

def word_count(phrase):

    phrase = validate_phrase(phrase)

    counter = 0
    word_count_dictionary = {}

    for word in phrase.split(" "):
        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
    return word_count_dictionary


def validate_phrase(phrase):
    """Remove punctuation and lowercase all words"""

    updated_phrase = ''
    for words in phrase.lower():
        if words in punctuation_marks:
            updated_phrase += words.strip(punctuation_marks)
        else:
            updated_phrase += words
    return updated_phrase

print(word_count(phrase))