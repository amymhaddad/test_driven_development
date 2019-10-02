from string import punctuation as punctuation_marks
from string import digits as numbers

phrase = 'I am 12 years old!'

def word_count(phrase):

    phrase = validate_phrase(phrase)

    counter = 0
    word_count_dictionary = {}

    for word in phrase.split(" "):            
        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
        
        if word == '' and len(phrase)>1:
            del word_count_dictionary[word]
    return word_count_dictionary


def validate_phrase(phrase):
    """Remove punctuation and lowercase all words"""

    updated_phrase = ''
    for words in phrase.lower():
        if words in punctuation_marks:
            updated_phrase += words.strip(punctuation_marks)
        elif words in numbers:
            # import pdb; pdb.set_trace()
            continue
        else:
            updated_phrase += words


    return updated_phrase
    # return updated_phrase.strip(" ")

print(word_count(phrase))

# print(validate_phrase(phrase))

