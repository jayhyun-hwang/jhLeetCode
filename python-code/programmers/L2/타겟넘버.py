def get_numbers(numbers, idx, cur_sum, target, res_list):
    if idx == len(numbers):
        if cur_sum == target:
            res_list.append(True)
        return
    get_numbers(numbers, idx + 1, cur_sum - numbers[idx], target, res_list)
    get_numbers(numbers, idx + 1, cur_sum + numbers[idx], target, res_list)


def solution(numbers, target):
    res_list = []
    get_numbers(numbers, 0, 0, target, res_list)
    answer = len(res_list)
    return answer
