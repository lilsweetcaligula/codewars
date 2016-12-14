def group_check(s):
    left_parens = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    right_parens = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for char in s:
        if char in left_parens:
            stack.append(char)
        elif char in right_parens:
            if len(stack) == 0 or right_parens[char] != stack[-1]:
                return False
            else:
                stack.pop()
    return len(stack) == 0
                