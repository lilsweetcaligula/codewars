def compare(s1,s2):
    if not s1 or not s2:
        return True
    strings = (
        ''.join(char for char in s.upper() if char.isalpha()) 
            for s in (s1, s2))
    values = list(map(lambda string: sum(ord(char) for char in string), strings))
    return all(pair[0] == pair[1] for pair in zip(values, values[1:]))