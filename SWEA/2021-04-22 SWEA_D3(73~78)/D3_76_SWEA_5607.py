# 조합
# 자연수 N와 R가 주어진다. 이 때의 N combination R의 값을 1234567891로 나눈 나머지를  출력하세요.
# 예를들면 N이 4, R이 2라면 4 combination 2는 (4 * 3) / (2 * 1) = 6이 된다.


# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)
# 각 케이스의 첫 줄에 정수 N, R이 주어진다. (1 ≤ N ≤ 1000000, 0 ≤ R ≤ N)


# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, N combination R을 1234567891로 나눈 나머지를 출력하시오.


# def recursive_combi(n, r):
#     if mm[n][r]:
#         return mm[n][r]
#
#     if r == 0 or n == r:
#         mm[n][r] = 1
#         return 1
#
#     mm[n][r] = recursive_combi(n-1, r-1) + recursive_combi(n-1, r)
#
#     return mm[n][r]


for t in range(1, int(input())+1):
    N, R = map(int, input().split())
    mm = [[0]*(R+1) for _ in range(N+1)]
    queue = [(1, 0), (1, 1)]
    ans = 0
    while queue:
        n, r = queue.pop(0)

        queue.append((n + 1, r))
        if r == 0:
            mm[n][r] = 1
            ans += 1
        elif r == n and r < R:
            mm[n][r] = 1
            ans += 1
            queue.append((n+1, r+1))
        else:
            mm[n][r] = mm[n-1][r-1] + mm[n-1][r]
            ans += mm[n][r]

        if n == N and r == R:
            break

    print('#%d %d' % (t, mm[N][R]%1234567891))
