row_sum_odd_numbers = lambda n: n ** 3def row_sum_odd_numbers(n):
    number = 1
    total = 0
    for level in range(n + 1):
        total = 0
        count = level
        while count > 0:
            if number % 2:
                total += number
            number += 2
            count -= 1        
    return total  