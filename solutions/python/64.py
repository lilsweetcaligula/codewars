def validate_sequence(sequence):
    from operator import eq
    from functools import reduce
    differences = list(map(lambda pair: abs(pair[1] - pair[0]), zip(sequence, sequence[1:])))
    return all(map(lambda pair: eq(pair[1], pair[0]), zip(differences, differences[1:])))