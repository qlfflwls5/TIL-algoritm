# 글자수
# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
# 예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
# 파이썬의 경우 딕셔너리를 이용할 수 있다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 0
# live에서 풀이한 모범 답안
T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    cnt_list = [0] * len(str1)

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt_list[i] += 1

    ans = 0
    for cnt in cnt_list:
        if ans < cnt:
            ans = cnt

    print(ans)


# 1
# 내 코드, 메소드 안쓰고 풀기
T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    # A~Z까지의 개수를 담을 길이 26의 카운트 리스트 생성
    cnt_list = [0]*26
    for char in str2:
        # str2에서 알파벳 하나씩을 가져와 ord()를 이용해 cnt_list의 0번째는 'A'의 개수, 25번째는 'Z'의 개수를 담기
        cnt_list[ord(char)-65] += 1

    max_cnt = 0
    for char in str1:
        # str1에서 알파벳 하나씩을 가져와 ord()를 이용해 cnt_list에 해당 알파벳이 몇 번 등장했는지를 알고 최대값 비교하기
        if cnt_list[ord(char)-65] > max_cnt:
            max_cnt = cnt_list[ord(char)-65]

    print('#%d %d' %(t, max_cnt))


# 2
# dict 사용법
# dict.fromkeys(seq, val) 을 하면 seq의 각 요소를 키로하여 val을 값으로 담는다. 카운트 리스트를 선택적으로 초기화해 만들 때 좋다.
T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    N, M = len(str1), len(str2)
    cnt_dict = dict.fromkeys(str1, 0)

    for char in str2:
        if char in cnt_dict.keys():
            cnt_dict[char] += 1

    print('#%d %d' %(t, max(cnt_dict.values())))


# 3
# count 메소드 사용법
T = int(input())
for t in range(1, T+1):
    str1, str2 = input(), input()
    cnt_list = [str2.count(char) for char in str1]
    print('#%s %s' % (t, max(cnt_list)))