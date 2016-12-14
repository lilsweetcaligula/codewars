def reverse_fun(n):
    for i in range(len(n)):
        n = n[:i] + ''.join(reversed(n[i:]))
    return n