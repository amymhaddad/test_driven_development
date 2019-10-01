
def word_count(phrase):
    counter = 0
    word_count_dictionary = {}


    for i, word in enumerate(phrase.split(" ")):
        if i == 0: 
            word = word.lower()

        
        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
    return word_count_dictionary

print(word_count('My name is Jill and my home is in Boston'))

# {'my': 2, 'name': 1, 'is': 2, 'Jill': 1, 'and': 1, 'home': 1, 'in': 1, 'boston': 1}
