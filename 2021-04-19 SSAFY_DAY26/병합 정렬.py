# 병합 정렬
# 알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.
# 정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.
# N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.
# 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
# 정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.
# 알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
# 5<=N<=1,000,000, 0 <= ai <= 1,000,000


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.


def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    a_arr = mergesort(arr[:mid])
    b_arr = mergesort(arr[mid:])
    ai, bi = 0, 0
    temp = []
    while ai < len(a_arr) and bi < len(b_arr):
        if a_arr[ai] <= b_arr[bi]:
            temp.append(a_arr[ai])
            ai += 1
        else:
            temp.append(b_arr[bi])
            bi += 1

    if ai == len(a_arr):
        temp.extend(b_arr[bi:])
    else:
        global cnt
        cnt += 1
        temp.extend(a_arr[ai:])

    return temp


for t in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = mergesort(arr)
    print('#%d %d %d' % (t, arr[N//2], cnt))