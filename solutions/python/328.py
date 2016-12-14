def sel_number(n, d):
    def is_valid(n, d = 10):
        n_str = str(n)
        return (len(n_str) > 1
            and all(
                0 < int(n_str[i]) - int(n_str[i - 1]) <= d 
                    for i in range(1, len(n_str))
            ))
    return len(filter(lambda n: is_valid(n, d), range(n + 1)))