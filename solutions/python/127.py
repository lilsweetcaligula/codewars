# boolean_to_string = str

def boolean_to_string(boolean):
    try:
        lookup = ['False', 'True']
        return lookup[boolean]
    except ValueError:
        return ''