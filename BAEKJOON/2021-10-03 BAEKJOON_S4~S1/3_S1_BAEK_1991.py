# 트리 순회

# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 예를 들어 위와 같은 이진 트리가 입력되면,
#
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.


# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.


# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
def order(node):
    if node == '.':
        return

    pre_way.append(node)
    order(tree[ord(node) - 65][1])
    in_way.append(node)
    order(tree[ord(node) - 65][2])
    post_way.append(node)


N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N):
    p, cl, cr = input().split()
    tree[ord(p) - 65].extend([p, cl, cr])

pre_way, in_way, post_way = [], [], []
order('A')
print('\n'.join([''.join(pre_way), ''.join(in_way), ''.join(post_way)]))


