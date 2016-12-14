# return masked string
maskify = (lambda cc: 
    '#' * len(cc[:-4]) + cc[-4:])