# 📘 SWEA 알고리즘 풀이

> 싸피의 인재들과 함께하는 SWEA 알고리즘 풀이!! Difficulty 1부터 정복해 나가자!

+ SWEA의 Difficulty 1부터 정답율이 높은순으로 알고리즘 문제를 풀어나가며 정리한 내용들이다.
+ 내가 문제를 어떻게 풀어나갈지 생각한 과정과 스터디를 함께한 동료들의 좋은 코드들이 담겨있다.

**2021-02-11 추가**

+ 백준(BAEKJOON)의 문제들을 단계순으로 풀어나갈 것이다. 
+ 스터디가 아닌 혼자의 힘으로 풀어나가므로 제출 목록에서 다른 사람들의 코드를 보며 학습해나갈 것이다.
+ 이하 commit format
  + SWEA 풀이 - `0000-00-00 TIL D0(0~0)`
  + BAEKJOON 풀이 - `0000-00-00 TIL LV0(0~0)`

**2021-02-13 추가**

+ 싸피 알고리즘학습을 통해 푼 문제들을 정리하며 다양한 풀이를 검토할 것이다.
+ SWEA 홈페이지에서 누구나 접근 가능한 문제들이며, 기존에 스터디에서 진행하던 SWEA 문제 풀이에 더해지는 것들이다.
+ 이하 commit format
  + SWEA 풀이 - `0000-00-00 TIL D0(0~0)`
  + BAEKJOON 풀이 - `0000-00-00 TIL LV0(0~0)`
  + SSAFY알고리즘 풀이 - `0000-00-00 TIL DAY00(D0~D0)`
    + 알고리즘 학습 과정 DAY00의 문제들의, 난이도 범위 D0~D0

**2021-02-23 추가**

+ 문제 번호만 써져있다보니 문제의 제목을 몰라 나중에 다시 찾아보기 힘들 것 같다.
+ 앞으로는 README에 그날 푼 문제들의 제목을 나열할 것이다. 이전 README도 2021-02-23부로 업데이트 한다.



## 2021-01-26

+ Difficulty 1의 정답율순 1번 ~ 10번의 문제를 풀었다.

+ **스탬프 찍기, 아주 간단한 계산기, 신문 헤드라인, 자릿수 더하기, N줄 덧셈, 1대1 가위바위보, 서랍의 비밀번호, 대각선 출력하기, 간단한 N의 약수, 몫과 나머지 출력하기**

+ **반복, 사칙연산, if문, 나머지** 등에 대해 배웠다.

+ `list`의 `.insert()`와 `index`를 활용하여 반복문에서 위치를 바꾸며 요소를 삽입하는 것이 가능하다는 것을 배웠다. 매우 효율적인 것 같다.

+ 공백을 사이에 두고 입력 받은 두 수를 변수에 넣기 위해 `a, b = tuple(map(int, input().split()))`와 같이 써야 할 것 같았지만, `tuple()`을 굳이 안해줘도 `map_object`상태로 두 변수에 대입하는 것이 가능했다.

  가독성과 간결성을 위해 `a, b = map(int, input().split())`으로 쓰자!



## 2021-01-28

+ Difficulty 1의 정답율순 11번 ~ 19번의 문제를 풀었다. Difficulty 1 완료!
+ **최대수 구하기, 큰 놈, 작은 놈, 같은 놈, 알파벳을 숫자로 변환, 중간값 찾기, 더블더블, 거꾸로 출력해 보아요, 홀수만 더하기, 평균값 구하기, 연월일 달력**
+ **max 구현, 대소 비교, 인덱싱, 날짜 계산** 등을 배웠다.
+ `round(n, r)`는 `n`을 반올림하여 `r`자리까지 나타내는 함수이다. 이를 직접 구현하고 싶다면 이런 식으로 구현이 가능하다는 것을 알았다.

```python
# avg를 소수 첫 째자리에서 반올림하고 싶을 때

# 원래의 avg에서 정수부(int(avg))를 빼면 소수부만 남고, 이게 0.5보다 크면 반올림한다.
if avg - int(avg) >= 0.5:
    print(f'#{i} {int(avg) + 1}')
else:
    print(f'#{i} {int(avg)}')
```

+ 세상에 `02 == 2`는 안되지만, `int('02') == 2`는 된다. `int('02')`는 2다.

+ 새로운 메서드를 배웠다. `str.rjust(n, char)` => n만큼의 자리를 할애하고 오른쪽 정렬, 빈 공간 char로 채우기
+ 느낀점
  + 만약 if문, elif문 등을 통해서 같은 값을 반환해야 하는 경우가 많이 나오면 구조를 다시 짜보자!
  + if문도 if 안에 if가 들어가는 경우 `and`로 연결할 수 있다는 것을 알았다.



## 2021-02-02

+ Difficulty 2의 정답율순 1번 ~ 2번 문제를 풀었다.
+ **간단한 소인수분해, Base64 Decoder**
+ **딕셔너리, 나머지, 아스키코드, 2진수, 비트**에 대해 익힐 수 있었다.
+ 난이도 1이 올라갔다고 정말 매우 어려워졌다.
+ `dict`나 `list`를 사용하여 푸는 것은 코드가 간결해 보이고 실력이 있어 보일 수 있으나, **실제 실행시간과 메모리의 효율성** 측면에서는 **하나하나 코드로 적어내는 것**이 더 빠를 때가 있다는 것을 알았다.
+ 느낀점 및 배운 것들

```python
# 10진수를 2진수로 변환하는 두 가지 방법의 차이점을 보자.
bin(10) 		# '0b1010'이 반환된다. 즉, bin()은 이진수 수식어인 '0b'가 붙는다.
format(10, 'b') # '1010'이 반환된다. bin()과 다르게 깔끔히 숫자 부분만 반환된다.
# 따라서, 문제의 경우에 따라 필요한 것을 골라서 쓸 수 있어야 한다.

# 다른 진수에서 10진수로 바꾸는 방법
int('1010', 2) # int(진수 문자열, 진수)를 통해서 10진수로 변환이 가능하다.

# 문자열 앞에 문자 채워넣기
# 저번에 배웠던 내용이나, 익숙하지가 않아 사용하지 못하였다. 외워두자.
binary += format(ord(c)-65, 'b').rjust(6, '0') # 오른쪽으로 정렬, 6자리 마련, '0'으로 채움
```



## 2021-02-04

+ Difficulty 2의 정답율순 3번 ~ 6번 문제를 풀었다.
+ **지그재그 숫자, 새로운 불면증 치료법, 수도 요금 경쟁, 초심자의 회문 검사**
+ **나머지, 배열, 중복 검사, 카운트, 회문**의 알고리즘을 익혀봤다.
+ 저번 보다는 쉬웠으나 민석이의 불면증이 매우 어려웠다.
+ 공백을 기준으로 입력을 받는 것들을 **리스트**가 아닌 **요소**들로 받고 싶을 때는 아래와 같이 직접 받아도 된다.

```python
P, Q, R, S, W = map(int, input().split())
```

+ **펠린드롬** 문제에서 별다른 제약사항이 없다면 빨리 푸는 방법

```python
word == word[::-1] # 단어와 거꾸로 읽은 것이 같은지 확인
```

+ 느낀점 및 배운 것들
  + 함수의 사용 때문에 주력 데이터 구조를 정하면 좋다고 한다.
    + ex) `set`과 `list`를 전부 쓰려다 보면 함수에서 헷갈릴 수 있으니, `list`만 사용하는 연습
  + 중복을 신경쓰지 않고 요소를 세는 방법의 접근
    + `set`을 사용하는 방법
    + `list`와 `.count()`를 사용하는 방법
    + `list`에 미리 전체 요소를 넣어놓고 해당 요소가 나올 때 마다 `.remove()`를 해서 빈 리스트가 될 때까지 하는 방법



## 2021-02-09

+ Difficulty 2의 정답율순 7번 ~ 10번 문제를 풀었다. **(10번은 못풀었다.) SWEA1979 꼭 다시** => **풀었다!**
+ **두 개의 숫자열, 날짜 계산기, 패턴 마디의 길이, 어디에 단어가 들어갈 수 있을까**
+ **슬라이딩 윈도우, 날짜 계산, 슬라이싱, 이중 배열**의 알고리즘을 배웠다.
+ 전체적으로 매우 어려웠다.
+ min과 max를 구하는 문제에서는 `float('inf')`를 활용해도 좋다.

```python
# 초기값 설정
max_num = float('-inf')
min_num = float('inf')
```

+ **그래도 min, max 초기값 설정은 내 SWEA D2_7_1959를 따르자! 이게 제일 좋은 것 같다.**

```python
for문 ~ :
    작업~
    if i == 0:
        max_num = temp_num
    if temp_num > max_num:
        max_num = temp_num
```

+ 구간을 나눠 비교해야 하는 문제는 마냥 index 접근보다는 **slicing**접근도 좋다!
+ 이중배열을 만들 때는 리스트 내포 기능을 사용해도 수월하다.

```python
alist = [list(map(int, input().split())) for i in range(n)]
```

+ 이중배열에서 행과 열의 스위칭에 주의하자(헷갈리지 말자)

```python
for i in range(n):
    for j in range(n):
        alist[i][j] # => 행 접근
        alist[j][i] # => 열 접근
```



## 2021-02-11

+ 백준 1단계 문제의 단계순 1번 ~ 11번 문제를 풀었다. 1단계 완료!
+ **Hello World출력, 격려의 문구, 고양이, 강아지, 더하기, 빼기, 곱하기, 나누기, 나머지, 곱셈의 과정**
+ 알고리즘의 기초가 되는 **사칙연산**의 매우 간단한 문제들이었다.
+ **나머지의 특성**과 **정수에서 각 자릿수를 가져오는 방식**이 이번 회의 포인트였다.

```python
# 나머지의 특성
(A+B) % C == ((A%C) + (B%C)) % C
(A*B) % C == ((A%C) * (B%C)) % C
```

```python
# 정수에서 각 자릿수를 가져오는 방식
while num > 0:
    num % 10 # 이게 각 자릿수가 된다.
    num //= 10
```

+ 느낀점 및 배운 것들
  + 기초가 탄탄해야 한다.
  + 앞으로의 모든 알고리즘에서 최대한 내장함수를 사용하지 않을 것이다.
  + 오늘 배운 이 기본 사칙연산들이 알고리즘의 근간이 될 것이다.



## 2021-02-13

+ 백준 2단계 문제의 단계순 1번 ~ 5번 문제를 풀었다. 2단계 완료!
+ **두 수 비교하기, 시험 성적, 윤년, 알람시계, 사분면 고르기**
+ **if문**에 대한 간단한 문제들이었다.
+ **분기를 어떻게 나누는가**는 코드의 길이와 불필요한 실행을 줄이는데에 직결된다.

```python
# x, y의 값을 입력받고 몇 사분면에 위치하는지 찾는 문제
# 단순히 x의 부호와 y의 부호를 하나하나 따져 찾는 방법
A = int(input())
B = int(input())

if A > 0 and B > 0:
    result = 1
elif A > 0 and B < 0:
    result = 4
elif A < 0 and B > 0:
    result = 2
else:
    result = 3
```

```python
# x와 y를 곱한 것을 토대로 찾는 방법
A = int(input())
B = int(input())
if A*B > 0 :
    if A > 0:
        result = 1
    else:
        result = 3
else:
    if A > 0:
        result = 4
    else:
        result = 2
```

+ 후자의 경우 **직관성**은 떨어질 수 있어도 **코드 작성이 줄고 편리하다.**
+ 줄이 더 많아보이는가? 그러나...

```python
# 후자의 코드를 삼항연산자로 표현하면
A = int(input())
B = int(input())
if A*B > 0 :
    result = 1 if A > 0 else 3
else:
    result = 4 if A > 0 else 2
```

+ **삼항연산자**를 사용하면 매우 간단하게 나타낼 수 있다.
+ 전자의 경우는 조건 자체가 길기 때문에 삼항연산자를 사용하더라도 코드가 지저분해진다.



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



## 2021-02-16

+ Difficulty 2의 정답율순 11번 ~ 17번 문제를 풀었다. SSAFY과정에서 푼 문제들 제외
+ **가랏! RC카!, 숫자 배열 회전, 스도쿠 검증, 시각 덧셈, 직사각형 길이 찾기**
+ 또 한번 매우 어려웠다.
+ **이차원 배열**을 활용하는 문제들이 킬링 문제들이었다.
  +  이차원 배열을 만들지 않고 풀 수 있다면 가장 좋다.
  + **직접 배열을 만들려고 들지 마라**
+ 코드의 복잡성을 피하기 위해 **함수화**를 생활화 하자.
+ **중복 검사**에서는 count 리스트를 계속 활용해왔지만 **set**을 사용하는 것이 가장 효율적이다.
+ 이하 중요한 내용들은 전부 코드에 있다.



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



## 2021-02-18

+ Difficulty 2의 정답율순 18번 ~ 25번 문제를 풀었다. SSAFY과정에서 푼 문제들 제외, **D2 완료!**
+ **파스칼의 삼각형, 간단한 369게임, 조교의 성적 메기기, 간단한 압축 풀기, 중간 평균값 구하기, 최빈수 구하기, 백만장자 프로젝트**
+ 역시 난이도가 높았다. 그러나, 배열에 관련된 문제를 많이 풀었어서 그런지 이해는 잘 된다.
+ **배열 활용, 나머지와 정수나눗셈 활용, 정렬, 카운트 리스트, 셀렉션(선택 정렬), 슬라이싱** 등 여러 알고리즘적 기법들을 사용해야 하는 문제들이었다.
+ **리스트에서 일정 구간을 옮겨다니거나/떼와서** 이용해야 하는 경우 **슬라이싱**을 사용하면 정말 편리하다. 복잡하게 가려고 하지말자!
+ **슬라이싱은 범위를 넘어가는 부분까지 참조를해도 요소가 있는 곳 까지만 알아서 잘라서 가져온다.** **(중요)**

```python
# D2_1946번 간단한 압축풀기

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 모든 알파벳을 주어지는 개수만큼 저장할 리스트
    arr = []
    for i in range(N):
        C, K = input().split()
        K = int(K)
        arr += [C]*K

    print('#%d' % t)
    i = 0
    # 알파벳들을 저장한 리스트에서 10개씩 슬라이싱해서 출력한다. 슬라이싱은 범위가 넘어가면 자동으로 요소가 존재하는 부분까지만 가져온다.
    while len(arr) > i:
        print(''.join(arr[i:i+10]))
        i += 10

# 이 문제에서 arr의 길이는 절대 10의 배수 단위가 아닐 수 있다. 하지만 10씩 끊어서 가져오는 반복문을 반복하면 알아서 10개씩 끊어오다가 마지막에 나머지만큼 끊어서 가져온다.
```

+ 느낀점 및 배운점
  + **제발 문제를 제대로 잘 보자**. 3,6,9 같은 문제는 문제를 제대로 안읽어서 40분을 낭비했다.
  + 슬슬 내장함수를 곁들여서 풀어도 괜찮을 것 같다.
  + 정렬을 오랜만에 다시 접하니 제대로 작성은 했지만 시간이 걸렸다. 더 익숙해지자.



## 2021-02-20

+ 싸피 Day03의 알고리즘 문제들을 복습하였다.
+ **두 개의 숫자열, 삼성시의 버스 노선**
+ **슬라이딩 윈도우, 카운트 리스트 활용** 등을 더 배웠다.
+ **횟수, 높이** 등을 묻는 문제에서 **주어진 조건**을 잘보자. **카운트 리스트의 길이**를 파악할 수 있다.
+ 주어진 입력의 순서대로 코드를 처리할 수 있는지를 파악하자. 모든걸 다 저장해놓고 쓰려하지 마라.



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



## 2021-02-23

+ Difficulty 3의 정답율순 1번 ~ 5번 문제를 풀었다.
+ **준환이의 운동관리, 거듭 제곱(재귀), 회문1, 암호문3, 모음이 보이지 않는 사람**
+ **조건표현식, 재귀, 이중 배열, 회문, string, 슬라이싱** 등의 알고리즘적 기법들을 사용해야 하는 문제들이었다.
+ 회문을 찾는 경우 `N-M+1`이라는 것과 `arr[i][j+k] != arr[i][j+M-1-k]`가 정말 자주 쓰일 것이다.
  + 혹은 `arr[i+j] != arr[i+M-1-j]`

```python
# D3_1215번 회문1

# 한 행에 대해 길이가 M인 팰린드롬의 개수를 찾는 함수
def palindrome(string):
    cnt = 0
    for i in range(N-M+1):
        for j in range(M//2):
            if string[i+j] != string[i+M-1-j]:
                break
        else:
            cnt += 1

    return cnt


for t in range(1, 11):
    # N = 정사각형 이중배열 한 변의 길이, M = 회문의 길이
    N, M = 8, int(input())
    arr = [input() for _ in range(N)]
    cnt = 0
    for i in range(N):
        # 가로 검사와 세로 검사를 차례로 하겠다. zip(*arr)을 통해 행열을 전환한다.
        for temp_arr in arr, zip(*arr):
            # 다만 zip(*arr)에서 가져오는 string은 사실 type이 tuple이다.
            for string in temp_arr:
                cnt += palindrome(string)

    print('#%d %d' %(t, cnt))
```

+ 느낀점 및 배운점
  + **제발 문제를 제대로 잘 보자**. 암호문3도 어렵지 않은데 fail을 한 번 했다.
  + 그 외에 문제적으로 어려운 것은 딱히 없었다.
  + `zip`에 대한 특성을 한 번 idle을 통해 알아보았다.

```python
>>> arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

>>> zip(*arr)
<zip object at 0x0000020C7D49BC40>

>>> for row in zip(*arr):
    print(row)

(0, 0, 0)
(0, 0, 0)
(0, 0, 0)

>>> for row in zip(*arr):
    print(type(row), row)
    
<class 'tuple'> (0, 0, 0) # zip의 내용물은 전부 타입이 tuple로 되어있다.
<class 'tuple'> (0, 0, 0)
<class 'tuple'> (0, 0, 0)

>>> type(zip(*arr))
<class 'zip'>

>>> zip(*arr)[0] # 가장 신기한 부분은 zip이 iterable하면서, 인덱싱은 안된다는 것이다. generator의 특성인 것일까?
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    zip(*arr)[0]
TypeError: 'zip' object is not subscriptable
```



## 2021-02-25

+ 삼성 소프트웨어 역량 시험 IM대비로 기존에 풀었던 문제들을 리뷰했다.
+ **영준이의 카드 카운팅, 오목 판정, 원재의 메모리 복구하기, 퍼펙트 셔플, 농작물 수확하기, 쇠막대기 자르기, 백만장자 프로젝트, 자기 방으로 돌아가기, 진기의 최고급 붕어빵, 재미있는 오르셀 게임**

+ 이중 배열에 있어서 인덱스를 계산하는 것이 매우 까다롭고 실수할 여지가 많다. **실제 손으로 써가며 풀어보자.**

+ 이제 대부분의 알고리즘 문제들은 단순히 문제의 흐름대로 코드를 쭉 짜기보다는 그 속에서 숨어있는 규칙을 찾거나 가장 효율적인 알고리즘을 찾아야 한다.
  + 백만장자 프로젝트 같은 경우, 주어진 데이터를 거꾸로 읽어야 효율적이다.
  + 붕어빵의 경우 실제 문제의 상황을 코드로 구현하는 것이 아니라, 답을 빠르게 구할 수 있도록 상황을 정리하여 코딩해야 한다.
  + 오르셀과 같은 경우, 게임을 코드로 구현해야 하는데 말로 풀어놓은 게임 규칙을 그대로 코드에 어떻게 가장 효율적으로 구현할 수 있는가를 생각해야 했다.