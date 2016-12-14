def body_count(code):
    import re
    pattern = r'.*([A-Z]\d){5}\.\-[A-Z]%\d\.\d{2}\..*'
    return re.match(pattern, code) != None