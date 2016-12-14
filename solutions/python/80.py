def make_lazy(*args, **kwargs):
    return lambda: args[0](*args[1:], **kwargs)def make_lazy(*args):
    func = args[0]
    return lambda: func(*args[1:])