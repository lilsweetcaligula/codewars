def compute_mean(iterable):
    return sum(iterable) / float(len(iterable))

def compute_standard_deviation(iterable, mean):
    return (
        sum((value - mean) ** 2 for value in iterable) 
            / (len(iterable) - 1.0)
            ) ** 0.5

def sensor_analysis(sensor_data, ndigits = 4):
    distances = [value 
        for log in sensor_data 
            for key, value in zip(log, log[1:]) 
                if isinstance(key, str) and 'Distance' in key]
    mean = compute_mean(distances)
    standard_deviation = compute_standard_deviation(distances, mean)
    return round(mean, ndigits), round(standard_deviation, ndigits)