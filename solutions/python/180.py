def find_next_square(sq):
    return -1 if (sq ** 0.5) % 1.0 > 0 else (sq ** 0.5 + 1) ** 2