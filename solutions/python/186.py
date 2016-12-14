getCount = (lambda inputStr: 
    len([char for char in inputStr if char.lower() in 'aeoui']))def getCount(inputStr):
    from collections import Counter
    counter = Counter(char for char in inputStr if char.lower() in 'aeoui')
    return sum(counter.values())