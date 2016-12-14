def Xbonacci(signature,n):
    sequence = signature[:]
    x = len(signature)
    for times in range(len(sequence), n):
        sequence.append(sum(sequence[-x:]))
    return sequence[:n]