def armstrong(number):
    number_list = [int(num) for num in str(number)]

    total = [number ** len(number_list) for number in number_list]

    return bool(sum(total) == number)
