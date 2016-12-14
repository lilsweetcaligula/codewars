def zipvalidate(postcode):
    import re
    return re.match(r'\A[1-46]\d{5}\Z', postcode) != None