def my_first_kata(a,b):
    if not (type(a) == type(b) == int):
        return False
    return a % b + b % a