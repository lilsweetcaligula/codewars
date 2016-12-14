def duplicate_count(text):
    from collections import Counter
    counter = Counter(text.lower())
    count = 0
    for char, frequency in counter.items():
        if frequency > 1:
            count += 1
    return count