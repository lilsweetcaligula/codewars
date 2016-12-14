def chinese_zodiac(year):
    year -= 1984
    return ' '.join((elements[(year // 2) % len(elements)], animals[year % len(animals)]))def chinese_zodiac(year):
    init = 60 * (year // 60) + 4
    return ' '.join((
        elements[((year - init) // 2) % len(elements)], 
        animals[((year - init) % len(animals))]))