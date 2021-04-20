# 이진탐색
# 1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
# 이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
# 추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.
# 다음은 1부터 6까지의 숫자를 완전 이진 트리 형태인 이진 탐색 트리에 저장한 경우이다.
# 완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.
# N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 N이 주어진다. 1<=N<=1000


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 중위순회의 차례대로 1씩 증가하는 값을 집어넣으면 된다.
def inorder(node):
    if node:
        inorder(tree[node][0])
        global cnt
        tree[node][2] = cnt
        cnt += 1
        inorder(tree[node][1])


for t in range(1, int(input())+1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)] # 왼쪽 자식, 오른쪽 자식, 값
    # 완전 이진트리 구성
    for i in range(2, N+1):
        # 2 ~ N까지의 노드에 대해 부모 노드의 자식 노드 정보에 자신을 심는다. 자신이 짝수면 부모의 왼쪽 자식 노드, 홀수면 부모의 오른쪽 자식 노드가 된다.
        tree[i//2][i%2] = i

    cnt = 1
    inorder(1)
    print('#%d %d %d' % (t, tree[1][2], tree[N//2][2]))


# 2
# 깔끔하게
# 완전 이진트리를 다 구성할 필요가 없다. -> 부모와 자식간의 관계가 *2와 *2+1의 관계로 나타낼 수 있기 떄문에
# 모범답안으로 뽑혔다.
def inorder(node):
    if node <= N:
        inorder(node*2)
        global cnt
        tree[node] = cnt
        cnt += 1
        inorder(node*2+1)


for t in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inorder(1)
    print('#%d %d %d' % (t, tree[1], tree[N//2]))


# 3
# 교수님의 내 2번 풀이 최적화
# 테스트케이스가 많을수록 함수호출이 줄기 때문에 효율적이 된다.
# 내 풀이는 내려갔다 올라오는 것이고 이 풀이는 내려가기만 한다.
# 대신 깔끔한 풀이는 내 2번대로 쓰는게 좋다고 한다.
def inorder(node):
    if node*2 <= N:
        inorder(node*2)
    global cnt
    tree[node] = cnt
    cnt += 1
    if node*2+1 <= N:
        inorder(node*2+1)


# 4
# 호근님 풀이
# 아예 입력받을 때마다 왼쪽, 오른쪽, 위쪽으로 움직여가며 값을 넣을 자리를 찾았다.
# 한 번 값을 넣고 나면 다음 시행에서는 이전에 값을 넣었던 자리부터 시작하는 것이다.
def insert(i, n):
    # 왼쪽으로
    if i * 2 <= N and not bst[i * 2]:
        while i * 2 <= N and not bst[i * 2]:
            i = i * 2
        bst[i] = n
        return i

    # 오른쪽으로
    elif i * 2 + 1 <= N and not bst[i * 2 + 1]:
        i = i * 2 + 1
        while i * 2 <= N and not bst[i * 2]:
            i = i * 2
        bst[i] = n
        return i

    # 위로
    else:
        while bst[i]:
            i = i // 2
        bst[i] = n
        return i


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    i = 1
    bst = [0] * (N + 1)
    for n in range(1, N + 1):
        i = insert(i, n)

    print('#%d %d %d' % (test_case, bst[1], bst[N // 2]))

for t in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inorder(1)
    print('#%d %d %d' % (t, tree[1], tree[N//2]))