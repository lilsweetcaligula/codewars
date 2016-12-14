def disemvowel(string):
    return ''.join(filter(lambda char: char.lower() not in 'aeoui', string))