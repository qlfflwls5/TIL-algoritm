# 2021.02.23_0222복습_DFS





## 새롭게 배운 것들



## 1. statement & expression

+ statement
  + simple statement
    + `;`를 이용해서 한 줄에 여러 개를 나열할 수 있다.
    + expression : 1개의 **object**로 표현될 수 있는 것
      + 상수, 이름, 연산자를 포함한 식(거듭제곱, 산술, 비교, 논리, 비트), 호출식, lambda식, 조건표현식
    + expression이 아닌 simple statement: =, +=, break, continue, return, ...
  + compound statement
    + `:`으로 header를 마무리하고, 다음줄에 들여쓰기해서 block을 만들 수 있다.
    + if문, for문, while문 등



+ expression을 사용할 수 있는 위치
  + 이름 = expression
  + return expression
  + 함수(argument)의 argument



+ `(lambda x : x + 10)(5)`: 15가 나올 것
  + 여기서 `()`의 역할은 **객체화**하는 것
  + 객체화가 된다는 것은 `.`을 찍거나 기타 가능한 연산을 할 수 있다는 것







## 2. 슬라이싱, UnboundLocalError (중요)

```python
a = [1, 2]

def func():
    a.append(3)
    a[0] = 100
    a[1:2] = [10, 20, 30, 40]

    
func()
print(a) # [100, 10, 20, 30, 40, 3]
# a[1:2]의 범위가 [10, 20, 30, 40]이 된 것이다. (중요)
# 즉 슬라이싱은, 범위를 범위로 바꿀 수 있다.


a = [1, 2]

def func():
    b, c = 1, 2
    a.append(3)
    a[0] = 100
    a[1:2] = [10, 20, 30, 40]
    a = a[::-1]


func() # 에러 -> a = a[::-1]에서 새로운 지역변수가 생긴다.
# func()를 호출하는 동시에 local namespace가 생성 {'b': ?, 'c': ?, 'a': ?} 값은 모르는 채로 일단 지역변수를 지정
# 그 후 a.append(3)을 할 때 지역변수 a는 아직 값이 bounding되어있지 않기 때문에 append를 수행할 수 없는 것이다. unbounderror
# 즉, 문제가 생긴 이유는 지역변수를 만든 a = a[::-1]이지만, 에러는 그전에 발생할 수도 있다.
```







## 3. DFS

+ DFS 반복

```python
# live 중 DFS 연습문제 3
# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오.
# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7


# DFS 반복
V, E = 7, 8
# 입력이 아래와 같다면
edges = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
edges = list(map(int, edges.split())) # input().split()으로 쓰게 될 것
edges = [(edges[i], edges[i+1]) for i in range(0, len(edges), 2)]
# 입력이 아래와 같다면
# 7 8
# 1 2
# 1 3
# 2 4
# 3 5
# 4 6
# 5 6
# 6 7
# 3 7
# edges = [tuple(map(int, input().split())) for _ in range(E)]


# 인접행렬
AM = [[0]*(V+1) for _ in range(V+1)]
for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1 # 방향성이 없을 때만 이 문장이 추가된다.


# 인접리스트
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s) # 방향성이 없을 때만 이 문장이 추가된다.


# 스택 함수 => 실제 문제 풀 때는 가장 위에 적게 될 것
def push(stack, v):
    stack.append(v)


def pop(stack):
    if len(stack) == 0:
        return

    return stack.pop(-1)


# DFS 구현
stack = []
visited = [False]*(V+1)
# 경로를 저장할 리스트
way = []
# 정점 1부터 시작한다했으므로
push(stack, 1) # 그냥 append 사용해도 된다.
while len(stack):
    v = pop(stack) # 그냥 pop 사용해도 된다. while문 조건에서 어차피 길이가 0이면 걸러진다.
    if not visited[v]:
        visited[v] = True
        way.append(v)
        for w in AL[v]:
            if not visited[w]:
                push(stack, w)
        # 인접 행렬을 사용하는 경우
        # for w in range(AM[v]):
        #     if AM[v][w] and not visited[w]:
        #         push(stack, w)

print(way)
```

+ DFS 재귀

```python
# live 중 DFS 연습문제 3
# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오.
# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7


# DFS 재귀
V, E = 7, 8
# 입력이 아래와 같다면
edges = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
edges = list(map(int, edges.split())) # input().split()으로 쓰게 될 것
edges = [(edges[i], edges[i+1]) for i in range(0, len(edges), 2)]
# 입력이 아래와 같다면
# 7 8
# 1 2
# 1 3
# 2 4
# 3 5
# 4 6
# 5 6
# 6 7
# 3 7
# edges = [tuple(map(int, input().split())) for _ in range(E)]


# 인접행렬
AM = [[0]*(V+1) for _ in range(V+1)]
for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1 # 방향성이 없을 때만 이 문장이 추가된다.


# 인접리스트
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s) # 방향성이 없을 때만 이 문장이 추가된다.


# DFS 재귀 구현
# 반복에서와 다르게 v는 방문되지 않은 정점으로, 방문하러 들어온 것
# visited[v] = 1 -> 방문처리를 한다.
# 방문하지 않은 인접요소들을 찾아 DFS를 재호출
# 문제는 visited다. 여러 테스트 케이스를 받으면 각 테스트 케이스마다 visited를 초기화 해야 할 것
def DFS(AL, v):
    visited[v] = 1
    way.append(v)

    for w in AL[v]:
        if not visited[w]:
            DFS(AL, w)
            
            
visited = [0]*(V+1)
way = []
DFS(AL, 1)
print(way)
```

