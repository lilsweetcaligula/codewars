def show_me(name):
    import re
    return all(
        map(
            lambda token: re.match(r'\A[A-Z][a-z]*\Z', token) != None, 
            name.split('-')
            ))