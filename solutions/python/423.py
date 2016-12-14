mxdiflg = (lambda a1, a2: -1 if 0 in (len(a1), len(a2)) 
    else max(abs(len(max(a1, key = len)) - len(min(a2, key = len))), 
             abs(len(max(a2, key = len)) - len(min(a1, key = len)))))