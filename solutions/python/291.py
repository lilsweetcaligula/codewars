def sort_array(source_array):
    oddNumbers = iter(sorted(value for value in source_array if value % 2))
    return [next(oddNumbers) if value % 2 else value for value in source_array]def sort_array(source_array):
    oddNumbers = sorted(value for value in source_array if value % 2)
    return list(reversed([oddNumbers.pop() if value % 2 else value for value in reversed(source_array)]))def sort_array(L):
    oddNumbers = iter(sorted(value for value in L if value % 2))
    for index, value in enumerate(L):
        if value % 2:
            L[index] = next(oddNumbers)
    return L