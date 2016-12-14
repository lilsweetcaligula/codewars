def distances_from_average(test_list):
    average = sum(test_list) / float(len(test_list))
    return [round(average - value, 2) for value in test_list]