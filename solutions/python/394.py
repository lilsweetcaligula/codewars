def fibs_fizz_buzz(n):
    previous, current = 0, 1
    fibonaccis = []
    while n > 0:
        if current % 3 == 0 and current % 5 == 0:
            fibonaccis.append('FizzBuzz')
        elif current % 3 == 0:
            fibonaccis.append('Fizz')
        elif current % 5 == 0:
            fibonaccis.append('Buzz')
        else:
            fibonaccis.append(current)
        previous, current = current, previous + current
        n -= 1
    return fibonaccis