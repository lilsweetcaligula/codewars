def get_a_down_arrow_of(n):
    from itertools import chain
    lines = []
    for m in reversed(range(1, n + 1)):
        line = ''.join(
            chain(
                (str(digit % 10) for digit in range(1, m + 1)),
                (str(digit % 10) for digit in reversed(range(1, m)))))
        lines.append('{:^{width}}'.format(line, width = 2 * n - 1).rstrip())
    return '\n'.join(lines)