import string

is_pangram = (lambda s: 
    string.ascii_lowercase == ''.join(sorted(set(filter(str.isalpha, s.lower())))))