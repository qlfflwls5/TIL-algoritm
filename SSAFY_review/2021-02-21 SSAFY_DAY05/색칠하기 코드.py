# 색칠하기
# 그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
# 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
# 예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
# 2
# 2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
# 3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
# 다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
# color = 1 (빨강), color = 2 (파랑)


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 두 색이 겹치는 곳을 찾아야 한다.단순히 카운트나 부호로 따지기에는 한 색이 두 번 겹쳐있는 경우가 있을 수 있으므로 안된다.
# 메모리와 시간의 낭비가 조금 있겠지만 확실하게 나누기 위해서는 각 리스트 요소의 부분을 문자열로 하는 것이 좋을 것 같다. 'r'과 'b'

# 1
# 함수 사용
def color_rb(arr, r1, c1, r2, c2, color):
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            # 이 if문을 arr[i][j] == 0 or arr[i][j] == color로 하고 내용을 arr[i][j] = color로 해도 좋을듯. else의 내용은 arr[i][j] += color로
            # 다만 이 경우에는 빨간색, 파란색이 번갈아 겹쳐지면 불가능하다. 내 풀이는 다 가능하다.
            if color == 1:
                arr[i][j] += 'r'
            else:
                arr[i][j] += 'b'


def check_purple(arr):
    purple = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if 'rb' in arr[i][j] or 'br' in arr[i][j]:
                purple += 1
    return purple


T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 빈 문자열을 요소로 갖는 10*10의 이중배열 생성
    arr = [['']*10 for _ in range(10)]
    # 빨간색, 파란색 색칠하기
    for _ in range(N):
        color_rb(arr, *map(int, input().split()))
    # 보라색인 부분 찾기
    print('#%d %d' %(t, check_purple(arr)))


# 2
# 함수 미사용
T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 빈 문자열을 요소로 갖는 10*10의 이중배열 생성
    arr = [['']*10 for _ in range(10)]
    # 빨간색, 파란색 색칠하기
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:
                    arr[i][j] += 'r'
                else:
                    arr[i][j] += 'b'
    # 보라색인 부분 찾기
    purple = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if 'rb' in arr[i][j] or 'br' in arr[i][j]:
                purple += 1
    print('#%d %d' %(t, purple))


# 3
# 비트연산을 사용해도 좋다.
# 기본을 0b11로 전부 채우고, 빨강이면 0b01을 &연산, 파란색이면 0b10을 &연산하면 0b00이 되면 보라색인 것이다.
def check_purple(arr):
    cnt = 0
    for r in range(len(arr)):
        for c in range(len(arr)):
            if arr[r][c] == 0:
                cnt += 1
    return cnt


def color_rb(arr, r1, c1, r2, c2, color):
    # 무색 11 빨강 01 파랑 10 보라 00
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            arr[r][c] &= color


T = int(input())
for t in range(1, T + 1):
    r, c = 10, 10
    arr = [[3] * r for _ in range(c)]
    N = int(input())
    for i in range(N):
        color_rb(arr, *map(int, input().split()))

    print('#%d %d' % (t, check_purple(arr)))


# 4
# 이중배열을 풀 때는 메모리가 많이 소요된다.
# 따라서 이 이중배열을 그냥 리스트 두 개로 나누어서 푸는 방법도 생각해봐야 한다.
# 예를 들어, 이 문제와 같은 경우 red리스트와 blue리스트를 만들어 풀면 기본 arr을 안만들어도 된다.
# red리스트에는 red에 대한 위치의 정보를, blue에는 blue에 대한 위치의 정보를 담고 둘이 겹치는 곳이 purple이 된다.
# 이를 희소행렬이라고 한다. 배경 이중배열이 너무 크고 데이터는 적은 경우 이중배열을 만들지말고 데이터 개개의 '좌표'를 활용한다.