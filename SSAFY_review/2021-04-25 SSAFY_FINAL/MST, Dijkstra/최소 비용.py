# 최소 비용
# 출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.
# 다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.
# (표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)
# 인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.


# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 표의 가로, 세로 칸수N, 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공된다.
# 1<=T<=50, 3<=N<=100, 0<=H<1000


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


def dijkstra(sr, sc):
    D = [[INF]*N for _ in range(N)]
    D[sr][sc] = 0
    queue = [(sr, sc)]
    front = 0
    while front < len(queue):
        r, c = queue[front]
        front += 1
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                w = 1 if arr[r][c] >= arr[nr][nc] else arr[nr][nc] - arr[r][c] + 1
                if D[nr][nc] > D[r][c] + w:
                    D[nr][nc] = D[r][c] + w
                    queue.append((nr, nc))

    return D[N-1][N-1]


INF = 1e7
drc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#%d %d' % (t, dijkstra(0, 0)))