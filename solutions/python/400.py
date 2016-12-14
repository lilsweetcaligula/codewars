def movie(card, ticket, perc):
    class System:
        def __init__(self):
            self.amount = 0.0
            self.times = -1
        def __next__(self):
            raise NotImplementedError()
            
    class SystemA(System):
        def __init__(self, ticket):
            super(SystemA, self).__init__()
            self.ticket = ticket
        def __next__(self):
            self.amount += self.ticket
            self.times += 1
            
    class SystemB(SystemA):
        def __init__(self, card, ticket, perc):
            super(SystemB, self).__init__(ticket)
            self.amount += card
            self.perc = perc
        def __next__(self):
            super(SystemB, self).__next__()
            self.ticket *= self.perc

    from math import ceil
    system_a, system_b = SystemA(ticket), SystemB(card, ticket, perc)
    while not (ceil(system_b.amount) < system_a.amount):
        for system in (system_a, system_b):
            next(system)
    return system_a.times