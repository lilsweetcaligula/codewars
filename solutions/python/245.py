def to_freud(sentence):
    from itertools import repeat
    return ' '.join(repeat('sex', times = len(sentence.split())))