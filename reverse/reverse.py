def reverse(word):
    """Reverse a given word"""

    reversed_word = ""

    for index in range(len(word), 0, -1):
        reversed_word += word[index - 1]
    return reversed_word.lower()
