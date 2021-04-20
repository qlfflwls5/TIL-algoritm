# min, max 구하기
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


# [입력]
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 1
# max함수와 min함수를 구현해서 문제를 해결한다.
def get_max(*args):
    max_num = args[0]
    for i in range(1, len(args)):
        if args[i] > max_num:
            max_num = args[i]
    return max_num

def get_min(*args):
    min_num = args[0]
    for i in range(1, len(args)):
        if args[i] < min_num:
            min_num = args[i]
    return min_num


T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_tuple = tuple(map(int, input().split()))
    max_num = get_max(*num_tuple)
    min_num = get_min(*num_tuple)
    ans = max_num - min_num
    print('#%d %d' % (t, ans))

# max 함수 쓸 때 0번째를 제외한 1번째부터 끝까지를 나타내는 방법
# args[1:] 쓰면 된다. range(1, len(args))쓰지 말고!


#2
# 이 문제에선 max-min을 한 번에 하는 함수를 만드는 것이 낫다. 따로 함수 두 개를 만들지 말고.
# 모범코드
def get_min_max(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num - min_num


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    D = list(map(int, input().split()))
    ans = get_min_max(D)
    print('#%d %d' % (t, ans))


# 3
# 정렬을 한 후 0번째와 마지막 번째의 차이를 구해도 되겠다.