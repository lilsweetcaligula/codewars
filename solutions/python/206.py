def sum_consecutives(L):
    currentSum = 0
    result = []
    index = 0
    while index < len(L):
        value = L[index]
        while index < len(L) - 1 and L[index] == L[index + 1]:
            value += L[index]
            index += 1
        result.append(value)
        index += 1
    return result
