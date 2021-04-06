# 이진탐색트리 생성
# 이진탐색트리의 생성 연산을 구현하세요!
# 모든 연산 수행 후의 이진탐색트리를 전위운행(preorder) 수행해서 출력합니다.

# 8 <- 초기 생성할 노드 개수
# 9 4 3 6 12 15 13 17  <- 초기 생성할 노드의 값

# * 노드 탐색, 전위운행(preorder)에 대한 함수도 생성합니다.
# 각 기능은 함수로 작성하도록 합니다.

# 생성 후 Tree의 모습


def search(x, root):
    # 루트 노드의 parent는 0으로 한다.
    if x == root:
        return 0
    # 만약 다음 자식에 내가 있다면 지금의 root가 parent다.
    if tree[root][0] == x:
        return root
    if tree[root][1] == x:
        return root
    # 다음 자식이 내가 아니라면 자식으로 내려가 탐색을 반복한다.
    if x < root and tree[root][0]:
        return search(x, tree[root][0])
    if x > root and tree[root][1]:
        return search(x, tree[root][1])
    # 내가 없는 상태, 즉 탐색 실패의 경우 삽입을 한다면 지금의 root가 parent다.
    return root


def preorder(node):
    if node:
        way.append(node)
        preorder(tree[node][0])
        preorder(tree[node][1])


N = int(input())
node_list = list(map(int, input().split()))
V = max(node_list)
# 왼쪽 자식 노드와 오른쪽 자식 노드에 대한 정보를 가짐
tree = [[0, 0] for _ in range(V+1)]
root = node_list[0]
for node in node_list:
    parent = search(node, root)
    if parent > node:
        tree[parent][0] = node
    elif parent < node:
        tree[parent][1] = node

way = []
preorder(root)
print('-'.join(map(str, way)))


# 2
# 교수님 답안
# root라는 dummy를 주어서 실제 루트 노드는 root의 오른쪽 자식으로 삼는다. root의 변경이 없다.
root = [0, 0, 0]  # dummy


def inorder(node):
    if not node:
        return
    inorder(node[1])
    answer.append(str(node[0]))
    inorder(node[2])


def preorder(node):
    if not node:
        return
    answer.append(str(node[0]))
    preorder(node[1])
    preorder(node[2])


def bt_search(x):
    parent = root  # root = [0, 0, 0]
    curr = root  # curr = [0, 0, 0]
    while curr:
        if x == curr[0]:
            break
        parent = curr
        curr = curr[1] if x < curr[0] else curr[2]  # curr = 0
    return parent, curr  # [0, 0, 0], [0,0,0],   [9, 0, 0], 0   일 수 있기 때문에


def bt_insert(x):
    parent, curr = bt_search(x)  # 부모노드, 탐색노드 가져오기
    if type(curr) is list and curr[0] == x:  # 조건 변경
        print('the value %d is already exist' % (x))
        return

    lr_child = 1 if x < parent[0] else 2
    parent[lr_child] = [x, 0, 0]


N = int(input())  # map(int, input().split())
n_node = list(map(int, input().split()))

for value in n_node:
    bt_insert(value)

answer = []
preorder(root[2])
print('-'.join(answer))

