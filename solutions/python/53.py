def substring_test(str1, str2):
    str1, str2 = (s.lower() for s in (str1, str2))
    suffixes = [
        str2[start:end] 
            for start in range(len(str2)) 
            for end in range(start + 2, len(str2) + 1)]
    for suffix in suffixes:
        if suffix in str1:
            return True
    return False