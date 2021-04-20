# 정식이의 은행업무
# 삼성은행의 신입사원 정식이는 실수를 저질렀다.
# 은행 업무가 마감되기 직전인 지금, 송금할 금액을 까먹고 말았다.
# 하지만 다행스럽게도 정식이는 평소 금액을 2진수와 3진수의 두 가지 형태로 기억하고 다니며, 기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것만은 알고 있다.
# 예를 들어 현재 기억이 2진수 1010과 3진수 212을 말해주고 있다면 이는 14의 2진수인 1110와 14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.
# 정식이는 실수를 바로잡기 위해 당신에게 부탁을 하였다.
# 정식이가 송금액을 추측하는 프로그램을 만들어주자.
# ( 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.  추측할 수 없는 경우는 주어지지 않는다. )


# [입력]
# 10개 이하의 테스트 케이스가 주어진다.
# 첫 번째 줄에는 테스트케이스의 개수가 주어진다.
# 하나의 케이스는 두 줄로 되어있다.
# 각 케이스의 첫 번째 줄은 정식이가 기억하는 송금액의 2진수 표현, 두 번째 줄은 송금액의 3진수 표현이 주어진다.
# (3 ≤ 2진수, 3진수의 자릿수 <40)


# [출력]
# 원래 송금하기로 하였던 금액을 케이스마다 한 줄에 하나씩 출력한다.


# 0
# 혼자 풀어보기
def get_num(binary, tenary):
    len_b, len_t = len(binary), len(tenary)
    # 2진수의 각 자리를 바꾼 모든 경우의 수
    b = int(binary, 2)
    for i in range(len_b):
        b_set.add(b ^ (1 << i))

    # 3진수의 각 자리를 바꾼 모든 경우의 수를 구하고 2진수 set안에 있으면 종료
    for i in range(len_t):
        for j in range(3):
            if tenary[i] != str(j):
                temp = int(tenary[:i] + '%d' % j + tenary[i + 1:], 3)
                if temp in b_set:
                    return temp


for t in range(1, int(input())+1):
    binary = input()
    tenary = input()
    b_set = set()
    print('#%d %d' % (t, get_num(binary, tenary)))


# 1
# ^를 이용한 라이브식 풀이
def f(b, t):
    # 2진수 처리
    # n진수를 10진수로 바꾸는 법 == int(n진수, n)이랑 같은 거임
    bint = 0
    for x in b:
        bint = bint*2 + int(x)
    # 여기까지
    binary = []
    for i in range(len(b)):
        binary.append(bint ^ (1 << i)) # 2진수의 1비트씩을 바꿔서 저장. ^연산은 1인 부분만 invert시킨다.

    # 3진수 처리
    for i in range(len(t)): # 3진수에서 다른 두 수로 바꿔볼 자리
        num1 = 0 # (x+1) % 3 즉, 첫 번째 다른 수로 바꿀 것
        num2 = 0 # (x+2) % 3 두 번째 다른 수로 바꿀 것
        for j in range(len(t)):
            # 바꿀 자리가 아니면 그대로 갖고 오고,
            if i != j:
                num1 = num1*3 + int(t[j])
                num2 = num2*3 + int(t[j])
            # 바꿀 자리라면 첫 번째 바꾼 수는 num1, 두 번째 바꾼 수는 num2가 된다.
            else:
                num1 = num1 * 3 + (int(t[j]) + 1)%3 # 0은 1로, 1은 2로, 2는 0으로 바꿔봄
                num2 = num2 * 3 + (int(t[j]) + 2)%3 # 0은 2로, 1은 0으로, 2는 1로 바꿔봄
        if num1 in binary:
            return num1
        if num2 in binary:
            return num2


for t in range(1, int(input())+1):
    binary = input()
    tenary = input()
    print(f(binary, tenary))


