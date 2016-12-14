sxore = (lambda x:
    x if x % 4 == 0 
	    else x + 1 if x % 2 == 0
	    else 1 if (x - 1) % 4 == 0
	    else 0)