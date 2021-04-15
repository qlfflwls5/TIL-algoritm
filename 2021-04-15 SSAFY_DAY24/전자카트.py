# 전자카트
# 골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.
# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.
# 각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.
# 두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.
# N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.
# e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91
# e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89
# 이 경우 최소 소비량은 89가 된다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


def perm(level, room, S):
    if S > min_e[0]:
        return

    if level == N-1:
        if S + e[room][0] < min_e[0]:
            min_e[0] = S + e[room][0]
        return

    for i in range(1, N):
        if not check[i] and i != room:
            check[i] = 1
            perm(level+1, i, S + e[room][i])
            check[i] = 0


for t in range(1, int(input())+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    min_e = [N << 8]
    perm(0, 0, 0)
    print('#%d %d' % (t, min_e[0]))


# 2
# 호근님 코드 - 뭘까
# visited를 리스트가 아닌 비트연산으로 하는 것! 방문할 때마다 visited |= 1 << i를 통해서 구현.
# 예를 들어, 첫 요소를 방문하면 visited가 0001이 되고, 두 번째 요소를 방문하면 0001 |= 1 << 2, 0011이 된다.
# 이후 재귀 부분에서 1~n까지의 j를 통해 1 << j & visited를 해서 1이 아닐 때만 해당 요소에 대해 재귀를 수행한다.
# 위 예를 이용하자면 visited가 0011일때, j는 1, 2에서는 1 << j & visited가 1이므로 재귀를 하지 않고 j가 3, 4일 때는 값이 0이므로 방문하지 않은 것이니 재귀를 한다.
# (1 << N) - 1을 하면 N개의 1로 이루어진 비트가 된다. 즉, 모든 요소를 다 방문한 상태 
def go(i, visited):
    visited |= 1 << i
    if visited == (1 << N) - 1:
        return grid[i][0]
    return min(grid[i][j] + go(j, visited) for j in range(N) if not 1 << j & visited)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print('#%d %d' % (test_case, go(0, 0)))
    
    
# 3
# swap을 통한 순열 구현
# 시작지점은 포함을 안한 순열을 구한 것이다. 예를 들어, 1 - 2 - 3 - 1이라면 2 - 3을 구하는 순열이다.
# 꼭 작업을 머리에 그려보자
def battery_use(idx):
    if idx == manage_num:
        global battery
        # 시작지점을 빼고 구한 순열이므로 이것을 더해준다. 예를들어, 1 - 2와 3 - 1은 따로 구해서 더해준 것
        battery_sum = area[0][manage[0]] + area[manage[-1]][0]
        for i in range(manage_num - 1):
            battery_sum += area[manage[i]][manage[i + 1]]
        battery.append(battery_sum)
    else:
        for i in range(idx, manage_num):
            manage[idx], manage[i] = manage[i], manage[idx]
            battery_use(idx + 1)
            manage[idx], manage[i] = manage[i], manage[idx]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    manage = list(range(1, N))
    manage_num = N - 1
    battery = []
    battery_use(0)
    print('#%d %d' % (t, min(battery)))