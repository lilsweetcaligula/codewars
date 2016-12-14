def last(*args):
    return(
        args[-1][-1] if args and hasattr(args[-1], '__getitem__') 
        else args[-1] if args 
        else None)