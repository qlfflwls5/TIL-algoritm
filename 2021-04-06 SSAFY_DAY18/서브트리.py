# 서브트리
# 주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.
# 이런 경우의 트리는 부모 노드를 인덱스로 다음과 같은 방법으로 나타낼 수 있다. 자식 노드가 0인 경우는 노드가 자식이 없는 경우이다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
# 노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 1
def preorder(x):
    if x:
        global cnt
        cnt += 1
        preorder(left[x])
        preorder(right[x])


for t in range(1, int(input())+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    left = [0]*(E+2)
    right = [0]*(E+2)
    for p, c in zip(edges[::2], edges[1::2]):
        if left[p]:
            right[p] = c
        else:
            left[p] = c

    cnt = 0
    preorder(N)
    print('#%d %d' % (t, cnt))


# 2
# 개수만 세는 것이라면...
for t in range(1, int(input())+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    sub_node = {N}
    cnt = 1
    for i in range(E):
        if edges[2*i] in sub_node:
            cnt += 1
            sub_node.add(edges[2*i+1])

    print('#%d %d' % (t, cnt))


# 3
# 서브트리에 대한 풀이
def subtree(n):
    global cnt
    node = tree[n]
    cnt += 1
    if node:
        for i in node:
            subtree(i)


for t in range(1, int(input()) + 1):
    e, n = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[] for _ in range(e + 2)]
    for i in range(e):
        tree[nodes[2 * i]].append(nodes[2 * i + 1])
    cnt = 0
    subtree(n)
    print('#%d %d' % (t, cnt))