def get_planet_name(planet_id):
    # This doesn't work; Fix it!
    lookup = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    return lookup[planet_id - 1]