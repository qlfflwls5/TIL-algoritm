# 버블정렬
# 인접한 두 수의 크기를 계속 비교해가는 알고리즘이다.

arr = [55, 7, 78, 12, 42]

def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

BubbleSort(arr)
print(arr)