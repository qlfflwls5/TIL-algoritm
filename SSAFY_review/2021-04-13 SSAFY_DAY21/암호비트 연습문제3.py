# 암호비트 - 연습문제 3
# 16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오. 암호는 연속되어있다.
# 예를 들어 0DEC 인 경우 00 001101 111011 00 으로 해석되어 0, 2 가 출력된다.

# 0   001101
# 1   010011
# 2   111011
# 3   110001
# 4   100011
# 5   110111
# 6   001011
# 7   111101
# 8   011001
# 9   101111


def dec(code):
    for i in range(len(code)//6):
        binary = code[i*6:(i+1)*6]
        result.append(enc[binary])


def find_code(binary):
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            for j in range(len(binary[:i+1])):
                if binary[j] == '1':
                    code = binary[j:i+1].zfill(len(binary[j:i+1])//6*6+6 if len(binary[j:i+1])%6 else 0)
                    dec(code)
                    return

enc = {
    '001101': '0',
    '010011': '1',
    '111011': '2',
    '110001': '3',
    '100011': '4',
    '110111': '5',
    '001011': '6',
    '111101': '7',
    '011001': '8',
    '101111': '9'
}
for t in range(1, int(input())+1):
    hexa = input()
    binary = bin(int('0x'+hexa, 16))[2:].zfill(len(hexa)*4)
    result = []
    find_code(binary)

    print('#%d %s' % (t, ', '.join(result)))