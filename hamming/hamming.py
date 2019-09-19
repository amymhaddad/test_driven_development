"""Calculate the Hamming difference between two DNA strands."""


def hamming(strand1, strand2):

    count = 0
    if len(strand1) != len(strand2):
        raise ArgumentError("The lists are different lengths")
    if strand1 == "" or strand2 == "":
        raise Arugument("The strings are empty.")

    return sum([count + 1 for i, letter in enumerate(strand1) if letter != strand2[i]])
