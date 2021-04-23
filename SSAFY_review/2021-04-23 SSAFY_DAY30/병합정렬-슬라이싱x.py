# 슬라이싱을 사용하지 않은 병합정렬 최적화
def mergesort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low+high)//2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        ai, bi = low, mid
        while ai < mid and bi < high:
            if arr[ai] <= arr[bi]:
                temp.append(arr[ai])
                ai += 1
            else:
                temp.append(arr[bi])
                bi += 1

        while ai < mid:
            temp.append(arr[ai])
        while bi < high:
            temp.append(arr[bi])

        for i in range(low, high):
            arr[i] = temp[i-low]

    return sort(0, len(arr))