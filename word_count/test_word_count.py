
from word_count import word_count

def test_count_single_word():
    #setup 
    phrase = 'word'

    assert word_count(phrase) == {'word': 1}