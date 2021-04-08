# 루트 시각화
# 루트 있는 트리를 입력으로 받아 아래와 같이 출력하는 알고리즘을 작성하라 .
# 트리의 각 노드에는 1,000 미만의 자연수가 저장되어 있다 .
# 트리의 노드 연결 관계는 다음과 같이 표현해야 한다 .
# 아래 출력에서 루트에는 자식이 3 개 있고 그 자식들 중 하나는 더 이상 자식이 없는 것임을 알 수 있을 것이다.

# [030]--+--[054]-----[001]
#        +--[002]
#        L--[045]-----[123]

# 입력은 전체 노드의 개수 N이 주어지고, 그 아래줄에 부모 노드와 자식 노드의 쌍으로 주어진다고 가정한다.
# 위의 예에서는 30 54 30 2 30 45 54 1 45 123


def draw_tree(level, p, c):
    if level == 0:
        print('[%s]' % c.zfill(3), end='')
        for node in tree[c]:
            draw_tree(level+1, c, node)
        return

    if len(tree[p]) > 1:
        if c == tree[p][0]:
            print('--+--[%s]' % c.zfill(3), end='')
        elif c == tree[p][-1]:
            print((2*level-1) * '     ', end='')
            print('  L--[%s]' % c.zfill(3), end='')
        else:
            print((2*level-1) * '     ', end='')
            print('  +--[%s]' % c.zfill(3), end='')
    elif len(tree[p]) == 1:
        print('-----[%s]' % c.zfill(3), end='')

    if not tree.get(c):
        print()
        return
    for node in tree[c]:
        draw_tree(level+1, c, node)


N = int(input())
tree = {}
e = list(input().split())
for i in range(N-1):
    tree[e[2*i]] = tree.get(e[2*i], []) + [e[2*i+1]]

draw_tree(0, 0, e[0])