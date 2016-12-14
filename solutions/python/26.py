def testit(s):
    return ' '.join(sub[:-1].lower() + sub[-1].upper() for sub in s.split())