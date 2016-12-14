def case_id(c_str):
    import re
    patterns = {
        'camel': r'\A[$a-z][$a-z0-9]+([$A-Z0-9][$a-z0-9]+)+\Z',
        'snake': r'\A[$a-z][$a-z0-9]+?(_[$a-z0-9][$a-z0-9]+?)+\Z',
        'kebab': r'\A[$a-z][$a-z0-9]+?(-[$a-z0-9][$a-z0-9]+?)+\Z',
    }
    for pattern in patterns:
        if re.match(patterns[pattern], c_str):
            return pattern
    return 'none'