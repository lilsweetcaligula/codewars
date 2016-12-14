averages = (lambda arr: 
    [sum(pair) / len(pair) for pair in zip(arr, arr[1:])] if arr else [])