get_sum = lambda a, b: sum(range(min(a, b), max(a, b) + 1))def get_sum(a,b):
    return(
        sum(range(a, b + 1) if a < b 
            else range(a, b - 1, -1) if a > b 
            else [a]))