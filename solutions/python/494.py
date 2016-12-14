def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    narcissistics = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 
        598, 1306, 1676, 2427, 2646798, 12157692622039623539
    ]
    from bisect import bisect
    i, j = (bisect(narcissistics, value) - 1 for value in (a, b))
    first = i if i >= 0 and narcissistics[i] == a else i + 1
    last = j + 1
    return narcissistics[first:last]