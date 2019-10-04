

number = '3598215088'

def isbn(number):
    if number == '' or len(number) < 10:
        return False


    
    
    

def validate_number(number):
    
    return [int(num) for num in number]

numbers = validate_number(number)

index = [digit for digit in reversed(range(11))]


total = 0
for n, i in zip(numbers, index):
    total += n*i
print(total % 11)