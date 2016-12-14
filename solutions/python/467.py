def get_score(n):
    result = 50
    step = 100
    for times in range(n - 1):
        result += step
        step += 50
    return result