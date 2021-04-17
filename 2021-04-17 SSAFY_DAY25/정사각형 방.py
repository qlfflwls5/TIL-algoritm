# 정사각형 방
# N^2개의 방이 N×N형태로 늘어서 있다.
# 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N^2 이하의 수 A(i,j)가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
# 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 10^3)이 주어진다.
# 다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N^2) 이 공백 하나로 구분되어 주어진다.
# Ai, j는 모두 서로 다른 수이다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.
# 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.


# [예제 풀이]
# 첫 번째 테스트 케이스는 1 또는 3이 적힌 곳에 있어야 한다.
# 두 번째 테스트 케이스는 3 또는 6이 적힌 곳에 있어야 한다.


# 1
# 각 칸에서 경로를 나아가는 방법
def find_head(r, c):
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and arr[r + dr][c + dc] == arr[r][c] - 1:
            visited[nr][nc] = 1
            r, c = find_head(nr, nc)

    return r, c


def find_tail(r, c):
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and arr[r + dr][c + dc] == arr[r][c] + 1:
            visited[nr][nc] = 1
            r, c = find_tail(nr, nc)

    return r, c


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    way_list = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                sr, sc = find_head(i, j)
                er, ec = find_tail(i, j)
                way_list.append((arr[sr][sc], arr[er][ec] - arr[sr][sc] + 1))

    head, max_room = sorted(way_list, key=lambda x: (-x[1], x[0]))[0]

    print('#%d %d %d' % (t, head, max_room))


# 2
# 라이브 답안
# 결국 연결되려면 주위에 나보다 1 큰 숫자가 있는 것. 1 작은 것은 연결되었다고 생각하지 않는다. 중복이 되니까
# 그리고 나중에 연결된 길이에 1을 더해준다(나 자신)
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * (N ** 2 + 1)
    for r in range(N):
        for c in range(N):
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[r + dr][c + dc] - arr[r][c] == 1:
                    check[arr[r][c]] = 1
                    break

    for i in range(N ** 2, 0, -1):
        if check[i - 1]:
            check[i - 1] += check[i]

    max_room, min_v = 0, 0
    for i in range(N ** 2 + 1):
        if check[i] > max_room:
            max_room, min_v = check[i], i

    print('#%d %d %d' % (t, min_v, max_room + 1))