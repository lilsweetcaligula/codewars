def dominator(values):
    from collections import Counter    
    sortedValues = sorted(
        Counter(values).items(), key = lambda pair: pair[1], reverse = True)
    return(
        sortedValues[0][0] if sortedValues and sortedValues[0][1] > len(values) // 2 
        else -1)
    def dominator(values):
    from collections import Counter    
    sortedValues = sorted(
        Counter(values).items(), key = lambda pair: pair[1], reverse = True)
    return sortedValues[0][0] if sortedValues and sortedValues[0][1] > len(values) // 2 else -1
    