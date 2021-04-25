# 최소 신장 트리
# 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.
# 0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
# 다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다.
# 1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 1
# prim
def prim(s):
    MST = [0]*(V+1)
    D = [float('inf')]*(V+1)
    D[s] = 0
    for _ in range(V+1):
        min_v = float('inf')
        for i, d in enumerate(D):
            if not MST[i] and d < min_v:
                v, min_v = i, d

    MST[v] = 1
    for e, w in AL[v]:
        if not MST[e]:
            D[e] = min(D[e], w)
    print(D)
    return sum(D)


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        AL[s].append((e, w))
        AL[e].append((s, w))

    print('#%d %d' % (t, prim(0)))


# 2
# kruskal
def find_set(x):
    if x != p[x]:
        x = p[x]

    return x


def kruskal():
    S = 0
    cnt = 0
    for s, e, w in edges:
        rep_s, rep_e = find_set(s), find_set(e)
        if rep_s != rep_e:
            S += w
            cnt += 1
            p[rep_e] = rep_s
            if cnt == V:
                break

    return S


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    p = [i for i in range(V+1)]
    edges = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    print('#%d %d' % (t, kruskal()))
