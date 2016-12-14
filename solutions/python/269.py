def gps(s, x):
    from math import floor
    distances = [abs(x[index] - x[index - 1]) for index in range(1, len(x))]
    speeds = [dist / s * 3600.0 for dist in distances]
    return floor(max(speeds if speeds else [0]))