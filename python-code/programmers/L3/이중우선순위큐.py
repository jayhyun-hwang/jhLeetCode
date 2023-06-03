import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    for op in operations:
        [command, n_str] = op.split(" ")
        n = int(n_str)
        if command == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
        elif command == "D" and n == 1:
            if len(max_heap) < 1:
                continue
            heapq.heappop(max_heap)
            min_heap = []
            for ele in max_heap:
                heapq.heappush(min_heap, -ele)
        elif command == "D" and n == -1:
            if len(min_heap) < 1:
                continue
            heapq.heappop(min_heap)
            max_heap = []
            for ele in min_heap:
                heapq.heappush(max_heap, -ele)
    answer = [0,0] if len(min_heap) < 1 else [-(heapq.heappop(max_heap)), heapq.heappop(min_heap)]
            
    return answer


# [0,0]
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

# [333, -45]
print(
    solution([
        "I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1",
        "I 333"
    ]))
