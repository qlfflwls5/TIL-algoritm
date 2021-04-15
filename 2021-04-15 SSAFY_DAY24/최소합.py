# 최소합
# 그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
# 그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# DP
# 각 칸에서 왼쪽과 위쪽 칸까지 오는 동안의 최소 비용을 택한다.
for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        arr[0][i] += arr[0][i-1]
        arr[i][0] += arr[i-1][0]

    for i in range(1, N):
        for j in range(1, N):
            arr[i][j] += min(arr[i-1][j], arr[i][j-1])

    print('#%d %d' % (t, arr[N-1][N-1]))


# 2
# BFS
# 비가중치 그래프이기 때문에 visited를 사용할 수 없다.(다른 경우에서 또 방문해야 할 수도 있기 때문에)
# 대신 cost를 통해서 방문을 구현할 수 있다.
dr = [0, 1]
dc = [1, 0]


def BFS(sr, sc):
    q = [[sr, sc]]
    cost[sr][sc] = arr[sr][sc]

    while q:
        cr, cc = q.pop(0)
        for i in range(2):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if nr < N and nc < N:
                temp = cost[cr][cc] + arr[nr][nc]
                # 아직 방문을 안한 곳이거나, 이전 방문보다 현재 방문이 더 최소합인 경우 cost 업데이트
                if cost[nr][nc] == 0 or cost[nr][nc] > temp:
                    cost[nr][nc] = temp
                    # 현재 경로가 최소합인 경우에만 큐에 넣고 나아간다. 최소합이 아니라면 여기서 중단됨
                    q.append([nr, nc])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0] * N for _ in range(N)]
    BFS(0, 0)
    print('#%d %d' % (t, cost[N - 1][N - 1]))