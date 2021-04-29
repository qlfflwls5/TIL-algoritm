# 0/1 Knapsack
# 민수에게는 1번부터 N번까지의 번호가 부여된 N(1≤N100)개의 물건과 최대 K(1≤K≤1000) 부피만큼을 넣을 수 있는 가방이 있다.
# 1번 물건부터 N번 물건 각각은 부피  Vi와 가치 Ci 를 가지고 있다. (1≤Vi, Ci≤100)
# 민수는 물건들 중 몇 개를 선택하여 가방에 넣어서 그 가치의 합을 최대화하려고 한다.
# 단, 선택한 물건들의 부피 합이 K 이하여야 한다.
# 민수가 가방에 담을 수 있는 최대 가치를 계산하자.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫째 줄에 물건의 개수와 가방의 부피인 N K가 주어진다.
# 다음 N개의 줄에 걸쳐서 i번 물건의 정보를 나타내는 부피  Vi와 가치 Ci가 주어진다.


# [출력]
# 각 테스트 케이스마다 가방에 담을 수 있는 최대 가치를 출력한다.


# 1
# DP - 구글링을 해서 내용을 이해하고 풀이했다.
# N-1번째 부터 시작하여 1씩 줄어드는 i번째를 기준으로
def knapsack(v, i):
    # 현재 부피가 K이거나, i가 -1이면(모든 물건에 대한 탐색 완료) 더 이상 넣을 것이 없다. 0반환
    if v == K or i == -1:
        return 0
    # i번째 물건을 넣었을 때 부피를 초과하여 넣을 수 없다면 i-1번째까지의 최적 결과와 이번 결과가 같다.
    if v + V[i] > K:
        return knapsack(v, i-1)
    # i번째 물건을 넣을 수 있다면 i번째 물건을 넣으면서 늘어난 부피와 늘어난 가치를 고려한 최적 결과와, 넣지 않았을 때(i-1번째의 최적 결과) 중 max값을 리턴
    return max(C[i] + knapsack(v+V[i], i-1), knapsack(v, i-1))


for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    V = []
    C = []
    for _ in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    print('#%d %d' % (t, knapsack(0, N-1)))


# 2
# DP - 2차원 배열
def knapsack(k, v, c, n):  # W: 가방의 부피 한도, wt: 각 물건의 부피, val: 각 물건의 가치, n: 물건의 수
    arr = [[0]*(k+1) for _ in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(k+1):  # 각 칸을 돌면서
            if i==0 or w==0:  # 0번째 행/열은 0으로 세팅
                arr[i][w] = 0
            elif v[i-1] <= w:  # 점화식을 그대로 프로그램으로
                arr[i][w] = max(c[i-1]+arr[i-1][w-v[i-1]], arr[i-1][w])  # max 함수 사용하여 큰 것 선택
            else:
                arr[i][w] = arr[i-1][w]
    return arr[n][k]


for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    V = []
    C = []
    for _ in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    print('#%d %d' % (t, knapsack(K, V, C, N)))
