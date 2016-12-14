in_asc_order = (lambda arr: 
    all(arr[index - 1] < arr[index] for index in range(1, len(arr))))