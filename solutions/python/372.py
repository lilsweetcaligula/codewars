def unite_unique(*arrays):
    values = set()
    result = []
    for array in arrays:
        for value in array:
            if value not in values:
                values.add(value)
                result.append(value)
    return result