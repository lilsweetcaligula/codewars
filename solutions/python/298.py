from itertools import chain

pattern = (lambda count: '\n'.join(
    ''.join(str(digit) for digit in chain(range(start, count + 1), range(1, start)))
    for start in range(1, count + 1)))