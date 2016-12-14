def validate_word(word):
    from collections import Counter
    frequencies = Counter(word.lower()).values()
    return all(a == b for a, b in zip(frequencies, frequencies[1:]))