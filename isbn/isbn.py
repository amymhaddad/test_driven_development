

number = '3598215088'

def isbn(number):
    total = 0
    index = [digit for digit in reversed(range(11))]
    numbers = [int(num) for num in number]

    #validity check to be exceptions 
    if number == '' or len(number) < 10:
        return False
    else:
        for num, i in zip(numbers, index):
            print(num, i)
            total += num * i 
       
        return bool(total % 11 == 0)

    

print(isbn(number))
    
    
    

# def validate_number(number):
    
#     return [int(num) for num in number]

# numbers = validate_number(number)

# index = [digit for digit in reversed(range(11))]


# total = 0
# for n, i in zip(numbers, index):
#     total += n*i
# print(total % 11)