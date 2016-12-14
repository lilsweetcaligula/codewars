import string

next_letter = (lambda s: 
    s.translate(
        str.maketrans(
            string.ascii_lowercase, 
            string.ascii_lowercase[1:] + string.ascii_lowercase[:1])
    ).translate(
        str.maketrans(
            string.ascii_uppercase, 
            string.ascii_uppercase[1:] + string.ascii_uppercase[:1])
        )
    )