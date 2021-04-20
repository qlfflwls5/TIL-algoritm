# 그래프 경로 코드
# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
# 예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
# 노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
# 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
# E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 1
# 스택 함수 다 사용해보기, AM으로 풀기
def push(s, v):
    s.append(v)


def pop(s):
    if len(s) == 0:
        return

    return s.pop(-1)


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    
    # 인접행렬 만들기
    AM = [[0]*(V+1) for _ in range(V+1)]
    for s, e in edges:
        AM[s][e] = 1

    stack = []
    visited = [0]*(V+1)
    way = []
    result = 0
    push(stack, S) # 그냥 append쓰면 되긴 한다. 구색을 맞춰보았다.
    while len(stack):
        v = pop(stack) # while문의 조건 때문에 어차피 pop그냥 해도 index error는 안나지만 구색을 맞춰보았다.
        if not visited[v]:
            visited[v] = 1
            if v == G:
                result = 1
                break
            way.append(v)
            for w in range(len(AM[v])):
                if AM[v][w] and not visited[w]:
                    push(stack, w)

    print('#%d %d' %(t, result))
    
    
# 2
# 스택 함수 사용하지 않고 AL로 풀기
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    AL = [[] for _ in range(V+1)]
    for s, e in edges:
        AL[s].append(e)

    stack = []
    visited = [0]*(V+1)
    way = []
    result = 0
    stack.append(S)
    while len(stack):
        v = stack.pop(-1)
        if not visited[v]:
            visited[v] = 1
            if v == G:
                result = 1
                break
            way.append(v)
            for w in AL[v]:
                stack.append(w)

    print('#%d %d' %(t, result))


# 3
# 재귀
def DFS_Recursive(AL, v):
    visited[v] = 1
    way.append(v)
    if v == G:
        return

    for w in AL[v]:
        if not visited[w]:
            DFS_Recursive(AL, w)

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    AL = [[] for _ in range(V+1)]
    for s, e in edges:
        AL[s].append(e)

    visited = [0]*(V+1)
    way = []
    DFS_Recursive(AL, S)
    if way[-1] == G:
        result = 1
    else:
        result = 0

    print('#%d %d' %(t, result))