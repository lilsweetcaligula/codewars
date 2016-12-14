def ordered_count(data):
    from collections import OrderedDict
    occurences = OrderedDict()
    for char in data:
        occurences[char] = occurences.get(char, 0) + 1
    return list(occurences.items())def ordered_count(data):
    occurences = {}
    for index, char in enumerate(data):
        if char not in occurences:
            occurences[char] = { 'count' : 1, 'firstIndex' : index }
        else:
            occurences[char]['count'] += 1
    return [(char, data['count']) for char, data in 
        sorted(occurences.items(), key = lambda x : x[1]['firstIndex'])]