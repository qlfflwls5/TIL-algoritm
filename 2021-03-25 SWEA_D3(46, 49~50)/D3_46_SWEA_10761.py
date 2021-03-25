# 신뢰
# 오렌지와 블루는 순진하고 귀여운 로봇 친구들이다.
# 하지만 정체불명의 인공지능 악마가 두 로봇을 서로 다른 복도에 가둬놓고, 실험을 진행하고 있다.
# 한 복도에는 1 이상 100 이하의 정수로 구분되는 100개의 버튼이 존재한다.
# 버튼 K는 복도의 시작점에서 K미터 떨어져 있다. 두 로봇은 버튼 1에서 시작한다.
# 매 1초마다, 로봇은 복도의 양 방향 중 하나로 1미터 걷거나, 자기 위치에 있는 버튼을 누르거나, 아무 것도 하지 않는다.

# 오렌지와 블루는 서로 다른 복도에 있음에 유의하라.

# 하나의 테스트는 여러 개의 버튼 수열로 표시되는데, 이는 로봇들이 수열에 표시된 순서대로 버튼을 눌러야 함을 뜻한다.
# 버튼은 O x, B x와 같은 형태로 주어지는데, O x는 오렌지가 해당 버튼을 눌러야 함을 뜻하고, B x는 블루가 해당 버튼을 눌러야 함을 뜻한다.
# 순서대로 버튼을 눌러야 하기 때문에, 두 로봇이 동시에 버튼을 누를 수는 없다. 두 로봇 모두 수열을 정확히 알고 있다.
# 악마는 테스트가 끝나면 두 로봇에게 케이크를 주기로 약속했다.
# 테스트를 끝낼 수 있는 가장 빠른 시간은 언제인가?


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 각 테스트 케이스는 다음과 같이 구성되었다.
# 1. 첫 번째 정수는 테스트에서 눌러야 하는 버튼의 개수 N 이다. (1 <= N <= 100)
# 2. 이후 버튼 N개가 공백으로 구분되어 한 줄에 주어진다. 버튼이 “O x” 의 형태이면 오렌지가 버튼 x를 눌러야 하며, “B x”의 형태이면 블루가 버튼 x를 눌러야 한다. (1 <= x <= 100)


# [출력]
# 각 테스트 케이스마다 최소 시간을 출력하라.


for t in range(1, int(input())+1):
    data = list(input().split())
    pos_B, pos_O = 1, 1
    # 이번 시행에서 각 로봇이 사용한 시간
    time_B, time_O = 0, 0
    # 각 로봇이 상대 로봇이 움직이는 동안 같이 움직이며 세이브 한 시간
    save_B, save_O = 0, 0
    result = 0
    for i in range(1, len(data), 2):
        robot = data[i]
        button = int(data[i+1])
        # 완전 중복인데 함수화하면 짧아질 듯?
        if robot == 'B':
            # 버튼에 도달하기까지 필요한 시간 = 버튼까지의 거리 - 반대쪽 로봇이 움직인 동안 같이 움직여 세이브한 시간
            need_time = abs(button - pos_B) - save_B
            # 버튼을 도달하기까지 필요한 시간보다 세이브한 시간이 많으면 누르는 시간 1초만 계산
            time_B = need_time + 1 if need_time > 0 else 1
            result += time_B
            # 사용한 시간만큼 반대쪽 로봇의 시간이 세이브된다.
            save_O += time_B
            # 시행이 끝났으므로 '사용한 시간'은 0으로 초기화, 위치는 버튼으로
            time_O, pos_B = 0, button
            # 반대쪽 로봇이 쌓아준 세이브 타임을 썼으므로 0으로 초기화
            save_B = 0
        else:
            need_time = abs(button - pos_O) - save_O
            time_O = need_time + 1 if need_time > 0 else 1
            result += time_O
            save_B += time_O
            time_B, pos_O = 0, button
            save_O = 0

    print('#%d %d' % (t, result))


# 2
# 좀 짧게 정리
for t in range(1, int(input())+1):
    data, B, O, result = list(input().split()), [1, 0, 0], [1, 0, 0], 0
    for i in range(1, len(data), 2):
        robot, oppose = (B, O) if data[i] == 'B' else (O, B)
        button = int(data[i+1])
        need_time = abs(button - robot[0]) - robot[2]
        robot[1] = need_time + 1 if need_time > 0 else 1
        result, oppose[2], robot[0], robot[2] = result + robot[1], oppose[2] + robot[1], button, 0

    print('#%d %d' % (t, result))