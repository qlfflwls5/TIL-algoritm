# 트리 순회
# 첫 줄에는 트리의 노드의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다. 간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상“부모 자식”순서로 표기된다.
# 아래 예에서 두 번째 줄 처음 1 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
# 간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.
# 13 ← 노드의 수
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
#
# 이진 트리를 전/중/후위 순회하고 방문한 노드의 번호를 출력하시오.


def order(node):
    if node:
        pre_way.append(str(node))
        order(tree[node][0])
        in_way.append(str(node))
        order(tree[node][1])
        post_way.append(str(node))


for t in range(1, int(input())+1):
    N = int(input())
    tree = [[0, 0] for _ in range(N+1)]
    edges = list(map(int, input().split()))
    for p, c in zip(edges[::2], edges[1::2]):
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c

    pre_way, in_way, post_way = [], [], []
    order(edges[0])
    print('#%d\n%s\n%s\n%s' % (t, '-'.join(pre_way), '-'.join(in_way), '-'.join(post_way)))

