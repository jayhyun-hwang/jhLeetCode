# dict 순회
# for k in dict_name:
# for k in dict_name.keys():
# for v in dict_name.values():
# for k, v in dict_name.items():
def solution(clothes):
    c_dict = dict()
    for name, key in clothes:
        if key not in c_dict:
            c_dict[key] = []
        c_dict[key].append(name)
    answer = 1
    for v in c_dict.values():
        answer *= len(v) + 1
    return answer - 1


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
print(solution([["crow_mask", "face"], [
      "blue_sunglasses", "face"], ["smoky_makeup", "face"]]))  # 3
