# 숫자 만들기
# 선표는 게임을 통해 사칙 연산을 공부하고 있다.
# N개의 숫자가 적혀 있는 게임 판이 있고, +, -, x, / 의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구해보기로 했다.
# 수식을 계산할 때 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산한다.
# 예를 들어 1, 2, 3 이 적힌 게임 판에 +와 x를 넣어 1 + 2 * 3을 만들면 1 + 2를 먼저 계산하고 그 뒤에 * 를 계산한다.
# 즉 1+2*3의 결과는 9이다.
# 주어진 연산자 카드를 사용하여 수식을 계산했을 때 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하시오.


# [예시]
# [Figure 1] 과 같이 [3,5,3,7,9]가 적힌 숫자판과 [‘+’ 2개, ‘-‘ 1개, ‘/’ 1개]의 연산자 카드가 주어진 경우를 생각해보자.
# 이 경우 최댓값은 3 - 5 / 3 + 7 + 9 = 16, 최솟값은 3 + 5 + 3 / 7 - 9 = -8 이다.
# 즉 결과는 최댓값과 최솟값의 차이 ( 16 - ( -8 ) ) 로 24 가 답이 된다.


# [제약사항]
# 1. 시간 제한 : 최대 50 개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 모두 3 초
# 2. 게임 판에 적힌 숫자의 개수 N 은 3 이상 12 이하의 정수이다. ( 3 ≤ N ≤ 12 )
# 3. 연산자 카드 개수의 총 합은 항상 N - 1 이다.
# 4. 게임 판에 적힌 숫자는 1 이상 9 이하의 정수이다.
# 5. 수식을 완성할 때 각 연산자 카드를 모두 사용해야 한다..
# 6. 숫자와 숫자 사이에는 연산자가 1 개만 들어가야 한다.
# 7. 완성된 수식을 계산할 때 연산자의 우선 순위는 고려하지 않고, 왼쪽에서 오른쪽으로 차례대로 계산한다.
# 8. 나눗셈을 계산 할 때 소수점 이하는 버린다.
# 9. 입력으로 주어지는 숫자의 순서는 변경할 수 없다.
# 10. 연산 중의 값은 -100,000,000 이상 100,000,000 이하임이 보장된다.


# [입력]
# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,
# 그 다음 줄부터 T 개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 숫자의 개수 N 이 주어진다.
# 다음 줄에는 '+', '-', '*', '/' 순서대로 연산자 카드의 개수가 공백을 사이에 두고 주어진다.
# 다음 줄에는 수식에 들어가는 N 개의 숫자가 순서대로 공백을 사이에 두고 주어진다.


# [출력]
# 테스트 케이스 개수만큼 T 개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
# 각 줄은 "#t" 로 시작하고 공백을 하나 둔 다음 정답을 출력한다. ( t 는 1 부터 시작하는 테스트 케이스의 번호이다. )
# 정답은 연산자 카드를 사용하여 만들 수 있는 수식으로 얻은 결과값 중 최댓값과 최솟값의 차이이다.


# 4개 종류의 operator에서 N-1개의 연산자를 뽑는 것. 중복순열?
# 중복으로 뽑는 대신, 개수의 조건이 걸려있는 문제.
# nPr = n!/r!이고, 0!은 1이다. 그리고, aabcd의 5개에서 5개를 나열하는 것 처럼 중복이 있다면 5P5/2!이 된다. 3개가 중복되면 3!으로 나눈다.
def combi(level):
    if level >= N - 1:
        global max_v, min_v
        result = num[0]
        for i in range(N - 1):
            if arr[i] == 0:
                result += num[i + 1]
            elif arr[i] == 1:
                result -= num[i + 1]
            elif arr[i] == 2:
                result *= num[i + 1]
            elif arr[i] == 3:
                if result < 0 < num[i + 1]:
                    result = -(-result // num[i + 1])
                elif num[i + 1] < 0 < result:
                    result = -(result // -num[i + 1])
                else:
                    result //= num[i + 1]
        if result > max_v:
            max_v = result
        if result < min_v:
            min_v = result

        return

    # +, -, *, /의 개수를 순회, 각 연산자는 순서대로 0, 1, 2, 3으로 매칭된다.
    for i in range(4):
        # 해당 연산자의 개수가 남아있으면, arr의 level번째에 연산자 번호를 넣는다.
        if op[i] > 0:
            arr[level] = i
            op[i] -= 1
            combi(level + 1)
            op[i] += 1


# 이렇게 하면 좀 느리다.
# calc = {0: (lambda a, b: a + b), 1: (lambda a, b: a - b), 2: (lambda a, b: a * b), 3: (lambda a, b: -(-a // b) if b > 0 > a else -(a // -b) if a > 0 > b else a // b)}
for t in range(1, int(input()) + 1):
    N = int(input())
    op = list(map(int, input().split()))
    num = list(map(int, input().split()))
    # 연산자 번호로 짜여진 연산자 순서 판이 될 리스트
    arr = [0] * (N - 1)
    max_v, min_v = -100000000, 100000000
    combi(0)
    print('#%d %d' % (t, abs(max_v - min_v)))

# 재귀의 인자를 활용하는 것을 아끼지 말자. 코드가 짧고 단순해진다.
# 은교님 코드
# dic = {0: (lambda a,b: a+b), 1: (lambda a,b: a-b), 2: (lambda a,b: a*b), 3: (lambda a,b: int(a/b))}
#
# def calc(idx, result, op1, op2, op3, op4):
#     global mx, mn
#     if idx == N-1:
#         mx = max(result, mx)
#         mn = min(result, mn)
#         return
#
#     else:
#         if op1 > 0:
#             n_result = dic[0](result, nums[idx+1])
#             calc(idx+1, n_result, op1-1, op2, op3, op4)
#         if op2 > 0:
#             n_result = dic[1](result, nums[idx+1])
#             calc(idx + 1, n_result, op1, op2-1, op3, op4)
#         if op3 > 0:
#             n_result = dic[2](result, nums[idx+1])
#             calc(idx + 1, n_result, op1, op2, op3-1, op4)
#         if op4 > 0:
#             n_result = dic[3](result, nums[idx+1])
#             calc(idx + 1, n_result, op1, op2, op3, op4-1)
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     opers = list(map(int, input().split()))
#     nums = list(map(int, input().split()))
#     mx = -100000000000
#     mn = 100000000000
#     calc(0, nums[0], opers[0], opers[1], opers[2], opers[3])
#
#     ans = mx-mn
#     print("#%d %d" % (t, ans))