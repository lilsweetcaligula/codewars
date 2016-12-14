def ipValidator(ip):
    try:
        import re
        match = re.search('^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip)
        if match:
            bytes = match.groups()
            return all(0 <= int(byte) < 256 for byte in bytes)
        return False
    except ValueError:
        return False
    
    