# 회문찾기_이중배열
# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 펠린드롬은 한 리스트(행) 혹은 문자열 내에서 검사를 시행해야 한다.
# 가로, 세로에서 각각 펠린드롬을 찾아야 하므로 세로에서 찾을 때는 행, 열을 전환한 상태에서 행마다 펠린드롬을 찾는 작업이 필요하다.
# # 전치행렬 만들기
# def transpose(arr, N):
#     arr_trans = [list(arr[i]) for i in range(N)]
#     for i in range(N):
#         for j in range(N):
#             arr_trans[j][i] = arr[i][j]
#
#     return arr_trans
#
#
# # 펠린드롬 검사하기
# def pelindrome(arr, i, N, M):
#     result = ''
#     for j in range(N-M+1):
#         for k in range(M//2):
#             if arr[i][j+k] != arr[i][j+M-1-k]:
#                 break
#         else:
#             result = ''.join(arr[i][j:j + M])
#
#     return result
#
#
# T = int(input())
# for t in range(1, T+1):
#     # N = arr의 길이 M = 펠린드롬의 길이
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     arr_trans = transpose(arr, N)
#     ans = ''
#     while not len(ans):
#         for i in range(N):
#             ans = pelindrome(arr, i, N, M) + pelindrome(arr_trans, i, N, M)
#             if ans:
#                 break
#
#     print('#%d %s' %(t, ans))


# zip을 사용하면 열을 각각의 리스트로 받아올 수 있다! (**중요**)
# 이중배열 arr에 대해 list(zip(*arr))를 하면 전치 행렬이 된다.
# 팰린드롬 검사하기
def palindrome(row, N, M):
    result = ''
    for j in range(N-M+1):
        for k in range(M//2):
            if row[j+k] != row[j+M-1-k]:
                break
        else:
            result = ''.join(row[j:j + M])

    return result


T = int(input())
for t in range(1, T+1):
    # N = arr의 길이 M = 팰린드롬의 길이
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ''
    while not len(ans):
        for i in range(N):
            ans = palindrome(arr[i], N, M) + palindrome(list(zip(*arr))[i], N, M)
            if ans:
                break

    print('#%d %s' %(t, ans))
