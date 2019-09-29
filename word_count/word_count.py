
def word_count(phrase):
    counter = 0
    word_count_dictionary = {}


    for word in phrase.split(" "):
        # import pdb; pdb.set_trace()
        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1
    return word_count_dictionary

print(word_count('two words'))


