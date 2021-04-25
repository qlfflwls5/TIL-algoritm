# 서브트리
# 트리의 일부를 서브 트리라고 한다. 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
# 주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
# 노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


def subtree(node):
    if node:
        cnt[0] += 1
        subtree(tree[node][0])
        subtree(tree[node][1])


for t in range(1, int(input())+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(E + 2)]
    for i in range(E):
        if tree[edges[i*2]][0]:
            tree[edges[i*2]][1] = edges[i*2 + 1]
        else:
            tree[edges[i*2]][0] = edges[i*2 + 1]

    cnt = [0]
    subtree(N)
    print('#%d %d' % (t, cnt[0]))