# 콩 많이 심기
# 콩을 사랑하는 민석이의 취미는 n*m 크기의 사각형 밭에 콩을 늘어놓는 것이다.
# 한 칸에 콩 하나씩을 놓을 수 있는데, 2가 싫은 민석이는 콩들 사이의 길이가 2가 되지 않도록 하면서 최대한 많은 콩을 놓으려고 한다.
# 예를 들어 다음과 같이 콩을 배치할 수 없다.
# 콩1(x1, y1)과 콩2(x2, y2) 사이의 길이는 좌표를 이용해 거리를 구하는 공식으로 구한다.
# 민석이를 도와서 사각형 밭에 최대로 콩을 늘어놓자.


# [입력]
# 첫째 줄에 테스트 케이스의 수 T (1 ≤ T ≤ 10)가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 가로길이 N, 세로길이 M이 주어진다.
# (1 ≤ N, M ≤ 1000)


# [출력]
# 각 테스트 케이스마다 밭에 놓을 수 있는 콩의 최대 개수를 출력하라.


# [HINT]
# 3*2 밭에 콩을 배치하는 경우 다음과 같이 최대 4개를 배치할 수 있다.
# 1 1 0
# 0 1 1


# 1
# 1 1 0 0 1
# 1 1 0 0 1
# 0 0 1 1 0
# 0 0 1 1 0
# 1 1 0 0 1
# 이런식으로 심는 것이 최대다.
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            i_mod, j_mod = i % 4, j % 4
            if (0 <= i_mod <= 1 and 0 <= j_mod <= 1) or (2 <= i_mod <= 3 and 2 <= j_mod <= 3):
                arr[i][j] = 1

    result = 0
    for row in arr:
        result += sum(row)

    print('#%d %d' % (t, result))


# 2
# 델타를 사용해 2칸씩 멀리 떨어진 곳에 불가 체크를 해주기
drc = [(0, 2), (2, 0), (0, -2), (-2, 0)]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [[0]*N for _ in range(M)]
    cnt = 0
    for r in range(M):
        for c in range(N):
            if not grid[r][c]:
                cnt += 1
                for dr, dc in drc:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<M and 0<=nc<N:
                        grid[nr][nc] = 1

    print("#%d %d" % (t, cnt))