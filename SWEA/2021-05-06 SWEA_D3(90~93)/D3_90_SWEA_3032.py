# 홍준이의 숫자 놀이
# 숫자를 좋아하는 홍준이는 다음과 같은 놀이를 하고 있다.
# 서로소인 두 자연수 A와 B를 정한 후, Ax + By = 1이 되는 x와 y를 계산하는 것이다.
# 홍준이는 A와 B가 작을 때에는 암산으로 쉽게 계산할 수 있었는데, 두 수가 클 때의 계산에는 어려움을 느끼고 있다.
# 여러분은 홍준이를 도와, 두 자연수 A와 B가 주어졌을 때에 Ax + By = 1이 되는 x와 y를 계산하는 프로그램을 작성하시오.


# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 10,000)
# 각 테스트케이스의 첫째 줄에 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10^9)


# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(테스트케이스 번호) “를 출력하고, Ax + By = 1이 되는 x와 y를 출력한다.
# 가능한 x와 y 쌍이 유일하지 않다면, 아무것이나 출력해도 된다.
# 가능한 해가 없는 경우에는 -1을 출력한다.


# 1
# 런타임에러
for t in range(1, int(input())+1):
    A, B = map(int, input().split())
    if A == 1:
        result = '1 0'
    elif B == 1:
        result = '0 1'
    else:
        mul = A * B
        A_list = [x for x in range(A, mul+1, A) if x <= mul]
        B_list = [x for x in range(B, mul+1, B) if x <= mul]
        A_i, B_i = 0, 0
        while A_i < len(A_list) and B_i < len(B_list):
            if abs(A_list[A_i] - B_list[B_i]) == 1:
                result = '%d %d' % (A_i + 1, -(B_i + 1)) if A_list[A_i] > B_list[B_i] else '%d %d' % (-(A_i + 1), B_i+1)
                break
            elif A_list[A_i] > B_list[B_i]:
                B_i += 1
            else:
                A_i += 1
        else:
            result = '-1'

    print('#%d %s' % (t, result))


# 2
# 확장 유클리드 정리
def euclid(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    return [x, y]


for t in range(1, int(input())+1):
    A, B = map(int, input().split())
    print("#%d %s" % (t, ' '.join(map(str, euclid(A, B)))))