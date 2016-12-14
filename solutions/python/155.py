def compound_array(a, b):
    from itertools import izip_longest as zip_longest
    compound = []
    for pair in zip_longest(a, b):
        compound.extend(list(filter(lambda value: value != None, pair)))
    return compound