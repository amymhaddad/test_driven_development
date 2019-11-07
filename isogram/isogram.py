
def isogram(string):

    unique_letters = set()
    for letter in string:
        unique_letters.add(letter)
    if len(unique_letters) == len(string):
        return True
    return False
            


print(isogram('catt'))