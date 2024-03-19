def solution(s):
    answer = 0
    sl = len(s)
    merged = s*2
    for i in range(sl):
        stack = []
        for j in range(i, i + sl):
            val = merged[j]
            if val == '(' or val == '{' or val == '[':
                stack.append(val)
            elif val == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(val)
                    break
            elif val == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(val)
                    break
            elif val == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(val)
                    break
        if len(stack) == 0:
            answer += 1
    return answer


print(solution("[](){}"))  # 3
print(solution("}]()[{"))  # 2
print(solution("[)(]"))  # 0
print(solution("}}}"))  # 0
