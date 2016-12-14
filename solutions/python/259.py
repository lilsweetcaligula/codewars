def parse_mana_cost(mana):
    import re    
    match = re.match(r'\A(?P<generic>\d+)?(?P<colors>[wubrg]+)?\Z', mana, re.IGNORECASE)
    if match:
        data = {}
        if match.group('generic'):
            count = int(match.group('generic'))
            if count > 0:
                data['*'] = count
        if match.group('colors'):
            for color in match.group('colors'):
                data[color.lower()] = match.group('colors').count(color)
        return data
    return None