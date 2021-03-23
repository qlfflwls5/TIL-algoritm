# 새샘이의 7-3-5 게임
# 숫자게임을 좋아하는 새샘이는 서로 다른 7개의 정수 중에서 3개의 정수를 골라 합을 구해서 수를 만들려고 한다.
# 이렇게 만들 수 있는 수 중에서 5번째로 큰 수를 출력하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 7개의 서로 다른 정수가 공백으로 구분되어 주어진다. 각 정수는 1이상 100이하이다.


# [출력]
# 각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 답을 출력한다.


def combi(level, start, S):
    if level >= K:
        sum_set.add(S)
        return

    for i in range(start, M-K+level+1):
        combi(level+1, i+1, S+num[i])


for t in range(1, int(input())+1):
    num = list(map(int, input().split()))
    M, K = 7, 3
    sum_set = set()
    combi(0, 0, 0)
    print('#%d %d' % (t, sorted(list(sum_set), reverse=True)[4]))
