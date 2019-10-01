from string import punctuation as punctuation_marks

# phrase = 'My! name is Jill and my home is in Boston!'

def word_count(phrase):

    phrase = remove_puncutation(phrase)

    counter = 0
    word_count_dictionary = {}


    for i, word in enumerate(phrase.split(" ")):
        if i == 0: 
            word = word.lower()

        
        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
    return word_count_dictionary



# {'my': 2, 'name': 1, 'is': 2, 'Jill': 1, 'and': 1, 'home': 1, 'in': 1, 'boston': 1}


def remove_puncutation(phrase):

    updated_phrase = ''
    for words in phrase:
        for letter in words:
            if letter in punctuation_marks:
                updated_phrase += words.strip(punctuation_marks)
            else:
                updated_phrase += words
    return updated_phrase

# print(word_count(phrase))