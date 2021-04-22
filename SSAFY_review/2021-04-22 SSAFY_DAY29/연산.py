# dijkstra-연산
# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
# 단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
# 예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


# [입력]
# 첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# '백만 이하의 자연수'에 조심해야 한다.
# 반복 수가 크므로 pop, append가 아닌 front, rear를 사용해 queue를 구현한다.
# 만약 가능만 하다면, append는 놔둬서 queue의 길이를 생각하지 않고, pop만 front를 통해 구현하는 것이 낫다.
def BFS_perm(S):
    # visited가 중요. 이미 방문한 숫자는 다시 갈 필요가 없다.
    visited = [0]*(10**6+1)
    queue = [tuple()]*(10**6+1)
    front, rear = 0, 0
    visited[S] = 1
    queue[rear] = (0, S)
    rear += 1
    while front < rear:
        level, S = queue[front]
        front += 1
        if S == M:
            min_v[0] = min(min_v[0], level)
            break

        for i in range(4):
            temp = calc[i](S)
            if 0 < temp <= 10**6 and not visited[temp]:
                visited[temp] = 1
                queue[rear] = (level+1, temp)
                rear += 1


calc = {0: (lambda x: x+1), 1: (lambda x: x-1), 2: (lambda x: x*2), 3: (lambda x: x-10)}
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    min_v = [float('inf')]
    BFS_perm(N)
    print('#%d %d' %(t, min_v[0]))


# 2
# 엄청 빠르다.
def calc():
    cnt = [0] * 1000001
    q = [N]
    front = 0
    while q:
        temp = q[front]
        front += 1
        for i in range(4):
            if i == 3:
                x = temp * dx[i]
            else:
                x = temp + dx[i]
            if 0 <= x < 1000001 and cnt[x] == 0:
                cnt[x] = cnt[temp] + 1
                if x == M:
                    return cnt[x]
                q.append(x)


dx = [1, -1, -10, 2]
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    result = calc()
    print('#%d %d' % (t, result))