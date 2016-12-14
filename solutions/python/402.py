# The cmp function - forever missed.
close_compare = lambda a, b, margin = 0: 0 if abs(a - b) <= margin else (a > b) - (a < b)