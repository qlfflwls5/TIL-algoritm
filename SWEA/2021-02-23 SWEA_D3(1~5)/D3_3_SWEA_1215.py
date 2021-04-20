# 회문1
# 주어진 8x8 평면 글자판에서 가로, 세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 문제이다.
# 위와 같은 글자판이 주어졌을 때, 길이가 5인 회문은 붉은색 테두리로 표시된 4개가 있으며 따라서 4를 반환하면 된다.


# [제약 사항]
# 각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
# 글자 판은 무조건 정사각형으로 주어진다.
# ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
# 가로, 세로 각각에 대해서 직선으로만 판단한다.
# 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.


# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트 케이스가 주어진다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.


import sys


sys.stdin = open('1215_input.txt')
# for t in range(1, 11):
#     N, M = 8, int(input())
#     arr = [input() for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         for j in range(N-M+1):
#             r_flag, c_flag = 1, 1
#             for k in range(M//2):
#                 if arr[i][j+k] != arr[i][j+M-1-k]:
#                     r_flag = 0
#                     # break 넣으려했는데, 안된다.
#                 if arr[j+k][i] != arr[j+M-1-k][i]:
#                     c_flag = 0
#                     # break 넣으려했는데, 안된다.
#                     # 안전하게 가로 세로 따로 검사하자... break를 못한다면 필요없는 검사까지 하게 되어 비효율적이다.
#
#             cnt += r_flag + c_flag
#
#     print('#%d %d' %(t, cnt))


# 2
# 제대로 푸는 법
# 한 행에 대해 길이가 M인 팰린드롬의 개수를 찾는 함수
def palindrome(string):
    cnt = 0
    for i in range(N-M+1):
        for j in range(M//2):
            if string[i+j] != string[i+M-1-j]:
                break
        else:
            cnt += 1

    return cnt


for t in range(1, 11):
    N, M = 8, int(input())
    arr = [input() for _ in range(N)]
    cnt = 0
    for i in range(N):
        # 가로 검사와 세로 검사를 차례로 하겠다. zip(*arr)을 통해 행열을 전환한다.
        for temp_arr in arr, zip(*arr):
            # 다만 zip(*arr)에서 가져오는 string은 사실 type이 tuple이다.
            for string in temp_arr:
                cnt += palindrome(string)

    print('#%d %d' %(t, cnt))