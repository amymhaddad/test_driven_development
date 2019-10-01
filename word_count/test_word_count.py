
from word_count import word_count

def test_count_single_word():
    assert word_count('word')
    

def test_two_words_separated_by_single_space():
    assert word_count('two words') == {'two':1, 'words': 1}

def test_repeated_words_separated_by_single_space():
    assert word_count('house house dog') == {'house': 2, 'dog':1}

def test_words_with_capital_letters():
    assert word_count('My name is Jill and my home is in Boston') == {'my': 2, 'name': 1, 'is': 2, 'Jill': 1, 'and': 1, 'home': 1, 'in': 1, 'Boston': 1}
    # counter == count_each_phrase




# def test_count_single_word():
#     #setup 
#     phrase = 'word'
#     count_each_phrase = {'word': 1}

#     #exercise 
#     counter = word_count(phrase)

#     #verify
#     assert counter == count_each_phrase
#     # assert word_count(phrase) == {'word': 1}