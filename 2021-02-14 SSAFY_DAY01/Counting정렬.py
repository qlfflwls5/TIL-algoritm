T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num_list = list(input().split())
    sort_list = list(num_list)

    max_num = int(num_list[0][0])
    for num in num_list:
        if int(num[0]) > max_num:
            max_num = int(num[0])

    count_list = [0] * (max_num + 1)

    for i in range(len(num_list)):
        count_list[int(num_list[i][0])] += 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]

    for i in range(len(sort_list) - 1, -1, -1):
        sort_list[count_list[int(num_list[i][0])] - 1] = num_list[i]
        count_list[int(num_list[i][0])] -= 1

    ans = ' '.join(sort_list)
    print('#%d %s' %(t, ans))