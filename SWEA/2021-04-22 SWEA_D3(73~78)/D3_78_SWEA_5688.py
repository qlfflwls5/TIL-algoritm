# 세제곱근을 찾아라
# 양의 정수 N에 대해 N = X^3가 되는 양의 정수X 를 구하여라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤10^18) 이 주어진다.


# [출력]
# 각 테스트 케이스마다 첫 번째 줄에는‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다.)를 출력하고, N = X^3가 되는 양의 정수 X를 출력한다.
# 만약 이런 X가 존재하지 않으면 -1을 출력한다.


def binary_search(N):
    if N == 1:
        return 1
    l = 0
    r = int(N**1/2)
    while l <= r:
        mid = (l + r) // 2
        M = mid**3
        if M == N:
            return mid
        elif M > N:
            r = mid - 1
        else:
            l = mid + 1

    return -1


for t in range(1, int(input())+1):
    N = int(input())
    print('#%d %d' % (t, binary_search(N)))
