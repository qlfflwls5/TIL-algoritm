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


def find_set(x):
    while x != p[x]:
        x = p[x]

    return x


N = int(input())
planets = [list(map(int, input().split())) + [i] for i in range(N)]
edges = []
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(1, N):
        edges.append([planets[j-1][3], planets[j][3], abs(planets[j-1][i] - planets[j][i])])

edges.sort(key=lambda x: x[2])
print(edges)
p = [i for i in range(N)]
S = 0
cnt = 0
for s, e, w in edges:
    if find_set(s) != find_set(e):
        p[find_set(e)] = find_set(s)
        S += w
        cnt += 1
        if cnt == N-1:
            break

print(S)