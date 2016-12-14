def add_length(string, separator = " "):
    return ["{} {}".format(substring, len(substring)) for substring in string.split(separator)]def add_length(string, separator = " "):
    return ["{0} {1}".format(substring, len(substring)) for substring in string.split(separator)]