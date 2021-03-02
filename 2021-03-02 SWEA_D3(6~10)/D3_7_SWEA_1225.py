# 암호생성기
# 다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

# - 8개의 숫자를 입력 받는다.
# - 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
# 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

# 이와 같은 작업을 한 사이클이라 한다.
# - 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.


# [제약 사항]
# 주어지는 각 수는 integer 범위를 넘지 않는다.
# 마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.


# [입력]
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고, 그 다음 줄에는 8개의 데이터가 주어진다.


# [출력]
# #부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.


import sys
sys.stdin = open('1225_input.txt')


# 1
# 8번의 싸이클을 돌면 제자리, 각 자리가 15씩 감소
for _ in range(1, 11):
    t = int(input())
    num = list(map(int, input().split()))
    # 가장 작은 숫자를 15로 나눈 몫보다 1적은 수를 구해 그 수*15를 모든 요소에서 뺄 것이다.
    # 그러면 마지막 제자리 싸이클을 돌기 전 원래의 순서대로 되어있는 상태가 된다.
    min_15x = min(num)//15 - 1
    for i in range(len(num)):
        num[i] -= 15*min_15x
    # 싸이클을 도는 것을 구현해 0이 생길 때까지 돌린다.
    while 0 not in num:
        for i in range(5):
            temp = num.pop(0)-(i+1)
            if temp <= 0:
                num.append(0)
                break
            else:
                num.append(temp)

    print('#%d' % t, end=' ')
    print(*num)


# 2
# 그냥 규칙만 쓴 코드
def cycle():
    for i in range(1, 6):
        x = num_list.pop(0) - i
        if x <= 0:
            num_list.append(0)
            return 0
        else:
            num_list.append(x)
    return 1

for t in range(1, 11):
    a = int(input())
    num_list = list(map(int, input().split()))
    while cycle():
        pass
    print("#%d" %t, end=' ')
    print(*num_list)