import heapq


def solution(s):
    s = s[1:-1]
    temp_list = []
    is_open = False
    heap = []
    num_str = ""
    for ele in s:
        if ele == "{":
            temp_list = []
            is_open = True
        elif ele == "}":
            is_open = False
            temp_list.append(int(num_str))
            heapq.heappush(heap, (len(temp_list), tuple(temp_list)))
            num_str = ""
        elif ele == ",":
            if is_open:
                temp_list.append(int(num_str))
                num_str = ""
        else:
            num_str += ele
    res_set = set()
    answer = []
    while heap:
        _, tp = heapq.heappop(heap)
        for ele in tp:
            if ele not in res_set:
                answer.append(ele)
                res_set.add(ele)
    return answer
