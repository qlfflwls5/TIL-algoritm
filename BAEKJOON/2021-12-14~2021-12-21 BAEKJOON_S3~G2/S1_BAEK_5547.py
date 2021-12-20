# 일루미네이션
# 부유한 집안의 상속자 상근이네 집은 그림과 같이 1미터의 정육각형이 붙어있는 상태이다.
# 크리스마스가 다가오기 때문에, 여자친구에게 잘 보이기 위해 상근이는 건물의 벽면을 조명으로 장식하려고 한다.
# 외부에 보이지 않는 부분에 조명을 장식하는 것은 낭비라고 생각했기 때문에, 밖에서 보이는 부분만 장식하려고 한다.
# 위의 그림은 상공에서 본 상근이네 집의 건물 배치이다.
# 정육각형 안의 숫자는 좌표를 나타낸다. 여기서 회색 정육각형은 건물의 위치이고, 흰색은 건물이 없는 곳이다.
# 위에서 붉은 색 선으로 표시된 부분이 밖에서 보이는 벽이고, 이 벽에 조명을 장식할 것이다. 벽의 총 길이는 64미터이다.
# 상근이네 집의 건물 위치 지도가 주어졌을 때, 조명을 장식할 벽면의 길이의 합을 구하는 프로그램을 작성하시오.
# 지도의 바깥은 자유롭게 왕래 할 수 있는 곳이고, 인접한 건물 사이는 통과할 수 없다.


# 입력
# 첫째 줄에 두 개의 정수 W와 H가 주어진다. (1 ≤ W, H ≤ 100) 다음 H줄에는 상근이네 집의 건물 배치가 주어진다.
# i+1줄에는 W개의 정수가 공백으로 구분되어 있다. j번째 (1 ≤ j ≤ w) 정수의 좌표는 (j, i)이며, 건물이 있을 때는 1이고, 없을 때는 0이다.
# 주어지는 입력에는 건물이 적어도 하나 있다.
# 지도는 다음과 같은 규칙에 의해 만들어졌다.
# 지도의 가장 왼쪽 위에 있는 정육각형의 좌표는 (1,1)이다.
# (x,y)의 오른족에 있는 정육각형의 좌표는 (x+1,y)이다.
# y가 홀수 일 때, 아래쪽에 있는 정육각형의 좌표는 (x,y+1)이다.
# y가 짝수 일 때, 오른쪽 아래에 있는 정육각형의 좌표는 (x,y+1)이다.


# 출력
# 조명을 장식하는 벽면의 길이의 합을 출력한다.


# 예제 입력 1
# 8 4
# 0 1 0 1 0 1 1 1
# 0 1 1 0 0 1 0 0
# 1 0 1 0 1 1 1 1
# 0 1 1 0 1 0 1 0
# 예제 출력 1
# 64

# 예제 입력 2
# 8 5
# 0 1 1 1 0 1 1 1
# 0 1 0 0 1 1 0 0
# 1 0 0 1 1 1 1 1
# 0 1 0 1 1 0 1 0
# 0 1 1 0 1 1 0 0
# 예제 출력 2
# 56


# 갈 수 없는 길을 찾으면 될 듯 -> 주위 6방향으로 쭉 나갔을 때 모두 끝까지 못가고 건물에 막히는 경우
# 건물의 6방향 주위 인접 1칸이 갈 수 없는 길이거나 건물이면 벽을 세울 수 없음
y_even_drc = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]
y_odd_drc = [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
unable_road = set()
visited = [[0]*W for _ in range(H)]
for r in range(H):
    for c in range(W):
        if not arr[r][c] and not visited[r][c]:
            stack = [(r, c)]
            candidate = [(r, c)]
            visited[r][c] = 1
            flag = 0
            while stack:
                vr, vc = stack.pop()
                for dr, dc in y_even_drc if vr % 2 == 0 else y_odd_drc:
                    nr, nc = vr + dr, vc + dc
                    if 0 <= nr < H and 0 <= nc < W and not arr[nr][nc] and not visited[nr][nc]:
                        stack.append((nr, nc))
                        candidate.append((nr, nc))
                        visited[nr][nc] = 1
                    if not (0 <= nr < H and 0 <= nc < W):
                        flag = 1

            if not flag:
                for i, j in candidate:
                    unable_road.add((i, j))

wall = 0
for r in range(H):
    for c in range(W):
        if arr[r][c]:
            for dr, dc in y_odd_drc if r % 2 != 0 else y_even_drc:
                nr, nc = r + dr, c + dc
                if (0 <= nr < H and 0 <= nc < W and not arr[nr][nc] and (nr, nc) not in unable_road) or not (0 <= nr < H and 0 <= nc < W):
                    wall += 1

print(wall)