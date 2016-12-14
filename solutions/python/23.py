def range_parser(string):
    tokens = string.split(',')
    result = []
    for token in tokens:
        limits_str, _, step_str = token.partition(':')
        start_str, _, end_str = limits_str.partition('-')
        start = int(start_str)
        step = int(step_str) if step_str else 1
        end = 1 + (int(end_str) if end_str else start)
        subrange = range(start, end, step)
        result.extend(subrange)
    return result