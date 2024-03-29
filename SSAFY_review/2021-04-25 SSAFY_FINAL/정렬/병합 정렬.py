# 숫자를 정렬하자
# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.


# [제약 사항]
# N 은 5 이상 50 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    a_arr = merge_sort(arr[:mid])
    b_arr = merge_sort(arr[mid:])
    ai, bi = 0, 0
    temp = []
    while ai < len(a_arr) and bi < len(b_arr):
        if a_arr[ai] <= b_arr[bi]:
            temp.append(a_arr[ai])
            ai += 1
        else:
            temp.append(b_arr[bi])
            bi += 1

    temp.extend(a_arr[ai:])
    temp.extend(b_arr[bi:])

    return temp


for t in range(1, int(input())+1):
    N = int(input())
    num = list(map(int, input().split()))
    result = merge_sort(num)
    print('#%d %s' % (t, ' '.join(map(str, result))))