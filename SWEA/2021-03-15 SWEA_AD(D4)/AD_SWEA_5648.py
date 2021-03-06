# 원자 소멸 시뮬레이션
# 원자력 발전소에서 근무하는 상원이는, 발전소에서 발생하는 에너지를 미리 계산하기 위해 원자들의 움직임을 시뮬레이션 하는 프로그램을 만들려고 한다.
# 원자들은 2차원 평면에서 이동하며 두 개 이상의 원자가 충돌 할 경우 충돌한 원자들은 각자 보유한 에너지를 모두 방출하고 소멸된다.
# 원자의 움직임은 다음과 같다.

# 1. 원자의 최초 위치는 2차원 평면상의 [x, y] 이다.
# 2. 원자는 각자 고유의 움직이는 방향을 가지고 있다. (상하좌우 4방향)
#  - 상: y 가 증가하는 방향
#  - 하: y 가 감소하는 방향
#  - 좌: x 가 감소하는 방향
#  - 우: x 가 증가하는 방향
# 3. 모든 원자들의 이동속도는 동일하다. 즉, 1초에 1만큼의 거리를 이동한다.
# 4. 모든 원자들은 최초 위치에서 동시에 이동을 시작한다.
# 5. 두 개 이상의 원자가 동시에 충돌 할 경우 충돌한 원자들은 모두 보유한 에너지를 방출하고 소멸된다.

# [그림-1] 과 같이 원자들의 [x, y] 위치와 이동방향이 주어지고 각 원자들의 보유 에너지가 1 이라고 가정해보자. (실제 입력에서 원자들의 보유 에너지는 각각 다를 수 있다.)
# 충돌된 원자들이 소멸하면서 방출하는 에너지는 다음과 같다.

# 1초 후에 I, J 원자가 충돌 후 소멸하면서 2 에너지 방출
# 1.5초 후에 A, B 원자가 충돌 후 소멸하면서 2 에너지 방출
# 2초 후에 D, E, G, H 원자가 충돌 후 소멸하면서 4 에너지 방출
# 3초 후에 M, N 원자가 충돌 후 소멸하면서 2 에너지 방출

# [그림-1]의 경우 시간이 흘러도 원자 C, F, K, L 은 영원히 충돌하지 않아 소멸되지 않는다.
# 따라서 원자들이 소멸되면서 방출하는 에너지의 총합은 10 이다.
# N 개의 원자들의 [x, y] 위치, 이동 방향, 보유 에너지가 주어질 때 원자들이 소멸되면서 방출하는 에너지의 총합을 구하는 프로그램을 작성하라.


# [제약 사항]
# 1. 원자들의 수 N 은 1,000개 이하이다. (1≤N≤1,000)
# 2. 각 원자들의 보유 에너지 K 는 1 이상 100 이하이다. (1≤K≤100)
# 3. 원자들의 처음 위치 [x, y] 는 -1,000 이상 1,000 이하의 정수로 주어진다. (-1,000≤x,y≤1,000)
# 4. 원자들은 2차원 평면 위에서 움직이며 원자들이 움직일 수 있는 좌표의 범위에 제한은 없다.
# 5. 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)로 주어진다.
# 6. 원자들은 동시에 1초에 이동 방향으로 1만큼 이동한다.
# 7. 원자들의 최초 위치는 서로 중복되지 않는다.
# 8. 원자들은 2개 이상의 원자들이 서로 충돌할 경우 보유한 에너지를 방출하면서 바로 소멸된다.
# 9. 원자들은 이동 방향은 처음에 주어진 방향에서 바뀌지 않는다.
# 10. 원자들이 충돌하여 소멸되며 방출되는 에너지는 다른 원자의 위치나 이동 방향에 영향을 주지 않는다.


# [입력]
# 입력의 가장 첫 줄에는 총 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터는 각 테스트 케이스가 주어진다. 각 테스트 케이스의 첫째 줄에는 원자들의 수 N이 주어진다.
# 다음 N개의 줄에는 원자들의 x 위치, y 위치, 이동 방향, 보유 에너지 K가 주어진다.
# 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)로 주어진다.


# [출력]
# 테스트 케이스 T에 대한 결과는 “#T”을 찍고, 방출되는 에너지의 총합을 출력한다. (T는 테스트케이스의 번호를 의미하며 1부터 시작한다. )


# BFS를 통해 특정 점에서 퍼져나갈 때 같은 위치에 있으며 점을 향해 오는 원자를 소멸시키는 식으로 진행할 것이다.
# 이를 위해서는 원자가 만나는 공간이 0.5의 공간이면 안된다. 그래서 모든 원자의 좌표를 x2하여 무조건 사이의 거리가 짝수가 되게 한다. 전체 격자도 x2를 할 것이다.
# 원자의 진로 방향에 있는 모든 점에 대해서만 수행할 것이다.
# 0으로 된 격자에 원자가 갈 수 있는 길을 -1로 표시하고 원자의 위치에는 원자의 에너지를 표시한다.
# 0이 아닌 지점에서 BFS를 진행하고, 같은 거리에 있는 4개의 상하좌우 위치에서 1이상인 지점이 2개 이상이면 그 값들을 전부 누적 에너지에 더하고 -1로 바꾼다.
# 가지치기는 할 수 있으면 한다.
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우
for t in range(1, int(input())+1):
    N = int(input())
    arr = [[0]*4001 for _ in range(4001)]
    queue = []
    # 격자 세팅
    for _ in range(N):
        atom = list(map(int, input().split()))
        atom[0], atom[1] = (-atom[1] + 1000) * 2, (atom[0] + 1000) * 2
        queue.append((atom[0], atom[1], 0))
        if atom[2] == 0:
            for r in range(0, atom[0]+1):
                if arr[r][atom[1]] == 0:
                    arr[r][atom[1]] = -1
                    queue.append((r, atom[1], 0))
        elif atom[2] == 1:
            for r in range(atom[0], 4001):
                if arr[r][atom[1]] == 0:
                    arr[r][atom[1]] = -1
                    queue.append((r, atom[1], 0))
        elif atom[2] == 2:
            for c in range(0, atom[1]+1):
                if arr[atom[0]][c] == 0:
                    arr[atom[0]][c] = -1
                    queue.append((atom[0], c, 0))
        else:
            for c in range(atom[1], 4001):
                if arr[atom[0]][c] == 0:
                    arr[atom[0]][c] = -1
                    queue.append((atom[0], c, 0))

        arr[atom[0]][atom[1]] = atom[3]

    for i in range(4001):
        for j in range(4001):
            if arr[i][j]:
                pass



