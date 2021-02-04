# 지그재그 숫자
# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.


# [예제 풀이]
# N이 5일 경우,
# 1 – 2 + 3 – 4 + 5 = 3
# N이 6일 경우,
# 1 – 2 + 3 – 4 + 5 – 6 = -3


# [제약사항]
# N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.


# [출력]
# 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 누적된 값을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 입력
# 2
# 5
# 6
 

#  출력
# #1 3
# #2 -3


T = int(input())
for k in range(1, T + 1):
    # 결과값으로 만들 변수를 생성하고 값을 0으로 초기화
    total = 0
    n = int(input())
    # 1부터 n까지 홀 수면 total에 더하고 짝수면 total에서 뺀다.
    for i in range(1, n + 1):
        if i % 2:
            total += i
        else:
            total -= i
    
    print(f'#{k} {total}')