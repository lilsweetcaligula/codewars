#fix the function below!

def convert_num(number, base):
    try:
        if base == 'hex':
            return hex(number)
        if base == 'bin':
            return bin(number)
        return 'Invalid base input'
    except TypeError:
        return 'Invalid number input'