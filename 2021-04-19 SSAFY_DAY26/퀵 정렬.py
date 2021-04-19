# 퀵 정렬
# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
# 5<=N<=1,000,000, 0 <= ai <= 1,000,000


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, , N/2번 원소를 출력한다.


# 1
# 이건 정석
def quicksort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quicksort(arr, l, s-1)
        quicksort(arr, s+1, r)


def partition(arr, l, r):
    p = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


for t in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    quicksort(A, 0, N-1)
    print('#%d %d' % (t, A[N//2]))
    
    
# 2
# 이건 간추려서
def quicksort(l, r):
    if l < r:
        p = A[r]
        i = l
        for j in range(l, r):
            if A[j] <= p:
                A[i], A[j] = A[j], A[i]
                i += 1

        A[i], A[r] = A[r], A[i]
        quicksort(l, i-1)
        quicksort(i+1, r)


for t in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    quicksort(0, N-1)
    print('#%d %d' % (t, A[N//2]))