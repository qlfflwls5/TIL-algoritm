# Dijkstra
# Dijkstra 알고리즘을 사용하여 주어진 그래프에 a를 시작정점으로 하여 모든 다른 정점까지의 최단거리(비용)를 계산하여 출력한다
# 정점은 'a'부터 시작하여 'b', 'c'와 같이 나열되며 25개를 넘지 않는다. 방향성 그래프이며, 간선에 가중치 정보가 있다.
# 입력 정보는
# 각 test_case 마다
# 첫 번째 줄에 정점의수 간선의수가 주어지며
# 다음 줄 부터 간선의 정보가 출발 도착 가중치 순서로 주어진다.


def dijkstra(s):
    # U: 방문 처리용, D: 시작 정점으로부터 각 정점까지의 최단 거리
    U = [0]*(V)
    D = [float('inf')]*V

    # 먼저 시작 정점에 대한 1시행 처리
    U[s] = 1
    D[s] = 0
    for w, c in AL[s]:
        D[w] = c

    # 시작 정점 이외의 나머지 정점에 대한 처리
    for _ in range(V-1):
        # 방문하지 않은 정점 중에 D값이 가장 작은 정점에 대해, 방문 처리하고, 인접 정점들의 최단 거리를 필요하면 갱신
        # 수정 1: min을 위해서 리스트를 만들기 위한 대괄호 안써도 된다. iterator는 min그냥 가능
        # 수정 2: 기존 코드는 v = D.index(min([D[x] for x in range(V) if not U[x]]))였다. 이렇게 하면 가중치가 같은 녀석들의 경우 단순히 D에서 index로 찾아오므로 문제가 발생
        #         따라서, 방문하지 않은 index에 대해서만 고려할 수 있도록 해야 한다.
        v = min((D[x], x) for x in range(V) if not U[x])[1]
        U[v] = 1
        for w, c in AL[v]:
            D[w] = min(D[w], D[v]+c)

    return D


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V)]
    for _ in range(E):
        s, e, c = input().split()
        AL[ord(s)-97].append((ord(e)-97, int(c)))

    result = dijkstra(0)
    print('#%d %s' % (t, ' '.join(map(str, result))))