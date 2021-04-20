# 부분집합의 합
# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 
# 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 1
# 부분집합에 비트연산을 활용하는 방법
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    # 1~12를 담은 리스트 생성
    arr = list(range(1, 13))
    # 조건을 만족하는 부분집합의 개수를 담을 변수 생성
    result = 0
    # 모든 부분집합의 개수에 대하여 각 i번째 부분집합의 i를 이진수로 표현한 것에 1이 N개 들어있는지,
    # 해당 1이 있는 위치를 인덱스로 대응하여 가져온 arr의 값의 합이 K인지를 확인해야 한다.
    for i in range(1 << 12):
        total = 0
        cnt = 0
        # j는 마스크가 되어 i를 2진수로 표현한 것에서의 뒤에서부터 1의 위치를 의미하게 된다.
        for j in range(12):
            if i & (1 << j):
                total += arr[j]
                cnt += 1
            # 효율적으로 하기 위해 조건을 넘어서면 반복 그만. 하지만 이 조건문이 더 비효율적일 수도 있다. 때에 따라 다름부
            if cnt > N or total > K:
                break
                
        if cnt == N and total == K:
            result += 1
            
    print('#%d %d' %(t, result))


# 위의 코드에서 부분집합을 만드는 코드를 t의 바깥으로 빼서 따로 만드는 것이 테스트 케이스가 많을 때는 훨씬 효율적이다.
# arr = list(range(1, 13))
# lst = [] # 부분집합을 전부 넣을 리스트
# for i in range(1 << 12):
#     sub_lst = []
#     for j in range(12):
#         if i & (1 << j):
#             sub_lst.append(arr[j])
#     lst.append(sub_lst)
# 이후 부분집합을 전부 만들었기 때문에 여기서 길이가 N이고 합이 K인 것을 찾으면 된다.
# answer = [1 for i in lst if len(i) == N if sum(i) == K]
# len(answer)나 sum(answer)가 답이 된다.


# 다시 한 번, 위의 방식으로 푼다고 할 때, lst를 길이에 따라서 나누어 부분집합을 만들 수는 없을까?
# 예를 들어, lst[1] = [[1], [2], [3] , ... [12]]
# lst [2] = [[1, 2], [1, 3], [1, 4], ... [11, 12]]
# lst = [[]*13]
# lst[len(sub_lst)] += sub_lst


# 2
# 부분집합의 합에서 비트연산이 아닌 새롭게 풀 수 있는 방법
# 1) 초기화
# sums는 (요소의 개수, 요소의 합) tuple로 이루어진 list
# 초기화된 sums에 있는 (0, 0)은 공집합이다.
sums = [(0, 0)]
# 2) 모든 부분집합 구하기
for num in range(1, 13):
    sums += [(_cnt + 1, _sum + num) for _cnt, _sum in sums]
    print(sums)
# 3) 조건에 맞는 것 찾기
answer = 0
for sum_tuple in sums:
    if sum_tuple == (N, K):
        answer += 1
