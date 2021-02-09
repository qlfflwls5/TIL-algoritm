# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.


# [제약 사항]
# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
# 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.


# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys

sys.stdin = open("1979_input.txt")

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    # 리스트 내포를 통해서 이중배열 만들기
    puzzle = [list(map(int, input().split())) for i in range(N)]
 
    result = 0
    for i in range(N):
        # 행에서의 1의 개수를 세는 변수, 한 줄 끝나면 0으로 초기화
        row_count = 0
        # 열에서의 1의 개수를 세는 변수, 한 줄 끝나면 0으로 초기화
        col_count = 0
        for j in range(N):
            # 1이 나올 때마다 count를 누적시키고 0이 나오면 0으로 초기화
            row_count = row_count * puzzle[i][j] + puzzle[i][j]
            col_count = col_count * puzzle[j][i] + puzzle[j][i]
            # 1이 세 번 쌓였을 경우
            if row_count == K:
                # 다음 인덱스가 없는 경우(지금이 줄의 마지막인 경우)와 다음 인덱스가 0인 경우에만 result에 1을 더한다.
                # 다음 인덱스가 있으면서 1인경우에는 1이 3개가 이어진 것이 아니므로 제외해야 하기 때문이다.
                # 행의 입장에서 볼 때는 해당 행의 '다음 열'에 0이 오거나 없어야 하고
                # 열의 입장에서 볼 때는 해당 열의 '다음 행'에 0이 오거나 없어야 한다.
                if j == (N - 1) or puzzle[i][j+1] == 0:
                    result += 1
            if col_count == K:
                if j == (N - 1) or puzzle[j+1][i] == 0:
                    result += 1
 
    print('#%d %d' %(t, result))
        