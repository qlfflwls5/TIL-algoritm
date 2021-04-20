# 오목판정
# N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다.
# 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.
# 다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다. 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.


# [출력]
# 각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다.


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    flag = 0
    for i in range(N):
        # 검사용 변수들
        diag_1, diag_2, diag_3, diag_4, r_cnt, c_cnt = 0, 0, 0, 0, 0, 0
        # 가로, 세로 한 줄 검사
        for j in range(N):
            # 가로 검사
            if arr[i][j] == 'o':
                r_cnt += 1
            else:
                r_cnt = 0
            # 세로 검사
            if arr[j][i] == 'o':
                c_cnt += 1
            else:
                c_cnt = 0
            # 대각선의 경우 적용할 범위 -> 이게 가장 중요하다. i + j가 N 이상이면 index error가 발생한다.
            if i < N - 5 + 1 and i + j < N:
                # 좌상 대각선에서 아래로 나아가는 대각선 검사 (\모양으로 절반 기준 하향하는 대각선)
                if arr[i + j][j] == 'o':
                    diag_1 += 1
                else:
                    diag_1 = 0
                # 좌상 대각선에서 위로 나아가는 대각선 검사 (\모양으로 절반 기준 상향하는 대각선)
                if arr[j][i + j] == 'o':
                    diag_2 += 1
                else:
                    diag_2 = 0
                # 우상 대각선에서 위로 나아가는 대각선 검사 (/모양으로 절반 기준 하향하는 대각선)
                if arr[i + j][N - 1 - j] == 'o':
                    diag_3 += 1
                else:
                    diag_3 = 0
                # 우상 대각선에서 위로 나아가는 대각선 검사 (/모양으로 절반 기준 상향하는 대각선)
                if arr[j][N - 1 - i - j] == 'o':
                    diag_4 += 1
                else:
                    diag_4 = 0

            if r_cnt == 5 or c_cnt == 5 or diag_1 == 5 or diag_2 == 5 or diag_3 == 5 or diag_4 == 5:
                flag = 1
                break

        if flag == 1:
            break

    result = 'YES' if flag else 'NO'
    print('#%d %s' % (t, result))


# 2
# 이거 델타로 풀어보자! DFS도 활용을 하였다!
# 5*5의 판에서 오목을 진행하면 인접 리스트를 만들기 위해서 이를
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# 로 보겠다는 것이다! 'o'인 각 칸이 정점이 되고, 'o'인 정점이 인접해 있으면 이를 경로로 보아 이 경로가 오목이 완성되는지 확인한다.
# ex) . . . . o
#     . . . o .
#     . . o . .
#     . o . . .
#     o . . . .
# 일때, 5 - 9 - 13 - 17 - 21 경로가 오목이다.
def DFS(AL, v):
    # 이미 오목을 찾았다면 아무것도 하지 않고 리턴
    global result
    if result == 'YES':
        return

    # 경로에 정점을 추가
    way.append(v)
    # 경로의 길이가 5가 되었을 때 각 경로의 정점들의 차가 같으면 일정 방향으로 쭉 뻗은 오목인 것이다.
    if len(way) == 5:
        if way[0] - way[1] == way[1] - way[2] == way[2] - way[3] == way[3] - way[4]:
            result = 'YES'
            return

    # 정점의 인접한 정점들 중
    for w in AL[v]:
        # 같은 방향에 있는 정점으로만 경로가 뻗어져나간다. ex) 아래로 나가던 중이면 아래로만 뻗어져 나간다. 다른 것은 가지치기
        if len(way) > 1:
            if w - way[-1] == way[1] - way[0]:
                DFS(AL, w)
                # result = 'YES'일 때도 pop을 하면 인덱스 에러가 난다.
                if result == 'NO':
                    way.pop()
        # 처음 인접한 정점이 방향을 결정할 것이므로 바로 재귀를 실행한다.
        else:
            DFS(AL, w)
            # 가장 중요. 내가 갔던 길이 오목이 아니라면 다시 갈림길로 되돌아와 다른 길로 나아가며 way를 새로 써야한다.
            # 따라서 되돌아 나올 때마다 나온만큼 way를 pop하여 경로를 복구한다.
            way.pop()


# 현재를 기준으로 뻗어져나가는 오목을 검색할 것이므로 오른쪽, 오른쪽 아래, 아래, 왼쪽 아래를 검사하면 된다.
drc = [[0, 1], [1, 1], [1, 0], [1, -1]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # arr의 첫 칸부터 마지막 칸까지 1~N**2를 써넣었을 때 이를 각각 정점으로 보고 연결된 것을 찾을 것이다.
    AL = [[] for _ in range(N**2+1)]

    # 델타 검색이 가능한 범위 내에서만 실행하도록 조건을 주었는데 비효율적으로 짰다.
    for dr, dc in drc:
        if dc < 0:
            s, e = 1, N
        else:
            s, e = 0, N-dc
        for i in range(N-dr):
            for j in range(s, e):
                if arr[i][j] == 'o':
                    if arr[i + dr][j + dc] == 'o':
                        # arr[i][j]의 인접리스트에 추가
                        # AL[i*N+j+1]이 arr[i][j]의 위치, 델타 검색을 기준으로 인접한 정점의 AL 값은 i*N+j+1 + dr*N+dc
                        AL[i * N + j + 1].append(i * N + j + 1 + dr * N + dc)

    result = 'NO'
    for i in range(N):
        for j in range(N):
            # 현재 위치가 정점에 해당하는 경우에만 DFS실행
            if arr[i][j] == 'o':
                way = []
                DFS(AL, i*N+j+1)

    print('#%d %s' % (t, result))


# 3
# 은교님 코드 -> 대각선 한 번에 구함!
# 대각선 체크하는게 대박 힘들었다... 다섯개 셀 수 있는 출발 인덱스 구하기가 핵심
def check_omok(arr):
    # 행 검사
    N = len(arr)
    for r in range(N):
        for c in range(N-4): # 비교 시작점
            for i in range(5):
                if arr[r][c+i] != 'o':
                    break
            else:
                return 'YES'
    # 열 검사
    for c in range(N): # N = 6 일 때를 상상
        for r in range(N-4):
            for i in range(5):
                if arr[r+i][c] != 'o':
                    break
            else:
                return 'YES'

    # 좌상향 대각선
    drc = [[1, 1], [1, -1]]
    for c in range(N-4): # 0, 1
        for r in range(N-4): # 0, 1
            for i in range(5):
                if arr[r+(drc[0][0]*i)][c+(drc[0][1]*i)] != 'o':
                    break
            else:
                return 'YES'

    # 우상향 대각선
    for c in range(N-1, 3, -1): # 5, 4
        for r in range(N-4): # 0, 1
            for i in range(5):
                if arr[r+(drc[1][0]*i)][c+(drc[1][1]*i)] != 'o':
                    break
            else:
                return 'YES'
    return 'NO'

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []
    for n in range(N):
        tmp = []
        tmp.extend(input())
        board += [tmp]
    result = check_omok(board)
    print("#%d %s" % (t, result))
