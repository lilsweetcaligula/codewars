def filter_long_words(sentence, n):
    return filter(lambda word: len(word) > n, sentence.split())