# 전기버스
# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.


# [입력]
# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )


# [출력]
# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.


# 1
# 해당 위치에서 충전을 해야하는가를 확인
# 복잡하지만 규칙이 있다. 이전 충전기와 다음 충전기 사이의 거리가 K보다 멀다면 무조건 지금 충전기에서 충전을 해야한다.
# 문제는 K보다 멀지 않을 때이다. 지금 바로 충전을 해야하는지, 다음 충전기에서 해도 되는지를 판별해야한다.
# 최대 효율을 위해서는 K 거리 내에 여러 충전기가 있을 경우 가장 마지막 충전기에서 충전을 해야 한다.
# 그러므로 이전 충전기와 다음 충전기가 K거리 내에 있는 경우 지금 충전기에서 충전을 해야 하는 경우는 K번째 전의 충전기와 내가 연달아 붙어있을 때 뿐이다.
T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    K_list = list(range(N+1))
    result = 0

    if M_list[0] > K or N - M_list[-1] > K:
        print('#%d 0' % t)
        continue

    for i in range(len(M_list)):
        # 충전기 사이 거리가 K보다 크면 불가능
        if M_list[i] - M_list[i-1] > K:
            result = 0
            break
        # 첫 시작에서 첫 충전기까지의 거리를 계산
        if i == 0:
            if M_list[1] > K:
                result += 1
        # 마지막 충전기에서 도착점까지의 거리를 계산
        elif i == len(M_list) - 1:
            if len(M_list) - M_list[i - 1] > K:
                result += 1
        # 현재 위치의 충전기에서 충전을 해야하는지를 판별
        else:
            # 이전 충전기와 다음 충전기 사이의 거리가 K보다 멀면 지금 충전해야함
            if M_list[i+1] - M_list[i-1] > K:
                result += 1
            # K이하이면 K번째 전의 충전기와 지금 충전기 사이의 거리가 K라면(이하여도됨) 충전하고 아니면 하지 않는다.
            else:
                if M_list[i] - M_list[i-K] <= K:
                    result += 1

    print('#%d %d' %(t, result))
    
    
# 2
# 지금 위치에서 K칸 만큼 가는데, 그 도중 가장 먼 곳으로 간다!
# 예를들어, 연달아 붙어있다면 최소 정류장을 거치기 위해 가장 띄엄띄엄 가야하는데
# 이를 뒤부터 탐색해서 최대의 정류장을 가게 되는 것
T = int(input())
for t in range(1, T + 1):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split()))
    result = 0
    start = 0
    impossible = False
    while True:
        end = start + k
        # 끝에 도달하거나 불가능이면 탈출
        if end >= n or impossible:
            break
        # 뒤부터 탐색하여 K범위 내 가장 먼 충전기와 만나면 진행, 못만나면 불가능
        for i in range(end, start - 1, -1):
            # 간 곳이 start와 같으면 충전기가 없는 것이다. 불가능으로 판별
            if i == start:
                impossible = True
                break
            # 간 곳이 충전기이면 진행
            if i in stations:
                start = i
                result += 1
                break

    if impossible:
        print('#%s 0' % t)
    else:
        print('#%s %s' % (t, result))


# 3
T = int(input())

for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    x = 0
    cnt = 0

    while x < N - K: # N - K까지만 가도 다음 회차에 무조건 통과하므로
        for i in range(K, 0, -1):
            if x + i in M_list: # 근데 이거 중요. in은 순차 탐색으로 복잡도를 높인다. 안쓰는게 좋다
                x += i
                cnt += 1
                break
        else:
            x = N
            cnt = 0

    print('#%d %d' % (t, cnt))