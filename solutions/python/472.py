def tribonacci(signature,n):
    sequence = signature[:]
    for times in range(len(sequence), n):
        sequence.append(sum(sequence[-3:]))
    return sequence[:n]def tribonacci(signature,n):
    sequence = signature[:]
    for times in range(n):
        sequence.append(sum(sequence[-3:]))
    return sequence[:n]def tribonacci(signature,n):
    sequence = signature[:]
    for times in range(len(sequence), n):
        sequence.append(sum(sequence[-index] for index in range(1, 4)))
    return sequence[:n]