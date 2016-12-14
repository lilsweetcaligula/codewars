def calculate_age(year_of_birth, current_year):
    distance = abs(current_year - year_of_birth)
    if year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(
            distance, 's' if distance > 1 else '')
    elif year_of_birth < current_year:
        return 'You are {} year{} old.'.format(
            distance, 's' if distance > 1 else '')
    return 'You were born this very year!'
    