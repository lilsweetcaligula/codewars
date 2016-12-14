def duplicate_encode(word):
    from collections import Counter
    word = word.casefold()
    counter = Counter(word)
    result = ''
    for letter in word:
        if counter[letter] > 1:
            result += ')'
        else:
            result += '('
    return result