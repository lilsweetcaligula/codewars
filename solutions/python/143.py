def consecutive(arr):
    if not arr:
        return 0
    return len(set(range(min(arr), max(arr) + 1)) ^ set(arr))