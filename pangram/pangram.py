from string import ascii_lowercase as alphabet


def pangram(sentence):

    sentence_letters_in_alphabet = set(
        letter for letter in sentence.lower() if letter in alphabet
    )

    return set(alphabet).issubset(sentence_letters_in_alphabet)
