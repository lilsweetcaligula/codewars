def closest_sum(values, num):
    sums = set()
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            for k in range(j + 1, len(values)):
                sums.add(sum(values[index] for index in (i, j, k)))
    return min(sums, key = lambda value: abs(num - value))