# 깊이가 있는 그래프 탐색에 유리
# keyword) 그래프 깊이가 깊다. 모든 경로 추적. 해를 찾을 때까지 추적. 미로추적. 당신을 알 수 있는 친구 찾기
# 탐색대상 스택으로 구현

graph = {
  0: [1, 2, 4],
  1: [0, 3],
  2: [0],
  3: [1, 5],
  4: [0],
  5: [3],
}

# visited - set() 필수
# route - 탐색 경로, visited로 대체 가능(순서 보장 X)
# stack - 탐색 대상(LIFO). 비어있지 않으면 계속 진행. 재귀로 대체 가능
# vertex - 현재 노드. 임시 변수 필수

def dfs(graph, start):
    visited = set()
    route = []
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        route.append(vertex)
        visited.add(vertex)
        
        stack.extend(reversed(graph[vertex]))
    
    return route
  
print(dfs(graph, 0))
