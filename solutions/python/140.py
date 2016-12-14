def sort_it(words, n, separator = ', '):
    return separator.join(sorted(words.split(separator), key = lambda word: word[n - 1]))