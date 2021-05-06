# [professional] 합
# N개의 정수가 입력으로 주어진다.
# 이때 연속하여 몇 개의 정수를 골라 합을 구할 수 있다.
# 예를 들어, 1 3 -8 18 -8 이 있다고 하자.
# 그럼 2번부터 4번까지의 수를 골라 합을 구하면, 3+(-8)+18 = 13이다.
# 이렇게 연속해서 정수를 골라 합을 구할 때, 그 합의 최대가 몇인지 구하는 프로그램을 작성하세요.


# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)
# 각 테스트 케이스 첫째 줄에 숫자 N이 주어진다. (3 ≤ N ≤ 100,000)
# 둘째 줄에는 절대값이 1000이하의 정수 N개가 공백을 사이에 두고 입력된다.


# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, 연속된 정수의 합의 최대값을 출력하시오.


# i번째 기준 내 앞까지의 최적해에 나를 더한 것과 나 자신 중에 큰 것이 i번째 최적해가 된다.
for t in range(1, int(input())+1):
    N = int(input())
    num = list(map(int, input().split()))
    DP = [0]*N
    DP[0] = num[0]
    for i in range(1, N):
        DP[i] = max(DP[i-1] + num[i], num[i])

    print('#%d %d' % (t, max(DP)))


# 2
# DP가 아닌 풀이
def get_total(nums):
    global max_total

    # 음수로만 이루어져 있다면 제일 큰 값이 큰 합
    positive = 0
    for i in range(N):
        if nums[i] > 0:
            positive = 1

    if not positive:
        max_total = max(nums)
        return

    total = 0
    for i in range(N):
        total += nums[i]
        if total > max_total:
            max_total = total
        # 합이 음수가 되는 순간 그 다음 원소부터
        if total < 0:
            total = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_total = -10 ** 20
    get_total(nums)
    print('#%d %d' % (t, max_total))


# 3
# DP 뒤부터
for t in range(1, int(input())+1):
    N, num_list = int(input()), list(map(int, input().split()))
    dp = [0]*N
    dp[N-1] = num_list[N-1]
    for i in range(N-2, -1, -1):
        dp[i] = max(num_list[i], num_list[i] + dp[i+1])
    print("#%d %d" %(t, max(dp)))