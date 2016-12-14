class Ghost(object):
    def __init__(self, seed = None):
        import random
        rand = random.Random(seed)
        self.color = rand.choice(('white', 'yellow', 'purple', 'red'))