def get_format(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def primenumber(x):
    x = int(x)
    if x == 1:
        return False
    for i in range(2, int(x ** (1/2) + 1)):  # 2부터 x의 제곱근까지의 숫자
        if x % i == 0:  # 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True


def solution(n, k):
    org_s = get_format(n, k)
    target_list = [x for x in org_s.split("0") if len(x) > 0]
    answer = 0
    for ele in target_list:
        if primenumber(ele) == True:
            answer += 1
    return answer
