# 이진수 표현
# 정수 N, M 이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 각 테스트 케이스는 다음과 같이 구성되었다.
# 첫 번째 줄에 정수 N, M이 주어진다. (1 ≤ N ≤ 30 , 0 ≤ M ≤ 108)


# [출력]
# 각 테스트 케이스마다 한 줄씩
# 마지막 N개의 비트가 모두 켜져 있다면 ON
# 아니면 OFF 를 출력하라.


for t in range(1, int(input())+1):
    N, M = map(int, input().split())

    for _ in range(N):
        if not M % 2:
            result = 'OFF'
            break
        M //= 2
    else:
        result = 'ON'

    print('#%d %s' % (t, result))
