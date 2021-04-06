# 트리의 전위순회
# 첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
# 간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 “부모 자식” 순서로 표기된다.
# 아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
# 간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.
#
# 다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.
# 13 ← 정점의 개수
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13


# 1
# 전위순회
def preorder_travers(node):
    way.append(node)
    if len(tree[node]) >= 3:
        preorder_travers(tree[node][2])
    # way.append(node) 중위순회
    if len(tree[node]) == 4:
        preorder_travers(tree[node][3])
    # way.append(node) 후위순회


V = int(input())
E = list(map(int, input().split()))
# 확장 문제에서의 활용을 위해 tree가 담는 정보는 현재 노드, 부모 노드, 왼쪽 자식 노드, 오른쪽 자식 노드
tree = [[i, 0] for i in range(V+1)]
for i in range(0, len(E), 2):
    # 자식
    tree[E[i]].append(E[i+1])
    # 부모
    tree[E[i+1]][1] = E[i]

root = 0
for i in range(1, V+1):
    if tree[i][1] == 0:
        root = i

way = []
preorder_travers(root)
print('-'.join(map(str, way)))

# 2개씩 건너뛰면서 2개씩 가져오는 방법
# for a, b in zip(E[::2], E[1::2]):


# 2
# 라이브 답안
V, E = map(int, input().split())
edge = list(map(int, input().split()))

left = [0] * (V + 1)  # 부모를 인덱스로 왼쪽 자식 번호 저장
right = [0] * (V + 1)  # 부모를 인덱스로 오른쪽 자식 번호 저장

pa = [0] * (V + 1)  # 자식을 인덱스로 부모번호 저장

for i in range(E):
    n1, n2 = edge[i * 2], edge[i * 2 + 1]  # n1부모, n2자식
    if left[n1] == 0:  # 왼쪽 자식이 없으면
        left[n1] = n2  # 부모를 인덱스로 자식번호 저장
    else:
        right[n1] = n2  # 부모를 인덱스로 자식번호 저장

    pa[n2] = n1  # 자식을 인덱스로 부모를 저장

root = 0
for i in range(1, V + 1):  # 루트 찾기
    if pa[i] == 0:  # 부모가 없으면 root
        root = i
        break


def preorder(n):
    if n > 0:
        print(n, end=' ')
        preorder(left[n])
        preorder(right[n])


preorder(root)