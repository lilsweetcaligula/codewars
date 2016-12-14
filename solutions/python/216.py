def name_score(name):
    lookup = {}
    for group, score in alpha.items():
        for char in group:
            lookup[char] = score
    return { 
        name: sum((lookup[char.upper()] for char in name if char.upper() in lookup) or [0]) 
    }