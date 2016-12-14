def how_much_water(L,X,N, ndigits = 2):
    if N < X:
        return 'Not enough clothes'
    elif N > 2 * X:
        return 'Too much clothes'
    difference = N - X
    return round(1.1 ** difference * L, ndigits)def how_much_water(L,X,N, ndigits = 2):
    if N > 2 * X:
        return 'Too much clothes'
    elif N < X:
        return 'Not enough clothes'
    difference = N - X
    while difference > 0:
        L += L * 0.1
        difference -= 1
    return round(L, ndigits)