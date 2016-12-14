hotpo = (lambda number, count = 0: 
    count if number == 1 
    else hotpo(3 * number + 1, count + 1) if number % 2 
    else hotpo(number / 2, count + 1))def hotpo(number):
    count = 0
    while number != 1:
        number = 3 * number + 1 if number % 2 else number / 2
        count += 1
    return count