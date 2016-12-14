def year_days(year):
    days = 366 if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else 365
    return '{} has {} days'.format(year, days)