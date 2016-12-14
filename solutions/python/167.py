def ones_counter(data):
    from itertools import groupby
    result = []
    for label, group in groupby(data):
        if label:
            result.append(len(list(group)))
    return result