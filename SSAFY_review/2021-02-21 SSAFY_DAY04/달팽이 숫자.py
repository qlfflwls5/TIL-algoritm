# 달팽이 숫자
# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


# [제약사항]
# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.


# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 1
# 규칙과 델타검색을 통한 풀이
# 4*4 배열
# 4 -> 3 -> 3-> 2 -> 2- > 1-> 1
# 5*5 배열
# 5 -> 4 -> 4 -> 3 -> 3 -> 2 -> 2 -> 1 -> 1
# 반복 횟수: N*2-1

# 우, 하, 좌, 상
drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    drc_index = 0
    cnt = 1
    # 전체 규칙에 맞추기 위해서는 첫 시작도 델타를 통해 이동해 온 것이어야 한다.
    # 모든 시작은 전부 우측으로 이동하므로 첫 열을 -1로 설정해 처음 시행에서 0이되게 한다.
    r, c = 0, -1
    for i in range(N*2-1):
        # i마다 drc[drc_index % 4]의 쪽으로 N-((i+1)//2) 만큼 간다. i마다 drc_index는 1씩 올라야 한다.
        # 1칸 움직일 때마다 cnt는 1씩 오른다. r이나 c도 drc_index에 따라 1만큼 변화한다.
        for j in range(N-((i+1)//2)):
            r += drc[drc_index%4][0]
            c += drc[drc_index%4][1]
            arr[r][c] = cnt
            cnt += 1
        drc_index += 1
    print('#%d' % t)
    for i in range(N):
        print(*arr[i])


# 2
# 자기 자신의 위치에서의 풀이
# 좌, 상이 0이 아니고 우가 0이라면 우로
# 상, 우가 0이 아니고 하가 0이라면 하로
# 우, 하가 0이 아니고 좌가 0이라면 좌로
# 하, 좌가 0이 아니고 상이 0이라면 상으로
T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 주위를 1로 둘러싼 N*N arr만들기. 규칙을 테두리에도 적용하기 위해서
    arr = [[1]*(N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] = 0
    r, c = 1, 0
    for i in range(1, N**2+1):
        up, down, left, right = arr[r-1][c], arr[r+1][c], arr[r][c-1], arr[r][c+1]
        if left != 0 and up != 0 and right == 0:
            c += 1
            arr[r][c] = i
        elif up != 0 and right != 0 and down == 0:
            r += 1
            arr[r][c] = i
        elif right != 0 and down != 0 and left == 0:
            c -= 1
            arr[r][c] = i
        elif down != 0 and left != 0 and up == 0:
            r -= 1
            arr[r][c] = i
    print('#%d' % t)
    # 주위의 1을 제외하고 출력
    for i in range(N):
        print(*arr[i+1][1:-1])


# 3
# sw를 이용하는 방법
# 우 -> 하 -> 좌 -> 상의 규칙을 보면 우 -> 하는 행이나 열이 1씩 증가하고 좌 -> 상은 행이나 열이 1씩 감소하는 것이다.
# 두 번마다 증가/감소가 스왑한다.
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    r, c = 0, -1
    num = 0
    loop = N
    sw = 1
    # 처음만 규칙이 다른 것을 적용하기 위해 for문 두 번 사이에 loop를 감소하는 식을 넣는다. 첫 시행만 loop가 N인 상태에서 실행,
    # 두 번째 시행부터는 동일한 loop에서 두 번 실행된다. 마지막 loop가 0일 때는 어차피 for문이 실행이 안되므로 알아서 처리된다.
    while loop > 0:
        for x in range(loop):
            c += sw
            num += 1
            arr[r][c] = num

        loop -= 1
        for x in range(loop):
            r += sw
            num += 1
            arr[r][c] = num
        sw = -sw

    for x in arr:

        print(x)



