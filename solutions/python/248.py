def winner(candidates):
    try:
        if (len(candidates) != 3 
            or not all(len(candidate['scores']) in (1,2) and candidate.get('name', False)
                for candidate in candidates)
            or not all(score % 5 == 0 and 5 <= score <= 100 
                for candidate in candidates
                    for score in candidate['scores'])):
            raise ValueError()
        else:
            candidates = filter(
                lambda candidate: 5 <= sum(candidate['scores']) <= 100, candidates)
            return min(candidates, key = lambda candidate: 100 - sum(candidate['scores']))['name']
    except (KeyError, ValueError):
        return False  