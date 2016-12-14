def max_rot(n):
    digits = str(n)
    candidates = []
    for start in range(len(digits)):
        candidate = int(digits)
        candidates.append(candidate)        
        left   = digits[:start]
        right  = digits[start + 1:] + digits[start]
        digits = left + right
    return max(candidates)