# N-Queen
# 8*8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제는 잘 알려져 있는 문제이다.
# 이 문제의 조금 더 일반화된 문제는 Franz Nauck이 1850년에 제기했다.
# N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 N(1 ≤ N ≤ 10)이 주어진다.


# [출력]
# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


# 1
# 서로 대각선에 있으면 행과 열의 차이가 같음을 이용해서 구하기
# level은 체스판의 행 번호, i는 체스판의 열 번호이다.
def DFS(level):
    if level >= N:
        global cnt
        cnt += 1
        return

    for i in range(N):
        if not col[i]:
            # 기존에 있던 퀸들의 위치와 지금 놓으려는 위치의 행, 열 차이가 같으면 대각선에 있는 것
            for r, c in queen_list:
                if abs(level - r) == abs(i - c):
                    break
            else:
                col[i] = 1
                queen_list.add((level, i))
                DFS(level+1)
                col[i] = 0
                queen_list.remove((level, i))


drc = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
for t in range(1, int(input())+1):
    N = int(input())
    col = [0]*N
    queen_list = set()
    cnt = 0
    DFS(0)
    print('#%d %d' % (t, cnt))


# 2
# 대각선 자체에 잘보면 특성이 있다.
# n*n의 배열에서 대각선의 개수는 좌상, 우상 대각선 각각 2*n-1이다.
# 그리고, 행과 열의 인덱스를 이용해 각 대각선을 나타낼 수 있다.
# n이 4일 때,
# 우상 대각선(행 + 열)
# 0 1 2 3
#       4
#       5
#       6
# 좌상 대각선(행 - 열 + n - 1)
# 3 2 1 0
# 4
# 5
# 6

# level은 행 번호, i는 열 번호가 된다.
def DFS(level):
    if level >= N:
        cnt[0] += 1
        return

    for i in range(N):
        if not col[i] and not diag_r[level+i] and not diag_l[level-i+N-1]:
            col[i], diag_r[level+i], diag_l[level-i+N-1] = 1, 1, 1
            DFS(level+1)
            col[i], diag_r[level+i], diag_l[level-i+N-1] = 0, 0, 0


for t in range(1, int(input())+1):
    N = int(input())
    # 열, 우상 대각선, 좌상 대각선 방문 체크용
    col, diag_r, diag_l = [0]*N, [0]*(2*N-1), [0]*(2*N-1)
    cnt = [0]
    DFS(0)
    print('#%d %d' % (t, cnt[0]))