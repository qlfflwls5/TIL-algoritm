# 파도반 수열
# 아래 그림과 같이 삼각형이 나선모양으로 늘어서 있는 형태를 생각해보자.
# 아래 그림과 같이 삼각형이 나선모양으로 늘어서 있는 처음에 이 나선은 한 변의 길이가 1인 정삼각형에서 시작한다.
# 그리고 현재 만들어진 나선에서 가장 긴 변에 그 변의 길이와 같은 크기의 정삼각형을 추가해 넣는다. 파도반 수열 PN은 나선에 N번째로 추가한 나선의 길이를 의미하는 수열이다.
# P1에서 P10까지를 순서대로 나열하면 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.
# N이 주어질 때 PN을 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 100 )이 주어진다.


# [출력]
# 각 테스트 케이스마다 PN을 출력한다.


for t in range(1, int(input())+1):
    N = int(input())
    DP = [1, 1, 1, 2, 2]
    for i in range(5, N):
        DP.append(DP[i-1] + DP[i-5])
    print('#%d %d' % (t, DP[N-1]))
