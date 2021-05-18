# 달리기
# N명의 사람이 달리기를 했고 순위가 매겨졌다.
# 같은 사람이 같은 시점에 완주한 경우가 없었기 때문에, 모든 사람의 등수는 다르다.
# 이제 이 달리기를 한 지 너무 오래되어 정확한 순위를 기억하는 사람은 없고,
# 어떤 두 사람을 비교할 때 누가 먼저 들어왔는지에 대한 정보만 M개 남아있다.
# 이 때, N명의 사람이 들어오는 순서로 가능한 모든 경우의 수를 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 두 정수 N,M이 공백으로 구분되어 주어진다.
# 다음 M개의 줄의 i번째 줄에는 두 정수 Xi, Yi가 공백으로 구분되어 주어진다.
# 이는 달리기를 한 N명의 사람을 차례대로 1에서 N까지 번호로 정했을 때,
# xi번 사람이 yi번 사람보다 먼저 완주했다는 것을 나타낸다.
# 같은 조건이 여러 번 주어지는 경우는 없으며, M개의 모든 경우를 만족하는 등수가 적어도 하나는 존재한다.


# [출력]
# 각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 각 테스트 케이스마다 N명의 사람이 들어오는 순서로 가능한 모든 경우의 수를 출력한다.


# 내 풀이
# 답은 맞으나, 제한시간 초과
def DFS(level, now):
    if level == len(consider)-1:
        global cnt
        cnt += 1
        visited[now] = 0
        return

    for i in consider:
        if i != now and not visited[i] and check(i):
            visited[i] = 1
            DFS(level+1, i)
            visited[i] = 0


def check(i):
    for f in front[i]:
        if not visited[f]:
            return 0

    return 1


def factorial(N):
    if N == 1:
        return 1

    return N * factorial(N-1)


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    front = [[] for _ in range(N+1)]
    consider = set()
    for _ in range(M):
        x, y = map(int, input().split())
        front[y].append(x)
        consider.add(x)
        consider.add(y)

    consider = list(consider)
    visited = [0] * (N + 1)
    cnt = 0
    for i in range(1, N+1):
        if i in consider and not front[i]:
            visited[i] = 1
            DFS(0, i)
            visited[i] = 0

    print('#%d %d' % (t, (factorial(N) // factorial(len(consider)) * cnt)))


# 2
# 홈페이지 정답자들의 풀이 -> dp
def dp(n):
    if n == (1 << N) - 1:
        return 1
    if arr[n] != - 1:
        return arr[n]
    arr[n] = 0
    for i in range(N):
        if n & (1 << i) == 0 and solve(n, i):
            arr[n] += dp(n | (1 << i))
    return arr[n]


def solve(n, idx):
    for i in data[idx]:
        if (n & 1 << i) > 0:
            return False
    return True


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [[] for _ in range(N)]

    for _ in range(M):
        x, y = map(int, input().split())
        data[y - 1].append(x - 1)

    arr = [- 1] * (1 << N)
    print("#{} {}".format(test_case + 1, dp(0)))