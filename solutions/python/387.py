def array(string, inputSeparator = ",", outputSeparator = " "):
    return outputSeparator.join(substring for substring in string.split(inputSeparator)[1:-1]) or Nonedef array(string, separator = " "):
    result = separator.join(substring for substring in string.split(',')[1:-1])
    if len(result) == 0:
        return None
    return result