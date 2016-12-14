def rotate(arr, n):
    n %= len(arr)
    return arr[-n:] + arr[:-n]