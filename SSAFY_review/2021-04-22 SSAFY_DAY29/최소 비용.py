# 최소 비용
# 출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.
# 다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.
# (표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)
# 인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.
# 이동 가능한 지역의 높이 정보에 따라 최소 연료 소비량을 출력하는 프로그램을 만드시오.


# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 표의 가로, 세로 칸수N, 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공된다.
# 1<=T<=50, 3<=N<=100, 0<=H<1000


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 다익스트라의 2차원 배열용이다. 기본 다익스트라와 구조가 똑같고, 방문하지 않은 최소 D값을 지닌 정점을 찾기 위한 작업의 시간 단축을 위해
# check라는 set을 사용하는 것만 추가되었다. 이는 기본 다익스트라에서도 사용이 가능할 것이다.
# 또, 기본 다익스트라에서는 D[0]에 대한 시행을 먼저 해줬는데, 사실 안해줘도 된다.
def dijkstra(sr, sc):
    U = [[0]*N for _ in range(N)]
    D = [[float('inf')]*N for _ in range(N)]
    D[sr][sc] = 0
    # 이 부분이 핵심. 다익스트라에서는 방문하지 않은 정점들의 D값 중 가장 작은 D값을 가지는 정점을 다음에 시행의 대상으로 하는데,
    # 코드의 흐름대로 생각해보면, 방문하지 않았으면서 D값이 inf가 아닌 후보군은 현재 D값이 업데이트 된 녀석들이다.
    # 즉, 인접 정점들 중 D값이 갱신된 녀석들
    check = {(0, 0)}
    for _ in range(V):
        # check내에서 방문하지 않고 D값이 최소인 정점 찾기
        r, c = min((D[i][j], (i, j)) for i, j in check if not U[i][j])[1]

        # 시행의 대상이 된 정점은 최단 거리가 확정된 것이다. 방문 처리를 하고 check에서도 없애준다.(안없애면 시간 초과)
        U[r][c] = 1
        check.remove((r, c))

        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                w = 1 if arr[nr][nc] - arr[r][c] <= 0 else arr[nr][nc] - arr[r][c] + 1
                if D[nr][nc] > D[r][c] + w:
                    D[nr][nc] = D[r][c] + w
                    check.add((nr, nc))

    return D[N-1][N-1]


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(1, int(input())+1):
    N = int(input())
    V = N**2
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#%d %d' % (t, dijkstra(0, 0)))


# 2
# BFS 풀이
# 2차원에서의 성능은 이게 더 좋다
# 유방향 가중치 그래프에서 BFS는 visited가 아닌 cost의 느낌으로 사용해서 푼다.(여기서는 cnt)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def search():
    q = [[0, 0]]
    cnt = [[987654321] * N for _ in range(N)]
    cnt[0][0] = 0
    while q:
        cr, cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                height = (area[nr][nc] - area[cr][cc]) if area[nr][nc] > area[cr][cc] else 0
                if cnt[nr][nc] > cnt[cr][cc] + 1 + height:
                    cnt[nr][nc] = cnt[cr][cc] + 1 + height
                    q.append([nr, nc])
    return cnt[-1][-1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    result = search()
    print('#%d %d' % (t, result))