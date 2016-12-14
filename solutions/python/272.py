import re

validate_usr = lambda username: re.match(r'^[a-z0-9_]{4,16}$', username) != Nonedef validate_usr(username):
    import re
    match = re.match(r'^[a-z0-9_]+$', username)
    if match:
        start, end = match.span()
        return 4 <= end - start <= 16
    return False