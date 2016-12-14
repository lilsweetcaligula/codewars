def rps(p1, p2):
    lookup = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    return('Draw!' if p1 == p2 
        else 'Player 1 won!' if p2 == lookup[p1] 
        else 'Player 2 won!')