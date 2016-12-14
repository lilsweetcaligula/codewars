def obfuscate(email):
    return email.replace('@', ' [at] ').replace('.', ' [dot] ')def obfuscate(email):
    import re
    return re.sub(r'\.', ' [dot] ', re.sub(r'@', ' [at] ', email))