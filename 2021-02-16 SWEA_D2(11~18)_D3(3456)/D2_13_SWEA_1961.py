# 숫자 배열 회전
# N x N 행렬이 주어질 때,
# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


# [제약 사항]
# N은 3 이상 7 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
# 다음 N 줄에는 N x N 행렬이 주어진다.


# [출력]
# 출력의 첫 줄은 '#t'로 시작하고,
# 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


import sys


sys.stdin = open('1961_input.txt')

# 90도 회전하는 식은 다음과 같다. arr_90[j][N-1-i] = arr[i][j]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 복제가 아닌 복사를 하기 위해서
    arr_90 = [list(arr[i]) for i in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[j][N-1-i] = arr[i][j]
    # 90도 회전한 arr를 90도 회전시키면 180도가 된다.
    arr_180 = [list(arr_90[i]) for i in range(N)]
    for i in range(N):
        for j in range(N):
            arr_180[j][N-1-i] = arr_90[i][j]
    # 180도 회전한 arr를 90도 회전시키면 270도가 된다.
    arr_270 = [list(arr_180[i]) for i in range(N)]
    for i in range(N):
        for j in range(N):
            arr_270[j][N-1-i] = arr_180[i][j]

    result_list = []
    for i in range(N):
        result_list = result_list + [arr_90[i]] + [arr_180[i]] + [arr_270[i]]

    print('#%d' % t)
    # 각 90도, 180도, 270도 이차원 배열의 행을 차례로 출력해야 한다.
    for i in range(N):
        result = ''
        for j in range(3):
            for k in range(N):
                result += str(result_list[i*3+j][k])
            if j != 2:
                result += ' '
        print(result)


# 승현님 코드
# 배열을 실제로 만드는 것이 아니라 값만 가져와서 바로바로 출력한다.
# 90도: 첫 col, 마지막 row부터
# 180도: 마지막 row , 마지막 col부터
# 270도: 마지막 col , 첫번째 row부터
# rotate 에는 0, 1, 2 index에 각각 90, 180, 270도 회전한 row가 들어감
for t in range(1, int(input())+1):
    print("#%d" %t)
    size = int(input())
    square = [0]*size
    for i in range(size):
        square[i] = list(map(str, input().split()))
    for a in range(1, size+1):
        rotate = ['']*3
        for b in range(1, size+1):
            rotate[0] += str(square[size-b][a-1])
            rotate[1] += str(square[size-a][size-b])
            rotate[2] += str(square[b-1][size-a])
        print(rotate[0], rotate[1], rotate[2])