# Sum
# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

# [제약 사항]
# 총 10개의 테스트 케이스가 주어진다.
# 배열의 크기는 100X100으로 동일하다.
# 각 행의 합은 integer 범위를 넘어가지 않는다.
# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.


# [입력]
# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.


import sys

sys.stdin = open("hw_sum_input.txt")

#1
for _ in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    diag1, diag2 = 0, 0
    for i in range(100):
        row, col = 0, 0
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
            if i == j:
                diag1 += arr[i][j]
            if i == 99-j:
                diag2 += arr[i][j]
        if i == 0:
            max_row = row
            max_col = col
        else:
            if max_row < row:
                max_row = row
            if max_col < col:
                max_col = col
    max_list = [max_row, max_col, diag1, diag2]
    result = max_list[0]
    for i in range(1, len(max_list)):
        if result < max_list[i]:
            result = max_list[i]
    print('#%d %d' %(t, result))


# 2
# 이게 더 효율적이고 좋은 것 같다.
for _ in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    diag1, diag2 = 0, 0
    result_list = []
    for i in range(100):
        row, col = 0, 0
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
            if i == j:
                diag1 += arr[i][j]
            if i == 99 - j:
                diag2 += arr[i][j]
        result_list += [row]
        result_list += [col]
    result_list += [diag1]
    result_list += [diag2]
    result = result_list[0]
    for i in range(1, len(result_list)):
        if result < result_list[i]:
            result = result_list[i]
    print('#%d %d' % (t, result))


