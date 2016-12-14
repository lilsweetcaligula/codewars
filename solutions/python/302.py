flatten = (lambda lst: 
    sum([item if isinstance(item, list) else [item] for item in lst], []))from itertools import chain
from functools import reduce
from operator import add

flatten = (lambda lst: reduce(
        add, 
        chain(item if isinstance(item, list) else [item] for item in lst), 
        []))def flatten(lst):
    result = []
    for item in lst:
        if hasattr(item, '__iter__'):
            result.extend(item)
        else:
            result.append(item)
    return result