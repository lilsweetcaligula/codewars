def triple_trouble(*strings):
    return ''.join(''.join(substring) for substring in zip(*strings))