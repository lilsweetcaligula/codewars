def filter_string(string):
    return int(''.join(char for char in string if char.isdigit()))