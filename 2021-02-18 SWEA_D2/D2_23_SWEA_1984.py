# 중간 평균값 구하기
# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)


# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


T = int(input())
for t in range(1, T+1):
    num_list = list(map(int, input().split()))
    # 최소값의 인덱스와 최대값의 인덱스를 찾아 최소값과 최대값을 0번째, 1번째로 보내 버릴 것 (셀렉션)
    min_i, max_i = 0, 0
    for i in range(1, len(num_list)):
        if num_list[min_i] > num_list[i]:
            min_i = i
        if num_list[max_i] < num_list[i]:
            max_i = i
    num_list[0], num_list[max_i] = num_list[max_i], num_list[0]
    num_list[1], num_list[min_i] = num_list[min_i], num_list[1]

    cnt, total = 0, 0
    for i in range(2, len(num_list)):
        cnt += 1
        total += num_list[i]

    result = total/cnt
    # result에서 int(result)를 빼면 소수부만 남는다. 이를 활용해 반올림을 구현한다.
    if result - int(result) >= 0.5:
        result = int(result) + 1
    else:
        result = int(result)

    print('#%d %d' %(t, result))

