truncate_string = (lambda s, n, ending = '...':
        [s, s[:n - len(ending)] + ending, s[:n] + ending]
        [(len(s) > n) + (len(s) > n and n <= 3)])
    