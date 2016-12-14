class Item:
    def __init__(self, count = 0, price = 0.0):
        self.count = count
        self.price = price       
        
    def __eq__(self, other):
        if type(other) == int:
            return self.count == other
        return super(Item, self).__eq__(other)
    
class Sandwich(Item):
    def __init__(self, count = 0, price = 0.0):
        super(Sandwich, self).__init__(count, price)
        
class Salad(Item):
    def __init__(self, count = 0, price = 0.0):
        super(Salad, self).__init__(count, price)
        
class Wrap(Item):
    def __init__(self, count = 0, price = 0.0):
        super(Wrap, self).__init__(count, price)
        
class FrenchFries(Item):
    def __init__(self, count = 0, price = 0.0):
        super(FrenchFries, self).__init__(count, price)
        
items = (
    Sandwich(4, 8.0),
    Salad(6, 7.0),
    Wrap(5, 6.5),
    FrenchFries(10, 1.2)
)
sandwiches, salads, wraps, frenchFries = items
totalPrice = sum(item.price * item.count for item in items)