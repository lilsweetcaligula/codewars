get_real_floor = (lambda n: 
    n if n < 0 
    else 0 if n in (0, 1) 
    else n - 2 if n > 13 
    else n - 1)