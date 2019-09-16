def anagram(given_word, anagram_choices):
    return [
        word
        for word in anagram_choices
        if sorted(word.lower()) == sorted(given_word.lower())
    ]
