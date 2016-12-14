def midpoint_sum(values):
    right_sum = sum(values)
    left_sum = 0
    for index, value in enumerate(values):
        right_sum -= value
        if (left_sum == right_sum 
            and index not in (0, len(values) - 1)):
            return index
        else:
            left_sum += value            
    return None