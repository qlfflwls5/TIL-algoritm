# 2021.02.10_0209풀이+문제들





## 새롭게 배운 것들



## 1. min max

```python
# 정렬을 해서 맨 앞과 맨 뒤
def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
T = int(input())

for t in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    Bubble_sort(number)
    print('#{} {}'.format(t, number[-1]-number[0]))
```

```python
# 순회를 하며 min과 max 일일이 비교
T = int(input())

for t in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    
    max_v = float('-inf')
    min_v = float('inf')
    
    for i in range(N):
        if max_v < number[i]:
            max_v = number[i]
        if min_v > number[i]:
            min_v = number[i]
    print('#{} {}'.format(t, max_v-min_v))
```







## 2. 전기 버스

+ 매 i마다 3칸 뒤 부터 시작하여 3칸 뒤가 정류소인지, 2칸 뒤가 정류소인지, 1칸 뒤가 정류소인지 찾는 법
+ 팁

```python
charge = [0] + charge + [N]
# 이건
# charge.insert(0, 0)
# charge.append(N)
# 과 같다.
```

+ 라이브 답안

```python 
T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    
    charge = list(map(int, input().split()))
    ans = 0
    
    charge = [0] + charge + [N] # [0, 1, 3, 5, 7, 9, 10]과 같이 만든다.
   	last = 0
    
    # 충전소에 출발점과 도착점을 넣었으니 M+2
    for i in range(1, M+2):
        if charge[i] - charge[i-1] > K:
            ans = 0
            break
        
        # 갈 수 있다면 아무 작업x
        # 갈 수 없다면 내 바로 직전 충전소로 위치 옮기고 횟수 1 증가
        if charge[i] > last + K:
            last = charge[i-1]
            ans +=1
    print('#{} {}'.format(t, ans))
            
```







## 3. 구간합

+ 슬라이딩 윈도우로 푼다.
+ 빠져 나가는 값을 빼고 새로 들어오는 값을 더해가는 식으로







## 4. Flatten

+ 내가 했던 방법
+ 버블정렬 방법 - 박스들을 전부 정렬하는 것

```python
def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
for t in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    
    for i in range(N):
        Bubble_sort(box)
        box[0] += 1
        box[-1] -= 1
    
    Bubble_sort(box)
```

+ **count 리스트를 이용하는 방법**

+ 제일 높은 높이의 인덱스가 하나 줄고 두 번째로 높은 높이의 인덱스가 하나 늘고, 제일 낮은 높이의 인덱스가 하나 줄고 두 번째로 낮은 높이의 인덱스가 하나 느는 것을 반복해서 count 리스트의 길이가 2 이하면 평탄화가 된 것
+ ex) 8이 제일 높은 높이고 1이 제일 낮은 높이면 8에서 1을 주면 높이가 8, 1인 count는 1이 줄고, 높이가 7, 2인 count는 1이 늘어난다.

```python
for t in range(1, 11):
    N = int(input())
    box = list(map(int, input()))
    
    # 높이 카운트 리스트
    h_cnt = [0]*101
    
    # 초기화
    min_value = 100
    max_value = 1 # 최저의 높이는 0이 아니라 1이다.
    
    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾아보자.
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]
            
     while N > 0 and min_value < max_value-1:
        # 상자 옮기기
        h_cnt[min_value] -= 1
        h_cnt[min_value + 1] += 1
        
        h_cnt[max_value] -=1
        h_cnt[max_value - 1] += 1
        
        # 포인터를 변경하자.
        if h_cnt[min_value] == 0:
            min_value += 1
            
        if h_cnt[max_value] == 0:
            max_value -=1
        
        # 덤프 줄이기
        N -= 1
        
        print(max_value - min_value)
```







## 5. 삼성시의 버스 노선

+ 문제를 잘 읽어라. 문제에서 주는 조건은 훨씬 풀이를 쉽게 만든다.

```python
T = int(input())
for i in range(1, T+1):
    N = int(input())
    bus_stop = [0]*5001
    
    for i in range(N):
        A, B = map(int, input().split())
        
        # 해당 정류장에 지나는 버스의 대수 누적
        for j in range(A, B+1):
            bus_stop[j] += 1
            
    P = in(input()) # 우리가 확인하고 싶은 버스정류장의 수
    
    print('#{}'.format(t), end='')
    for i in range(P):
        C = int(input()) # 우리가 확인하고 싶은 정류장의 번호
        print(bus_stop[C], end='')
    print()
```

+ **두 개의 숫자열과 삼성시의 버스 노선은 무조건 외워야 한다.**