# 등산로 조성
# 등산로를 조성하려고 한다.
# 등산로를 만들기 위한 부지는 N * N 크기를 가지고 있으며, 이곳에 최대한 긴 등산로를 만들 계획이다.
# 등산로 부지는 아래 [Fig. 1]과 같이 숫자가 표시된 지도로 주어지며, 각 숫자는 지형의 높이를 나타낸다.
# 등산로를 만드는 규칙은 다음과 같다.

#    ① 등산로는 가장 높은 봉우리에서 시작해야 한다.

#    ② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
#        즉, 높이가 같은 곳 혹은 높은 지형이나, 대각선 방향의 연결은 불가능하다.

#    ③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.

# N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다.
# 이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성하라.


# [예시]
# 9 3 2 3 2
# 6 3 1 7 5
# 3 4 8 9 9
# 2 3 7 7 7
# 7 6 5 5 8
# 위 [Fig. 1]과 같이 N = 5인 지도가 주어진 경우를 살펴보자.
# 가장 높은 봉우리는 높이가 9로 표시된 세 군데이다.
# 이 세 곳에서 출발하는 가장 긴 등산로 중 하나는 (2, 3)에서 시작한 9 - 8 - 4 - 3 - 1과 같고, 이 때 길이는 5가 된다.
# 만약 최대 공사 가능 깊이 K = 1로 주어질 경우,
# 아래 [Fig. 3]과 같이 (2, 3) 부분의 높이를 9에서 8로 깎으면 길이가 6인 등산로를 만들 수 있다. (2, 4)에서 시작 9 - 8 - 7 - 3 - 2 - 1
# 이 예에서 만들 수 있는 가장 긴 등산로는 위와 같으며, 출력할 정답은 6이 된다.


# [제약 사항]
# 1. 시간 제한 : 최대 51개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초
# 2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
# 3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)
# 4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.
# 5. 지도에서 가장 높은 봉우리는 최대 5개이다.
# 6. 지형은 정수 단위로만 깎을 수 있다.
# 7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.


# [입력]
# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K가 차례로 주어진다.
# 그 다음 N개의 줄에는 N * N 크기의 지도 정보가 주어진다.


# [출력]
# 테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
# 각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t는 1부터 시작하는 테스트 케이스의 번호이다)
# 출력해야 할 정답은 만들 수 있는 가장 긴 등산로의 길이이다.


# 가장 높은 곳을 찾는다.
# DFS가 좋을 것 같다.
# 사방 탐색을 통해 낮으면 이동하고, 같거나 높다면 아직 깎는 행위를 안했을 때, 깎아서 더 낮아진다면 깎고 간다.
# 끝까지 이동했을 때의 거리가 현재의 최대 거리보다 길다면 갱신한다.
def DFS(r, c):
    # 가지치기: 현재 위치의 높이 + 깎았으면 0, 안깎았으면 1 + 이전까지의 길이가 max_path보다 같거나 작으면 더 진행 x
    global chance, max_path
    if arr[r][c] + chance + visited[r][c] - 1 <= max_path:
        return

    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                if arr[nr][nc] < arr[r][c]:
                    visited[nr][nc] = visited[r][c] + 1
                    DFS(nr, nc)
                    visited[nr][nc] = 0
                elif chance and arr[nr][nc] - arr[r][c] < K:
                    temp = arr[nr][nc]
                    arr[nr][nc] = arr[r][c] - 1
                    visited[nr][nc] = visited[r][c] + 1
                    chance = 0
                    DFS(nr, nc)
                    arr[nr][nc] = temp
                    visited[nr][nc] = 0
                    chance = 1
                else:
                    if visited[r][c] > max_path:
                        max_path = visited[r][c]


drc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    # max_h는 최대 높이, max_list는 최대 높이를 가진 곳의 좌표 리스트
    max_h, max_list = 0, []
    arr = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] > max_h:
                max_h, max_list = row[j], [(i, j)]
            elif row[j] == max_h:
                max_list.append((i, j))
        arr.append(row)
    # max_path는 최대 길이 산책로, chance는 깎는 기회
    max_path, chance = 0, 1
    visited = [[0]*N for _ in range(N)]
    for r, c in max_list:
        # 한 최고점에서의 탐색 시작을 위해 현재 최고점을 산책로 길이 1로 놓는다.
        visited[r][c] = 1
        DFS(r, c)
        # 한 최고점에서의 탐색이 끝나면 산책로 길이 0으로 초기화.
        visited[r][c] = 0

    print('#%d %d' % (t, max_path))

# visited가 난잡하면 DFS의 인자에 cnt를 넣어서 세자.
# 은교님
# def DFS_recur(r, c, cnt, flag):
#     global mx_length
#     visited[r][c] = 1
#     # 최댓값 갱신
#     if cnt > mx_length:
#         mx_length = cnt
#
#     for dr, dc in drc:
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
#             # 작으면 DFS 호출
#             if mountain[nr][nc] < mountain[r][c]:
#                 DFS_recur(nr, nc, cnt + 1, flag)
#             # 크거나 같은데 차이가 K 미만, 아직 안 깎았으면 깎고 DFS 호출
#             elif mountain[nr][nc] - mountain[r][c] < K and flag:
#                 tmp = mountain[nr][nc] - mountain[r][c] + 1
#                 mountain[nr][nc] -= tmp
#                 DFS_recur(nr, nc, cnt + 1, 0)
#                 # 깎았던 거 원상 복귀
#                 mountain[nr][nc] += tmp
#             else:
#                 continue
#         else:
#             continue
#     visited[r][c] = 0