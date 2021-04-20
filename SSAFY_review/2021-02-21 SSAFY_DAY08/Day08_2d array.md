# 2021.02.19_0218문제풀이





## 새롭게 배운 것들



## 1. 회문2

+ 나는 특이한 방법으로 각 요소에 대해 양옆으로 확장해 나가며 회문을 찾는 알고리즘을 작성했다.
  + 다행히 실행시간도 제일 빠르고 효율적인 코드였다!
+ 하지만, 어떤 상황이 올지 모르므로 일반적인 회문을 찾는 법을 코드로 짜보자
  + 회문의 길이를 모르므로 회문이 **가장 길 때(len(string))부터 짧을 때(1)까지를 역으로 range**하여 각 길이에 대해서 회문을 탐색하는 방법
  + 이 때 회문 검사는 평소에 하던대로 **길이//2**만큼만 앞뒤로 비교하면 될 것이다.

```python
def my_find(M):
    # 전체크기가 N이다.
    for i in range(N):
        for j in range(N-M+1):
            # 스왑 통한 회문 검사
            # 가로 검사
            for k in range(M//2):
                # 앞뒤검사
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                # 회문임
                elif k == M//2 - 1:
                    return M
            # 세로 검사
            for k in range(M//2):
                if words[j+k][i] != words[j+M-1-k][i]:
                    break
                elif k == M//2 - 1:
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
```





## 2. 글자수

+ 패턴 찾기에서 요소 하나하나를 찾는 것 같은 경우, **즉 요소 하나하나를 인덱스나 패턴처럼 사용해야 할 경우**

+ 무조건 **딕셔너리**를 사용하는 것이 좋다!
+ SWEA의 글자수 같은 문제가 해당된다.
+ 혹은 카운트 리스트를 활용한다. 이는 조금 복잡하고 더 느릴 수도 있다.

```python
# live에서의 딕셔너리 활용 방법
T = int(imput())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    
    # 키 = 문자, value = 카운트한 수
    my_dict = {}
    
    # set으로 중복을 막고자
    for key in set(str1):
        my_dict[key] = 0
    
    for key in str2:
        if key in my_dict:
            my_dict[key] += 1
    
    ans = 0
    for value in my_dict.values():
        if value > ans:
            ans = value
    
    print(ans)
    

# live에서의 카운트 리스트 활용 방법
T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    
    # 이 부분이 중요하다. 카운트 리스트와 str1의 인덱스가 대응하므로 str[0]의 개수는 cnt_list[0]이다.
    cnt_list = [0]*len(str1)
    
    # 검색 실시
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt_list[i] += 1
    
    ans = 0
    for cnt in cnt_list:
        if ans < cnt:
            ans = cnt
    
    print(ans)
```







## 3. 숫자배열 회전

