# 삼국지
# 삼국지는 3 개의 나라가 자신의 병력으로 전체 지역을 통일하는 것을 목표로 하는 게임이다.
# 입력으로 N × N 크기의 지도에 3 가지 정보가 주어진다.
# [Fig. 1-1] 은 각 지역의 소유 정보를 나타낸다. 1 ~ 3 까지의 숫자로 지역의 소유 나라를 나타내며, 0 은 산악지역으로 아무도 소유할 수 없는 지역이다.
# [Fig. 1-2] 는 각 지역의 병력 정보를 나타낸다. 산악 지역은 0 임이 보장된다.
# [Fig. 1-3] 은 각 지역의 병력 보충 정보를 나타낸다. 산악 지역은 0 임이 보장된다.
# 이 게임에서 병력의 충돌 외에 다른 전략은 없으며, 아래 규칙에 따라 게임이 진행된다.

# 1.     게임은 매 턴마다 병력의 공격, 지원, 보충 순서로 진행된다.
#   공격과 지원은 한 나라씩 진행하고, 보충은 나라와 상관없이 전 지역에서 발생한다.
#   즉, 1 번 나라(공격, 지원), 전체 보충, 2 번 나라(공격, 지원), 전체 보충, 3 번 나라(공격, 지원), 전체 보충, 다시 1 번 나라 순으로 진행된다.
#   병력이 없는 나라가 있다면 그 턴은 진행하지 않는다.

# 2.     상대방 지역의 병력보다 상하좌우로 인접한 자신의 나라의 병력의 합이 5 배를 초과할 경우, 각 지역에서 1/4 의 병력을 보내 공격한다.
#   공격으로 인해 병력이 충돌하면, 두 나라의 병력의 차이만큼의 병력이 남게 된다.

# 예를 들어, 녹색으로 표시된 2 번 나라의 턴에 [Fig. 2-1] 과 같은 병력 정보가 주어진다면, [Fig. 2-2] 와 같이 공격이 이루어진다.
# 정 중앙의 370 병력을 가진 지역과 인접한 2 번 나라 병력의 합이 3100 (400+2000+700) 으로 5 배를 초과하므로, 각 지역에서 1/4 씩 병력을 보내어 공격한다.
# 오른쪽 하단 250 병력을 가진 지역과 인접한 2 번 나라 병력의 합이 2700 (2000+700) 으로 5 배를 초과하므로, 각 지역에서 1/4 씩 병력을 보내어 공격한다.
# 공격이 종료된 후의 병력 정보는 [Fig. 2-3] 과 같다.

# 3.     각 지역은 같은 나라의 상하좌우 인접한 지역으로 병력을 지원한다. 병력을 지원하는 조건은 2 가지가 있다.
#   a.     인접한 지역 중 다른 나라의 지역이 없는 경우, 모든 인접한 지역으로 그 지역의 병력의 1/5을 각각 지원한다.
#   b.     인접한 지역 중 다른 나라의 지역이 있을 경우, 그 지역의 병력이 인접한 아군 나라의 병력의 5 배를 초과할 경우에만, 그 지역의 병력의 1/5을 인접한 지역으로 지원한다.

# 4.     병력의 보충 정도는 지역마다 다르며, 매 턴마다 모든 팀, 모든 지역의 병력이 보충된다.

# 5.     턴이 종료되는 시점에 지도에서 한 개의 나라만 남게 되면 게임이 종료된다.

# 입력으로 N × N 크기의 정보가 주어졌을 때, 삼국을 통일하는 나라의 전체 병력의 수를 출력하는 프로그램을 작성하라.


# 공격과 지원에서 가장 문제가 되는 것은, 공격과 지원 가능여부를 판단하고 값을 구해놓은 뒤 모든 계산은 마지막에 몰아서 한다는 것이다.
# 즉, 매 공격 가능 지역, 지원 가능 지역 발견마다 실제 공격과 지원을 할 수 있는 것이 아니다. 전부 정보를 저장해뒀다가 마지막에 실행한다.
def attack(x):
    # 적 영역의 좌표를 담는다. 적 영역에서 사방탐색을 해서 내가 공격이 가능한지를 알아야 하기 때문이다.
    enemy_area = []
    for i in range(N):
        for j in range(N):
            if area[i][j] != x and area[i][j] != 0:
                enemy_area.append((i, j))
    
    # 적 영역의 개수와 산의 개수가 N**2와 같다면 내 영역이 없는 것이다. 패배 처리 후 리턴
    if len(enemy_area) + mountain == N**2:
        defeat.add(x)
        return

    # 공격의 정보를 담을 리스트
    attack_list = []
    # 각 적의 영역에 대해서
    for r, c in enemy_area:
        # 사방에 있는 나의 영역과 그 영역들의 병력 합을 구해놓는다. 중요한 것은 공격에 보낼 병력을 여기서 정하는 것이다.
        my_area = []
        my_power = 0
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and area[nr][nc] == x:
                my_area.append((nr, nc, mp[nr][nc]//4))
                my_power += mp[nr][nc]

        # 만약 병력 합이 적 영역의 병력의 5배를 초과하면 공격이 가능하다. 공격 리스트에 내 영역에 대한 정보와 적 영역의 좌표를 묶어 담는다.
        # 이 묶은 한 세트가 공격 커맨드같이 될 것이다.
        if my_power > mp[r][c]*5:
            attack_list.append((my_area, r, c))

    # 공격 정보 리스트에서 커맨드를 하나씩 가져와 모든 계산만 처리한다. 공격에 보낼 병력의 값을 여기서 구하면 계산의 영향을 받아 틀린 답이 된다.
    for my_area, r, c in attack_list:
        for mr, mc, attack_power in my_area:
            mp[mr][mc] -= attack_power
            mp[r][c] -= attack_power

        # 공격을 했다는 것은 내 영역이 된다는 것이고, 적 병력과 내 병력의 차만큼이 내 병력이 된다. 절대값을 씌우면 된다.
        area[r][c] = x
        mp[r][c] = abs(mp[r][c])

    # 만약 적의 영역 개수와 내 공격의 개수가 같다면 모든 적의 영역을 내 영역으로 만든 것이므로 victory가 된다.
    if len(enemy_area) == len(attack_list):
        global victory
        victory = 1


def support(x):
    # 지원은 내 영역에서 사방탐색을 하므로 내 영역의 좌표들을 담는다.
    my_area = []
    for i in range(N):
        for j in range(N):
            if area[i][j] == x:
                my_area.append((i, j))

    # 공격과 마찬가지로 값을 구해 정보만 담을 지원 리스트이다. 계산은 나중에 한다.
    support_list = []
    for r, c in my_area:
        # 인접한 영역을 담을 리스트
        adj_list = []
        flag = 0
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                if area[nr][nc] != 0:
                    # 인접 영역에 상대 영역이 있다면 지원 유형 중의 2번째다.
                    if area[nr][nc] != x:
                        flag = 1
                    else:
                        adj_list.append((nr, nc))

        # 지원 유형에 따라 다른 지원 커맨드를 지원 정보 리스트에 담는다. 지원 병력 값은 여기서 구한다.
        support_power = mp[r][c] // 5
        if flag:
            support_area = []
            for ar, ac in adj_list:
                if mp[ar][ac]*5 < mp[r][c]:
                    support_area.append((ar, ac))

            support_list.append((support_area, r, c, support_power))
        else:
            support_list.append((adj_list, r, c, support_power))

    # 지원 정보 리스트에서 각 지원 커맨드를 꺼내와 계산을 실행한다. 공격과 마찬가지로 여기서 지원 병력 값을 구하면 틀린다.
    for support_area, r, c, support_power in support_list:
        for sr, sc in support_area:
            mp[sr][sc] += support_power
            mp[r][c] -= support_power


# 보충은 그냥 더한다.
def supplement():
    for i in range(N):
        for j in range(N):
            mp[i][j] += sup[i][j]


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(1, int(input())+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    mp = [list(map(int, input().split())) for _ in range(N)]
    sup = [list(map(int, input().split())) for _ in range(N)]
    # 산의 개수를 미리 구해놓는다. 나중에 attack 함수에서 적들 칸의 개수 + 산의 개수가 N**2면 나는 패배한 것이다.
    mountain = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] == 0:
                mountain += 1

    defeat = set()
    victory = 0
    turn = 0
    while not victory:
        # turn%3+1을 통해서 1, 2, 3을 번갈아 받는다.
        x = turn % 3 + 1
        turn += 1
        # 내가 패배한 상태면 진행하지 않는다. 중복을 피해 이것을 지우고 싶다면 attack함수 내에서 어차피 똑같이 써야 한다.
        if x in defeat:
            continue

        attack(x)
        # 패배했는지 여부를 attack 함수에서 판단한다. 따라서 여기도 패배했는지의 확인을 해야 한다.
        if x in defeat:
            continue

        support(x)
        supplement()

    result = 0
    for i in range(N):
        for j in range(N):
            result += mp[i][j]

    print('#%d %d' % (t, result))