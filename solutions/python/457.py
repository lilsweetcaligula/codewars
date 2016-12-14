def cooking_time(eggs, eggs_in_pot = 8, minutes_to_boil_one_egg = 5):
    from math import ceil
    return ceil(eggs / eggs_in_pot) * minutes_to_boil_one_egg