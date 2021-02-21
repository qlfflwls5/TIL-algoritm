# 파리 퇴치
# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
# 죽은 파리의 개수를 구하라!


# [제약 사항]
# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 다음 N 줄에 걸쳐 N x N 배열이 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


import sys

sys.stdin = open("파리퇴치_input.txt")

# 각 위치에 대하여 파리채가 몇 마리의 파리를 잡을 수 있는지를 리턴하는 함수
def fly_sum(arr, M, r, c):
    total = 0
    for i in range(r, r+M):
        for j in range(c, c+M):
            total += arr[i][j]
    return total


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 파리채의 시작점이 위치할 수 있는 모든 곳을 순회하며 함수 실행
    for r in range(N-M+1):
        for c in range(N-M+1):
            # 최대값의 초기값은 r == 0, c == 0일 때
            if r == 0 and c == 0:
                max_sum = fly_sum(arr, M, r, c)
            else:
                if max_sum < fly_sum(arr, M, r, c):
                    max_sum = fly_sum(arr, M, r, c)
    print('#%d %d' %(t, max_sum))