def every(array: list, interval: int = 1, startIndex: int = 0) -> list:
    return array[startIndex::interval]def every(array, interval = None, start_index = None):
    interval = interval if interval and interval > 0 else 1
    start_index = start_index if start_index and start_index > 0 else 0
    return array[start_index::interval]