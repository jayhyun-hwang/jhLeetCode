def solution(n, computers):
    network_count = 0
    visited = set()

    for i, row in enumerate(computers):
        if i in visited:
            continue
        network_count += 1
        stack = []

        stack.append(i)
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            visited.add(vertex)
            tmp_network = computers[vertex]
            for j, val in enumerate(reversed(tmp_network)):
                if val != 1:
                    continue
                idx = n - j - 1
                stack.append(idx)

    return network_count
