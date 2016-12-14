def generator (from_, to_, step_):
    try:
        return(
            list(range(from_, to_ + 1, step_)) if from_ < to_ 
                else list(range(from_, to_ - 1, -step_)))
    except ValueError:
        return []