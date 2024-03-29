# 아주 간단한 계산기
# 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.


# [제약 사항]
# 1. 두 개의 자연수 a, b는 1부터 9까지의 자연수이다. (1 ≤ a, b ≤ 9)
# 2. 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.
# 3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.


# [입력]
# 입력으로 두 개의 자연수 a, b가 빈 칸을 두고 주어진다.


# [출력]
# 사칙연산의 결과를 각 줄에 순서대로 출력한다.


# a와 b를 .split()을 사용하여 입력받은 문자열을 공백을 기준으로 나누고,
# map()을 사용하여 각 나누어진 문자에 대해 int()를 실행한다.
# 이를 tuple()을 통해 튜플로 만들어 a와 b에 저장한다.
a, b = tuple(map(int, input().split())) # 이거 tuple 안써도 됨!
print(a + b)
print(a - b)
print(a * b)
# 나누기 연산의 결과에서 소수점 이하는 버리기로 했으므로 정수 나눗셈을 사용한다.
print(a // b)