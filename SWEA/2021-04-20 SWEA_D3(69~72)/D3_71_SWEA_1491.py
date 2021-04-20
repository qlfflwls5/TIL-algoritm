# 원재의 벽 꾸미기
# 새 집으로 이사를 온 원재는 밋밋한 방을 꾸미기 위해 1 X 1타일 N개를 이용해 R X C 크기의 직사각형 인테리어를 하나 만들어 벽면을 꾸미려고 한다.
# 그런데, 원재의 방은 정사각형 형태이기 때문에 만드는 직사각형 인테리어를 최대한 정사각형에 가깝게 만들면서, 최대한 많은 타일을 사용하려고 한다.
# 두 조건을 모두 만족하기 어렵다고 판단한 원재는 이 두 조건에 대해 가중치 A, B를 가지고 나름의 식을 도출해냈다.
# A X |R – C| + B X (N - R X C)
# 원재는 위의 값을 최소화하려고 한다. 최소화된 이 값을 출력하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 세 정수 N, A, B(1 ≤ N, A, B ≤ 10^5)가 공백으로 구분되어 주어진다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 답을 출력한다.


for t in range(1, int(input())+1):
    N, A, B = map(int, input().split())
    # 기준은 N의 루트 값보다 크지 않은 가장 큰 정수
    R = int(N**(1/2))
    C = R
    min_v = B*(N-R*C)
    # 1부터 R까지의 i에 대해서 i*C가 R*R보다 작지 않은 경우만 확인
    # i*C가 R*R보다 작으면서 주어진 가중치 식의 값이 더 작아질 수는 없다.(R*R은 A*|R-C|부분이 0이기 때문에)
    for i in range(1, R+1):
        C = N // i
        while i*C > R**2:
            v = A*abs(i-C) + B*(N-i*C)
            if v < min_v:
                min_v = v
            C -= 1

    print('#%d %d' % (t, min_v))
