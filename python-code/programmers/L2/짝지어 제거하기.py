def solution(s):
    stack = []
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return 1 if len(stack) == 0 else 0


print(solution("baabaa")) # 1
print(solution("cdcd")) # 0
