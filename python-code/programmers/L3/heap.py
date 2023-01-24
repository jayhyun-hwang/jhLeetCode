import heapq


def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    for op in operations:
        cmd = op.split(' ')
        if cmd[0] == 'I':
            num = int(cmd[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        elif cmd[0] == 'D':
            flag = cmd[1]
            if flag == '1':
                if len(max_heap) > 0:
                    heapq.heappop(max_heap)
                    min_heap = []
                    for val in max_heap:
                        heapq.heappush(min_heap, val[1])
            elif flag == '-1':
                if len(min_heap) > 0:
                    heapq.heappop(min_heap)
                    max_heap = []
                    for val in min_heap:
                        heapq.heappush(max_heap, (-val, val))
    max_res = 0 if len(max_heap) < 1 else heapq.heappop(max_heap)[1]
    min_res = 0 if len(min_heap) < 1 else heapq.heappop(min_heap)
    answer.append(max_res)
    answer.append(min_res)
    return answer


# [0,0]
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

# [333, -45]
print(
    solution([
        "I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1",
        "I 333"
    ]))
