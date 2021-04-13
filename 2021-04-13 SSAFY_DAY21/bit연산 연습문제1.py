# 연습문제 1
# 0과 1로 이루어진 1차 배열에서 7개 byte(글자)를 묶어서 10진수로 출력하기
# 예를 들어 입력이 다음과 같다면 결과로 1, 13을 출력한다.

# 입력 첫 줄에 testcast의 수가 입력되고
# 다음 줄 부터 testcast의 수만큼 0과 1로 이루어진 문자열이 입력된다


# 1
def BtoD(byte, num):
    decimal = []
    for i in range(len(num)//byte):
        binary = num[i*byte:(i+1)*byte]
        d, b = 0, 1
        for j in range(byte-1, -1, -1):
            d += int(binary[j])*b
            b *= 2
        decimal.append(str(d))

    return decimal


for t in range(1, int(input())+1):
    num = input()
    decimal = BtoD(7, num)
    print('#%d %s' % (t, ' '.join(decimal)))


# 2
# 위 함수를 다듬어 보자
# 쉬프트를 사용해서 곱셈을 구현하고, 뒤에서부터 읽는 것도 안해도 된다.
def BtoD(byte, num):
    decimal = []
    for i in range(len(num)//byte):
        binary = num[i*byte:(i+1)*byte]
        d, b = 0, byte-1
        for bin_num in binary:
            if bin_num:
                d += int(bin_num) << b
            b -= 1
        decimal.append(str(d))

    return decimal
    

# 3
# 함수 내 binary = num[i*byte:(i+1)*byte] 부분을 쉬프트로 바꿔볼 수 없을까?
# i & (1 << j)의 의미에 대해 생각해보자


# 4
# 람다식 활용
def BtoD(byte, num):
    decimal = []
    for i in range(len(num)//byte):
        binary = list(map(int, num[i*byte:(i+1)*byte]))
        int_num = sum(map(lambda x: x[1] << x[0], enumerate(binary[::-1])))
        decimal.append(str(int_num))

    return decimal


# 5
# 교수님의 수정
def BtoD(byte, num):
    decimal = []
    for i in range(len(num)//byte):
        binary = list(map(int, num[i*byte:(i+1)*byte]))
        int_num = sum(1 << i for i, x in enumerate(binary[::-1]) if x == '1')
        decimal.append(str(int_num))

    return decimal


# 6
# mask_bits 활용 (중요)
def BtoD(nbits, num):
    cnt = len(num)//nbits         # 숫자 개수
    mask_bits = ((1<<nbits) - 1)  # mask bit 작성 0b1111111
    num = int(num, 2)             # 정수로 변경
    decimal = [(num >> (i*nbits)) & mask_bits for i in range(cnt)] # 0b111111 & 0b111 은 7이다. 이런 성질을 이용한 것. 마스크 비트 만큼만 계산하니깐 오른쪽 쉬프트로 떙겨오면서 마스크 적용
    return decimal

BtoD(7, '11001000000010')