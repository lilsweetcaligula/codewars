def int_diff(L, difference):
    from functools import reduce
    from operator import sub
    return ([
        abs(reduce(sub, pair)) 
            for i in range(len(L)) 
                for pair in zip(L, L[i + 1:])].count(difference))