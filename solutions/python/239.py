def find_dup(arr):
    arr.sort()
    return filter(lambda pair: pair[0] == pair[1], zip(arr, arr[1:]))[0][0]