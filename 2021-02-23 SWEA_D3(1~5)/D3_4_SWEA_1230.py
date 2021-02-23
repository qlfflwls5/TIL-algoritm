# 암호문3
# 0 ~ 999999 사이의 수를 나열하여 만든 암호문이 있다.
# 암호문을 급히 수정해야 할 일이 발생했는데, 이 암호문은 특수 제작된 처리기로만 수정이 가능하다.
# 이 처리기는 다음과 같이 3개의 기능을 제공한다.

# 1. I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
# 2. D(삭제) x, y : 앞에서부터 x의 위치 바로 다음부터 y개의 숫자를 삭제한다.[ ex) D 4 4 ]
# 3. A(추가) y, s : 암호문의 맨 뒤에 y개의 숫자를 덧붙인다. s는 덧붙일 숫자들이다. [ ex) A 2 421257 796813 ]
# 위의 규칙에 맞게 작성된 명령어를 나열하여 만든 문자열이 주어졌을 때, 암호문을 수정하고, 수정된 결과의 처음 10개 숫자를 출력하는 프로그램을 작성하여라.


# [입력]
# 첫 번째 줄 : 원본 암호문의 길이 N ( 2000 ≤ N ≤ 4000 의 정수)
# 두 번째 줄 : 원본 암호문
# 세 번째 줄 : 명령어의 개수 ( 250 ≤ N ≤ 500 의 정수)
# 네 번째 줄 : 명령어
# 위와 같은 네 줄이 한 개의 테스트 케이스이며, 총 10개의 테스트 케이스가 주어진다.


# [출력]
# #기호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 수정된 암호문의 처음 10개 항을 출력한다.


# [제약 사항]
# 실행 시간 60ms 이하


import sys


sys.stdin = open('1230_input.txt')


def I(c_list, i, x, y):
    global origin
    # insert를 통해 넣으려면 for문으로 돌려야 한다.
    origin = origin[:x] + c_list[i+3:i+3+y] + origin[x:]


def D(x, y):
    global origin
    origin = origin[:x] + origin[x+y:]


def A(c_list, i, y):
    global origin
    origin += c_list[i+2:i+2+y]


for t in range(1, 11):
    N = int(input())
    origin = list(map(int, input().split()))
    C = int(input())
    c_list = list(input().split())
    for i in range(len(c_list)):
        if c_list[i] == 'I':
            I(c_list, i, int(c_list[i+1]), int(c_list[i+2]))
        elif c_list[i] == 'D':
            D(int(c_list[i+1]), int(c_list[i+2]))
        elif c_list[i] == 'A':
            A(c_list, i, int(c_list[i+1]))

    print('#%d' % t, end=' ')
    print(*origin[:10])


# 2
for t in range(1, 11):
    N = int(input())
    origin = list(map(int, input().split()))
    C = int(input())
    c_list = list(input().split())
    for i in range(len(c_list)):
        if c_list[i] == 'I':
            x, y = int(c_list[i+1]), int(c_list[i+2])
            origin = origin[:x] + c_list[i+3:i+3+y] + origin[x:]
        elif c_list[i] == 'D':
            x, y = int(c_list[i+1]), int(c_list[i+2])
            origin = origin[:x] + origin[x+y:]
        elif c_list[i] == 'A':
            y = int(c_list[i+1])
            origin += c_list[i+2:i+2+y]

    print('#%d' % t, end=' ')
    print(*origin[:10])
