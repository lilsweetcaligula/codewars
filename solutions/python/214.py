def conference_picker(cities_visited, cities_offered):
    cities_visited = set(cities_visited)
    for city_offered in cities_offered:
        if city_offered not in cities_visited:
            return city_offered
    return 'No worthwhile conferences this year!'