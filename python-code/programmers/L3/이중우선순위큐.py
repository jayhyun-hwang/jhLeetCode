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
    answer = [0, 0] if len(
        min_heap) < 1 else [-(heapq.heappop(max_heap)), heapq.heappop(min_heap)]

    return answer


def solution2(operations):
    answer = []
    max_heap = []
    min_heap = []
    for operation in operations:
        # print(operation)
        command, n = operation.split(" ")
        n = int(n)
        if command == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
        elif command == "D":
            if len(max_heap) < 1:
                continue
            if n == 1:
                heapq.heappop(max_heap)
                target = min_heap
                source_heap = max_heap
            else:
                heapq.heappop(min_heap)
                target = max_heap
                source_heap = min_heap
            target.clear()
            for ele in source_heap:
                heapq.heappush(target, -ele)
        # print(min_heap)
        # print(max_heap)
    if len(max_heap) < 1:
        return [0, 0]
    answer.append(heapq.heappop(max_heap) * -1)
    answer.append(heapq.heappop(min_heap))
    return answer


def solution3(operations):
    max_heap = []
    min_heap = []
    for op in operations:
        [cmd, num] = op.split(" ")
        num = int(num)
        if cmd == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -1 * num)
            continue
        # cmd === "D"
        if len(min_heap) < 1:
            continue
        if num == -1:
            popped = min_heap
            target = max_heap
        elif num == 1:
            popped = max_heap
            target = min_heap
        heapq.heappop(popped)
        target.clear()
        for ele in popped:
            heapq.heappush(target, -1 * ele)
    if len(min_heap) < 1:
        return [0, 0]
    answer = [-1 * heapq.heappop(max_heap), heapq.heappop(min_heap)]
    return answer


# [0,0]
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

# [333, -45]
print(
    solution([
        "I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1",
        "I 333"
    ]))

# [0,0]
print(solution2(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

# [333, -45]
print(
    solution2([
        "I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1",
        "I 333"
    ]))


# [0,0]
print(solution3(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

# [333, -45]
print(
    solution3([
        "I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1",
        "I 333"
    ]))


def solution4(operations):
    min_heap = []
    max_heap = []

    for op in operations:
        [command, num_str] = op.split(" ")
        num = int(num_str)
        print(command, num_str)
        if command == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            continue
        if command == "D":
            if len(min_heap) < 1:
                continue
            if num > 0:
                heapq.heappop(max_heap)
                min_heap = []
                for val in max_heap:
                    heapq.heappush(min_heap, -val)
            else:
                heapq.heappop(min_heap)
                max_heap = []
                for val in min_heap:
                    heapq.heappush(max_heap, -val)
    if len(min_heap) < 1:
        return [0, 0]
    return [max(min_heap), min(min_heap)]


# [0,0]
print(solution4(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

# [333, -45]
print(
    solution4([
        "I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1",
        "I 333"
    ]))
