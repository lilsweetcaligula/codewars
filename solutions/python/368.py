#def rental_car_cost(days, costPerWeek = 40.0):
#    total = days * costPerWeek
#    discount = 0.0 if days < 3 else 20.0 if days < 7 else 50.0
#    return total - discount

rental_car_cost = lambda days, costPerWeek = 40.0 : days * costPerWeek - (0.0 if days < 3 else 20.0 if days < 7 else 50.0)