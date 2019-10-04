scrabble_score = {
    "A, E, I, O, U, L, N, R, S, T": 1,
    "D, G": 2,
    "B, C, M, P": 3,
    "F, H, V, W, Y ": 4,
    "K": 5,
    "J,X": 8,
    "Q,Z": 10,
}


def scrabble(word):
    """Calculate the scrabble score for a given word"""

    total_score = 0
    for letters, score in scrabble_score.items():
        for letter in word.lower():
            if letter in letters.lower():
                total_score += score
    return total_score
