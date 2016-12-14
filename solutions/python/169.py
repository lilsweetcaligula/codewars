def number(bus_stops):
    passengers = zip(*bus_stops)
    return sum(passengers[0]) - sum(passengers[1])