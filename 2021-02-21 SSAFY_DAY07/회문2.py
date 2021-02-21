# 회문 2
# "기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.


# [제약사항]
# 각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
# 글자 판은 무조건 정사각형으로 주어진다.
# ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
# 가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.


# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트케이스가 주어진다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.


import sys


def max_palindrome(string):
    N = len(string)
    max_len = 0
    # 처음은 회문을 검사할 필요가 없다. 이후 i와 i-1을 묶어 회문의 중심으로 볼 것이기 때문이다. 중심이 하나일 경우에도 할 필요가 없다.
    for i in range(1, N):
        # 중심 문자가 양끝에 닿아 끝난 것인지와 짝수 길이인지를 판별해야 한다. (양끝에 닿아 끝난 것이면 양옆으로 뻗어나가면서 회문을 찾는 방법으로 끝나는 것이 아니므로)
        # 양끝에 닿아서 강제로 끝난 것이면 is_end가 1이된다.
        is_end = 0
        # string[i] == string[i-1]의 경우 짝수일 수도 있고, 홀수일 수도 있다.
        # 짝수 길이의 회문인지 홀수 길이의 회문인지 알기 위해서는 '중심'에 있는 연속되는 같은 문자들이 짝수개인지 홀수개인지 알아야한다.
        # 아래 if문은 '중심 문자'가 몇 번 반복되는지를 확인하는 부분이다.
        # 중심 문자가 2번 이상 반복될 때
        if string[i] == string[i - 1]:
            # 중심 문자
            center = string[i]
            # 중심 문자의 현재 인덱스에서 양옆으로 퍼져 나갈 것이다. 초기 중심 문자의 길이는 1이다.
            temp_i, temp_j = i, i
            temp_len = 1
            # 양끝 중에 도달할 수도 있으니 그때까지
            while 0 < temp_i and temp_j < N - 1:
                # 초기 중심문자 2개를 기준으로 양옆으로 뻗어나가기
                temp_i -= 1
                temp_j += 1
                # 양옆 중에 하나라도 중심 문자와 다를 경우 중단(ex) 중심문자가 'B'인데 'ABBB'와 같이 양옆 중 하나가 중심문자와 다르다면 중단)
                if string[temp_i] != center or string[temp_j] != center:
                    break
                # 양옆이 같다면 중심 문자의 길이를 2 늘린다.
                temp_len += 2
            # break문에 걸리지 않고 양끝 중에 도달하여 반복문이 종료한 경우
            else:
                is_end = 1
                # 오른쪽 끝에 닿으면서 길이가 짝수
                if temp_j == N - 1 and string[temp_i - 1] == center:
                    temp_len += 1
                    temp_i -= 1
                    # 오른쪽 끝에 닿으면서 길이가 홀수는 처리가 필요가 없다.
                # 왼쪽 끝에 닿으면서 길이가 짝수
                elif temp_i == 0 and string[temp_j] != center:
                    temp_len -= 1
                    temp_j -= 1
                    # 왼쪽 끝에 닿으면서 길이가 홀수는 처리가 필요가 없다.
            
            # break문을 통하여 양옆 중 하나라도 중심 문자와 달라 끝난 경우        
            if not is_end:
                # 짝수 팰린드롬
                if string[temp_i] == center:
                    temp_len += 1
                    temp_j -= 1
                # 홀수 팰린드롬
                else:
                    temp_i += 1
                    temp_j -= 1
        # 중심 문자가 단 한 개일 때
        else:
            temp_len, temp_i, temp_j = 1, i, i

        # 여기서부터 중심 문자로부터 양옆으로 뻗어져 나간다.
        # 중심 문자의 양끝 인덱스를 가져온다.
        i = temp_i
        j = temp_j
        # 전체의 양끝 중에 하나에 도달할 때까지
        while 0 < i and j < N - 1:
            # i와 j를 1씩 줄이면 현재 회문에서 양옆의 값의 인덱스가 된다.
            i -= 1
            j += 1
            # 양옆의 값이 다르다면 반복을 중단, 같다면 회문의 길이를 2 늘린다.
            if string[i] != string[j]:
                break
            temp_len += 2

        if max_len < temp_len:
            max_len = temp_len

    return max_len


sys.stdin = open('palidrome2_input.txt')
for t in range(1, 11):
    n = int(input())
    arr_row = [input() for _ in range(100)]
    max_result = 0
    # 행 기준 이중배열과 열 기준 이중배열을 한 번씩 가져와서
    for arr in arr_row, zip(*arr_row):
        # 각 이중배열의 문자열을 하나씩 가져와서 회문 검사
        for string in arr:
            temp_result = max_palindrome(string)
            if max_result < temp_result:
                max_result = temp_result

    print('#%d %d' %(t, max_result))


# 2
# 일반적인 회문 풀이
# 길이를 모르므로 모든 길이에 대하여 회문 검사를 한다. 완전 탐색
def my_find(M):
    # 전체크기가 N이다.
    for i in range(N):
        for j in range(N - M + 1):
            # 스왑 통한 회문 검사
            # 가로 검사
            for k in range(M // 2):
                # 앞뒤검사
                if words[i][j + k] != words[i][j + M - 1 - k]:
                    break
                # 회문임
                elif k == M // 2 - 1:
                    return M
            # 세로 검사
            for k in range(M // 2):
                if words[j + k][i] != words[j + M - 1 - k][i]:
                    break
                elif k == M // 2 - 1:
                    return M
    return 0


for _ in range(10):
    tc_num = int(input())

    N = 100
    words = [input() for i in range(N)]

    # 가장 길이가 긴 회문부터 검사를 한다.
    for i in range(N, 0, -1):
        ans = my_find(i)

        if ans:
            break

    print('#{} {}'.format(tc_num, ans))
