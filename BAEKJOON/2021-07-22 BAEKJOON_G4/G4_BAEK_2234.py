# 성곽
# 대략 위의 그림과 같이 생긴 성곽이 있다. 굵은 선은 벽을 나타내고, 점선은 벽이 없어서 지나다닐 수 있는 통로를 나타낸다.
# 이러한 형태의 성의 지도를 입력받아서 다음을 계산하는 프로그램을 작성하시오.

# 이 성에 있는 방의 개수
# 가장 넓은 방의 넓이
# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
# 위의 예에서는 방은 5개고, 가장 큰 방은 9개의 칸으로 이루어져 있으며, 위의 그림에서 화살표가 가리키는 벽을 제거하면 16인 크기의 방을 얻을 수 있다.
#
# 성은 m×n(1 ≤ m, n ≤ 50)개의 정사각형 칸으로 이루어진다. 성에는 최소 두 개의 방이 있어서, 항상 하나의 벽을 제거하여 두 방을 합치는 경우가 있다.


# 입력
# 첫째 줄에 두 정수 n, m이 주어진다. 다음 m개의 줄에는 n개의 정수로 벽에 대한 정보가 주어진다.
# 벽에 대한 정보는 한 정수로 주어지는데, 서쪽에 벽이 있을 때는 1을, 북쪽에 벽이 있을 때는 2를, 동쪽에 벽이 있을 때는 4를,
# 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다. 참고로 이진수의 각 비트를 생각하면 쉽다. 따라서 이 값은 0부터 15까지의 범위 안에 있다.


# 출력
# 첫째 줄에 1의 답을, 둘째 줄에 2의 답을, 셋째 줄에 3의 답을 출력한다.


# 실제로 벽을 뚫는 것을 구현하는 것은 어렵다. 벽을 뚫어서 갈 수 있다는 것은 두 방이 인접해있다는 뜻.
# 즉, 인접한 방의 크기의 합을 구하는 방법으로 푼다.
# 이를 위해 visited 배열을 각 방의 고유 번호로 채울 것이다. 그리고 visited 배열에서 인접한 칸의 번호가 다르면 두 방이 인접한 것이다.
# {각 방의 고유 번호 : 각 방의 크기}의 구조를 갖는 딕셔너리를 만든다.
def dfs(i, j):
    stack = [(i, j)]
    # visited를 방의 고유한 숫자로 채울 것이다.
    visited[i][j] = i*n + j + 1
    # 방의 크기를 선언
    cnt = 1
    while stack:
        r, c = stack.pop()
        # 남동북서 방향으로 순회를 위해 for문 선언
        for k in range(4):
            # bin과 zfill을 이용해 뚫려있는 벽 찾기
            # if bin(arr[r][c])[2:].zfill(4)[k] == '0':
            # 비트 연산을 이용해 뚫려있는 벽 찾기
            if arr[r][c] & (1 << 3 - k) == 0:
                nr, nc = r + drc[k][0], c + drc[k][1]
                if not visited[nr][nc]:
                    stack.append((nr, nc))
                    # 방문 표시를 하면서, 고유한 숫자를 넣어준다.
                    visited[nr][nc] = i*n + j + 1
                    cnt += 1

    return cnt


# 남, 동, 북, 서로 역순으로 찾을 것
drc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(m)]
# 키 값은 각 방의 고유한 숫자, value 값은 방의 크기를 가질 딕셔너리 선언
room_dict = dict()
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            # {방의 고유한 숫자 : 방의 크기}
            room_dict[i*n + j + 1] = (dfs(i, j))

# visited 배열에서 인접한 두 칸의 고유 숫자가 다르면 다른 방인 것. room_dict를 이용해 각 방의 크기를 더해 이어질 수 있는 최대 크기를 구한다.
max_two_room = 0
for i in range(m):
    for j in range(n):
        for dr, dc in drc:
            nr, nc = i + dr, j + dc
            if 0 <= nr < m and 0 <= nc < n and visited[i][j] != visited[nr][nc]:
                max_two_room = max(room_dict[visited[i][j]] + room_dict[visited[nr][nc]], max_two_room)

print("%d\n%d\n%d" % (len(room_dict), max(room_dict.values()), max_two_room))