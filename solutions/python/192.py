def length_of_sequence(arr,n):
    targets = list(filter(lambda pair: pair[1] == n, enumerate(arr)))
    if len(targets) != 2:
        return 0
    elif targets[0][0] == 0 and targets[-1][0] == len(arr) - 1:
        return len(arr)
    return targets[1][0] - targets[0][0] + 1