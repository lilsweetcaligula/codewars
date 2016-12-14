def find_longest(string):
    words = string.split()
    return max(map(len, words))