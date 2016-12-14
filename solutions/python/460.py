def string_clean(s):
    """
    Function will return the cleaned string
    """
    return filter(lambda char: not char.isdigit(), s)