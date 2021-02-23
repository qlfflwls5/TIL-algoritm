# 숫자를 입력받아 해당 숫자를 문자열로 바꿔 반환하는 함수


def itoa(num):
    result = ''
    sign = ''
    if num < 0:
        num = -num
        sign = '-'
    while num > 0:
        result = chr(num % 10 + ord('0')) + result
        num //= 10

    return sign + result

print(itoa(1234), type(itoa(1234)))