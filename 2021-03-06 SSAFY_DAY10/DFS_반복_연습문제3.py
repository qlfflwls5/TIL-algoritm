# live 중 DFS 연습문제 3
# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오.
# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7


# DFS 반복
V, E = 7, 8
# 입력이 아래와 같다면
edges = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
edges = list(map(int, edges.split())) # input().split()으로 쓰게 될 것
edges = [(edges[i], edges[i+1]) for i in range(0, len(edges), 2)]
# 입력이 아래와 같다면
# 7 8
# 1 2
# 1 3
# 2 4
# 3 5
# 4 6
# 5 6
# 6 7
# 3 7
# edges = [tuple(map(int, input().split())) for _ in range(E)]


# 인접행렬
AM = [[0]*(V+1) for _ in range(V+1)]
for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1 # 방향성이 없을 때만 이 문장이 추가된다.


# 인접리스트
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s) # 방향성이 없을 때만 이 문장이 추가된다.


# 스택 함수 => 실제 문제 풀 때는 가장 위에 적게 될 것
def push(stack, v):
    stack.append(v)


def pop(stack):
    if len(stack) == 0:
        return

    return stack.pop(-1)


# DFS 구현
stack = []
visited = [False]*(V+1)
# 경로를 저장할 리스트
way = []
# 정점 1부터 시작한다했으므로
push(stack, 1) # 그냥 append 사용해도 된다.
while len(stack):
    v = pop(stack) # 그냥 pop 사용해도 된다. while문 조건에서 어차피 길이가 0이면 걸러진다.
    if not visited[v]:
        visited[v] = True
        way.append(v)
        for w in AL[v]:
            if not visited[w]:
                push(stack, w)
        # 인접 행렬을 사용하는 경우
        # for w in range(len(AM[v])):
        #     if AM[v][w] and not visited[w]:
        #         push(stack, w)

print(way)
