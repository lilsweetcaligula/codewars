def grader(score):
    predicates = (
        lambda grade: 'D' if 0.6 <= grade < 0.7 else False,
        lambda grade: 'C' if 0.7 <= grade < 0.8 else False,
        lambda grade: 'B' if 0.8 <= grade < 0.9 else False,
        lambda grade: 'A' if 0.9 <= grade <= 1.0 else False,
    )
    for predicate in predicates:
        result = predicate(score)
        if result:
            return result
    return 'F'