def high_and_low(numbers):
    values = list(map(int, numbers.split()))
    return ' '.join(map(str, (max(values), min(values))))
    