def mine_color(file, rank):
    colors = 'black', 'white'
    files  = 'abcdefgh'
    ranks  = 1,2,3,4,5,6,7,8
    return colors[(files.index(file.lower()) % len(colors) + ranks.index(rank)) % len(colors)]