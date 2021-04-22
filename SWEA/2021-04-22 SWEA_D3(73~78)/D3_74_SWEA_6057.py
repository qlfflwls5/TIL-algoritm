# 그래프의 삼각형
# 정점이 N개, 간선이 M개 있는 그래프가 주어진다. 정점에는 1번에서 N번까지의 번호가 붙어 있다.
# 이 때, i번 정점과 j번 정점 사이에, j번 정점과 k번 정점 사이에, k번 정점과 i번 정점 사이에
# 모두 간선이 있는 ( i, j, k ) (단, i < j < k )를 삼각형이라고 하자.
# 삼각형의 개수를 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 N, M이 공백으로 구분되어 주어진다.
# 다음 M개의 줄에는 두 정수 x, y가 공백으로 구분되어 주어진다.
# 이는 x번 정점과 y번 정점 사이에 간선이 있다는 의미이다.
# 반대로 y번 정점과 x번 정점 사이에 간선이 있다는 의미도 된다.
# 같은 간선을 의미하는 입력이 여러 번 주어지지 않는다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후,
# 삼각형의 개수를 출력한다.


def find_set(x):
    while x != p[x]:
        x = p[x]

    return x


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    # KRUSKAL 싸이클 확인용
    p = [i for i in range(N+1)]
    # x와 y를 잇는 간선을 넣고 싸이클이 생겼을 때, x와 y에 공통 인접 정점이 있는지 확인하기 위해(있다면 삼각형)
    AL = [[] for _ in range(N+1)]
    cnt = 0
    for _ in range(M):
        x, y = map(int, input().split())
        AL[x].append(y)
        AL[y].append(x)
        rep_x, rep_y = find_set(x), find_set(y)
        # 대표자가 다를 때 유니온
        if rep_x != rep_y:
            p[rep_y] = rep_x
        # 대표자가 같다면 싸이클이 생성된 것
        else:
            # x의 인접 정점들에 대하여 y의 인접 정점 리스트에 있다면 삼각형 생성된 것
            for v in AL[x]:
                if v in AL[y]:
                    cnt += 1

    print('#%d %d' % (t, cnt))


# 2
# 간단히 푸는 법
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    AL = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        AL[v1].extend([v2])
        AL[v2].extend([v1])
    cnt = 0
    for i in range(1, N+2):
        for j in range(i+1, N+2):
            for k in range(j+1, N+2):
                if j in AL[i] and k in AL[j] and i in AL[k]:
                    cnt +=1

    print('#%d' % tc, cnt)