def remove_every_other(my_list):
    return [value for index, value in enumerate(my_list) if (index + 1) % 2 != 0]
