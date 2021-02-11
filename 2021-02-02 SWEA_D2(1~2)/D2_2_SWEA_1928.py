# Base64 Decoder


# 다음과 같이 Encoding 을 한다.
# 1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.
# 2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.
# 입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.
# 'A' = 0 ~ 'Z' = 25, 'a' = 26 ~ 'z' = 51, '0' = 52 ~ '9' = 61, '+' = 62, '/' = 63


# [제약사항]
# 문자열의 길이는 항상 4의 배수로 주어진다.
# 그리고 문자열의 길이는 100000을 넘지 않는다.


# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스는 Encoding 된 상태로 주어지는 문자열이다.


# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 입력
# 10
# TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u
# U3VzcGljaW9uIGZvbGxvd3MgY2xvc2Ugb24gbWlzdHJ1c3Qu
# VG8gZG91YnQgaXMgc2FmZXIgdGhhbiB0byBiZSBzZWN1cmUu
# T25seSB0aGUganVzdCBtYW4gZW5qb3lzIHBlYWNlIG9mIG1pbmQu
# QSBmdWxsIGJlbGx5IGlzIHRoZSBtb3RoZXIgb2YgYWxsIGV2aWwu
# QSBnaWZ0IGluIHNlYXNvbiBpcyBhIGRvdWJsZSBmYXZvciB0byB0aGUgbmVlZHku
# Qm9va3MgYXJlIHNoaXBzIHdoaWNoIHBhc3MgdGhyb3VnaCB0aGUgdmFzdCBzZWFzIG9mIHRpbWUu
# TGV0IHRoeSBzcGVlY2ggYmUgc2hvcnQsIGNvbXByZWhlbmRpbmcgbXVjaCBpbiBmZXcgd29yZHMu
# VGhlIHdvcmxkIGlzIGEgYmVhdXRpZnVsIGJvb2ssIGJ1dCBvZiBsaXR0bGUgdXNlIHRvIGhpbSB3aG8gY2Fubm90IHJlYWQgaXQu
# SGUgd2hvIHNwYXJlcyB0aGUgcm9kIGhhdGVzIGhpcyBzb24sIGJ1dCBoZSB3aG8gbG92ZXMgaGltIGlzIGNhcmVmdWwgdG8gZGlzY2lwbGluZSBoaW0u


# 출력
# #1 Life itself is a quotation.
# #2 Suspicion follows close on mistrust.
# #3 To doubt is safer than to be secure.
# #4 Only the just man enjoys peace of mind.
# #5 A full belly is the mother of all evil.
# #6 A gift in season is a double favor to the needy.
# #7 Books are ships which pass through the vast seas of time.
# #8 Let thy speech be short, comprehending much in few words.
# #9 The world is a beautiful book, but of little use to him who cannot read it.
# #10 He who spares the rod hates his son, but he who loves him is careful to discipline him.


# 인코딩 과정 -> ord(문자)를 2진수로 표현, 앞에서 6개씩 끊어서 Base64의 표에서 변환한다.
# 이에 따른 디코딩 과정 -> 1문자씩 가져와 해당 문자가 가진 Base64표의 숫자를 2진수로 변환한 것을 연결한 후, 8자씩 끊어서 이를 chr()하면 본래 단어가 나올 것!
T = int(input())
for k in range(1, T + 1):
    # 결과를 담을 문자열을 생성한다.
    result = ''
    # 인코딩 된 문장을 입력받는다.
    encode = input()
    # 인코딩 된 문장을 2진수의 문자열로 만들어야 하기 때문에 빈 문자열을 생성한다.
    binary_str = ''
    # 인코딩 된 문장에서 한 문자씩 가져와 Base64표에 따라 숫자를 구하고(아스키 코드 표를 이용한다),
    # 해당 숫자를 bin()을 통해 이진수의 문자열로 변환하는데 이때 앞에 '0b'라는 이진수를 표현하는 수식어가 붙게 된다.    ex) '0b1010'
    # 인코딩이 이진수를 6자리씩 끊어온 것이기 때문에 6자리가 안되는 것들은 앞에 '0'을 붙여 6자리로 만들어주어야 한다.    ex) '1010' -> '001010'
    # 하지만, 앞에 '0b'가 있고 str은 문자 삽입이 안되므로, bin()한 것을 [2:]로 슬라이싱 해와,    ex) '0b1010'이면 '1010'만 가져온다.
    # 전체 길이가 6이 될 때까지 앞에 '0'을 추가해주고 binary_bin에 이어 붙인다.    ex) 가져온 '1010'을 '001010'으로 만들어 추가
    for i in encode:
        if i.isalpha() and 65 <= ord(i) <= 90:
            num = ord(i) - 65
        elif i.isalpha() and 97 <= ord(i) <= 122:
            num = ord(i) - 71
        elif i.isdigit() and 0 <= int(i) <= 9:
            num = int(i) + 52
        elif i == '+':
            num = 62
        elif i == '/':
            num = 63
        temp_bin = bin(num)[2:]
        while len(temp_bin) < 6:
            temp_bin = '0' + temp_bin
        binary_str += temp_bin
    
    # 완성된 이진수 문자열에서 이제 8개씩 가져와 이를 아스키 코드를 통해 문자로 바꿔야 한다.
    # 8개씩 끊어가져와서 int(이진수)를 통해 10진수로 변환한 후 아스키 코드에서 그 10진수를 이용해 chr()로 문자를 찾는다.
    for i in range(len(binary_str)//8):
        bin_num = binary_str[i * 8:i * 8 + 8]
        result += chr(int(bin_num, 2))
    
    print(f'#{k} {result}')
        

# 함수 import해서 하는법
# import base64

# T = int(input())
# for t in range(1, T+1):
#     print(f"#{t} {base64.b64decode(input()).decode('utf-8')}")


# 중간중간 더 쉽게 하는법
# 이진수로 변환할 때 '0b'안붙이고 변환하는법 -> format(10진수, 'b') 사용
# 문자의 앞쪽 채우는법 -> .rjust(총 자릿수, 채울 문자) 사용  ex) binary_str.rjust(6, '0')


# 하면서 새로 배운 것
# int(진수 문자열, 진수) 를 통해 10진수로 변환 가능