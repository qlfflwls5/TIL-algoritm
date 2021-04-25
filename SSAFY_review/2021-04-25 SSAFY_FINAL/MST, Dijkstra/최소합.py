# 최소합
# 그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


drc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[2000]*N for _ in range(N)]
    D[0][0] = arr[0][0]
    queue = [(0, 0)]
    front = 0
    while front < len(queue):
        r, c = queue[front]
        front += 1
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                temp = D[r][c] + arr[nr][nc]
                if D[nr][nc] > temp:
                    D[nr][nc] = temp
                    queue.append((nr, nc))

    print('#%d %d' % (t, D[N-1][N-1]))