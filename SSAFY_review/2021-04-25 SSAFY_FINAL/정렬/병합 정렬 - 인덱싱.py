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
    def sort(l, r):
        if r - l < 2:
            return
        mid = (l + r)//2
        sort(l, mid)
        sort(mid, r)
        merge(l, mid, r)

    def merge(l, mid, r):
        ai, bi = l, mid
        temp = []
        while ai < mid and bi < r:
            if arr[ai] < arr[bi]:
                temp.append(arr[ai])
                ai += 1
            else:
                temp.append(arr[bi])
                bi += 1

        temp.extend(arr[ai:mid])
        temp.extend(arr[bi:r])

        for i in range(l, r):
            arr[i] = temp[i-l]

    return sort(0, len(arr))


for t in range(1, int(input())+1):
    N = int(input())
    num = list(map(int, input().split()))
    merge_sort(num)
    print('#%d %s' % (t, ' '.join(map(str,num))))