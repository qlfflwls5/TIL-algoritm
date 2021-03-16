# 무선 충전
# 스마트폰을 무선 충전 할 때 최적의 BC (Battery Charger)를 선택하는 알고리즘을 개발하고자 한다.
# [그림 1]과 같이 가로 세로 10*10 영역의 지도가 주어졌을 때, 설치된 BC 정보는 다음과 같다.
#                          BC 1     BC 2    BC 3
# 위치 Location (X, Y)    (4, 4)  (7, 10)  (6, 3)
# 충전 범위 Coverage (C)     1       3        2
# 성능 Performance (P)      100      40       70

# BC의 충전 범위가 C일 때, BC와 거리가 C 이하이면 BC에 접속할 수 있다.
# 이때, 두 지점 A(XA, YA), B(XB, YB) 사이의 거리는 다음과 같이 구할 수 있다.
#     D = |XA – XB| + |YA – YB|
# 위의 [그림 1]에서 (4,3)과 (5,4) 지점은 BC 1과 BC 3의 충전 범위에 모두 속하기 때문에, 이 위치에서는 두 BC 중 하나를 선택하여 접속할 수 있다.

# [그림 2]와 같이 사용자 A와 B의 이동 궤적이 주어졌다고 가정하자. T는 초(Second)를 의미한다. 예를 들어 5초에 사용자 A는 (5, 2) 지점에, 사용자 B는 (6, 9) 지점에 위치한다.
# 매초마다 특정 BC의 충전 범위에 안에 들어오면 해당 BC에 접속이 가능하다. 따라서 T=5에 사용자 A는 BC 3에, 사용자 B는 BC 2에 접속할 수 있다.
# 이때, 접속한 BC의 성능(P)만큼 배터리를 충전 할 수 있다. 만약 한 BC에 두 명의 사용자가 접속한 경우, 접속한 사용자의 수만큼 충전 양을 균등하게 분배한다.
# BC의 정보와 사용자의 이동 궤적이 주어졌을 때, 모든 사용자가 충전한 양의 합의 최댓값을 구하는 프로그램을 작성하라.

# [그림 2]에서 T=11일 때, 사용자 A는 BC 1과 3 둘 중 하나에 접속이 가능하다.
# 같은 시간에 사용자 B는 BC 1에 접속할 수 밖에 없다.
# 따라서 사용자 A가 같은 BC 1에 접속한다면 충전되는 양를 반씩 나눠 갖게 되어 비효율적이다.
# 따라서 사용자 A가 BC 3에 접속하는 것이 더 이득이다.


# [제약사항]
# 1. 지도의 가로, 세로 크기는 10이다.
# 2. 사용자는 총 2명이며, 사용자A는 지도의 (1, 1) 지점에서, 사용자B는 지도의 (10, 10) 지점에서 출발한다.
# 3. 총 이동 시간 M은 20이상 100이하의 정수이다. (20 ≤ M ≤ 100)
# 4. BC의 개수 A는 1이상 8이하의 정수이다. (1 ≤ A ≤ 8)
# 5. BC의 충전 범위 C는 1이상 4이하의 정수이다. (1 ≤ C ≤ 4)
# 6. BC의 성능 P는 10이상 500이하의 짝수이다. (10 ≤ P ≤ 500)
# 7. 사용자의 초기 위치(0초)부터 충전을 할 수 있다.
# 8. 같은 위치에 2개 이상의 BC가 설치된 경우는 없다. 그러나 사용자A, B가 동시에 같은 위치로 이동할 수는 있다. 사용자가 지도 밖으로 이동하는 경우는 없다.


# [입력]
# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄에는 총 이동 시간(M), BC의 개수(A)가 주어진다.
# 그 다음 2개의 줄에는 각각 사용자 A와 B의 이동 정보가 주어진다.
# 한 사용자의 이동 정보는 M개의 숫자로 구성되며, 각각의 숫자는 다음과 같이 매초마다 이동 방향을 의미한다.
#     0       1       2       3       4
#    이동x    상      우      하      좌
# 그 다음 줄에는 A개의 줄에 걸쳐 BC의 정보가 주어진다.
# 하나의 BC 정보는 좌표(X, Y), 충전 범위(C), 처리량(P)로 구성된다.


# [출력]
# 출력은 "#t"를 찍고 한 칸 띄운 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
# 정답은 모든 사용자의 충전량 합의 최대값을 출력한다.


# 한 칸 이동할 때 마다 각 BC와의 거리를 모두 재서 해당 BC의 충전 범위 내에 들어가면 temp 리스트 안에 [p, BC번호]를 담는다.
# p를 기준으로 정렬하고서 temp[0][0]이 충전할 양이다.
# A와 B가 같은 BC에 접속을 하였다면, temp[0]이 서로 같을 것이다.
# 이때, 둘 다 temp의 길이가 1이라면 둘 다 teamp[0][0] // 2만큼을 충전한다. (둘 다 하나의 BC 영역내에 있는 경우)
# 만약 한 쪽의 temp 길이가 1이고 다른 쪽은 2이상이라면 길이가 1인쪽은 temp[0][0], 2이상인쪽은 temp[1][0]을 충전한다.
# 만약 둘 다 길이가 2이상이라면 A의 temp[0][0] + B의 temp[1][0]과 A의 temp [1][0] + B의 temp[0][0] 중에 큰 쪽 만큼 충전한다.
drc = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
for t in range(1, int(input())+1):
    M, A = map(int, input().split())
    arr = [[0]*10 for _ in range(10)]
    a, b = [0, 0], [9, 9]
    a_move = list(map(int, input().split()))
    b_move = list(map(int, input().split()))
    BC_list = []
    for _ in range(A):
        BC = list(map(int, input().split()))
        # x, y좌표 프로그래밍에 맞게 보정
        BC[0], BC[1] = BC[1] - 1, BC[0] - 1
        BC_list.append(BC)
    charge = 0
    # 첫 시작도 포함하므로 M+1초라고 생각한다. 한 칸 이동을 가장 마지막에 한다.
    for time in range(M+1):
        temp_a, temp_b = [], []
        for i in range(A):
            BC = BC_list[i]
            # temp_a와 temp_b에 각각 a와 b가 속한 BC의 [성능, BC번호]를 담는다.
            if abs(a[0] - BC[0]) + abs(a[1] - BC[1]) <= BC[2]:
                temp_a.append([BC[3], i])
            if abs(b[0] - BC[0]) + abs(b[1] - BC[1]) <= BC[2]:
                temp_b.append([BC[3], i])
        # 성능 순으로 내림차순
        temp_a.sort(key=lambda x: x[0], reverse=True)
        temp_b.sort(key=lambda x: x[0], reverse=True)
        # 둘 중 하나 이상이 길이가 0이라면 간단하게 처리
        if not temp_a and not temp_b:
            if time < M:
                a[0], a[1] = a[0] + drc[a_move[time]][0], a[1] + drc[a_move[time]][1]
                b[0], b[1] = b[0] + drc[b_move[time]][0], b[1] + drc[b_move[time]][1]
            continue
        elif not temp_a and temp_b:
            charge += temp_b[0][0]
        elif temp_a and not temp_b:
            charge += temp_a[0][0]
        # 둘 다 하나 이상의 BC에 속한다면
        else:
            # temp_a와 temp_b의 첫 요소([성능, BC번호])가 같다면 갈라서거나 충전량을 나눠야하는 상황이고, 그게 아니라면 각자의 최대 획득 성능인 temp[0][0]을 충전한다.
            if temp_a[0] == temp_b[0]:
                # 둘 다 지금 BC 하나 밖에 안속한다면 나눠야 한다. 즉, 둘의 충전량 합이 해당 BC의 성능이다.
                if len(temp_a) == len(temp_b) == 1:
                    charge += temp_a[0][0]
                # 둘 중 한 명만 해당 BC밖에 안속하고 다른 한 명이 여러 BC에 속한다면 여러 BC에 속한 쪽이 다음 충전량 큰 쪽으로 양보한다.
                elif len(temp_a) == 1 and len(temp_b) > 1:
                    charge += temp_a[0][0] + temp_b[1][0]
                elif len(temp_a) > 1 and len(temp_b) == 1:
                    charge += temp_a[1][0] + temp_b[0][0]
                # 둘 다 여러 BC에 속한다면 temp_a[0][0] + temp_b[1][0]와 temp_a[1][0] + temp_b[0][0] 중에 큰 쪽 만큼 충전한다.
                else:
                    charge += max(temp_a[0][0] + temp_b[1][0], temp_a[1][0] + temp_b[0][0])
            else:
                charge += temp_a[0][0] + temp_b[0][0]

        if time < M:
            a[0], a[1] = a[0] + drc[a_move[time]][0], a[1] + drc[a_move[time]][1]
            b[0], b[1] = b[0] + drc[b_move[time]][0], b[1] + drc[b_move[time]][1]
    
    print('#%d %d' % (t, charge))