def cycle(sequence):
    visited = set()
    for fast_index, value in enumerate(sequence):
        if value in visited:
            for slow_index in range(fast_index):
                if sequence[slow_index] == sequence[fast_index]:
                    return [slow_index, fast_index - slow_index]
        else:
            visited.add(value)
    return []