# Gravity
# 상자들이 쌓여있는 방이 있다.
# 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때,
# 낙차가 가장 큰 상자를 구하여 그 낙차를 리턴 하는 프로그램을 작성하시오.


# 중력은 회전이 완료된 후 적용된다.
# 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
# 방의 가로길이는 항상 100이며, 세로 길이도 항상 100이다.
# 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다.


# 예) 총 26개의 상자가 회전 후, 오른쪽 방 그림의 상태가 된다. A 상자의 낙차가 7로 가장 크므로 7을 리턴하면 된다.
# 회전 결과, B상자의 낙차는 6, C상자의 낙차는 1이다.


import sys

sys.stdin = open('input_gravity.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    max_fall = 0
    # 자신보다 높이가 같거나 큰 것이 오른쪽으로 몇 개 있는지 알면 된다.
    for i in range(0, len(boxes) - 1):
        bigger = 0
        for j in range(i + 1, len(boxes)):
            if boxes[j] >= boxes[i]:
                bigger += 1
        # 각 박스탑에서 낙차가 가장 큰 박스의 낙차는 다음과 같다.
        i_max_fall = len(boxes) - i - 1 - bigger
        if i_max_fall > max_fall:
            max_fall = i_max_fall

    print('#%d %d' %(t, max_fall))