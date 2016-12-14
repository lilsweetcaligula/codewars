def converter(mpg):
    LITERS_IN_GALLON = 4.54609188
    KM_IN_MI = 1.609344
    return float('{:.2f}'.format(mpg * KM_IN_MI / LITERS_IN_GALLON))