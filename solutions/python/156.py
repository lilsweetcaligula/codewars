def calc(expr):
    import operator
    operator_lookup = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    tokens = expr.split()
    value_stack = []
    for token in tokens:
        try:
            value = float(token)
            value_stack.append(value)
        except ValueError:
            if token in operator_lookup:
                b, a = value_stack.pop(), value_stack.pop()
                operation = operator_lookup[token]
                result = operation(a, b)
                value_stack.append(result)
            else:
                raise
    return value_stack and value_stack.pop() or 0
            
            