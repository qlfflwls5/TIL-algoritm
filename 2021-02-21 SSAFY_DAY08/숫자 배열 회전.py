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


sys.stdin = open('숫자배열회전_input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    print('#%d' % t)
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 진짜로 90도, 180도, 270도 돌리지 말고 각 행에 출력되는 값을 어떻게 뽑아올 수 있는지 생각해보자
    # 각 i번째 행에 대하여 90도로 돌린 i번째 행, 180도로 돌린 i번째 행, 270도로 돌린 i번째 행을 출력하면 되는 것이다.
    # 즉, 90도 180도 270도 돌리면 각각 어느 요소가 어디로 이동하는지의 규칙을 찾으면 된다.
    for i in range(N):
        result = ''
        for j in range(N):
            result += str(arr[N-j-1][i])
        result += ' '
        for j in range(N):
            result += str(arr[N-i-1][N-j-1])
        result += ' '
        for j in range(N):
            result += str(arr[j][N-i-1])

        print(result)


# 2
# 90도 회전을 한다는 것은, 기존 arr에서 열마다 가져와 이를 거꾸로 해서 행으로 출력하는 것
# ex) 123 -> 첫 열이 147이다 이를 거꾸로하면 741이 되고 이는 90도 회전한 arr의 첫 행이 된다.
#     456
#     789
T = int(input())


def reverse_map(lst):
    return list(reversed(lst))


for t in range(1, T + 1):
    N = int(input())
    square = []

    for _ in range(N):
        square.append(list(map(str, input().split())))

    square_90 = list(map(reverse_map, list(zip(*square))))
    square_180 = list(map(reverse_map, list(zip(*square_90))))
    square_270 = list(map(reverse_map, list(zip(*square_180))))

    print('#%d' % t)
    for i in range(N):
        print("".join(square_90[i]), end=" ")
        print("".join(square_180[i]), end=" ")
        print("".join(square_270[i]))


# 2
# 훈규님 코드
# 내 셀프스터디 풀이와 같은 방식이지만 훨씬 깔끔하고 좋다. print문 잘보자.
def shift90(arr):
    new_arr = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_arr[c][N - r - 1] = arr[r][c]
    return new_arr


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    nums = [list(map(int, input().split())) for _ in range(N)]

    num_90 = shift90(nums)
    num_180 = shift90(num_90)
    num_270 = shift90(num_180)

    print('#%d' % tc)
    for i in range(N):
        print(''.join(map(str, num_90[i])), ''.join(map(str, num_180[i])), ''.join(map(str, num_270[i])))
