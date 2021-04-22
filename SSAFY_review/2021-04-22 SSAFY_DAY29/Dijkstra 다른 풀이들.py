# 1
# 딕셔너리를 이용해 가독성은 떨어져도 효율이 좋은 코드
def dijkstra(s):
    # s : 시작 값
    # U: 방문표시
    U = {s: 1}
    # D : 가중치의 최솟값
    D = {x: float('inf') for x in graph}
    D[s] = 0
    for i in graph.get(s):  # graph.get(s): {'c': 5, 'b': 3}, i: 'c', 'b'(순서는 모름)
        D[i] = graph.get(s).get(i)
    queue = [s]
    # 모든정점에 대해
    while queue:
        x = queue.pop(0)
        # D[w]가 최소인 정점 w 선택
        if graph.get(x):    # x에 연결된 정점들이 있으면
            for i in sorted(D.items(), key=lambda x: x[1]):
                if not U.get(i[0]):
                    w = i[0]
                    queue.append(w)
                    U[w] = 1
                    # w에 인접한 모든 정점 v
                    for v in graph.get(w).keys():
                        D[v] = min(D.get(v), D.get(w) + graph.get(w).get(v))
                    break

    return D


for tc in range(1, 1 + int(input())):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    graph = {chr(x): {} for x in range(ord('a'), ord('a') + N)}

    for i in range(E):
        u, v, w = input().split()
        if graph.get(u):
            if graph.get(u).get(v):
                graph[u][v].add(int(w))
            else:
                graph[u][v] = int(w)
        else:
            graph[u] = {v: int(w)}

    # print(graph)
    res = dijkstra('a')
    ans = [res.get(i) for i in sorted(graph)]
    print('#{} {}'.format(tc, ' '.join(map(str, ans))))


# 2
# 다익스트라 재귀
def dijkstra(i, w):
    for end, weight in adj_list[i]:
        if D[end] > w + weight:
            D[end] = w + weight
            dijkstra(end, w + weight)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    D = [float('inf')] * N
    adj_list = [[] for _ in range(N)]
    for _ in range(M):
        s, e, w = input().split()
        adj_list[ord(s) - 97].append((ord(e) - 97, int(w)))
    D[0] = 0
    dijkstra(0, 0)
    ans = ' '.join(map(str, D))
    print('#%d %s' % (test_case, ans))