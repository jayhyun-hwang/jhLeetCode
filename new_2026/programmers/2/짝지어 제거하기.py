def solution(s):
    stack = []
    pre = ""
    for val in s:
        if val == pre:
            stack.pop()
            pre = stack[-1] if stack else ""
        else:
            stack.append(val)
            pre = val
    return 1 if len(stack) == 0 else 0
