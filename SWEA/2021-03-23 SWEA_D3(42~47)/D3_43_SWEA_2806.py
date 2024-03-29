# N-Queen
# 8*8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제는 잘 알려져 있는 문제이다.
# 퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있다. 이 문제의 한가지 정답은 아래 그림과 같다.
# 이 문제의 조금 더 일반화된 문제는 Franz Nauck이 1850년에 제기했다.
# N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 N(1 ≤ N ≤ 10)이 주어진다.


# [출력]
# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


# level은 말의 개수이자 각 행
def DFS(level):
    # 모든 말을 다 채우면 cnt += 1
    if level >= N:
        global cnt
        cnt += 1
        return
    # 각 행에서 0~N-1번째 열 중에 선택
    for i in range(N):
        # 만약 i번째 열이 아직 선택되지 않았다면 놓을 수 있는지 체크(대각선 공격 영역에 들어가는지 확인하는 것이다.)
        if not col[i]:
            # 퀸이 놓여져 있는 좌표를 하나씩 가져와서
            for r, c in queen_list:
                # 현재의 행과 기존에 퀸이 놓여진 행의 거리와, 현재의 행이 선택한 열과 기존에 퀸이 놓여진 열의 거리가 같다면 대각선에 있는 것이다.
                # ex) 현재의 행과 열이 (2, 2)고, 기존의 퀸이 놓여진 행과 열이 (1, 1)이라면 행 간의 거리와 열 간의 거리가 같고, 대각선에 있는 것이다.
                if abs(level - r) == abs(i - c):
                    break
            else:
                # 공격 영역에 없다면 열을 차지하고, 퀸 리스트에 추가하고, 다음 레벨 실행
                col[i] = 1
                queen_list.append((level, i))
                DFS(level+1)
                # 탐색이 끝나면 열을 되돌려주고, 퀸 리스트에서도 제거
                col[i] = 0
                queen_list.pop()


drc = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
for t in range(1, int(input())+1):
    N = int(input())
    # N줄의 열, 각 행에서 열을 선택하는 식으로 할 것이다. (이러면 퀸의 가로 세로 공격 영역에 대한 탐색은 알아서 이루어진다.)
    col = [0]*N
    # 행이 열을 선택하면, 그 위치가 퀸의 위치이고 이를 저장할 것이다.
    queen_list = []
    cnt = 0
    DFS(0)
    print('#%d %d' % (t, cnt))
