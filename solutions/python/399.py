def distinct(seq):
    values = set()
    result = []
    for value in seq:
        if value not in values:
            values.add(value)
            result.append(value)
    return result