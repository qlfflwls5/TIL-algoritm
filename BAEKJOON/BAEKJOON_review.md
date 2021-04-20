# BAEKJOON_review

> BAEKJOON ONLINE JUDGE https://www.acmicpc.net/

<br/>

<br/>

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

<br/>

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

<br/>

## 2021-03-30

+ 백준 특강 문제들을 풀었다.
+ **제곱근, 소풍, 요세푸스 문제 3, 골드바흐 파티션**
+ 정말 한 문제도 풀지 못했다. 백준에서 각각 난이도 브론즈1, 실버2, 골드1, 플레티넘의 난이도를 하는 문제들이라고 한다.
+ 약간의 좌절감을 맛보았다... 주말에 다시 풀어냈으나 푸는 방법의 리뷰를 들은 것이라 나중에 잊혀질 때쯤 다시 도전해 봐야겠다.

<br/>

## 2021-04-09

+ 알고리즘 과목평가를 위한 대비 문제로 백준의 2178번을 풀었다.

+ **미로 탐색**

+ **BFS**의 알고리즘을 사용해 풀어야 하는 문제들이었다.

+ 주어진 미로의 좌상단에서 우하단까지 가는 최단 거리를 구하는 것이다.

  + 평소처럼 BFS로 풀었으나 시간 초과가 발생했다! -> 왜?

+ 평소의 풀이

  + ```python
    drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    queue = [(0, 0, 1)]
    while queue:
        r, c, cnt = queue.pop(0)
        if r == N - 1 and c == M - 1:
            print(cnt)
            break
        visited[r][c] = 1
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc]:
                queue.append((nr, nc, cnt+1))
    ```

  + 즉, queue안에 (행, 열, 거리)의 정보가 담기게 된다.

  + 혹시나 `deque()`를 사용하면 빨리 풀릴까 하여 `from collections import deque`를 하고 `queue = deque()`와 `queue.popleft()`를 사용해 풀어봤지만 이번엔 메모리 초과가 발생했다.

    + 'queue에 세 번째 값으로 거리를 하나 더 주는 것이 문제인가?'라는 생각을 했다.

+ 수정한 정답의 풀이

  + ```python
    from collections import deque
    
    
    drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        r, c = queue.popleft()
        if r == N - 1 and c == M - 1:
            print(visited[N-1][M-1])
            break
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    ```

  + 예상이 맞았다. 거리의 계산을 queue의 세 번째 값을 1씩 더해가며 구하는 것이 아닌, **visited**를 이용하여 BFS 한 단계마다 visited의 값을 1씩 늘려 저장하는 식으로 구현하니 문제가 없었다.

+ 느낀점 및 배운점

  + 처음 BFS를 통해 최단거리를 구하는 문제를 풀 때, queue의 세 번째 값으로 아예 거리값을 계속 갱신해서 넣어주는 풀이와 visited를 이용해서 visited가 1씩 누적하여 올라가는 풀이 두 가지를 배웠는데 무슨 차이인지 배우지는 않았었다.
  + 하지만 이번 문제를 통해서  값을 하나 더 넘겨주는 방식은 안전하지 않다는 것을 알았다.
    + 정말 안타깝게도 이유가 무엇인지는 잘 모르겠다.
    + python의 `time`을 통해서 두 가지 방법일 경우의 코드 실행시간을 찍어봤는데, 비슷하다...
      + 아마 테스트 케이스의 차이일 수도 있겠지만, 백준 내부의 테스트 케이스를 모르므로 일단은 재귀나 반복의 구조에서 가능하면 **데이터의 구조**를 건드리지 말고 값만 샥 바꿀 수 있는 것을 택하자.
        + 데이터의 구조란 queue를 말하는 것이고, 값이란 visited의 각 값을 말한 것

