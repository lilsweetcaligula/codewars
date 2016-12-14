def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the global namespace
    a, b = (greek_alphabet.index(letter) for letter in (lhs, rhs))
    return (a > b) - (a < b)