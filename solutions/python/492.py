def namelist(people):
    names = [person['name'] for person in people]
    if len(names) <= 1:
        return ''.join(names)
    return ' & '.join((', '.join(names[:-1]), ''.join(names[-1:])))
    