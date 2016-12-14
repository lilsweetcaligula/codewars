def shorter_reverse_longer(a,b):
    shorter, longer = (
        (b, a) if len(a) == len(b) 
            else sorted((a, b), key = len))
    return '{0}{1}{0}'.format(shorter, longer[::-1])