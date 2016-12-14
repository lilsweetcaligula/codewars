def two_highest(sequence: list) -> list:
    if type(sequence) != list:
        return False
    if len(sequence) == 0:
        return []
    firstHighest = secondHighest = max(sequence)
    for item in sequence:
        if ((item < firstHighest == secondHighest) 
            or (secondHighest < item < firstHighest)):
            secondHighest = item
    return sorted([firstHighest, secondHighest], reverse = True)
        