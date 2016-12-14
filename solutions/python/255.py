whitespace_number = (lambda n: (' ' if n > 0 else '\t' if n < 0 else '') 
    + bin(abs(n))[2:].translate(str.maketrans('01', ' \t')) + '\n')