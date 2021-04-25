# baby-gin
# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
# 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.

# 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.

# 입력 예
# 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)
# 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다. (456, 000)
# 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 baby-gin 이 아니다. (123을 run으로 사용하더라도 011이 run이나 triplet가 아님)

# baby-gin인 경우 'Baby Gin' 아닌 경우 'Lose'로 출력하라.


def perm(level, S):
    if flag[0]:
        return

    if level == 6:
        if (isrun(S[:3]) or istriplet(S[:3])) and (isrun(S[3:]) or istriplet(S[3:])):
            flag[0] = 1
        return
    
    # swap -> perm의 인자는 level하나뿐, 0으로 시작. isrun, istriplet에 num을 직접 넘기기
    # for i in range(level, 6):
    #     num[i], num[level] = num[level], num[i]
    #     perm(level+1)
    #     num[i], num[level] = num[level], num[i]
    
    for i in range(6):
        if not check[i]:
            check[i] = 1
            perm(level+1, S + [num[i]])
            check[i] = 0


def istriplet(arr):
    if arr[0] == arr[1] == arr[2]:
        return True

    return False


def isrun(arr):
    return 1 if arr[1] == arr[0] + 1 and arr[2] == arr[1] + 1 else 0


for t in range(1, int(input())+1):
    num = list(map(int, input()))
    flag = [0]
    check = [0]*6
    perm(0, [])
    print('#%d %s' % (t, 'Baby Gin' if flag[0] else 'Lose'))
