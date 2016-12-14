def revrot(string, sz):
    if sz == 0:
        return ''
    chunks = [string[start:start + sz] for start in range(0, len(string) - len(string) % sz, sz)]
    cubed_sums = [sum(int(digit) ** 3 for digit in chunk) for chunk in chunks]
    for index, chunk in enumerate(chunks):
        if cubed_sums[index] % 2:
            chunks[index] = chunk[1:] + chunk[:1]
        else:
            chunks[index] = chunk[::-1]
    return ''.join(chunks)