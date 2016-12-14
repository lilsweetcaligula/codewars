def fizzbuzz(n):
    return [
        'FizzBuzz' if value % 15 == 0 
        else 'Buzz' if value % 5 == 0 
        else 'Fizz' if value % 3 == 0 
        else value for value in range(1, n + 1)]