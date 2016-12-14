def duplicates(array):
    result = []
    lookup = set()
    stored = set()
    for index, value in enumerate(array):
        if value not in stored and value in lookup:
            result.append(value)
            stored.add(value)
        lookup.add(value)
    return result