# 구간합 코드
# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
# 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 1
# 매구간마다 구간합을 구해 비교하면 최대값, 최소값 찾기
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = 0
    # max_sum과 min_sum의 첫 값을 첫 구간합으로 주기
    for i in range(M):
        max_sum += a_list[i]
        min_sum += a_list[i]
    # 그 이후부터 계속해서 구간합을 구하며 크기 비교, N-M+1이 중요하다.
    for i in range(1, N-M+1):
        temp_sum = 0
        for j in range(i, i+M):
            temp_sum += a_list[j]
        if temp_sum > max_sum:
            max_sum = temp_sum
        elif temp_sum < min_sum:
            min_sum = temp_sum
    print('#%d %d' %(t, max_sum - min_sum))


# 2번째 풀이 이게 더 좋은 방법이다. 구간합 슬라이딩 윈도우
# 구간합은 슬라이딩 윈도우로 풀어라. 대소 비교 이전에 그냥 나가는거 뺴고 들어오는거 더하자.
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    max_sum, min_sum, temp_sum = 0, 0, 0
    # 첫 최대값, 최소값은 첫 구간합으로 준다.
    for i in range(M):
        max_sum += a_list[i]
        min_sum += a_list[i]
        temp_sum += a_list[i]
    # 그 이후부터 한 칸 이동하여 i번째 인덱스에 올때마다 i-1번째를 이전 구간합에서 빼고 i+M-1번째를 이전 구간합에 더해 새로운 구간합을 구한다.
    for i in range(1, N-M+1):
        temp_sum = temp_sum + a_list[i+M-1] - a_list[i-1]
        if temp_sum > max_sum:
            max_sum = temp_sum
        if temp_sum < min_sum:
            min_sum = temp_sum

    print('#%d %d' %(t, max_sum - min_sum))



