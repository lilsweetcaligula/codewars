def multiple_split(string, delimiters=[]):
    import re
    print('|\\'.join(delimiters))
    return [sub for sub in re.split(
        '|'.join('\\' + delim for delim in delimiters), string) 
            if len(sub) > 0]