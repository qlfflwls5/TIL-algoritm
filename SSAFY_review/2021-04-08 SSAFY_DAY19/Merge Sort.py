# Merge Sort


def merge_sort(arr):
    # 하나가 남을 때까지 쪼개놨으면 자기 자신 리턴
    if len(arr) == 1:
        return arr
    # 가운데 정하기
    mid = len(arr) // 2
    # 쪼개서 왼쪽
    a_arr = merge_sort(arr[:mid])
    # 쪼개서 오른쪽
    b_arr = merge_sort(arr[mid:])
    # 아래에서 넘어온 두 조각을 정렬
    temp = [] # a_arr, b_arr을 합쳐서 하나의 정렬된 배열
    ai = bi = 0
    while ai < len(a_arr) and bi < len(b_arr):
        if a_arr[ai] < b_arr[bi]:
            temp.append(a_arr[ai])
            ai += 1
        else:
            temp.append(b_arr[bi])
            bi += 1
    if ai == len(a_arr):
        temp.extend(b_arr[bi:])
    else:
        temp.extend(a_arr[ai:])

    return(temp)


a = [5, 1, 9, 6, 8, 4, 2, 3]
print(merge_sort(a))