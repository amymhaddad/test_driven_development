

number = '3598215088'
# number = ''

def isbn(number):
    total = 0
    index = [digit for digit in reversed(range(11))]
    numbers = [int(num) for num in number]

    if valid_number(number):
        for num, i in zip(numbers, index):
            total += num * i 
        return bool(total % 11 == 0)
    return valid_number(number)


def valid_number(number):
    return bool(len(number) == 10 )
    
 
print(isbn(number))   
