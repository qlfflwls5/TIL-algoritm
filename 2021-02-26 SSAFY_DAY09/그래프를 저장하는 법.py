# 1
# 방향성 있는 비가중치 그래프
V, E = 5, 6  # V = 정점, E = 간선
edges = [(1, 2), (2, 3), (1, 4), (2, 4), (1, 5), (3, 5)]

# 인접행렬
AM = [[0] * (V + 1) for _ in range(V + 1)]  # 0을 안쓰니깐 V+1 크기로 만드는 것
for s, e in edges:
    AM[s][e] = 1

for line in AM:
    print(line)

# 인접리스트 -> 성능적으로 인접행렬보다 좋다.
AL = [[] for _ in range(V + 1)]
for s, e in edges:
    AL[s].append(e)

for v in range(1, V + 1):
    if AL[v]:
        print(v, AL[v])
# [2, 4, 5], [3, 4], [5]


# 2
# 방향성이 없는 비가중치 그래프
V, E = 7, 8
edges = [(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (3, 7), (4, 6), (5, 6)]

AM = [[0] * (V + 1) for _ in range(V + 1)]
for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1

AL = [[] for _ in range(V + 1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s)