#Try to make your own gcd method without importing stuff
def mygcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x