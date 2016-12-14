def double_check(s):
    return any(pair[0] == pair[1] for pair in zip(s.lower(), s.lower()[1:]))