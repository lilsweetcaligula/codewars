def pop_shift(src, dest1 = '', dest2 = ''):
    if len(src) <= 1:
        return [dest1, dest2, src]
    return pop_shift(src[1:-1], dest1 + src[-1], dest2 + src[0])