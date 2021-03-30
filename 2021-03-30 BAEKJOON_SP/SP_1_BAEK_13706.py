# 제곱근
# 정수 N이 주어졌을 때, N의 제곱근을 구하는 프로그램을 작성하시오.


# [입력]
# 첫째 줄에 양의 정수 N이 주어진다. 정수 N의 제곱근은 항상 정수이며, N의 길이는 800자리를 넘지 않는다.


# [출력]
# 첫째 줄에 정수 N의 제곱근을 출력한다.


# 0
# 마지막으로 다시 푼 것
N = int(input())
start, end = 0, 10**((len(str(N))+1)//2)
while True:
    middle = (start + end) // 2
    if middle**2 > N:
        end = middle - 1
    elif middle**2 < N:
        start = middle + 1
    else:
        print(middle)
        break


# 1
# 런타임에러
N = int(input())
L = len(str(N))
num = [0, 0] + [1] * (10**((L+1)//2)-1)
result = 1
for i in range(2, 10**((L+1)//2)+1):
    if num[i] and N % i == 0:
        temp = 0
        while N % i == 0:
            N //= i
            temp += 1
        result *= i * temp // 2
        for j in range(i*2, 10**((L+1)//2)+1, i):
            num[j] = 0

print(result)


# 2
# 이진탐색
N = int(input())
a, b = 1, 10**400
while True:
    mid = (a+b)//2
    if mid**2 == N:
        break
    elif mid**2 > N:
        b = mid
    else:
        a = mid
print(mid)