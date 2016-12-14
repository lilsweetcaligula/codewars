def example_sort(arr, example_arr):
    lookup = { value: index for index, value in enumerate(example_arr) }
    return sorted(arr, key = lambda value: lookup[value])