def isDigit(string):
    try:
        value = float(string)
        return True
    except ValueError:
        return False
    