def coins(one, two, five, goal):
    for ones in range(one + 1):
        for twos in range(two + 1):
            for fives in range(five + 1):
                result = ones*1 + twos*2 + fives*5
                if result == goal:
                    return True
    
    return False