# 1. A, B 배열에서 B의 각 요소를 A에서 이진탐색을 이용해 찾을 때 비교횟수 누적값 출력, 못찾았다면 0으로
# 2. A, B 배열에서 B의 각 요소를 A에서 이진탐색으로 K번 비교 내에 찾을 수 있는지 검사하여, 찾을 수 있는 것의 개수 출력
# 3. A, B 배열에서 못 찾았을 경우 작은 것 중 가장 큰 것 검색
# 4. A, B 배열에서 못 찾았을 경우 큰 것 중 가장 작은 것 검색
# 5. A, B 배열에서 A에 중복 데이터가 있다고 할 때 가장 앞의 것을 찾기


# 1, 2, 3, 4번 동시 해결
def binary_search(b):
    s, e = 0, len_A - 1
    accumulate = 0
    while s <= e:
        mid = (s+e)//2
        accumulate += 1
        if A[mid] == b:
            if K >= accumulate:
                K_cnt[0] += 1
            print('%d의 비교 횟수: ' % b, accumulate)
            return accumulate
        elif A[mid] > b:
            e = mid - 1
        else:
            s = mid + 1

    if e >= 0:
        list3.append((b, A[e]))
    if s < len_A:
        list4.append((b, A[s]))
    return 0


for t in range(1, int(input())+1):
    len_A, len_B = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    K_cnt = [0]
    accumulate_sum = 0
    # 3번의 답들, 4번의 답들을 담을 리스트
    list3, list4 = [], []
    for b in B:
        accumulate_sum += binary_search(b)

    print('3번: ', list3)
    print('4번: ',list4)
    print('총 누적 비교 횟수: ', accumulate_sum)
    print('K번 횟수 내 비교 완료: ', K_cnt[0])


# 5번
def binary_search(b):
    s, e = 0, len_A - 1
    while s <= e:
        mid = (s+e)//2
        # 끝의 것을 갖고 오고 싶다면 등호를 빼고 e를 리턴하면 됨
        if A[mid] >= b:
            e = mid - 1
        else:
            s = mid + 1

    return s if 0 <= s < len_A else -1


for t in range(1, int(input())+1):
    len_A, len_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for b in B:
        print('%d의 첫 인덱스: ' % b, binary_search(b))