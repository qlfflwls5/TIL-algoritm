# 이진 문자열 복원
# 동욱이는 어떤 길이가 N인 어떤 이진 문자열을 가지고 있었다.
# 이진 문자열은 ‘0’ 또는 ‘1’의 두 문자로 이루어진 문자열인데, 동욱이는 원래 문자열이 무엇인지 까먹어 버렸다.
# 이렇게 원래의 문자열을 까먹는 일이 많은 동욱이는 원래의 문자열을 복원해 내기 위한 정보를 만들어 놓았고,
# 그 정보는 인접한 두 문자를 끊어 봤을 때 각각의 쌍이 몇 번씩 등장하는지를 적어 놓은 것이다.
# 단, 인접한 두 문자를 끊어 볼 때 두칸씩 이동하지 않고 한칸만 이동하여 본다.
# 예를 들어 “01000110”는 인접한 두 문자를 끊어 봤을 때, “01”, “10”, “00”, “00”, “01”, “11”, “10”의 일곱 가지의 문자열이 있고
# 동욱이는 이를 “00” 두 개, “01” 두 개, “10” 두 개, “11” 한 개로 적어 놓은 것이다.
# 동욱이를 도와 이런 정보가 주어졌을 때 원래 문자열로 가능한 문자열이 있는지 없는지 판별하고 만약 있다면 가능한 것 중 하나를 아무거나 출력하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 네 정수 A,B,C,D (0 ≤ A,B,C,D ≤ 20)가 공백으로 구분되어 주어진다. 순서대로 “00”, “01”, “10”, “11”의 개수를 의미한다. A+B+C+D ≥ 1임이 보장된다.


# [출력]
# 각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 조건을 만족하는 이진 문자열 중 아무거나 하나를 출력한다. 만약 조건을 만족하는 문자열이 없다면 “impossible”을 출력한다.


for t in range(1, int(input())+1):
    A, B, C, D = map(int, input().split())
    if A and not B and not C and not D:
        result = '0'*(A+1)
    elif D and not A and not B and not C:
        result = '1'*(D+1)
    elif B == C and B:
        result = '0'*(A+1) + '10'*(B-1) + '1'*(D+1) + '0'
    elif B - C == 1:
        result = '0'*(A+1) + '10'*C + '1'*(D+1)
    elif C - B == 1:
        result = '1'*(D+1) + '01'*B + '0'*(A+1)
    else:
        result = 'impossible'

    print('#%d %s' % (t, result))
