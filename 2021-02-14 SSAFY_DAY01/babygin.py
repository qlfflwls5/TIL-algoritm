# Baby-gin Game
# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
# 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
# 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
# 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.


# 입력 예
# 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)
# 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다. (456, 000)
# 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 baby-gin 이 아니다. (123을 run으로 사용하더라도 011이 run이나 triplet가 아님)


# baby-gin인 경우 'Baby Gin' 아닌 경우 'Lose'로 출력하라.


# 완전 탐색을 통해 뽑은 6장의 카드의 모든 조합에서 앞 세 장과 뒤 세 장의 run, triplet여부를 확인한다.
import sys

sys.stdin = open('babygin_input2.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = []
    Gin = False
    for i in range(6):
        num += [N % 10]
        N //= 10
    for i1 in range(len(num)):
        for i2 in range(len(num)):
            if i1 != i2:
                for i3 in range(len(num)):
                    if i3 != i2 and i3 != i1:
                        for i4 in range(len(num)):
                            if i4 != i3 and i4 != i2 and i4 != i1:
                                for i5 in range(len(num)):
                                    if i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1:
                                        for i6 in range(len(num)):
                                            if i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1:
                                                if num[i1] == num[i2] == num[i3] and num[i4] == num[i5] == num[i6]:
                                                    Gin = True
                                                if num[i1] == num[i2] == num[i3] and num[i4] + 1 == num[i5] and num[i5] + 1 == num[i6]:
                                                    Gin = True
                                                if num[i1] + 1 == num[i2] and num[i2] + 1 == num[i3] and num[i4] == num[i5] == num[i6]:
                                                    Gin = True
                                                if num[i1] + 1 == num[i2] and num[i2] + 1 == num[i3] and num[i4] + 1 == num[i5] and num[i5] + 1 == num[i6]:
                                                    Gin = True

    result = 'Baby Gin' if Gin else 'Lose'
    print('#%d %s' %(t, result))
