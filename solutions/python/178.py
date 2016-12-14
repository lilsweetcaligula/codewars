def repeat_sum(sequences):
    from itertools import chain
    from collections import Counter
    result = []
    counter = Counter(
        chain(
            *(set(sequence) for sequence in sequences)
        )).items()
    for item, count in counter:
        if count > 1:
            result.append(item)
    return sum(result)