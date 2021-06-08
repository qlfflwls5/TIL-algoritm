# 나는 개구리로소이다
# 개구리 한 마리가 한번 울면 “croak”하는 소리가 난다. 개구리 한 마리가 계속 여러 번 울면 울음소리가 다음처럼 나타날 수 있다.
# “croakcroak”, “croak”, “croakcroakcroakcroak”
# 영은이는 개구리를 연구하기 위해 많은 개구리를 사육한다. 영은이는 개구리들을 키우는 우리에 들어와 울음소리를 녹음했다.
# 여러 개구리가 동시에 울면 울음소리가 섞여서 녹음된다.
# 이 때 한 개구리의 울음소리는 녹음된 울음소리에서 부분 문자열로 나타난다. 이 부분 문자열은 연속하지 않아도 된다. 예를 들어 "crcoarkcoroakak"와 같을 수 있다.
# 그렇다면, 녹음을 할 때 있었던 개구리는 최소 몇 마리일까?


# [입력]
# 첫 번째 줄에 테스트 케이스의 수가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 개구리들의 울음소리를 나타내는 길이 5 이상 2,500이하인 문자열이 주어진다. 이 문자열은 ‘c’, ‘r’, ‘o’, ‘a’, ‘k’로만 이루어져 있다.


# [출력]
# 각 테스트 케이스마다 첫번째 줄에는 ‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다.)를 출력하고, 개구리의 최소 수를 출력한다.
# 개구리의 울음소리로 불가능한 경우 -1을 출력하면 된다.


for t in range(1, int(input())+1):
    W = input()
    result = 0
    c, r, o, a, k = 0, 0, 0, 0, 0
    pre_k = 0
    for w in W:
        if w == 'c':
            c += 1
            result += 1
            # croakccrrooaakk와 같은 경우를 해결하기 위해서 pre_k가 필요
            if pre_k:
                result -= 1
                pre_k -= 1
        elif w == 'r' and c > r:
            r += 1
        elif w == 'o' and r > o:
            o += 1
        elif w == 'a' and o > a:
            a += 1
        elif w == 'k' and a > k:
            k += 1
            pre_k += 1
        else:
            result = -1
            break

    if not c == r == o == a == k:
        result = -1

    print('#%d %d' % (t, result))