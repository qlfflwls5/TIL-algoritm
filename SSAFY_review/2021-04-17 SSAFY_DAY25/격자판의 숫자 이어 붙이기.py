# 격자판의 숫자 이어붙이기
# 4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.
# 격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.
# 이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.
# 단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.
# 격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스마다 4개의 줄에 걸쳐서, 각 줄마다 4개의 정수로 격자판의 정보가 주어진다.


# [출력]
# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 격자판을 이동하며 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 출력한다.


# 1
def get_num(level, r, c, S):
    if level == 7:
        num.add(S)
        return

    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            get_num(level+1, nr, nc, S+arr[nr][nc])


drc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for t in range(1, int(input())+1):
    arr = [list(input().split()) for _ in range(4)]
    num = set()
    for i in range(4):
        for j in range(4):
            get_num(0, i, j, '')

    print('#%d %d' % (t, len(num)))


# 2
# 1번과 비슷한 코드인데 실행시간이 1.7~1.8배는 더 빠르다. 이유가 뭘까?
# 1. 1번 코드에서의 arr = [list(input().split()) for _ in range(4)] 에서 list 변환이 필요가 없다. .split()은 어차피 list를 반환한다.
# 2. 치명적인 실수다. 1번 코드에서는 레벨을 0으로 시작하고 S를 ''로 초기값을 줬다.
#    이렇게 했을 때 실제 어떠한 한 위치에서 만드는 길이 7의 숫자는 해당 위치를 포함하지 않은 이웃한 칸부터 시작한 7자리 숫자.
#    즉, 레벨을 1부터 시작하고 S의 초기값을 현재 위치의 숫자로 주는 것이 맞는 풀이다. 이러면 모든 경우에서 depth가 1씩 줄어든다.
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_line(n, r, c, line):
    if n == 7:
        lines.add(line)
        return
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            get_line(n + 1, nr, nc, line + grid[nr][nc])


for t in range(1, int(input()) + 1):
    grid = [input().split() for _ in range(4)]
    lines = set()
    for r in range(4):
        for c in range(4):
            get_line(1, r, c, grid[r][c])

    print('#%d %d' % (t, len(lines)))
    
    
# 3
# 2번에서 깨우친 것에 따라 수정한 1번 코드
# 1번의 실행시간은 540ms였고, 수정한 이 코드는 350ms다.
def get_num(level, r, c, S):
    if level == 7:
        num.add(S)
        return

    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            get_num(level+1, nr, nc, S+arr[nr][nc])


drc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for t in range(1, int(input())+1):
    arr = [input().split() for _ in range(4)]
    num = set()
    for i in range(4):
        for j in range(4):
            get_num(1, i, j, arr[i][j])

    print('#%d %d' % (t, len(num)))