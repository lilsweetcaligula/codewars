def new_avg(arr, newavg):
    from math import ceil
    donation = ceil(newavg * (len(arr) + 1) - sum(arr))
    if donation <= 0:
        raise ValueError()
    return donation