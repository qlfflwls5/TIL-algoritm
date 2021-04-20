# 최소 생산 비용
# A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.
# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.
# 예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다..
#     A  B  C
# 1   73 21 21
# 2   11 59 40
# 3   24 31 83
# 이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 제품 수 N이 주어지고, 이후 제품당 한 줄 씩 N개의 줄에 걸쳐 공장별 생산비용 Vij가 주어진다. 3<=N<=15,   1<=Vij<=99


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


def DFS(level, S):
    if S >= min_S[0]:
        return

    if level == N:
        min_S[0] = S
        return

    for i in range(N):
        if not col[i]:
            col[i] = 1
            DFS(level+1, S+cost[level][i])
            col[i] = 0


for t in range(1, int(input())+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    col = [0]*N
    min_S = [1500]
    DFS(0, 0)
    print('#%d %d' % (t, min_S[0]))

