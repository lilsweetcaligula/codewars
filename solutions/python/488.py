def abbreviate(s):
    import re
    pattern = r'\w{4,}'
    targets = map(
        lambda word: word[0] + str(len(word) - 2) + word[-1], 
        re.findall(pattern, s))
    return re.sub(pattern, '{}', s).format(*targets)