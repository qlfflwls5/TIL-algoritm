# 행성 터널
# 때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다.
# 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.
# 행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.


# 입력
# 첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다.
# 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다.
# 한 위치에 행성이 두 개 이상 있는 경우는 없다.


# 출력
# 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.


# 예제 입력 1
# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19
# 예제 출력 1
# 4


from sys import stdin
input = stdin.readline


def find_set(p, x):
    if x != p[x]:
        p[x] = find_set(p, p[x])
    return p[x]


N = int(input())
planets = [list(map(int, input().split())) + [i] for i in range(N)]
edges = []
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(1, N):
        edges.append([planets[j-1][3], planets[j][3], abs(planets[j-1][i] - planets[j][i])])

edges.sort(key=lambda x: x[2])
p = [i for i in range(N)]
S = 0
cnt = 0
for s, e, w in edges:
    if find_set(p, s) != find_set(p, e):
        p[find_set(p, e)] = find_set(p, s)
        S += w
        cnt += 1
        if cnt == N-1:
            break

print(S)


# 2
# 경로 압축을 사용하지 않고도 정렬을 필요한 부분만 해줌으로써 시간 초과하지 않고 통과할 수 있는 풀이
from sys import stdin
input = stdin.readline


def find(k):
    while numbers[k] != k:
        k = numbers[k]
    return k

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        numbers[y] = x
    else:
        numbers[x] = y


N = int(input())
numbers = [i for i in range(N)]
xyz = [[] for _ in range(3)]
connections = []
ans = 0
for i in range(N):
    a, b, c = map(int, input().split())
    xyz[0].append([i, a])
    xyz[1].append([i, b])
    xyz[2].append([i, c])

for i in range(3):
    xyz[i].sort(key=lambda x: x[1])

for i in range(3):
    for j in range(N-1):
        connections.append([xyz[i][j][0], xyz[i][j+1][0], abs(xyz[i][j][1] - xyz[i][j+1][1])])

connections.sort(key=lambda x: x[2])

for i in range(len(connections)):
    if find(numbers[connections[i][0]]) != find(numbers[connections[i][1]]):
        union(connections[i][0], connections[i][1])
        ans += connections[i][2]

print(ans)