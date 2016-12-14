def longest_word(letters):
    from collections import Counter
    from itertools import takewhile
    counter = Counter(letters)
    candidates = sorted(
        (word for word in words if sum((Counter(word) - counter).values()) <= 0),
        key = len,
        reverse = True)
    return list(takewhile(lambda word: len(word) == len(candidates[0]), candidates)) or None