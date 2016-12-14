def match(candidate, job, wiggle = 0.1):
    return candidate['min_salary'] - candidate['min_salary'] * wiggle <= job['max_salary']