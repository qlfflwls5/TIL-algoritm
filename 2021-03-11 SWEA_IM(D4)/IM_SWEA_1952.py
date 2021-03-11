# 수영장
# 김 프로는 수영장을 이용한다.
# 김 프로는 지출이 너무 많아 내년 1년 동안 각 달의 이용 계획을 수립하고 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 있다.
# 수영장에서 판매하고 있는 이용권은 아래와 같이 4 종류이다.

#    ① 1일 이용권 : 1일 이용이 가능하다.
#    ② 1달 이용권 : 1달 동안 이용이 가능하다. 1달 이용권은 매달 1일부터 시작한다.
#    ③ 3달 이용권 : 연속된 3달 동안 이용이 가능하다. 3달 이용권은 매달 1일부터 시작한다.
#        (11월, 12월에도 3달 이용권을 사용할 수 있다 / 다음 해의 이용권만을 구매할 수 있기 때문에 3달 이용권은 11월, 12월, 1윌 이나 12월, 1월, 2월 동안 사용하도록 구매할 수는 없다.)
#    ④ 1년 이용권 : 1년 동안 이용이 가능하다. 1년 이용권은 매년 1월 1일부터 시작한다.

# 각 달의 이용 계획은 [Table 1]의 형태로 수립된다.
# 이용 계획에 나타나는 숫자는 해당 달에 수영장을 이용할 날의 수를 의미한다.
# 각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,
# 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램을 작성하라.


# [예시]
# 수영장에서 판매하는 1일 이용권, 1달 이용권, 3달 이용권, 1년 이용권의 요금은 각각 10원, 40원, 100원, 300원이다.
# 이 때 수영장을 이용할 수 있는 방법은 [Table 2]와 같이 다양한 경우를 생각할 수 있다.
# 다른 경우도 가능하지만, 가장 적은 비용으로 수영장을 이용한 경우는 4번 경우이다.
# 따라서, 정답은 110이 된다.


# [제약 사항]
# 1. 시간 제한 : 최대 50개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초
# 2. 모든 종류의 이용권 요금은 10 이상 3,000 이하의 정수이다.
# 3. 각 달의 이용 계획은 각 달의 마지막 일자보다 크지 않다.


# [입력]
# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 1일 이용권의 요금, 1달 이용권의 요금, 3달 이용권의 요금, 1년 이용권의 요금이 순서대로 한 칸씩 띄고 주어진다.
# 그 다음 줄에는 1월부터 12월까지의 이용 계획이 주어진다.


# [출력]
# 테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
# 각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t는 1부터 시작하는 테스트 케이스의 번호이다)
# 출력해야 할 정답은 이용 계획대로 수영장을 이용하는 경우 중 가장 적게 지출하는 비용이다.


# 1 DFS
# 1 ~ 12월을 인덱스 상 0 ~ 11월로 볼 것이다.
def cost(month, S):
    # 가지치기1: 이번 달에 수영장을 가지 않으면 바로 다음 달로 넘어가기
    if month < 12 and not c[month]:
        cost(month+1, S)
        return

    # 가지치기2: 전 달까지의 요금이 이미 최소를 넘었으면 더 이상 탐색x
    global min_cost
    if S > min_cost:
        return

    # 종료조건
    if month >= 12:
        min_cost = S
        return
    
    # 작은 가지치기3: 이번 달의 1일권 사용 요금이 1달권 사용 요금보다 적다면 1일권을 택, 아니라면 1달권을 택
    if p[0]*c[month] < p[1]:
        cost(month+1, S+p[0]*c[month])
    else:
        cost(month+1, S+p[1])
    cost(month+3, S+p[2])


for t in range(1, int(input())+1):
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    min_cost = p[3]
    cost(0, 0)

    print('#%d %d' % (t, min_cost))

# 한 달 이용권이 일일 이용권보다 싸다면 일일 이용권을 할 필요가 없다. 잘 확인해보자.


# 2
# 승현님 DP
# 전 달까지의 요금 + 이번 달의 1일권 * 날짜
# 전 달까지의 요금 + 1달권
# 3달 전까지의 요금 + 3달권(현재 달까지 3달권에 포함시키므로 2달 전에 3달권을 산 것이다.)
# 이 셋 중 최소의 값이 현재 달의 DP다.
# 처음 1, 2월만 3달 전의 값이 없으므로 if처리 해주면 된다.
for t in range(1, int(input())+1):
    day, m_1, m_3, year = map(int, input().split())
    swim = [0] + list(map(int, input().split())) + [0, 0]
    swim_pay = [0]*15
    for month in range(1, 15):
        if month >= 3:
            swim_pay[month] = min(swim_pay[month-1]+day*swim[month], swim_pay[month-1]+m_1, swim_pay[month-3]+m_3)
        else:
            swim_pay[month] = min(swim_pay[month-1]+day*swim[month], swim_pay[month-1]+m_1)
    print("#%d %d" %(t, min(swim_pay[12], swim_pay[13], swim_pay[14], year)))


# 3
# 은교님 DP
def get_min(n): # n월까지의 최소요금
    if n == 1:
        return min(plan[n]*d, m, q, y)
    elif n == 2:
        return min(get_min(1)+min(plan[n]*d, m), q, y)
    elif n == 3:
        return min(get_min(2)+min(plan[n]*d, m), q, y)
    else:
        return min(get_min(n-1)+min(plan[n]*d, m), get_min(n-2)+q, get_min(n-3)+q, y)


T = int(input())
for t in range(1, T+1):
    d, m, q, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    result = get_min(12)
    print("#%d %d" % (t, result))