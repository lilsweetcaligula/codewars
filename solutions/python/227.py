def find_missing_numbers(arr):
    candidates = arr and range(min(arr), max(arr) + 1)
    return sorted(set(arr) ^ set(candidates))