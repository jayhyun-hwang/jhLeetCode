def solution(tickets):
    answer = []
    n = len(tickets)
    can_go = dict()
    for dep, dest in tickets:
        if dep not in can_go:
            can_go[dep] = dict()
        if dest not in can_go[dep]:
            can_go[dep][dest] = 0
        can_go[dep][dest] += 1
    stack = ["ICN"]
    route = []
    vertex = ""
    before = ""
    print(can_go)
    while stack:
        before = vertex
        vertex = stack.pop()
        if before != "":
            if vertex in can_go[before]:
                can_go[before][vertex] -= 1
        if vertex not in can_go:
            can_go[vertex] = dict()
        appendable = []
        for go, count in can_go[vertex].items():
            if count > 0:
                appendable.append(go)
        if len(appendable) < 1:
            if len(route) == n:
                route.append(vertex)
                return route
            can_go[before][vertex] += 1
            if len(route) >= 2 :
                can_go[route[-2]][before] += 1
            route.pop()
            continue
        route.append(vertex)
        appendable.sort(reverse=True)
        for ele in appendable:
            stack.append(ele)
        print(vertex, appendable)
        # print(stack)
        # print(route)
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"],
                ["JFK", "HND"]]))  # ["ICN", "JFK", "HND", "IAD"]
print(
    solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],
              ["ATL", "SFO"]]))  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution([["ICN", "JFK"], ["ICN", "AAD"],
                ["JFK", "ICN"]]))  # ["ICN", "JFK", "ICN", "AAD"]
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))  # ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"],
                ["B", "D"]]))  #["ICN", "A", "C", "A", "B", "D"]
