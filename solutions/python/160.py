def contain_all_rots(s, arr):
    if len(s) == 0:
        return True
    rotations = (s[-n:] + s[:-n] for n in range(len(s)))
    testSet = set(arr)
    return all(rotation in testSet for rotation in rotations)