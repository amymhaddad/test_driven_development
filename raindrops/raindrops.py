FACTORS_TO_SOUNDS = {3: "Pling", 5: "Plang", 7: "Plong"}


def raindrops(n):
    """Return a sound based on a number's factors"""

    list_of_factors = factors(n)

    if len(list_of_factors) == 0:
        return ""

    elif not common_factors(n):
        return str(n)

    return "".join(
        [
            FACTORS_TO_SOUNDS[number]
            for number in list_of_factors
            if number in FACTORS_TO_SOUNDS
        ]
    )


def factors(n):
    """Find the factors for a given number"""
    factors = []

    for outer_number in range(1, n + 1):
        for inner_number in range(1, n + 1):
            if outer_number * inner_number == n:
                factors.append(outer_number)
    return factors


def common_factors(n):
    """Determine if the factors for a given number have any factors in
    common with the given factors associated with sounds: 3, 5, 7"""

    factors_to_sounds_factors = set(FACTORS_TO_SOUNDS.keys())
    factors_of_n = set(factors(n))

    return factors_to_sounds_factors.intersection(factors_of_n)
