def solution(want, number, discount):
    answer = 0
    cnt_dict = dict()
    for i, ele in enumerate(want):
        cnt_dict[ele] = number[i]
    dl = len(discount)
    for i in range(dl - 9):
        temp_dict = cnt_dict.copy()
        for j in range(i, i + 10):
            dc = discount[j]
            if dc in temp_dict and temp_dict[dc] > 0:
                temp_dict[dc] -= 1
            else:
                break
        satisfied = True
        for val in temp_dict.values():
            if val != 0:
                satisfied = False
                break
        if satisfied:
            answer += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"],	[3, 2, 2, 2, 1],	["chicken", "apple", "apple",
      "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))  # 3
print(solution(["apple"],	[10],	["banana", "banana", "banana", "banana",
      "banana", "banana", "banana", "banana", "banana", "banana"]))  # 0
