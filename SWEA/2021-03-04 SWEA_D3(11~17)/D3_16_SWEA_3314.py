# 보충학습과 평균
# 산골에 있는 삼성초등학교에는 학생이 다섯 명 밖에 없다.
# 어제는 수행평가였고 오늘 점수가 나왔다. 점수가 40점 이상인 학생은 그 점수를 그대로 가지지만 40점 미만은 학생은 보충학습을 받고 점수를 40점으로 올릴 수 있다.
# 보충학습은 거부가 불가능하기 때문에 40점 미만인 학생은 40점을 받게 되는 것과 같다.
# 이 때 학생 5명의 점수를 알 때 보충을 받을 학생이 모두 보충을 받고 나면 점수의 평균이 몇인지 출력하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스마다 다섯 개의 정수가 공백으로 구분되어 주어진다.
# 점수는 모두 0이상 100이하인 5의 배수이다. 즉 평균은 항상 정수이다.


# [출력]
# 각 테스트 케이스마다 학생 5명의 평균 점수를 출력한다.


# 1
# 람다를 써봤다
def bochoong(x):
    if x < 40:
        return 40
    return x

T = int(input())
for t in range(1, T+1):
    score_list = list(map(lambda x: bochoong(x), list(map(int, input().split()))))
    print('#%d %d' % (t, sum(score_list)//len(score_list)))


# 2
T = int(input())
for t in range(1, T+1):
    score_list = list(map(int, input().split()))
    for i in range(len(score_list)):
        if score_list[i] < 40:
            score_list[i] = 40
    print('#%d %d' % (t, sum(score_list)//len(score_list)))