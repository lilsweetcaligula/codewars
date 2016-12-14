accum = (lambda s, separator = '-': 
    separator.join(sub.capitalize() for sub in 
        [character * (index + 1) for index, character in enumerate(s)]))