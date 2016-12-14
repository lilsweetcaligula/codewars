def title_to_number(title):
    cols = [ord(col.upper()) - ord('A') + 1 for col in title]
    return sum(col * 26 ** index for index, col in enumerate(reversed(cols)))