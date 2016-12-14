def chained(functions):
    def composite(arg):
        for function in functions:
            arg = function(arg)
        return arg
    return composite