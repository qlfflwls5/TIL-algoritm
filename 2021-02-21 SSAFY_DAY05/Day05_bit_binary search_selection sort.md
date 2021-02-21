# 2021.02.16_0215복습&문제풀이





## 새롭게 배운 것들



## 1. 색칠하기

```python
# 내 풀이
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
```

+ 이중 리스트 만들때
  + `[[0]*10]*10`같은 코드는 **절대 사용하지 말 것**
    + 이건 `[[0]*10]`이 10번 곱해지는 것이므로 '**얕은 복사**'가 기본적으로 일어나는 python에서는 10개의 `[0]*10`이 모두 같은 객체를 참조한다. 즉, 하나를 바꾸면 나머지 9줄이 전부 같이 바뀐다.
  + `[[0]*10 for _ in range(10)]`과 같이 바꿔야 한다. 얘는 for문으로 순회마다 새로운 객체 `[0]*10`이 생성이 되는 것이다.

+ 비트연산
  + &연산이나 |연산을 통해서 매우 다양한 풀이를 할 수 있다.
  + 예를 들어 **switch**의 역할을 비트 연산으로 할 수 있다.
  + 분기를 나눌 때에 이를 적절히 활용한다.

```python
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
```

+ 이중배열을 만들고 작업하는 것은 메모리의 소모가 크다.
  + 따라서 리스트 두 개로 나누어 푸는 방법이 있다.
  + 이 문제같은 경우 red와 blue의 좌표를 활용하는 방법이다.
  + 이중배열이 너무 크고 데이터는 적은 경우 데이터 개개의 **좌표**를 활용한다.







## 2. 부분집합의 합

```python
# 내 풀이
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    # 1~12를 담은 리스트 생성
    arr = list(range(1, 13))
    # 조건을 만족하는 부분집합의 개수를 담을 변수 생성
    result = 0
    # 모든 부분집합의 개수에 대하여 각 i번째 부분집합의 i를 이진수로 표현한 것에 1이 N개 들어있는지,
    # 해당 1이 있는 위치를 인덱스로 대응하여 가져온 arr의 값의 합이 K인지를 확인해야 한다.
    for i in range(1 << 12):
        total = 0
        cnt = 0
        # j는 마스크가 되어 i를 2진수로 표현한 것에서의 뒤에서부터 1의 위치를 의미하게 된다.
        for j in range(12):
            if i & (1 << j):
                total += arr[j]
                cnt += 1
            # 효율적으로 하기 위해 조건을 넘어서면 반복 그만. 하지만 이 조건문이 더 비효율적일 수도 있다. 때에 따라 다름부
            if cnt > N or total > K:
                break
                
        if cnt == N and total == K:
            result += 1
            
    print('#%d %d' %(t, result))
```

+ 부분집합을 전부 구하는 것은 비트연산을 활용한다고 배웠다.
+ 그러나, **1~n까지의 숫자 리스트**에서 부분집합을 활용할 때는 다음과 같은 방법이 유용하다.

```python
sums = [(0, 0)] # 초기값
for num in range(1, N+1):
    sums += [(_cnt+1, _sum+num) for _cnt, _sum in sums]
    # sums는 1부터 N까지의 숫자 리스트의 모든 부분집합의 개수와 합의 쌍을 요소로 갖는다.
```

+ **길이에 따라 부분집합을 나눠서 저장하기**

```python
# 예를 들어, lst[1] = [[1], [2], [3] , ... [12]]
# lst[2] = [[1, 2], [1, 3], [1, 4], ... [11, 12]]
lst = [[]*13] # 사전에 미리 제일 긴 부분집합의 길이 + 1개 만큼의 빈 이중배열을 만든다.
lst[len(sub_lst)] += sub_lst # 부분집합을 구한 후 이런식으로 lst에 저장한다.
```







## 3. 이진 탐색, 선택 정렬

+ 이진 탐색

```python
def binarySearch(P, key):
    l, r, cnt = 1, P, 0
    while l <= r:
        c = (l+r) // 2
        cnt += 1
        if c == key:
            return cnt
        # 원래 이진탐색은 r = c-1, l = c+1 식으로 하는게 맞으나, 이 문제는 조건이 이렇게 주어져 있다.
        elif c > key:
            r = c
        else:
            l = c


T = int(input())
for t in range(1, T+1):
    P, A, B = map(int, input().split())
    val_A, val_B = binarySearch(P, A), binarySearch(P, B)
    result = 'A' if val_A < val_B else '0' if val_A == val_B else 'B'
    print('#%d %s' %(t, result))
```

+ 선택 정렬

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst_num = list(map(int, input().split()))
    for i in range(0, 10):
        if i%2:
            min_i = i
            # 최소값을 찾아 현재 i번째의 값과 자리를 바꾼다.
            for j in range(i + 1, len(lst_num)):
                if lst_num[j] < lst_num[min_i]:
                    min_i = j

            lst_num[i], lst_num[min_i] = lst_num[min_i], lst_num[i]
        else:
            max_i = i
            # 최대값을 찾아 현재 i번째의 값과 자리를 바꾼다.
            for j in range(i + 1, len(lst_num)):
                if lst_num[j] > lst_num[max_i]:
                    max_i = j

            lst_num[i], lst_num[max_i] = lst_num[max_i], lst_num[i]

    print('#%d ' % t, end='')
    if len(lst_num) > 10:
        print(*lst_num[:10])
    else:
        print(*lst_num)
```







## 4. 사다리타기

+ 양끝에 닿았을 때가 문제의 포인트다.
  + 1) 패딩을 넣는다.
    + 양끝에 `[0]`을 집어넣어 모든 규칙에서 동일하게 적용되도록 한다.
  + 2) 상황에 맞게 계산하여 규칙을 지정한다.
    + 사다리타기에서 0번째 열에서는 왼쪽으로 갈 일이 없다. N-1번째 열에서는 오른쪽으로 갈 일이 없다.
    + 따라서, **왼쪽으로 가는 규칙에는 0 < c**의 조건을 넣고
    + **오른쪽으로 가는 규칙에서는 c < N-1**의 조건만 넣으면 규칙이 성립된다.
    + 왼쪽이나 오른쪽으로 갈 때는 쭉 가고 나서 항상 마지막에 직진을 1번 실행하여 다음 시행에 직진부터 적용되게 해야 한다.

