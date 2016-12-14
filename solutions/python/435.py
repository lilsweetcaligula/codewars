def mxdiflg(a1, a2):
    lens1, lens2 = (list(map(len, arr)) for arr in (a1, a2))
    return(
        lens1 and lens2 
            and max(abs(max(lens1) - min(lens2)), 
                abs(max(lens2) - min(lens1))) 
        or -1)