def solution(tickets):
    answer = []
    air_dict = dict()
    visited = dict()
    for depart, dest in tickets:
        if depart in air_dict:
            air_dict[depart].append(dest)
            visited[depart] += 1
        else:
            air_dict[depart] = [dest]
            visited[depart] = 1
    for k in air_dict:
        air_dict[k].sort(reverse=True)
    print(air_dict)
    vertex = ""
    stack = ["ICN"]
    route = []
    while stack:
        vertex = stack.pop()
        if vertex in visited and 1 > visited[vertex]:
            continue
        route.append(vertex)
        visited[vertex] -= 1
        for ele in air_dict[vertex]:
            stack.append(ele)
    print(route)
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"],
                ["JFK", "HND"]]))  # ["ICN", "JFK", "HND", "IAD"]
print(
    solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],
              ["ATL", "SFO"]]))  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
