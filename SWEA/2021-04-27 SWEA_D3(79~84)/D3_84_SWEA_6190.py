# 정곤이의 단조 증가하는 수
# 정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.
# 그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
# 어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.
# 예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
# 양의 정수 N 개 A1, …, AN이 주어진다.
#  1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.
# 두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.


# [출력]
# 각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.
# 만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.


# 1
# 조합을 이용
def combi(level, start, S):
    if level == 2:
        danzo(str(S))
        return

    for i in range(start, len(A)-2+level+1):
        combi(level+1, i+1, S*A[i])


def danzo(S):
    global max_v
    if int(S) < int(max_v):
        return

    for i in range(1, len(S)):
        if int(S[i]) < int(S[i-1]):
            return

    max_v = S


for t in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    max_v = '0'
    combi(0, 0, 1)
    print('#%d %s' % (t, max_v if max_v != '0' else '-1'))


# 2
# 이 문제는 진짜 조합을 쓰라는 문제가 아니다. 정렬을 이용해보자
def danzo(S):
    global max_v
    for i in range(1, len(S)):
        if int(S[i]) < int(S[i-1]):
            return

    max_v = int(S)


for t in range(1, int(input())+1):
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    max_v = -1
    for i in range(N-1):
        for j in range(i+1, N):
            k = A[i]*A[j]
            if k <= max_v:
                break
            danzo(str(k))

    print('#%d %d' % (t, max_v))