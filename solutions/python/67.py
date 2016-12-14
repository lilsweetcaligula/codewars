def anagrams(word, candidates):
    wordSortedChars = sorted(word)
    return [candidate for candidate in candidates if sorted(wordSortedChars) == sorted(candidate)]