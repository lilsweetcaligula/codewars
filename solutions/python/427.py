def find_outlier(integers):
    odd_integers = []
    even_integers = []
    for integer in integers:
        if integer % 2:
            odd_integers.append(integer)
        else:
            even_integers.append(integer)
    for sequence in (odd_integers, even_integers):
        if len(sequence) == 1:
            return sequence[0]
    return None