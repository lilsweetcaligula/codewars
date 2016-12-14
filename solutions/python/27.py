def err_bob(string):
    import re
    pattern = r'\w+'
    words = re.findall(pattern, string)
    for index, word in enumerate(words):
        if word[-1].isupper() and word[-1] not in 'AEOUI':
            words[index] = word + 'ERR'
        elif word[-1].islower() and word[-1] not in 'aeoui':
            words[index] = word + 'err'
    return re.sub(pattern, '{}', string).format(*words)