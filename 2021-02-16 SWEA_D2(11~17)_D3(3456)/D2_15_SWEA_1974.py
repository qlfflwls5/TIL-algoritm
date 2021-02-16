# 스도쿠 검증
# 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


# [제약 사항]
# 1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
# 2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


import sys


sys.stdin = open('1974_input.txt')

N = 9
T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1
    cnt_list_row = [0]*9
    cnt_list_col = [0]*9
    cnt_list_square = [0]*9
    for i in range(N):
        for j in range(N):
            cnt_list_row[arr[i][j]-1] += 1
            cnt_list_col[arr[j][i]-1] += 1
            if i % 3 == 0 and j % 3 == 0:
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        cnt_list_square[arr[k][l]-1] += 1

                for cnt in cnt_list_square:
                    if cnt > 1:
                        result = 0

                cnt_list_square = [0] * 9

        for cnt in cnt_list_row:
            if cnt > 1:
                result = 0

        for cnt in cnt_list_col:
            if cnt > 1:
                result = 0

        cnt_list_row = [0] * 9
        cnt_list_col = [0] * 9

    print('#%d %d' %(t, result))
    
    
# 채은님 코드
# set과 range의 step을 사용해서 쉽게 해결
# set은 중복 검사용
# range의 step은 3*3 사각형 찾는용
def puzzle_check(arr, N):

    # 행 검사
    for r in range(N):
        num = []
        for c in range(N):
            num.append(arr[r][c])
        if len(set(num)) != N:
            return 0

    # 열 검사
    for c in range(N):
        num = []
        for r in range(N):
            num.append(arr[r][c])
        if len(set(num)) != N:
            return 0

    # 네모 검사 [0:3][3:6][6:9] <- 이건 틀렸다.
    for i in range(0, N, 3):
        num = []
        for r in range(i, i + 3):
            for c in range(i, i + 3):
                num.append(arr[r][c])
        if len(set(num)) != N:
            return 0

    return 1

T = int(input())
N = 9
for t in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = puzzle_check(puzzle, N)
    print('#%d %d' %(t, ans))