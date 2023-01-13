def find_max_palindrome(s: str) -> int:
    for i, val in enumerate(s):
        if i == len(s) // 2:
            return len(s)
        if val == s[len(s) - 1 - i]:
            continue


def solution(s: str) -> int:
    answer = 0
    max_palindrome = 0
    find_max_palindrome(s)
    # for i, val in enumerate(s):

    return answer


print(solution("abcdcba"))
print(solution("abacde"))