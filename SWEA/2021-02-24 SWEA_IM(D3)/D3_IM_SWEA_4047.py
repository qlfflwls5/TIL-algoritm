# 영준이의 카드 카운팅
# 최근 영준이는 카드 게임에 꽂혀 있다.
# 영준이가 하는 카드 게임에는 한 덱의 카드가 필요한데 여기서 얘기하는 “한 덱”이란 스페이드, 다이아몬드, 하트, 클로버 무늬 별로 각각 A, 2~10, J, Q, K의 라벨 즉 4개의 무늬 별로
# 각각 13장씩 총 52장의 카드가 있는 모음을 의미한다.
# 편의상 A는 1, J, Q, K는 11, 12, 13으로 하여 1~13의 숫자가 카드에 적혀있다고 하자.
# 영준이는 몇 장의 카드를 이미 가지고 있는데 게임을 하기 위해서 몇 장의 카드가 더 필요한지 알고 싶어 한다.
# 그리고 이미 겹치는 카드를 가지고 있다면 오류를 출력하고자 한다.
# 지금 가지고 있는 카드의 정보가 주어지면 이 작업을 수행하는 프로그램을 작성하라.


# [입력]
# 맨 위 줄에 테스트케이스의 개수가 주어진다.
# 각 테스트케이스 별로 순서대로 첫 번째 줄에 지금 영준이가 가지고 있는 카드에 대한 정보 S (1 ≤ |S| ≤ 1000)가 주어진다.
# S는 각각 3자리로 표현되는 카드들의 정보를 붙여서 만든 하나의 문자열인데 각 카드는 TXY 꼴로 표현되며,
# T는 카드의 무늬(S, D, H, C)이며 XY는 카드의 숫자 (01 ~ 13)이다.


# [출력]
# 각 테스트케이스 별로 순서대로 한 줄씩 답을 출력하는데, 문자열 S를 보고 지금 무늬 별로(S, D, H, C 순서로) 몇 장의 카드가 부족한지 출력하여라.
# 이미 겹치는 카드가 있다면 문자열 “ERROR” (쌍따옴표는 출력하지 않는다)를 출력한다


# 각 무늬 별로 카운트 리스트를 만들어 카드의 숫자를 셀 것이다. 카운트가 2가 되는 순간 작업은 종료하고 ERROR를 반환한다.
# 카운트가 다 끝나고 각 무늬와 13의 차이가 부족한 개수다.
T = int(input())
for t in range(1, T+1):
    # 카운트 리스트
    S, D, H, C = [0]*13, [0]*13, [0]*13, [0]*13
    data = input()
    i = 0
    while i < len(data)-1:
        if data[i] == 'S':
            # 카운트 리스트의 길이가 13, 0~12로 맞춰져 있으므로 실제 저장할 때는 1을 뺀 인덱스에 카운트하기
            S[int(data[i+1:i+3])-1] += 1
            if S[int(data[i+1:i+3])-1] > 1:
                result = 'ERROR'
                break
        elif data[i] == 'D':
            D[int(data[i + 1:i + 3]) - 1] += 1
            if D[int(data[i+1:i+3])-1] > 1:
                result = 'ERROR'
                break
        elif data[i] == 'H':
            H[int(data[i + 1:i + 3]) - 1] += 1
            if H[int(data[i+1:i+3])-1] > 1:
                result = 'ERROR'
                break
        elif data[i] == 'C':
            C[int(data[i + 1:i + 3]) - 1] += 1
            if C[int(data[i+1:i+3])-1] > 1:
                result = 'ERROR'
                break
        i += 3
    else:
        result = '%d %d %d %d' % (13-sum(S), 13-sum(D), 13-sum(H), 13-sum(C))

    print('#%d %s' % (t, result))