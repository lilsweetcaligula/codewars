def ipv4_address(address):
    import re
    matches = [
        re.match(r'\A(\d)\Z|\A([1-9]\d+)\Z', byte) 
        and 0 <= int(byte) <= 255 
        for byte in address.split('.')]
    return all(matches) and len(matches) == 4