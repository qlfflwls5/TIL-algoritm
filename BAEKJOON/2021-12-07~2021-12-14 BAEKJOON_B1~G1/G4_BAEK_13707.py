# 합분해 2
# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.
# 덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.


# 입력
# 첫째 줄에 두 정수 N(1 ≤ N ≤ 5,000), K(1 ≤ K ≤ 5,000)가 주어진다.


# 출력
# 첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.


# 예제 입력 1
# 20 2
# 예제 출력 1
# 21


# 규칙 (위 + 왼쪽 = 나)
# 만들기(1, 2, 3, 4, ..., N)
# K별로
# 1 1 1 1
# 2 3 4 5
# 3 6 10 15
# 4 10 20
# 5 15 35
# 6 21
# 즉, K개로 N만들기 = K개로 N-1 만들기 + K-1개로 N 만들기 => 조합의 공식과 비슷
# N, K = map(int, input().split())
# dp = [[i] + [1] * (N-1) for i in range(1, K+1)]
# for i in range(1, K):
#     for j in range(1, N):
#         dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
#
# print(dp[K-1][N-1])


# 2 결국 규칙을 찾아보면 (N+K-1)개 중에 N개를 뽑는 조합 (N+K-1)CN
def nCr(n, r):
    numerator = 1
    denominator = 1
    k = min(r, n-r)
    for i in range(1, k+1):
        denominator *= i
        numerator *= n+1-i

    return numerator // denominator


N, K = map(int, input().split())
print(nCr(N+K-1, N) % 1000000000)