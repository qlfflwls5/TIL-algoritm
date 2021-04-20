# 소인수분해
# 숫자 N은 아래와 같다.
# N=2^a x 3^b x 5^c x 7^d x 11^e
# N이 주어질 때 a, b, c, d, e 를 출력하라.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.
#
#
# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 주어진 소수의 리스트를 만들어놓고, 리스트를 순회하며 소수를 하나씩 빼와 입력받은 수를 해당 소수로 나머지가 0이 아닐 때까지 나누면 된다.
# 횟수를 세기 위하여 카운트 리스트를 생성해 진행한다.
T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = [2, 3, 5, 7, 11]
    result_list = [0] * 5
    i = 0
    for num in num_list:
        while N % num == 0:
            result_list[i] += 1
            N //= num
        i += 1

    for i in range(len(result_list)):
        result_list[i] = str(result_list[i])
    ans = ' '.join(result_list)
    print('#%d %s' %(t, ans))