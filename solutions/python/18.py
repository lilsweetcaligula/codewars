def to_weird_case(string):
    result = ''
    index = 0
    for char in string:
        if index % 2:
            result += char.lower()
        else:
            result += char.upper()
        if char.isalpha():
            index += 1
        else:
            index = 0
    return result