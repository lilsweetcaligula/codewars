factorial = (lambda n: 
                None if n < 0 else 1 if n < 2 else n * factorial(n - 1))