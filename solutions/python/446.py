def validate_code(code):
    import re
    return re.match(r'^[123]', str(code)) != None