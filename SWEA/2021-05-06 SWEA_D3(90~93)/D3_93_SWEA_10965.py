# 제곱수 만들기
# 어떤 자연수 A가 주어진다. 여기에 자연수 B를 곱한 결과가 거듭제곱수가 되는 최소의 B를 구하는 프로그램을 작성하라. 여기서 자연수는 1이상인 정수를 뜻한다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T 가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 A(1≤A≤10^7) 가 주어진다.


# [출력]
# 각 테스트 케이스마다 A에 곱한 결과가 거듭제곱수가 되는 최소의 자연수를 출력한다.


# 채은님 코드
# 이 문제는 못풀었다.
prime_list = []
for i in range(2, int(10 ** (7 / 2))):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_list.append(i)

result = []
T = int(input())
for t in range(1, T + 1):
    A = int(input())
    B = 1
    if A ** (1 / 2) != int(A ** (1 / 2)):
        # 소인수분해 해서 지수를 짝수로
        for prime in prime_list:
            cnt = 0
            # 해당 소수로 나눠지지 않을 때까지
            while not A % prime and A >= prime:
                A //= prime
                cnt += 1
            # 해당 소수의 지수가 홀수이면 B에 곱해주기
            if cnt % 2:
                B *= prime
        # 남은 A까지 곱해줘야 B 완성
        B *= A
    result.append('#%d %d' % (t, B))
print('\n'.join(result))