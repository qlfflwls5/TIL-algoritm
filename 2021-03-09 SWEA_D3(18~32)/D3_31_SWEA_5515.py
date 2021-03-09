# 2016년 요일 맞추기
# 2016년 1월 1일은 금요일이었고, 문득 송송이는 특정 날짜의 요일을 맞추고 싶어졌다.
# 2016년은 윤년이기 때문에 2월 29일이 포함된다. 2016년 m월 d일은 무슨 요일인지 맞추는 프로그램을 작성하시오.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 m,d가 공백으로 구분되어 주어진다.
# m,d는 2016년 m월 d일을 정상적으로 나타낼 수 있는 두 정수이다.


# [출력]
# 각 테스트 케이스마다 2016년 m월 d일이 월요일이면 0, 화요일이면 1, 수요일이면 2, 목요일이면 3, 금요일이면 4, 토요일이면 5, 일요일이면 6을 출력한다.

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for i in range(1, 12):
    month[i] += month[i-1]

T = int(input())
for t in range(1, T+1):
    m, d = map(int, input().split())
    result = (month[m-1]+d-1+4) % 7
    print('#%d %d' % (t, result))