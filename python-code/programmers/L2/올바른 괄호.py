def solution(s):
    stack = []
    for ele in s:
        if ele == '(':
            stack.append(ele)
        if ele == ')':
            if len(stack) < 1:
                return False
            stack.pop()
    return True if len(stack) == 0 else False

print(solution("()()")) # true
print(solution("(())()")) # true
print(solution(")()(")) # false
print(solution("(()(")) # false
