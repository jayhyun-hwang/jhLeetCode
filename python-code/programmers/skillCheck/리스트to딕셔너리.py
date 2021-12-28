from typing import List

# List.remove 루프 사용 시 주의
# for ele in list: 루프에서 ele는 index로 접근하며, syntax 실행 시의 인덱스를 유지하므로,
# iterate 중 인 리스트가 변경될 경우, 잘못된 접근을 할 가능성이 높다.
# 이 문제의 경우, 해당 element가 삭제되었을 때, 다음 인덱스에 접근하지 못하고, 하나 건너 다음 value로 element 접근을 하는 문제가 있었다.
def solution(n: int, lost: List[int], reserve: List[int]) -> int:
    answer = -1

    lostDict = {val: True for val in lost}
    for val in lost:
        if val in reserve:
            del lostDict[val]
            reserve.remove(val)
    
    # 문제의 loop 부분
    # for val in lost:
    #     print("val",val)
    #     print("lost1",lost)
    #     print("reserve1", reserve)
    #     if val in reserve:
    #         lost.remove(val)
    #         reserve.remove(val)
    #     print("lost2",lost)
    #     print("reserve2", reserve)
    # lostDict = {val: True for val in lost}

    print(lost)
    print(lostDict)
    reserve.sort()
    for val in reserve:
        if val - 1 in lostDict:
            del lostDict[val - 1]
            continue
        if val + 1 in lostDict:
            del lostDict[val + 1]
            continue
    print(lostDict)
    answer = n - len(lostDict)
    return answer


# print(solution(6, [2, 4, 6], [1, 3, 5, 6]))
print(solution(9, [5, 6, 8, 1, 2], [2, 3, 1, 4, 8, 9]))
# print(solution(5, [2, 4], [3]))
# print(solution(3, [3], [1]))