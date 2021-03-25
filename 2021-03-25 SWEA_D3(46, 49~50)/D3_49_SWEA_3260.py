# 두 수의 덧셈
# 덧셈을 배운지 얼마 안 된 준환이는 덧셈에 아직도 어려움을 느낀다.
# 그래서 준환이는 N자리인 두 양수를 더하는 연습을 하기로 했다.
# 당신은 준환이를 위해 답안지를 만들어 주기로 했다.
# 두 양수가 주어질 때 두 수를 더한 결과를 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스마다 첫 번째 줄에 두 양의 정수 A, B(1 ≤ A, B< 10^100)가 공백으로 구분되어 주어진다.
# 두 수는 0으로 시작되지 않는다.


# [출력]
# 각 테스트 케이스마다 A+B값을 출력한다. 첫 번째 자리가 0으로 시작해서는 안 된다.


for t in range(1, int(input())+1):
    N, M = input().split()
    if len(N) > len(M):
        L, S = N, M
    else:
        L, S = M, N
    # 더 작은쪽의 길이
    len_s = len(S)
    # 이전 자리의 덧셈으로 인해 받는 영향. 이전 자리 덧셈이 10을 넘으면 1이 된다.
    add_num = 0
    result = ''
    # 겹치는 길이까지 덧셈
    for i in range(1, len_s+1):
        temp_sum = int(L[-i]) + int(S[-i]) + add_num
        if temp_sum < 10:
            result = str(temp_sum) + result
            add_num = 0
        else:
            result = str(temp_sum - 10) + result
            add_num = 1
    # 이후 긴 숫자에서 남은 쪽을 계산
    for i in range(len_s+1, len(L)+1):
        temp_sum = int(L[-i]) + add_num
        if temp_sum < 10:
            result = str(temp_sum) + result
            add_num = 0
        else:
            result = str(temp_sum - 10) + result
            add_num = 1
    # 마지막으로 가장 큰 자릿수가 덧셈으로 인해 10을 넘는지를 확인
    if add_num:
        result = '1' + result

    print('#%d %s' % (t, result))

# 그냥 덧셈해도 되더라...