# live 중 DFS 연습문제 3
# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오.
# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7


# DFS 재귀
V, E = 7, 8
# 입력이 아래와 같다면
edges = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
edges = list(map(int, edges.split())) # input().split()으로 쓰게 될 것
edges = [(edges[i], edges[i+1]) for i in range(0, len(edges), 2)]
# 입력이 아래와 같다면
# 7 8
# 1 2
# 1 3
# 2 4
# 3 5
# 4 6
# 5 6
# 6 7
# 3 7
# edges = [tuple(map(int, input().split())) for _ in range(E)]


# 인접행렬
AM = [[0]*(V+1) for _ in range(V+1)]
for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1 # 방향성이 없을 때만 이 문장이 추가된다.


# 인접리스트
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s) # 방향성이 없을 때만 이 문장이 추가된다.


# DFS 재귀 구현
# 반복에서와 다르게 v는 방문되지 않은 정점으로, 방문하러 들어온 것
# visited[v] = 1 -> 방문처리를 한다.
# 방문하지 않은 인접요소들을 찾아 DFS를 재호출
# 문제는 visited다. 여러 테스트 케이스를 받으면 각 테스트 케이스마다 visited를 초기화 해야 할 것
def DFS(AL, v):
    visited[v] = 1
    way.append(v)

    for w in AL[v]:
        if not visited[w]:
            DFS(AL, w)
            
            
visited = [0]*(V+1)
way = []
DFS(AL, 1)
print(way)