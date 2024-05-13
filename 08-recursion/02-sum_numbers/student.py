def sum_numbers(number):
    num = abs(number)
    
    if num < 10:
        return num
    else:
        return (num % 10) + sum_numbers(num // 10)