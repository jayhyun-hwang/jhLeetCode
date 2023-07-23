def find(a, parents):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a], parents)
    return parents[a]


def union(a, b, parents):
    a_parent = find(a, parents)
    b_parent = find(b, parents)
    u_parent = min(a_parent, b_parent)
    parents[a_parent] = u_parent
    parents[b_parent] = u_parent


def solution(n, costs):
    if n < 1:
        return 0
    answer = 0
    # costs.sort(key=lambda x : x[2])
    sorted_costs = sorted(costs, key=lambda x: x[2])
    parent_arr = []
    for i in range(n):
        parent_arr.append(i)
    union(sorted_costs[0][0], sorted_costs[0][1], parent_arr)
    cost = sorted_costs[0][2]
    for ele in sorted_costs:
        if find(ele[0], parent_arr) != find(ele[1], parent_arr):
            union(ele[0], ele[1], parent_arr)
            cost += ele[2]
    answer = cost
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])) # 4
print(solution(6, [[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 7], [3, 5, 4], [3, 4, 6], [4, 5, 2]])) # 12
