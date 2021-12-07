# 두 개의 탑
# 1번부터 N번까지의 지점이 있다. 각각의 지점들은 차례로, 그리고 원형으로 연결되어 있다.
# 이 지점들 중 두 곳에 두 개의 탑을 세우려고 하는데, 두 탑의 거리가 최대가 되도록 만들려고 한다.

# 지점들이 원형으로 연결되어 있기 때문에, 두 지점 사이에는 시계방향과 반시계방향의 두 경로가 존재한다.
# 두 지점 사이의 거리를 잴 때에는, 이러한 값들 중에서 더 작은 값을 거리로 한다.

# 연결되어 있는 두 지점 사이의 거리가 주어졌을 때, 두 탑의 거리의 최댓값을 계산하는 프로그램을 작성하시오.


# 입력
# 첫째 줄에 지점의 개수 N(2 ≤ N ≤ 50,000)이 주어진다. 다음 N개의 줄에는 차례로 두 지점 사이의 거리가 양의 정수로 주어진다. 전체 거리의 총 합은 1,000,000,000을 넘지 않는다.


# 출력
# 첫째 줄에 답을 출력한다.


# 예제 입력 1
# 5
# 1
# 2
# 3
# 4
# 5
# 예제 출력 1
# 7


from sys import stdin
input = stdin.readline

N = int(input())
dists = [0] + [int(input()) for _ in range(N)]
total = sum(dists)
limit = total // 2
max_v = 0
for i in range(1, N+1):
    dists[i] += dists[i-1]

end = 1
for i in range(N-1):
    while end < N and dists[end] - dists[i] <= limit:
        end += 1

    if dists[end] - dists[i] <= limit:
        max_v = max(max_v, dists[end] - dists[i])
    else:
        max_v = max(max_v, total - (dists[end] - dists[i]),
                dists[end-1] - dists[i])

print(max_v)


# 2
N = int(input())
dists = [int(input()) for _ in range(N)]
total = sum(dists)
s1, s2 = dists[0], total - dists[0]
max_v = 0
start, end = 0, 1
while start < end and end < N:
    max_v = max(max_v, min(s1, s2))
    if s1 < s2:
        s1 += dists[end]
        s2 -= dists[end]
        end += 1
    else:
        s1 -= dists[start]
        s2 += dists[start]
        start += 1

print(max_v)