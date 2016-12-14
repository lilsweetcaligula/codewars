def solution(number):
    a = b = c = 0
    for value in range(1, number):
        if value % 15 == 0:
            c += 1
        elif value % 5 == 0:
            b += 1
        elif value % 3 == 0:
            a += 1        
    return [a, b, c]