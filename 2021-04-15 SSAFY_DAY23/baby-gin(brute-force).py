# baby-gin
# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
# 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.

# 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.

# 입력 예
# 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)
# 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다. (456, 000)
# 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 baby-gin 이 아니다. (123을 run으로 사용하더라도 011이 run이나 triplet가 아님)

# baby-gin인 경우 'Baby Gin' 아닌 경우 'Lose'로 출력하라.


# 1
# swap을 통한 순열 생성
# 순열은 결국 두 개의 자리를 계속 바꿔가면서 만들어나가는 것으로 보는 것. 재귀호출 뒤에는 원상복구로 다시 스왑
def perm(k, n):
    if flag[0]:
        return

    if k == n:
        if (isrun(num[:3]) or istriplet(num[:3])) and (isrun(num[3:]) or istriplet(num[3:])):
            flag[0] = 1
        return

    for i in range(k, n):
        num[k], num[i] = num[i], num[k]
        perm(k+1, n)
        num[k], num[i] = num[i], num[k]


def isrun(arr):
    return 1 if arr[1] == arr[0] + 1 and arr[2] == arr[1] + 1 else 0


def istriplet(arr):
    return 1 if arr[0] == arr[1] == arr[2] else 0


for t in range(1, int(input())+1):
    num = list(map(int, input()[:6]))
    flag = [0]
    perm(0, 6)
    print('#%d %s' % (t, 'Baby Gin' if flag[0] else 'Lose'))


# 2
# 부분집합을 이용한 완전 검색
def perm(k, n):
    if flag[0]:
        return

    if k == n:
        if (isrun(sel[:3]) or istriplet(sel[:3])) and (isrun(sel[3:]) or istriplet(sel[3:])):
            flag[0] = 1
        return

    for i in range(n):
        if not check[i]:
            sel[k] = num[i]
            check[i] = 1
            perm(k+1, n)
            check[i] = 0


def isrun(arr):
    return 1 if arr[1] == arr[0] + 1 and arr[2] == arr[1] + 1 else 0


def istriplet(arr):
    return 1 if arr[0] == arr[1] == arr[2] else 0


for t in range(1, int(input())+1):
    num = list(map(int, input()[:6]))
    flag = [0]
    sel = [0]*6
    check = [0]*6
    perm(0, 6)
    print('#%d %s' % (t, 'Baby Gin' if flag[0] else 'Lose'))
