from string import digits

number = '359821507X'
# number = ''



def isbn(number):
    total = 0
    index = [digit for digit in reversed(range(11))]
    numbers = [int(num) for num in number if num in digits]

    if not valid_number(number):
        return False

    if number[-1] == 'X':
            total += 10
    for num, i in zip(numbers, index):
        total += num * i 
    return bool(total % 11 == 0)
  


def valid_number(number):
    return bool(len(number) == 10 )
    
 
print(isbn(number))   
