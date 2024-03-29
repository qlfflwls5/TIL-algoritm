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
    
    for i in range(len(temp)-1, -1, -1):
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

<br/>

## 2021-04-20 (2)

+ 싸피 Day27의 알고리즘 문제들을 복습하였다.

+ **이진 탐색, 이진 탐색_확장 문제, N-Queen, 최소 생산 비용, 전기버스2, 동철이의 일 분배**

+ **이진 탐색, 백트래킹, DP**의 기법을 사용했다.

+ 이진 탐색은 오랜만에 해보니 또 새로웠다. 기본적인 이진 탐색에서 확장된 문제들을 풀어보았다.

  + ```python
    # 1. A, B 배열에서 B의 각 요소를 A에서 이진탐색을 이용해 찾을 때 비교횟수 누적값 출력, 못찾았다면 0으로
    # 2. A, B 배열에서 B의 각 요소를 A에서 이진탐색으로 K번 비교 내에 찾을 수 있는지 검사하여, 찾을 수 있는 것의 개수 출력
    # 3. A, B 배열에서 못 찾았을 경우 작은 것 중 가장 큰 것 검색
    # 4. A, B 배열에서 못 찾았을 경우 큰 것 중 가장 작은 것 검색
    # 5. A, B 배열에서 A에 중복 데이터가 있다고 할 때 가장 앞의 것을 찾기
    
    
    # 1, 2, 3, 4번 동시 해결
    def binary_search(b):
        s, e = 0, len_A - 1
        accumulate = 0
        while s <= e:
            mid = (s+e)//2
            accumulate += 1
            if A[mid] == b:
                if K >= accumulate:
                    K_cnt[0] += 1
                print('%d의 비교 횟수: ' % b, accumulate)
                return accumulate
            elif A[mid] > b:
                e = mid - 1
            else:
                s = mid + 1
    
        if e >= 0:
            list3.append((b, A[e]))
        if s < len_A:
            list4.append((b, A[s]))
        return 0
    
    
    for t in range(1, int(input())+1):
        len_A, len_B = map(int, input().split())
        K = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        K_cnt = [0]
        accumulate_sum = 0
        # 3번의 답들, 4번의 답들을 담을 리스트
        list3, list4 = [], []
        for b in B:
            accumulate_sum += binary_search(b)
    
        print('3번: ', list3)
        print('4번: ',list4)
        print('총 누적 비교 횟수: ', accumulate_sum)
        print('K번 횟수 내 비교 완료: ', K_cnt[0])
        
    
    [입력]
    3
    5 5
    2
    1 3 5 7 9
    1 2 3 6 7
    [출력]
    1의 비교 횟수:  2
    3의 비교 횟수:  3
    7의 비교 횟수:  2
    3번:  [(2, 1), (6, 5)]
    4번:  [(2, 3), (6, 7)]
    총 누적 비교 횟수:  7
    K번 횟수 내 비교 완료:  2
        
    
    # 5번
    def binary_search(b):
        s, e = 0, len_A - 1
        while s <= e:
            mid = (s+e)//2
            # 끝의 것을 갖고 오고 싶다면 등호를 빼고 e를 리턴하면 됨
            if A[mid] >= b:
                e = mid - 1
            else:
                s = mid + 1
    
        return s if 0 <= s < len_A else -1
    
    
    for t in range(1, int(input())+1):
        len_A, len_B = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    
        for b in B:
            print('%d의 첫 인덱스: ' % b, binary_search(b))
    ```

+ **N-Queen** 유명한 문제라고 한다.

  + 행을 기준으로 열의 선택은 기존의 순열을 풀던 방법처럼 하면 쉽게 처리할 수 있으나 **대각선이 관건이었다.**
  + 처음에 나는 두 퀸의 행과 열의 차이가 같으면 대각선에 있다고 판단하여 풀어냈지만, 대각선 자체의 식을 구해 푸는 방법도 있었다.

  + ```python
    # 대각선 자체에 잘보면 특성이 있다.
    # n*n의 배열에서 대각선의 개수는 좌상, 우상 대각선 각각 2*n-1이다.
    # 그리고, 행과 열의 인덱스를 이용해 각 대각선을 나타낼 수 있다.
    # n이 4일 때,
    # 우상 대각선(행 + 열)
    # 0 1 2 3
    #       4
    #       5
    #       6
    # 좌상 대각선(행 - 열 + n - 1)
    # 3 2 1 0
    # 4
    # 5
    # 6
    
    # level은 행 번호, i는 열 번호가 된다.
    def DFS(level):
        if level >= N:
            cnt[0] += 1
            return
    
        for i in range(N):
            if not col[i] and not diag_r[level+i] and not diag_l[level-i+N-1]:
                col[i], diag_r[level+i], diag_l[level-i+N-1] = 1, 1, 1
                DFS(level+1)
                col[i], diag_r[level+i], diag_l[level-i+N-1] = 0, 0, 0
    
    
    for t in range(1, int(input())+1):
        N = int(input())
        # 열, 우상 대각선, 좌상 대각선 방문 체크용
        col, diag_r, diag_l = [0]*N, [0]*(2*N-1), [0]*(2*N-1)
        cnt = [0]
        DFS(0)
        print('#%d %d' % (t, cnt[0]))
    ```

+ **전기 버스2**는 처음 내가 제대로 DP를 이해하고 도전해보려 한 문제다.

  + ```python
    # 충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 
    # 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
    # 정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.
    
    # [입력]
    # 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
    # 다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N
    
    
    # 1
    # 백트래킹
    def DFS(cur, cnt):
        # 가지치기1: 이미 최소 교체 횟수를 넘은 경우
        if cnt >= min_change[0]:
            return
    
        end = cur + station[cur]
        if end >= N-1:
            min_change[0] = cnt
            return
    
        for i in range(cur+1, end+1):
            # 가지치기2: i에서 갈 수 있는 가장 먼 정류장이 현재 cur에서 갈 수 있는 경우 가지치기
            if i < N-1 and i + station[i] > end:
                DFS(i, cnt+1)
    
    
    for t in range(1, int(input())+1):
        data = list(map(int, input().split()))
        N, station = data[0], data[1:]
        min_change = [N]
        DFS(0, 0)
        print('#%d %d' % (t, min_change[0]))
        
        
    # 2
    # DP
    for t in range(1, int(input()) + 1):
        N, *station = map(int, input().split())
        dp = [[] for _ in range(N)]
        for i in range(N-1):
            for j in range(i+1, i+station[i]+1):
                if not dp[i]:
                    dp[j].append(0)
                elif j < N:
                    dp[j].append(min(dp[i])+1)
    
        print('#%d %d' % (t, min(dp[N-1])))
    ```

+ 느낀점 및 배운점

  + 오늘도 주요 문제들은 내가 작성한 코드를 그대로 적어보았다.
    + 나중에 이 코드를 다시 보면서 상기할 날이 올 것 같다.
  + DP의 세계는 정말 신기하다. 문제를 풀 때 문제를 정확하게 파악하는 능력이 요구될 것 같다.
  + 아쉽게도 알고리즘 학습은 곧 끝나고 DP도 거의 다루지 않지만, 다른 사이트에서 DP 문제들을 풀어볼 필요가 있을 것 같다.

<br/>

## 2021-04-22

+ 싸피 Day28의 알고리즘 문제들을 복습하였다.

+ **DFS, BFS, Dijkstra, 최장 경로**

+ **DFS, BFS, Dijkstra**의 기법을 사용했다.

+ 가중치 있는 유향 그래프에서 시작 정점과 각 정점 사이의 가중치 비용이나 경로를 구하는 기법인 **Dijkstra**를 새롭게 배웠다. 매우 중요한 개념같으니 알고리즘 자체를 이해하고 외워놓자.

  + ```python
    # 정점은 'a'부터 시작하여 'b', 'c'와 같이 나열되며 25개를 넘지 않는다. 방향성 그래프이며, 간선에 가중치 정보가 있다.
    
    
    def dijkstra(s):
        # U: 방문 처리용, D: 시작 정점으로부터 각 정점까지의 최단 거리
        U = [0]*(V)
        D = [float('inf')]*V
    
        # 먼저 시작 정점에 대한 1시행 처리
        U[s] = 1
        D[s] = 0
        for w, c in AL[s]:
            D[w] = c
    
        # 시작 정점 이외의 나머지 정점에 대한 처리
        for _ in range(V-1):
            # 방문하지 않은 정점 중에 D값이 가장 작은 정점에 대해, 방문 처리하고, 인접 정점들의 최단 거리를 필요하면 갱신
            # 수정 1: min을 위해서 리스트를 만들기 위한 대괄호 안써도 된다. iterator는 min그냥 가능
            # 수정 2: 기존 코드는 v = D.index(min([D[x] for x in range(V) if not U[x]]))였다. 이렇게 하면 가중치가 같은 녀석들의 경우 단순히 D에서 index로 찾아오므로 문제가 발생
            #         따라서, 방문하지 않은 index에 대해서만 고려할 수 있도록 해야 한다.
            v = min((D[x], x) for x in range(V) if not U[x])[1]
            U[v] = 1
            for w, c in AL[v]:
                D[w] = min(D[w], D[v]+c)
    
        return D
    
    
    for t in range(1, int(input())+1):
        V, E = map(int, input().split())
        AL = [[] for _ in range(V)]
        for _ in range(E):
            s, e, c = input().split()
            AL[ord(s)-97].append((ord(e)-97, int(c)))
    
        result = dijkstra(0)
        print('#%d %s' % (t, ' '.join(map(str, result))))
    ```

+ **최장 경로** 문제도 매우 유의미한 문제이다. 우리는 여태까지 BFS를 통한 **최단 거리** 문제만 풀었지, 주어진 그래프 내에서의 **최장 거리**는 푼 적이 없었다.

  + 최장 거리는 다음과 같이 구한다.

    1. 모든 정점에서 깊이 우선 탐색을 실시해야 한다.
    2. 문제는, **이번 경로에서 방문한 정점이 다음 경로에서 다시 방문할 수 있다는 것**이다.(돌아서 올 수도 있기 때문에)
    3. 따라서, 이번 경로의 최대 깊이로 내려가고 나서 갈림길로 되돌아와 다른 경로로 틀 때는, 돌아온 길만큼은 방문 처리를 초기화해줘야 한다.
    4. 이를 구현하기 위해 DFS를 재귀적으로 구성하고, 경로의 길이를 재기 위해 DFS 함수에 거리 누적합용 인자를 추가한다.

  + ```python
    def DFS_max(v, cnt):
        max_v[0] = max(max_v[0], cnt)
        visited[v] = 1
        for w in AL[v]:
            if not visited[w]:
                DFS_max(w, cnt + 1)
        # 방문 처리 초기화
        visited[v] = 0
    
    
    for t in range(1, int(input()) + 1):
        N, M = map(int, input().split())
        AL = [[] for _ in range(N + 1)]
        for _ in range(M):
            s, e = map(int, input().split())
            AL[s].append(e)
            AL[e].append(s)
    
        max_v = [0]
        # 모든 정점에서 다 DFS를 돌려본다.
        for i in range(1, N + 1):
            visited = [0] * (N + 1)
            DFS_max(i, 1)
    
        print('#%d %d' % (t, max_v[0]))
    ```

+ 느낀점 및 배운점

  + 싸피 알고리즘 수업의 마지막 단원인 그래프이다. Dijkstra를 중점적으로 배웠고 다른 Prim, KRUSKAL 알고리즘은 지나가는 식으로 배웠는데, 전부 매우 어려운 알고리즘인 것 같다.
    + 계속 이해를 반복 시도하자.
  + 최장 경로의 문제도 순간 굉장히 당황했던 문제다. DFS로 해결할 수 있음을 깨달았다.
  + **수정들**
    + Dijkstra 코드는 계속 수정을 한 부분이 있다.
    + 언제나 실수는 존재한다. 반례를 찾는 것도 능력이다. 잘 살펴보자.
    + 이제는 그래도 완벽한 것 같다...!

<br/>

## 2021-04-22

+ 싸피 Day29의 알고리즘 문제들을 복습하였다.

+ **Dijkstra, 그룹나누기, 연산, 최소 비용, 최소 신장 트리, 최소 이동 거리**

+ **Dijkstra, KRUSKAL, DFS, BFS**의 기법을 사용했다.

+ 저번의 **Dijkstra**의 알고리즘에 대해 조금 의문이 생겼다.

  + 과연 **시작 정점에서의 처리**를 따로 해주어야 하는가?

  + 방문하지 않은 정점 중 최단 거리가 가장 짧은 정점을 찾는 데에 꼭 **D를 전부 순회해야 하는가**?

    + **이 물음에 대한 해답으로서의 알고리즘을 직접 짜보았다.**

  + ```python
    def dijkstra(s):
        U = [0]*(V)
        D = [float('inf')]*V
        D[s] = 0
        # 원래 여기서 시작 정점의 첫 시행을 미리 해줬는데, 불필요한 것 같다. U[s] = 1과 시작 정점의 인접 정점들에 대한 처리를 해주었었다.
        # 대신 check라는 set을 이용해서 가장 작은 D값을 가질 수 있는 정점 후보군을 만든다.
        # 가장 작은 D값을 가질 수 있는 정점은 인접 정점에 해당되었던 것들만 가능하다.
        check = {s}
        for _ in range(V):
            v = min((D[x], x) for x in check if not U[x])[1]
            U[v] = 1
            # 만약 가장 작은 D값을 가진 정점으로 뽑혔다면, 이 정점의 최단 거리는 확정된 것
            # 더 이상 check에 있어봤자 반복만 한 번 더 하게 만드니 제거한다.
            check.remove(v)
            for w, c in AL[v]:
                D[w] = min(D[w], D[v]+c)
                # 여기가 인접 정점에 해당되는 것들을 check에 넣어주는 작업
                check.add(w)
    
        return D
    
    
    for t in range(1, int(input())+1):
        V, E = map(int, input().split())
        AL = [[] for _ in range(V)]
        for _ in range(E):
            s, e, c = input().split()
            AL[ord(s)-97].append((ord(e)-97, int(c)))
    
        result = dijkstra(0)
        print('#%d %s' % (t, ' '.join(map(str, result))))
    ```

+ **최소 비용**은 매우 어려웠던 문제로, **Dijkstra의 2차원 배열 적용** 문제다.

  + 나는 Dijkstra로 풀었으나, 사실 Dijkstra는 BFS와 비슷한 개념이라 BFS로 푼 풀이도 가져왔다.

    + **이 문제를 풀며 위의 Dijkstra 알고리즘에 대한 재고를 해보게 되었다.**

  + 속도는 BFS가 더 빨랐고, 가독성도 좋은 것 같다.

  + ```python
    # 다익스트라의 2차원 배열용이다. 기본 다익스트라와 구조가 똑같고, 방문하지 않은 최소 D값을 지닌 정점을 찾기 위한 작업의 시간 단축을 위해
    # check라는 set을 사용하는 것만 추가되었다. 이는 기본 다익스트라에서도 사용이 가능할 것이다.
    # 또, 기본 다익스트라에서는 D[0]에 대한 시행을 먼저 해줬는데, 사실 안해줘도 된다.
    def dijkstra(sr, sc):
        U = [[0]*N for _ in range(N)]
        D = [[float('inf')]*N for _ in range(N)]
        D[sr][sc] = 0
        # 이 부분이 핵심. 다익스트라에서는 방문하지 않은 정점들의 D값 중 가장 작은 D값을 가지는 정점을 다음에 시행의 대상으로 하는데,
        # 코드의 흐름대로 생각해보면, 방문하지 않았으면서 D값이 inf가 아닌 후보군은 현재 D값이 업데이트 된 녀석들이다.
        # 즉, 인접 정점들 중 D값이 갱신된 녀석들
        check = {(0, 0)}
        for _ in range(V):
            # check내에서 방문하지 않고 D값이 최소인 정점 찾기
            r, c = min((D[i][j], (i, j)) for i, j in check if not U[i][j])[1]
    
            # 시행의 대상이 된 정점은 최단 거리가 확정된 것이다. 방문 처리를 하고 check에서도 없애준다.(안없애면 시간 초과)
            U[r][c] = 1
            check.remove((r, c))
    
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    w = 1 if arr[nr][nc] - arr[r][c] <= 0 else arr[nr][nc] - arr[r][c] + 1
                    if D[nr][nc] > D[r][c] + w:
                        D[nr][nc] = D[r][c] + w
                        check.add((nr, nc))
    
        return D[N-1][N-1]
    
    
    drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for t in range(1, int(input())+1):
        N = int(input())
        V = N**2
        arr = [list(map(int, input().split())) for _ in range(N)]
        print('#%d %d' % (t, dijkstra(0, 0)))
    
    
    # 2
    # BFS 풀이
    # 2차원에서의 성능은 이게 더 좋다
    # 유방향 가중치 그래프에서 BFS는 visited가 아닌 cost의 느낌으로 사용해서 푼다.(여기서는 cnt)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    
    def search():
        q = [[0, 0]]
        cnt = [[987654321] * N for _ in range(N)]
        cnt[0][0] = 0
        while q:
            cr, cc = q.pop(0)
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    height = (area[nr][nc] - area[cr][cc]) if area[nr][nc] > area[cr][cc] else 0
                    if cnt[nr][nc] > cnt[cr][cc] + 1 + height:
                        cnt[nr][nc] = cnt[cr][cc] + 1 + height
                        q.append([nr, nc])
        return cnt[-1][-1]
    
    
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        area = [list(map(int, input().split())) for _ in range(N)]
        result = search()
        print('#%d %d' % (t, result))
    ```

+ **최소 신장 트리**는 MST로 불리며, 가장 기본적인 문제를 풀었다. KRUSKAL의 기본 이론이므로 적어놔야겠다.

  + ```python
    def find_set(x):
        while x != p[x]:
            x = p[x]
    
        return x
    
    
    def kruskal():
        S = 0
    
        for s, e, w in edges:
            rep_s, rep_e = find_set(s), find_set(e)
            if rep_s != rep_e:
                S += w
                p[rep_e] = rep_s
    
        return S
    
    
    for t in range(1, int(input())+1):
        V, E = map(int, input().split())
        edges = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
        p = [i for i in range(V + 1)]
    
        print('#%d %d' % (t, kruskal()))
    ```

+ 느낀점 및 배운점

  + Dijkstra와 BFS 사이에서 많은 헷갈림이 생긴다. 반에서 최소 비용 문제를 Dijkstra로 푼 사람이 나밖에 없었다. 모두들 BFS로 풀었는데, 실행시간이 더 빠르다.
    + 무엇을 선택해야 할까.
  + 싸피 과정이 짧은만큼 대체로 기본만 간단히 배운 느낌이 있어 아쉽다.
    + 진행하는 알고리즘 스터디에서 더 많은 것들을 풀고 익혀봐야 할 것 같다.

<br/>

## 2021-04-23

+ 싸피 Day29의 알고리즘 문제들을 복습하였다.

+ **병합정렬-슬라이싱, 보급로, 인수의 생일 파티, 창용 마을 무리의 개수, 하나로**

+ **병합정렬, KRUSKAL, PRIM, Dijkstra, 상호 배타 집합**의 기법을 사용했다.

+ 이번에 정말 많은 혼란을 겪었다.

  + Dijkstra에 대해서 다시 혼자 재정의를 내리게 되었다.

    + **원래 check라는 녀석을 썼으나, 이를 사용하지 않는게 훨씬 나은 것 같다.**
      + check는 이중 배열에서만 사용하자.

  + ```python
    def dijkstra(s):
        U = [0]*(V)
        D = [INF]*V
        D[s] = 0
        # 원래 여기서 시작 정점의 첫 시행을 미리 해줬는데, 불필요한 것 같다. U[s] = 1과 시작 정점의 인접 정점들에 대한 처리를 해주었었다.
        for _ in range(V):
            # 최소 D값을 갖는 방문하지 않는 정점을 이렇게 찾자. 이게 낫다.
            min_d = INF
            for i, d in enumerate(D):
                if not U[i] and d < min_d:
                    min_d, v = d, i
            U[v] = 1
            for w, c in AL[v]:
                    D[w] = min(D[w], D[v]+c)
    
        return D
    
    
    INF = 1e10
    for t in range(1, int(input())+1):
        V, E = map(int, input().split())
        AL = [[] for _ in range(V)]
        for _ in range(E):
            s, e, c = input().split()
            AL[ord(s)-97].append((ord(e)-97, int(c)))
    
        result = dijkstra(0)
        print('#%d %s' % (t, ' '.join(map(str, result))))
    ```

+ **Dijkstra와 Prim의 차이**를 깨닫는 것이 매우 중요해보였다.

  + 따라서, 이를 내가 느낀 바로 정리해보았다.

  + 다익스트라와 프림의 차이점

    + 다익스트라는 **유.무향 그래프** 둘 다 가능

    + 프림은 **무향 그래프만 가능(MST)**

      + **프림은 인접 정점의 거리 값을 갱신하는 과정에서 not visited처리를 해주어야 한다!**

      + 다익스트라의 경우, 어차피 시작 정점부터 누적되어 쌓여오는 것이기 때문에 이후의 D의 값이 더 커서 왔던 길을 되돌아 갈 수가 없다. **하지만, 프림의 경우 누적되어 쌓여오는 값이 아니라 당장 정점에서의 인접 정점으로의 거리만 D에 담기 때문에 min(D)를 갖는 정점을 구하는 부분에서 이전 정점을 방문해 루프가 생길 수 있다.**

  + ```python
    # prim의 구현 예
    # 다익스트라와 똑같다. U를 MST로, D를 key로 바꿨을 뿐
    INF = 10**12
    def prim(s):
        MST = [0]*N
        key = [INF]*N
        key[s] = 0
        # pi = [NULL]*N # 부모 찾기용(경로를 찾을 때)
        for _ in range(N):
            min_v = INF
            for i, k in enumerate(key):
                if not MST[i] and k < min_v:
                    min_v, v = k, i
    
            MST[v] = 1
            for w, cost in AL[v]:
                # Dijkstra와 똑같지만 MST에서는 이게 꼭 필요하다. 방문하지 않은 정점에 대해서만 진행
                if not MST[w]:
                    key[w] = min(key[w], cost)
    
        return round_up(sum(key)*E)
    ```

+ **KRUSKAL**의 수정본이다. 중요한 것을 하나 빼먹었었다.

  + KRUSKAL에서는 간선의 개수만큼만 간선 추가 작업을 하면 된다.

    + 즉, 정점의 개수가 N이라면 N-1번만
    + 따라서 이를 cnt를 사용해서 구현해 break를 걸어줘야 한다. 아래와 같이

  + ```python
    def kruskal():
        S = 0
        # 즉, 간선이 N-1개가 들어왔을 때, cnt가 N-1일 때까지만 간선을 넣는다.
        cnt = 0
        for w, s, e in edges:
            rep_s, rep_e = find_set(s), find_set(e)
            if rep_s != rep_e:
                p[rep_e] = rep_s
                S += w
                cnt += 1
                if cnt == N-1:
                    break
    
        return round_up(S*E)
    ```

+ **Dijkstra와 BFS**

  + 대체로 BFS식의 풀이가 더 빠른 것 같았다. 잘 알아두자

  + ```python
    # Dijksta를 BFS로 구현한 것의 예시
    # 이 문제는 갔다가 돌아오는 최단 경로를 찾는 문제로, 주어진 유향 그래프를 반전시켜서 한 번 더 다익스트라를 돌려야 하는 문제였다.
    INF = int(1e9)
     
    def dijkstra(start, graph):
        D = [INF] * (n+1)
        D[start] = 0
        queue = [start]
        rp = 0
        while rp < len(queue):
            node = queue[rp]
            rp += 1
            for n_node, w in graph[node]:
                d = D[node] + w
                if d < D[n_node]:
                    D[n_node] = d
                    queue.append(n_node)
        return D[1:]
     
    for t in range(1, int(input())+1):
        n, m, x = map(int, input().split())
        graph1, graph2 = [[] for _ in range(n+1)], [[] for _ in range(n+1)]
        for _ in range(m):
            s, e, w = map(int, input().split())
            graph1[s].append((e, w))
            graph2[e].append((s, w))
     
        result = max(a+b for a, b in zip(dijkstra(x, graph1), dijkstra(x, graph2)))
        print('#%s %s' % (t, result))
    ```

+ 느낀점 및 배운점

  + 오늘 사실 매우 멘탈 관리가 힘들었다. 내 방식대로 생각했던 Dijkstra보다 BFS로 사람들이 푸는 것이 훨씬 효율이 좋아 삽질을 했나 생각이 들었다.
    + 그래도 이런 삽질을 하면서 성장하는 것이라고 했다...
    + 확실히 더 깊게 Dijkstra의 구동 방식에 대해 생각해볼 수 있었던 것 같다.
      + 그래도 여전히 어렵긴하다.
  + 네이버 코딩테스트가 내일이라 시험을 마치고 다시 한 번 심도있게 봐야할 것 같다.

<br/>

## 2021-04-23

+ 싸피에서 제공하는 모의 A형 테스트 문제들을 풀었다.
  + 3시간 제한에 2시간 30분으로 완료했다.
+ **삼국지, 하강 모의실험**
+ **2차원 배열, 델타 검색**을 사용해서 푸는 문제들이었다.
+ 코딩테스트 대비용 문제들이라고 하였으나 생각보다 많은 알고리즘 기법들을 사용하는 문제들은 아니었다.
  + 두 문제 모두 시뮬레이션을 구현하는 문제였는데, 아직 코딩테스트를 본 적이 없어서 이런 느낌인지는 잘 모르겠다.
  + 특히 삼국지 문제는 생각을 놓쳐서는 안되는 문제였다.
    + **문제 해결력**과 **사고력**, **설계력**이 요구되는 문제인 것 같긴 했다.
  + 하강 모의실험 문제도 처음에 문제를 어떻게 풀 것인지 설계를 잘 하지 않으면 매우 어려운 문제가 된다.
+ 느낀점 및 배운점
  + 코딩테스트 대비를 위해서 풀었는데, 일단 통과를 해서 매우 기쁘다.
  + 하지만, 코로나로 인해 모의 A형만 계속 치루고 있어 실제 A형 취득은 못했다는 점, 폭넓은 알고리즘 문제가 아니라는 점이 아쉬웠다.

<br/>

## 2021-04-25

+ 싸피 Day17~30까지의 모든 문제들을 다시 풀어보았다.(중복되는 내용의 문제는 제외했다.)
+ 딱히 막히거나 하는 부분은 없었으나, 제일 기억이 잘 안나고 어려운 부분은 **진법** 부분이었다.
  + 비트 연산자에 대해 더 익숙해져보자
+ 코딩테스트를 한 번 경험해보고 나니, 특별히 알고리즘 기법 자체에 대한 것을 묻는다기 보다는 **문제 해결력**을 보고 어려운 알고리즘 기법을 사용할 것 없이 누구나 쓸 수 있을 만한 알고리즘으로 그것을 구현해낼 수 있는지를 보는 것 같다.
  + 따라서, 기법들을 달달 외우기 보다는 각각 어느 문제의, 어느 상황에서 사용했을 때 더 좋은 효율을 내는지를 보는 안목을 기르는 것이 좋을 것 같다.
+ 느낀점 및 배운점
  + 여태까지 배운 내용들을 다시 한 번 정리할 수 있는 시간이었다.
  + 내일 월말평가 잘 보자!

<br/>

## 2021-06-09

+ 싸피에서 진행하는 A형 대비 문제로 **무인도 탈출**을 풀었다.
  + 굉장히 어려운 문제였다. 정답률이 11%, **python으로 문제를 해결한 사람은 싸피 전체에서 10명도 되지 않았다.**
  + **나는 python으로 풀어 코딩 길이가 가장 짧으며 실행시간이 가장 짧은(C++, JAVA와 합쳐서 순위를 내어 3위) 코드를 만들어냈다!**
+ 이 문제는 주어진 상자로 탑을 쌓아 가장 높은 탑을 만드는 문제로, 상자를 회전시켜 쌓을 수 있고 아래 상자의 윗면의 면적보다 위 상자의 아래면의 면적이 작아야만 쌓을 수 있다.
+ 아마도 이 문제를 대부분 **DFS**로 접근했을 것이다.
  + 모든 경우의 수를 파악해서 가장 탑의 높이가 높을 때를 찾으면 되기 때문이다.
  + 하지만, 한 상자에서 가로 세로 높이를 바꿔 가며 나올 수 있는 경우의 수는 3가지, 최대 상자가 20개이므로 3의 20제곱만큼의 시간이 걸리게 된다. -> 절대 불가능
+ 따라서, 이 문제는 DP를 사용해 **아래부터 쌓아올리는 것이 아니라 위부터 아래로 쌓아 내려간다**라고 생각해야 풀 수 있다.
  + 예를 들어, (1, 2, 3)의 순서대로 상자를 쌓을 수 있다고 했을 때, 4의 위에 3을 쌓을 수 있다면 (1, 2, 3)을 묶어서 저장해놓고 4에 이어붙여 (1, 2, 3, 4)를 만들어야 중복을 피하고 빠르게 쌓을 수 있다.
    + 따라서, **메모이제이션의 개념을 활용한 DP**다.
+ 이 문제는 내 코드가 가장 빠르고 효율적이고 가독성이 좋기 때문에 코드를 첨부하겠다!

```python
# 1. 각각의 상자는 가로, 세로, 높이 축을 기준으로 90 도씩 회전시켜서 쌓을 수 있다.
# 2. N 개의 상자를 쌓는 순서에는 별다른 제약이 없으며, 모든 상자를 다 사용하지 않아도 된다.
# 3. 모든 상자의 밑면은, 바로 아래 쌓여진 상자의 윗면을 벗어나선 안된다.

# 입력으로 N 개의 상자들의 가로, 세로, 높이의 길이가 각각 주어질 때,
# 쌓을 수 있는 최대 높이를 계산하는 프로그램을 작성하라.


# DFS로 풀면 시간초과가 난다. DP를 이용해서 해결한다.
for t in range(1, int(input())+1):
    N = int(input())
    boxes = []
    for i in range(N):
        w, l, h = map(int, input().split())
        # 상자를 돌려서 나올 수 있는 가능한 가로, 세로, 높이 조합은 세 가지
        # 각각을 다른 상자로 볼 것이고, 실제로 같은 상자인지는 구별할 수 있어야 하므로 i(박스의 번호)를 추가로 저장한다.
        boxes.append((w, l, h, i))
        boxes.append((w, h, l, i))
        boxes.append((l, h, w, i))

    # 박스들을 면적순으로 정렬한다.
    # 면적이 더 작은 상자는 더 큰 상자 위에 쌓일 가능성이 있으나, 면적이 더 큰 상자는 절대 면적이 더 작은 상자 위에 쌓일 수 없다.
    boxes = sorted(boxes, key=lambda x: (x[0]*x[1]))
    # 맨 위(면적이 가장 적은) 상자부터 놓는다고 생각할 때 현재 놓은 상자를 포함해 만들 수 있는 최대 높이
    dp = [0]*(N*3)
    # 상자들을 쌓을 때 실제로 같은 상자인 경우(즉, i가 같은 경우) 당연히 중복해서 쌓을 수 없다.
    # 이를 확인하기 위해 각 dp 상황에서 각 i번째 상자가 갖는 높이, 없으면 0을 갖는 dp_h 리스트를 만든다.
    dp_h = [[0]*N for _ in range(N*3)]
    dp[0] = boxes[0][2]
    dp_h[0][boxes[0][3]] = boxes[0][2]
    for i in range(1, N*3):
        # 현재 상자
        cur = boxes[i]
        dp_i_candidate = []
        for j in range(i-1, -1, -1):
            # 면적이 더 작은 상자
            pre = boxes[j]
            # 이 조건을 만족하면 가로, 세로 범위 안에 들어와 위에 쌓일 수 있게 된다.
            if (cur[0] >= pre[0] and cur[1] >= pre[1]) or (cur[0] >= pre[1] and cur[1] >= pre[0]):
                # 현재 상자의 위에 쌓으려고 보니 이미 현재 상자와 실제로 같은 상자가 이미 사용된 경우,
                # 기존에 사용된 상자 높이를 없애고 현재 상자 높이를 대신 넣어서 dp를 구한다.
                if dp_h[j][cur[3]]:
                    dp_i_candidate.append((dp[j] - dp_h[j][cur[3]] + cur[2], j))
                else:
                    dp_i_candidate.append((dp[j] + cur[2], j))
        # dp 후보군 중에 가장 최대 높이를 갖는 dp를 택한다. 동시에 dp_h를 해당 dp의 경우에 맞게 세팅해준다.
        if dp_i_candidate:
            dp_pick = max(dp_i_candidate)
            dp[i] = dp_pick[0]
            dp_h[i] = list(dp_h[dp_pick[1]])
            dp_h[i][cur[3]] = cur[2]
        # dp 후보군이 없다면 현재 상자 혼자서만 탑을 쌓는 것이 가능한 상태이다.
        else:
            dp[i] = cur[2]
            dp_h[i][cur[3]] = cur[2]
    
    # 완성된 dp중 최댓값이 가장 높이 쌓을 수 있는 탑의 높이
    print('#%d %d' % (t, max(dp)))
```

+ 느낀점 및 배운점
  + 굉장히 머리를 많이 써야 하는 문제였다.
  + 단순한 DP가 아닌, DP 후보군을 다 구하고 그 속에서 최적해를 찾는 과정이 필요했다.
  + 사고력을 기르자.

<br/>

## 2021-06-11

+ 싸피에서 진행하는 알고리즘 문제 출제 대회에서 우수작들을 풀어보았다.
  + **우리의 문제도 전체 150개의 문제 중 TOP 5로 뽑혔다!**
    + 내가 만든 문제ㅎㅎ
+ **단식원, 금고털기**를 풀었다.
+ 단식원은 DFS를 통해 조합을 구한 후, BFS를 통해 그래프에 변화를 주어야 하는 문제다.
  + 또한, 하나의 조합에서 BFS를 진행하고 나면 격자판을 원상태로 되돌려줘야 한다.
  + 매우 어려운 문제였으나, 잘 풀어냈다.

```python
# 문제 단식원.py 참고

def bfs(sr, sc):
    queue = [(sr, sc)]
    rear = 0
    while rear < len(queue):
        r, c = queue[rear]
        rear += 1
        arr[r][c] = 2
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                queue.append((nr, nc))


def dfs(level, idx):
    global arr
    if level == 3:
        for r, c in chicken:
            bfs(r, c)

        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
                    global max_v
                    max_v = max(max_v, cnt)

        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2 and (i, j) not in chicken:
                    arr[i][j] = 0

        return

    for i in range(idx, len(possible) - 3 + level + 1):
        r, c = possible[i]
        arr[r][c] = 1
        dfs(level + 1, i + 1)
        arr[r][c] = 0


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    possible = []
    chicken = set()
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                possible.append((i, j))

            if arr[i][j] == 2:
                chicken.add((i, j))

    max_v = 0
    dfs(0, 0)

    print('#%d %d' % (t, max_v))
```

+ 금고털기는 아스키코드를 이용하여 푸는 문제로, 어렵지 않았다.
+ 느낀점 및 배운점
  + 우리들이 낸 문제도 SWEA의 문제만큼 꽤 완성도가 높았다.
  + 더욱이, 우리가 내려다 보니 여러 알고리즘을 합쳐서 풀게 한 문제도 있어서 굉장히 좋았다.
  + 문제 출제는 쉬운 일이 아니다...