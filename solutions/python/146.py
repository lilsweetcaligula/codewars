def score_test(tests, right, omit, wrong):
    counts = (tests.count(answer) for answer in (0, 1, 2))
    scores = map(
        lambda answer, scoring: answer * scoring, 
        (right, omit, -wrong), counts)
    return sum(scores)