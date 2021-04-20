# String
# 주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.
# Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.
# 위 문장에서 ti 를 검색하면, 답은 4이다.


# [제약 사항]
# 총 10개의 테스트 케이스가 주어진다.
# 문장의 길이는 1000자를 넘어가지 않는다.
# 한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.
# 한 문장에서는 하나의 문자열만 검색한다.


# [입력]
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.


import sys


sys.stdin = open('String_input.txt', 'r', encoding='utf-8')

for t in range(1, 11):
    tc = int(input())
    # 패턴
    p = input()
    # 전체 텍스트
    T = input()
    # 패턴이 전체 텍스트에 나타나는 횟수
    cnt = 0

    # for문으로 푸는 법
    # 0 ~ 전체 텍스트 길이 - 패턴 길이의 인덱스마다 검사 실행
    # for i in range(len(T)-len(p)+1):
    #     # i번째에서 패턴의 첫 요소와 같다면
    #     if T[i] == p[0]:
    #         # i번째 이후도 같은지 확인
    #         for j in range(1, len(p)):
    #             # 다른 부분이 있다면 break후 다음 시행
    #             if T[i+j] != p[j]:
    #                 break
    #         # break에 걸리지 않고 검사가 끝났을 경우 cnt 1증가
    #         else:
    #             cnt += 1
    
    # while문으로 푸는 법
    # i는 T의 인덱스, j는 p의 인덱스
    i = 0 
    j = 0
    while i < len(T):
        if T[i] != p[j]:
            # 만약 패턴이 다르다면 패턴을 검색하기 시작했던 위치로 되돌아감
            i -= j
            # 만약 패턴이 다르다면 j를 반복문의 마지막에 0으로 맞출 수 있도록 1을 미리 빼줌
            j = -1
        # 만약 j가 패턴의 마지막 index와 같을 때까지 증가했다면 패턴이 존재하는 것. cnt를 늘리고 j는 다시 -1로 초기화한다.
        if j == len(p)-1:
            cnt += 1
            j = -1
        i += 1
        j += 1

    print('#%d %d' %(tc, cnt))


