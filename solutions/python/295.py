def pattern(n):
    values = [str(value) for value in reversed(range(1, n + 1))]
    return '\n'.join(''.join(values[:end]) for end in reversed(range(1, n + 1)))