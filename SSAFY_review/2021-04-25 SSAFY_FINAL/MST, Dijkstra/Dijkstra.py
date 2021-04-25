# Dijkstra
# Dijkstra 알고리즘을 사용하여 주어진 그래프에 a를 시작정점으로 하여 모든 다른 정점까지의 최단거리(비용)를 계산하여 출력한다
# 정점은 'a'부터 시작하여 'b', 'c'와 같이 나열되며 25개를 넘지 않는다. 방향성 그래프이며, 간선에 가중치 정보가 있다.
# 입력 정보는
# 각 test_case 마다
# 첫 번째 줄에 정점의수 간선의수가 주어지며
# 다음 줄 부터 간선의 정보가 출발 도착 가중치 순서로 주어진다.


# def dijkstra(s):
#     U = [0]*V
#     D = [float('inf')]*V
#     D[s] = 0
#     for _ in range(V):
#         min_v = float('inf')
#         for i, d in enumerate(D):
#             if not U[i] and d < min_v:
#                 min_v, v = d, i
#
#         U[v] = 1
#         for e, w in AL[v]:
#             D[e] = min(D[e], D[v] + int(w))
#
#     return D


def dijkstra(s):
    D = [float('inf')]*V
    D[s] = 0
    queue = [s]
    front = 0
    while front < len(queue):
        v = queue[front]
        front += 1
        for e, w in AL[v]:
            if D[e] > D[v] + int(w):
                D[e] = D[v] + int(w)
                queue.append(e)

    return D


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V)]
    for _ in range(E):
        s, e, w = input().split()
        AL[ord(s)-97].append((ord(e)-97, w))

    result = dijkstra(0)
    print('#%d %s' % (t, ' '.join(map(str, result))))
