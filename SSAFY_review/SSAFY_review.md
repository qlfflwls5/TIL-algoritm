# SSAFY_review

> SSAFY 과정에서 SWEA 홈페이지의 문제를 푼 것에 대한 리뷰
>
> 혼자서 문제를 과정 자체가 수업이므로 대부분 나의 코드이다.

<br/>

<br/>

## 2021-02-14

+ 싸피 Day01의 알고리즘 문제들을 복습하였다.
+ **babgin, Counting정렬, gravity, view, 순열반복문, 숫자를 정렬하자, 쉬운 거스름돈**
+ **Bubble Sort, Counting Sort, 완전 탐색, 탐욕 알고리즘**을 배웠다.
+ 버블 정렬

```python
def BubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```

+ 카운팅 정렬

```python
def CountingSort(arr, temp, k):
	# arr은 정렬할 리스트
    # temp는 정렬할 리스트의 길이를 갖는 빈 리스트/arr의 복사본
    # k는 arr에서의 최대값
    # C는 카운트 리스트
    C = [0] * (k+1)
    for i in range(len(arr)):
        C[arr[i]] += 1
    
    for i in range(1, len(C)):
        C[i] += C[i-1]
    
    for i in range(len(temp), -1, -1):
        temp[C[arr[i]]-1] = arr[i]
        C[arr[i]] -= 1
```

+ 완전 탐색

```python
# 예) {1, 2, 3}을 포함하는 모든 순열을 생성하는 코드(중복 없이)
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i2 and i3 != i1:
                    print(i1, i2, i3)
```

+ 탐욕 알고리즘
  + 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행해 최종적인 해답에 도달
+ 느낀점 및 배운 것들
  + **정렬 알고리즘**은 하나만 알아서는 안되고 상황에 따라 알맞는 것을 사용해야 한다. 다 익숙해지자
  + 아직까지 탐욕 알고리즘은 무엇을 의미하는 것인지 잘 와닿지 않는다.

<br/>

## 2021-02-17

+ 싸피 Day02의 알고리즘 문제들을 복습하였다.
+ **flatten, min/max구하기, 구간합, 소인수분해, 숫자카드, 전기버스, 현주의 상자 바꾸기**
+ **min, max 구현, 슬라이딩 윈도우, 카운트 리스트 활용** 등을 배웠다.
+ min, max의 경우 크게 어렵지 않았다. 초기값만 잘 설정한다면 이후는 단순 크기 비교 후 대입의 문제다.
+ 슬라이딩 윈도우의 경우 발상의 전환이 필요하였다. 구간합을 구하는 방법은 두 가지가 있다.

```python
# 구간합 구하기
# arr = 배열, N = arr의 길이, K = 구간의 길이

# 1
# 슬라이딩 윈도우를 활용하지 않고 정말 구간합을 구하기
for i in range(N-K+1):
    range_sum = 0
    for j in range(K):
        range_sum += arr[i+j]
    
    range_sum # 활용
    
# 2
# 슬라이딩 윈도우를 이용해 구간합 구하기
# 나가는 것은 빼고 들어오는 것은 더하는 방식
# 구간합의 초기값을 구하는 작업이 먼저 필요하다.
for i in range(M):
    range_sum += arr[i]
    
for i in range(N-K+1):
    range_sum += arr[i+M-1] - arr[i-1]
    range_sum # 활용
    
# 1의 경우 이중 for문으로 시간복잡도가 커질 수 있다.
# 2의 경우 for문을 두 번 사용하였지만 전부 1단 for문이다.
```

+ **카운트 리스트**의 활용은 **배열**의 문제를 푸는 데에 있어 매우 효과적이다.
  + 특히, **인덱스와 값을 동시에 활용해야 하는 경우**에 매우 강력하다.

```python
arr = [10, 7, 5, 6, 4, 1, 3, 6, 5, 2, 7, 2, 3, 4, 1, 10, 9, 8, 7]
cnt_arr = [0] * (max(arr)+1) # 카운트 리스트는 0번째부터 시작하므로 arr의 최대값 +1 길이만큼 만든다.
for i in range(len(arr)):
    # 각 arr의 요소에 대해 해당 요소 자체가 카운트 리스트의 인덱스가 되고, 해당 인덱스의 카운트 리스트 값을 1씩 증가시킨다.
    cnt_arr[arr[i]] += 1
    
# 이렇게 완성된 카운트 리스트는 최대값, 최소값 문제나 카운팅 정렬 등에 활용되며 여러 역할을 할 수 있다.
```

<br/>

## 2021-02-20

+ 싸피 Day03의 알고리즘 문제들을 복습하였다.
+ **두 개의 숫자열, 삼성시의 버스 노선**
+ **슬라이딩 윈도우, 카운트 리스트 활용** 등을 더 배웠다.
+ **횟수, 높이** 등을 묻는 문제에서 **주어진 조건**을 잘보자. **카운트 리스트의 길이**를 파악할 수 있다.
+ 주어진 입력의 순서대로 코드를 처리할 수 있는지를 파악하자. 모든걸 다 저장해놓고 쓰려하지 마라.

<br/>

## 2021-02-21

+ 싸피 Day04의 알고리즘 문제들을 복습하였다.
+ **2차원 배열_델타 검색, sum, 달팽이 숫자, 부분집합**
+ **2차원 배열, 델타 검색, 모든 부분집합 검색** 등을 배웠다.
+ 2차원 배열을 행으로, 열로 자유롭게 다룰 수 있을 때까지 익숙해지는 것이 좋겠다.
+ **델타 검색**의 경우 `drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]`로 설정하는 것이 보통 유용하다.
  + 상, 하, 좌, 우 중 여러 개에 대한 작업을 해야할 때 사용한다.
+ 한 리스트에 대해 **모든 부분집합**을 찾는 방법은 다음과 같다.
  + **비트 연산**을 활용한다.

```python
# arr이 리스트
N = len(arr)
for i in range(1 << N): # i는 0~2^N까지 순회한다. 길이가 N인 집합의 부분집합 개수는 2^N개이다.
    sub_arr = []
    for j in range(N):
        if i & (j << N): # i를 이진수로 표현한 것에 1이 j번째(i의 끝부터)에 있는지 확인하는 것이다.
            sub_arr += [arr[j]] # ex) i의 이진수 표현이 01101일 때 j가 0, 2, 3일 때 1이 있다.
            					# 이때, j번째 요소들이 부분집합의 요소들이 된다.
```

+ 느낀점 및 배운점
  + **나에게 매우 중요한 부분**
    + 달팽이 숫자나 이전의 전기 버스와 같은 경우 나의 풀이법은 항상 '현재 위치에서 어느 규칙을 갖는가'에 집중되어 있었다. => 너무 비효율적일 수 있다.
    + 이보다는 **전체적으로 보았을 때 어떠한 규칙이 성립하는가**를 항상 우선적으로 쳐다보는 것이 좋겠다. 너무 시야가 좁아지지 말자.

<br/>

## 2021-02-21(2)

+ 싸피 Day05의 알고리즘 문제들을 복습하였다.
+ **ladder1, 부분집합의 합, 색칠하기, 어디에 단어가 들어갈 수 있을까, 이진탐색, 특별한 정렬, 파리 퇴치**
+ **비트 연산 활용, 부분집합의 합, 이진탐색, 선택정렬, 2차원 배열** 등에 대해 배웠다.
+ 비트 연산의 경우 **분기**나 **switch**의 역할로 활용하기 매우 좋음을 깨달았다.
  + ex) `3 & 1 = 1`, `3 & 2 = 2`, `3 & 1 & 2 = 0`을 활용하여 두 조건이 모두 만족하는지 한 쪽만 만족하는지 등을 판별할 수 있다.
+ 이중 배열을 만들 때는 **얕은 복사**의 개념에 대해 항상 유의를 하여야 한다.
+ 부분집합의 합

```python
# 1~12까지의 숫자 중에서 길이가 N이고 합이 K인 부분집합 찾기

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

+ **1~n까지의 숫자에서 부분집합을 따질 때, 부분집합의 길이와 합을 한꺼번에 효율적으로 구할 수 있다!**

```python
sums = [(0, 0)] # 초기값
for num in range(1, N+1):
    sums += [(_cnt+1, _sum+num) for _cnt, _sum in sums]
    # sums는 1부터 N까지의 숫자 리스트의 모든 부분집합의 개수와 합의 쌍을 요소로 갖는다.
```

+ 길이에 따라 부분집합을 나눠서 저장하고 싶을 때

```python
# 예를 들어, lst[1] = [[1], [2], [3] , ... [12]]
# lst[2] = [[1, 2], [1, 3], [1, 4], ... [11, 12]]
lst = [[]*13] # 사전에 미리 제일 긴 부분집합의 길이 + 1개 만큼의 빈 이중배열을 만든다.
lst[len(sub_lst)] += sub_lst # 부분집합을 구한 후 이런식으로 lst에 저장한다.
```

+ 이진 탐색
  + 무조건 정렬되어 있는 시퀀스에 대해서만 가능하다.
  + 중간값을 찾은 후 목표값과 비교하여 중간값을 기준으로 목표값이 있는 쪽만 탐색을 반복하는 알고리즘

```python
# P = 시퀀스, key = 목표값
def binarySearch(P, key):
    start, end = 0, len(P)-1
    while start <= end:
        middle = (start+end)//2
        if middle == key:
            return middle # 목표값의 인덱스를 반환
        elif middle > key:
            end = middle - 1 # middle이 목표값보다 크면 middle 이전부터 다시 탐색
        else:
            start = middle + 1 # middle이 목표값보다 작으면 middle 이후부터 다시 탐색
    return False # 목표값이 없는 경우
```

+ 선택 정렬
  + 내가 원하는 만큼만 정렬을 시행할 수 있다.
  + 최대값, 최소값, 2번째로 큰 값, 2번째로 작은 값, n번째까지 큰/작은 값 등만 찾고싶을 때 유용하다.

```python
def selectionSort(arr):
    N = len(arr)
    for i in range(N):
        min_i = i # 오름차순 정렬을 예시로 하고 있다.
        for j in range(i+1, N):
            if arr[min_i] > arr[j]:
                min_i = j
        
        arr[i], arr[min_i] = arr[min_i], arr[i] # i번째의 값과 i번째 이후의 최소값을 바꾼다.
```

+ 느낀점 및 배운점

  + 대부분의 문제는 막힘없이 풀었으나, 사다리타기의 문제에서 매우 고난을 겪었다.
  + 저번의 느낀점이 똑같은 문제점이었다. **전체적인 규칙이 아닌, 개별 칸에 대한 규칙을 찾으려 했다.**

  + 개별적인 규칙을 찾으려다 보면 **시작과 끝에서 규칙의 예외**가 발생하는 경우가 많다.
  + 따라서, 전체적으로 적용이 가능한 규칙을 찾거나, **패딩**을 넣어주는 것이 좋은 방법이다.

<br/>

## 2021-02-21(3)

+ 싸피 Day06의 알고리즘 문제들을 복습하였다.
+ **GNS, itoa, String, 고지식한 패턴 검색 알고리즘, 문자열 뒤집기**
+ **문자열, Brute force, itoa/atoi** 등을 배웠다.
+ 문자열을 활용한 문제로는 **문자열 내 패턴 찾기**, **회문 찾기**, **문자열 뒤집기**, **숫자로 변환하기** 등이 있다.
+ 패턴과 관련한 문제에는 **Brute force**, **KMP** 방식을 사용할 수 있다. KMP는 아직 제대로 배우지 않았다.

```python
# Brute Force

# while문
# T = 문자열, P = 패턴
def bruteForce(T, p):
    N = len(T)
    M = len(P)
    i = 0 # 문자열의 인덱스
    j = 0 # 패턴의 인덱스
    
    while i < N and  j < M:
        if T[i] != p[j]:
            # 만약 패턴이 다르다면 i를 반복의 마지막에 패턴 검사 시작 인덱스로 갈 수 있도록 맞춤
            i = i - j
            # 만약 패턴이 다르다면 j를 반복의 마지막에 0이 되도록 -1로 맞춤
            j = -1
        i += 1
        j += 1
    
    # 패턴을 찾아서 검색이 끝났을 때 j의 인덱스는 M이 되어있다. 마지막 인덱스에서 j += 1을 하며 끝나므로
    if j == M:
        return i # 패턴이 시작하는 인덱스
    else:
        return False # 패턴 못찾음
    
    
#  for문
def bruteForce(T, p):
    N = len(T)
    M = len(P)
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if T[i+j] != p[j]:
                break
            else:
                cnt += 1
         if cnt == M:
            return i
    return False
```

+ atoi/itoa
  + atoi: 문자에서 숫자로 바꾸기
  + itoa: 숫자에서 문자로 바꾸기

```python
# 둘 다 모두 ASCII코드를 활용한다.
def atoi(num):
    value = 0
    for i in range(len(num)):
        value *= 10
        value += ord(num[i]) - ord('0')
    
    return value


def itoa(num):
    result = ''
    # 부호
    sign = ''
    if num < 0:
        num = -num
        sign = '-'
    while num > 0:
        result = chr(num%10 + ord('0')) + result
        num //= 10
    
    return sign + result
```

<br/>

## 2021-02-21(4)

+ 싸피 Day07의 알고리즘 문제들을 복습하였다.

+ **가장 빠른 문자열 타이핑, 글자수, 문자열 비교, 쇠막대기 자르기, 회문 찾기, 회문2**

+ **string, 패턴 찾기, 2차원 배열에서의 회문** 등을 배웠다.

+ **글자수 세기** 같은 경우, **딕셔너리**를 사용하면 굉장히 간편하다.

  + `dict.fromkeys(arr, 초기값)`을 통해 쉽게 각 글자에 대한 딕셔너리를 만들자

+ **패턴 찾기**의 경우에도, **count 메서드**를 사용할 수 있다면 매우 간편하게 해결할 수 있다.

  + `if string.count(pattern): return 1`을 통해 count가 1이상이면 있다고 반환한다.

+ 이중 배열에서 회문 찾기의 경우, 회문을 검사하는 작업을 각 행과 각 열에서 실시한다고 생각하면 된다.

  회문의 길이(M)이 주어져 있는 경우

```python
def palindrome(row, N, M):
    result = ''
    for j in range(N-M+1):
        for k in range(M//2):
            if row[j+k] != row[j+M-1-k]:
                break
        else:
            result = ''.join(row[j:j + M])

    return result


T = int(input())
for t in range(1, T+1):
    # N = arr의 길이 M = 팰린드롬의 길이
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ''
    while not len(ans):
        for i in range(N):
            ans = palindrome(arr[i], N, M) + palindrome(list(zip(*arr))[i], N, M)
            if ans:
                break

    print('#%d %s' %(t, ans))
```

​	회문의 길이가 주어져 있지 않은 경우

```python
# 일반적인 풀이
def my_find(M):
    # 전체크기가 N이다.
    for i in range(N):
        for j in range(N - M + 1):
            # 스왑 통한 회문 검사
            # 가로 검사
            for k in range(M // 2):
                # 앞뒤검사
                if words[i][j + k] != words[i][j + M - 1 - k]:
                    break
                # 회문임
                elif k == M // 2 - 1:
                    return M
            # 세로 검사
            for k in range(M // 2):
                if words[j + k][i] != words[j + M - 1 - k][i]:
                    break
                elif k == M // 2 - 1:
                    return M
    return 0


for _ in range(10):
    tc_num = int(input())

    N = 100
    words = [input() for i in range(N)]

    # 가장 길이가 긴 회문부터 검사를 한다.
    for i in range(N, 0, -1):
        ans = my_find(i)

        if ans:
            break

    print('#{} {}'.format(tc_num, ans))
    
    
# 속도가 빠른 내 풀이
# 풀이한 논리
# 팰린드롬은 결국 '중심 문자'로부터 양옆으로 뻗어져나갈 때 양옆이 같은 문자열이다. (중심 문자에 대한 정의는 center_palindrome함수 내에 있다)
# 그러므로, 중심 문자를 구하는 부분과 그를 기준으로 양옆으로 뻗어져 나가며 팰린드롬을 구하는 부분으로 나뉘어 작동하는 방식이다.

# 한 문자열, 문자열의 길이, 팰린드롬을 검사할 인덱스를 인자로 받는다.
def center_palindrome(string, N, i):
    # 이하 center는 현재 i번째의 문자이며 '중심 문자'란 center가 반복되는 총 문자를 말한다. 예를 들어, 'ABBBA'에 i가 2라면 center는 'B', 중심 문자는 'BBB'이다.
    center = string[i]
    # center의 양 옆에서 시작, temp_i는 왼쪽으로 나아갈 것이고 temp_j는 오른쪽으로 나아갈 것이며, temp_len은 중심 문자의 총 길이다.
    temp_i, temp_j, temp_len = i - 1, i + 1, 1
    # 나아가다 끝에 도달하면 더 이상 나아가지 말아야 하므로 각각 temp_i와 temp_j의 플래그를 만든다. temp_i는 0에, temp_j는 N-1에 도달하면 끝까지 간 것이다.
    is_i_end, is_j_end = 0, 0
    while True:
        # 중심 문자의 왼쪽 문자(string[temp_i])가 center와 같다면 중심 문자의 길이를 1 늘리고 temp_i를 왼쪽 칸으로 옮긴다.
        if string[temp_i] == center and not is_i_end:
            # temp_i가 0이면서 0번째 문자가 center와 같다면 중심 문자의 길이만 1 늘려주고 is_i_end를 1로 바꿔 이후 temp_i에 대한 작업은 종료한다.
            if temp_i == 0:
                is_i_end = 1
                temp_len += 1
            else:
                temp_i -= 1
                temp_len += 1
        # 중심 문자의 오른쪽 문자(string[temp_j)가 center와 같다면 중심 문자의 길이를 1 늘리고 temp_j를 오른쪽 칸으로 옮긴다.
        if string[temp_j] == center and not is_j_end:
            # temp_j가 N-1이면서 N-1번째 문자가 center와 같다면 중심 문자의 길이만 1 늘려주고 is_j_end를 1로 바꿔 이후 temp_j에 대한 작업은 종료한다.
            if temp_j == N-1:
                is_j_end = 1
                temp_len += 1
            else:
                temp_j += 1
                temp_len += 1
        # 매 temp_i, temp_j에 대한 작업에서 중심 문자의 탐색이 끝나는 세 가지 경우의 수가 있다. 양 끝에 도달하지 않은 채로 끝난 경우, 한 쪽이 끝에 도달해서 끝난 경우
        # 전자의 경우 현재 temp_i와 temp_j번째 문자가 center와 다른 경우이다. 예) ABBBA에서 temp_i, temp_j는 각각 왼쪽 A, 오른쪽 A의 인덱스가 된다.
        # 후자의 경우 끝에 도달하지 않은 쪽의 문자가 center와 다른 경우이다. 예) ABBBB에서 temp_i는 A의 인덱스가 되고, BBBBA라면 temp_j는 A의 인덱스가 된다.
        # 각 경우에서 temp_i가 중심 문자의 시작, temp_j가 중심문자의 끝 번째가 되도록 조정한다.
        if string[temp_i] != center and string[temp_j] != center:
            temp_i += 1
            temp_j -= 1
            break
        elif temp_i == 0 and string[temp_j] != center:
            temp_j -= 1
            break
        elif temp_j == N-1 and string[temp_i] != center:
            temp_i += 1
            break

    return temp_i, temp_j, temp_len


# 중심 문자로부터 양옆으로 뻗어나가 팰린드롬을 검사할 함수
def max_palindrome(string):
    N = len(string)
    max_len = 0
    i = 1
    while i < N-1:
        temp_i, temp_j, temp_len = center_palindrome(string, N, i)
        # i를 중심 문자의 + 1번째로 계속 이동한다. 불필요한 반복을 줄일 수 있다.
        # 예) BBBABC가 있을 때, 첫 번째 B에서의 팰린드롬 검사를 실시했다면, 이후 중심 문자 내 연속되는 B에서는 검사를 안해도 된다. 다음 검사는 A부터 한다.
        i = temp_j + 1

        while 0 < temp_i and temp_j < N - 1:
            temp_i -= 1
            temp_j += 1
            if string[temp_i] != string[temp_j]:
                break
            temp_len += 2

        if max_len < temp_len:
            max_len = temp_len

    return max_len


for t in range(1, 11):
    n = int(input())
    arr_row = [input() for _ in range(100)]
    max_result = 0
    # 입력으로 받은 이중배열과 열 기준으로 바꾼 이중배열을 하나씩 가져와서
    for arr in arr_row, zip(*arr_row):
        # 해당 이중배열의 문자열을 하나씩 가져와서 가장 긴 팰린드롬의 길이를 구하기
        for string in arr:
            temp_result = max_palindrome(string)
            if max_result < temp_result:
                max_result = temp_result

    print('#%d %d' % (t, max_result))
```

+ 쇠막대기 자르기 문제는 매우 재밌는 문제였는데, 이런 문제일수록 규칙을 찾아내는 것이 중요하다.
+ 느낀점 및 배운점
  + 이중 배열에서의 회문찾기가 매우 어려웠다.
  + 특히, 회문의 길이가 정해져있지 않은 경우, **나는 조금 색다른 풀이를 하였는데** 이 방법은 회문의 길이가 짧을수록 효율이 좋으며, 회문의 길이가 길다하더라고 일반적인 방법보다 조금 비효율적이므로 평균적으로 효율적인 코드라고 할 수 있다.

<br/>

## 2021-02-21(5)

+ 싸피 Day08의 알고리즘 문제들을 복습하였다.
+ **숫자 배열 회전, 어디에 단어가 들어갈 수 있을까, 의석이의 세로로 말해요**
+ 2차원 배열의 회전, 각 행의 길이가 다른 2차원 배열 등을 배웠다.
+ 2차원 배열의 회전과 같은 경우 두 가지 풀이가 있을 수 있다.
  + 정말 배열을 회전시키기
  + 배열이 회전되었을 때에 값이 어디로 이동하는지를 파악해 인덱싱을 이용해 값만 빼오기

```python
# 숫자 배열 회전 문제

# 배열 자체를 회전시키는 풀이
# 배열을 90도 회전시키는 함수
def shift90(arr):
    # 이중 배열은 깊은 복사가 힘들기때문에 아예 새로운 배열을 만들어 버린다.
    new_arr = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_arr[c][N - r - 1] = arr[r][c]
    return new_arr


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    nums = [list(map(int, input().split())) for _ in range(N)]

    num_90 = shift90(nums)
    num_180 = shift90(num_90)
    num_270 = shift90(num_180)

    print('#%d' % tc)
    for i in range(N):
        print(''.join(map(str, num_90[i])), ''.join(map(str, num_180[i])), ''.join(map(str, num_270[i])))
        
  
# 회전되었을 때의 값만 빼오는 풀이
T = int(input())
for t in range(1, T+1):
    N = int(input())
    print('#%d' % t)
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 진짜로 90도, 180도, 270도 돌리지 말고 각 행에 출력되는 값을 어떻게 뽑아올 수 있는지 생각해보자
    # 각 i번째 행에 대하여 90도로 돌린 i번째 행, 180도로 돌린 i번째 행, 270도로 돌린 i번째 행을 출력하면 되는 것이다.
    # 즉, 90도 180도 270도 돌리면 각각 어느 요소가 어디로 이동하는지의 규칙을 찾으면 된다.
    for i in range(N):
        result = ''
        for j in range(N):
            result += str(arr[N-j-1][i])
        result += ' '
        for j in range(N):
            result += str(arr[N-i-1][N-j-1])
        result += ' '
        for j in range(N):
            result += str(arr[j][N-i-1])

        print(result)
```

+ 행의 길이가 서로 다를 때 열을 읽는 방법에는 다음과 같은 방법이 있다.
  + 제일 긴 행을 기준으로 하여 짧은 행들이 그 길이에 맞춰질 때까지 공백 데이터를 추가
  + 제일 긴 행의 길이를 갖는 리스트를 만들어 리스트 인덱스에 대응하는 행의 값들을 가져오기

```python
# 제일 긴 행을 기준으로 하여 짧은 행들이 그 길이에 맞춰질 때까지 공백 데이터를 추가 
T = int(input())
for t in range(1, T+1):
    N = 5
    data_arr = [list(input()) for _ in range(N)]
    
    # 가장 긴 길이를 찾는다. data_arr을 가장 긴 길이 * 가장 긴 길이 형태로 만들기 위해
    max_i = 0
    for i in range(N):
        if len(data_arr[max_i]) < len(data_arr[i]):
            max_i = i

    # 모든 row에 대하여 길이가 가장 긴 것에 맞춰질 때까지 공백을 삽입한다.
    for data in data_arr:
        while len(data) < len(data_arr[max_i]):
            data += ['']

    # 세로로 읽어와 result에 저장한다.
    result = ''
    for col in zip(*data_arr):
        for i in range(N):
            result += col[i]

    print('#%d %s' %(t, result))
    
    
# 제일 긴 행의 길이를 갖는 리스트를 만들어 리스트 인덱스에 대응하는 행의 값들을 가져오기
for t in range(1, int(input())+1):
    # 어차피 주어지는 글자는 15자 이하라고 하였다.
    result = ['']*15
    for _ in range(5):
        word = input()
        for i in range(len(word)):
            # result의 i번째에 각 줄의 i번째 문자가 차례로 들어간다!
            result[i] += word[i]

    print('#%s %s' % (t, ''.join(result)))
```

<br/>

## 2021-02-26

+ 싸피 Day09의 알고리즘 문제들을 복습하였다.

+ **괄호 검사, 그래프를 저장하는 법, 재귀-피보나치, 파스칼의 삼각형**

+ **스택, 인접행렬, 인접리스트, 재귀** 등의 알고리즘적 기법들을 사용해야 하는 문제들이었다.

+ DFS를 배우기 위한 전초 작업으로써 스택을 자세히 배우고, 주어지는 정점과 간선을 이용해 인접행렬과 인접리스트를 만드는 법을 배웠다.

+ 재귀는 개념은 알아도 그것이 실제로 어떻게 작동을 하는지 가늠하기가 매우 어려웠다.

+ 느낀점 및 배운점

  + 앞으로 재귀에서 발목이 많이 잡힐 것 같다.


<br/>

## 2021-03-06

+ 싸피 Day10의 알고리즘 문제들을 복습하였다.
+ **그래프 경로, 길찾기, 반복문자 지우기, 백만장자 프로젝트, 비밀번호, 종이 붙이기**
+ **스택, DFS, DP 맛보기** 등의 알고리즘적 기법들을 사용해야 하는 문제들이었다.
+ 이제부터 슬슬 여러 답 속에 진정한 답이 숨어져 있는 문제들이 자주 등장하는 것 같다.
  + 다른 시각에서 풀었을 때 / 내가 보조 자료를 만들어냈을 때 훨씬 효율적이고 쉬운 코딩이 가능한 문제

+ 느낀점 및 배운점
  + 스택과 기본적인 DFS를 알고 있으면 풀이가 가능한 문제들이었다.
  + 이정도의 기본 스택, DFS 사용 문제는 어렵지 않다.

<br/>

## 2021-04-06(2)

+ 싸피 Day17의 알고리즘 문제들을 복습하였다.
+ **트리의 전위순회, 중위순회, 이진탐색트리 생성, 이진탐색트리 연산연습**
+ **트리, 이진트리**에 관한 문제들이었다.
+ DFS, BFS를 넘어 트리라는 새로운 주제로 들어서서 싸피 알고리즘 학습 내용을 다시 리뷰하기 시작했다.
+ 트리의 순회

```python
def preorder_travers(node):
    way.append(node) # 전위순회
    if len(tree[node]) >= 3:
        preorder_travers(tree[node][2])
    # way.append(node) 중위순회
    if len(tree[node]) == 4:
        preorder_travers(tree[node][3])
    # way.append(node) 후위순회


V = int(input()) # 노드 개수
E = list(map(int, input().split())) # 간선 정보
# 확장 문제에서의 활용을 위해 tree가 담는 정보는 현재 노드, 부모 노드, 왼쪽 자식 노드, 오른쪽 자식 노드
tree = [[i, 0] for i in range(V+1)]
for i in range(0, len(E), 2):
    # 자식
    tree[E[i]].append(E[i+1])
    # 부모
    tree[E[i+1]][1] = E[i]

root = 0
for i in range(1, V+1):
    if tree[i][1] == 0:
        root = i

way = []
preorder_travers(root)
print('-'.join(map(str, way)))
```

+ 이진탐색트리
  + 코드가 굉장히 길고 내용이 어렵다. README에 전부 리뷰하기에는 양이 많으므로 코드로만 남겨놓겠다.

+ 느낀점 및 배운점
  + 기본적인 트리에 대한 내용을 배웠고, 이진트리에서 내가 원하는 곳으로 이동하는 방법들을 배웠다.
  + 부모 노드와 자식 노드를 자유롭게 왔다갔다 할 수 있도록 연습해야겠다.

<br/>

## 2021-04-06(3)

+ 싸피 Day18의 알고리즘 문제들을 복습하였다.

+ **서브트리, 이진탐색, 이진 힙, 노드의 합, 사칙연산**

+ **이진트리**에 관한 문제들이었다.

+ 이진트리는 각 노드가 가지는 정보가 **왼쪽 자식 노드, 오른쪽 자식 노드, 자신, 부모 노드**라는 것만 인지하면 생각보다 많이 어렵지는 않았다.

  + 또한 이를 활용해서 코드를 굉장히 간단하게 짤 수 있었고, 필요한 정보만을 내가 취하면 되기 때문에 동기들에 비해 내 코드가 **월등히 짧았다.**
  + 덕분에 수업 중에도 참신한 아이디어로 자주 언급이 되었다.

+ **완전 이진트리**에서 각 노드가 가지는 값만을 사용하여 해결해도 되는 문제라면, 복잡하게 노드에 자식 노드와 부모 노드의 정보를 담을 필요가 없다.

  + **완전 이진트리의 특성인 부모 노드와 자식 노드의 관계**를 사용한다.

    + 부모 노드의 번호가 N이라면 왼쪽 자식 노드는 2*N, 오른쪽 자식 노드는 2\*N+1이다.

  + 이를 통해 리프 노드부터 시작해서 문제를 풀어야 하는 경우, 노드의 값만 취하면 되는 경우와 같을 때에 매우 간단하게 해결할 수 있다.

  + 예시로 완전 이진 트리의 리프 노드에 자연수들이 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있을 때 L번 노드의 값을 구하는 코드는 아래와 같이 간단히 해결할 수 있다.

  + ```python
    for t in range(1, int(input())+1):
        N, M, L = map(int, input().split())
        # 일단 모든 트리의 노드의 값은 0으로 초기화한다.
        tree = [0] * (N+1)
        for _ in range(M):
            # 리프 노드 번호와 값을 입력받는다.
            node, v = map(int, input().split())
            tree[node] = v
    
        for i in range(N, 0, -1):
            # 부모 노드의 값에 자식 노드의 값을 더한다.
            tree[i//2] += tree[i]
    
        print('#%d %d' % (t, tree[L]))
    ```

+ 느낀점 및 배운점

  + 이진 트리를 배우며 링크드 리스트라는 개념도 함께 접했는데, 우리는 링크드 리스트라는 것을 구현하지는 않았다. `Class`를 사용하여 생성하는 것 같으므로, 연습해봐야 할 것 같다.
  + 사실 파이썬에서는 리스트를 사용해서 left와 right를 전부 편하게 구현할 수 있기 때문인 것 같다.
  + 트리의 구조에서 노드에 접근하는 방법이 다양한만큼, 동기들의 답안이 가지각색이었다. 많은 코드를 앞으로도 계속 해석하고 뜯어봐야겠다.
    + 코드가 다양할수록 더욱 더 승부욕이 붙는다. 이번 트리에서는 내 코드가 가장 짧고 효율적이고 좋았다!

<br/>

## 2021-04-08

+ 싸피 Day19의 알고리즘 문제들을 복습하였다.
+ **Merge Sort**
+ **합병정렬**에 대해 배웠다.
+ 합병정렬은 주어진 배열을 각 하나가 될 때까지 반으로 자르다가 하나가 되면 다시 역으로 돌아오면서 합병을 하며 정렬을 하는 알고리즘이다.
  + 합병정렬의 메리트는 시간복잡도가 언제나 **O(nlogn)**이라는 것이다.
    + 반씩 잘라 내려가기 때문에 내려가는 깊이 logn이고, 한 deapth마다 진행하는 정렬의 방식이 2개를 합병하는 과정에서 한 쪽의 길이만큼 비교가 이루어지므로 최대 n의 비교가 일어난다고 가정한다.

```python
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
    temp = [] # a_arr, b_arr을 정렬하며 합쳐서 담을 temp
    ai = bi = 0
    # 한쪽의 조각을 temp에 다 담을 때까지
    while ai < len(a_arr) and bi < len(b_arr):
        if a_arr[ai] < b_arr[bi]:
            temp.append(a_arr[ai])
            ai += 1
        else:
            temp.append(b_arr[bi])
            bi += 1
    # 담지 못한 나머지 조각을 전부 temp에 붓기
    if ai == len(a_arr):
        temp.extend(b_arr[bi:])
    else:
        temp.extend(a_arr[ai:])

    return(temp)


a = [5, 1, 9, 6, 8, 4, 2, 3]
print(merge_sort(a))
```

+ 느낀점 및 배운점
  + 사실 예전에 정렬에 대해 이것저것 검색을 해보다가 합병정렬에 대해서 읽어 봤었다.
  + 그때는 버블정렬, 카운팅정렬, 선택정렬만 알고 있었던 상태라 이해가 잘 되지 않았었다.
    + 하지만, 트리를 배우고 나서 다시 새롭게 보니 이해가 아주 잘되었다.
    + 특히, 시간복잡도가 이해가 안되었는데 대략 이해가 가는 것 같다.
  + 합병정렬은 다른 정렬들이 최악의 경우에 훨씬 큰 시간복잡도를 가지게 될 수도 있는 불안성을 가지지 않는다는 장점이 있다. 합병정렬은 최악의 상황에도 O(nlogn)이기 때문에 앞으로 정렬이 있을 때 활용해보면 좋을 것 같다.

<br/>

## 2021-04-08 (2)

+ 싸피 Day20의 알고리즘 문제들을 복습하였다.
+ **트리 시각화**
+ **트리를 그래프로 출력**하는 알고리즘을 짜보았다.
+ 컴퓨팅 사고력을 배우면서 트리의 구조를 그래프로 출력하는 코드를 짜보았다. 
  + 코딩 상 한 줄씩 출력해야 하기 때문에 DFS의 느낌으로 구동이 되는 것 같다.

```python
def draw_tree(level, p, c):
    # 루트 노드
    if level == 0:
        print('[%s]' % c.zfill(3), end='')
        for node in tree[c]:
            draw_tree(level+1, c, node)
        return
	# 자식 노드가 1개 이상이라면 폴더 구조같이 잇기
    if len(tree[p]) > 1:
        if c == tree[p][0]:
            print('--+--[%s]' % c.zfill(3), end='')
        elif c == tree[p][-1]:
            print((2*level-1) * '     ', end='')
            print('  L--[%s]' % c.zfill(3), end='')
        else:
            print((2*level-1) * '     ', end='')
            print('  +--[%s]' % c.zfill(3), end='')
    # 자식 노드가 1개라면 일직선으로만 잇기
    elif len(tree[p]) == 1:
        print('-----[%s]' % c.zfill(3), end='')
	# 자식 노드가 없다면(리프 노드라면) 그래프를 끝내고 다음 줄 출력하기
    if not tree.get(c):
        print()
        return
    for node in tree[c]:
        draw_tree(level+1, c, node)


N = int(input())
tree = {}
e = list(input().split())
for i in range(N-1):
    tree[e[2*i]] = tree.get(e[2*i], []) + [e[2*i+1]]

draw_tree(0, 0, e[0])
```

```pseudocode
# 입력
10
30 54 30 2 30 45 54 1 45 123 45 7 1 3 123 6 123 9 123 11 45 100


# 결과
[030]--+--[054]-----[001]-----[003]
       +--[002]
       L--[045]--+--[123]--+--[006]
                           L--[009]
                 L--[007]
```

+ 느낀점 및 배운점
  + 트리라는 구조를 실제로 출력해봤는데, 굉장히 재밌었다.
  + print문의 인간승리인 것 같다. 사실 보기에 좋은 것 같지 않아서 다른 사람들의 코드도 있다면 참고해봐야 할 것 같다.
  + 그래도 잘 나오는 것 보니 만족한다!

<br/>

## 2021-04-13 (2)

+ 싸피 Day21의 알고리즘 문제들을 복습하였다.
+ **bit연산 연습문제1, 단순 2진 암호코드, 암호비트 연습문제, 진법 연습문제2**
+ **비트연산, 이진**의 기본에 대해 배웠다.
+ 파이썬에서는 `int(숫자로 된 문자열, 진수)`를 통해서 숫자로 된 문자열을 해당 진수의 숫자로 바꾼 값을 얻을 수 있다.
+ 파이썬에서는 `bin(숫자)`를 통해 이진수로 바꿀 수 있다.
+ 이진에서의 곱셈과 나눗셈 연산은 `>>`, `<<`의 쉬프트로 구현할 수 있다.
+ **n개의 1로된 이진수를 만드는 법(Mask_bits)**
  + `(1 << n) - 1`
  + 매우 중요하다. 마스크 비트와 `&`연산을 활용해서 이진의 원하는 부분만을 뽑아올 수 있다.

+ 느낀점 및 배운점
  + 어렵다... 비트연산과 이진수는 문과인 나로서는 너무 낯설었다.
  + 이후의 수업을 잘 들어보자...!

<br/>

## 2021-04-13 (3)

+ 싸피 Day22의 알고리즘 문제들을 복습하였다.

+ **마스크 비트, 암호코드 스캔, 이진수, 이진수 표현, 이진수2**

+ **비트연산, 이진**의 기본에 대해 배웠다.

+ 오늘 스터디에서 리뷰한 지옥의 문제 '암호코드 스캔'을 풀었다.

+ 마스크 비트 부분은 어려우면서도 중요한 것 같아 기본적인 개념 코드를 리뷰하겠다.

  + ```python
    # 16진수 2자리씩 끊어서 가져오기
    
    
    def get_number(num, i):
        # (1 << n) - 1 : n = 8일 때 0xff가 된다.
        mask_bits = (1 << 8) - 1
        return (num >> 8*i) & mask_bits
    
    
    a = 0x12345678
    for i in range(4):
        print('0x%X' % get_number(a, i))
        
    # 0x78
    # 0x56
    # 0x34
    # 0x12
    ```

+ 느낀점 및 배운점

  + 정보처리기사 자격증 스터디에서 CT에 관련된 내용을 학습 중인데, 2진수에 관련된 내용을 한 번 봐야할 것 같다. 아직은 많이 아리송하다.
  + 그래도 어떻게 D5난이도의 문제를 풀었다. 실력이 늘고 있는 것 같다!

<br/>

## 2021-04-15 (3)

+ 싸피 Day23의 알고리즘 문제들을 복습하였다.
+ **숫자를 정렬하자(선택 정렬 재귀), 최대 상금, baby-gin(brute-force)**
+ **선택 정렬, 완전 탐색** 등의 기법을 사용했다.
+ 완전 탐색을 구현하는 방법은 언제나 많다.
  + 조합, 순열, 부분집합을 잘 알아놓자.
+ 느낀점 및 배운점
  + 그래도 좀 무난한 수업이었다.

<br/>

## 2021-04-15 (4)

+ 싸피 Day24의 알고리즘 문제들을 복습하였다.
+ **최소합, 전자카트, 컨테이너 운반, 화물 도크, baby-gin(hard)**
+ **순열, 그리디, DP**의 기법을 사용했다.
+ 새로운 알고리즘 기법들에 접하기 시작한다.
  + 사실, 그리디랑 DP가 어렵고 까다롭다고 하는데, 나는 뭔가 재미있는 것 같다.
+ 이번 문제들도 무난무난하게 다 풀었다.
  + 꾸준히 푸는 속도나 효율성이 반에서도 상위권이라 다행이다.
+ 느낀점 및 배운점
  + 앞으로 DP를 많이 다루게 될 것 같은데, 재밌다고 느낀 만큼 열심히 해보자!
  + 그리디의 경우 최적해를 찾는 것이기 때문에 정렬이 꽤 많이 사용된다는 느낌을 받았다.

<br/>

## 2021-04-17

+ 싸피 Day25의 알고리즘 문제들을 복습하였다.

+ **정식이의 은행업무, 격자판의 숫자 이어 붙이기, 쉬운 거스름돈, 정사각형 방, 장훈이의 높은 선반**

+ **비트 연산, n진수, 완전 탐색, 그리디, DP**의 기법을 사용했다.

+ **정식이의 은행업무**에서는 비트 연산의 `^`를 실제로 어떻게 사용하는지 배울 수 있었다.

  + 이에 비트 연산의 용도를 정리해보았다.

  + | OP   | 용도                          | 효과                                                         |
    | ---- | ----------------------------- | ------------------------------------------------------------ |
    | &    | selective-clear               | mask bit가 0인 경우 clear, 1인 경우 유지                     |
    | \|   | selective-set                 | mask bit가 1인 경우 set, 0인 경우 유지                       |
    | ^    | selective-invert<br />compare | mask bit가 1인 경우 invert, 0인 경우 유지<br />mask bit가 같으면 0 다르면 1 |
    | ~    | invert                        | 1의 보수를 구할 때 사용(모두 반전)<br />2의 보수는 이진수의 음수이다.(1의 보수 + 1) |

+ **격자판 숫자 이어 붙이기**의 경우 재귀 함수에서 인자를 어떻게 넣을 것이냐를 다시 생각해보게 되었다.

  + 흔히, 재귀를 사용할 때 `level`이라는 인자를 사용해서 종료 조건을 만들어준다.
  + 이때, 문제를 정확히 이해를 해서 `level`의 시작과 끝을 잘 정해줘야 불필요한 depth를 만들지 않는다.
    + 이는 엄청난 시간 효율 차이를 가져온다.
  + **따라서, 무조건 `level`이 0으로 시작해야 할 필요도 없고, 재귀의 인자로 넘겨주는 누적 연산값도 0이나 빈 값으로 시작할 필요가 없다.**
    + **`level`은 1로, 누적 연산값(보통 S)은 시작에서의 연산 값을 넣고 시작하면 깊이를 1줄일 수 있다.**

+ **정사각형 방**과 **장훈이의 높은 선반**은 아이디어를 떠올리기가 너무 어려운 문제들이었다.

  + **정사각형 방**은 DFS의 느낌으로 풀었으나, 수업 답안에서는 cnt_list를 활용했다.
  + **장훈이의 높은 선반**은 DP처럼 보이는 문제지만 매 선택지를 골라야 하는 것은 아니기 때문에, 결국 완전 탐색의 문제다.

+ 느낀점 및 배운점

  + 오늘 문제들은 많이 어려웠다.
  + 전부 다시 문제를 처음부터 풀어보았고 많은 것을 깨달았다. 이 깨달음이 잊혀지지 않았으면 좋겠다.

<br/>

## 2021-04-19

+ 싸피 Day26의 알고리즘 문제들을 복습하였다.

  + 여기까지 쓰고 보니 사실 아카이빙 느낌으로 쭉 길게 이어 쓰고 싶어서 README를 이렇게 작성했지만 정리를 언젠가 해야될 것 같다. 이렇게 길어질 줄 몰랐다.
  + Django 프로젝트를 하고 싶은데 알고리즘이 너무 힘들어서 요즘 시간이 안난다.. 다음 주부터 웹 트랙으로 다시 돌아가면 정말 열심히 만들어보자..! 우선 알고리즘 리뷰!

+ **퀵 정렬, 병합 정렬, 트리 순회, powerset 만들기**

+ **분할 정복, 백트래킹, 트리, 조합**의 기법을 사용했다.

+ 퀵 정렬은 여러가지 방법으로 할 수 있지만, 우리 수업에서는 가장 간단하게 생각해낼 수 있는 것으로 정리했다. `pivot`을 배열의 가장 끝 요소로 지정한다.

  + ```python
    # l: 각 arr(정렬 범위)의 시작 인덱스
    # r: 각 arr(정렬 범위)의 끝 인덱스
    # p: pivot값, 중앙에 위치하게 될 값(두 그룹을 나눌 기준 값) -> 우리는 r번째 값으로 잡는다.
    # i: j가 p보다 작은 값을 찾으면 그 값과 스왑할 위치의 인덱스, 스왑하면 1증가
    # j: p보다 작은 값을 찾으러 이동할 인덱스
    # j가 끝까지 이동한 뒤에는 i번째 값과 r번째 값(p)를 스왑
    
    def quicksort(arr, l, r):
        if l < r:
            s = partition(arr, l, r)
            quicksort(arr, l, s-1)
            quicksort(arr, s+1, r)
    
    
    def partition(arr, l, r):
        p = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= p:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
    
        arr[i], arr[r] = arr[r], arr[i]
        return i
    
    
    for t in range(1, int(input())+1):
        N = int(input())
        A = list(map(int, input().split()))
        quicksort(A, 0, N-1)
        print('#%d %d' % (t, A[N//2]))
    ```

+ 병합 정렬은(왜 합병 정렬이라고도 부르는지 모르겠다) 개인적으로 가장 신기하고도 효율적인 알고리즘이라고 생각한다.

  + 물론, 병합 정렬은 병합의 과정에서 새로운 배열을 계속 생성해야 하기 때문에 메모리의 소비가 크다.

  + ```python
    def mergesort(arr):
        if len(arr) < 2:
            return arr
    
        mid = len(arr)//2
        a_arr = mergesort(arr[:mid])
        b_arr = mergesort(arr[mid:])
        ai, bi = 0, 0
        temp = []
        # 이 부분이 가장 감탄스럽다.
        while ai < len(a_arr) and bi < len(b_arr):
            if a_arr[ai] <= b_arr[bi]:
                temp.append(a_arr[ai])
                ai += 1
            else:
                temp.append(b_arr[bi])
                bi += 1
    
        if ai == len(a_arr):
            temp.extend(b_arr[bi:])
        else:
            temp.extend(a_arr[ai:])
    
        return temp
    ```

+ 트리 순회는 개인적으로 가장 쉬운 문제였다. 나는 트리가 좀 잘 맞는 것 같다. 물론 힙은 어렵다.

  + ```python
    # 전위 순회, 중위 순회, 후위 순회를 모두 비교하며 구현하기 위해 order라는 함수 안에 전부 넣었다.
    
    def order(node):
        if node:
            # 전위 순회에서 부모 노드를 처리하는 곳
            pre_way.append(str(node))
            order(tree[node][0])
            # 중위 순회에서 부모 노드를 처리하는 곳
            in_way.append(str(node))
            order(tree[node][1])
            # 후위 순회에서 부모 노드를 처리하는 곳
            post_way.append(str(node))
    
    
    for t in range(1, int(input())+1):
        N = int(input())
        tree = [[0, 0] for _ in range(N+1)]
        edges = list(map(int, input().split()))
        # 주어진 입력은 부모노드와 자식노드의 쌍의 반복이며 2 1 1 4 4 3 과 같이 주어졌다.
        # 이를 트리로 집어넣는 방법은 아주 다양하다.
        for p, c in zip(edges[::2], edges[1::2]):
            if not tree[p][0]:
                tree[p][0] = c
            else:
                tree[p][1] = c
    
        pre_way, in_way, post_way = [], [], []
        order(edges[0])
    ```

+ powerset 만들기는 조합의 개념을 사용해서 쉽게 풀 수 있었다.

  + ```python
    # 입력받은 N개의 데이터에 대한 powerset 중 원소의 합이 M인 부분집합의 개수 구하기
    
    def powerset(start, S):
        if S > M:
            return
    
        if S == M:
            cnt[0] += 1
            return
    
        for i in range(start, N):
            powerset(i+1, S+data[i])
    
    
    for t in range(1, int(input())+1):
        N, M = map(int, input().split())
        data = list(map(int, input().split()))
        cnt = [0]
        powerset(0, 0)
        print('#%d %d' % (t, cnt[0]))
    ```

+ 느낀점 및 배운점

  + 오늘 문제들은 특별히 코드까지 모두 기록하였다.
    + 이 문제들은 어떠한 특별 케이스의 문제들이 아닌, 다른 문제들의 풀이에 기본적으로 쓰이게 될 뼈대 코드들이기 때문이다. 따라서, **매우 중요한 코드들이다.**
    + 특히 트리나 조합의 경우는 확실히 익숙해질 필요가 있다. 지금은 꽤 많이 익숙해진 것 같다.
    + 트리는 class를 사용하여 링크드 리스트를 구현할 수 있는데, 아직까지는 Python이 가지는 이점으로서 리스트를 사용해 구현했다. 다음 기회에는 링크드 리스트로 구현을 한 번 해봐야겠다.
  + 오늘 문제들은 기본기를 확인하는 문제들인 것 같았다. 술술 잘 풀렸고 매우 만족한다!