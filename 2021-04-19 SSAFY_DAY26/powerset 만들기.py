# powerset 만들기
# 입력 받은 N개의 데이터에 대한 powerset 중 원소의 합이 M인 부분집합의 개수를 출력하세요!
# N이 3인 데이터 집합 [1, 2, 3]에서 M이 5인 부분집합의 개수는 1개이고, M이 3인 부분집합의 개수는 2개이다


def powerset(start, S):
    if S > M:
        return

    if S == M:
        cnt[0] += 1
        return

    for i in range(start, N):
        powerset(i+1, S+data[i])


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    cnt = [0]
    powerset(0, 0)
    print('#%d %d' % (t, cnt[0]))