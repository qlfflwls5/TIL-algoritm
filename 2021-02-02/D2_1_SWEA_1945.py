# 숫자 N은 아래와 같다.
# N=2**a x 3**b x 5**c x 7**d x 11**e
# N이 주어질 때 a, b, c, d, e 를 출력하라.


# [제약 사항]
# N은 2 이상 10,000,000 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 입력
# 10  
# 6791400
# 1646400
# 1425600
# 8575
# 185625
# 6480
# 1185408
# 6561
# 25
# 330750


# 출력
# #1 3 2 2 3 1
# #2 6 1 2 3 0
# #3 6 4 2 0 1
# #4 0 0 2 3 0
# #5 0 3 4 0 1
# #6 4 4 1 0 0
# #7 7 3 0 3 0
# #8 0 8 0 0 0
# #9 0 0 2 0 0
# #10 1 3 3 2 0


# 딕셔너리를 통해 key들을 2, 3, 5, 7, 11로 하여 for문을 돌리면서 각각의 값이 되는 a, b, c, d, e를 구하는 것이 좋을 것 같다.
T = int(input())
for i in range(1, T + 1):
    n = int(input())
    # 각 키에 대한 값은 0으로 초기화하고, 각 키들을 꺼내 n을 키로 나눈 나머지가 0이 아닐 때까지 반복. 반복 시마다 키의 값을 1씩 늘린다.
    num_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    for key in num_dict:
        while n % key == 0:
            n //= key
            num_dict[key] += 1

    # 결과 출력
    print(f'#{i} {num_dict[2]} {num_dict[3]} {num_dict[5]} {num_dict[7]} {num_dict[11]}')


# 실행시간과 메모리는 하나하나 계산하는 것이 훨씬 효율적이다.
# while n % 2 == 0:
#   two += 1
#   n //= 2 