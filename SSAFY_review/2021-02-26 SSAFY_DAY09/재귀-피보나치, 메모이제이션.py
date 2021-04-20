# 그냥 일반적인 피보나치 수열 재귀호출 방법
def f(n):
    if n < 2:
        return n

    return f(n - 1) + f(n - 2)
# 그러나, 이 방법은 같은 수행을 너무 반복하기 때문에 40만 넘어가도 함수가 실행이 안된다.


# 메모이제이션을 통한 재귀 피보나치
# memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다.
# memo[0]을 0으로 memo[1]은 1로 초기화 한다.
def fibo(n):
    global memo
    # len(memo) > n이라면 이미 값이 구해져있다는 뜻이다.
    # len(memo) < n이라면 아직 값을 구하지 않았다는 뜻이다. 그 아래 단계 피보가 먼저 실행된다.
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
fibo(40)
print(memo)


# 메모이제이션 2
# 메모의 길이가 정해져있는 경우
memo2 = [-1]*21
memo2[0] = 0
memo2[1] = 1

# 20까지만 가능하다.
def fibo2(n):
    if memo2 [n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)

    return memo2[n]


print(fibo2(10))
print(memo2)


# DP 적용한 알고리즘
def fibo2(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]