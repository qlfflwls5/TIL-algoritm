# 이진탐색트리 연산연습
# 이진탐색트리의 생성(=삽입), 삭제 연산을 구현하세요!
# 모든 연산 수행 후의 이진탐색트리를 전위운행(preorder) 수행해서 출력합니다.
#
# 8 1 3  <- 초기 생성할 노드 개수, 추가 삽입 노드 개수, 삭제 노드 개수
# 9 4 3 6 12 15 13 17  <- 초기 생성할 노드의 값
# 5 <- 추가 삽입할 노드의 값
# 13 12 9 <- 삭제할 노드의 값
#
# * 노드 탐색, 전위운행(preorder)에 대한 함수도 생성합니다.
# 각 기능은 함수로 작성하도록 합니다.


# 1
# 클래스 미사용
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
        # way.append(node) # 중위순회 이진 탐색트리에서의 중위순회는 정렬된 값을 반환한다.
        preorder(tree[node][1])


def insert(node):
    global root
    parent = search(node, root)
    if parent > node:
        tree[parent][0] = node
    elif parent < node:
        tree[parent][1] = node


def delete(node):
    global root
    parent = search(node, root)
    child = 0
    # 자식이 없는 노드 삭제
    if not tree[node][0] and not tree[node][1]:
        # 부모에서만 삭제할 노드쪽의 노드를 0으로 하면 된다.
        if node < parent:
            tree[parent][0] = 0
        else:
            tree[parent][1] = 0
    # 자식이 하나인 노드 삭제
    elif (tree[node][0] and not tree[node][1]) or (tree[node][1] and not tree[node][0]):
        # 삭제할 노드의 자식이 있는 쪽 노드를 0으로 해줘야 한다.
        if tree[node][0]:
            child = tree[node][0]
            tree[node][0] = 0
        else:
            child = tree[node][1]
            tree[node][1] = 0
        # 부모 노드에 삭제할 노드의 자식 노드를 이어준다.
        if node < parent:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    # 자식이 둘인 노드 삭제
    else:
        # 오른쪽 자식 right의
        right = tree[node][1]
        child = right
        # 가장 왼쪽 자손 child를 가져와서
        while tree[child][0]:
            child = tree[child][0]
        # right랑 child가 같지 않으면 child가 right의 부모가 된다. 같다면 기존에 갖고 있던 오른쪽 자식을 그대로 들고 있게 놔둔다.
        if right != child:
            tree[child][1] = right

        # 삭제되는 노드의 부모에 child를 연결한다.
        if node < parent:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        
        # 삭제되는 노드의 자리를 차지하게 되는 가장 왼쪽 자손노드의 왼쪽 자식을 삭제되는 노드의 왼쪽 자식으로 한다.
        tree[child][0] = tree[node][0]
        # 삭제되는 노드의 자식 정보를 0으로 전부 바꾼다.
        tree[node][0], tree[node][1] = 0, 0
    # 만약 루트 노드의 삭제였다면, 루트를 child로 다시 지정한다.
    if node == root:
        root = child


v, i, d = map(int, input().split())
node_list = list(map(int, input().split()))
insert_list = list(map(int, input().split()))
delete_list = list(map(int, input().split()))
V = max(node_list)
# 왼쪽 자식 노드와 오른쪽 자식 노드에 대한 정보를 가짐
tree = [[0, 0] for _ in range(V+1)]
root = node_list[0]
for node in node_list:
    insert(node)

for insert_node in insert_list:
    insert(insert_node)

for delete_node in delete_list:
    delete(delete_node)

way = []
# search의 과정에서 루트 노드의 부모를 존재하지 않는 0번째 노드로 일단 사용했다. 의미는 없으나 깔끔하게 방문 작업 전에 이를 다시 초기화해준다.
tree[0][0], tree[0][1] = 0, 0
preorder(root)
print(*way)

# root를 외부에 하나의 리스트로 만들어서 전역으로 사용하는 것도 좋다. root = [0, 0, 0, 0] -> 부모, 나, 왼쪽 자식, 오른쪽 자식 과 같이
# 이후 탐색에서 부모가 0이면 root의 1번째를 현재 노드로 하면 된다.


# 2, 3은 교수님의 답안, root라는 더미 리스트 하나 안에서 시작으로 계속 요소가 리스트로 들어온다. tree를 리스트 내포로 쭉 표현
# [[0, 0, [9, [4, [3, 0, 0], [6, 0, 0]], [12, 0, [15, [13, 0, 0], [17, 0, 0]]]]]] 이런 식으로
# 2
# class를 사용한 링크드리스트 구현
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


root = [Node(0, 0, 0)]  # dummy


def inorder(node):
    if not node:
        return
    inorder(node.left)
    answer.append(str(node.value))
    inorder(node.right)


def preorder(node):
    if not node:
        return
    answer.append(str(node.value))
    preorder(node.left)
    preorder(node.right)


def bt_search(x):
    parent = root
    curr = root[0]  # 실제 root_node
    while curr:
        if x == curr.value:
            break
        parent = curr
        curr = curr.left if x < curr.value else curr.right  # 왼쪽 자식 또는 오른쪽 자식으로 이동
    # print(parent, curr)
    return parent, curr


def bt_insert(x):
    parent, curr = bt_search(x)  # 부모노드, 탐색노드 가져오기

    if curr:
        print('the value %d is already exist' % (x))
        return

    child = Node(x, 0, 0)
    if x < parent.value:
        parent.left = child  # 왼쪽 자식으로 등록
    else:
        parent.right = child  # 오른쪽 자식으로 등록


def bt_delete(x):
    # print('delete %d' % (x))
    parent, curr = bt_search(x)  # 부모노드, 삭제할 노드 가져오기
    if not curr:
        print('the value %d is not exist' % (x))
        return

    n_child = bool(curr.left) + bool(curr.right)
    # print('number of child:', n_child)
    if n_child == 0:
        if parent.left == curr:
            parent.left = 0
        else:
            parent.right = 0
    elif n_child == 1:
        child = curr.left if curr.left else curr.right
        if parent.left == curr:
            parent.left = child
        else:
            parent.right = child
    else:
        child = curr.right  # 삭제할 노드의 오른쪽 자식
        while child.left:  # 오른쪽 자식의 가장 왼쪽 자식으로 이동 (leaf 노드)
            child = child.left
        # print('selected child %d, parent %d' % (child.value, curr.value))
        new_value = child.value
        bt_delete(child.value)  # 선택된 자식 노드 삭제
        curr.value = new_value


N, M, K = map(int, input().split())
n_node, i_node, d_node = [list(map(int, input().split())) for _ in range(3)]

for value in n_node + i_node:
    bt_insert(value)

for value in d_node:
    bt_delete(value)

answer = []
preorder(root[0].right)
print(' '.join(answer))


# 3
# 내 코드랑 비슷한 방식인 교수님 답안
root = []  # dummy


def inorder(node):
    if not node:
        return
    inorder(node[2])
    answer.append(str(node[1]))
    inorder(node[3])


def preorder(node):
    if not node:
        return
    answer.append(str(node[1]))
    preorder(node[2])
    preorder(node[3])


def bt_search(x):
    parent = root
    curr = root
    while curr:
        if x == curr[1]:
            break
        parent = curr
        curr = curr[2] if x < curr[1] else curr[3]  # 왼쪽 자식 또는 오른쪽 자식으로 이동
    # print(parent, curr)
    return parent, curr


def bt_insert(x):
    global root
    # print('insert : ', x)
    parent, curr = bt_search(x)  # 부모노드, 탐색노드 가져오기
    if curr:
        print('the value %d is already exist' % (x))
        return

    if not parent:
        root = [0, x, 0, 0]
        return

    child = [parent, x, 0, 0]
    if x < parent[1]:
        parent[2] = child  # 왼쪽 자식으로 등록
    else:
        parent[3] = child  # 오른쪽 자식으로 등록


def bt_delete(x):
    global root
    # print('delete %d' % (x))
    parent, curr = bt_search(x)  # 부모노드, 삭제할 노드 가져오기
    if not curr:
        print('the value %d is not exist' % (x))
        return

    n_child = bool(curr[2]) + bool(curr[3])
    # print('number of child:', n_child)
    if not n_child:
        t_child = 2 if parent[2] == curr else 3  # 왼쪽 자식이면 2, 오른쪽 자식이면 3
        if not parent:  # parent가 없는 경우는 root node인 경우
            root = []
        else:
            parent[t_child] = 0
        return

    if n_child == 1:
        child = curr[2] if curr[2] else curr[3]  # 삭제 노드의 자식입니다.
        lr_child = 2 if parent[2] == curr else 3

        # parent 가 0 인 경우
        if not parent:
            root = child
        else:
            parent[lr_child] = child
        return

    if n_child == 2:
        child = curr[3]  # 삭제할 노드의 오른쪽 자식
        while child[2]:  # 오른쪽 자식의 왼쪽 자식으로 이동 (left 노드 찾기)
            child = child[2]
        # print('delete %d, selected child %d, parent %d' % (child[0][1], child[1], curr[1]))
        new_value = child[1]
        bt_delete(child[1])
        curr[1] = new_value


N, M, K = map(int, input().split())
n_node = list(map(int, input().split()))
i_node = list(map(int, input().split()))
d_node = list(map(int, input().split()))

for value in n_node + i_node:
    bt_insert(value)

for value in d_node:
    bt_delete(value)

answer = []
preorder(root)
print(' '.join(answer))
