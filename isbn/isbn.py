from string import digits


def isbn(number):
    """Determine if a given number is a valid isbn number"""

    total = 0
    index = [digit for digit in reversed(range(11))]
    numbers = standardize_isbn(number)

    if len(numbers) < 10:
        return False

    for num, i in zip(numbers, index):
        total += num * i
    return bool(total % 11 == 0)


def standardize_isbn(number):
    """Convert given string to integers"""
    numbers = [int(num) for num in number if num in digits]

    if number[-1] == "X":
        numbers.append(10)
    return numbers
