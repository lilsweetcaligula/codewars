def reverseWords(s):
    import re
    pattern = r'\S+'
    words = re.findall(pattern, s)
    return re.sub(pattern, '{}', s).format(*reversed(words))