# 100만 이하의 모든 소수
# 1 이상 100만(10^6) 이하의 모든 소수를 구하는 프로그램을 작성하시오.
# 참고로, 10 이하의 소수는 2, 3, 5, 7 이다.


# [입력]
# 이 문제의 입력은 없다.


# [출력]
# 1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.


# 현재의 수를 기준으로 10**6까지 사이에 있는 모든 배수를 다 지우면서 진행한다.
num = [0, 0] + [1] * (10**6 - 1)
for i in range(2, 10**6+1):
    if num[i]:
        print(i, end=' ')
        for j in range(i*2, 10**6+1, i):
            num[j] = 0


# 2
# 약수를 확인할 때는 본인의 루트 값 까지만 알면 된다.
def isprime(x):
    for prime in prime_list:
        # 루트를 넘어서면 나눠지지 않는 것이다.
        if prime**2 > x:
            break
        if x % prime == 0:
            return False
    return True


prime_list = [2]
for n in range(3, 1000001):
    if isprime(n):
        prime_list.append(n)
print(*prime_list)