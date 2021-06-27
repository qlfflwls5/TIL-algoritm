# DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.


# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.


# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
def dfs(s):
    visited = [0] * N
    stack = [s]
    result = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            result.append(v + 1)
            for w in AL[v][::-1]:
                if not visited[w]:
                    stack.append(w)

    return result


def bfs(s):
    visited = [0] * N
    queue = [s]
    visited[s] = 1
    rear = 0
    result = []
    while rear < len(queue):
        v = queue[rear]
        rear += 1
        result.append(v + 1)
        for w in AL[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = 1

    return result


N, M, V = map(int, input().split())
AL = [[] for _ in range(N)]
for _ in range(M):
    s, e = map(int, input().split())
    AL[s - 1].append(e - 1)
    AL[e - 1].append(s - 1)

for i in range(N):
    AL[i].sort()

print(*dfs(V - 1))
print(*bfs(V - 1))

