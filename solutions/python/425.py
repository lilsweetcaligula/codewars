def how_much_i_love_you(nb_petals):
    from itertools import cycle
    love_not = cycle(
        ('I love you', 'a little', 'a lot', 
        'passionately', 'madly', 'not at all'))
    for petal in range(nb_petals - 1):
        next(love_not)
    return next(love_not)