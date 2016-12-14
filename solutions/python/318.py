def show_sequence(n):
    numbers = range(n + 1)
    return '{lhs}{space}{operator}{space}{rhs}'.format(
        lhs = '+'.join(str(number) for number in numbers) if numbers else n,
        operator = '=' if n >= 0 else '<',
        rhs = sum(numbers) if n > 0 else 0,
        space = " " if n > 0 else "")