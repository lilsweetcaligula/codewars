def mineLocation(field):
    mine = 1
    for row in range(len(field)):
        if mine in field[row]:
            return [row, field[row].index(mine)]
    return None