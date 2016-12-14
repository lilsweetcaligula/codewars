def generate_link(user, isSecure = False):
    from urllib import pathname2url
    return r'http{}://www.codewars.com/users/{}'.format(
        's' if isSecure else '', 
        pathname2url(user))