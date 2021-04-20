# 벽돌 깨기
# 구술을 쏘아 벽돌을 깨트리는 게임을 하려고 한다.
# 구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 W x H 배열로 주어진다.
# ( 0 은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미한다. )
# 게임의 규칙은 다음과 같다.

# ① 구슬은 좌, 우로만 움직일 수 있어서 위에서 떨어뜨려 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
# ② 벽돌은 숫자 1 ~ 9 로 표현되며,
#     구술이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.
#     1이면 자기 자신만, 3이면 자기 자신부터 상하좌우 2칸까지 총 9칸을 제거한다.
# ③ 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.
#     즉, 연쇄반응이 일어난다. 만약 3이 적힌 벽돌이 깨지고 상하좌우 2칸 이내에 3이 적힌 벽돌이 또 있다면 그 벽돌의 상하좌우 2칸을 깬다.

# N 개의 구슬을 떨어트려 최대한 많은 벽돌을 제거하려고 한다.
# N, W, H, 그리고 벽돌들의 정보가 주어질 때, 남은 벽돌의 개수를 구하여라.


# [제약 사항]
# 1. 1 ≤ N ≤ 4
# 2. 2 ≤ W ≤ 12
# 3. 2 ≤ H ≤ 15


# [입력]
# 가장 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,
# 그 다음 줄부터 T 개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 N, W, H 가 순서대로 공백을 사이에 두고 주어지고,
# 다음 H 줄에 걸쳐 벽돌들의 정보가 1 줄에 W 개씩 주어진다.


# [출력]
# 출력은 #t 를 찍고 한 칸 띄운 다음 정답을 출력한다.
# (t 는 테스트 케이스의 번호를 의미하며 1 부터 시작한다)
# 모든 구슬을 떨어뜨릴 수 있는 경우를 구현하는 함수
def perm(level):
    # 종료조건
    if level >= N:
        global arr, min_v
        for c in shoot:
            for r in range(H):
                if arr[r][c]:
                    boom(r, c)
                    after()
                    break

        cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    cnt += 1
        min_v = min(min_v, cnt)
        # 복원
        arr = [list(save_arr[row]) for row in range(H)]
        return
    # 중복을 포함하여 val_c개에서 N개를 뽑는 순열(팩토리얼로 계산됨)
    for col in range(W):
        shoot[level] = col
        perm(level + 1)


# 각 구슬에 대해 벽돌이 꺠지는 함수
def boom(r, c):
    now = arr[r][c]
    arr[r][c] = 0
    for i in range(r - now + 1, r + now):
        if 0 <= i < H and arr[i][c] > 0:
            boom(i, c)
    for j in range(c - now + 1, c + now):
        if 0 <= j < W and arr[r][j] > 0:
            boom(r, j)


# 벽돌이 제거된 후 벽돌이 내려와 정리되는 함수
def after():
    # arr의 마지막 행에서부터의 모든 요소에 대해
    for i in range(H - 2, -1, -1):
        for j in range(W):
            # 현재 0이 아니고 아랫줄이 0이라면
            if arr[i][j] and not arr[i + 1][j]:
                r = i
                # 다음 줄이 경계밖이거나 값이 있을 때까지 행을 늘려 내려가고
                while r + 1 < H and not arr[r + 1][j]:
                    r += 1
                # 끝까지 내려간 곳의 값을 현재 값으로 바꾼 후, 현재 값은 0으로 바꾼다.
                arr[r][j], arr[i][j] = arr[i][j], 0


for t in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # 계속 판을 갖고 결과를 보고 복원해야 하므로 원본을 만들어 놓는다.
    save_arr = [list(arr[row]) for row in range(H)]
    min_v = W * H
    shoot = [0] * N
    perm(0)
    if min_v < 0:
        min_v = 0
    print('#%d %d' % (t, min_v))