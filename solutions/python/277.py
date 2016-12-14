def solution(s, step = 2):
    s = s + '_' if len(s) % 2 else s
    return [s[start:start + step] for start in range(0, len(s), step)]