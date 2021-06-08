# [Professional] 키 순서
# 1번부터 N번까지 번호가 붙여져 있는 학생들에 대하여 두 학생끼리 키를 비교한 결과의 일부가 주어져 있다.
# 단, N명의 학생들의 키는 모두 다르다고 가정한다.
# 예를 들어, 6명의 학생들에 대하여 6번만 키를 비교하였고, 그 결과가 다음과 같다고 하자.

# ● 1번 학생의 키 < 5번 학생의 키
# ● 3번 학생의 키 < 4번 학생의 키
# ● 5번 학생의 키 < 4번 학생의 키
# ● 4번 학생의 키 < 2번 학생의 키
# ● 4번 학생의 키 < 6번 학생의 키
# ● 5번 학생의 키 < 2번 학생의 키

# 이 비교 결과로부터 모든 학생 중에서 키가 가장 작은 학생부터 자신이 몇 번째인지 알 수 있는 학생들도 있고
# 그렇지 못한 학생들도 있다는 사실을 아래처럼 그림을 그려 쉽게 확인할 수 있다.
# a번 학생의 키가 b번 학생의 키보다 작다면, a에서 b로 화살표를 그려서 표현하였다.
# 1번은 5번보다 키가 작고, 5번은 4번보다 작기 때문에, 1번은 4번보다 작게 된다.
# 그러면 1번, 3번, 5번은 모두 4번보다 작게 된다.
# 또한 4번은 2번과 6번보다 작기 때문에, 4번 학생은 자기보다 작은 학생이 3명이 있고,
# 자기보다 큰 학생이 2명이 있게 되어 자신의 키가 몇 번째인지 정확히 알 수 있다.
# 그러나 4번을 제외한 학생들은 자신의 키가 몇 번째인지 알 수 없다.
# 학생들의 키를 비교한 결과가 주어질 때, 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명인지 계산하여 출력하는 프로그램을 작성하시오.


# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 15)
# 각 테스트 케이스의 첫 번째 줄에 학생들의 수 N이 주어진다. (2 ≤ N ≤ 500)
# 각 테스트 케이스의 두 번째 줄에 두 학생의 키를 비교한 횟수 M이 주어진다. (0 ≤ M ≤ N*(N-1)/2)
# 각 테스트 케이스의 세 번째 줄부터 M개의 줄에 걸쳐 두 학생의 키를 비교한 결과를 나타내는 두 양의 정수 a, b가 주어진다.
# 이는 번호가 a인 학생이 번호가 b인 학생보다 키가 작은 것을 의미한다. 이 때, 입력은 항상 모순이 없도록 주어진다.


# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고,
# 자신이 키가 몇 번째인지 알 수 있는 학생이 모두 몇 명인지를 출력한다.


# 트리를 올라가거나 내려가기만 해서 모든 노드를 갈 수 있으면 내 위치를 알 수 있는 것
# 그러나 매번 노드마다 재검사할 필요가 없다. 메모이제이션을 사용한다.
def find_shorter(node):
    # 더 키가 작은 노드가 없다면, 즉 키가 작은 것에서의 리프 노드라면 메모이제이션에는 길이가 0인 집합을 담고 자신을 원소로 하는 집합 반환
    if not shorter[node]:
        short_mm[node] = set()
        return {node}
    
    # 현재 노드의 메모이제이션 값이 될 집합
    short_set = set()
    # 나보다 키가 작다는 정보가 주어진 노드들에 대해서 작업
    for v in shorter[node]:
        # 노드 v의 메모이제이션 값이 있다면 그 값(집합)에 있는 모든 원소들을 내 집합에 add하고 v까지 add
        if short_mm[v] != -1:
            for w in short_mm[v]:
                short_set.add(w)
            short_set.add(v)
        # 노드 v의 메모이제이션 값이 없다면 해당 노드에 대한 find_shorter 재귀 호출 반환값(집합)을 내 집합에 add하고 v까지 add
        else:
            for w in find_shorter(v):
                short_set.add(w)
            short_set.add(v)
    
    # 현재 노드의 메모이제이션 값에 완성된 short_set을 할당
    short_mm[node] = short_set
    
    # 내 메모이제이션 값인 short_set을 반환(재귀호출 시 이를 반환하게 됨)
    return short_set


def find_taller(node):
    if not taller[node]:
        tall_mm[node] = set()
        return {node}

    tall_set = set()
    for v in taller[node]:
        if tall_mm[v] != -1:
            for w in tall_mm[v]:
                tall_set.add(w)
            tall_set.add(v)
        else:
            for w in find_taller(v):
                tall_set.add(w)
            tall_set.add(v)

    tall_mm[node] = tall_set

    return tall_set


for t in range(1, int(input())+1):
    N = int(input())
    M = int(input())
    taller = [[] for _ in range(N)]
    shorter = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        # 주어지는 입력값과 인덱스를 맞추기 위해 -1처리
        shorter[b-1].append(a-1)
        taller[a-1].append(b-1)
    
    # 메모이제이션
    tall_mm = [-1]*N
    short_mm = [-1]*N
    for i in range(N):
        # 가장 키가 큰 노드에서만 find_shorter를 실행해도 재귀로 모든 노드에서 실행되므로 가장 효율적
        if not taller[i]:
            find_shorter(i)
        # 가장 키가 작은 노드에서만 find_taller를 실행해도 재귀로 모든 노드에서 실행되므로 가장 효율적
        if not shorter[i]:
            find_taller(i)

    result = 0
    for i in range(N):
        # 각 노드에 대해 키가 작은 노드들의 수와 키가 큰 노드들의 수의 합이 N-1(자신을 제외한 모든 노드의 수)라면 내 위치를 알 수 있다.
        if len(short_mm[i]) + len(tall_mm[i]) == N-1:
            result += 1

    print('#%d %d' % (t, result))




