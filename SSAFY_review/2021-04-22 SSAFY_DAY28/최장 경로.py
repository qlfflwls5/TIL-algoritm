# 최장 경로
# N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하자.
# 정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.
# 경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.
# 경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 개의 자연수 N M(1 ≤ N ≤ 10, 0 ≤ M ≤ 20)이 주어진다.
# 두 번째 줄부터 M개의 줄에 걸쳐서 그래프의 간선 정보를 나타내는 두 정수 x y(1 ≤ x, y ≤ N)이 주어진다.
# x와 y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있다.


# [출력]
# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 그래프에서의 최장 경로의 길이를 출력한다.


def DFS_max(v, cnt):
    max_v[0] = max(max_v[0], cnt)
    visited[v] = 1
    for w in AL[v]:
        if not visited[w]:
            DFS_max(w, cnt + 1)
    visited[v] = 0


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    AL = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)

    max_v = [0]
    # 모든 정점에서 다 DFS를 돌려본다.
    for i in range(1, N + 1):
        visited = [0] * (N + 1)
        DFS_max(i, 1)

    print('#%d %d' % (t, max_v[0]))

