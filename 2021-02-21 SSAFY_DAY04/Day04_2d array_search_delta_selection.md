# 2021.02.15_2차원 배열 & 검색 & 선택정렬





## 새롭게 배운 것들



## 1. 2차원 배열의 선언

+ 1차원 List를 묶어놓은 List
+ 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
+ **2차원 List**의 선언: **세로길이**(행의 개수), **가로길이**(열의 개수)를 필요로 함
+ Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

```python
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
```

### 1.1 2차원 배열의 입력

+ 2차원 배열은 보통 행과 열, 값을 주어준다.

```python
3 4 # 행 열
1 2 3 4
5 6 7 8
9 10 11 12
```

+ 이러한 입력은 이러한 방법을 통해 처리한다. 크게 3가지

```python
# 1
N, M = map(in, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
# 2
N, M = map(in, input().split())
arr = [0] * N
for i in range(N):
    arr[i] = (list(map(int, input().split())))
    
# 3 리스트 내포 활용
N, M = map(in, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
```



### 1.2 2차원 배열의 접근

+ 배열 순회
  + n*m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법
+ **행 우선 순회**

```python
# i 행의 좌표
# j 열의 좌표
for i in range(len(arr)):
    for j in range(len(arr[0])): # for j in range(len(arr[0])-1, -1, -1) 하면 행 거꾸로 순회
        arr[i][j] # 필요한 연산 수행
```

+ **열 우선 순회**

```python
# i 행의 좌표
# j 열의 좌표
for j in range(len(arr)):
    for i in range(len(arr[0])): # for i in range(len(arr[i])-1, -1, -1) 하면 열 거꾸로 순회
        arr[i][j] # 필요한 연산 수행
```

+ **지그재그 순회**

```python
# i 행의 좌표
# j 열의 좌표
for i in range(len(arr)):
    for j in range(len(arr[0])):
        # m은 열의 길이
        arr[i][j + (m-1-2*j) * (i%2)] # 필요한 연산 수행
```

+ **델타를 이용한 2차원 배열의 탐색**
  + 2차 배열의 한 좌표에서 **4방향의 인접 배열 요소**를 탐색하는 방법

```python
arr[0...n-1][0...n-1]
# dx, dy로 써도 좋고 dr, dc로 써도 좋다. 예제 이후부터는 dr, dc로 쓰자
dr = [-1, 1, 0, 0] # 상하좌우
dc = [0, 0, -1, 1]
# 혹은
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 내가 (1, 1)에 있었다고 예시
r = 1
c = 1

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    # 근데 기존 r이 0이거나 n-1이거나 n이 0이거나 n-1이면 실행하면 안될 것이다.
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        continue
    arr[nr][nc] # 필요한 연산 수행
```

델타를 활용해서 **대각선 4방향**, 체스에서의 나이트의 움직임 등을 만들 수 있다.

+ 전치 행렬

```python
# i 행의 좌표
# j 열의 좌표
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
        	arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            
# 1 2 3      1 4 7
# 4 5 6  ->  2 5 8
# 7 8 9      3 6 9
```



### 1.3 연습문제 1

+ 5*5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후
+ 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
+ 예를 들어 7의 이웃한 값이 2, 6, 8, 12라면 차의 절대값의 합은 12이다.
  + |2 - 7| + |6 - 7| + |8 - 7| + |12 - 7| = 12
+ 전체 요소에서의 작업을 수행한 절대값의 총합을 구하여라



### 1.4 부분집합 합(Subset Sum) 문제 (부분집합 중요)

+ 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이되는 경우가 있는지를 알아내는 문제
+ 예를 들어, `[-7, -3, -2, 5, 8]`이라는 집합이 있을 때, `[-3, -2, 5]`는 이 집합의 부분집하이면서 합이 0이므로 이 경우의 답은 참이 된다.

+ 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, **우선 집합의 모든 부분집합을 생성한 후**에 각 부분집합의 합을 계산하여야 한다.
+ **주어진 집합의 부분집합을 생성하는 방법에 대해서 생각해보자.**

#### 1.4.1 부분집합의 수

+ 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 개수는 **2^n**개이다.

+ 이는 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수다.

#### 1.4.2 부분집합 생성하기

+ 각 원소가 부분집합에 포함되었는지를 loop를 이용하여 확인하고 부분집합을 생성하는 방법

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(*bit)
```

+ 위 예제는 2진수에 대한 완전 탐색이 된다. (0~15)
+ 이러한 코드를 한 반복문으로 할 수 없을까? -> **가장 윗 단계의 for문에서 전체 부분집합 개수 만큼 돌자**
  + `for i in range(2**len(bit))` 하면 알아서 0~15까지 돌 것



### 1.5 비트 연산자

+ 비트 연산자

  `&`: 비트 단위로 AND 연산을 한다.

  `|`: 비트 단위로 OR 연산을 한다.

  `<<`: 피연산자의 비트 열을 왼쪽으로 이동시킨다.

  `>>`: 피연산자의 비트 열을 오른쪽으로 이동시킨다.

+ `<<`연산자
  + 1 <<  n : 2^n 즉, **원소가 n개일 경우의 모든 부분집합의 수**를 의미한다.
  + 1.4.2에서의 식을 이제는 `for i in range(1 << n)`으로 쓸 수 있다.

+ `&`연산자

  + i & (1 << j): **i의 j번째 비트가 1인지 아닌지를 리턴한다.**

  + `for i in range(1 << n):`

    ​	`for j in range(n+1):`

    ​		`if i & ( 1 <<  j): `

+ 이를 통해 보다 간결하게 부분집합을 생성하는 방법

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

# 1 << N은 N길이의 리스트가 갖는 전체 부분집합의 개수. i는 각 부분집합의 길이가 된다.
for i in range(1 << n):
    # i를 2진수로 표현한 것에서 1이 있는 위치와 대응하여 해당 인덱스의 arr값을 가져온다.
    # ex) i가 0010100111이라면 arr[0], arr[1], arr[2], arr[5], arr[7]의 합이 total에 담긴다.
    # 이를 range(n)을 순회하는 j를 사용하여 i & (1 << j)를 통해 구현한다.
    # ex) i가 0010100111이라면 j가 0, 1, 2, 5, 7일 때 i & (1 << j)가 1이 된다.
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=", ") # 부분집합
    print()
print()
```

#### 1.5.1 연습문제 2

+ 부분집합 합 문제 구현하기
  + 실제로 10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성하라

```python
T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    # 편의상 N이라는 변수에 arr의 전체 길이를 담는다.
    N = len(arr)
    # 부분집합 중 합이 0인 것이 있으면 result를 1로 하고 반복문을 바로 종료할 것이다.
    result = 0
    # 1 << N은 N길이의 리스트가 갖는 전체 부분집합의 개수. i는 각 부분집합의 길이가 된다.
    # 공집합이면 부분집합의 합을 구하는 for문이 실행이 안될 것이고 total이 0이 되므로 이를 걸러내기 위해 길이(i)가 0일 때를 제외
    for i in range(1, 1 << N):
        # 각 부분집합의 합을 담을 변수 생성
        total = 0
        # i를 2진수로 표현한 것에서 1이 있는 위치와 대응하여 해당 인덱스의 arr값을 total에 더해 나간다.
        # ex) i가 0010100111이라면 arr[0], arr[1], arr[2], arr[5], arr[7]의 합이 total에 담긴다.
        # 이를 range(N)을 순회하는 j를 사용하여 i & (1 << j)를 통해 구현한다.
        # ex) i가 0010100111이라면 j가 0, 1, 2, 5, 7일 때 i & (1 << j)가 1이 된다.
        for j in range(N):
            if i & (1 << j):
                total += arr[j]
        # total이 0이면서 부분집합의 길이가 0이 아닐 때에 result를 1로 바꾸고 반복을 끝낸다.
        if total == 0:
            result = 1
            break
    print('#%d %d' %(t, result))
```







## 2. 문제 풀이

### 2.1 델타 검색

+ 모든 요소의 상하좌우 인접요소와의 차이의 절대값의 합 구하기

+ 델타 리스트는 반복문 밖으로 빼자. 변하지 않는 참조표는 위에 빼놓는다.

```python
# 각 요소에서 상하좌우 이웃한 요소에 접근하기 위한 델타 리스트. 이런건 밖으로 빼자
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    # 2차원 배열 입력 받기
    arr = [list(map(int, input().split())) for _ in range(5)]
    # 각 요소에서의 이웃한 요소와의 차의 절대값의 전체 합을 담을 변수
    total = 0
    for i in range(5):
        for j in range(5):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                # 상하좌우 중에 이차원 배열을 벗어나는 인덱스를 갖게 되는 경우, 혹은 인덱스가 -1인 경우가 아닐 때만 실행
                if 0 <= nr < 5 and 0 <= nc < 5:
                    dif = arr[nr][nc] - arr[i][j]
                    # 절대값을 구해야하므로 음수이면 -1을 곱한다.
                    if dif < 0:
                        dif = -dif
                    total += dif
    print('#%d %d' %(t, total))
```

+ 절대값의 구현에서 `n *= -1`보다는 `n = -n`이 메모리 절약에 좋다.







## 3. 검색

+ 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
+ 목적하는 탐색 키를 가진 항목을 찾는 것
  + 탐색 키: 자료를 구별하여 인식할 수 있는 키
+ 검색의 종류
  + **순차 검색**(sequential search)
  + **이진 검색**(binary search)
  + **인덱싱**(indexing)

### 3.1 순차 검색

+ 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  + 가장 간단하고 직관적인 검색 방법
  + 배열이나 연결 리스트 등 **순차구조**로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
  + 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우 **수행시간이 급격히 증가**

+ 2가지 경우
  + 정렬되어 있지 않은 경우
  + 정렬되어 있는 경우

#### 3.1.1 검색 과정

+ 첫 번재 원소부터 순서대로 **검색 대상**과 **키 값**이 같은 원소가 있는지 비교하며 찾는다.

+ 키 값이 동일한 원소를 찾으면 그 원소의 **인덱스를 반환**한다.

+ 자료구조의 **마지막**에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

  

#### 3.1.2 정렬되어 있지 않은 경우

+ 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
  + 첫 번째 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번 비교
  + 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수
    + = (1/n)*(1+2+3+4+5+...+n) = (n+1)/2
  + 시간 복잡도: O(n)

+ 구현 예

```python
def sequentialSearch(a, b, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n:
        retun i
    else:
        reutrn '못찾음'
        
# for문
def sequentialSearch(a, b, key):
    for i in range(len(a)):
        if key == arr[i]:
            return i
    else: # return이라 안써줘도 되긴 함
    	return '못찾음'
```



#### 3.1.3 정렬되어 있는 경우

+ 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정하자.
+ 자료를 순차적으로 검색하면서 키 값을 비교하여, **원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것**이므로 더 이상 검색하지 않고 검색을 종료한다.
+ 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
  + 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어든다.
  + 시간 복잡도: O(n)
+ 구현 예

```python
def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return '못찾음'
    
# for문
def sequentialSearch2(a, n, key):
    for i in range(len(a)):
        if key == arr[i]:
            return i
        elif key < arr[i]:
            return '%d까지만 찾음' % i
    else:
        return '못찾음'
```





### 3.2 이진 검색

+ 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속하는 방법
  + 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가며 빠르게 검색을 수행
+ 이진 검색을 하기 위해서는 **자료가 정렬된 상태**여야 한다. (중요)

#### 3.2.1 검색 과정

+ 자료의 **중앙**에 있는 원소를 고른다.
+ 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
+ 목표 값이 **중앙 원소의 값보다 작으면 자료의 왼쪽 반**에 대해서 새로 검색을 수행하고, **크다면 자료의 오른쪽 반**에 대해서 새로 검색을 수행한다.
+ 위 세 단계 과정을 찾고자 하는 값을 찾을 때까지 반복한다.



#### 3.2.2 구현

+ 검색 범위의 **시작점**과 **종료점**을 이용하여 검색을 반복 수행한다.
+ 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 **정렬 상태**로 유지하는 추가 작업이 필요하다.

```python
def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start+end) // 2
        if a[middle] == key: # 검색 성공
            return middle
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return '검색 실패'
```

+ 재귀 함수 이용
  + 위와 같은 코드를 아래와 같이 재귀를 이용하여 이진 검색을 구현할 수 있다.

```python
def binarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low+high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, high, key)
```

+ 시간 복잡도: O(logn)





### 3.3 셀렉션 알고리즘

+ 저장되어 있는 자료로부터 **k번째로 큰 혹은 작은 원소를 찾는 방법**을 셀렉션 알고리즘이라 한다.
  + **최소값**, **최대값** 혹은 **중간값**을 찾는 알고리즘을 의미하기도 한다.
+ 선택 과정
  + 셀렉션은 아래와 같은 과정을 통해 이루어진다.
    + **정렬 알고리즘을 이용하여 자료 정렬하기**
    + **원하는 순서에 있는 원소 가져오기**

#### 3.3.1 일반적인 셀렉션 알고리즘

+ 아래는 k번째로 작은 원소를 찾는 알고리즘
  + 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환한다.
  + k가 비교적 작을 때 유용하며 O(kn)의 수행시간을 필요로 한다.

```python
def select(list, k):
    for i in range(0, k):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list[k-1]
```



### 3.3.2 선택 정렬

+ 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
  + 앞서 살펴본 셀렉션 알고리즘을 전체 자료에 적용한 것이다.
+ 정렬 과정
  + 주어진 리스트 중에서 **최소값**을 찾는다.
  + 그 값을 리스트의 **맨 앞에 위치한 값과 교환**한다.
  + 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
+ 시간 복잡도: O(n^2)

```python
def selectionSort(a):
    for i in range(0, len(a)-1): # 맨 마지막은 할 필요가 없다.
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
```





### 3.4 연습문제

2차원 배열 달팽이 정렬

+ 전치행렬 만드는법

```python
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9. 10, 11, 12], [13, 14, 15, 16]]
for x in zip(*a):
    print(x)
# 1, 5, 9, 13
# 2, 6, 10, 14
# 3, 7, 11, 15
# 4, 8, 12, 16
```

+ 4*4 배열

4 -> 3 -> 3-> 2 -> 2- > 1-> 1

+ 5*5 배열

5 -> 4 -> 4 -> 3 -> 3 -> 2 -> 2 -> 1 -> 1

+ 반복 횟수: N*2-1

```python
# 우, 하, 좌, 상
drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    drc_index = 0
    cnt = 1
    # 전체 규칙에 맞추기 위해서는 첫 시작도 델타를 통해 이동해 온 것이어야 한다.
    # 모든 시작은 전부 우측으로 이동하므로 첫 열을 -1로 설정해 처음 시행에서 0이되게 한다.
    r, c = 0, -1
    for i in range(N*2-1):
        # i마다 drc[drc_index % 4]의 쪽으로 N-((i+1)//2) 만큼 간다. i마다 drc_index는 1씩 올라야 한다.
        # 1칸 움직일 때마다 cnt는 1씩 오른다. r이나 c도 drc_index에 따라 1만큼 변화한다.
        for j in range(N-((i+1)//2)):
            r += drc[drc_index%4][0]
            c += drc[drc_index%4][1]
            arr[r][c] = cnt
            cnt += 1
        drc_index += 1
    print('#%d' % t)
    for i in range(N):
        print(*arr[i])
```

