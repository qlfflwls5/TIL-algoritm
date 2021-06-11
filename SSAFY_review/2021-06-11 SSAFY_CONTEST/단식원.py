# 단식원
# 올 해에는 꼭 다이어트를 성공하고 싶은 싸피는 단식원에 들어가기로 결심했다.
# 그런데 함께 단식원에 들어온 사람들 중 치킨의 유혹을 뿌리치지 못한 사람들이 몰래 치킨을 사 먹는 일이 발생했다.
# 싸피는 치킨 냄새가 퍼지지 않도록 탈취제를 뿌리려고 한다.
# 단식원은 크기가 N x M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
# 단식원은 아무런 냄새가 나지 않는 빈칸, 탈취제를 뿌린 칸, 치킨 냄새가 나는 칸으로 나뉜다.

# 일부 칸은 치킨 냄새가 나는 칸이며, 이 치킨 냄새는 상하좌우로 인접한 빈칸으로 모두 퍼져 나갈 수 있다.
# 새로 탈취제를 뿌릴 칸의 개수는 3개이며, 꼭 3개의 칸을 확보해야 한다.
# 예를 들어, 아래와 같이 단식원이 생긴 경우를 살펴보자.

# 이때, 0은 아무런 냄새가 나지 않는 빈칸, 1은 탈취제를 뿌린 칸, 2는 치킨 냄새가 나는 칸이다.
# 탈취제를 뿌리지 않는다면, 치킨냄새는 모든 빈 칸으로 퍼져 나갈 수 있다.

# 1행5열, 2행4열, 4행4열에 탈취제를 뿌린다면 단식원의 모양은 아래와 같아지게 된다.
# 치킨냄새가 퍼진 뒤의 모습은 아래와 같아진다.
# 탈취제를 뿌린 3칸을 만든 뒤, 치킨냄새가 퍼질 수 없는 곳을 '날씬이존'이라고 한다. 위의 지도에서 날씬이존의 크기는 27이다.
# 단식원의 지도가 주어졌을 때 얻을 수 있는 날씬이존 크기의 최댓값을 구하는 프로그램을 작성하시오.


# [입력]
# 입력 파일의 첫 번째 줄에는 테스트케이스의 수 T가 주어진다. 그 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 5개의 테스트케이스가 주어진다.
# 테스트케이스의 첫째 줄에 단식원의 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 아무런 냄새가 나지 않는 빈 칸, 1은 탈취제를 뿌린 칸, 2는 치킨냄새가 나는 칸이다.
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈칸의 개수는 3개 이상이다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 얻을 수 있는 날씬이존의 최대 크기를 출력한다.


def bfs(sr, sc):
    queue = [(sr, sc)]
    rear = 0
    while rear < len(queue):
        r, c = queue[rear]
        rear += 1
        arr[r][c] = 2
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                queue.append((nr, nc))


def dfs(level, idx):
    global arr
    if level == 3:
        for r, c in chicken:
            bfs(r, c)

        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
                    global max_v
                    max_v = max(max_v, cnt)

        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2 and (i, j) not in chicken:
                    arr[i][j] = 0

        return

    for i in range(idx, len(possible) - 3 + level + 1):
        r, c = possible[i]
        arr[r][c] = 1
        dfs(level + 1, i + 1)
        arr[r][c] = 0


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    possible = []
    chicken = set()
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                possible.append((i, j))

            if arr[i][j] == 2:
                chicken.add((i, j))

    max_v = 0
    dfs(0, 0)

    print('#%d %d' % (t, max_v))