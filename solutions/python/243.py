def hamming_weight(x):
    mask  = 1
    count = 0
    while mask <= x:
        if x & mask: 
            count += 1
        mask <<= 1
    return count