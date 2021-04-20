# 전기버스2
# 충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
# 충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
# 정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.
# 다음은 1번에서 출발 5번이 종점인 경우의 예이다.
# 1번에서 장착한 충전지 용량이 2이므로, 3번 정류장까지 운행할 수 있다. 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.
# 마지막 정류장에는 배터리가 없다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다


def DFS(cur, cnt):
    # 가지치기1: 이미 최소 교체 횟수를 넘은 경우
    if cnt >= min_change[0]:
        return

    end = cur + station[cur]
    if end >= N-1:
        min_change[0] = cnt
        return

    for i in range(cur+1, end+1):
        # 가지치기2: i에서 갈 수 있는 가장 먼 정류장이 현재 cur에서 갈 수 있는 경우 가지치기
        if i < N-1 and i + station[i] > end:
            DFS(i, cnt+1)


for t in range(1, int(input())+1):
    data = list(map(int, input().split()))
    N, station = data[0], data[1:]
    min_change = [N]
    DFS(0, 0)
    print('#%d %d' % (t, min_change[0]))


# data 입력받는 부분 이렇게도 가능하다.
# N, *station = map(int, input().split())


# 2
# DP풀이
# 내 풀이는 아니다. 배워두자.
def dp(idx):
    min_change = N
    for i in range(idx):
        if battery_dp[i] + 1 < min_change and i + battery[i] >= idx:
            min_change = battery_dp[i] + 1
    return min_change


for t in range(1, int(input()) + 1):
    battery = list(map(int, input().split()))
    N, battery = battery[0], battery[1:]
    battery_dp = [0] * N
    min_arrive = N
    for i in range(1, N):
        battery_dp[i] = dp(i)
    print("#%d %d" % (t, battery_dp[-1] - 1))


# 거꾸로 가면서
# 만약 지금 정류장에서 한 번에 도착지점을 못간다면 도착지점을 갈 수 있는 정류장으로 이동해야 하니, +1
# 그 과정에서 가장 최소 횟수로 도달할 수 있는 곳에 가는 것
# mm(메모이제이션)은 i번째에서 몇 번을 충전해야 도달할 수 있는지를 저장한다.
def dp(i):
    if mm[i] is None:
        if i + S[i] >= N - 1:
            mm[i] = 0
        else:
            mm[i] = min(mm[i + 1: i + 1 + S[i]]) + 1
    return mm[i]


T = int(input())
for test_case in range(1, T + 1):
    N, *S = map(int, input().split())

    mm = [None] * N
    for i in range(N - 2, -1, -1):
        dp(i)

    print('#%d %d' % (test_case, mm[0]))


# 3
# 다른 dfs
def go(i, cnt, battery):
    global answer
    if i + battery >= N - 1:
        answer = min(answer, cnt)
        return
    if cnt >= answer:
        return
    # 배터리 잔량이 있으면 일단 계속 가기
    if battery:
        go(i + 1, cnt, battery - 1)
    # 그러다가 현재 배터리 잔량보다(갈 수 있는 거리) 더 큰 배터리가 있으면(더 멀리 갈 수 있으면) 갈아끼기
    if S[i] > battery:
        go(i + 1, cnt + 1, S[i] - 1)


T = int(input())
for test_case in range(1, T + 1):
    N, *S = map(int, input().split())

    answer = N - 2
    go(0, 0, 0)
    print('#%d %d' % (test_case, answer - 1))


# 4
# 나의 DP
for t in range(1, int(input()) + 1):
    N, *station = map(int, input().split())
    dp = [[] for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, i+station[i]+1):
            if not dp[i]:
                dp[j].append(1)
            elif j < N:
                dp[j].append(min(dp[i])+1)

    print('#%d %d' % (t, min(dp[N-1])-1))
