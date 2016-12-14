def histogram(results, histo_char = '#'):
    lines = []
    for roll, result in enumerate(results, start = 1):
        line = '{}|'.format(roll)
        if result:
            line += '{} {}'.format(histo_char * result, result)
        lines.append(line)
    return '\n'.join(reversed(lines)) + '\n'