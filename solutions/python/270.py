printer_error = (lambda s: 
    '{}/{}'.format(len([char for char in s if char not in 'abcdefghijklm']), len(s)))def printer_error(s):
    error_data = len(list(filter(lambda char: char not in 'abcedfghijklm', s))), len(s)
    return '{}/{}'.format(*error_data)