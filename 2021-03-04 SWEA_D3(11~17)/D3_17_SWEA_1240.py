# 단순 2진 암호코드
# 어떤 국가에서는 자국 내 방송국에서 스파이가 활동하는 사실을 알아냈다. 스파이는 영상물에 암호 코드를 삽입하여 송출하고 있었다.
# 암호 코드는 국가 내 중요 시설을 의미하는 숫자임을 알아냈다. 암호 코드의 규칙은 아래와 같다.

# 1. 총 8개의 숫자로 이루어져 있다.
# 2. 앞 7자리는 상품 고유의 번호를 나타내며, 마지막 자리는 검증 코드를 나타낸다.
#     - 검증코드는 아래와 같은 방법으로 계산한다.
#     “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.
#     상품 고유의 번호가 8801234일 경우,
#     “( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 ) + 검증 코드”
#     = “42 + 12 + 검증 코드”
#     = “54 + 검증 코드” 가 10 의 배수가 되어야 하므로, 검증코드는 6이 되어야 한다.

#     즉, 88012346 이 정상적인 암호코드고, 그 외의 검증코드가 포함된 경우 비정상적인 암호코드다.

# A 업체에서는 이 암호코드들을 빠르고 정확하게 인식할 수 있는 스캐너를 개발하려고 한다. 스캐너의 성능은 아래와 같은 방법으로 측정된다.

# 1. 세로 50. 가로 100 이하의 크기를 가진 직사각형 배열에 암호코드 정보가 포함되어 전달된다.
#    이 때, 하나의 배열에는 1개의 암호코드가 존재한다. (단, 모든 암호코드가 정상적인 암호코드임을 보장할 수 없다. 비정상적인 암호코드가 포함될 수 있다.)
# 2. 배열은 1, 0으로 이루어져 있으며 그 안에 포함되어 있는 암호코드 정보를 확인한다.
# 3. 포함된 암호코드들의 검증코드를 확인하여 정상적인 암호코드인지 확인한다.
# 4. 정상적인 암호코드들을 판별한 뒤 이 암호코드들에 적혀있는 숫자들의 합을 출력한다.
# 5. 이때, 총 소요시간이 적을수록 성능이 좋은 것으로 간주된다.

# 배열에 포함되어 있는 암호코드의 세부 규칙은 아래와 같다.

# 1. 암호코드 하나는 숫자 8개로 구성되며 시작 구분선, 종료 구분선은 별도로 존재하지 않는다.
# 2. 암호코드가 일부만 표시된 경우는 없다. 모든 암호코드는 8개의 숫자로 구성되어 있다.
# 3. 암호코드의 세로 길이는 5 ~ 50 칸이다.
# 4. 암호코드의 가로 길이는 총 길이는 56칸이다. 암호코드에 구성하는 숫자 하나가 차지하는 길이는 7칸이다. 각 숫자들을 그림으로 표시하는 방법은 다음과 같다.

# 암호코드 정보가 포함된 2차원 배열을 입력으로 받아 정상적인 암호코드를 판별하는 프로그램을 작성하라.


# [입력]
# 가장 첫줄은 전체 테스트 케이스의 수이다.
# 각 테스트 케이스의 첫 줄에 두 자연수가 주어지는데 각각 배열의 세로 크기 N, 배열의 가로크기 M이다 (1≤N<50, 1≤M<100).
# 그 다음 N개의 줄에는 M개의 배열의 값이 주어진다.


# [출력]
# 각 테스트 케이스의 답을 순서대로 표준출력으로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다.
# 이때 C는 케이스의 번호이다. 같은 줄에 빈칸을 하나 두고, 입력에 주어진 배열에서 정상적인 암호코드들에 포함된 숫자들의 합을 출력한다.


# [예제 풀이]
# 1번 케이스의 암호코드 정보를 추출하면 아래와 같다.

# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011

# 이 숫자가 나타내는 정보는 각각 아래와 같다.
# 0111011(7) 0110001(5) 0111011(7) 0110001(5) 0110001(5) 0001101(0) 0010011(2) 0111011(7)

# 검증코드가 맞는지 살펴보면, (7 + 7 + 5 + 2) * 3 + 5 + 5 + 0 + 7 = 80 이므로 올바른 암호코드라고 할 수 있다. 따라서 1번의 출력 값은 38이 된다.
# 2번 케이스도 같은 방식으로 계산할 경우, 검증코드가 틀렸음을 알 수 있다. 따라서 2번의 출력 값은 0이 된다.


def checkCode(crypto):
    numcode = []
    # 7개씩 잘라서 가져온 뒤 딕셔너리를 통해 해당하는 숫자를 numcode에 append시킨다.
    for i in range(8):
        numcode.append(code[crypto[i*7:(i+1)*7]])

    odd, even = 0, 0
    for i in range(7):
        if i % 2:
            even += numcode[i]
        else:
            odd += numcode[i]

    if (odd*3 + even + numcode[7]) % 10:
        return 0

    return sum(numcode)


code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111':8, '0001011': 9}
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    crypto = ''
    for _ in range(N):
        # strip('0')을 통해 0을 전부 날림
        temp = input().strip('0')
        # 암호문일 경우와 아직 암호문이 안나왔을 때만 crypto에 암호문을 넣기. 암호문 한 줄만 있으면 된다.
        if len(temp) > 0 and not crypto:
            crypto = temp
    # strip('0')으로 앞의 0이 날라간 경우 총 길이가 56이 될 떄까지 앞에 0을 채워주면 된다.
    while len(crypto) < 56:
        crypto = '0' + crypto

    print('#%d %d' % (t, checkCode(crypto)))


