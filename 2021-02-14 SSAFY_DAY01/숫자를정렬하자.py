import sys

sys.stdin = open("숫자를정렬하자_input.txt")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(len(num_list)-1, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    for i in range(len(num_list)):
        num_list[i] = str(num_list[i])
    ans = ' '.join(num_list)
    print('#%d %s' %(t, ans))