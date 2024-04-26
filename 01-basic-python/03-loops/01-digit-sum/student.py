def last_digit(n):
    return int(str(n)[-1])

def remove_last_digit(n):
    if n < 10 and n >= 0:
        return 0
    else:
        return int(str(n)[:-1])


def digit_sum(n):
    result = 0
    for i in str(n):
        result += int(i)

    return result