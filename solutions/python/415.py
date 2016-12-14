def count_positives_sum_negatives(array):
    return [len([value for value in array if value > 0]), sum([value for value in array if value < 0])]