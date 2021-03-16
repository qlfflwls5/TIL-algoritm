# 물놀이를 가자
# 여름이 되어 물놀이를 가는 사람들이 많다.
# 지도는 N×M크기의 격자로 표현이 가능하고, 위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이면 ‘W’, 땅이면 ‘L’로 표현된다.
# 어떤 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복하여 다른 칸으로 이동할 수 있다. 단, 격자 밖으로 나가는 이동은 불가능하다.
# 땅으로 표현된 모든 칸에 대해서, 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 모든 이동 횟수의 합을 출력하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 이 공백 하나로 구분되어 주어진다.
# 다음 개의 줄에는 길이 인 문자열이 주어진다. 문자열은 ‘W’또는 ‘L’로만 이루어져 있다. 모든 줄의 문자열을 모두 합쳤을 때, 적어도 하나의 ‘W’는 주어지는 것이 보장된다.


# [출력]
# 각 테스트 케이스마다 땅으로 표현된 모든 칸에 대해서, 물인 칸으로 이동하기 위한 최소 이동 횟수의 합을 출력한다


# 모든 W로부터 시작해 BFS를 진행한다. 그러면 각 W로부터 가장 가까이 있는 L에 방문 체크가될 것이고, 방문체크한 땅은 앞으로 방문하지 않을 것이므로
# 자동적으로 먼 W에서 도달한 L은 제외 처리가 된다.
# 이를 구현하려면 BFS를 시작할 때 queue의 초기값에 모든 W의 좌표를 넣으면 된다.
drc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = []
    visited = [[0] * M for _ in range(N)]
    queue = [0] * (N * M)
    front, rear = -1, -1
    for r in range(N):
        arr.append(input())
        for c in range(M):
            if arr[r][c] == 'W':
                rear += 1
                queue[rear] = (r, c)

    cnt = 0
    while front < rear:
        front += 1
        r, c = queue[front]
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 'L' and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    cnt += visited[nr][nc]
                    rear += 1
                    queue[rear] = (nr, nc)

    print('#%d %d' % (t, cnt))

# 여기서는 주어지는 입력량이 너무 커서 에러가 발생한다. 어떻게 입력을 가장 효율적으로 처리할 수 있을지의 싸움이다.
# 주어진 입력(str)을 list로 바꾸는 과정에서 굉장히 큰 시간 소모가 일어난다.
# from collections import deque를 한 후, queue = deque()로 생성하고, queue.popleft()를 사용하면 시간이 많이 단축된다.