# 16진수 암호
# # 16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오. 암호는 연속되어있다.
# # 예를 들어 0DEC 인 경우 00 001101 111011 00 으로 해석되어 0, 2 가 출력된다.


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
    code = bin(int(hexa, 16))[2:].zfill(len(hexa)*4).rstrip('0')
    prefix = len(code) % 6
    code = code[prefix:]
    dec = []
    for i in range(len(code)//6):
        dec.append(enc[code[i*6:(i+1)*6]])

    print('#%d %s' % (t, ', '.join(map(str, dec))))