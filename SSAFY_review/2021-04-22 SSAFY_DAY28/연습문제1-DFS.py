# DFS
# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다. 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오.
# 시작 정점을 1로 시작하시오.
# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
# 출력 결과의 예는 다음과 같다.
# 1-2-4-6-5-7-3  (다만, 본 문제에서는 채점을 위해 여러 개의 연결된 정점이 있다면 작은 번호를 먼저 선택하도록 합니다.)
# 1-3-7-6-5-2-4


def DFS(v):
    for w in AL[v]:
        if not visited[w]:
            visited[w] = 1
            way.append(w)
            DFS(w)


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)

    visited = [0]*(V+1)
    way = [1]
    visited[1] = 1
    DFS(1)
    print('#%d %s' % (t, '-'.join(map(str, way))))