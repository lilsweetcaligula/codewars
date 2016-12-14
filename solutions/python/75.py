def vowel_2_index(string):
    return ''.join(char if char.lower() not in 'aeoui' else str(index + 1) for index, char in enumerate(string))