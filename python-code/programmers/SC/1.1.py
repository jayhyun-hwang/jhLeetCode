def solution(num: int) -> bool:
    sep = num
    nums = []
    while(True):
        if sep < 10:
            nums.append(sep)
            break
        rem = sep % 10
        nums.append(rem)
        sep //= 10
    div = sum(nums)
    if num % div == 0:
        return True
    return False

print(solution(17))