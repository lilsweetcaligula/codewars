def remove(text, what):
    chars = []
    for char in text:
        if char in what and what[char] > 0:
            what[char] -= 1
        else:
            chars.append(char)
    return ''.join(chars)