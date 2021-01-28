# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.


# [제약 사항]
# 문자열의 최대 길이는 200이다.


# [입력]
# 알파벳으로 이루어진 문자열이 주어진다.


# [출력]
# 각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.


# 입력
# ABCDEFGHIJKLMNOPQRSTUVWXYZ


# 출력
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26


# 알파벳을 숫자로 변환하는 문제. 아스키 코드에서 'A' = 65임을 이용하여 문제를 푼다.
# 알파벳으로 이루어진 문자열 전체를 한 str로 하여 받는다.
s = input()
# 이를 리스트로 변환해 각 알파벳이 한 요소를 이루는 리스트를 생성한다.
s_list = list(s)
# 각 요소인 알파벳들이 숫자로 변환되어 저장될 빈 리스트를 생성한다.
num_list = []
# 알파벳 리스트를 순회하며 알파벳의 아스키 코드 10진수 값에서 64를 뺀 값을 num_list에 추가한다.
for char in s_list:
    num_list.append(str(ord(char) - 64))

# num_list의 각 요소들 사이에 공백을 삽입하여 출력한다.
print(' '.join(num_list))


# 은교님 답안 .extend()를 활용하였다.
empty_list = []
empty_list.extend(s)
for i in range(len(empty_list)):
    print(f'{(ord(empty_list[i]) - 64)}' + " ", end='')
