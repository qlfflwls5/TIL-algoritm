# 2021.02.09_0208풀이





## 새롭게 배운 것들



## 1. View 숙제 풀이

+ max함수 구현

```python
def get_max(*args):
    max_num = args[0]
    for arg in args:
        if arg > max_num:
            max_num = arg
    return max_num

...
x = builds[i-2], builds[i-1], builds[i+1], builds[i+2]
a = builds[i] - get_maximum(x)
```

+ **근데 지금 이 문제에서는 주변 2칸의 빌딩들의 최대값을 구하기 위해 저 `*args`에 넣으면 에러가 난다!**

  + `arg`부분이 `tuple`타입으로 들어오기 때문에 비교가 안된다. 왜?
  + **네 개의 빌딩 값이 하나의 튜플로 묶여서, 그 튜플 자체가 args의 한 요소로 들어온다.**
  + 해결 방법:
  + `a = builds[i] - get_maximum[*x]`  **x앞에 *을 붙여준다.**

  + **x에다가 넣는 과정에서 x가 튜플이 되기 때문이다.**

+ **조건표현식을 잘 활용하자** => 코드를 간결하게 하는 비법





## 2. Min, Max 함수

+ min, max 함수 만들 때 0번째를 제외한 1번째부터 끝까지를 나타내는 방법
+ **args[1:]를 쓰면 된다. range(1, len(args)) 하지말고!**

```python
def get_max(*args):
    max_num = args[0]
    # 이부분
    for i in range(1, len(args)):
        if args[i] > max_num:
            max_num = args[i]
    return max_num
```

+ **정렬**을 해서 0번째와 마지막번째의 차이를 구하는 것도 좋겠다!
+ 버블 정렬

```python
# 기존과 range안에만 바꿔보기
for i in range(N-1):
    for j in range(N-i-1):
        if nums[j] > nums[j+1]:
            ...
```



---

이하 코드로 TIL