def palindrome_pairs(words):
    result = []
    for firstIndex, firstWord in enumerate(words):
        for secondIndex, secondWord in enumerate(words):
            if firstIndex != secondIndex:
                candidate = str(firstWord) + str(secondWord)
                if candidate == candidate[::-1]:
                    result.append([firstIndex, secondIndex])
    return result