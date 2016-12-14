from itertools import imap

lstzip = lambda a, b, fn: list(imap(fn, a, b))