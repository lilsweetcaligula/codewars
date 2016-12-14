def split_the_bill(x, ndigits = 2):
    split = sum(x.values()) / float(len(x))
    return { name:round(spent - split, ndigits) for name, spent in x.items() }