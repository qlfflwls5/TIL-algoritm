# Counting정렬
# 주어진 N 길이의 2글자 문자열(숫자 2개)을 첫 번째 숫자를 기준으로 오름차순으로 정렬하여 출력하라.
# 이때, 발생 순서를 그대로 유지하며 정렬되도록 하시오.


# [제약 사항]
# N 은 5 이상 50 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 2글자 문자열(숫자 2개로 구성)이 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num_list = list(input().split())
    # 카운팅 정렬에서는 복사본이나 정렬할 리스트와 같은 길이를 갖는 임시 리스트가 필요하다.
    sort_list = list(num_list)
    # 카운팅 정렬에서는 카운트 리스트를 만들기 위해 정렬할 리스트에서 가장 큰 숫자를 알아야 한다.
    max_num = int(num_list[0][0])
    for num in num_list:
        if int(num[0]) > max_num:
            max_num = int(num[0])

    # 카운트 리스트는 모든 요소가 0이며 길이는 최대값+1이다. 0을 포함하기 때문에 +1을 한다.
    count_list = [0] * (max_num + 1)
    # 정렬할 리스트를 순회하며 카운트 리스트를 구성한다.
    for i in range(len(num_list)):
        count_list[int(num_list[i][0])] += 1
    # 카운트 리스트를 누적합 해나간다.
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]
    # 미리 준비해뒀던 복사본이나 임시 리스트에 카운트 리스트를 활용하여 정렬한다.
    for i in range(len(sort_list) - 1, -1, -1):
        sort_list[count_list[int(num_list[i][0])] - 1] = num_list[i]
        count_list[int(num_list[i][0])] -= 1

    ans = ' '.join(sort_list)
    print('#%d %s' %(t, ans))