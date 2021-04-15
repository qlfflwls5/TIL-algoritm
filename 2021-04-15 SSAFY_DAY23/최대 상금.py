# 최대 상금
# 퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.
# 우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.
# 예를 들어, 다음 그림과 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회라고 하자.
# 교환전>
# 3  2  8  8  8
# 처음에는 첫번째 숫자판의 3과 네 번째 숫자판의 8을 교환해서 8, 2, 8, 3, 8이 되었다.
# 다음으로, 두 번째 숫자판 2와 마지막에 있는 8을 교환해서 8, 8, 8, 3, 2이 되었다.
# 정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.
# 숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.
# 위의 예에서와 같이 최종적으로 숫자판들이 8,8,8,3,2의 순서가 되면 88832원의 보너스 상금을 획득한다.
# 여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.

# 다음과 같은 경우 1회의 교환 횟수가 주어졌을 때 반드시 1회 교환을 수행하므로 결과값은 49가 된다.
# 9  4 -> 4  9
# 94의 경우 2회 교환하게 되면 원래의 94가 된다.
# 정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.


# [입력]
# 가장 첫 줄은 전체 테스트 케이스의 수이다.
# 최대 20개의 테스트 케이스가 표준 입력을 통하여 주어진다.
# 각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.
# 숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.


# [출력]
# 각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.
# 같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.


for t in range(1, int(input())+1):
    num, cnt = input().split()
    num, cnt = list(map(int, num)), int(cnt)
    # max값들끼리의 숫자가 중복될 때 문제가 생긴다.
    # 예를 들어, 선택 정렬을 사용할 것이기 때문에 3288을 두 번 교환하면 8823이 된다. 내가 원하는 것은 8832이다.
    # 따라서, max값과 자리를 바꿔 이동하게 된 숫자들은 그들끼리 다시 정렬을 해줘야 한다.
    # 그러면서도 같은 max값과 바뀐 숫자들끼리 내에서 정렬을 해줘야 한다.
    # 예를 들어, 32417788이라면 3과 2는 같은 8과 바뀌니 둘이 정렬하고 4와 1은 같은 7로 바뀌니 둘이 정렬해야 한다. 88774132가 되도록.
    # 그러므로 카운트 리스트와 비슷하게 인덱스를 이용하여 각 max값에 해당하는 곳에 자리를 바꾼 수들을 저장한다.
    changed_list = [[] for _ in range(10)]
    for i in range(0, len(num)-1):
        max_i = i
        for j in range(i+1, len(num)):
            if num[j] >= num[max_i]:
                max_i = j

        if num[max_i] != num[i]:
            cnt -= 1
            changed_list[num[max_i]].append(max_i)
            num[i], num[max_i] = num[max_i], num[i]
            # 최대값이 있던 자리에 밀려난 숫자가 온 것이므로 최대값이 있던 자리를 changed_list에 append

        if cnt == 0:
            break
    # 횟수가 남아있다면 그것은 이미 내림차순으로 정렬이 된 상태를 의미한다.
    if cnt:
        # 만약 중간에 중복되는 자리가 있으면 그 둘을 서로 계속 swap할 것이므로 그냥 실행 안한거나 같다. ex) 7770
        # 또한, 남은 교환 횟수가 짝수여도 그냥 제자리에 돌아온 것이나 마찬가지.
        # 즉, 중복이 없으면서 교환 횟수가 홀수일 때만 일의 자리와 십의 자리를 바꿔준다.
        if len(num) == len(set(num)) and cnt % 2:
            num[-1], num[-2] = num[-2], num[-1]
    # 내림차순 정렬이 안되어 있는 상태라면 max값과 자리를 바꾼 수들끼리의 정렬을 실행
    else:
        # 카운트 리스트 내의 각 리스트에 대하여(각 max값에 대해 자리를 바꾼 수들의 리스트에 대하여)
        for c_list in changed_list:
            # 자리를 바꾼 수가 2개 이상이라면
            if len(c_list) > 1:
                # 총 바꿀 횟수는 자리를 바꾼 수들의 개수 - 1번. 예) 3, 2, 1이 있다면 적어도 2번은 선택 정렬해야 정렬이 된다.
                change_cnt = len(c_list) - 1
                # 선택 정렬을 하기 위해서 일단 수들을 오름차순 정렬한다.
                c_list.sort()
                # 인덱스를 이용하여 수들끼리의 정렬을 구현한다.
                for i in range(len(c_list) - 1):
                    max_i = c_list[i]
                    for j in range(i + 1, len(c_list)):
                        if num[c_list[j]] >= num[max_i]:
                            max_i = c_list[j]
                    num[c_list[i]], num[max_i] = num[max_i], num[c_list[i]]
                    change_cnt -= 1
                    if change_cnt == 0:
                        break

    result = 0
    won = 1
    for i in range(len(num)-1, -1, -1):
        result += num[i]*won
        won *= 10

    print('#%d %d' % (t, result))


# 2
# 영주님 코드
for t in range(1, int(input())+1):
    numbers, n = input().split()
    length = len(numbers)
    cases = {numbers}
    for _ in range(int(n)):
        changed = set()
        for case in cases:
            case_list = list(case)
            for i in range(length):
                for j in range(i+1, length):
                    case_list[i], case_list[j] = case_list[j], case_list[i]
                    changed.add(''.join(case_list))
                    case_list[i], case_list[j] = case_list[j], case_list[i]
        cases = set(changed)
    print('#%s %s' % (t, max(map(int, cases))))