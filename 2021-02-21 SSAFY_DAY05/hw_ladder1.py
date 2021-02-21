# Ladder1
# 점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.
# 김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.
# 사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

# 아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨)
# 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.
# X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.
# 방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.
# 문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.

# 아래 <그림 2>와 같은 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서,
# 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라 (‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).


# 어느 곳으로 출발해야 도착지점 '2'에 도달하는지를 찾는 문제다.
# 거꾸로 생각하자. '2'부터 출발하면 어느 출발지점에 도착하는지를 찾으면 된다.
import sys

sys.stdin = open('ladder1_input.txt')

# 1
# 각 행의 양 끝에 0을 더해서 예외를 없애주는 덧대기식 풀이
for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(len(arr)):
        arr[i] = [0] + arr[i] + [0]
    r, c = 99, [c for c in range(len(arr[99])) if arr[99][c] == 2][0]
    len(arr[99])
    while r > 0:
            while arr[r][c-1] + arr[r][c+1] == 0 and r > 0:
                r -= 1
            if arr[r][c-1]:
                while arr[r][c-1]:
                    c -= 1
                else:
                    r -= 1
            else:
                while arr[r][c+1]:
                    c += 1
                else:
                    r -= 1

    print('#%d %d' %(N, c-1))


# 2
# 처음 풀이였다. 각 칸에서 계산하기
for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    r, c = 99, [c for c in range(len(arr[99])) if arr[99][c] == 2][0]
    direction = 'up'
    while r > 0:
        if c == 0:
            if arr[r][c+1] == 1 and direction != 'left':
                c += 1
                direction = 'right'
            else:
                r -= 1
                direction = 'up'
        elif c == 99:
            if arr[r][c-1] == 1 and direction != 'right':
                c -= 1
                direction = 'left'
            else:
                r -= 1
                direction = 'up'
        elif arr[r][c-1] == 1 and direction != 'right':
            c -= 1
            direction = 'left'
        elif arr[r][c+1] == 1 and direction != 'left':
            c += 1
            direction = 'right'
        else:
            r -= 1
            direction = 'up'
    print('#%d %d' %(N, c))


    # 3
    # 최재연님 풀이 중 규칙 부분
    # while nr > 0:
    #     if nc > 0 and arr[nr][nc - 1] == 1:
    #         while nc > 0 and arr[nr][nc - 1] != 0:
    #             nc -= 1
    #         nr -= 1
    #
    #     elif nc < 99 and arr[nr][nc + 1] == 1:
    #         while nc < 99 and arr[nr][nc + 1] != 0:
    #             nc += 1
    #         nr -= 1
    #
    #     else:
    #         nr -= 1