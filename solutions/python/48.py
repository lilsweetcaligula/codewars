def is_prime(value):
    if value % 2 == 0:
        return value == 2
    elif value > 2:
        limit = int(value ** 0.5)
        for divisor in range(3, limit + 1):
            if value % divisor == 0:
                return False
        return True
    return False

def number_property(n):
    return [is_prime(n), n % 2 == 0, n % 10 == 0]