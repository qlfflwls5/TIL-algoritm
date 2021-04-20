import sys


def center_palindrome(string, N, i):
    is_end = 0
    if string[i] == string[i - 1]:
        center = string[i]
        temp_i, temp_j = i, i
        temp_len = 1
        while 0 < temp_i and temp_j < N - 1:
            temp_i -= 1
            temp_j += 1
            if string[temp_i] != center or string[temp_j] != center:
                break
            temp_len += 2
        else:
            is_end = 1
            if temp_j == N - 1 and string[temp_i - 1] == center:
                temp_len += 1
                temp_i -= 1
            elif temp_i == 0 and string[temp_j] != center:
                temp_len -= 1
                temp_j -= 1

        if not is_end:
            if string[temp_i] == center:
                temp_len += 1
                temp_j -= 1
            else:
                temp_i += 1
                temp_j -= 1
    else:
        temp_len, temp_i, temp_j = 1, i, i

        return temp_len, temp_i, temp_j


def max_palindrome(string):
    N = len(string)
    max_len = 0
    for i in range(1, N - 1):
        temp_len, temp_i, temp_j = center_palindrome(string, N, i)

        i = temp_i
        j = temp_j
        while 0 < i and j < N - 1:
            i -= 1
            j += 1
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
    for arr in arr_row, zip(*arr_row):
        for string in arr:
            temp_result = max_palindrome(string)
            if max_result < temp_result:
                max_result = temp_result

    print('#%d %d' % (t, max_result))