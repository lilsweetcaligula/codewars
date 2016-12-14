def compose(s1, s2):
    lines1, lines2 = (s.split() for s in (s1, s2))
    return '\n'.join(
        pair[0][:index] + pair[1][:len(pair[1]) - index + 1]
             for index, pair in enumerate(zip(lines1, lines2[::-1]), start = 1))