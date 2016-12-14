def alphabet_position(text):
    from string import ascii_lowercase
    lookup = { letter: index for index, letter in enumerate(ascii_lowercase.casefold(), start = 1) }
    return ' '.join(str(lookup[char.casefold()]) for char in text if char.casefold() in lookup)