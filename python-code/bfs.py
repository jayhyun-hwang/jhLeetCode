# 깊이가 얕은 그래프 탐색에 유리
# keyword) 최단경로(네이게이션). 그래프가 얕다. P2P에서 가까운 Peer를 찾을 때.
# 탐색대상 큐로 구현

graph = {
  0: [1, 2, 4],
  1: [0, 3],
  2: [0],
  3: [1, 5],
  4: [0],
  5: [3],
}

# visited - set 방문한 노드. 필수
# route - 경로를 담은 자료구조. visited로 대체 가능
# queue - 탐색 대상 자료구조(FIFO). 비어있지 않으면 계속 진행. 필수
# vertex - 현재 노드. 임시 변수 필수
import collections

def bfs(graph, start):
    visited = set()
    route = []
    queue = collections.deque([])
    
    queue.append(start)
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        route.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append(neighbor)
    
    return route
  
print(bfs(graph, 0))
