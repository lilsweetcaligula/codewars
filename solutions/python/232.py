def next_id(arr):
    return (arr or 0) and sorted(set(range(0, max(arr) + 2)).difference(set(arr)))[0]
    