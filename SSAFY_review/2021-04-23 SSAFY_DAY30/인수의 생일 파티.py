# 인수의 생일 파티
# 인수가 사는 마을에는 N개의 집이 있고, 각 집에는 한 명의 사람이 살고 있다.
# N개의 집을 정점으로 볼 때, 도로는 어떤 집에서 다른 어떤 집으로 이동이 가능한 단방향 간선으로 볼 수 있으며, 각각에 대해서 이동하는데 시간이 정해져 있다.
# 도로는 모든 집들 간에 이동이 가능하도록 구성되어 있다.
# 집에 1번에서 N번까지의 번호를 붙일 때, 인수의 집은 X번 집이다.
# 오늘은 인수의 생일이기 때문에 모든 마을 사람들이 인수의 생일을 축하해주기 위해 X번 집으로 모인다.
# 각 사람들은 자신의 집에서 X번 집으로 오고 가기 위해 최단 시간으로 이동한다.
# 도로가 단 방향이기 때문에 이용하는 도로는 오고 갈 때 다를 것이다.
# X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집은 어느 정도 걸리는지 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 세 정수 N,M,X(1 ≤ X ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000)가 공백으로 구분되어 주어진다.
# 다음 M개의 각 줄에는 세 정수 x, y, c (1 ≤ x, y ＜ N, 1 ≤ c ≤ 100)가 공백으로 구분되어 주어진다.
# 이는 x번 집에서 y번 집으로 가는 데 시간이 c가 걸리는 단 방향 도로가 존재한다는 뜻이다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 오고 가는데 걸리는 시간이 가장 긴 거리를 출력한다.


# 모든 N번의 집에서 X번으로 갔다가 X번에서 모든 N번으로 가는 비용을 알아야 한다.
# 이를 나눠 따져보면, X번에서 모든 N번으로 가는 것은 X에서의 Dijkstra를 단순히 사용하면 될 것이다.
# 하지만, 모든 N번의 집에서 X번으로 가는 경우를 따질 때, 모든 N에서의 Dijkstra를 구할 것인가? -> 아니다.
# N에서 X로 가는 길을 반전시킨다. 즉, 비용이 똑같은 X에서 N으로 가는 길로 만들어버린다. 이후 X에서 Dijkstra를 하면 각 N에서 오는 길의 비용을 구할 수 있다.
def dijkstra(X, AL):
    U = [0] * (N + 1)
    D = [INF] * (N + 1)
    D[X] = 0
    for _ in range(N):
        min_D = INF
        for i, d in enumerate(D):
            if not U[i] and d < min_D:
                min_D, v = d, i
        U[v] = 1
        for e, w in AL[v]:
            D[e] = min(D[e], D[v] + w)

    return D[1:]


INF = 1e6
for t in range(1, int(input()) + 1):
    N, M, X = map(int, input().split())
    AL = [[] for _ in range(N + 1)]
    r_AL = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        AL[s].append((e, w))
        r_AL[e].append((s, w))

    result = max(a + b for a, b in zip(dijkstra(X, AL), dijkstra(X, r_AL)))
    print('#%d %d' % (t, result))
    
    
# 2
# 다익스트라보다 BFS형이 훨씬 좋다
INF = int(1e9)


def dijkstra(start, graph):
    D = [INF] * (n + 1)
    D[start] = 0
    queue = [start]
    rp = 0
    while rp < len(queue):
        node = queue[rp]
        rp += 1
        for n_node, w in graph[node]:
            d = D[node] + w
            if d < D[n_node]:
                D[n_node] = d
                queue.append(n_node)
    return D[1:]


for t in range(1, int(input()) + 1):
    n, m, x = map(int, input().split())
    graph1, graph2 = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph1[s].append((e, w))
        graph2[e].append((s, w))

    result = max(a + b for a, b in zip(dijkstra(x, graph1), dijkstra(x, graph2)))
    print('#%s %s' % (t, result))