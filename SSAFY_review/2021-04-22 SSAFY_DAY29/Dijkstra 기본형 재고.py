# Dijkstra
# Dijkstra 알고리즘을 사용하여 주어진 그래프에 a를 시작정점으로 하여 모든 다른 정점까지의 최단거리(비용)를 계산하여 출력한다
# 정점은 'a'부터 시작하여 'b', 'c'와 같이 나열되며 25개를 넘지 않는다. 방향성 그래프이며, 간선에 가중치 정보가 있다.
# 입력 정보는
# 각 test_case 마다
# 첫 번째 줄에 정점의수 간선의수가 주어지며
# 다음 줄 부터 간선의 정보가 출발 도착 가중치 순서로 주어진다.


def dijkstra(s):
    U = [0]*(V)
    D = [float('inf')]*V
    D[s] = 0
    # 원래 여기서 시작 정점의 첫 시행을 미리 해줬는데, 불필요한 것 같다. U[s] = 1과 시작 정점의 인접 정점들에 대한 처리를 해주었었다.
    # 대신 check라는 set을 이용해서 가장 작은 D값을 가질 수 있는 정점 후보군을 만든다.
    check = {s}
    for _ in range(V):
        v = min((D[x], x) for x in check if not U[x])[1]
        U[v] = 1
        check.remove(v)
        for w, c in AL[v]:
            D[w] = min(D[w], D[v]+c)
            check.add(w)

    return D


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V)]
    for _ in range(E):
        s, e, c = input().split()
        AL[ord(s)-97].append((ord(e)-97, int(c)))

    result = dijkstra(0)
    print('#%d %s' % (t, ' '.join(map(str, result))))