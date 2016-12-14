def get_count(*args):
    words = args[0] if args else ''
    vowels = set('aeoui')
    vowelCount = (len(
        [char for char in words if char.lower() in vowels])
            if isinstance(words, basestring) else 0)
    consonantCount = (len(
        [char for char in words if char.isalpha() and char.lower() not in vowels])
            if isinstance(words, basestring) else 0)
    return { 'vowels': vowelCount, 'consonants': consonantCount }
    