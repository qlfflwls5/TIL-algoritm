# 파스칼의 삼각형
# 크기가 N인 파스칼의 삼각형을 만들어야 한다.
# 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
# 1. 첫 번째 줄은 항상 숫자 1이다.
# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

# N이 4일 경우,
# 1
# 11
# 121
# 1331

# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.


# [제약 사항]
# 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.


# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
# 삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 1
# [1]부터 시작하여 끝에 [1]을 붙여가며, 다음 arr에서 range(1~len(arr)-1)의 인덱스 i를 가지는 각 요소들에 i-1번째 요소를 더하면 된다.
T = int(input())
for t in range(1, T+1):
    N = int(input())
    print('#%d' % t)
    # 첫 번째 시행에서 arr은 [1]
    arr = [1]
    for i in range(N):
        # arr을 출력하고,
        print(*arr)
        # arr의 마지막에 1을 추가한다.
        arr += [1]
        # 이 arr의 1 ~ -2번째까지 요소들은 각각 자기 이전의 인덱스와 더한 값을 가져야 한다.
        # 하지만, 이는 순차로 일어나기 때문에 뒷 인덱스에서는 앞의 변화된 값을 더하게 된다.
        # 그러므로 arr원본을 유지하고 있는 temp_arr이 필요하다.
        temp_arr = list(arr)
        # arr의 해당 요소들은 temp_arr의 이전 인덱스의 값들을 더한다.
        for j in range(1, i+1):
            arr[j] += temp_arr[j-1]


# 2
# 스택 사용하기
def push(v):
    stack.append(v)


def pop():
    if not stack:
        return
    return stack.pop(-1)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = []
    stack = []
    arr = [1]
    result += [arr]
    for i in range(N-1):
        for v in arr:
            push(v)

        arr = stack + [0]
        for j in range(len(stack)):
            arr[-j-1] += pop()

        result += [arr]

    print('#%d' % t)
    for arr in result:
        print(*arr)
    # print('\n'.join(*arr)) -> 이거 중요. 꼭 하자.
    # 혹은, print('\n'.join(' '.join(map(str, num)) for num in tri)) -> 꼭!
        
        
# 3
# 초기값 안줘도 되는 코드 -> 이거 좋다.
# 이렇게 미리 자리를 다 마련해두고 하는 것이 append를 통해 리스트의 크기를 변경하는 방식보다 더 효율적이다.
T = int(input())
for t in range(1, T+1):
    N = int(input())
    tri = [[1]*i for i in range(1, N+1)] # [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]
    for i in range(2, N):
        for j in range(1, i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
    print('#%d' % t)
    for num in tri:
        print(' '.join(map(str, num)))


# 4
for t in range(1, int(input())+1):
    N = int(input())
    result = [[1]]
    for i in range(1, N):
        temp = [1] + [result[i - 1][j - 1] + result[i - 1][j] for j in range(1, i)] + [1]
        result.append(temp)

    print('#%d' % t)
    print('\n'.join(' '.join(map(str, result[k])) for k in range(N)))