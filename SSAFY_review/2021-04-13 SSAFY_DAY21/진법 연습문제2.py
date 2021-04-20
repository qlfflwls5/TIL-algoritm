# 진법 - 연습문제2
# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해 보자
# 예를 들어 0F97A3 이 입력일 경우 2진수로 변환하면 000011111001011110100011 이며, 7bit씩 묶어 십진수로 출력하면
# 0000111 1100101 1110100 011 이 되므로  7, 101, 116, 3을 출력한다


def BtoD(bit, num):
    for i in range(len(num)//bit):
        binary = num[i*bit:(i+1)*bit]
        d, b = 0, 1
        for j in range(bit-1, -1, -1):
            d += int(binary[j])*b
            b *= 2
        decimal.append(str(d))

    if len(num) % bit and len(num) > bit:
        new_bit = len(num) % bit
        BtoD(new_bit, num[len(num)-new_bit:])


for t in range(1, int(input())+1):
    hexa = input()
    binary = bin(int('0x'+hexa, 16))[2:]
    bin_num = binary.zfill(len(hexa)*4)
    decimal = []
    BtoD(7, bin_num)
    print('#%d %s' % (t, ', '.join(decimal)))