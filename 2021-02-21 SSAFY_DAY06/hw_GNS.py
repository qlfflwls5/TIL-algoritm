# GNS
# 숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
# 예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.


# [입력]
# 입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
# 그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.
# 그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.


import sys


sys.stdin = open('GNS_test_input.txt')

# 1
# 카운팅 정렬을 사용하였다.
# 입력받은 문자들을 숫자로 바꿔주는 함수
def decrypt(str_num):
    for i in range(len(str_list)):
        if str_num == str_list[i]:
            return i


str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for t in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    num_list = list(map(decrypt, input().split()))
    result_list = list(num_list)
    cnt_list = [0]*10
    for i in range(N):
        cnt_list[num_list[i]] += 1

    for i in range(1, 10):
        cnt_list[i] += cnt_list[i-1]

    for i in range(N-1, -1, -1):
        result_list[cnt_list[num_list[i]]-1] = str_list[num_list[i]]
        cnt_list[num_list[i]] -= 1

    print('#%d\n%s' % (t, ' '.join(result_list)))

# 카운팅 정렬을 전부 실행하는 것이 아니라, 지금은 str_list가 주어져있으므로
# 카운트 리스트를 만들기만하고 이를 바로 활용할 수도 있겠다.
# result = ''
# for i in range(10):
#     result += (str_list[i] + ' ') * cnt_list[i]
# 즉, 카운팅 정렬을 stable하지 않게 하는 법인데, 여기는 str_list가 있어서 해도 문제가 없을 것 같다.


# str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# my_table = dict(zip(str_list, range(str_list))
# 이건 딕셔너리를 만드는 방법임 알아두면 좋다.