def find_parent(p, tree):
    if p == tree[p]:
        return p
    return find_parent(tree[p], tree)

def union_node(a, b, tree):
    p = min(find_parent(a, tree), find_parent(b, tree))
    tree[a] = p
    tree[b] = p

def solution(n, costs):
    if n < 1:
        return 0
    answer = 0
    print(costs)
    costs.sort(key=lambda x : x[2])
    print(costs)
    parent_tree = []
    remain_set = set()
    for i in range(n):
        remain_set.add(i)
        parent_tree.append(i)
    print(remain_set)
    union_node(costs[0][0], costs[0][1], parent_tree)
    root = parent_tree[costs[0][0]]
    cur_cost = costs[0][2]
    for ele in costs:
        p1 = find_parent(ele[0], parent_tree)
        p2 = find_parent(ele[1], parent_tree)
        if p1 != root or p2 != root:
            union_node(ele[0], ele[1], parent_tree)
            cur_cost += ele[2]
    answer = cur_cost
    return answer