# def solution(elements):
#     merged = elements + elements
#     sum_set = set(elements)
#     for i in range(2, len(elements) + 1):
#         left = 0
#         right = i - 1
#         temp_sum = 0
#         for j in range(left, right + 1):
#             temp_sum += merged[j]
#         sum_set.add(temp_sum)
#         for _ in range(len(elements)):
#             temp_sum -= merged[left]
#             left += 1
#             right += 1
#             temp_sum += merged[right]
#             sum_set.add(temp_sum)
#     return len(sum_set)

def solution(elements):
    merged = elements + elements
    sum_set = set()
    for i in range(1, len(elements) + 1):
        left = 0
        right = i - 1
        temp_sum = sum(merged[left:right + 1])
        sum_set.add(temp_sum)
        for _ in range(len(elements)):
            temp_sum -= merged[left]
            left += 1
            right += 1
            temp_sum += merged[right]
            sum_set.add(temp_sum)
    return len(sum_set)


print(solution([7, 9, 1, 1, 4]))  # 18
