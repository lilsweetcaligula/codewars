def smaller(arr):
    return [len(filter(lambda value: value < arr[index], arr[index + 1:])) for index in range(len(arr))]