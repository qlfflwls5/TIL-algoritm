# 요리사
# 두 명의 손님에게 음식을 제공하려고 한다.
# 두 명의 손님은 식성이 비슷하기 때문에, 최대한 비슷한 맛의 음식을 만들어 내야 한다.
# N개의 식재료가 있다.
# 식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)
# 이때, 각각의 음식을 A음식, B음식이라고 하자.
# 비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야 한다.
# 음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게 된다.
# 식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다. (1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)
# 각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합이다.
# 식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고,
# 가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때,
# 두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.


# [예시]
# N = 4인 예를 생각해보자. 시너지 Sij는 [Table 1]과 같이 주어진다.
# (세로축으로 i번째 위치에 있고 가로축으로 j번째 위치에 있는 값이 Sij이다.)
# 식재료 1과 식재료 2를 A음식으로 만들고 식재료 3과 식재료 4를 B음식으로 만드는 경우를 생각하자.

# 1) 식재료 1을 식재료 2와 같이 요리했을 때 발생하는 시너지 S12는 5이다.
# 2) 식재료 2를 식재료 1과 같이 요리했을 때 발생하는 시너지 S21는 4이다.
# 3) A음식의 맛은 5 + 4 = 9가 된다.
# 4) 식재료 3을 식재료 4와 같이 요리했을 때 발생하는 시너지 S34는 3이다.
# 5) 식재료 4를 식재료 3과 같이 요리했을 때 발생하는 시너지 S43은 3이다.
# 6) B음식의 맛은 3 + 3 = 6이 된다.

# 따라서, 두 음식 간의 맛의 차이는 |9 – 6| = 3이 된다.


# [제약사항]
# 1. 시간 제한 : 최대 50개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 모두 3초
# 2. 식재료의 수 N은 4이상 16이하의 짝수이다. (4 ≤ N ≤ 16)
# 3. 시너지 Sij는 1이상 20,000이하의 정수이다. (1 ≤ Sij ≤ 20,000, i ≠ j)
# 4. i와 j가 서로 같은 경우의 Sij값은 정의되지 않는다. 입력에서는 0으로 주어진다.


# [입력]
# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고,
# 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 식재료의 수 N이 주어진다.
# 다음 N개의 줄에는 N * N개의 시너지 Sij값들이 주어진다. i와 j가 서로 같은 경우는 0으로 주어진다.


# [출력]
# 테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
# 각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t 는 1부터 시작하는 테스트 케이스의 번호이다.)
# 정답은 두 음식 간의 맛의 차이가 최소가 되도록 A음식과 B음식을 만들었을 때 그 차이 값이다.

# N개의 재료 중에서 N//2개를 뽑는 함수
def combi(level, start):
    # 종료조건
    if level >= N//2:
        global min_dif
        result = get_taste(A, B)
        if result < min_dif:
            min_dif = result
        return

    for i in range(start, N-N//2+level+1):
        # 이렇게 remove append를 일일이 해주는 것이 나중에 A에서 없는 것을 for문을 돌며 찾아 B를 만드는 것보다 훨씬 실행시간이 짧다.
        A.remove(i)
        B.append(i)
        combi(level+1, i+1)
        A.append(i)
        B.remove(i)


def get_taste(A, B):
    taste_A, taste_B = 0, 0
    for i in range(N//2):
        for j in range(N//2):
            taste_A += arr[A[i]][A[j]]
            taste_B += arr[B[i]][B[j]]

    return abs(taste_A - taste_B)


for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_dif = 987654321
    # A만 구성하고, B는 A에 없는 것으로 만들 것이다.
    A = list(range(N))
    B = []
    combi(0, 0)

    print('#%d %d' % (t, min_dif))


# 2
# 승현님 - 빠르다
def cook(a, b):
    global min_dif
    a_mat = 0
    b_mat = 0
    for i in range(1, N // 2):
        for j in range(i):
            a_mat += synergy[a[j]][a[i] - a[j] - 1]
            b_mat += synergy[b[j]][b[i] - b[j] - 1]
    min_dif = min(min_dif, abs(a_mat - b_mat))


def divide(a, b, num):
    if num == N:
        cook(a, b)
    else:
        if len(a) < N // 2:
            divide(a + [num], b, num + 1)
        if len(b) < N // 2:
            divide(a, b + [num], num + 1)
    return


for t in range(1, int(input()) + 1):
    N = int(input())
    syn = [list(map(int, input().split())) for _ in range(N)]
    synergy = [[] for _ in range(N - 1)]
    for i in range(1, N):
        for j in range(i):
            synergy[j].append(syn[i][j] + syn[j][i])
    min_dif = float('inf')
    divide([0], [], 1)
    print("#%d %d" % (t, min_dif))