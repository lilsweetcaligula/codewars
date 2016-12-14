def combine(*objects):
    from itertools import chain
    result = {}
    for key, value in chain(*(obj.items() for obj in objects)):
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result