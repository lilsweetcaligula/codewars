#preloaded variable: "dictionary"

def make_backronym(acronym):
    return ' '.join(dictionary.get(char.upper(), char.upper()) for char in acronym)