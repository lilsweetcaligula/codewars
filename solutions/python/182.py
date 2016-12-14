def is_isogram(string):
    return sorted(string.casefold()) == (sorted(set(string.casefold())))