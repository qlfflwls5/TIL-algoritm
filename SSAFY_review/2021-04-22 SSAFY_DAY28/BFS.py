# BFS
# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
# 모든 정점을 너비우선탐색 하여 경로를 출력하시오. 시작 정점을 1로 시작하시오.
# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

# 출력 결과의 예는 다음과 같다.
# 1-2-3-4-5-7-6


def BFS(v):
    visited = [0] * (V + 1)
    queue = [v]
    visited[1] = 1
    while queue:
        x = queue.pop(0)
        for w in AL[x]:
            if not visited[w]:
                visited[w] = 1
                way.append(w)
                queue.append(w)


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)

    way = [1]
    BFS(1)
    print('#%d %s' % (t, ' '.join(map(str, way))))
    
    
# 2
# pop과 append를 활용하는 것이 아닌, front rear를 활용해서 해보기(front는 삭제용, rear는 삽입용)
# 이 경우 queue가 먼저 고정된 길이를 갖는다.(정점의 개수)
def BFS(v):
    visited = [0] * (V + 1)
    queue = [0] * V
    front, rear = 0, 0
    visited[v] =1
    queue[rear] = v
    rear += 1
    while rear > front:
        x = queue[front]
        front += 1
        for w in AL[x]:
            if not visited[w]:
                visited[w] = 1
                queue[rear] = w
                rear += 1

    return queue


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)

    print('#%d %s' % (t, ' '.join(map(str, BFS(1)))))